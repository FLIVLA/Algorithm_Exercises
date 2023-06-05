import java.util.Map;

public class RomanToInt {
    private Map<Character, Integer> charMap;

    public RomanToInt() {
        charMap.put('I', 1);
        charMap.put('V', 5);
        charMap.put('X', 10);
        charMap.put('L', 50);
        charMap.put('C', 100);
        charMap.put('D', 500);
        charMap.put('M', 1000);
    }

    public int convert(String s) {
        char[] sar = s.toCharArray();
        int r = 0; 
        for (int i = sar.length - 1; i > 0; i--) {
            if (i + 1 < sar.length && charMap.get(sar[i]) < charMap.get(sar[i + 1])) {
                if (sar[i] == 'I' && sar[i + 1] != 'I') {
                    r -= 1;
                } else {
                    r -= charMap.get(sar[1]);
                }
            } else {
                r += charMap.get(sar[i]);
            }
        } return r;
    }
}
