from QandA import dataset

with open("questions.py", "w") as f:
    f.write("questions = [")
    for q, a in dataset:
        f.write(f"\"\"\"{q}\"\"\",\n")
    f.write("]")
    
    f.write("answers = [")
    for q, a in dataset:
        f.write(f"\"\"\"{a}\"\"\",\n")
    f.write("]")