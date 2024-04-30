#age=19
#NAME="Gaurav kumar"

def myadd(num,d):
    return (num+d)
def mysub(num,d):
    return (num-d)
def main():
    while True:
        print("1.Addition")
        print("2.Substruction")
        print("9.exit")
        ch=int(input("enter the choice number"))
        if ch==9:
                break
        elif ch>=1 and ch<=2:
            a=int(input("ente the first number"))
            b=int(input("ente the second number"))
            if ch==1:
                print("sum:",myadd(a,b))
            elif ch==2:
                print("Difference:",mysub(a,b))
        else:
            print("Invalid choice")




main()       
print("Addition",myadd(78,65))
print("Subtruction",mysub(78,65))
