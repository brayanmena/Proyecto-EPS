public class PrecioTotal {
    // atributos
    private double totalPrecios;
    private double totalCaja;
    private double totalDocumento;
    private Mercancia Mercancia[];
    double valor;
    double valorDoc;

    // constructor
    public PrecioTotal(Mercancia mercancia[]) {
        this.Mercancia = mercancia;
    }

    // metodos
    public void calcularTotales() {
        for (int i = 0; i < Mercancia.length; i++) {

            if (Mercancia[i].getClass() == Caja.class) {
                valor += Mercancia[i].calcularPrecio();
                this.totalCaja = valor;
            } else if (Mercancia[i].getClass() == Documento.class) {
                valorDoc += Mercancia[i].calcularPrecio();
                this.totalDocumento = valorDoc;
            }
        }
        this.totalPrecios = totalCaja + totalDocumento;
    }

    public void mostrarTotales() {

        calcularTotales();
        System.out.println("Total Mercancía " + totalPrecios);
        System.out.println("Total Cajas " + totalCaja);
        System.out.println("Total Documentos " + totalDocumento);
    }
}