import easyocr

reader = easyocr.Reader(['en'])


def extract_text():
    try:
        result = reader.readtext('chinese.jpg')
        print(result)
    except Exception as error:
        print(error)
