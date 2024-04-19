dict_of_species: dict[str,int] = {
    'H': 1,
    'NH4': 1,
    'Na': 1,
    'Cl' : -1,
    'OH': -1
    }

class chemicals:
    
    
    def __init__(self,chem: str,oxidation = 0)-> str:
        
        self.chemical_list: list =[]
        self.chem: str = ''
        
        for species in dict_of_species:
            if species in chem:
                self.chemical_list.append(species)
        
        self.factors: dict = {self.chemical_list[0]: 1,self.chemical_list[1]:1}
        
        while True:
            
            sum : int= self.factors[self.chemical_list[0]]*dict_of_species[self.chemical_list[0]] + self.factors[self.chemical_list[1]]*dict_of_species[self.chemical_list[1]]
            
            if sum < oxidation:
                self.factors[0]+= 1
            if sum > oxidation:
                self.factors[1]+= 1
            
            if sum == oxidation:
                break
        
        needsPar: dict = {self.chemical_list[0]: 0, self.chemical_list[1]: 0}
        
        for chemicals in self.chemical_list:
            for char in chemicals:
                if char.isupper():
                    needsPar[chemicals] += 1
        
        for chemical in self.chemical_list:
            if needsPar[chemical] >= 2 and self.factors[chemical] > 1:
                self.chem += '('+chemical+')'+self.factors[chemical]
            elif self.factors[chemical] > 1:
                self.chem += chemical + self.factors[chemical]
            else: self.chem += chemical
        
        return self.chem


def reaction(reactant_1: str, reactant_2: str)-> list[str]:
    return [chemicals(reactant_1.chemical_list[0]+chemicals(reactant_2.chemical_list[1])),chemicals(reactant_2.chemical_list[0]+chemicals(reactant_1.chemical_list[1]))]

def all_possible_species(*arg_of_species)->list[str]:
    oxidationSort:list[list[str],list[str],list[str]]=[[],[],[]]
    turner: list[str] = []
    for i in arg_of_species:
        if dict_of_species[i] > 0:
            oxidationSort[0].append(i)
        elif dict_of_species[i] < 0:
            oxidationSort[1].append(i)
        elif dict_of_species[i] == 0:
            oxidationSort[2].append(i)
        else: raise Exception('idk what happened')
    
    for j in oxidationSort[0]:
        for k in oxidationSort[1]:
            turner.append(j+k)
    return turner

print(all_possible_species(input("chemicals").split(' ')))
