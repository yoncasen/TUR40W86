meme_dictionary = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }


word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!): ")


if word in meme_dictionary.keys():
    # Kelime eşleşiyorsa ne yapmalıyız?
    meaning = meme_dictionary[word]
    print("Anlamı:", meaning)
else:
    # Kelime eşleşmiyorsa ne yapmalıyız?
    print("Maalesef sözlükte bu kelime yok.") 
