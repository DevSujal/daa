class mySolution {
    public boolean isunique(int i, String sub, char subchar){
        if(i >= sub.length()){
            return true;
        }
        if(sub.charAt(i) == subchar){
            return false;
        }
        return isunique(i+1, sub, subchar);
    }

    public String lenOfSubstring(String s){
        String sub = "", temp = "";
        for(int i = 0; i < s.length(); i++){
            char subchar = s.charAt(i);
            if(isunique(0, sub, subchar)){
                sub +=  subchar;
            }else{
                if(sub.length() > temp.length()){
                    temp = sub;
                }
                sub = "";
                sub += s.charAt(i-1);
                i--;
            }
            System.out.println(sub);
        }
        return sub.length() > temp.length() ? sub : temp;
    }
    public int lengthOfLongestSubstring(String s) {
        return lenOfSubstring(s).length();
    }
    public static void main(String[] args) {
        mySolution sol = new mySolution();
        System.out.println(sol.lengthOfLongestSubstring("dvdf")); 
    }
}