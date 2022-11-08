def generator():
    yield "H"
    yield "E"
    yield "L"
    yield "L"
    yield "O"

test = generator()
for i in test:
    print(i)