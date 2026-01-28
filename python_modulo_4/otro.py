class Libros:
    datos = ["id", "isbn", "titulo", "autor", "precio", "stock"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c))

    def sumar_stock(self, cantidad):
        if cantidad > 0:
            self.stock += cantidad



libro = Libros(id=1, isbn=12365489996325412, titulo= "un buen libro", autor= "Juan Rojas", precio= 17000, stock= 100)

print(libro.stock)


libro.sumar_stock(14)
print(libro.stock)
print(libro.__dict__)

print( "=" * 40)
print( "Marcos")
print( "=" * 40)

class Libro:
    datos = ["id_libro", "titulo", "autor", "isbn", "categoria", "precio", "stock", "estado"]
    
    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c, None))

    def actualizar_precio(self, nuevo_precio):
        self.precio = nuevo_precio

    def actualizar_stock(self, nuevo_stock):
        self.stock = nuevo_stock

    def stock_disponible(self):
        return self.stock > 0

    def mostrar_detalle(self):
        print(f"Libro: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}, Stock: {self.stock}")

print("Clase Libro cargada correctamente.")

libro = Libro(id_libro=1, titulo="1984", autor="George Orwell", isbn="1234567890", categoria="Ficción", precio=15.99, stock=10, estado="Nuevo")
print("Detalle completo del libro:")
print(libro.__dict__)

print("Detalles resumidos del libro:")
libro.mostrar_detalle()

print("Actualizando precio y stock...")
libro.actualizar_precio(10990)
libro.stock_disponible()
libro.actualizar_stock(15)
print(libro.__dict__)


'''print( "=" * 40)
print( "Mauricio")
print( "=" * 40)


class Libros:
    datos = ["id", "isbn", "titulo", "autor", "precio", "stock"]

    def __init__(self, **kwargs):
        for c in self.datos:
            setattr(self, c, kwargs.get(c))

    def disponibilidad(self):
        # True si hay stock disponible
        return (self.stock or 0) > 0

    def informacion(self):
        # Descripción breve del libro
        return f"Título: {self.titulo}, Autor: {self.autor}, Precio: {self.precio}, Stock: {self.stock}"

libro = Libros(
    id=1,
    isbn=123123,
    titulo="mishi hermosos",
    autor="Misha hermosa",
    precio=100000,  
    stock=15
)

print(libro.stock)            
print(libro.disponibilidad()) 
print(libro.informacion())'''




