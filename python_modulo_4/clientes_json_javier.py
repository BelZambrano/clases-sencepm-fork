import json
import uuid
from typing import List, Dict, Any

class Cliente:
    campos = ["id", "nombre", "telefono", "email", "estado"]
    
    def __init__(self, **kwargs):
        for campo in self.campos:
            setattr(self, campo, kwargs.get(campo))
        if not self.id:
            self.id = uuid.uuid4().hex[:8] 
        if not self.estado:
            self.estado = "activo"
    
    def to_dict(self) -> Dict[str, Any]:
        return {campo: getattr(self, campo) for campo in self.campos}
    
    def __str__(self) -> str:
        return f"ID: {self.id} | {self.nombre} ({self.estado})"

class GestorClientes:
    
    def __init__(self, archivo: str = "clientes.json"):
        self.archivo = archivo
        self.clientes: List[Dict[str, Any]] = self._cargar()
    
    def _cargar(self) -> List[Dict[str, Any]]:
        try:
            with open(self.archivo, "r", encoding="utf-8") as f:
                return json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            return []
    
    def _guardar(self) -> None:
        with open(self.archivo, "w", encoding="utf-8") as f:
            json.dump(self.clientes, f, ensure_ascii=False, indent=2)
    
    def agregar_cliente(self, **kwargs) -> None:
        cliente = Cliente(**kwargs)
        self.clientes.append(cliente.to_dict())
        self._guardar()
        print(f"Cliente agregado: {cliente}")
    
    def ver_clientes(self) -> None:
        if not self.clientes:
            print("No hay clientes.")
            return
        print("\n=== CLIENTES ===")
        for c in self.clientes:
            print(
                f"ID: {c.get('id','')} | {c.get('nombre','')} | {c.get('telefono','')} | "
                f"{c.get('email','')} | {c.get('estado','')}"
            )  # CAMBIO: uso get() para evitar KeyError si falta una clave

        print(f"Total: {len(self.clientes)}")
    
    def editar_cliente(self, id_cliente: str, **kwargs) -> None:
        for i, c in enumerate(self.clientes):
            if c["id"] == id_cliente:
                for clave, valor in kwargs.items():
                    if clave in Cliente.campos:
                        c[clave] = valor
                self._guardar()
                print(f"Cliente {id_cliente} editado.")
                return
        print("Cliente no encontrado.")

def main() -> None:
    gestor = GestorClientes()
    while True:
        print("\n1. Agregar | 2. Ver | 3. Editar | 0. Salir")
        op = input("Opción: ")
        if op == "1":
            gestor.agregar_cliente(
                nombre=input("Nombre: "),
                telefono=input("Teléfono: "),
                email=input("Email: ")
            )
        elif op == "2":
            gestor.ver_clientes()
        elif op == "3":
            id_edit = input("ID a editar: ")
            print("Campos: nombre, telefono, email, estado")
            cambios = {}
            for campo in ["nombre", "telefono", "email", "estado"]:
                val = input(f"{campo.capitalize()}: ").strip()
                if val:
                    cambios[campo] = val
            gestor.editar_cliente(id_edit, **cambios)
        elif op == "0":
            break

if __name__ == "__main__":
    main()