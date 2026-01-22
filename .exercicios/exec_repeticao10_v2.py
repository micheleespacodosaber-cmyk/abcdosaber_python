# importacao de modulos py
import exec_repeticao10_v2_modulo as mod 

# programa principal 
praias = mod.informar_praias()
num_praias_distam_mais_15km = mod.calcular_praias_distancia_mais_15km(praias)
qtd_media_veranistas = mod.calcular_media_veranistas_acesso_nao_asfaltado(praias)
praias_acesso_asfaltado_menos_1000 = mod.obter_praias_acesso_asfaltado_menos_1000(praias)
mod.exibir_resultados(num_praias_distam_mais_15km, qtd_media_veranistas, praias_acesso_asfaltado_menos_1000)
