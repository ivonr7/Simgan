import os
import sys 
import numpy as np
import matplotlib.pyplot as plt
import random
class Data:
    #defines class variables
    __slots__=(
        "size",
        "current_index",
        "img",
        "verbose",
        "base_images",
        "ground_truths",
        "subsets",
        "data_folder",
        # "get_img",
        # "show_img"

    )
    
    
    def __init__(self,quantity:int=10000,verbose:bool=False):
        self.verbose=verbose
        self.size=quantity
        self.current_index=0

        if "simgan" not in os.getcwd().lower():
            os.chdir(r"C:\Users\ONI\Desktop\Simgan\Simgan")
        self.data_folder=r"archive/MPIIGaze/Data/"
        self.base_images=self.load_images()
    #getters
    #----------------------

    #behaves like a queue only loads next img
    def get_img(self):
        path=self.base_images[self.current_index]
        if self.verbose:
            print("getting img:",path)
        self.img=plt.imread(path)
        self.current_index+=1
        return self.img

    #shows img --sanity check
    def show_img(self):
        if self.verbose:
            print("showing image")
        plt.imshow(self.img)
        plt.show()
    
    #loads img urls
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
        return images




            
    

if __name__ == "__main__":
    dat=Data(100000)
    dat.get_img()
    dat.show_img()