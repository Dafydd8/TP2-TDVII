import converter

entities = [
    "accededocumento",
    "capacidad",
    "documentodigital",
    "efectordesalud",
    "efectordesaludservicio",
    "efectortercernivel",
    "formaenvio",
    "hce",
    "hcecapacidad",
    "hcegeneraobrassociales",
    "hcegeneraprepagas",
    "hcegenerareceta",
    "persona",
    "problema",
    "provincia",
    "servicio"
]

for entity in entities:
    print(f"Converting {entity}...")
    converter.convert(entity)
