import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;

public class MeaningParseWrapper{
    /**
    * Takes a morphological parse of an Inuktitut word and prints the meaning parse.
    * Wraps the meaning parser from Uqailaut Inuktitut parser. 
    */
    public static void main(String[] args){
    	DonneesLinguistiquesAbstract.init();
        String word = args[0];
		System.out.println(Decomposer.getMeaningsInString(word, "en", true, true));
    }
}
