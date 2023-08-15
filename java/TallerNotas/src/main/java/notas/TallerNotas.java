package notas;

import asigntaturas.Asignatura;
import estudiantes.Estudiante;
import estudiantes.MenuEstudiante;
import java.util.Scanner;
import seccion.Seccion;

public class TallerNotas {

    // Este es el array con las 5 asignaturas que vemos, como dijo el profesor de crear con los nombres
    // y solo preguntar las notas
    static String[] listaDeAsignaturasQueVemos = {
        "Ingles",
        "Calculo", 
        "Fisica",
        "Programación",
        "Estadistica"
    };

    public static void main(String[] args) {

        // instanciamos la clase MenuEstudiantes que es donde estan todos los metodos creados
        // como el de cargarDatosDelArchivoTXT(Los estudiantes), calcularCantidadAprobados
        // calcularPromedio (este es calcular el promedio de cada asignatura)
        // agregarNotasEstudiantes etc...
        MenuEstudiante estudiantes = new MenuEstudiante();

        // instanciamos la clase Seccion, este pide por parametros la cantidad de estudiantes en la sección
        // aqui estan todos los metodos necesarios, agregarPromedio (aqui agregamos los promedios de cada estudiante)
        // promedioGeneral (cuando tenemos todos los promedios de los estudiantes, sacamos el general de la sección)
        Seccion seccion = new Seccion(estudiantes.cantidadEstudiantes());

      

        Scanner entrada = new Scanner(System.in);

        // Recorremos el array de estudiantes con un forEach, este contiene todo los nombres de los estudiantes que obtuvimos
        // del archivo txt
        for (String estudiante : estudiantes.todosLosEstudiantesDelArchivoTXT()) {

            System.out.println("");
            System.out.println("Ingrese las notas de: " + estudiante);
            System.out.println("");

      
            int contador = 0;

            // Con este for recorremos el array de asignaturas que creamos arriba, que contiene las asignaturas que vemos.
            for (String asignatura : listaDeAsignaturasQueVemos) {

                try {

                    // pedimos las notas de cada asignatura, (auto evaluación, proyecto de aula, evaluación docente) con 
                    //una validación que valida que la nota debe de ser mayor a 0 y menos a 5.1
                    System.out.println("Ingrese la nota definitiva de auto evaluación: " + asignatura);

                    double notaAutoEvaluacion = entrada.nextDouble();

                    while (notaAutoEvaluacion < 0 || notaAutoEvaluacion >= 5.1) {

                        System.out.println("");
                        System.out.println("La nota de auto evaluación debe de ser mayor a 0 y menor a 5");
                        System.out.println("");

                        notaAutoEvaluacion = entrada.nextDouble();
                    }

                    System.out.println("Ingrese la nota definitiva de proyecto de aula: " + asignatura);

                    double notaProyectoAula = entrada.nextDouble();

                    while (notaProyectoAula < 0 || notaProyectoAula >= 5.1) {

                        System.out.println("");
                        System.out.println("La nota de proyecto de aula debe de ser mayor a 0 y menor a 5");
                        System.out.println("");

                        notaProyectoAula = entrada.nextDouble();
                    }

                    System.out.println("Ingrese la nota definitiva de la evaluación docente: " + asignatura);

                    double notaEvaluacionDocente = entrada.nextDouble();

                    while (notaEvaluacionDocente < 0 || notaEvaluacionDocente >= 5.1) {

                        System.out.println("");
                        System.out.println("La nota de evaluación docente debe de ser mayor a 0 y menor a 5");
                        System.out.println("");

                        notaEvaluacionDocente = entrada.nextDouble();
                    }

                    // Aqui sacamos el promedio de cada asignatura, sabiendo que la (auto evaluación value el 15%, 
                    // proyecto de aula vale el 25% y evaluación docente vale el 60%) y el resultado lo guardamos
                    // en la variable promedioCadaAsignatura
                    double promedioCadaAsignatura = (notaAutoEvaluacion * 0.15) + (notaProyectoAula * 0.25) + (notaEvaluacionDocente * 0.60);

                    // Utilizando la variable (promedioCadaAsignatura) hacemos una condición que nos dice que si el promedio 
                    // es mayor o igual a 3 significa que el estudiante gano la asignatura y a la hora de guardarla como vemos
                    // enviamos un true a una variable creada en asignatura llamada aproboLaMateria que es un boolean
                    // y si no significa que perdio y enviamos un false
                    if (promedioCadaAsignatura >= 3.0) {
                        listaAsignaturasDeUnEstudiante[contador] = new Asignatura(asignatura, notaAutoEvaluacion, notaProyectoAula, notaEvaluacionDocente, promedioCadaAsignatura, true);
                    } else {
                        listaAsignaturasDeUnEstudiante[contador] = new Asignatura(asignatura, notaAutoEvaluacion, notaProyectoAula, notaEvaluacionDocente, promedioCadaAsignatura, false);
                    }

                    contador++;

                } catch (Exception e) {

                    System.out.println("Error al ingresar una nota: " + e);
                    return;
                }

            }

            // promedioFinalEstudiante contiene el promedio final del estudiante con las 5 materias
            double promedioFinalEstudiante = estudiantes.calcularPromedio(listaAsignaturasDeUnEstudiante);

            // calcularCantidadAprobados es un array que en su posicion 1 contiene la cantidad de asignaturas aprobadas y reprobadas
            byte[] calcularCantidadAprobados = estudiantes.calcularCantidadAprobados(listaAsignaturasDeUnEstudiante);

            byte cuantasNotasAprobadas = calcularCantidadAprobados[0];
            byte cuantasNotasReprobadas = calcularCantidadAprobados[1];

            // Agregamos un nuevo estudiante con los datos necesarios
            estudiantes.agregarNotasEstudiantes(new Estudiante(estudiante, listaAsignaturasDeUnEstudiante, promedioFinalEstudiante, cuantasNotasAprobadas, cuantasNotasReprobadas));

            // Agregamos el promedio final del estudiante
            seccion.agregarPromedio(promedioFinalEstudiante);
        }

     
    }
}
