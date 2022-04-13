from hpyml import hpyml
#read examp1
#прочитайте examp1


#give names for files | filename - html, css_name - css
#раздача имен файлам | filename - html, css_name - css
pyml = hpyml(filename="textfile", css_name = "designfile")





main = pyml.block(pyml)
type_button = pyml.block(pyml)
button = pyml.block(pyml)
footer = pyml.block(pyml)
small = pyml.block(pyml)
a = pyml.block(pyml)
space = pyml.block(pyml)

main.open("div",class_="main")
pyml.html_text({"h2" : "Why hpyml is good?","h6": "IDK, lol"})
type_button.open(block="p",class_="button")

#                             атрибуты стоит помещать в '', их значения в ""
#                             attributes should be put in '', their values ​​in ""
#                              ↓attr       ↓val↓      attr↓
button.open(block="a",attrs = 'href = "http://www.yandex.ru"',text="link to yandex!")
button.exit()
type_button.exit()
main.exit()

space.open(block="br")


footer.open(block="div",class_="footer")
small.open(block="small")
a.open(block="a",text="Contact us!",attrs = 'href = "https://www.youtube.com/"')

a.exit()
small.exit()
footer.exit()



pyml.end()

#CSS!!!
pyml.css({
    "body" : {"background" : "rgb(0,0,0,0.6)"}
})

pyml.css({
    ".main" : {
    "text-align" : "center",
    "background" : "rgb(0,0,0,0.7)",
    "border-radius":"15px",
    "color" : "rgb(255,255,255,0.8)",
    "padding" : "15px",
    "margin" : "15px",
    "box-shadow" : "0px 0px 5px 5px rgb(0,0,0,0.8)",
    "text-decoration" : "none"}
})

pyml.css({
    ".main:hover" : {
    "color" : "rgb(155,155,0)",
    "text-align" : "center",
    "text-shadow" : " 0px 0px 15px rgb(0,0,0)"}
})

pyml.css({
    ".footer" : {
    "text-align" : "center",
    "background" : "rgb(0,0,0,0.7)",
    "border-radius":"15px",
    "padding" : "10px",
    "margin" : "10px",
    "box-shadow" : "0px 0px 5px 5px rgb(0,0,0,0.8)"
    }
})



