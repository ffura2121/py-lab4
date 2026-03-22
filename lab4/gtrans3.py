from modules import mod_gtrans3 as m

text = "Hello world"
print(m.TransLate(text, "auto", "uk"))
print(m.LangDetect(text))
print(m.CodeLang("en"))