import PySimpleGUI as sg 
import main

main.main()

font = ("Times New Roman", 12)
FontTitle = ("Times New Roman", 60)
FontSubtitle = ("Times New Roman", 20)
font2 = ("Times New Roman", 6)
font3 = ("Times New Roman", 24)

LayoutMenu = [
    [sg.Text('Menu de Sorteio', text_color="Black", background_color="White", font=FontSubtitle)],
    [sg.Image("Logo.png", size=(300,300), background_color="White")],
    [sg.Button('Sortear', size=(12, 3), button_color="Black")]]

Janela = sg.Window('Menu', LayoutMenu, background_color = "White", element_justification='c')
event, values = Janela.Read()

LayoutFinal = [
    [sg.Text("Resultado do sorteio", font=FontSubtitle,text_color="Black", background_color='White')],
    [sg.Text(f"Equipe 1: {main.saida1}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 2: {main.saida2}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 3: {main.saida3}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 4: {main.saida4}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 5: {main.saida5}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 6: {main.saida6}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 7: {main.saida7}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 8: {main.saida8}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 9: {main.saida9}", text_color="Black", background_color="White")],
    [sg.Text(f"Equipe 10: {main.saida10}", text_color="Black", background_color="White")]
]


if event == "Sortear":
    Janela.close()
    Janela2 = sg.Window('Resultado', LayoutFinal, size = (400,350), background_color="White", element_justification='c')
    event2, values2 = Janela2.Read()