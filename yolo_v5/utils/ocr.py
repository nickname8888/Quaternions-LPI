# # crop = r"C:\Users\Rishi\Desktop\Regional number plate\general car imgs\g3.png"

from distutils.command import upload
import easyocr
from utils.post import post
from utils.stringCleaning import stringClean
from utils.cloudDB import storePlate
from utils.uploadImg import uploadimg
from utils.regex import check_numberplate
PREV_PLATE = ""
def eng_ocr(crop, crp_img_path):
  global PREV_PLATE
  reader = easyocr.Reader(['en'])
  res = reader.readtext(crop, mag_ratio=2, paragraph='False',detail=0, contrast_ths=0.3, batch_size=3) 
  print(crp_img_path, res)
  op = stringClean(res)
  if PREV_PLATE == op:
    ...
  elif op == '' or op == ' ':
    ...
  elif check_numberplate(op):
    url = uploadimg(str(crp_img_path))
    storePlate(url,op)
    PREV_PLATE = op
    return op
  return ''
  
  print(type(op))
  post(res)
  

# import easyocr
# # # from post import post


# crop = r"C:\Users\Rishi\Desktop\Regional number plate\general car imgs\g3.png"
# def eng_ocr(crop):
#   reader = easyocr.Reader(['en'])
#   res = reader.readtext(crop, mag_ratio=2,paragraph='False', detail=0, blocklist=".,;:[]?(){}/-/+!@#$%^&~`", contrast_ths=0.3, batch_size=2)
#   print(res) 
#   print(res[1])
#   print(type(res[1]))
#   # post(res)

# eng_ocr(crop)