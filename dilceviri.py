from googletrans import Translator

def translate_text(text, target_language):
    translator = Translator()
    translated_text = translator.translate(text, dest=target_language)
    return translated_text.text

def main():
    print("Dil Çeviri Programına Hoş Geldiniz!")
    source_text = input("Çevrilecek metni girin: ")
    target_language = input("Hedef dil kodunu girin (örn. 'en' for English): ")

    translated_text = translate_text(source_text, target_language)
    print(f"Çevrilen metin: {translated_text}")

if __name__ == "__main__":
    main()
