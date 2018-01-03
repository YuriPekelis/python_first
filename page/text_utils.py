class TextUtils:
    def extract_price_from_text(text):
        text = str(text).replace("$", "")
        text = str(text).replace(",", "")
        return float (text)