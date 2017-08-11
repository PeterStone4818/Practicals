def main():
    score = float(input("Enter score: "))
    if score < 0:
        print("Invalid Score")
    elif score > 100:
        print("Invalid score")
    else:
        result = score_catagory(score)
    print (result)


def score_catagory(score):
    if score > 90:
        result = ("Awesome")
    elif score >= 50:
        result = ("Passable")
    else:
        result = ("Bad")
    return result


main()
