class Solution(object):
    def minNumberOfHours(self, initialEnergy, initialExperience, energy, experience):
        training_hours = 0
        
        for e, exp in zip(energy, experience):
            # Check energy
            if initialEnergy <= e:
                needed_energy = e - initialEnergy + 1
                training_hours += needed_energy
                initialEnergy += needed_energy
                
            # Check experience
            if initialExperience <= exp:
                needed_exp = exp - initialExperience + 1
                training_hours += needed_exp
                initialExperience += needed_exp
                
            # Simulate the fight
            initialEnergy -= e
            initialExperience += exp
            
        return training_hours
        