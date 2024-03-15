# PDF Resume Analyzer

O PDF Resume Analyzer é um programa em Python que extrai informações de currículos em formato PDF e realiza uma análise detalhada dos dados contidos neles.

## Funcionalidades

- **Extração de Dados:** Extrai informações essenciais de currículos em PDF, como nome, endereço, histórico educacional, experiência profissional e habilidades.
- **Análise de Dados:** Utiliza processamento de linguagem natural para analisar os dados extraídos e identificar competências-chave, experiências relevantes e outras informações importantes.
- **Geração de Relatórios:** Gera relatórios resumidos destacando os pontos fortes e fracos dos candidatos com base na análise dos currículos.
- **Interface de Usuário:** Pode ser executado por meio de uma interface de linha de comando ou uma interface gráfica do usuário para facilitar a interação.

## Tecnologias Utilizadas

- Python
- PyPDF2
- spaCy
- pandas

## Como Usar

1. Instale as dependências do projeto:

```{bash}
pip install -r requirements.txt
```

2. Execute o programa, fornecendo o caminho para o arquivo PDF do currículo:

```{bash}
python pdf_resume_analyzer.py --file caminho_para_curriculo.pdf
```

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para propor melhorias, reportar bugs ou adicionar novas funcionalidades. Por favor, siga as diretrizes de contribuição.

## Licença

Este projeto está licenciado sob a [Licença MIT](LICENSE).
