class Solution {

    public String encode(List<String> strs) {
        if (strs.isEmpty()){
            return null;
        }
        String encodedString = String.join(String.valueOf(Character.MIN_VALUE), strs);
        System.out.println(encodedString);
        return encodedString;
    }

    public List<String> decode(String str) {
        if (str == null){
            return List.of();
        }
        return Arrays.stream(str.split(String.valueOf(Character.MIN_VALUE), -1)).toList();
    }
}
