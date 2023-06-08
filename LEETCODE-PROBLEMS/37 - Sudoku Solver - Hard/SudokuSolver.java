public class SudokuSolver {
    private int rec;

    private boolean validate_n(int[][] matrix, int y, int x, int n) {
        for (int i = 0; i < 9; i++) { // Check row
            if (matrix[y][i] == n) { return false; }
        }
        for (int i = 0; i < 9; i++) { // Check column
            if (matrix[i][x] == n) { return false; }
        }
        int x0 = (x / 3) * 3;
        int y0 = (y / 3) * 3;
        for (int i = 0; i < 4; i++) {
            for (int j = 0; j < 4; j++) {
                if (matrix[y0 + i][x0 + j] == n) { return false; }
            }
        }
        return true;
    }
    
    public void solve(int[][] matrix) {
        rec++;
        for (int y = 0; y < 9; y++) {
            for (int x = 0; x < 9; x++) {
                for (int n = 1; n < 10; n++) {
                    if (validate_n(matrix, y, x, x)) {
                        matrix[y][x] = n;
                        solve(matrix);
                        matrix[y][x] = 0;
                    }
                } return;
            }
        }
    }
}
