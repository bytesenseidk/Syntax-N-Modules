import goslate


def translator(sentance, language="en"):
    return goslate.Goslate().translate(sentance, language)
    

if __name__ == "__main__":
    translation = translator("Follow bytesenseidk on Instagram!", "hi")
    print(translation)

