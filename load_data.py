import os
import sys 
import numpy as np
import matplotlib.pyplot as plt
import random
class Data:
    #defines class variables
    __slots__=(
        "size",
        "verbose",
        "base_images",
        "ground_truths",
        "subsets",
        "data_folder"
    )
    
    
    def __init__(self,quantity:int=10000,verbose:bool=False):
        self.verbose=verbose
        self.size=quantity
        if "simgan" not in os.getcwd().lower():
            os.chdir(r"C:\Users\ONI\Desktop\Simgan\Simgan")
        self.data_folder=r"archive/MPIIGaze/Data/"
        self.base_images=self.load_images()
    
    
    def load_images(self):
        image_folder=r"Original/"
        subsets=os.listdir(os.path.join(self.data_folder,image_folder))
        sample_size=self.size//len(subsets) if self.size//len(subsets) else 1
        self.subsets=random.choices(subsets,
            k=sample_size if sample_size<len(subsets) else len(subsets)-1
        )
        if self.verbose:
            print(f"choosing from subsets: {self.subsets[0:]}") 
        for p in self.subsets:
            folder=os.path.join(self.data_folder,image_folder,p)
            days=os.listdir(folder)
            day_size=sample_size//len(days) if sample_size//len(days) else 1
            chosen_days=random.choices(days,
                k=day_size if day_size<len(days)-1  else len(days)-2 
            )
            if self.verbose:
                print(f"choosing from days: {chosen_days[0:]}")
            for day in chosen_days:
                path=os.path.join(
                        self.data_folder,
                        image_folder,
                        p,
                        day
                    )

                images=[os.path.join(path,file) for file in os.listdir(path)]
        images=random.choices(images,k=self.size)
        assert len(images) == self.size




            
    

if __name__ == "__main__":
    dat=Data(100000)