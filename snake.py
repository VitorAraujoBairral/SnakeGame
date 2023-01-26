import turtle as tr

#Criar a tela
wn = tr.Screen()
wn.setup(width=800, height=600)
wn.bgcolor("gray")
wn.title("Snake")
wn.tracer(0)


#Criar a cobra
def instanciarCobra(parte):
    parte.speed(0)
    parte.shape("square")
    parte.color("Green")
    parte.penup()
    parte.Aceleration = [0, 0]

cabeca = tr.Turtle()
cobra = [cabeca]

instanciarCobra(cobra[0])

#Cria a movimentação da cobra
#Cria o alimento e o crescimento da cobra
#Cria a mecânica de morte

#loop principal do jogo:
while True:

    wn.update()