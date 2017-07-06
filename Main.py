from PID import PID
from control.matlab import *
from Analise import Analise
from matplotlib.pyplot import * 
from Parametros import Parametros

def dadosPID(pid):
    Kp = pid.getKp()
    Ki = pid.getKi()
    Kd = pid.getKd()
    gain = pid.getGain()
    
    print("C(s):",pid.getControlador())
    print("Função Transferencia do sistema:",pid.getSistem())
    print("Resposta ao degrau:",pid.getStepResponse())
    try:
        tempo, resposta, T = pid.step(0, 6)
        plot(tempo, resposta.T)
        grid()
        title('Resposta ao Degrau (Kp ='+str(Kp)+', Ki ='+str(Ki)+', Kd ='+str(Kd)+', Ganho ='+str(gain)+')')
        ylabel('Amplitude')
        xlabel('Tempo (segundos)')
    except:
        print('...')

def Root_Locus(F, Kp, Ki, Kd, ganho):
    try:
        print("Zeros: ", zero(F))
        print("Polos: ", pole(F))
        rlocus(F)
        title('Raizes (Kp ='+str(Kp)+', Ki ='+str(Ki)+', Kd ='+str(Kd)+', Ganho ='+str(ganho)+')')
        grid()
    except:
        print ("Root Locus >> Raízes puramente complexas... >> AssertionError: Quadratic has a nontrivial imaginary part")
        
A = Analise()
pid = PID()
print("Ball And Beam")
op_main = 'R'
while (op_main == 'r' or op_main == 'R'):
    op = input("[1] Ver analise do sistema\n[2] Ver modelagem do sistema\n>>")

    if (op == '1'):
        print("Planta: ",A.getPlant())
        print("Zeros: ",A.getZeros())
        print("Polos: ",A.getPolos())
        
        tempo, resposta, T, G = A.getStepResponse()
        
        plot(tempo, resposta.T)
        grid()
        title('Resposta ao Degrau do Sistema')
        ylabel('Amplitude')
        xlabel('Tempo (segundos)')

        A.plotRoots()
        show()
    elif (op == '2'):
        print("\nModelagem do sistema")
        op_modelagem = input("\n[1] Modelagem ideal (Kp = 15, Ki = 0, Kd = 40)\n[2] Inserir valores para Kp, Kd e Ki\n>>")
        if (op_modelagem == '1'):
            Root_Locus(pid.getSistem(),pid.getKp(), pid.getKi(), pid.getKd(), pid.getGain())
            dadosPID(pid)
            show()
                
        elif(op_modelagem == '2'):
            print("\nInserir valores")
            Kp = float(input("\nKp = "))
            Ki = float(input("\nKi = "))
            Kd = float(input("\nKd = "))
            ganho = pid.getGain()
            
            print ("Ganho atual: ",ganho)
            op_gain = input ("[1] Alterar o ganho atual\n[2] Manter ganho\n>>")
            if (op_gain == '1'):
                ganho = float(input("\nGanho = "))
                
            pid.pid(Kp,Ki,Kd,ganho)
            Root_Locus(pid.getSistem(),pid.getKp(), pid.getKi(), pid.getKd(), pid.getGain())
            dadosPID(pid)
            show()
            print("Observe que o sistema não tem redução de grau entre o denominador e o numerador")
            print("Portanto podem ser encontrados polos e zeros a mais...")
            print("O sistema também não suporta caso de raízes puramente complexas...")
                  
        else:
            print("Opção inválida")
    else:
        print("Opção inválida")

    op_main = input("\n\n\n[R] Para repetir\n[Outra tecla] Para sair...\n>>")
