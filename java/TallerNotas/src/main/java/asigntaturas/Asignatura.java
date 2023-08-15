package asigntaturas;

public class Asignatura {

    private String nombreAsignatura;
    private double notaAutoEvalucion;
    private double notaProyectoAula;
    private double notaAprobacionDocente;


    public Asignatura(String nombreAsignatura, double notaAutoEvalucion, double notaProyectoAula, double notaAprobacionDocente, double promedioAsignatura, boolean aproboLaMateria) {
        this.nombreAsignatura = nombreAsignatura;
        this.notaAutoEvalucion = notaAutoEvalucion;
        this.notaProyectoAula = notaProyectoAula;
        this.notaAprobacionDocente = notaAprobacionDocente;

    }

    public String getNombreAsignatura() {
        return nombreAsignatura;
    }

    public double getNotaAutoEvalucion() {
        return notaAutoEvalucion;
    }

    public double getNotaProyectoAula() {
        return notaProyectoAula;
    }

    public double getNotaAprobacionDocente() {
        return notaAprobacionDocente;
    }


}
