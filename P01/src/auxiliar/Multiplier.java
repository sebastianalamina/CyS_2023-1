package auxiliar;

/**
 * Clase auxiliar que se encargarán de hacer la multiplicación de matrices.
 */
public class Multiplier{

    // Va a tener como atributo un renglón (que pertenece a la matriz A) y una columna
    // (que pertenece a la matriz B). Se encarga de hacer el producto punto de estos dos 
    // elementos y guarda el resultado en el atributo pp.
    private int[] renglon;
    private int[] columna;
    public int pp;

    public Multiplier(int[] renglon, int[] columna) {
        this.renglon = renglon;
        this.columna = columna;
    }
    
    
    public void multiplica() {
        this.pp = Matrices.productoPunto(renglon, columna);
    }
}
