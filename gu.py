def count_characters(s):
    counts = {}
    for char in s:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

text = input("请输入一个字符串：")
result = count_characters(text)
for char, count in result.items():
    print(char, "出现了", count, "次")
