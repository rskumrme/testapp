public class Test {
  public static void main(String[] args) {
    String txt = "Hello " + "World";
    System.out.println(txt.toUpperCase());   // Outputs "HELLO WORLD"
    System.out.println(txt.toLowerCase());   // Outputs "hello world"

    String txt = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    System.out.println("The length of the txt string is: " + txt.length());
  }
}
