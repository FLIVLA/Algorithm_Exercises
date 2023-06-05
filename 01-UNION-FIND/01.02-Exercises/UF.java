public class UF 
{
    private int[] id; // access to component id (site indexed)
    private int count; // number of components


    UF(int N) {
        count = N;
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    boolean connected(int p, int q) {
        return find(p) == find(q);
    }

    int count() {
        return count;
    }

    //#region QUICK FIND APPROACH

    /* The quick find method is quick bot not suited for
     * large problems, because union() has to scan through
     * the whole id[] for each input pair. */

    void union(int p, int q) {
        // put p and q into he same component.
        int pId = quickFind(p);
        int qId = quickFind(q);

        // nothing to do if p and q are already in the same component.
        if (pId == qId) return;

        // Rename p's component to q's name
        for (int i = 0; i < id.length; i++)
            if (id[i] == pId) id[i] = qId;
        count--;
    }

    int quickFind(int p) {
        return id[p];
    }

    //#endregion


    int find(int p) {
        return 0;
    }
}