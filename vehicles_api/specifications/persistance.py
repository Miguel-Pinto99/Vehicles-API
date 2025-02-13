from ..services.http import HTTPClient
from enum import Enum
from .models import Specification
from typing import Optional, Dict, Any



class API(Enum):
    APK = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?"

def SpecsLogic(plate: str) -> None:
    specs = GetSpecs(plate)
    if specs:
        vehicle_specs = ParseSpecs(specs)
        SaveSpecs(vehicle_specs)
    
def GetSpecs(plate: str) -> Optional[Dict[str, Any]]:
    client = HTTPClient(API.APK.value)
    response = client.get(f"kenteken={plate}")
    return response[0]

def SaveSpecs(vehicle_specs: Specification) -> None:
    vehicle_specs.save()

def ParseSpecs(specs: Dict[str, Any]) -> Specification:
    return Specification(
        plate=specs.get("kenteken"),
        brand=specs.get("merk"),
        model=specs.get("handelsbenaming"),
        year=specs.get("datum_eerste_toelating"),
        fuel=specs.get("brandstof_omschrijving")
    )