from ..services.http import HTTPClient
from enum import Enum
from .models import Specification
from typing import Optional, Dict, Any
from ..vehicles.models import Vehicle


class API(Enum):
    APK = "https://opendata.rdw.nl/resource/m9d7-ebf2.json?"

def SpecsLogic(vehicle: Vehicle) -> None:
    specs = GetSpecs(vehicle.plate)
    if not 'error' in specs and specs:
        specs = specs[0]
        vehicle_specs = ParseSpecs(vehicle,specs)
        SaveSpecs(vehicle_specs)
    else:
        ValueError("No specs found")

def GetSpecs(plate: str) -> Optional[Dict[str, Any]]:
    client = HTTPClient(API.APK.value)
    response = client.get(f"kenteken={plate}")
    return response

def SaveSpecs(vehicle_specs: Specification) -> None:
    vehicle_specs.save()

def ParseSpecs(vehicle: Vehicle,specs: Dict[str, Any]) -> Specification:
    return Specification(
        vehicle=vehicle,
        brand=specs.get("merk"),
        model=specs.get("handelsbenaming"),
        first_registry=specs.get("datum_eerste_toelating"),
        fuel=specs.get("brandstof_omschrijving")
    )
