# python can be used to perform opertations on files
# read(), write(), readlines(), close() , seek(), delete() , create()

""" Type so all Files

1. Text Files: .txt, .docx, .py, .log etc.
2. Image Files: .jpg, .png, .gif, .bmp, .svg etc.
3. Audio Files: .mp3, .wav, .ogg, .flac etc.
4. Video Files: .mp4, .avi, .mov, .mkv etc.
5. Executable Files / Software Files: .exe, .msi, .bat, .sh etc.
6. Database Files: .db, .sqlite, .csv, .json etc.
7. Compressed Files: .zip, .tar, .gz, .bz2 etc.
8. Web Files: .html, .css, .js, .php etc.
9. Executable Files / Software Files: .exe, .msi, .bat, .sh etc.
10. Data Files: .csv, .json, .xml, .yaml etc.
11. Presentation Files: .ppt, .pptx, .odp etc.
12. Spreadsheet Files: .xls, .xlsx, .ods etc.
13. Document Files: .doc, .docx, .odt etc.
14. Database Files: .db, .sqlite, .csv, .json etc.
15. Compressed Files: .zip, .tar, .gz, .bz2 etc.
16. Web Files: .html, .css, .js, .php etc.


Binar Files : .mp4, .mp3, .jpg, .png etc.
"""

# open() : we have to open a file before reading or writing.
# f = open ("filename", "mode")
# it returns a file object
# types of mode : r, w, a, r+, w+, a+ , x, x+, b, t, t+, b+, rb, wb, ab, rb+, wb+, ab+
# r : read mode , open for reading(default)
# w : write mode , open for writting, truncating the file first
# a : append mode
# r+ : read and write mode
# w+ : write and read mode
# a+ : append and read mode
# x : create mode , create n new file and open it for writtng
# x+ : create and read mode
# b : binary mode
# t : text mode, default  
# t+ : text and read mode 
# b+ : binary and read mode

f = open("test.txt", "r")
data = f.read()
# line1 = f.readline()
# line2 = f.readlines()

print("full data", data)
# print(line1)
# print(line2)
print(type(f))


f.close()

