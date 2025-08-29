count=0
filename = input("Enter the file name(Ending with .txt )")
with open(filename,"r") as file:
    skills = file.read().lower()
skills_to_check = ["python", "java","html","css","c","c++"]

for skill in skills_to_check:
    if skill in skills:
        count +=1
        print(f"✌️ {skill.upper()} FOUND!! ")
    else:
          print(f"😦 {skill.upper()} NOT FOUND!! ")

print("TOTAL SKILLS MATCHED : ",count ," out of 5")
