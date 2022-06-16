import os
import sys 
import numpy as np
import matplotlib.pyplot as plt
import random
class Data:
    #defines class variables
    __slots__=(
        "size",
        "base_images",
        "ground_truths",
        "subsets",
        "data_folder"
    )
    
    
    def __init__(self,quantity:np.int16=10000):
        self.size=quantity
        if "simgan" not in os.getcwd().lower():
            os.chdir(r"C:\Users\ONI\Desktop\Simgan\Simgan")
        self.data_folder=r"archive/MPIIGaze/Data/"
        self.base_images=self.load_images()
    
    
    def load_images(self):
        image_folder=r"Original/"
        subsets=os.listdir(os.path.join(self.data_folder,image_folder))
        sample_size=int(self.size/len(subsets))
        self.subsets=random.choices(subsets,
            k=3
        )
        for p in self.subsets:
            folder=os.path.join(self.data_folder,image_folder,p)
            days=os.listdir(folder)
            day_size=sample_size//len(days)
            chosen_days=random.choices(days,
                k=day_size if day_size<len(days)-1 else len(days)-2 
            )
            for day in chosen_days:
                path=os.path.join(
                        self.data_folder,
                        image_folder,
                        p,
                        day
                    )

                images=[os.path.join(path,file) for file in os.listdir(path)]
        images=random.choices(images,k=self.size)    




            
    

if __name__ == "__main__":
    dat=Data(1000)