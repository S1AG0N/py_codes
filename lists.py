pp = (["vee","phil"])
new = input("who is the new guy in town: ")
print(f"wow welcome {new}. So now we are three:")
more_new = input("we have anyone else?:")

pp.extend([new,more_new])
for name in pp:
    print(name)
print(f"so the last one is {pp[len(pp)-1]}")
