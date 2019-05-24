package GeneticTSP;



public class MainRun {

	public static void main(String[] args) {
		
		
		
		GeneticAlgorithm GA=new GeneticAlgorithm();
		
		
		SpeciesPopulation speciesPopulation = new SpeciesPopulation();

		
		SpeciesIndividual bestRate=GA.run(speciesPopulation);

		
		bestRate.printRate();

	}

}
