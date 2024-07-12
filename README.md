# Langchain Restaurant Name Generator with GoogleAI


![Restaurant Name Generator Demo](Media/appname.gif)

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

    > [!NOTE]
    >
    > Replace the `AIzaSyCJBmdqxxxxxxxxxxxxxxxxxxxxx` with your GoogleAI api key.


5. Create a `.gitignore` file, edit and add `.env` to ensure the `.env` file with the API key does not commit.

    ```console
    echo ".env" >> .gitignore
    ```

    > [!NOTE]  
    > Highlights information that users should take into account, even when skimming.

    > [!TIP]
    > Optional information to help a user be more successful.

    > [!IMPORTANT]  
    > Crucial information necessary for users to succeed.

    > [!WARNING]  
    > Critical content demanding immediate user attention due to potential risks.

    > [!CAUTION]
    > Negative potential consequences of an action.

## Set up the Restaurant Name Generator Application

