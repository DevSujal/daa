import java.io.BufferedReader;
import java.io.InputStreamReader;

class TestClass {
    public static long findNumberOfOvertakes(int n, int velocity[]) {
        long numberOfOvertakes = 0;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (velocity[i] > velocity[j]) {
                    numberOfOvertakes++;
                }
            }
        }
        return numberOfOvertakes;
    }

    public static void main(String args[]) {
        // BufferedReader
        try (
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in));) {

            int n = Integer.parseInt(br.readLine());

            String velString[] = br.readLine().split(" ");
            String posString[] = br.readLine().split(" ");
            int velocity[] = new int[n];
            int position[] = new int[n];
            int horse_velocity[] = new int[n];
            for (int i = 0; i < n; i++) {
                velocity[i] = Integer.parseInt(velString[i]);
                position[i] = Integer.parseInt(posString[i]);
                horse_velocity[position[i] - 1] = velocity[i];
            }
            System.out.println(findNumberOfOvertakes(n, horse_velocity));
        }

        catch (Exception e) {
            System.out.println("An Exception Occured");
        }
    }
}
