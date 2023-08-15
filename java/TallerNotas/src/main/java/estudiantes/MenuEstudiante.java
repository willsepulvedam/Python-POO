package estudiantes;

import asigntaturas.Asignatura;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.ArrayList;

public class MenuEstudiante {

    /* "listaDeEstudiantesTXT": una lista (ArrayList) de cadenas de texto que representa los nombres 
    de los estudiantes cargados desde un archivo de texto. */
    ArrayList<String> listaDeEstudiantesTXT;
    
    /* "estudiantes": una lista de objetos de tipo "Estudiante" que se agregan mediante un método llamado 
    "agregarNotasEstudiantes". */
    ArrayList<Estudiante> estudiantes;

    public MenuEstudiante() {
        listaDeEstudiantesTXT = new ArrayList<>();
        estudiantes = new ArrayList<>();

        cargarDatosDelArchivoTXT();
    }
    
    /* "agregarNotasEstudiantes": recibe un objeto de tipo "Estudiante" y lo agrega a la lista "estudiantes". */

    public void agregarNotasEstudiantes(Estudiante nuevoEstudiante) {
        try {
            estudiantes.add(nuevoEstudiante);
        } catch (Exception e) {
            System.out.println("No se pudo agregar el estudiante");
        }
    }
    
    // mostrarDatosEstudiantes(): método que muestra los datos de todos los estudiantes guardados en la lista estudiantes.

    public void mostrarDatosEstudiantes() {
        for (Estudiante estudiante : estudiantes) {
            System.out.println(estudiante.toString());
        }
    }
    
    /* calcularPromedio(Asignatura[] asignaturas): método que calcula el promedio de las notas finales de un array de objetos 
    Asignatura, que se le envia por parametro desde la clase principal */

    public double calcularPromedio(Asignatura asignaturas) {

        double suma = 0;

        for (Asignatura asignatura : asignaturas) {
            suma += asignatura.getPromedioAsignatura();
        }

        double promedioNotaFinal = suma / 5;

        return promedioNotaFinal;
    }
    
    /* calcularCantidadAprobados(Asignatura[] asignaturas): método que calcula la cantidad de asignaturas aprobadas y reprobadas 
       de un array de objetos Asignatura, y devuelve un array de bytes con esa información, el primer lugar es el de las notas
       aprobadas y la segunda de las reprobadas */
    
     public byte[] calcularCantidadAprobados(Asignatura asignaturas) {
        byte numAprobados = 0;
        byte numReprobados = 0;
        
        for (Asignatura asignatura : asignaturas) {
            System.out.println(asignatura.isAproboLaMateria());
            if (asignatura.isAproboLaMateria()) {
                numAprobados++;
            } else {
                numReprobados++;
            }
        }
        
        byte[] cuantasAproboYReprobo = {numAprobados, numReprobados};
        
        return cuantasAproboYReprobo;
    }

     /* cargarDatosDelArchivoTXT() se encarga de cargar los datos de los estudiantes desde un archivo de texto y 
        almacenarlos en la lista listaDeEstudiantesTXT. */
     
    private void cargarDatosDelArchivoTXT() {
        try {
            File file = new File("listado-seccion4.txt");
            try ( FileReader reader = new FileReader(file)) {
                BufferedReader bufferedReader = new BufferedReader(reader);
                String line;
                while ((line = bufferedReader.readLine()) != null) {

                    listaDeEstudiantesTXT.add(line);

                }
            }
        } catch (IOException e) {
            System.out.println("Error: " + e);
        }
    }
    
    // todosLosEstudiantes(): método que devuelve la lista de estudiantes como una lista de cadenas de texto.

    public ArrayList<String> todosLosEstudiantesDelArchivoTXT() {
        return listaDeEstudiantesTXT;
    }
    
    // cantidadEstudiantes(): método que devuelve la cantidad de estudiantes en la lista listaDeEstudiantesTXT.
    
    public int cantidadEstudiantes() {
        return listaDeEstudiantesTXT.size();
    }
    
    // todosLosEstudiantesConSusNotas(): Retorna todo los estudiantes que guardamos con sus respectivas notas
    
    public ArrayList<Estudiante> todosLosEstudiantesConSusNotas() {
        return estudiantes;
    }

}
