<?php


class Persona {
    public $nombre;
    public $edad;
    public $genero;

    public function __construct($nombre, $edad, $genero) {
        $this->nombre = $nombre;
        $this->edad = $edad;
        $this->genero = $genero;
    }

    public function presentar() {
        echo "Hola, mi nombre es {$this->nombre}, tengo {$this->edad} años y soy {$this->genero}.
";
    }
}


$persona = new Persona("Juan", 30, "masculino");
$persona->presentar();

echo "
";

class Rectangulo {
    public $base;
    public $altura;

    public function __construct($base, $altura) {
        $this->base = $base;
        $this->altura = $altura;
    }

    public function calcularArea() {
        return $this->base * $this->altura;
    }
}


$rectangulo = new Rectangulo(10, 5);
echo "El área del rectángulo con base {$rectangulo->base} y altura {$rectangulo->altura} es: " . $rectangulo->calcularArea() . ".
";

echo "
";


class Animal {
    public $especie;

    public function __construct($especie) {
        $this->especie = $especie;
    }

    public function emitirSonido() {
        echo "Este animal hace un sonido genérico.
";
    }
}

class Perro extends Animal {
    public $raza;

    public function __construct($especie, $raza) {
        parent::__construct($especie);
        $this->raza = $raza;
    }

    public function emitirSonido() {
        echo "Guau guau! Soy un {$this->raza}.
";
    }
}


$perro = new Perro("mamífero", "Golden Retriever");
$perro->emitirSonido();

echo "
";


class Producto {
    public $nombre;
    public $precio;

    public function __construct($nombre, $precio) {
        $this->nombre = $nombre;
        $this->precio = $precio;
    }

    public function mostrarDetalles() {
        echo "Producto: {$this->nombre}, Precio: {$this->precio} USD.
";
    }
}

class Electrodomestico extends Producto {
    public $consumo;

    public function __construct($nombre, $precio, $consumo) {
        parent::__construct($nombre, $precio);
        $this->consumo = $consumo;
    }

    public function mostrarDetalles() {
        echo "Electrodoméstico: {$this->nombre}, Precio: {$this->precio} USD, Consumo: {$this->consumo} kWh.
";
    }
}


$producto = new Producto("Libro", 20);
$producto->mostrarDetalles();

$electrodomestico = new Electrodomestico("Refrigerador", 500, 150);
$electrodomestico->mostrarDetalles();

echo "
";


class ConversorMoneda {
    private $factorDolarAEuro = 0.85;
    private $factorEuroADolar = 1.18;

    public function convertirDolaresAEuros($dolares) {
        return $dolares * $this->factorDolarAEuro;
    }

    public function convertirEurosADolares($euros) {
        return $euros * $this->factorEuroADolar;
    }
}


$conversor = new ConversorMoneda();
$dolares = 100;
$euros = 85;
echo "{$dolares} USD son " . $conversor->convertirDolaresAEuros($dolares) . " EUR.
";
echo "{$euros} EUR son " . $conversor->convertirEurosADolares($euros) . " USD.
";

