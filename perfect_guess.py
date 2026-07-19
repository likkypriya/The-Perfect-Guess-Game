import random 

print("🎯 Welcome to Perfect Guess Game!")
print("Choose difficulty level:")
print("1. Easy (1-50)")
print("2. Medium (1-100)")
print("3. Hard (1-200)")

choice=int(input("Enter choice (1/2/3): "))
if choice==1:
    n=random.randint(1,50)
    max_range=50
elif choice==2:
    n=random.randint(1,100)
    max_range=100
else:
    n=random.randint(1,200)
    max_range=200

a=-1
guesses=0

while(a!=n):
    guesses+=1
    a=int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
    elif(a<n):
        print("Higher number please")

score=max_range//guesses
print(f"You have guessed the number {n} correctly in {guesses} attempts")
print(f"Your score: {score}")