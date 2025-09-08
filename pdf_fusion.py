import sys
import os
import pypdf


output_name = sys.argv[1]

if ".pdf" not in output_name[-4:]:
    output_name += ".pdf"

i = 1
new_output_name = output_name
while os.path.exists(new_output_name):
    new_output_name = output_name[:-4] + f"({i})" + ".pdf"
    i+=1

output_name = new_output_name


merger = pypdf.PdfWriter()

for pdf in sys.argv[2:]:
    merger.append(pdf)

merger.write(output_name)
merger.close()