public class Tarea2 {
    public static void main(String[] args) {
        int numerolf = 2;
        if (numerolf == 0) {
            System.out.println("el numero es Cero");

        } else if (numerolf >= 0) {
            System.out.println("el numero es Positivo");
        } else {
            System.out.println("el numero es Negativo");
        }

        int numeroWhile = -1;
        while (numeroWhile < 3) {
            System.out.println("el numero " + numeroWhile + " es menor a 3");
            numeroWhile++;
        }

        do {
            System.out.println("el numero " + numeroWhile + " es menor a 3");
        } while (numeroWhile > 3);

        int numeroFor = 0;
        for (;numeroFor <= 3;numeroFor++){
            System.out.println("valor de numeroFor es " + numeroFor);
        }
        var estacion = "Invierno";
        switch (estacion) {
            case "Primavera":
                System.out.println("La estacion es Primavera");
                break;
            case "Verano":
                System.out.println("La estacion es Verano");
                break;
            case "Invierno":
                System.out.println("La estacion es Invierno");
                break;
            default:
                System.out.println("La estacion es Otoño");
        }
    }
}

