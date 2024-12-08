from typing import Any


class Observation:
    def __init__(self, infos: dict[str, Any]):
        self.infos = infos
    def __str__(self) -> str:
        infos_string = ""
        for info_key, info_value in self.infos.items():
            infos_string += f"{info_key}={str(info_value)}"
        return f"Observation: [{infos_string}]"