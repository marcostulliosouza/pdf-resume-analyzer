import PyPDF2
import spacy
from spacy.matcher import Matcher
import pandas as pd

# Carregar modelo de linguagem em português
nlp = spacy.load("pt_core_news_sm")

def extrair_texto_pdf(caminho_pdf):
    """Extrai texto de um arquivo PDF."""
    texto = ""
    with open(caminho_pdf, "rb") as arquivo_pdf:
        leitor_pdf = PyPDF2.PdfFileReader(arquivo_pdf)
        for pagina in range(leitor_pdf.numPages):
            texto += leitor_pdf.getPage(pagina).extractText()
    return texto

def analisar_curriculo(texto):
    """Realiza análise do currículo."""
    # Processar o texto com o modelo de linguagem
    doc = nlp(texto)

    # Inicializar matcher para encontrar seções relevantes
    matcher = Matcher(nlp.vocab)
    matcher.add("HABILIDADES", None, [{"LOWER": {"IN": ["habilidades", "competências"]}}])

    # Encontrar seções relevantes no texto
    secoes = {}
    for match_id, start, end in matcher(doc):
        secao = doc[start:end]
        secoes[secao.text.lower()] = secao.end

    # Extrair dados de seções relevantes
    habilidades = ""
    if "habilidades" in secoes:
        habilidades = doc[secoes["habilidades"]:].text

    return {"habilidades": habilidades}

def main():
    caminho_pdf = input("Digite o caminho para o arquivo PDF do currículo: ")
    texto_pdf = extrair_texto_pdf(caminho_pdf)
    resultado_analise = analisar_curriculo(texto_pdf)
    print("Habilidades:")
    print(resultado_analise["habilidades"])

if __name__ == "__main__":
    main()
