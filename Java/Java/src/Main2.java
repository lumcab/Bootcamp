public class Main2 {
    public static void main(String[] args) {
        System.out.print("Numero de puertas: ");
        Coche añadirPuerta = new Coche();
        añadirPuerta.puertasCoche();
        System.out.println(añadirPuerta.puertas);
        añadirPuerta.puertasCoche();
        System.out.print("Numero de puertas: ");
        System.out.println(añadirPuerta.puertas);
        añadirPuerta.puertasCoche();
        System.out.print("Numero de puertas: ");
        System.out.println(añadirPuerta.puertas);
        System.out.println(" ");
        int result = suma(2, 3, 4);
        System.out.print("resultado: ");
        System.out.println(result);
    /*primer mensaje en un programa
    de varias lineas
     */
        //mensaje de una linea

    }
    public static int suma( int a, int b, int c){
        return a+b+c;
    }
}


