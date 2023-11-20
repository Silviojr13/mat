import re
import ttg

class FormulaLogica:
    def __init__(self, formula):
        self.formula = formula.lower()
        self.variaveis = self._encontrar_variaveis()
        self.operacoes = self._encontrar_operacoes()

    def _encontrar_variaveis(self):
        return set(re.findall(r'\b[a-zA-Z]\b', self.formula))

    def _encontrar_operacoes(self):
        operacoes_encontradas = re.findall(r'\b(and|or|not|nor|xor|nand|implies)\b', self.formula)
        dict_operacoes = {}
        for operacao in operacoes_encontradas:
            dict_operacoes[operacao] = dict_operacoes.get(operacao, 0) + 1
        return dict_operacoes

    def gerar_tabela(self):
        return ttg.Truths(list(self.variaveis), [self.formula], ints=False).as_prettytable()

def main():
    while True:
        formula = input("Digite uma fórmula lógica | EXEMPLO: a and b : ")
        formula_logica = FormulaLogica(formula)
        print(f'Fórmula em minúsculo: {formula_logica.formula}')
        print(f'Variáveis: {formula_logica.variaveis}')
        print(f'Operações:')
        for operacao, contagem in formula_logica.operacoes.items():
            print(f'{operacao}: {contagem} vez(es)')
        print(formula_logica.gerar_tabela())
        continuar = input('Deseja continuar? S | N ')
        if continuar.lower() == 'n':
            print("Saindo... Obrigado por usar o programa!")
            break

if __name__ == "__main__":
    main()
