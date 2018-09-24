require 'fileutils'
require 'sqlite3'
require 'uri'
require 'net/http'
require 'set'
require 'thread'

# https://news.ycombinator.com/item?id=13721452 
# I wrote this(1) script to check for any affected sites from local Chrome history. It checks for the header `cf-ray` in the response headers from the domain.
# It is not an exhaustive list but I was able to find few important ones like my bank site.
# https://gist.github.com/kamaljoshi/2cce5f6d35cd28de8f6dbb27d586f064

chrome_history_location = "#{ENV['HOME']}/Library/Application\ Support/Google/Chrome/Default/History"
temp_location = "/tmp/Chrome_history"
FileUtils.cp(chrome_history_location, temp_location)

sqlite_db = SQLite3::Database.new temp_location
chrome_history = sqlite_db.execute('SELECT DISTINCT(url) FROM urls;').flatten; nil
domain_set = Set.new
cloudflare_set = Set.new
query_uris = Array.new

chrome_history.each do |url|
  host = URI.parse(url).host rescue nil
  query_uris += [URI::HTTPS.build({host: host}), URI::HTTP.build({host: host})] if !domain_set.include?(host) && !host.nil?
  domain_set.add(host)
end; nil

uri_mutex, set_mutex, read_mutex = Mutex.new, Mutex.new, Mutex.new
(1..16).map do
  Thread.new(query_uris, cloudflare_set) do |query_uris, cloudflare_set|
    while !(uri = uri_mutex.synchronize { query_uris.pop }).nil?
      cf_header_present = !Net::HTTP.get_response(uri)['cf-ray'].nil? rescue nil
      read_mutex.synchronize{ print("#{query_uris.length} remaining\r") }
      set_mutex.synchronize { cloudflare_set.add(uri.host) } if cf_header_present
    end
  end
end.each(&:join); nil

FileUtils.rm([temp_location])

#p cloudflare_set.to_a.sort
cloudflare_set.each do |el|
    puts el
end
