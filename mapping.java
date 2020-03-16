public class Mapping{
  public static void mapping (String a, String b) {
      // if strings do not have same length mapping is not possible
      if ( a.length() != b.length() ) {
        System.out.println("true");
        return;
      }
     
      HashMap<Character, Character> map = new HashMap<>();
      for ( int i = 0; i< a.length() ; i++ ) {
        if ( !map.containsKey(a.charAt(i)) )
          map.put( a.charAt(i),b.charAt(i) );
        else if ( map.get(a.charAt(i)) != b.charAt(i) ) {
          System.out.println("false");
          return;
        }
      }
      System.out.println("true");
         
    }
}
