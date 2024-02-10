import flet as ft
from flet import (
    Text,
    AlertDialog,
    TextField,
    TextButton,
    Column,
    Container,
    LinearGradient,
    alignment,
    border_radius,
    padding,
    Image,
    UserControl,
    Row,
    IconButton,
    margin,
    icons,
    border,
    Card,
    transform,
    animation,
    Icon,
    SnackBar,
    Checkbox,
    Page,
    Scale,
)
from random import *

def main(page: ft.Page):
    page.title = "Password Generator"
    page.theme_mode = "dark"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    user_input = ft.TextField(label="", width=450)
    c1 = ft.Checkbox(label="Заглавные буквы")
    c2 = ft.Checkbox(label="Цифры")
    c3 = ft.Checkbox(label="Специальные символы")
    alphabet = [chr(i) for i in range(97, 123)]
    alphabet1 = [chr(i) for i in range(65, 91)]
    nums = ["1","2","3","4","5","6","7","8","9","0"]
    symbols = ["!","@","#","$","%","^","&","*",";","."]
    kek = []


    def change_theme(e):
        # smena temi
        if page.theme_mode == "dark":
            page.theme_mode = "light"
        else:
            page.theme_mode = "dark"
        page.update()

    def print(e):
        if c1.value == False and c2.value == False and c3.value == False:
            for i in range(18):
                kek.append(choice(alphabet))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == True and c2.value == False and c3.value == False:
            for i in range(9):
                kek.append(choice(alphabet1))
                kek.append(choice(alphabet))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == True and c2.value == True and c3.value == False:
            for i in range(6):
                kek.append(choice(alphabet1))
                kek.append(choice(alphabet))
                kek.append(choice(nums))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == True and c2.value == True and c3.value == True:
            for i in range(5):
                kek.append(choice(alphabet1))
                kek.append(choice(alphabet))
                kek.append(choice(nums))
                kek.append(choice(symbols))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == False and c2.value == True and c3.value == True:
            for i in range(6):
                kek.append(choice(alphabet))
                kek.append(choice(nums))
                kek.append(choice(symbols))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == True and c2.value == False and c3.value == True:
            for i in range(6):
                kek.append(choice(alphabet1))
                kek.append(choice(alphabet))
                kek.append(choice(symbols))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == False and c2.value == True and c3.value == False:
            for i in range(9):
                kek.append(choice(alphabet))
                kek.append(choice(nums))
            user_input.value = "".join(kek)
            kek.clear()
        elif c1.value == False and c2.value == False and c3.value == True:
            for i in range(9):
                kek.append(choice(alphabet))
                kek.append(choice(symbols))
            user_input.value = "".join(kek)
            kek.clear()
        page.update()

    page.add(
        ft.Row(
            [
                ft.Column(
                    [
                        user_input,
                        c1,
                        c2,
                        c3,
                        ft.OutlinedButton(text="сгенерировать", on_click=print)
                    ]
                ),
                ft.IconButton(ft.icons.SUNNY, on_click=change_theme),
            ],
            alignment=ft.MainAxisAlignment.CENTER
        ),
    ),
ft.app(target = main)