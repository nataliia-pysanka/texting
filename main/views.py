from PIL import Image, ImageDraw, ImageFont
from django.shortcuts import render
from django import forms
from texting.settings import STATIC_ROOT

font_path = "main/fonts/Noteworthy.ttc"
box = {'start': [], 'finish': []}


class MessageForm(forms.Form):
    msg = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Input greetings ...',
                                                       'id': 'msg'}))
    start_x = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                            'id': 'start_x'}))
    start_y = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                            'id': 'start_y'}))
    finish_x = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                          'id': 'finish_x'}))
    finish_y = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                          'id': 'finish_y'}))
    image_path = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                          'id': 'img'}))
    image_width = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                          'id': 'img_width'}))
    image_height = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden',
                                                          'id': 'img_height'}))


def greet(request):
    if request.method == "POST":
        form = MessageForm(request.POST)
        if form.is_valid():
            msg = f'{form.cleaned_data["msg"]}'
            start = (float(form.cleaned_data["start_x"]),
                     float(form.cleaned_data["start_y"]))
            finish = (float(form.cleaned_data["finish_x"]),
                    float(form.cleaned_data["finish_y"]))
            image_path = 'static/images/' + form.cleaned_data["image_path"]
            web_size = (float(form.cleaned_data["image_width"]),
                          float(form.cleaned_data["image_height"]))
            write_text(image_path, start, finish, web_size, font_path, msg)
            return render(request, 'main/1.html', {})
        else:
            return render(request, 'main/index.html', {'form': form})
    return render(request, 'main/index.html', {'form': MessageForm()})


def resize(xy, wh, real_size, web_size):
    x = xy[0] * real_size[0] / web_size[0]
    y = xy[1] * real_size[1] / web_size[1]
    w = (wh[0] - xy[0]) * real_size[0] / web_size[0]
    h = (wh[1] - xy[1]) * real_size[1] / web_size[1]
    return x, y, w, h


def write_text(path, start, finish, web_size, font_path, text):
    with Image.open(path) as image:
        x, y, w, h = resize(start, finish, (image.width, image.height), web_size)

        word = text.split(' ')
        for size in range(6, 30):
            index = 0
            font = ImageFont.truetype(font_path, size=size)
            y = font.getsize(font_path)[1]
            while index < len(word):
                buffer_size = 0
                while buffer_size <= (w - (size * 3)):
                    buffer_size += len(word[index]) + 1
                    index += 1
                    if index == len(word):
                        break
                y += (size * 1.5)
            if y > h:
                size -= 1
                break
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype(font_path, size=size)

        index = 0
        draw.rounded_rectangle([x, y, x+w, y+h], radius=5, fill='white', outline=None, width=1)
        # draw.text((x, y), text=f'x={x}, y={y}, w={w}, h={h}', fill=0, font=font)
        # draw.text((2*x, 2*y), text=f'start={start}, finish={finish}', fill=1, font=font)
        while index < len(word):
            buffer = ''
            while font.getsize(buffer)[0] <= (w - (size * 3)):
                buffer = buffer + word[index] + ' '
                index += 1
                if index == len(word):
                    break
            draw.text((x + (size * 1.5), y), text=buffer, fill=0, font=font)
            y += (size * 1.5)

        image.save(STATIC_ROOT / 'images/new.jpeg')
        return True

