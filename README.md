# Gerador de Mesa DXF

Este script Python gera um arquivo DXF contendo um desenho de uma mesa com furos em grade regular, ideal para mesas de solda ou trabalho.

## 📋 Especificações

- Dimensões da mesa: Calculadas automaticamente com base no número de colunas e linhas
- Diâmetro dos furos: 16mm
- Espaçamento entre furos: 100mm
- Margem da borda: 50mm

## 🚀 Requisitos

- Python 3.x
- Biblioteca ezdxf

## 💻 Instalação

1. Clone este repositório:

```bash
git clone https://github.com/seu-usuario/gerador-mesa-dxf.git
cd gerador-mesa-dxf
```

2. Instale as dependências:

```bash
pip install -r requirements.txt
```

## 🛠️ Uso

O script aceita os seguintes argumentos:

```bash
python gerar_mesa.py -colunas <número> -linhas <número>
```

### Argumentos:

- `-colunas`: Número de colunas de furos (deve ser maior que zero)
- `-linhas`: Número de linhas de furos (deve ser maior que zero)

### Exemplo:

```bash
python gerar_mesa.py -colunas 4 -linhas 3
```

Isso irá gerar uma mesa de solda com:

- 4 colunas de furos
- 3 linhas de furos
- Tamanho total: 400mm x 300mm
- Arquivo de saída: mesa_solda_400x300.dxf

Para ver todas as opções disponíveis:

```bash
python gerar_mesa.py --help
```

## ⚙️ Personalização

Para modificar as dimensões da mesa ou outras especificações, edite as variáveis no início do arquivo `gerar_mesa.py`:

```python
DIAMETRO_FURO = 16  # em milímetros
ESPACAMENTO = 100   # em milímetros
MARGEM = 50        # em milímetros
```

## 🤝 Contribuição

Sinta-se à vontade para contribuir com este projeto através de:

1. Pull requests
2. Reportando issues
3. Sugerindo melhorias
4. Compartilhando o projeto

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo `LICENSE` para mais detalhes.

## 📞 Suporte

Se você encontrar algum problema ou tiver dúvidas, por favor:

1. Abra uma issue no GitHub
2. Entre em contato através do email: izidorio@bento.dev.br
