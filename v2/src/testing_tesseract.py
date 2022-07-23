import os
import PyPDF2
import camelot
#%%
#-----------------------------------------------------------------------
#%%
pdf_path = "/Users/mac/Documents/MT_Airport_Digital_Mockup/v2/src/coruna_AD.pdf"
pdf_tables = camelot.read_pdf(pdf_path, pages='3')
# with open(pdf_path)
pdf_tables[1].to_json('coruna.json')
print(pdf_tables[1].df)
