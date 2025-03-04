import pandas

nato_read = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_data = pandas.DataFrame(nato_read)

# for (index,rows) in nato_data.iterrows():
#     print(rows.code)


print("Welcome to NATO Alphabet: ")
out = {}
user_in = input("Enter A Word: ").upper()
for c in user_in:
    for (index, rows) in nato_data.iterrows():
        if rows.code[0] == c:
            out[c] = rows.code
print(out)
