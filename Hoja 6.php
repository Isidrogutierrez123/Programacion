<?php


class Libro {
    public $titulo;
    public $autor;
    public $numeroPaginas;

    public function __construct($titulo, $autor, $numeroPaginas) {
        $this->titulo = $titulo;
        $this->autor = $autor;
        $this->numeroPaginas = $numeroPaginas;
    }

    public function mostrarInfo() {
        echo "Título: {$this->titulo}, Autor: {$this->autor}, Número de páginas: {$this->numeroPaginas}.
";
    }
}


$libro = new Libro("1984", "George Orwell", 328);
$libro->mostrarInfo();

echo "
";


class Circulo {
    public $radio;

    public function __construct($radio) {
        $this->radio = $radio;
    }

    public function calcularArea() {
        return pi() * pow($this->radio, 2);
    }
}


$circulo = new Circulo(5);
echo "El área del círculo con radio {$circulo->radio} es: " . $circulo->calcularArea() . ".
";

echo "
";


class Vehiculo {
    public $marca;

    public function __construct($marca) {
        $this->marca = $marca;
    }

    public function encender() {
        echo "El vehículo de marca {$this->marca} está encendido.
";
    }
}

// Clase hija "Coche"
class Coche extends Vehiculo {
    public $modelo;

    public function __construct($marca, $modelo) {
        parent::__construct($marca);
        $this->modelo = $modelo;
    }

    public function mostrarDetalles() {
        echo "Marca: {$this->marca}, Modelo: {$this->modelo}.
";
    }
}

$coche = new Coche("Toyota", "Corolla");
$coche->encender();
$coche->mostrarDetalles();

echo "
";


class Empleado {
    public $nombre;
    public $sueldo;

    public function __construct($nombre, $sueldo) {
        $this->nombre = $nombre;
        $this->sueldo = $sueldo;
    }

    public function mostrarDetalles() {
        echo "Empleado: {$this->nombre}, Sueldo: {$this->sueldo}.
";
    }
}


class Gerente extends Empleado {
    public $departamento;

    public function __construct($nombre, $sueldo, $departamento) {
        parent::__construct($nombre, $sueldo);
        $this->departamento = $departamento;
    }

    public function mostrarDetalles() {
        echo "Gerente: {$this->nombre}, Sueldo: {$this->sueldo}, Departamento: {$this->departamento}.
";
    }
}


$empleado = new Empleado("Juan", 3000);
$empleado->mostrarDetalles();

$gerente = new Gerente("Ana", 5000, "Recursos Humanos");
$gerente->mostrarDetalles();

echo "
";


class Calculadora {

    public function sumar($a, $b) {
        return $a + $b;
    }

    public function restar($a, $b) {
        return $a - $b;
    }

    public function multiplicar($a, $b) {
        return $a * $b;
    }

    public function dividir($a, $b) {
        if ($b == 0) {
            return "Error: División por cero.";
        }
        return $a / $b;
    }
}


$calculadora = new Calculadora();
echo "Suma: " . $calculadora->sumar(10, 5) . ".
";
echo "Resta: " . $calculadora->restar(10, 5) . ".
";
echo "Multiplicación: " . $calculadora->multiplicar(10, 5) . ".
";
echo "División: " . $calculadora->dividir(10, 5) . ".
";
echo "División por cero: " . $calculadora->dividir(10, 0) . ".
";
