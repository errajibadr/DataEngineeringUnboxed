import pandas
from docling.document_converter import DocumentConverter

dataframe = pandas.read_csv("data.csv")


source = "complexe_pdf.pdf"  # PDF path or URL https://arxiv.org/pdf/2408.09869
converter = DocumentConverter()
result = converter.convert(source)
print(result.document.export_to_markdown())  # output: "### Docling Technical Report[...]"
