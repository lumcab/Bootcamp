public class Main {
    public static void main(String[] args) {
        Coche coche = new Coche(); //heredada o extendida
        coche.setTipo("Coupe");
        System.out.println(coche.getTipo());
        coche.setVelocidadMaxima(120);
        coche.setTipoCombustible("Gasolina");
        coche.setMatricula("ABC123");
        System.out.println("Puertas = " + coche.puertasCoche());
        coche.setSonido("BRRR"); //funcion abtracta
        System.out.println("Velocidad maxima " + coche.getVelocidadMaxima());
        System.out.println("Tipo de combustible " + coche.getTipoCombustible());
        System.out.println("Matricula " + coche.getMatricula());

        motoElectrica moto = new motoElectrica(); //heredada o extendida
        moto.setTipo("Scutter");
        System.out.println(moto.getTipo());
        moto.setVelocidadMaxima(70);
        moto.setTipoCombustible("Electrica");
        moto.setMatricula("ABC12A ");
        moto.setSonido("null"); //funcion abtracta
        System.out.println("Velocidad maxima " + moto.getVelocidadMaxima());
        System.out.println("Tipo de combustible " + moto.getTipoCombustible());
        System.out.println("Matricula " + moto.getMatricula());
        System.out.println(moto.getSonido());

        Motor motor = new Motor();
        motor.diHola();
    }
}