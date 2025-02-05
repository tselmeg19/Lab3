hicheel1 = input("Хичээл 1-ийн нэр: ")
hicheel2 = input("Хичээл 2-ийн нэр: ")

index = int(input("Хичээл 1-ийн нэрэнд Хичээл 2-ын ямар дугаарт байгаа үсгийг хайх вэ?: "))

if 0 <= index < len(hicheel2):  
    search_char = hicheel2[index]
    found_index = hicheel1.find(search_char) 
    print(f"{index} дугаар дахь '{search_char}' үсэг хичээл 1-ийн нэрэнд {found_index} дугаарт дээр олдлоо.")
else:
    print(f"{index} дугаар дахь үсэг хичээл 1-ийн нэрэнд -1 дугаарт дээр олдлоо.")
