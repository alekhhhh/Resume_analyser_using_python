import PyPDF2
filename = input("Enter the file name(With .pdf extension): ")
with open(filename , "rb") as file:
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
      text += page.extract_text()
print("\n--- Extracted Text (first 500 characters) ---\n")
print(text[:500])
