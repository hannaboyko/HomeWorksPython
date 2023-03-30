def domains(list1, list2):
    rnd = rand.randrange(100, 999)
    name = list1[rand.randint(0, len(list1) - 1)]
    domain = list2[rand.randint(0, len(list2) - 1)]
    s = ''.join(rand.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    result = f"{name}.{rnd}@{s}.{domain}"
    return result

list1 = ["king", "miller", "kean"]
list2 = ["net", "com", "ua"]
result = domains(list1, list2)
print(result)
