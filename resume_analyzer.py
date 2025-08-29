import PyPDF2
filename = input("Enter file name: ")
if filename.endswith(".pdf"):
    with open(filename , "rb") as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    text = text.lower()
    skills_to_check = ["python","java","html","css","c","c++","sql"]
    count = 0
    for skill in skills_to_check:
        if skill in text:
            count += 1
            print(f"✌️ {skill.upper()} FOUND!!")
        else:
            print(f"😒 {skill.upper()} NOT FOUND!!")
    print("\nTOTAL SKILLS MATCHED:", count, "out of", len(skills_to_check))

elif filename.endswith(".txt"):
  count=0
  with open(filename,"r") as file:
    skills = file.read().lower()
  skills_to_check = ["python", "java","html","css","c","c++"]
  for skill in skills_to_check:
    if skill in skills:
        count +=1
        print(f"✌️ {skill.upper()} FOUND!! ")
    else:
        print(f"😦 {skill.upper()} NOT FOUND!! ")
  print("TOTAL SKILLS MATCHED : ", count ," out of", len(skills_to_check))
else:
  print("UNSUPPORTED FILETYPE")
