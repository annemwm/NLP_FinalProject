import applications.Decomposer;
import donnees.DonneesLinguistiquesAbstract;

public class MeaningParseWrapper{
    public static void main(String[] args){
    	DonneesLinguistiquesAbstract.init();
        String word = args[0];
		System.out.println(Decomposer.getMeaningsInString(word, "en", true, true));
    }
}
