from distutils.command import upload
import easyocr
from utils.post import post
from utils.stringCleaning import stringClean
# from utils.cloudDB import storePlate
# from utils.uploadImg import uploadimg

PREV_PLATE = ""

def eng_ocr(crop, crp_img_path):
    global PREV_PLATE
    reader = easyocr.Reader(['en'])
    res = reader.readtext(crop, detail=0, paragraph=True) 
    print(crp_img_path, res)
    op = stringClean(res)
    print(op)
    # print()
    file1 = open("D:/Datasets/LPI/pipeline/DEEPBLUE_FINAL/outputs.txt", "a")  # append mode
    file1.write(op + ' ' + crp_img_path)
    file1.write('\n')
    file1.close()
    if PREV_PLATE == op:
        ...
    elif op == '' or op == ' ':
        ...
    else:
        # url = uploadimg(str(crp_img_path))
        # storePlate(url,op)
        # Append-adds at last
        PREV_PLATE = op
        return op
    return ''
  
  # print(type(op))
  # post(res)
  
def stringClean(lstOp):
    if len(lstOp) == 0:
        return ''
    clean = ""
    actual_string = ""
    length = len(lstOp)
    if length >= 2:
        actual_string = lstOp[1]
    else:
        actual_string = lstOp[0]

    actual_string = actual_string.upper()

    clean = actual_string
    if len(clean)<=8 or len(clean)>10:
        return ''
    return clean

# import easyocr
# from post import post

# crop = r"C:\Users\Rishi\Desktop\Regional number plate\general car imgs\g3.png"

# def eng_ocr(crop):
#   reader = easyocr.Reader(['en'])
#   res = reader.readtext(crop, detail=0, paragraph=True) 
#   print(res)
#   print(type(res))
#   post(res)

# eng_ocr(crop)


def eng_ocr_chatacter(crop, crp_img_path):
  global PREV_PLATE
  reader = easyocr.Reader(['en'])
  res = reader.readtext(crop, detail=0, paragraph=True) 
#   print(crp_img_path, res)
  op = stringCleanCharacter(res)
  # print(op)
  # print()
  # if PREV_PLATE == op:
  #   ...
  # elif op == '' or op == ' ':
  #   ...
  # else:
  #   url = uploadimg(str(crp_img_path))
  #   storePlate(url,op)
  #   Append-adds at last
  #   PREV_PLATE = op
  file1 = open("D:/Datasets/LPI/pipeline/DEEPBLUE_FINAL/outputs.txt", "a")  # append mode
  file1.write(op + ' ' + crp_img_path)
  file1.write('\n')
  file1.close()
  
  # print(type(op))
  # post(res)
  return op

def stringCleanCharacter(lstOp):
    if len(lstOp) == 0:
        return ''
    clean = ""
    actual_string = ""
    length = len(lstOp)
    if length >= 2:
        actual_string = lstOp[1]
    else:
        actual_string = lstOp[0]

    actual_string = actual_string.upper()

    clean = actual_string
    # if len(clean)<=8 or len(clean)>10:
    #     return ''
    return clean
