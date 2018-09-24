__author__ = 'Bryan Cairns'

# Error handling
# KISS - Keep it simple / stupid

def doSomething(number):
    try:
        x = 5
        y = x / number
        print(y)
    except OSError:
        print("OS Error")
    except ZeroDivisionError:
        print("Please do not div by zero")

    except Exception as e:
        print("Something went boom: %s" % e)

    finally:
        print("Finally I get to run")

print("Starting Program")
doSomething(0)
print("Ending Program")