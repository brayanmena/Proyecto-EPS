import java.lang.Math;

public class CompraFlota {
    private int Tiempo;
    private double Capital;
    private double Interes;

    public String compararCompra(int pTiempo, double pCapital, double pInteres) {
        double 𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝑆𝑖𝑚𝑝𝑙𝑒 = pCapital * pInteres * pTiempo;
        double 𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝐶𝑜𝑚𝑝𝑢𝑒𝑠𝑡𝑜 = pCapital * ((Math.pow(1 + pInteres, pTiempo) - 1));
        double respuesta = 𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝐶𝑜𝑚𝑝𝑢𝑒𝑠𝑡𝑜 - 𝑖𝑛𝑡𝑒𝑟𝑒𝑠𝑆𝑖𝑚𝑝𝑙𝑒;

        if (pInteres == 0) {
            return "Faltan datos para calcular la diferencia en el total de intereses generados para el proyecto.";
        } else {
            return "La diferencia en el total de intereses generados para el proyecto, si escogemos entre evaluarlo a una tasa de interés Compuesto y evaluarlo a una tasa de interés Simple, asciende a la cifra de: $"
                    + respuesta;
        }
    }
}
