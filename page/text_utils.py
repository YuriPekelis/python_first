class TextUtils:

    def extract_price_from_text(text):
        return float(text.replace("$", "")
                     .replace(",", "")
                     .replace("US", ""))
