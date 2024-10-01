# RAG system for CDMX Traffic Regulations
### version 0.1

<p align="center">
  <img src="images\transito.jpg">
</p>

---
## Index
- 1.[Objective and description of the problem](#1-objective-and-description-of-the-problem)
- 2.[Technologies](#2-technologies)
  - 2.1.[Alternative A - One host machine.](#21-host-machine-technologies)
- 3.[Data Architecture](#3-data-architecture)
- 4.[Data description](#4-data-description)
- 5.[Instructions on how to replicate the project](#5-instructions-on-how-to-replicate-the-project)
  - 5.1.[Setting up alternative A](#51-setting-up-alternative-a)
    - 5.1.1.[Setting up instance](#511-setting-up-instance)
    - 5.1.2.[Creating file system](#512-creating-file-system)
    - 5.1.3.[Creating AWS S3 Bucket](#513-creating-aws-s3-bucket)
    - 5.1.4.[Creating services with docker-compose](#514-creating-services-with-docker--compose)
  - 5.2 [Setting uo alternative B](#52-setting-up-alternative-b)
    - 5.2.1 [Setting up server machine](#521-setting-up-server-machine)
    - 5.2.2 [Setting up user machine](#521-setting-up-user-machine) 
- 6.[Testing](#6-testing) 
  - 6.1.[Testing the ETL pipeline](#61-testing-the-etl-pipeline)
  - 6.2.[Testing the MLops pipeline](#62-testing-the-mlops-pipeline)
  - 6.3 [Looker Studio](#63-looker-studio)
- 7.[Future enhancements ](#9-future-enhancements)
- 8.[References](#10-references)
---
## 1. Objective and description of the problem
<p align="justify">
Traffic regulations documents play a crucial role in the development of cities around the world. This project aims to create a RAG (Retrieval-Augmented Generation) system for the traffic regulation document of Mexico City, Mexico. The target population for the project includes new drivers who are unfamiliar with the various articles that exist, as well as experienced drivers who have questions or doubts about any article in the document. The goal is to help these drivers better understand and navigate the traffic regulations.
</p>

I'm attacching the link to the traffic regulations document, the document is in Spanish:
>https://www.ssc.cdmx.gob.mx/storage/app/media/Transito/Actualizaciones/Reglamento-de-Transito-CDMX.pdf

## 2. Technologies
For setting up the VM Instance or Local Machine please install these tools:

- Miniconda environment (Python=3.11.9)
- Docker

After installed Miniconda environment please install the requirements file.

### 2.1 Host machine technologies
For this version it is all constructed in python using python libraries.
- <p align="justify">
  <b>Docker</b> : for creating the eleastic-search image.
  </p>

- <p align="justify">
  <b>Jupyter</b>:  is an open-source project that provides an interactive computing environment.
  </p>
  
- <p align="justify">
  <b>Pandas</b>:  is a data manipulation library.
  </p>

- <p align="justify">
  <b>pdfplumber</b>: is a pdf manipulation library.
  </p>

- <p align="justify">
  <b>openai</b>: is the Open AI library to their API.
  </p>

- <p align="justify">
  <b>pdfplumber</b>: is a pdf manipulation library.
  </p>
  
- <p align="justify">
  <b>Elastic Search</b>: is a search and analytics engine.
  </p>

- <p align="justify">
  <b>sentence_transformers</b>: is a python library for sentence embeddings.
  </p>

- <p align="justify">
  <b>Plotly Dash</b>: Is a framework for bouilding analytical web application in python.
  </p>
  
## 3. Data Architecture
Alternative A
<p align="center">
  <img src="images\diagram_v2.svg">
</p>

Alternative B
<p align="center">
  <img src="images\diagram_v3.svg">
</p>

## 4. Data description

<p align="justify">
The source of information is public, that means everyone has acces to this information. Also, this data is provided by the open data platform of IFT. 
</p>

<p align="justify">
 This information si provided in csv format, also I provide a google sheets document where is the original schema structure and data description of the tables. This information is uploaded monthly.
</p>

> https://docs.google.com/spreadsheets/d/176qSChhhpF43hzslsFscsAcBblJ0Wa_cyBHnzWTq1Eg/edit?usp=sharing

<b>Tables:</b>

- Lineas
- Tráfico de datos
- Indice de concentración
- Participacion de mercado

## 5. Instructions on how to replicate the project
### 5.1. Setting up alternative A
For this option need a host machine with Linux included, I used Debian distribution but is not necesary. You can use a virtual machine or your own computer, a good option if you don´t have a linux distribution instance yoou can use github codespace.

#### 5.1.1 Setting up instance.
Install the listed tools in your instance:

- Miniconda environment
- Docker
- Docker-Compose
- terraform
- git
- AWS
  
If you want steps for installing those tools, please check [`here`](./create_instance.md).

#### 5.1.2 Creating fyle system.

After finished point [6.1.1 Setting up instance.](#-setting-up-instance). Please copy this repository in a folder.

#### 5.1.3 Creating AWS S3 Bucket.
Inside of directory aws_infrastructure resides the tf files that allows to create a simple s3 bucket with standard configuration.
In order to run configuration you need to have your AWS credentials as environment variables after you have your credentials you can use the next command inside the directory /aws_infrastructure to initializate terraform and the setup of AWS. You can modify the variables.tf files if you want to change the bucket name and the region. 

```
terraform init 
```

Use the next command to create the AWS infrastructure with terraform.

```
terraform apply
```

You can always check if your bucket has beeen created using AWS cli. 

```
aws s3 ls
```

#### 5.1.4 Creating services with docker-compose

Inside of directory airflow_mlflow_files please create a .env file with these variables and fill then with your own choises. Be carefull the name you use in the POSTGRESS_DB variable because it is going to be the db used for airflow so maybe is better to leave it just like this but is up to you. The AIRFLOW_UID is only your user id you can see it using the command id -u. Also create these directories if they dont exists.

```
mkdir -p ./dags ./logs ./plugins ./config
```

```
AIRFLOW_UID=1001
POSTGRES_USER="user"
POSTGRES_PASSWORD="password"
POSTGRES_DB="airflow"
_AIRFLOW_WWW_USER_USERNAME="user"
_AIRFLOW_WWW_USER_PASSWORD="user"
BUCKET="s3://your_bucket_name/mlflow/"
```

Inside of directory airflow_mlflow_files resides a yaml file that have the configurations to install the images of airflow, mlflow and postgress. Please check if you´re inside the /airflow_mlflow_files directory and run the next command.

```
docker-compose up --build
```

Feel free to not use the --build command this is only to see the logs of the services.

You can check if the containers are up using 

```
docker ps
```
### 5.2. Setting up alternative B

#### 5.2.1 Setting up server machine
In this case follow the instructions from 5.1.1 to 5.1.4 but in the machine that you want to use like a server to host Mlops, Airflow, Postgress

#### 5.2.2 Setting up user machine 
Please install the libraries that are required in order to comunicate with the server machine and S3.

## 6. Testing
### 6.1. Testing the ETL pipeline 
In this section I'm using the airflow orchestator to automate the ETL process. Inside the <code>airflow_mlflow_files/dags</code> is the <code>etl_ift.py</code> code that do all the ETL pipe. now this code have two differents modules that were created that have the functions that are used to download the files and the data types transformations also the tweak for some columns  <code>airflow_mlflow_files/pluggins/schemas_tweaks</code>, <code>airflow_mlflow_files/pluggins/functions_ift</code>. This code is constructed in order to executate every 4 months, because this is the time that the origin updates. In general this pipe extracts the code, do some transformations and upload to an S3 Bucket. 

<p align="center">
  <img src="images\airflow_dashboard_success_1.png">
</p>

<p align="center">
  <img src="images\subidas.png">
</p>

### 6.2 Testing the Mlops pipeline
In this section <code>jupyter_files</code> I'm using Jupyter Lab to do all the Machine Learning cycle, using differents libraries to plotting, data manipulations, Machine learning and Mlops. In the <code>jupyter_files/EDA_1.ipynb</code> is all the exploratory analysis and in the <code>jupyter_files/Model_and_MLFlow.ipynb</code> is an example of how to use mlflow and creating the model and playin with them, also exist a very simple example of production state of the model <code>predict</code> <code>test</code>.

<p align="center">
  <img src="images\mlflow_code.png">
</p>

<p align="center">
  <img src="images\mlflow_dashboard.png">
</p>

<p align="center">
  <img src="images\mlflow_s3_artifacts.png">
</p>

<p align="center">
  <img src="images\mlflow_register.png">
</p>

this is only a comment becuse in the new version of mlflow in deprecated the option to change the state of the registred model. 
<p align="center">
  <img src="images\mlflow_stagind_deprecated.png">
</p>

### 6.3 Looker Studio
In looker, made a simple interactive dashboard of the market share in order to be more clear.

<p align="center">
  <img src="images\dashboard_market_share.png">
</p>

## Future enhancements
- The ETL process have some troubles downloading the files and for that reason the child tasks are flagged as wrong, maybe do it sequentaily all the etl process per table make better results.
- Make a better model for my project, the model that is in 6.2 is only an example showing the proccess but I have to tweak more the model, a linear regression maybe is not the best choise for a time serie.
- Tweak the dashboard; right now the dashboard is quite simple , maybe helps to get more an idea of what probler I'm trying to forecast but the problem has more information.
- migrate all to cloud, many things in this project can be all in cloud, i'm thinking in using Redshift for data analysis, machine learning,tabular data storage, quicksight for dashboard creation, S3 for objects storage more like an data lake and Managed workflows (MWAA)for orchestation.
