#agenda do ano
def agendaAno():
    agenda = [True, True, True, True, True, True, True, True, True, True, True]

    return ([agenda]*31,
            [agenda]*28,
            [agenda]*31,
            [agenda]*30,
            [agenda]*31,
            [agenda]*30,
            [agenda]*31,
            [agenda]*31,
            [agenda]*30,
            [agenda]*31,
            [agenda]*30,
            [agenda]*31
           )

#verifica se um horário especifico está liberado
def verificaHorario(mes,dia,horario,agenda):
    return agenda[mes-1][dia-1][horario-8]

#verifica os dias do mês com horários disponiveis
def diasNoMesDisponiveis(agenda,mes):
    listaDeDias = []
    for i in range(len(agenda[mes-1])):
        if True in agenda[mes-1][i]:
            listaDeDias.append(f"dia {i+1}")
    return listaDeDias

#verifica os horarios disponives em um dia especifico
def horarioNoDiaDisponiveis(agenda,mes,dia):
    listaDehoras = []
    for i in range(11):
        if True == agenda[mes-1][dia-1][i]:
            listaDehoras.append(f"hora {i+8}")
    return listaDehoras

#agenda um horario
def agendarHora(mes,dia,horario,agenda):
    agenda[mes-1][dia-1][horario-8] = False
    return agenda[mes-1][dia-1][horario-8]

#desmarca um horario
def desmarcarHora(mes,dia,horario,agenda):
    agenda[mes-1][dia-1][horario-8] = True
    return agenda[mes-1][dia-1][horario-8]

def main():
    agenda = agendaAno()
    print(horarioNoDiaDisponiveis(agenda,10,12))
