# Comparison Of Identification Techniques
A number of common identification techniques were implemented on various systems and analysed in terms on their robustness and speed. Robustness is a measure of the identification model's sensitivity to variations in inputs and process uncertainties. Currently, the TClab is used to generate input and output data. So far, the ARX and ARMAX models have been implemented.

Instructions to clone this repository:

A) Helpful links for first time git and github users.

https://www.git-tower.com/learn/git/ebook/en/command-line/appendix/command-line-101
https://www.earthdatascience.org/workshops/intro-version-control-git/basic-git-commands/

B) A method to separate data from code was implemented. The modules configparser, pathlib and pandas were used; if you haven't heard of these you can read about it here: https://negfeedback.blogspot.com/2019/04/how-to-separate-your-data-from-your-code.html. 

After the repository is cloned, open the file "Comparison-Of-Identification-Techniques" and proceed as follows to create your own config.ini file:

1) Create your own data storage folder, "my_data_folder" perhaps.
2) open a new text document in the directory
3) copy and fill,

[paths]

input_datadir=~/\your_path_to_directory\Comparison-of-Identification-Techniques\your_data_storage_folder\Data\Input_Data

result_datadir=~/\your_path_to_directory\Comparison-of-Identification-Techniques\your_data_storage_folder\Data\Results

IMAGES_datadir=~/\your_path_to_directory\Comparison-of-Identification-Techniques\your_data_storage_folder\Report\IMAGES

4) example:

[paths]

input_datadir=~/\Desktop\my_projects\Comparison-of-Identification-Techniques\my_data_folder\Data\Input_Data

5) Save as config and close the text document, in the file's properties change the extention from .txt to .ini

