"""prepro"""
def main():
    """hello"""
    grade = float(input())
    if grade >= 2:
        print("I'm so happy.")
    elif grade < 1:
        print("I'm so sad.")
    else:
        print("%.2f" %(4.00 - grade))
main()
