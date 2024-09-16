import java.util.Scanner;
public class longword {
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        int max=0,s1=0,flag=0,i;
        for(i=0;i<s.length();i++){
            if(s.charAt(i)==' '){
                if(max<s1) {
                    max=s1;
                    flag =i-s1;
                }
                s1=0;
                continue;
            }
            s1++;
        }
        /*if(max<s1) {
            max=s1;
            flag =s.length()-s1;
        }*/
        char[] str= s.toCharArray();
        for(i=flag;i<=flag+max;i++){
            System.out.print(str[i]);
        }
    }
}