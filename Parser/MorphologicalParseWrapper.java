import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;

public class MorphologicalParseWrapper{
    /**
    * Takes an Inuktitut word and prints the morpholocical parse.
    * Wraps the morphological parser from Uqailaut Inuktitut parser. 
    */
    public static void main(String[] args){
    	DonneesLinguistiquesAbstract.init();
        String word = args[0];
		System.out.println(Decomposer.decomposeToMultilineString(word));
    }
}
