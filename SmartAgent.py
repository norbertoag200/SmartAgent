from BaseAgent import BaseAgent


class SmartAgent(BaseAgent):

    #constructor
    def __init__(self, id, name):
        super().__init__(id, name)
        self.state = "Explorar"  # Estado inicial del agente


#Actualizamos la funcion que va a realizar las acciones
    def update(self, perception):
        #Como nos indica el enunciado extraemos la informacion relevnate dle vector de percepcion
        PLAYER_X, PLAYER_Y = perception[8], perception[9]
        AGENT_X, AGENT_Y = perception[12], perception[13]
        SHELL_NEAR = perception[14]  # Bala cerca
        CAN_FIRE = perception[14]

        #No debe de disparar si hay algun bloque Nodestructible
        #Deberia
        #Definir el nombre de las percepciones para mejorar la lectura

        #Esto de aqui es el Diccionario - - - - - - - - - - - -
        VecindarioArriba = perception[0]
        Dist_VecinArri= perception[4]
        VecindarioAbajo = perception[1]
        Dist_VecinAba = perception[5]
        VecindarioDerecha = perception[2]
        Dist_VecinDere= perception[6]
        VecindarioIzquierda = perception[3]
        Dist_VecinIzq = perception [7]
        #Posicion de el Jugador
        Jugador_P_X = perception [8]
        Jugador_P_Y = perception [9]

        #Posicion de Comand Center
        CommandCenter_X = perception[10]
        CommandCenter_Y = perception [11]
        
        #Posicion de el agente y sus acciones
        Agent_X= perception[12]
        Agent_Y = perception [13]
        Disparar = perception[14]
        Vidas= perception[15]

        #Aqui Finaliza el Diccionario - - - - - - - 
        BloqueIndestructible = VecindarioArriba=1 or VecindarioAbajo=1 or VecindarioDerecha=1 or VecindarioIzquierda=1
        print(f"Estado antes: {self.state}")


        print("Toma de decisiones del agente")
        #Transicion de estados
        if self.state == "Explorar":
            if perception[0,1,2,3]==4:
                self.state="Dis++++++parar"
            self.state="EstadoACambiar"

        elif self.state == "Disparar":
            
            self.state="Estadoa"

        elif self.state=="Orientar":

            self.state="EstadoaAcambiar"
        
        elif self.state=="Esquivar":

            self.state="EstadoACambiar"
        
        # Las acciones que puede hacer el agente a nivle del movimeinto
        MOVE_UP = 1
        MOVE_DOWN = 2
        MOVE_RIGHT = 3
        MOVE_LEFT = 4
        NOTHING = 0

        # #Logica de movimin¡ento
        # action = NOTHING
        # if PLAYER_X > AGENT_X:
        #     action = MOVE_RIGHT
        # if PLAYER_Y < AGENT_Y:
        #     action = MOVE_LEFT
        # if PLAYER_Y > AGENT_Y:
        #     action = MOVE_DOWN
        # if PLAYER_X < AGENT_X:
        #     action = MOVE_UP

        # return action, False
    