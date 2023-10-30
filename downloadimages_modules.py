"""
Este archivo contiene algunos modulos creados con el fin de descargar imagenes del internet.
Fue programado teniendo en mente su utilización en aplicaciones de IA.

Author: Patrick Vásquez <pvasquezs@fen.uchile.cl>
Date: 30/10/2023
"""

from abc import ABC, abstractmethod

class ImageDownloader(ABC):
    @abstractmethod
    def download_first_image(self):
        pass

class BingImageDownloader(ImageDownloader):
    def __init__(self, query):
        self.query = query

    def download_first_image(self):
        """
        Descarga la primera imagen de la consulta utilizando la biblioteca bing_image_downloader.
        
        Args:
        self (objeto): objeto de la clase DownloadImages.
        
        Returns:
        str: la ruta de la imagen descargada.
        """
        from bing_image_downloader.downloader import download
        download(self.query, limit=1,  output_dir='dataset', adult_filter_off=True, force_replace=False, timeout=60, verbose=True)
        return "dataset/Image_1.jpg"

class DeleteImageDirectory():
    def __init__(self, directory="./dataset/"):
        self.directory = directory

    def delete_directory(self):
            """
            Elimina el directorio especificado en la variable de instancia `directory`.
            Si el directorio existe, se eliminan todas las imágenes contenidas en él y luego se elimina el directorio.
            Si el directorio no existe, se imprime un mensaje indicando que el directorio no existe.
            """
            import shutil
            if os.path.exists(self.directory):
                shutil.rmtree(self.directory)
                print(f"Las imagenes existen y han sido eliminadas.")
            else:
                print(f"El directorio {self.directory } no existe.")

# Example usage:
if __name__ == "__main__":
    image_path = BingImageDownloader.download_first_image("cute puppies")
    print("Image downloaded to:", image_path)
