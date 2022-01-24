from django.shortcuts import render
# from PIL import Image, ImageDraw, ImageFont
#
#
# def write_text(path, text):
#     with Image.open(path) as image:
#         w_width = finish[0] - start[0]
#         w_height = finish[1] - start[1]
#         word = main_text.split(' ')
#
#         for size in range(8, 25):
#             index = 0
#             font = ImageFont.truetype(font_path, size=size)
#             y = font.getsize(font_path)[1]
#             while index < len(word):
#                 buffer_size = 0
#                 while buffer_size <= w_width:
#                     buffer_size += len(word[index]) + 1
#                     index += 1
#                     if index == len(word):
#                         break
#                 y += (size * 1.5)
#             if y > w_height:
#                 size -= 1
#                 # print(y)
#                 break
#         # print(size)
#         draw = ImageDraw.Draw(image)
#         font = ImageFont.truetype(font_path, size=size)
#
#         index = 0
#
#         x = start[0]
#         y = start[1]
#         while index < len(word):
#             buffer = ''
#             while font.getsize(buffer)[0] <= w_width:
#                 buffer = buffer + word[index] + ' '
#                 index += 1
#                 if index == len(word):
#                     break
#             draw.text((x, y), text=buffer, fill=0, font=font)
#             y += (size * 1.5)
#
#         image.save(out_file)
#
#
# in_file = 'how.jpeg'
# out_file = 'new.jpg'
#
# font_path = "/System/Library/Fonts/Noteworthy.ttc"
# start = (340, 40)
# finish = (560, 100)
# main_text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '''
#
#
#
#
#
#

