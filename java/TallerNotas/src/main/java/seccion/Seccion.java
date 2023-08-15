package seccion;

public class Seccion {

    private int numEstudiantes;
    private double sumaPromedio;
    
    // Seccion(int numEstudiantes): constructor de la clase que inicializa la cantidad de estudiantes y la suma de promedios.

    public Seccion(int numEstudiantes) {
        this.numEstudiantes = numEstudiantes;
        this.sumaPromedio = 0;
    }
    
    // agregarPromedio(double promedio): método que recibe un promedio y lo agrega a la suma de promedios de la sección.
    // de cada estudiante

    public void agregarPromedio(double promedio) {
        this.sumaPromedio += promedio;
    }
    
    // promedioGeneral(): método que calcula el promedio general de la sección, es decir, el promedio de todos los promedios 
    // de los estudiantes en la sección.

    public double promedioGeneral() {
        return this.sumaPromedio / this.numEstudiantes;
    }
    
    // esto son los getters para obtener los valores de los atributos

    public int getNumEstudiantes() {
        return numEstudiantes;
    }

    public double getSumaPromedio() {
        return sumaPromedio;
    }

}
