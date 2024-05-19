class Validator():
    def __init__(self):
        self.from_ = None
        self.to_ = None
    
    def validate(self,from_,to_):
        if from_ is None or to_ is None:
            return False
        else:
            return True
    def validmoves(self) -> bool:
        # Moves object stores the possible moves from the current position 
        moves={
            'a':{
                'non_jump':['c', 'd', 'e', 'f'],
                'jump' :['i', 'j', 'k', 'l']
            },
            'b':{
                'non_jump':['h', 'c'],
                'jump' :['n','d']

            },
            'c':{
                'non_jump':['i', 'b', 'd'],
                'jump' :['o', 'e']
            },
            'd':{
                'non_jump':['e', 'c', 'f'],
                'jump' :['p', 'g']
            },
            'e':{
                'non_jump':['f', 'd', 'g'],
                'jump' :['q', 'h']

            },
            'f':{
                'non_jump':['g', 'e', 'h'],
                'jump' :['r', 'i']
            },
            
            
        }

        return True
    




        
