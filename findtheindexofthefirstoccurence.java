class Solutionn {
    public static int strStr(String haystack, String needle) {
        int size = needle.length();
        char[] arr = haystack.toCharArray();
        int maxsize = arr.length;
        System.out.println(maxsize);
        for(int i = 0; i < maxsize; i++){
            System.out.println(i);
            if(maxsize - i > size){
                return -1;
            }
            String temp = "";
            for(int j = i; j < size + i; j++){
                temp += arr[j];
                System.out.println(temp);
            }
            // System.out.println(temp);

            if(temp.equals(needle)){
                return i;
            }
        }
    return -1;
    }

    public static void main(String[] args) {
        System.out.println(strStr("sadbutsad", "sad"));
    }
}