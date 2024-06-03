class Solution {
    public static int maxUnits(int storage_capacity, int [][]profitWeight){
       int  n = profitWeight.length;
       int post;
       for (int i = 0; i < n - 1; i++) {
           post = i;
           for (int j = i + 1; j < n; j++)
               if(profitWeight[j][1] > profitWeight[post][1]){

                   post = j;
               }
   
           if(post != i){

              int temp[] = profitWeight[i];
              profitWeight[i] = profitWeight[post];
              profitWeight[post] = temp;
           }
       }
        int profit = 0;
    
        for (int i = 0; i < n; i++){

            if(profitWeight[i][0]  <= storage_capacity){

                profit += profitWeight[i][1] * profitWeight[i][0];
                storage_capacity -=  profitWeight[i][0];
            }
            else{
                profit +=  profitWeight[i][1] * storage_capacity;
                break;
            }
        }
    
        return profit;
    }
    public int maximumUnits(int[][] boxTypes, int truckSize) {
        return maxUnits(truckSize, boxTypes);
    }
}





