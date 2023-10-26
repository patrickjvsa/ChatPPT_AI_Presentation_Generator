"""
Este archivo contiene algunos modulos creados con el fin de trabajar con archivos pptx.
Fue programado teniendo en mente su utilización en aplicaciones de IA.

Author: Patrick Vásquez <pvasquezs@fen.uchile.cl>
Date: 26/10/2023
"""

class Presentation():
    def __init__(self, title, author, template = "./templates/template.pptx"):
        from pptx import Presentation
        self.title = title
        self.author = author
        self.template = template
        self.presentation = Presentation(template)

    def add_frontpage(self):
        """
        Añade una diapositiva de portada a la presentación con el título y autor especificados.

        Args:
        - titulo (str): El título de la presentación.
        - autor (str): El autor de la presentación.

        Returns:
        - None
        """
        from pptx import Presentation
        slide_layout = self.presentation.slide_layouts[0]  
        slide = self.presentation.slides.add_slide(slide_layout)
        content_placeholder = slide.placeholders[0]
        content_placeholder.text = f"{self.title}"
        content_placeholder = slide.placeholders[1]
        content_placeholder.text = f"{self.author}"

    def add_index(self, indice):
        """
        Añade un índice a la presentación.

        Args:
        - indice (str): El índice a agregar.

        Returns:
        - None
        """
        from pptx import Presentation
        slide_layout = self.presentation.slide_layouts[1]  
        slide = self.presentation.slides.add_slide(slide_layout)
        content_placeholder = slide.placeholders[0]
        content_placeholder.text = "Indice"
        content_placeholder = slide.placeholders[1]
        content_placeholder.text = f"{indice}"

    def save_presentation(self, name="my_presentation.pptx"):
        """
        Guarda la presentación actual en un archivo con el nombre especificado.
        
        Args:
        - name (str): El nombre del archivo de la presentación. Por defecto es "my_presentation.pptx".
        Returns:
        - None
        """
        from pptx import Presentation
        self.presentation.save("./output/" + name)
        # cuando exista la webapp, hay que mover ese decorador output del modulo al archivo app.py

    def create_photo_slide_cat(self):
        """
        Crea una diapositiva con una foto de un gato.

        Args:
        - None

        Returns:
        - None
        """
        from pptx import Presentation
        from pptx.util import Inches
        slide_layout = self.presentation.slide_layouts[3]  
        slide = self.presentation.slides.add_slide(slide_layout)
        content_placeholder = slide.placeholders[0]
        content_placeholder.text = "Foto de gato"
        # Agrega una imagen a la diapositiva
        left = Inches(2)  # Ajusta la posición izquierda de la imagen
        top = Inches(3)   # Ajusta la posición superior de la imagen
        width = Inches(4) # Ajusta el ancho de la imagen
        height = Inches(3) # Ajusta la altura de la imagen
        image_path = "./photos/cat.jpg"  # Ruta a la imagen que deseas agregar
        pic = slide.shapes.add_picture(image_path, left, top, width, height)

        # Es necesario borrar las imagenes que se descarguen

def main():
    print("Ejecutando programa principal...")
    presentation = Presentation("Título", "Autor")
    print("Plantilla cargada con éxito.")
    presentation.add_frontpage()
    print("Portada agregada con éxito.")
    presentation.add_index("Índice")
    print("Índice agregado con éxito.")
    presentation.create_photo_slide_cat()
    print("Gato agregado con éxito.")
    presentation.save_presentation("my_presentation.pptx")
    print("Presentación guardada con éxito.")

if __name__ == "__main__":
    main()

