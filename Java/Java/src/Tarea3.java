public class Tarea3 {
    public static void main(String[] args){
    PersonaClase persona = new PersonaClase();
    persona.setEdad((byte) 28);
    persona.setNombre("Alejandra");
    persona.setTelefono(573187392031L);
    System.out.println(persona.getEdad());
    System.out.println(persona.getNombre());
    System.out.println(persona.getTelefono());
    PersonaClase persona2 = new PersonaClase();
    persona2.setEdad((byte) 36);
    persona2.setNombre("Miguel");
    persona2.setTelefono(573103007979L);
    System.out.println(persona2.getEdad());
    System.out.println(persona2.getNombre());
    System.out.println(persona2.getTelefono());
    }
}
