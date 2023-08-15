package estudiantes;

import asigntaturas.Asignatura;
import java.util.Arrays;

public class Estudiante {

    private String nombreEstudiante;
    private double promedioNotaFinal;
    private byte asignaturasAprobadas;
    private byte asignaturasPerdidas;

    public Estudiante(String nombreEstudiante, Asignatura[] asignaturas, double promedioNotaFinal, byte asignaturasAprobadas, byte asignaturasPerdidas) {
        this.nombreEstudiante = nombreEstudiante;

        this.promedioNotaFinal = promedioNotaFinal;
        this.asignaturasAprobadas = asignaturasAprobadas;
        this.asignaturasPerdidas = asignaturasPerdidas;
    }

    public String getNombreEstudiante() {
        return nombreEstudiante;
    }


    public double getPromedioNotaFinal() {
        return promedioNotaFinal;
    }

    public byte getAsignaturasAprobadas() {
        return asignaturasAprobadas;
    }

    public byte getAsignaturasPerdidas() {
        return asignaturasPerdidas;
    }

    @Override
    public String toString() {
        return "Estudiante{" + "nombreEstudiante=" + nombreEstudiante + ", asignaturas=" + Arrays.toString(asignaturas) + ", promedioNotaFinal=" + promedioNotaFinal + ", asignaturasAprobadas=" + asignaturasAprobadas + ", asignaturasPerdidas=" + asignaturasPerdidas + '}';
    }

}
