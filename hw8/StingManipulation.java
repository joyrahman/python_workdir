import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;

/**
 * Created with IntelliJ IDEA.
 * User: Sharif
 * Date: 3/26/14
 * Time: 4:20 AM
 * To change this template use File | Settings | File Templates.
 */
public class StingManipulation {
    public static String source = null;
    public static String target = null;
    public static int[] optimal;

    public static void main(String args[]) {
        ReadInput();
        System.out.print(" ");
//        for (int i = 0; i < source.length(); i++) {
//            System.out.print(" " + source.charAt(i));
//        }
//        System.out.println();
        optimal = new int[source.length() + 1];
        for (int i = 1; i < source.length() + 1; i++) {
            int min = 999999;
            for (int j = 0; j < i; j++) {
                int costWithFlip = 1 + EditDistance(source.substring(j, i), new StringBuffer(target.substring(j, i)).reverse().toString())+optimal[j];
                int costNoFlip = EditDistance(source.substring(j, i), target.substring(j, i))+optimal[j];
                if(min>costWithFlip){
                    min=costWithFlip;
                }
                if(min>costNoFlip){
                    min=costNoFlip;
                }
		System.out.println(i+" "+j+" "+min+" "+costWithFlip+" "+costNoFlip);
            }
            optimal[i]=min;
            //System.out.println("min"+min);
        }
        System.out.println("source: " + source);
        System.out.println("target: " + target);
        System.out.println("Operation: " + optimal[source.length()]);


    }

    private static int EditDistance(String s, String d) {
        int distance = 0;
        for (int i = 0; i < s.length(); i++) {
            if (s.charAt(i) != d.charAt(i)) {
                distance++;
            }

        }
        return distance;
    }

    private static void ReadInput() {
        File inputFile;
//        String fileName = (args[0] == null) ? "example.txt" : args[0];
        inputFile = new File("example.txt");

        BufferedReader reader = null;

        try {
            reader = new BufferedReader(new FileReader(inputFile));
            String line = null;
            int i = 1;
            while ((line = reader.readLine()) != null) {
                if (i == 1) {
                    source = line.substring(3);
                    i++;
                } else {
                    target = line.substring(3);
                }
            }
            reader.close();
        } catch (Exception e) {

            e.printStackTrace();
        }
    }
}
