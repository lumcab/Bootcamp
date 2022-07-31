abstract class Vehiculo {
        private String tipo;
        private int velocidadMaxima;
        private String tipoCombustible;
        private String matricula;

        String sonido;

    public String getTipo() {
        return tipo;
    }

    public void setTipo(String tipo) {
        this.tipo = tipo;
    }

    public int getVelocidadMaxima() {
        return velocidadMaxima;
    }

    public void setVelocidadMaxima(int velocidadMaxima) {
        this.velocidadMaxima = velocidadMaxima;
    }

    public String getTipoCombustible() {
        return tipoCombustible;
    }

    public void setTipoCombustible(String tipoCombustible) {
        this.tipoCombustible = tipoCombustible;
    }

    public String getMatricula() {
        return matricula;
    }

    public void setMatricula(String matricula) {
        this.matricula = matricula;
    }

    abstract String getSonido(); //funcion abtracta
    abstract void setSonido(String sonido); //funcion abtracta
}
 class Coche extends Vehiculo{
    byte puertas = 1;
    public void diHola(){
        System.out.println("Hola desde Coche");
    }
    public byte puertasCoche() {
        this.puertas++;
        //System.out.println(puertas);
        return puertas;
            }
     public String getSonido() {
         return "Sonido coche " + sonido;
     }
     public void setSonido(String sonido) {
         this.sonido = sonido;
     }
}
class motoElectrica extends Vehiculo{
    public String getSonido() {
        return "Sonido moto " + sonido;
    }
    public void setSonido(String sonido) {
        this.sonido = sonido;
    }
}
class Motor extends Coche {
    public void diHola(){
        System.out.println("Hola desde Motor");
    }
}

