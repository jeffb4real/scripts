# This is a shell script

# cat ipadd.txt | grep -e /\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b/

echo
echo 1-------------
echo

grep -e '(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)' ipadd.txt
# echo $1:$2:$3:$4

echo
echo 2-------------
echo

grep -E '([0-9]{1,3}\.)([0-9]{1,3}\.)([0-9]{1,3}\.)([0-9]{1,3})' ipadd.txt >nul
echo $_1:$2:$3:$4 

echo
echo 3-------------
echo

grep -E '([0-9]{1,3}\.){3}[0-9]{1,3}' ipadd.txt
