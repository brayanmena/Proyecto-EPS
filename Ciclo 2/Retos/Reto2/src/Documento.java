public class Documento extends Mercancia {
    // constantes
    private static final int TIEMPO = 2;

    // atributos

    // constructores
    public Documento(double peso, double tamanio) {
        super(peso, tamanio);
    }

    public Documento(double peso) {
        super.setpeso(peso);
    }

    public Documento() {
        super.getpeso();
        super.gettamanio();
    }

    // metodos
    public double calcularPrecio() {
        double precioFinal = (super.getprecioBase() + (super.getpeso() * super.gettamanio() * TIEMPO));
        return precioFinal;
    }

    public double getTIEMPO() {
        return TIEMPO;
    }
}
