'''
Script para escalar uniformemente las diferentes fotos de los sensores de Milesight IoT manteniendo
el radio de aspecto fijo y garantizar que todas las imagenes tengan el mismo ancho.
'''
from PIL import Image

def scale_image(image_path, base_width):
    # Abre la imagen desde la ruta especificada
    image = Image.open(image_path)
    
    # Calcula el porcentaje de la base deseada respecto al ancho original
    w_percent = (base_width / float(image.size[0]))
    
    # Calcula la nueva altura manteniendo el radio de aspecto
    h_size = int((float(image.size[1]) * float(w_percent)))
    
    # Redimensiona la imagen
    scaled_image = image.resize((base_width, h_size), Image.Resampling.LANCZOS)
    
    return scaled_image

# Ruta de la imagen a escalar
image_path1 = 'GS301.png'
image_path2 = 'VS121.png'

# Anchura deseada para todas las imágenes
base_width = 500

# Escala la imagen y muestra el resultado
scaled_img1 = scale_image(image_path1, base_width)
scaled_img2 = scale_image(image_path2, base_width)
#scaled_img1.show()

# Guarda la imagen escalada
scaled_img1.save('GS301_WidthScale.png')
scaled_img2.save('VS121_WidthScale.png')
