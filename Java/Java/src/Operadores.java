public class Operadores {
    public static void main(String[] args){
        String n = "Variable"; //Variable
        System.out.println(n);

        System.out.println("Ejemplo de Ciclo For");
        byte a[] = {5,10,20,30,40}; //Array

        // for (int i : numeros) {    forma simple de escribir un for
        for (byte i = 0; i< a.length; i++){  //Ciclo for
            System.out.println("valor de la lista. " + a[i]);
        }
        System.out.println("Ejemplo de IF ELSE");
        int numerolf = 2;
        if (numerolf == 0) {
            System.out.println("el numero es Cero");

        }
        else if (numerolf >= 0){
            System.out.println("el numero es Positivo");
        }
        else{
            System.out.println("el numero es Negativo");
        }

        System.out.println("Ejemplo de Switch");
        var dia = "domingo";
        switch (dia) {
            case "lunes":
                System.out.println("Hoy se trabaja");
                break;
            case "martes":
                System.out.println("Hoy se trabaja");
                break;
            case "miercoles":
                System.out.println("Hoy se trabaja");
                break;
            case "jueves":
                System.out.println("Hoy se trabaja");
                break;
            case "viernes":
                System.out.println("Hoy se trabaja");
                break;
            case "sabado":
                System.out.println("Hoy se no trabaja");
                break;
                default:
                    System.out.println("Hoy se no trabaja");
        }
    }
}
