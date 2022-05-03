from re import compile

def check_numberplate(plate): 
    plate_format = compile('^[A-Z]{2}?[0-9]{1,2}?[A-Z]{1,3}?[0-9]{1,4}$')
    plate = plate.upper().replace(" ", "")
    if plate_format.match(plate) is not None:
        return 1
    else:
        return 0

# platez = ["MH05EL2747", "MH05EL2247", "MH05EL2747", "MH05DK7160", "MH04BL8616"]
# correct_platez = []
# for plate in platez: 
#     output = check_numberplate(plate)
#     if output: 
#         # log to db 
#         print(output)
#         correct_platez.append(output)
#     else: 
#         # ofc don't log to db 
# #         pass
    
# print("#####################################")
# print(check_numberplate("MH05E00047"))