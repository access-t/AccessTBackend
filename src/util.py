import base64

def base64_encode(image):
  return base64.b64encode(image.read()).decode("utf-8")