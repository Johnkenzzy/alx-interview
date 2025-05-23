text = "Hello € 😀"
utf8_encoded = text.encode('utf-8')
decoded_text = utf8_encoded.decode('utf-8')

print(decoded_text)  # Output: Hello € 😀
