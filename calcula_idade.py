from datetime import datetime

data_nasc = input("Digite sua data de nacsimento (dd/mm/yyyy): ")
nascimento = datetime.strptime(data_nasc, "%d/%m/%Y")
hoje = datetime.today()
idade = hoje.year - nascimento.year

print(f"voce tem {idade} anos atualmente.")