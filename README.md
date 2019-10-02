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


---

# Logiciel PMA TCB

Ce logiciel permet de créer des fichiers d'analyse quantitative.
Il y a deux principaux cas d'utilisation. Le premier consiste à créer des fichiers quantitatifs 
avec le système de nommage approprié. Le deuxième est de les combiner en un 
fichier Excel unique pour une analyse plus approfondie.

# Installation

Tout d'abord, Python 3 est requis sur votre machine.

Vous devez d'abord accéder à votre exécutable "python3". Accéder à son répertoire 
si nécessaire (par exemple sous Windows).


```bash
python3 -m pip install https://github.com/PMA-2020/tcb/zipball/master
```

# Mises à jpur

Mettre à jour le logiciel avec
```bash
python3 -m pip install https://github.com/PMA-2020/tcb/zipball/master --upgrade
```

# Cas d’usage  1 : création de fichiers quantitatifs vierges

Il y a deux entrées :

1. Gabarit d'évaluation quantitative vide. Nous en ferons des copies 
du fichier. Une version récente de ce fichier a été nommée 
`PMA-TCB-Assessment-Template-v2-EN.xlsx`. Il existe aussi une version française
de ce fichier:
 `PMA-TCB-Assessment-Template-v3_FR.xlsx`. Ces fichiers se trouvent dans les dossiers Dropbox TCB.
2. Une liste maitresse du personnel. Un modèle se trouve ici dans ce référentiel
[files/TCB-Personnel-Masterlist.xlsx](files/TCB-Personnel-Masterlist.xlsx?raw=true).
Tout ce que nous spécifions dans les colonnes appropriées "Country", "Whom to assess" 
(l'apprenant), et "Assessor". Le "Assessor" est la personne qui remplit

 

l'évaluation quantitative. Il peut s'agir de l'apprenant ou de quelqu'un d'autre, comme un  superviseur.  Cette partie du logiciel ne fait que créer des copies du gabarit et les nomme  correctement. Le schéma de dénomination est:
```
[NAME-OF-LEARNER]_[COUNTRY]_[NAME-OF-ASSESSOR].xlsx
```

et un exemple du schéma de dénomination est "Joe-Flacco_USA_Jim-Harbaugh.xlsx".Ici l’apprenant est Joe Flacco et l'évaluateur est Jim Harbaugh. Leur pays est: les USA.  Exemple d'usage:

```bash
python3 -m tcb.create -t PMA-TCB-Quant-Assessment-Template-srt_EN.xlsx -p TCB-Personnel-Masterlist.xlsx -o output_directory/
```

et les fichiers créés sont placés dans  le dossier `output_directory/`
 

# Cas d’usage 2: combinaison des résultats

L'entrée dans cette partie du logiciel est un dossier contenant tous les éléments remplis 
des évaluations quantitatives. Le schéma de dénomination du fichier est important.Il 
doit correspondre à

```
[NAME-OF-LEARNER]_[COUNTRY]_[NAME-OF-ASSESSOR].xlsx
```

car ces champs deviennent des entrées de données dans la serie de données. 

Chaque évaluation quantitative devient une ligne dans la serie de données combinées.

Exemple d’usage:


```bash
python3 -m tcb.combine results_directory/
```

et la serie de données combinées est enregistrée à `tcb_results.xlsx dans le répertoire en cours.
