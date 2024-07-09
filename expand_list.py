
def enclose(all_target=[ 1,[2,[3]] ]):
    res = []
    def main_func(target):
        for item in target:
            if type(item) != list:
                res.append(item)
            else:
                main_func(item)
    main_func(all_target)
    return res

print(enclose())