import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.HashMap;

public class MorphologicalParser{
    /**
    * Takes the parsed Inuktitut phrases and writes the morpholocical parse to file.
    * Uses the morphological parser from Uqailaut Inuktitut parser.
    */
    public static void main(String[] args){
    	DonneesLinguistiquesAbstract.init();
        BufferedReader reader;
        BufferedWriter writer;
        try{
            reader = new BufferedReader(new FileReader("../Inuktitut_Parsed.txt"));
            writer = new BufferedWriter(new FileWriter("../Morph_Parsed.txt", true));
            String line = reader.readLine();
            HashMap<String, String> memo = new HashMap<String, String>();
            while(line != null){
                String[] splitline = line.trim().replace(",", " ").split(" ");
                String morph = "";
                for(String word : splitline){
                    System.out.println(word);
                    String parse;
                    if(memo.containsKey(word)){
                        parse = memo.get(word);
                    }
                    else{
                        try{
                            parse = Decomposer.decomposeToArrayOfStrings(word.toLowerCase())[0];
                        }
                        catch(Exception e){
                            parse = word;
                        }
                    }
                    memo.put(word, parse);
                    morph = morph + " " + parse;
                }
                writer.append(morph + "\n");
                line = reader.readLine();
            }
            reader.close();
            writer.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
}
