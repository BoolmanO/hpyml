
from hpyml import hpyml

#старт, создание переменной для hpyml, обязателен
<<<<<<< HEAD
#принимает аргументы title,filename(название html файла),css_name(название css файла)
#название вводится без расширения

#takes arguments title,filename(html file name),css_name(css file name)
#name is entered without extension
#start, creating a variable for hpyml, required

pyml = hpyml()



=======
#start, creating a variable for hpyml, required
pyml = hpyml()

#метод start принимает аргументы title,filename(название html файла),css_name(название css файла)
#название вводится без расширения

#start method takes arguments title,filename(html file name),css_name(css file name)
#name is entered without extension

pyml.start()
>>>>>>> 034f52f699c77184547e95ff969aa370a6222d7b


#создание переменной для блока1 #creating a variable for block1
#creating a variable for block1
block1 = pyml.block(pyml)



#метод open принимает в себе такие параметры как block(тег) div или p (<> не нужен), class_ класс объекта, attrs атрибуты, text текст
#по умолчанию div,None,"","" (то есть пустота и тег див)

#open method accepts such parameters as block(tag) div or p (<> not needed), class_ object class, attrs attributes, text text
#default div,None,"","" (i.e. empty and div tag)

block1.open(class_="main",text="Example text!")



#простое массовое создание тега и текста в нем
#simple mass creation of a tag and text in it
#                 tag      text         тег      текст
<<<<<<< HEAD
pyml.html_text({ "p" : "2nd example", "h2" : "34th example" })
=======
pyml.html_text({ "p" : "2nd example", "h2" : "3th example" })
>>>>>>> 034f52f699c77184547e95ff969aa370a6222d7b


#закрытие тега, не принимает параметров
#closing tag, takes no parameters
block1.exit()

#время для CSS!
#time for CSS!


#метод css принимает аргументы в виде словаря {.class или просто tag : {cвойство : параметр свойства,свойство : параметр свойства}}
#css method accepts dictionary arguments {.class simply or tag : {property : parameter,property : property parameter}}

params_main = {
"text-align" : "center",
"padding" : "15px",
"margin" : "15px",
"background" : "rgb(0,0,0,0.6)",
"border-radius" : "15px",
"color" : "rgb(255,255,255,0.8)"
}

params_body = {
    "background" : "rgb(0,0,0,0.4)"
}
pyml.css( {".main": params_main, "body" : params_body} )

#это равносильно pyml.css({"body" : params_body}) и pyml.css({".main" : params_main})
#this is equivalent to pyml.css({"body" : params_body}) and pyml.css({".main" : params_main})


#обязательное закрытие html документа!
#obligatory closing of the html document!
pyml.end()


