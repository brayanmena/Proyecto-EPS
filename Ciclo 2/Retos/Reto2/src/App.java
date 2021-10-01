public class App {
    public static void main(String[] args) throws Exception {
        Mercancia mercancia[] = new Mercancia[5];
        mercancia[0] = new Caja(100.0, 10.0);
        mercancia[1] = new Caja(200);
        mercancia[2] = new Documento(150, 20.0);
        mercancia[3] = new Documento();
        mercancia[4] = new Caja();
        PrecioTotal solucion = new PrecioTotal(mercancia);
        solucion.mostrarTotales();
    }
}