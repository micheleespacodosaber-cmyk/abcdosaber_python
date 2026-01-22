# definicao de classes
class Praia:
    def __init__(self, nome, distancia_centro, media_veranistas, tipo_acesso):
        self.nome = nome
        self.distancia_centro = distancia_centro
        self.media_veranistas = media_veranistas
        self.tipo_acesso = tipo_acesso

    def exibir_informacoes(self):
        print()
        print(f"Nome: {self.nome}")
        print(f"Distância do Centro: {self.distancia_centro} km")
        print(f"Média de Veranistas: {self.media_veranistas}")
        print(f"Tipo de Acesso: {self.tipo_acesso}")
        print("-" * 30)

# programa principal 
# praia = Praia("Copacabana", 5, 20000, 1)
# praia.exibir_informacoes()  
praias = []
qtd_praias = int(input("Digite a quantidade de praias a serem cadastradas: "))
for i in range(qtd_praias):
    nome = input(f"\nDigite o nome da {i+1}a. praia: ")
    distancia_centro = float(input("Digite a distância do centro (em km): "))
    media_veranistas = int(input("Digite a média de veranistas: "))
    tipo_acesso = int(input("Digite o tipo de acesso (0 - Não asfaltado, 1 - Asfaltado: "))

    praia = Praia(nome, distancia_centro, media_veranistas, tipo_acesso)
    praias.append(praia)    

# numero de praias que distam mais de 15 km do centro
# num_praias_distam_mais_15km = sum(1 for praia in praias if praia.distancia_centro > 15)
num_praias_distam_mais_15km = 0
for praia in praias:
    if praia.distancia_centro > 15:
        num_praias_distam_mais_15km += 1

# quantidade média de veranistas, na última temporada, nas praias com acesso não asfaltado;
qtd_media_veranistas = 0
qtd_veranistas_acesso_nao_asfaltado = 0
total_praias_acesso_nao_asfaltado = 0
for praia in praias:
    if praia.tipo_acesso == 0:
        qtd_veranistas_acesso_nao_asfaltado += praia.media_veranistas
        total_praias_acesso_nao_asfaltado += 1

if total_praias_acesso_nao_asfaltado > 0:
    qtd_media_veranistas = qtd_veranistas_acesso_nao_asfaltado / total_praias_acesso_nao_asfaltado


# nome e distância do centro, em km, de todas as praias de acesso asfaltado que tiveram menos de 1000 veranistas
praias_acesso_asfaltado_menos_1000 = []
for praia in praias:
    if praia.tipo_acesso == 1 and praia.media_veranistas < 1000:
        praias_acesso_asfaltado_menos_1000.append(praia)

# exibicao dos resultados
print(f"\nNúmero de praias que distam mais de 15 km do centro: {num_praias_distam_mais_15km}")
print(f"Média de veranistas nas praias com acesso não asfaltado: {qtd_media_veranistas:.2f}")

print("\nPraias de acesso asfaltado com menos de 1000 veranistas:")  
for praia in praias_acesso_asfaltado_menos_1000:
    print(f"Nome: {praia.nome}, Distância do Centro: {praia.distancia_centro} km")
