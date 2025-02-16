from pyrosm import get_data

def downloadExtract(location, dataDir):
    extract = get_data(location, directory=dataDir)
    print("Data was downloaded to:", extract)
