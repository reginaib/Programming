"""
>>> table = mass_table('mass.txt')
>>> table['A']
71.03711
>>> table['E']
129.04259

>>> protein_mass('SKADYEK', table)
839.40248
>>> protein_mass('SKADYEK', table, peptide=True)
821.3919199999999
"""


def mass_table(location):
    mass_dict = {}
    with open(location, "r", encoding='utf-8') as file:
        for line in file:
            line = line.split(' ')
            line = [el for el in line if len(el) > 0]
            if line[0].isupper() and float(line[1]):
                mass_dict[line[0]] = float(line[1])
    return mass_dict


def protein_mass(prot_seq, mass_dict, peptide=False):
    mm = sum(mass_dict[letter] for letter in prot_seq)
    if not peptide:
        mm += 18.01528  # Mass of water (H2O)
    return mm

