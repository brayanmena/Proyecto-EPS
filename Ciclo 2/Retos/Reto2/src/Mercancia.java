public class Mercancia {
    // constantes
    private static final double PESO = 10.0;
    private static final double TAMANIO = 4.5;
    private static double PRECIO_BASE = 1000.0;

    // atributos
    private double peso = PESO;
    private double tamanio = TAMANIO;
    private double precioBase = PRECIO_BASE;

    // atributos
    public Mercancia(double peso, double tamanio) {
        this.peso = peso;
        this.tamanio = tamanio;
    }

    public Mercancia(double precioBase) {
        this.precioBase = precioBase;
    }

    public Mercancia() {

    }

    public double calcularPrecio() {
        return 0.0;
    }

    public double getpeso() {
        return peso;
    }

    public double gettamanio() {
        return tamanio;
    }

    public double getprecioBase() {
        return precioBase;
    }

    public void setpeso(double peso) {
        this.peso = peso;
    }

    public void settamanio(double tamanio) {
        this.tamanio = tamanio;
    }

}