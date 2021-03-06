#MODULE FILE



from os import path




class hpyml:





		
    def __init__(self,title="",filename="index",css_name="styles"):

        self.main = path.abspath(path.dirname(__file__))

        self.link_to_html = f"{self.main}\{filename}"
        self.link_to_css = f"{self.main}\{css_name}"




			
        
        with open(f"{self.link_to_html}.html","w+") as f:
            code = f"""
<!DOCTYPE html>
<html>

<head>
	<meta charset="UTF-8">
	<title>{title}</title>
	<link rel="stylesheet" href="{self.link_to_css}.css">		
</head>

<body>
				

				"""
            f.write(code)
            f.close()
				
        with open(f"{self.link_to_css}.css","w+") as f:

            f.close()
            
        	
        
            

				
    def end(self):

        with open(f"{self.link_to_html}.html","a") as f:



            f.write("</body>")
            f.write("\n")
            f.write("</html>")
    def css(self,params_css=None):
				

        with open(f"{self.link_to_css}.css","a") as f:


            
            for obj in params_css:
                l = params_css.get(obj)
                f.write("\n")
                f.write(obj + "{")
                f.write("\n")
				    
                for sel_n in l:

                    sel_val = l[sel_n]

                    f.write(f"{sel_n} : {sel_val}; ")
                    f.write("\n")

                f.write("}")
			
            f.close()



    def html_text(self,params_html=None,class_=None):

        with open(f"{self.link_to_html}.html","a") as f:

            for obj in params_html:

                text = params_html.get(obj)

                if class_ is None:
                    code = f"<{obj}>{text}</{obj}>"
                else:
                    code = f'<{obj} class = "{class_}">{text}</{obj}>'

                f.write(code)
                f.write("\n")
                
            f.close()




class block:
    is_open = 0
    filename = "index"
    pyml = ""
	
	
	

    def __init__(self,pyml):
		
        self.filename = pyml.link_to_html

    def open(self,block="div",class_=None,attrs = "",text=""):
        with open(f"{self.filename}.html","a") as f:

            if self.is_open == 1:
                return "BlockError"


            if class_ is None:
                code = f"<{block} {attrs}>{text}"

            else:
                code = f'<{block} {attrs} class = "{class_}">{text}'

            self.name = block


            f.write(code)
            f.write("\n")
            self.is_open = 1
            f.close()

                
    def exit(self):
        with open(f"{self.filename}.html","a") as f :
            f.write(f"</{self.name}>")
            f.write("\n")
            f.close()





					
						
					
			
		
		