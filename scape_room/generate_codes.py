import random
with open('index.html', 'r') as template:
    sample_template = template.read()
    paths = [
    "A1", "A2", "A3", "A4", "A5",
    "B1", "B2", "B3", "B4", "B5",
    "C1", "C2", "C3", "C4", "C5",
    "D1", "D2", "D3", "D4", "D5",
    "F1", "F2", "F3", "F4", "F5",
    ]
    keys = "1234567890ABCD*#"
    for path in paths:
        code = ""
        for i in range(8):
            code = code + random.choice(keys)
        final = sample_template.replace("code", code)
        with open(path+".html", 'w') as file:
            file.write(final)

