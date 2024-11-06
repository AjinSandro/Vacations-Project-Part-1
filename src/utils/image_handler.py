from pathlib import Path
from flask import current_app
from uuid import uuid4
class ImageHandler:

    @staticmethod
    def save_image(image):
        suffix = Path(image.filename).suffix # suffix of a.png is png. suffix of h.jpg is jpg.
        vacation_picture_file = str(uuid4()) + suffix # create unique name
        if not vacation_picture_file : return None
        image_path = Path(current_app.root_path) / "static/images" / vacation_picture_file # static/images/123123123-32131-kek.png
        image.save(image_path) # save the image on the server side on static/images/123123123-32131-kek.png
        return vacation_picture_file
        
    @staticmethod
    def get_image_path(vacation_picture_file):
        image_path = Path(current_app.root_path) / "static/images" / vacation_picture_file
        if not image_path.exists():
            image_path = Path(current_app.root_path) / "static/images/noimage.png"
        return image_path
    
    @staticmethod
    def update_image(old_image_name, image):
        if not image.filename :return old_image_name
        vacation_picture_file = ImageHandler.save_image(image)
        ImageHandler.delete_image(old_image_name)
        return vacation_picture_file
    
    @staticmethod
    def delete_image(vacation_picture_file):
        if not vacation_picture_file: return # do nothing
        if vacation_picture_file == "noimage.png":
            return
        image_path = Path(current_app.root_path) / "static/images" / vacation_picture_file
        image_path.unlink(missing_ok = True)
