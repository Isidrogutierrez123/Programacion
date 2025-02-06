<?php

class CuentaBancaria {
    public $titular;
    public $saldo;
    public $tipoDeCuenta;

    public function __construct($titular, $saldo, $tipoDeCuenta) {
        $this->titular = $titular;
        $this->saldo = $saldo;
        $this->tipoDeCuenta = $tipoDeCuenta;
    }

    public function depositar($cantidad) {
        $this->saldo += $cantidad;
        echo "Se han depositado {$cantidad} USD. Saldo actual: {$this->saldo} USD.
";
    }

    public function retirar($cantidad) {
        if ($cantidad <= $this->saldo) {
            $this->saldo -= $cantidad;
            echo "Se han retirado {$cantidad} USD. Saldo actual: {$this->saldo} USD.
";
        } else {
            echo "Fondos insuficientes para retirar {$cantidad} USD.
";
        }
    }

    public function mostrarInfo() {
        echo "Titular: {$this->titular}, Tipo de Cuenta: {$this->tipoDeCuenta}, Saldo: {$this->saldo} USD.
";
    }
}


$cuenta = new CuentaBancaria("Carlos", 1000, "Ahorros");
$cuenta->mostrarInfo();
$cuenta->depositar(500);
$cuenta->retirar(300);
$cuenta->retirar(1500);
$cuenta->mostrarInfo();

echo "
";

class Tarea {
    public $nombre;
    public $descripcion;
    public $fechaLimite;
    public $estado;

    public function __construct($nombre, $descripcion, $fechaLimite) {
        $this->nombre = $nombre;
        $this->descripcion = $descripcion;
        $this->fechaLimite = $fechaLimite;
        $this->estado = "pendiente";
    }

    public function marcarComoCompletada() {
        $this->estado = "completada";
    }

    public function editarDescripcion($nuevaDescripcion) {
        $this->descripcion = $nuevaDescripcion;
    }

    public function mostrarTarea() {
        echo "Tarea: {$this->nombre}, Descripción: {$this->descripcion}, Fecha Límite: {$this->fechaLimite}, Estado: {$this->estado}.
";
    }
}

$tareas = [
    new Tarea("Comprar víveres", "Ir al supermercado", "2025-01-20"),
    new Tarea("Estudiar PHP", "Repasar herencia y POO", "2025-01-22"),
];

$tareas[0]->marcarComoCompletada();
$tareas[1]->editarDescripcion("Practicar con ejercicios avanzados de POO");

foreach ($tareas as $tarea) {
    $tarea->mostrarTarea();
}

echo "
";

class Empleado {
    public $nombre;
    public $sueldo;
    public $aniosExperiencia;

    public function __construct($nombre, $sueldo, $aniosExperiencia) {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
        $this->aniosExperiencia = $aniosExperiencia;
    }

    public function calcularBonus() {
        return ($this->sueldo * 0.05) * floor($this->aniosExperiencia / 2);
    }

    public function mostrarDetalles() {
        echo "Empleado: {$this->nombre}, Sueldo: {$this->sueldo}, Años de Experiencia: {$this->aniosExperiencia}, Bonus: {$this->calcularBonus()} USD.
";
    }
}

class Consultor extends Empleado {
    public $horasPorProyecto;

    public function __construct($nombre, $sueldo, $aniosExperiencia, $horasPorProyecto) {
        parent::__construct($nombre, $sueldo, $aniosExperiencia);
        $this->horasPorProyecto = $horasPorProyecto;
    }

    public function calcularBonus() {
        $bonus = parent::calcularBonus();
        if ($this->horasPorProyecto > 100) {
            $bonus += 200; // Bonus adicional
        }
        return $bonus;
    }
}


$empleado = new Empleado("Luis", 3000, 6);
$consultor = new Consultor("Marta", 4000, 4, 120);

$empleado->mostrarDetalles();
$consultor->mostrarDetalles();

echo "
";


class Carrito {
    public $productos = [];

    public function agregarProducto($nombre, $precio, $cantidad) {
        $this->productos[] = ["nombre" => $nombre, "precio" => $precio, "cantidad" => $cantidad];
    }

    public function quitarProducto($nombre) {
        $this->productos = array_filter($this->productos, function ($producto) use ($nombre) {
            return $producto["nombre"] !== $nombre;
        });
    }

    public function calcularTotal() {
        $total = 0;
        foreach ($this->productos as $producto) {
            $total += $producto["precio"] * $producto["cantidad"];
        }
        return $total;
    }

    public function mostrarDetalleCarrito() {
        foreach ($this->productos as $producto) {
            echo "Producto: {$producto['nombre']}, Precio: {$producto['precio']} USD, Cantidad: {$producto['cantidad']}.
";
        }
    }
}

$carrito = new Carrito();
$carrito->agregarProducto("Manzanas", 2, 5);
$carrito->agregarProducto("Pan", 3, 2);
$carrito->mostrarDetalleCarrito();
echo "Total: {$carrito->calcularTotal()} USD.
";

$carrito->quitarProducto("Pan");
$carrito->mostrarDetalleCarrito();
echo "Total tras eliminar el pan: {$carrito->calcularTotal()} USD.
";

echo "
";

class Personaje {
    public $nombre;
    public $nivel;
    public $puntosVida;
    public $puntosAtaque;

    public function __construct($nombre, $nivel, $puntosVida, $puntosAtaque) {
        $this->nombre = $nombre;
        $this->nivel = $nivel;
        $this->puntosVida = $puntosVida;
        $this->puntosAtaque = $puntosAtaque;
    }

    public function atacar(Personaje $objetivo) {
        $objetivo->puntosVida -= $this->puntosAtaque;
        echo "{$this->nombre} ataca a {$objetivo->nombre} y le quita {$this->puntosAtaque} puntos de vida.
";
    }

    public function curarse() {
        $this->puntosVida += 10;
        echo "{$this->nombre} se cura y ahora tiene {$this->puntosVida} puntos de vida.
";
    }

    public function subirNivel() {
        $this->nivel++;
        $this->puntosAtaque += 5;
        $this->puntosVida += 20;
        echo "{$this->nombre} sube al nivel {$this->nivel}. Ataque: {$this->puntosAtaque}, Vida: {$this->puntosVida}.
";
    }
}


$jugador1 = new Personaje("Guerrero", 1, 100, 15);
$jugador2 = new Personaje("Mago", 1, 80, 20);

$jugador1->atacar($jugador2);
$jugador2->curarse();
$jugador1->subirNivel();

