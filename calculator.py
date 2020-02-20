vars_ = dict()
while True:
    a_b = input()
    if a_b == "":
        continue
    elif a_b == "/exit":
        print("Bye!")
        break
    elif a_b == '/help':
        print("basic calculator")
    else:
        try:
            print(eval(a_b))
        except SyntaxError:
            if a_b.startswith("/"):
                print("Unknown command")
            else:

                sub = a_b[:a_b.find("=")].strip()
                val = a_b[a_b.find("=") + 1:].strip()
                bools = True
                if a_b.count("=") > 1 :
                    bools = False
                    print("Invalid assignment")
                else:
                    for i in val:
                        if ord(i) > 58 and i not in vars_:
                            bools = False
                            print("Invalid assignment")
                            break
                    for i in sub:
                        if ord(i) < 57:
                            bools = False
                            print("Invalid identifier")
                            break
                        else:
                            bools = True
                if len(vars_) == 0 and bools:
                    vars_ = {sub: val}
                elif bools:
                    vars_[sub] = val
        except NameError:
            sub2 = a_b.split()
            counter = []
            for i in sub2:
                if i in vars_:
                    counter.append(vars_[i])
                elif i in '+-*/1234567890':
                    counter.append(i)

                else:
                    print("Unknown variable")
                    break
            else:
                try:
                    print(eval("".join(counter)))
                except NameError:
                    for i in counter:
                        if i in vars_:
                            ind = counter.index(i)
                            del counter[ind]
                            counter.insert(ind, vars_[i])

                    print(eval("".join(counter)))
