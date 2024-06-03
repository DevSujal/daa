import java.io.BufferedReader;
import java.io.InputStreamReader;

public class overtakeProblemHackerearth {
    public static long findNumberOfOvertakes(int n, int velocity[]) {
        return divide(velocity, 0, n - 1);
    }

    public static long divide(int arr[], int first, int last) {
        long count = 0;
        if (first < last) {
            int mid = (first + last) / 2;
            count = divide(arr, first, mid) + divide(arr, mid + 1, last) + merge(arr, first, mid, last);
        }
        return count;
    }

    public static long merge(int arr[], int first, int mid, int last) {
        int newArr[] = new int[last - first + 1];
        int x1 = first;
        int x2 = mid + 1;
        int x = 0;
        long count = 0;
        while (x1 <= mid && x2 <= last) {
            if (arr[x1] <= arr[x2]) {
                newArr[x++] = arr[x1++];
            } else {
                newArr[x++] = arr[x2++];
                count += (mid - x1 + 1);
            }
        }
        while (x1 <= mid)
            newArr[x++] = arr[x1++];

        while (x2 <= last)
            newArr[x++] = arr[x2++];

        for (int i = first; i <= last; i++) {
            arr[i] = newArr[i - first];
        }
        return count;
    }

    public static void main(String args[]){
        // BufferedReader
        try (
                BufferedReader br = new BufferedReader(new InputStreamReader(System.in))) {

            int n = Integer.parseInt(br.readLine());
            String velocity[] = br.readLine().split(" ");
            String position[] = br.readLine().split(" ");
            int horse_velocity[] = new int[n];
            for (int i = 0; i < n; i++) {
                horse_velocity[Integer.parseInt(position[i]) - 1] = Integer.parseInt(velocity[i]);
            }
            System.out.println(findNumberOfOvertakes(n, horse_velocity));
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}
