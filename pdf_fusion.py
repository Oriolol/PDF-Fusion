import sys
import os
import pypdf


output_name = sys.argv[1]
input_pdfs = []
for pdf in sys.argv[2:]:
    input_pdfs.append(os.path.join("Input",pdf))
if ".pdf" not in output_name[-4:]:
    output_name += ".pdf"

i = 1
new_output_name = os.path.join("Output",output_name)
while os.path.exists(new_output_name):
    new_output_name = output_name[:-4] + f"({i})" + ".pdf"
    i+=1

output_name = new_output_name


merger = pypdf.PdfWriter()

for pdf in input_pdfs:
    merger.append(pdf)

merger.write(output_name)
merger.close()