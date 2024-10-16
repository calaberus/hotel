from datetime import datetime

# Clase Habitacion
class Habitacion:
    def __init__(self, numero, tipo):
        self.numero = numero
        self.tipo = tipo  # 'individual' o 'doble'
        self.disponible = True

    def __str__(self):
        estado = 'disponible' if self.disponible else 'reservada'
        return f'Habitación {self.numero} ({self.tipo}) está {estado}.'

# Clase Huesped
class Huesped:
    def __init__(self, nombre, identificacion):
        self.nombre = nombre
        self.identificacion = identificacion

    def __str__(self):
        return f'Huésped: {self.nombre} ({self.identificacion})'

# Clase Reserva
class Reserva:
    def __init__(self, huesped, habitacion, fecha_inicio, fecha_fin):
        self.huesped = huesped
        self.habitacion = habitacion
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.activa = True

    def __str__(self):
        return (f'Reserva para {self.huesped.nombre} en la habitación {self.habitacion.numero} '
                f'del {self.fecha_inicio.strftime("%d/%m/%Y")} al {self.fecha_fin.strftime("%d/%m/%Y")}. '
                f'Estado: {"activa" if self.activa else "finalizada"}')

# Clase Sistema de Reservas
class SistemaReservas:
    def __init__(self):
        self.habitaciones = []
        self.reservas = []

    def agregar_habitacion(self, numero, tipo):
        habitacion = Habitacion(numero, tipo)
        self.habitaciones.append(habitacion)

    def mostrar_habitaciones_disponibles(self):
        disponibles = [h for h in self.habitaciones if h.disponible]
        if disponibles:
            print("Habitaciones disponibles:")
            for habitacion in disponibles:
                print(habitacion)
        else:
            print("No hay habitaciones disponibles.")

    def realizar_reserva(self, huesped, numero_habitacion, fecha_inicio, fecha_fin):
        habitacion = next((h for h in self.habitaciones if h.numero == numero_habitacion and h.disponible), None)
        if habitacion:
            habitacion.disponible = False
            reserva = Reserva(huesped, habitacion, fecha_inicio, fecha_fin)
            self.reservas.append(reserva)
            print(f'Reserva exitosa:\n{reserva}')
        else:
            print(f'La habitación {numero_habitacion} no está disponible.')

    def cancelar_reserva(self, numero_habitacion):
        reserva = next((r for r in self.reservas if r.habitacion.numero == numero_habitacion and r.activa), None)
        if reserva:
            reserva.habitacion.disponible = True
            reserva.activa = False
            print(f'Reserva cancelada:\n{reserva}')
        else:
            print(f'No se encontró una reserva activa para la habitación {numero_habitacion}.')

# Crear sistema de reservas
sistema = SistemaReservas()

# Agregar habitaciones al sistema
sistema.agregar_habitacion(101, 'individual')
sistema.agregar_habitacion(102, 'doble')
sistema.agregar_habitacion(103, 'doble')

# Mostrar habitaciones disponibles
sistema.mostrar_habitaciones_disponibles()

# Crear un huésped
huesped1 = Huesped("Andres Sanchez", "2452841")

# Realizar una reserva
sistema.realizar_reserva(huesped1, 102, datetime(2024, 10, 14), datetime(2024, 10, 16))

# Mostrar habitaciones disponibles después de la reserva
sistema.mostrar_habitaciones_disponibles()

# Cancelar la reserva
sistema.cancelar_reserva(102)

# Mostrar habitaciones disponibles después de cancelar la reserva
sistema.mostrar_habitaciones_disponibles()
