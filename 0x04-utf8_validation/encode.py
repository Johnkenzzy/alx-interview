text = "Hello € 😀"
utf8_encoded = text.encode('utf-8')

print(utf8_encoded)  # Output: b'Hello \xe2\x82\xac \xf0\x9f\x98\x80'
