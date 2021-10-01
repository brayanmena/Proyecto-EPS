import java.util.Scanner;

public class App {
    public static void main(String[] args) throws Exception {
        System.out.println("Hola, mundo!");// Mostar texto en pantalla
        // "sc" es el objeto que permite acceder a los métodos de la clase Scanner
        Scanner sc = new Scanner(System.in);

        // Invocar el método "saludar"
        System.out.print("Digite el nombre: ");
        String nombre = sc.nextLine();
        System.out.println(saludar(nombre));

        // Invocar el método "dtnumero"
        System.out.print("Ingrese el número: ");
        int numero = sc.nextInt();
        System.out.println(dtnumero(numero));

        // Invocar el método "conversion_grados"
        System.out.print("Ingrese los grados centigrados: ");
        double c = sc.nextDouble();
        System.out.println("Grados Fahrenheit: " + conversion_grados(c));

        // Invocar el método "operador_condicional"
        System.out.print("Ingrese el número: ");
        int n = sc.nextInt();
        System.out.println(operador_condicional(n));
    }

    public static String saludar(String msg) {
        return "Hola " + msg + "!";
    }

    public static String dtnumero(int n) {
        return "Doble = " + (n * 2) + " Triple = " + (n * 3);
    }

    public static double conversion_grados(double c) {
        return 32 + (9 * (c / 5));
    }

    public static String operador_condicional(int n) {
        return n % 2 == 0 ? n + " es par" : n + " es impar";
        /*
         * String resultado = ""; if (n % 2 == 0){ resultado = n + " es par"; }else{
         * resultado = n + " es impar"; } return resultado;
         */
    }
}
