import time
import concurrent.futures
from PIL import Image, ImageFilter

img_names = img_urls = [
    '/photo-1516117172878-fd2c41f4a759.jpg',
    '/photo-1532009324734-20a7a5813719.jpg',
    '/photo-1524429656589-6633a470097c.jpg',
    '/photo-1530224264768-7ff8c1789d79.jpg',
    '/photo-1564135624576-c5c88640f235.jpg',
    '/photo-1541698444083-023c97d3f4b6.jpg',
    '/photo-1522364723953-452d3431c267.jpg',
    '/photo-1530122037265-a5f1f91d3b99.jpg',
    '/photo-1516972810927-80185027ca84.jpg',
    '/photo-1550439062-609e1531270e.jpg',
    '/photo-1549692520-acc6669e2f0c.jpg'
]

start = time.perf_counter()

size = (1200, 1200)

# for img_name in img_names:
def process_image(img_name):
    img = Image.open(f"./Input/{img_name}")

    img = img.filter(ImageFilter.GaussianBlur(15))

    img.thumbnail(size)
    img.save(f'./Output/{img_name}')
    print(f'{img_name} was processed...')

with concurrent.futures.ProcessPoolExecutor() as executor:
    executor.map(process_image, img_names)

finish = time.perf_counter()

print(f'Finished in {finish-start} seconds')