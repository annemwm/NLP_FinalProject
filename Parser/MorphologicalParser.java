import applications.Decompose;
import data.LinguisticDataAbstract;
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
        int startPoint = 0;
        if(args.length > 0){
            try{
                startPoint = Integer.parseInt(args[0]);
            }
            catch(Exception e){}
        }
        LinguisticDataAbstract.init();
        BufferedReader reader;
        BufferedWriter writer;
        try{
            reader = new BufferedReader(new FileReader("../Inuktitut_Parsed.txt"));
            writer = new BufferedWriter(new FileWriter("../Morph_Parsed.txt", true));
            String line = reader.readLine();
            HashMap<String, String> memo = new HashMap<String, String>();
            long startTime = System.currentTimeMillis();
            int num = 1;
            while(line != null){
                if(num < startPoint){
                    line = reader.readLine();
                    num++;
                    continue;
                }
                System.out.print("Line Number: " + num + "/527430 Elapsed Seconds at Previous Line:" + ((System.currentTimeMillis() - startTime)/1000.0) + "\r");
                String[] splitline = line.trim().replace(",", " ").split(" ");
                String morph = "";
                for(String word : splitline){
                    if(word.trim().length() == 0){
                        continue;
                    }
                    String parse;
                    if(memo.containsKey(word)){
                        parse = memo.get(word);
                    }
                    else if(word.length() > 30){
                      parse = word;
                    }
                    else{
                        try{
                            parse = Decompose.decomposeToArrayOfStrings(word.toLowerCase())[0];
                        }
                        catch(Throwable e){
                            parse = word;
                        }
                    }
                    memo.put(word, parse);
                    morph = morph + " " + parse;
                }
                writer.append(morph + "\n");
                line = reader.readLine();
                num++;
            }
            reader.close();
            writer.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
}
