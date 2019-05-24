package GeneticTSP;

import java.util.Random;


public class SpeciesIndividual {
	
	String[] genes;
	float distance;
	float fitness;
	SpeciesIndividual next;
	float rate;
	
	SpeciesIndividual()
	{
		
		this.genes=new String[TSPData.CITY_NUM];
		this.fitness=0.0f;
		this.distance=0.0f;
		this.next=null;
		rate=0.0f;
	}
	
	
	void createByRandomGenes()
	{
		
		for(int i = 0;i < genes.length;i++)
		{
			genes[i]=Integer.toString(i+1);
		}
		
		
		Random rand=new Random();

		for(int j=0;j<genes.length;j++)
		{
			int num= j + rand.nextInt(genes.length-j);
			
			
			String tmp;
			tmp=genes[num];
			genes[num]=genes[j];
			genes[j]=tmp;
		}
	}
	
	
	void createByGreedyGenes()
	{
		Random rand=new Random();
		int i= rand.nextInt(TSPData.CITY_NUM); 
		genes[0]=Integer.toString(i+1);
		int j;
		int cityNum=0;
		do
		{
			cityNum++;
			
			
			float minDis=Integer.MAX_VALUE;
			int minCity=0;
			for(j=0;j<TSPData.CITY_NUM;j++)
			{
				if(j != i)
				{
					
					boolean repeat=false;
					for(int n=0;n<cityNum;n++)
					{
						if(Integer.parseInt(genes[n]) == j+1)
						{
							repeat=true;
							break;
						}
					}
					if(repeat == false)
					{
						
						if(TSPData.disMap[i][j] < minDis)
						{
							minDis=TSPData.disMap[i][j];
							minCity=j;
						}
					}
				}
			}
			
			
			genes[cityNum]=Integer.toString(minCity+1);
			i=minCity;
		}while(cityNum < TSPData.CITY_NUM-1);
	}
	
	
	void calFitness()
	{
		float totalDis=0.0f;
		for(int i = 0;i < TSPData.CITY_NUM;i++)
		{
			int curCity=Integer.parseInt(this.genes[i])-1;
			int nextCity=Integer.parseInt(this.genes[(i+1) % TSPData.CITY_NUM])-1;

			totalDis += TSPData.disMap[curCity][nextCity];
		}
		
		this.distance=totalDis;
		this.fitness=1.0f/totalDis;
	}
	
	
	public SpeciesIndividual clone()
	{	
		SpeciesIndividual species=new SpeciesIndividual();
		
		
		for(int i=0;i<this.genes.length;i++)
			species.genes[i]=this.genes[i];
		species.distance=this.distance;
		species.fitness=this.fitness;
	
		return species;	
	}
	
	
	void printRate()
	{
		for(int i=0;i<genes.length;i++)
			System.out.print(genes[i]+"->");
		System.out.print(genes[0]+"\n");
		System.out.print("distance" + distance);
	}

}
