from Bio.PDB import PDBParser

def extract_coordinates(pdb_file, atom_name):
    parser = PDBParser(QUIET=True)
    structure = parser.get_structure('RNA', pdb_file)
    coords = []

    for atom in structure.get_atoms():
        if atom.get_name() == atom_name:
            coords.append(atom.get_coord())
    
    return np.array(coords)

native_coords = extract_coordinates("native.pdb", "C3'")
predicted_coords = extract_coordinates("predicted.pdb", "C3'")