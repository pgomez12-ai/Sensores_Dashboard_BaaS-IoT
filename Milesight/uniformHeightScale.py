'''
Script para escalar uniformemente las diferentes fotos de los sensores de Milesight IoT manteniendo
el radio de aspecto fijo y garantizar que todas las imagenes tengan el mismo alto.
'''
from PIL import Image

def scale_image(image_path, base_height):
    # Abre la imagen desde la ruta especificada
    image = Image.open(image_path)
    
    # Calcula el porcentaje de la altura deseada respecto a la altura original
    h_percent = (base_height / float(image.size[1]))
    
    # Calcula la nueva anchura manteniendo el radio de aspecto
    w_size = int((float(image.size[0]) * float(h_percent)))
    
    # Redimensiona la imagen usando el método LANCZOS
    scaled_image = image.resize((w_size, base_height), Image.Resampling.LANCZOS)
    
    return scaled_image

# Ruta de la imagen a escalar
image_path1 = 'GS301.png'
image_path2 = 'VS121.png'
image_path3 = 'WS101.png'
image_path4 = 'WS201.png'

# Altura deseada para todas las imágenes
base_height = 380

# Escala la imagen y muestra el resultado
scaled_img1 = scale_image(image_path1, base_height)
scaled_img2 = scale_image(image_path2, base_height)
scaled_img3 = scale_image(image_path3, base_height)
scaled_img4 = scale_image(image_path4, base_height)
#scaled_img1.show()

# Guarda la imagen escalada
scaled_img1.save('GS301_HeightScale.png')
scaled_img2.save('VS121_HeightScale.png')
scaled_img3.save('WS101_HeightScale.png')
scaled_img4.save('WS201_HeightScale.png')