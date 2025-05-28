# -*- coding: utf-8 -*-
import ezdxf
import os
import argparse
import sys

def validar_entrada(valor, nome):
    if valor <= 0:
        print(f"Erro: O número de {nome} deve ser maior que zero.")
        sys.exit(1)

def gerar_mesa_dxf(num_cols, num_rows):
    # Valida as entradas
    validar_entrada(num_cols, "colunas")
    validar_entrada(num_rows, "linhas")
    
    # Cria um novo documento DXF
    doc = ezdxf.new(dxfversion='R2010')
    msp = doc.modelspace()

    # Calcula o tamanho do retângulo
    rect_width = num_cols * 100
    rect_height = num_rows * 100
    
    # Desenha o retângulo principal
    msp.add_lwpolyline([(0, 0), (rect_width, 0), (rect_width, rect_height), (0, rect_height), (0, 0)])

    # Configurações dos furos
    rect_size = 100  # Tamanho do retângulo (100x100mm)
    hole_diameter = 16  # Diâmetro do furo
    margin = 0  # Margem da borda

    # Gera os furos
    for row in range(num_rows):
        for col in range(num_cols):
            # Calcula a posição do centro do furo
            center_x = margin + (col * rect_size) + (rect_size / 2)
            center_y = margin + (row * rect_size) + (rect_size / 2)
            
            # Adiciona o furo
            msp.add_circle((center_x, center_y), hole_diameter / 2)

    # Obtém o diretório atual e cria o caminho completo do arquivo
    diretorio_atual = os.path.dirname(os.path.abspath(__file__))
    caminho_arquivo = os.path.join(diretorio_atual, f"mesa_solda_{rect_width}x{rect_height}.dxf")

    # Salva o arquivo
    doc.saveas(caminho_arquivo)
    print(f"Arquivo '{caminho_arquivo}' gerado com sucesso!")

if __name__ == "__main__":
    # Configura o parser de argumentos
    parser = argparse.ArgumentParser(
        description='Gera um arquivo DXF de uma mesa de solda com furos.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Exemplo de uso:
    python gerar_mesa.py -colunas 4 -linhas 3
    
    Isso irá gerar uma mesa de solda com:
    - 4 colunas de furos
    - 3 linhas de furos
    - Tamanho total: 400mm x 300mm
    - Arquivo de saída: mesa_solda_400x300.dxf
        '''
    )
    parser.add_argument('-colunas', type=int, required=True, 
                       help='Número de colunas de furos (deve ser maior que zero)')
    parser.add_argument('-linhas', type=int, required=True, 
                       help='Número de linhas de furos (deve ser maior que zero)')
    
    # Processa os argumentos
    args = parser.parse_args()
    
    # Gera a mesa com os parâmetros fornecidos
    gerar_mesa_dxf(args.colunas, args.linhas) 