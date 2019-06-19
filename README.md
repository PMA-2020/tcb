# PMA TCB software

This software is for creating quantitative analysis files.

There are two main use cases. The first is to create the quantitative files 
with the proper naming scheme. The second is to combine them together into a 
single Excel file for further analysis.

# Installation

First, Python 3 is required on your machine.

You first need access to your `python3` executable. Navigate to its enclosing 
directory if needed (such as on Windows).

```bash
python3 -m pip install https://github.com/PMA-2020/tcb/zipball/master
```

# Updates

Update the software with

```bash
python3 -m pip install https://github.com/PMA-2020/tcb/zipball/master --upgrade
```

# Use case 1: creating blank quantitative files

There are two inputs:

1. The blank quantitative assessment template. We will make copies of this 
file. A recent version of this file was named 
`PMA-TCB-Assessment-Template-v2-EN.xlsx`. There is also a French version
of this file: `PMA-TCB-Assessment-Template-v3_FR.xlsx`. These files can be found in the TCB Dropbox folders. 
2. A master personnel list. There is a template found here in this repository
at [files/TCB-Personnel-Masterlist.xlsx](files/TCB-Personnel-Masterlist.xlsx?raw=true).
All we are specifying in the proper columns "Country", "Whom to assess" 
(the learner), and "Assessor". The "Assessor" is the person who is filling out 
the quantitative assessment. It can be the learner or someone else, such as a 
supervisor.

All this part of the software does is create copies of the template and names 
them properly. The naming scheme is

```
[NAME-OF-LEARNER]_[COUNTRY]_[NAME-OF-ASSESSOR].xlsx
```

and an example of the naming scheme is `Joe-Flacco_USA_Jim-Harbaugh.xlsx`. Here
the learner is Joe Flacco and the assessor is Jim Harbaugh. Their country is 
USA.

Sample usage:

```bash
python3 -m tcb.create -t PMA-TCB-Quant-Assessment-Template-srt_EN.xlsx -p TCB-Personnel-Masterlist.xlsx -o output_directory/
```

and the created files are placed in the `output_directory/` folder.

# Use case 2: combining results

The input to this part of the software is a folder containing all the filled 
out quantitative assessments. The naming scheme of the file is important. It 
should match   

```
[NAME-OF-LEARNER]_[COUNTRY]_[NAME-OF-ASSESSOR].xlsx
```

because those fields become data entries in the dataset. 

Each quantitative assessment becomes a row in the combined dataset.

Sample usage:

```bash
python3 -m tcb.combine results_directory/
```

and the combined dataset is saved at `tcb_results.xlsx` in the current 
directory.
