import os, werkzeug


def save_file(file, path, filename):
  image_name = werkzeug.utils.secure_filename(filename)
  new_path = os.path.join("../images", *path)
  if not os.path.exists(new_path):
    os.makedirs(new_path)
  file.save(os.path.join(new_path, image_name))