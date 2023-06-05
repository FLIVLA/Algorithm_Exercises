/** QUICK-FIND APPROACH FOR THE UNION FIND PROBLEM */
public class QuickFindUF {
    private int[] id;

    /** Set if of each object to itself 
     * (N array accesses)
     * @param N initial array length
     */
    public QuickFindUF(int N) {
        id = new int[N];
        for (int i = 0; i < N; i++) {
            id[i] = i;
        }
    }

    public boolean connected(int p, int q) {
        return id[p] == id[q];
    }

    /** UNION
     * change all entries with id[p] to id[q]
     * (at most 2N + 2 accesses)
     * @param p
     * @param q
     */
    public void union(int p, int q) {
        int pid = id[p];
        int qid = id[q];

        for (int i = 0; i < id.length; i++) {
            if (id[i] == pid) {
                id[i] = qid;
            }
        }
    }   
}
