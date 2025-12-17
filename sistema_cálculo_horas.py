# 1. Cálculo da Base Bruta
# Salário Fixo: Valor do seu salário mensal.
# Adicional de 1/3: Salário Bruto ÷ 3. Esse é um valor extra pago por lei.

def valor_hora(carga, salario):
    valor_h =  salario/carga
    return valor_h

def cal_extra_50(valor_hr):
    hor_extra =  valor_hr * 1.5
    return hor_extra

def total(salario, quantidade_extra, valor_extraa):
    qua =  quantidade_extra * valor_extraa
    cal_total =  salario + qua
    return cal_total

# Vale-Transporte: Desconta-se até 6% do salário básico para cobrir 
# o custo do transporte, se o funcionário usar.
# Vale-Refeição/Alimentação: Desconto permitido em até 20% do valor concedido, 
# mediante acordo.

def desconto(salario):

    resto =  salario - (100*0.06) 
    resto -= 100*0.2
    return resto
   

def ferias(salario):
    um_terco = salario/3
    return um_terco

def sistema_rh():
    while True:
    print('SISTEMA DE CALCULOS TRABALHISTAS')
    salario =  float(input('SALARIO: '))
    carga =  float(input('Carga horária'))
    valor_hr  =  valor_hora(carga, salario)
    print('valor hora R$ ', round(valor_hr, 2))
    valor_ex_ = cal_extra_50(valor_hr)
    print('valor da hora extra 50% R$ ', round(valor_ex_,2))
    quantidade_extra = float(input('Quantidade de extra -  '))
    total_ = total(salario, quantidade_extra, valor_ex_)

    print('Total Salario com extra R$', round(total_,2))
    sal_descontos_ =  desconto(total_)
    print('SALARIO COM DESCONTO R$', round(sal_descontos_,2))
    print('------------------- FÉRIAS ----------------------')
    valor_receber_ferias  = ferias(total_)
    print('FERIAS R$', round(valor_receber_ferias,2))
    tt = valor_receber_ferias + total_
    print('A RECEBER R$',round(tt,2) ) 
sistema_rh()


# Para calcular hora extra, primeiro encontre o valor da sua hora normal 
# (salário / jornada mensal), depois aplique o adicional 
# (mínimo 50% em dia útil, 100% em feriado/domingo) sobre esse valor, 
# e por fim, multiplique pelo total de horas extras trabalhadas,
#  lembrando que também incide o DSR (Descanso Semanal Remunerado)





input('digite entre para sair...')