import time

def main():
    response = ""
    good_answers = ["yes", "sure", "fine", "ok"]
    while response  != "yes":
        response = input("Will you be my friend?")
        response = response.lower()
    print("Horaaay")
    for number in range(10):
        print("Hooray, we will play forever, and ever, and ever")
        time.sleep(1)



main()