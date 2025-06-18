# Python 3.6 - Formatted string literals

def demo():
    track = "Perfect"
    artist = "Ed Sheeran"
    album = "divide"
    download = 1276738
    print(f"track name = {track}, artist = {artist}, download = {download:,}")  # string interpolation
    print("track name = {}, artist = {}".format(track, artist))


if __name__ == '__main__':
    demo()


'''---------------------------------------------------------------------------------------------------'''   

text = "   hello World 123   "

print(text.isalpha())  # False  (มีช่องว่าง + เลข)

print(text.isdigit())  # False

print(text.find("World"))  # 9  (ถ้านับช่องว่างด้วย)

print(text.lower())  # "   hello world 123   "
print(text.upper())  # "   HELLO WORLD 123   "

print(text.strip())  # "hello World 123"

print(text.replace("World", "Python"))  # "   hello Python 123   "

print(text.strip().split())  # ['hello', 'World', '123']

words = text.strip().split()  # ['hello', 'World', '123']
print(" | ".join(words))  # "hello | World | 123"

print(text.strip().capitalize())  # "Hello world 123"
print(text.strip().title())  # "Hello World 123"

name = "hello World 123"
print("Text is: {}".format(name))  # "Text is: hello World 123"