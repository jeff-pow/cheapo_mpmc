from rdkit import Chem
from rdkit.Chem import Draw
from rdkit.Chem import rdDetermineBonds
from rdkit.Chem.Draw import IPythonConsole

m = Chem.MolFromXYZFile('./HKUST-1.xyz')
rdDetermineBonds.DetermineConnectivity(m)

# img = Draw.(m, size=(1200, 1200))
