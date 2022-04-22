from fileinput import filename
from hpyml import hpyml,block

pyml = hpyml(filename="susindex",css_name="sustyle")



main = block(pyml)
main.open(class_="my_class",block="div",text="sus")
main.exit()
pyml.end()

pyml.css({
    "body" : {"background" : "rgb(0,0,0,0.4)"},
    ".my_class" : {"background" : "rgb(0,0,0,0.6)","border-radius" : "15px","padding" : "15px","margin" : "15px","text-align" : "center", "color" : "rgb(255,255,255)","font-size" : "25px"} 
})

