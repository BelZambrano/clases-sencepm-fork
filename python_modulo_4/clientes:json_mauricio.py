from __future__ import annotations

import json
from pathlib import Path
from typing import List, Dict, Any, Optional

from dataclasses import dataclass, asdict

# Ruta del JSON único
JSON_PATH = Path("clientes.json")

@dataclass
class Cliente:
    id: Optional[int] = None
    nombre: str = ""
    correo: str = ""
    telefono: str = ""
    direccion: str = ""

    @classmethod
    def from_dict(cls, d: Dict[str, Any]) -> "Cliente":
        return cls(
            id=d.get("id"),
            nombre=d.get("nombre", ""),
            correo=d.get("correo", ""),
            telefono=d.get("telefono", ""),
            direccion=d.get("direccion", "")
        )

    def to_dict(self) -> Dict[str, Any]:
        return asdict(self)

    # Lectura/escritura del JSON
    @staticmethod
    def _load(path: Path) -> List[Dict[str, Any]]:
        if not path.exists():
            return []
        try:
            with path.open("r", encoding="utf-8") as f:
                data = json.load(f)
                return data if isinstance(data, list) else []
        except Exception:
            return []

    @staticmethod
    def _save(path: Path, data: List[Dict[str, Any]]) -> None:
        with path.open("w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    @staticmethod
    def _next_id(data: List[Dict[str, Any]]) -> int:
        m = 0
        for item in data:
            try:
                v = int(item.get("id", 0))
                if v > m:
                    m = v
            except (ValueError, TypeError):
                pass
        return m + 1

    @classmethod
    def all(cls, path: Path = JSON_PATH) -> List["Cliente"]:
        return [cls.from_dict(d) for d in cls._load(path)]

    def save(self, path: Path = JSON_PATH) -> None:
        data = self._load(path)
        if self.id is None:
            self.id = self._next_id(data)
        else:
            if any(int(it.get("id", -1)) == int(self.id) for it in data):
                raise ValueError(f"El id {self.id} ya existe.")
        data.append(self.to_dict())
        self._save(path, data)

    @classmethod
    def edit(cls, id: int, changes: Dict[str, Any], path: Path = JSON_PATH) -> bool:
        data = cls._load(path)
        for item in data:
            if int(item.get("id", -1)) == int(id):
                item.update(changes)
                cls._save(path, data)
                return True
        return False

# ------------------ Menú interactivo ------------------

def pedir_nuevo_cliente() -> Cliente:
    nombre = input("Nombre: ").strip()
    correo = input("Correo: ").strip()
    telefono = input("Teléfono: ").strip()
    direccion = input("Dirección: ").strip()
    return Cliente(nombre=nombre, correo=correo, telefono=telefono, direccion=direccion)

def listar():
    clientes = Cliente.all()
    if not clientes:
        print("No hay clientes almacenados.")
        return
    print("\n-- Lista de clientes --")
    for c in clientes:
        print(f"ID: {c.id} | Nombre: {c.nombre} | Correo: {c.correo} | Teléfono: {c.telefono} | Dirección: {c.direccion}")
    print("----------------------\n")

def agregar():
    c = pedir_nuevo_cliente()
    c.save()
    print(f"Cliente agregado con ID: {c.id}")

def editar():
    id_text = input("ID del cliente a editar: ").strip()
    if not id_text.isdigit():
        print("ID inválido.\n")
        return
    cid = int(id_text)
    cambios: Dict[str, Any] = {}
    print("Deja vacío para no cambiar un campo.")
    for label in ("nombre", "correo", "telefono", "direccion"):
        val = input(f"Nuevo {label.capitalize()}: ").strip()
        if val:
            cambios[label] = val
    if cambios:
        if Cliente.edit(cid, cambios):
            print("Editado exitosamente.\n")
        else:
            print("Cliente no encontrado.\n")
    else:
        print("No se realizaron cambios.\n")

def mostrar_menu():
    print("==== Gestión de Clientes ====")
    print("1. Agregar cliente")
    print("2. Ver clientes")
    print("3. Editar cliente")
    print("4. Salir")
    print("=============================")

def main() -> None:
    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción (1-4): ").strip()
        if opcion == "1":
            agregar()
        elif opcion == "2":
            listar()
        elif opcion == "3":
            editar()
        elif opcion == "4":
            print("Saliendo. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intenta nuevamente.\n")

if __name__ == "__main__":
    main()