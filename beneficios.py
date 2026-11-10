class FundoDePensao:
    def __init__(self, nome_instituicao):
        # Define o ator que executa a ação
        self.nome_instituicao = nome_instituicao

    def transferir_pagamento(self, nome_beneficiario, oraculo_emitiu_obito):
        """
        Regra de Negócio: O pagamento mensal do benefício só pode ser transferido
        se não existir atestado de óbito emitido por Oráculo na blockchain.

        """

        print(f"\nA processar o benefício de: {nome_beneficiario}...")

        # A condição: Só transfere se a variável óbito for falsa (not oraculo_emitiu_obito)

        if not oraculo_emitiu_obito:
            print(f"✅ SUCESSO: {self.nome_instituicao} transferiu o pagamento mensal para {nome_beneficiario}.")
            return True
        else:
            print(f"❌ BLOQUEADO: O programa validou um atestado de óbito emitido por um Oráculo na blockchain.")
            return False

        
# ==========================================
# TESTES DE VALIDAÇÃO (Simulação do Oráculo)
# ==========================================

if __name__ == "__main__":
    # 1. Instanciamos a instituição pagadora
    estado = FundoDePensao("Estado (Segurança Social)")

    # 2. Cenário A: O Oráculo NÃO emitiu atestado de óbito (Cidadão Vivo)
    obito_joao = False
    estado.transferir_pagamento("João Silva", obito_joao)

    # 3. Cenário B: O Oráculo (Hospital/Cartório) EMITIU o atestado na rede (Cidadão Falecido)
    obito_maria = True
    estado.transferir_pagamento("Maria Santos", obito_maria)

