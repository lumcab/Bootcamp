public class Tarea4 {
    public static void main(String[] args){
        Cliente cliente = new Cliente();
        cliente.setNombre("Aleja");
        cliente.setEdad((byte)28);
        cliente.setTelefono(573216064583L);
        cliente.setCredito(500000);
        System.out.println("Nombre: " + cliente.getNombre());
        System.out.println("Edad: " + cliente.getEdad());
        System.out.println("Telefono: " + cliente.getTelefono());
        System.out.println("Credito: " + cliente.getCredito());
        Trabajador trabajador = new Trabajador();
        trabajador.setNombre("Aleja");
        trabajador.setEdad((byte)28);
        trabajador.setTelefono(573216064583L);
        trabajador.setSalario(1000000);
        System.out.println("Nombre: " + trabajador.getNombre());
        System.out.println("Edad: " + trabajador.getEdad());
        System.out.println("Telefono: " + trabajador.getTelefono());
        System.out.println("Salario: " + trabajador.getSalario());
    }
}

