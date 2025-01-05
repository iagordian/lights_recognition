
from abc import ABC
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from typing import Dict, Optional

class ModelLearnLineGraph(ABC):

    def __init__(self, data_dict: Dict[int, float], title: str, y_label: Optional[str] = 'Значение', x_label: Optional[str] = 'Номер эпохи'):
        
        self.fig = plt.figure(figsize=(18, 12))
        self.ax = self.fig.add_subplot()
        self.ax.tick_params(axis='both', which='major', labelsize=12)
        plt.grid(alpha=0.3, color='grey', linestyle='--', zorder=1)

        self.data = pd.DataFrame(
            data_dict.items(),
            columns=[x_label, y_label]
        )

        plt.title(title, fontweight="bold")
        plt.ylabel(y_label, fontweight="bold")
        plt.xlabel(x_label, fontweight="bold")
        
        sns.lineplot(data=self.data, x=x_label, y=y_label, marker='o', zorder=2, 
                     markerfacecolor='white', markersize=8, color='#8a2be2', markeredgecolor='#8a2be2')
        
        for i, data in enumerate(zip(self.data[y_label], self.data[x_label]), start=1):

            accur, size = data
            accur = round(accur, 3)
            accur_next = self.data[y_label][i] if i != self.data[y_label].shape[0] else 0

            if all([
                i != self.data[y_label].shape[0],
                accur > accur_next or accur_next - accur > 0.06
            ]):
                accur_pos = accur + 0.001
            else:
                accur_pos = accur - 0.0015

            self.ax.annotate(accur, (size + 0.07, accur_pos), zorder=2, fontweight="bold")



    def save_to_file(self, file_name: str):
        self.fig.savefig(file_name)

class LossGraph(ModelLearnLineGraph):

    def __init__(self, data_dict: Dict[int, float]):

        super().__init__(data_dict, 'Loss')

class AucGraph(ModelLearnLineGraph):

    def __init__(self, data_dict: Dict[int, float]):

        super().__init__(data_dict, 'Auc')