from hyperon import MeTTa

metta = MeTTa()
metta.run('''
(gene ENSG00000290825)
(gene_type (gene ENSG00000290825) lncRNA)
(chr (gene ENSG00000290825) chr1)
(start (gene ENSG00000290825) 11869)
(end (gene ENSG00000290825) 14409)
(gene_name (gene ENSG00000290825) DDX11L2)
(synonyms (gene ENSG00000290825) (HGNC:37102 DEAD/H_\ (Asp-Glu-Ala-Asp/His\)_box_polypeptide_11_like_1 DEAD/H-box_helicase_11_like_1_\ (pseudogene\) DEAD/H_\ (Asp-Glu-Ala-Asp/His\)_box_helicase_11_like_1 DEAD/H_box_polypeptide_11_like_1 DDX11L1))
(source (gene ENSG00000290825) GENCODE)
(source_url (gene ENSG00000290825) https://www.gencodegenes.org/human/)
(gene ENSG00000223972)
(gene_type (gene ENSG00000223972) transcribed_unprocessed_pseudogene)
(chr (gene ENSG00000223972) chr1)
(start (gene ENSG00000223972) 12010)
(end (gene ENSG00000223972) 13670)
(gene_name (gene ENSG00000223972) DDX11L1)
(synonyms (gene ENSG00000223972) (HGNC:37102 DEAD/H_\ (Asp-Glu-Ala-Asp/His\)_box_polypeptide_11_like_1 DEAD/H-box_helicase_11_like_1_\ (pseudogene\) DEAD/H_\ (Asp-Glu-Ala-Asp/His\)_box_helicase_11_like_1 DEAD/H_box_polypeptide_11_like_1 DDX11L1))
(source (gene ENSG00000223972) GENCODE)
(source_url (gene ENSG00000223972) https://www.gencodegenes.org/human/)
''')

result = metta.run(''' 
	!(match &self ($x (gene $y) $m) ($x $y $m))
''')
print(result)
#print(metta.run('!(match &self (Parent Tom $x) $x)')) # [[Liz, Bob]]
#print(metta.run('!(match &self (Parent $x Bob) $x)')) # [[Tom, Pam]]
'''
atom1 = metta.parse_single('(A )(B)')
atom2 = metta.parse_single('(A B) (C D)')
metta.space().add_atom(atom2)
#print(metta.run("!(match &self (A $x) $x)"))
#print(atom1) # (A B)
#print(atom2) # (A B)

atom3 = metta.parse_all('(A) (B)')
#print(atom3)


pattern = metta.parse_single('(Parent $x Bob)')
print(metta.space().query(pattern)) # [{ $x <- Pam }, { $x <- Tom }]
#In contrast to match in MeTTa itself,
# # query doesn't take the output pattern, 
# but just returns options for variable bindings, 
# which can be useful for further custom processing in Python. 
# It would be useful to have a possibility to define patterns directly in Python instead of parsing them from strings.
'''