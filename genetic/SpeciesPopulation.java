package GeneticTSP;


public class SpeciesPopulation {
	
	SpeciesIndividual head;
	int speciesNum;
	
	SpeciesPopulation()
	{
		head=new SpeciesIndividual();
		speciesNum=TSPData.SPECIES_NUM;
	}
	
	
	void add(SpeciesIndividual species)
	{
		SpeciesIndividual point=head;
		while(point.next != null)
			point=point.next;
		point.next=species;
	}
	
	
	void traverse()
	{
		SpeciesIndividual point=head.next;
		while(point != null)
		{
			for(int i=0;i<TSPData.CITY_NUM;i++)
				System.out.print(point.genes[i]+" ");
			System.out.println(point.distance);
			point=point.next;
		}
		System.out.println("_______________________");
	}

}
