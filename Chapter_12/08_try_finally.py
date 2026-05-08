def main():
    try:
        a = int(input("Hey, Enter a number: "))
        print(a)
        return

    except Exception as e:
        print(e)
        return

    finally:
        print("I am inside finally") # always runs but used in functions for definitly run cause without finally the orint wont print here cause of return
        

main()