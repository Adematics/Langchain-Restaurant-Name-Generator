# Langchian Restaurant Name Generator with GoogleAI


<video controls src="Media/appmedia.mp4" title="Title"></video>

## Prerequisite
Before you begin:
* Install Python 
* Signup to GoogleAI account : https://aistudio.google.com/ 

## Preparing the Enviroment

To run the restaurant name generator app, you need to set up Langchain and GoogleAI environemt packages. Follow the steps below to set up your application environment.

1. Install pipenv to manage the package dependencies of your application.
    
    ```console
    pip install pipenv
    ```

2. Install the Langchain and GoogleGenerativeAI model packages

    ```console
    pipenv install langchain-google-genai langchain_core langchain
    ```

3. Create a new GoogleAI API key as follows:

    * Go to https://aistudio.google.com/app/apikey
    * Create a key and copy it

4. Create a `.env` file, edit and save the API key.

    ```console
    api_key = "AIzaSyCJBmdqxxxxxxxxxxxxxxxxxxxxx"
    ```
5. Create a `.gitignore` file, edit and add `.env` to ensure the `.env` file with the API key does not commit.

    ```console
    echo ".enc" >> .gitignore
    ```

## Set up the Restaurant Name Generator Application

