# The loop's else branch is always executed once, regardless of whether the loop has entered its body or not.
i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("else",i)

# Modify the above program a bit so that the loop has no chance to execute its body even once:
i = 5
while i < 5:  #here loop does not enter it's the body
    print(i)
    i += 1
else:
    print("else", i)