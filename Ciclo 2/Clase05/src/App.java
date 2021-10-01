import javax.swing.JOptionPane;

public class App {
    public static void main(String[] args) throws Exception {
        JOptionPane.showMessageDialog(null, "Hola!! Grupo #32");

        String nombre = JOptionPane.showInputDialog("Ingrese su nombre...");
        JOptionPane.showMessageDialog(null, "Nombre: " + nombre + "!.");

        int numero1 = Integer.parseInt(JOptionPane.showInputDialog("Digite un número: "));
        double numero2 = Integer.parseInt(JOptionPane.showInputDialog("Digite otro número: "));

        JOptionPane.showMessageDialog(null,
                "El numero_1 ingresado es: " + numero1 + " y el segundo numero es: " + numero2);
        JOptionPane.showMessageDialog(null, "La suma es: " + (numero1 + numero2));
        JOptionPane.showMessageDialog(null, "La resta es: " + (numero1 - numero2));
        JOptionPane.showMessageDialog(null, "La multiplicación es: " + (numero1 * numero2));
        JOptionPane.showMessageDialog(null, "La división es: " + (numero1 / numero2));
    }
}
