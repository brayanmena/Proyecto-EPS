public class Caja extends Mercancia {
    // constantes
    private static final double CAPACIDAD = 8.0;

    // atributos

    // constructores
    public Caja(double peso, double tamanio) {
        super(peso, tamanio);

    }

    public Caja(double precioBase) {
        super(precioBase);
    }

    public Caja() {
        super.getpeso();
        super.gettamanio();
    }

    // metodos
    public double calcularPrecio() {
        double precioFinal = (super.getprecioBase() + (super.getpeso() * super.gettamanio() * CAPACIDAD));
        return precioFinal;
    }

    public double getCAPACIDAD() {
        return CAPACIDAD;
    }
}