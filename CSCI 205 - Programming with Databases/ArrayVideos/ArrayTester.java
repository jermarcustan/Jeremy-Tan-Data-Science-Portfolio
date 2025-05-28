public class ArrayTester {

    public static void main(String[] args) {
        int[] nums = new int[5];
        nums[0] = 6;
        nums[1] = 10;
        nums[2] = 7;
        nums[3] = 15;
        nums[4] = 3;
        
        for(int i = 0; i < nums.length; i++) {
            System.out.println(nums[i]);
        }

        for(int i = nums.length-1; i >= 0; i--) {
            System.out.println(nums[i]);
        }

        String[] words = new String[3];

        words[0]= "jer";
        words[1] = "banana";
        words[2] = "man";

        for(String word:words){
            System.out.println(word);
        }
    }
}