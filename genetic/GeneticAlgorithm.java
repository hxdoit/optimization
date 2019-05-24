package GeneticTSP;

import java.util.Random;


public class GeneticAlgorithm {
	
	    
		SpeciesIndividual run(SpeciesPopulation list)
		{
			
			createBeginningSpecies(list);
			
			for(int i=1;i<=TSPData.DEVELOP_NUM;i++)
			{
				
				select(list);
				
				
				crossover(list);
				
				
				mutate(list);
			}	
			
			return getBest(list);
		}
		
		
		void createBeginningSpecies(SpeciesPopulation list)
		{
			
			int randomNum=(int)(TSPData.SPECIES_NUM);
			for(int i=1;i<=randomNum;i++)
			{
				SpeciesIndividual species=new SpeciesIndividual();
				species.createByRandomGenes();

				list.add(species);
			}
			






	


		}

		
		void calRate(SpeciesPopulation list)
		{
			
			float totalFitness=0.0f;
			list.speciesNum=0;
			SpeciesIndividual point=list.head.next;
			while(point != null)
			{
				point.calFitness();
				
				totalFitness += point.fitness;
				list.speciesNum++;

				point=point.next;
			}

			
			point=list.head.next;
			while(point != null)
			{
				point.rate=point.fitness/totalFitness;
				point=point.next;
			}
		}
		
		
		void select(SpeciesPopulation list)
		{			
			
			calRate(list);
			
			
			float talentDis=Float.MAX_VALUE;
			SpeciesIndividual talentSpecies=null;
			SpeciesIndividual point=list.head.next;

			while(point!=null)
			{
				if(talentDis > point.distance)
				{
					talentDis=point.distance;
					talentSpecies=point;
				}
				point=point.next;
			}

			
			SpeciesPopulation newSpeciesPopulation=new SpeciesPopulation();
			int talentNum=(int)(list.speciesNum/4);
			for(int i=1;i<=talentNum;i++)
			{
				
				SpeciesIndividual newSpecies=talentSpecies.clone();
				newSpeciesPopulation.add(newSpecies);
			}

			
			int roundNum=list.speciesNum-talentNum;
			for(int i=1;i<=roundNum;i++)
			{
				
				float rate=(float)Math.random();
				
				SpeciesIndividual oldPoint=list.head.next;
				while(oldPoint != null && oldPoint != talentSpecies)
				{
					if(rate <= oldPoint.rate)
					{
						SpeciesIndividual newSpecies=oldPoint.clone();
						newSpeciesPopulation.add(newSpecies);
						
						break;
					}
					else
					{
						rate=rate-oldPoint.rate;
					}
					oldPoint=oldPoint.next;
				}
				if(oldPoint == null || oldPoint == talentSpecies)
				{
					
					point=list.head;
					while(point.next != null)
						point=point.next;
					SpeciesIndividual newSpecies=point.clone();
					newSpeciesPopulation.add(newSpecies);
				}
				
			}
			list.head=newSpeciesPopulation.head;
		}
		
		
		void crossover(SpeciesPopulation list)
		{
			
			float rate=(float)Math.random();
			if(rate > TSPData.pcl && rate < TSPData.pch)
			{			
				SpeciesIndividual point=list.head.next;
				Random rand=new Random();
				int find=rand.nextInt(list.speciesNum);
				while(point != null && find != 0)
				{
					point=point.next;
					find--;
				}
			
				if(point.next != null)
				{
					int begin=rand.nextInt(TSPData.CITY_NUM);

					
					for(int i=begin;i<TSPData.CITY_NUM;i++)
					{
						
						
						int fir,sec;
						for(fir=0;!point.genes[fir].equals(point.next.genes[i]);fir++);
						for(sec=0;!point.next.genes[sec].equals(point.genes[i]);sec++);
						
						String tmp;
						tmp=point.genes[i];
						point.genes[i]=point.next.genes[i];
						point.next.genes[i]=tmp;
						
						
						point.genes[fir]=point.next.genes[i];
						point.next.genes[sec]=point.genes[i];
						
					}
				}
			}
		}
		
		
		void mutate(SpeciesPopulation list)
		{	
			
			SpeciesIndividual point=list.head.next;
			while(point != null)
			{
				float rate=(float)Math.random();
				if(rate < TSPData.pm)
				{
					
					Random rand=new Random();
					int left=rand.nextInt(TSPData.CITY_NUM);
					int right=rand.nextInt(TSPData.CITY_NUM);
					if(left > right)
					{
						int tmp;
						tmp=left;
						left=right;
						right=tmp;
					}
					
					
					while(left < right)
					{
						String tmp;
						tmp=point.genes[left];
						point.genes[left]=point.genes[right];
						point.genes[right]=tmp;

						left++;
						right--;
					}
				}
				point=point.next;
			}
		}

		
		SpeciesIndividual getBest(SpeciesPopulation list)
		{
			float distance=Float.MAX_VALUE;
			SpeciesIndividual bestSpecies=null;
			SpeciesIndividual point=list.head.next;
			while(point != null)
			{
				if(distance > point.distance)
				{
					bestSpecies=point;
					distance=point.distance;
				}

				point=point.next;
			}
			
			return bestSpecies;
		}

}
