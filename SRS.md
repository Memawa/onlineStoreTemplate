# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Mekhi Washington](emailto:mwashi35@uncc.edu)
* [Adrian Dominguez-Hernandez](emailto:adoming8@uncc.edu)
* [Derin Tekin](mmailto:dtekin1@uncc.edu)
* [Name](mmailto:email@uncc.edu)

## Revisions

When a change is made to the document, a new revision should be created. The revision should be added to the table below with all information filled out.

| Version | Date | Description | Author | Reviewed By |
| --- | --- | --- | --- | --- |
| 1.0 | 03/22/23 | Initial draft | [David Gary](mailto:dgary9@uncc.edu) | [David Gary](mailto:dgary@uncc.edu) |

## Table of Contents

1. [Introduction](#introduction)
2. [Requirements](#requirements)
3. [Constraints](#constraints)
4. [Use Cases](#use-cases)
5. [User Stories](#user-stories)
6. [Glossary](#glossary)

## Introduction

Our project is going to be an online music store. Our software will display music albums the user can buy and when they click/purchase on the album the software will display popular artists from that category and merch they might want to buy. They will be hardcoded. 



## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:**Database1.
  * **Description:** Hardcode the database 
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** it is important because the code will not properly funciton and the main function of the store wouldn't run
  * **Testing:** There isn't much testing in the database 
* **ID:**Main1
  * **Description:** The main file will have all the methods used to grab the genres, artists, merch, and prices.
  * **Type:** Functional
  * **Priority:** 1
  * **Rationale:** Without this file we will just have a database with no use. this file will put those values to use
  * **Testing:** making sure the main file is pulling the right values from the database. And displays them right.

  Function 1 
    Description- Being able to buy and sell music
    Type- Functional
    Priority-5
    Rationals-It is the main function of our store
    Testing- Can be tested by running a fake checkout/selling test
  
  Function 2
    Description- Recommend artist for that artist you picked
    Type- Functional
    Priority-3
    Rationals-Enhances the experience with our program so that we can 
    Testing- Can be tested by running a the sell/checkout function

   Function 3
    Description- Merch Shop
    Type- Functional
    Priority-3
    Rationals-Would allow customers to buy merch from there favorite artist's 
    Testing- Can be tested by running a the sell/checkout function
  



## Constraints

We can only commit/make changes to a file if everyone is in 100% agreeance. Espicially the main file.

  -Having 5 weeks to have this project done.
  -Not enough funding


## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **ID:** A unique identifier for the use case. This should be a number that is unique across the entire document (something like UC-1, UC-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A description of the use case that gives the user a high-level overview of how the system is interacted with.
  * **Actors:** A list of the actors that are involved in the use case. Only include the actors that are directly involved. Actors are the people or things that interact with the system. For example, when ordering at a fast food restaurant, one might have the following actors: the customer, the cashier, and the cook. But only the customer and the cashier are directly involved in the use case of ordering food. The cook is not directly involved in the use case of ordering food.
  * **Preconditions:** A list of the preconditions for the use case. This should be a list of the preconditions for the use case, which are the conditions that must be met before the use case can be executed. Continuing with the restaurant example, the customer must have money in their wallet and the cashier must be logged in to the system before the use case of ordering food can be executed.
  * **Postconditions:** A list of the postconditions for the use case. This should be a list of the postconditions for the use case, which are the conditions that must be met after the use case has been executed. Continuing with the restaurant example, the customer must have their food and the cashier must have the customer's money after the use case of ordering food has been executed.

## User Stories

* **US-1:** 
  * **Type of user:** Customer 
  * **Description:** As a person that enjoys music, I want to browse the website and be able to look at different types of albums and artists that the website provides. 

* **US-2:** 
  * **Type of user:** Customer
  * **Description:**As a music lover, I want to be able to add multiple albums to my list and purchase them in any time I would like. 

* **US-3:** 
  * **Type of user:** Customer
  * **Description:**I want the website to provide me with recommendations because sometimes I want to find new music and I don’t know where to look so I want recommendations when I purchase my music. 

* **US-4:** 
  * **Type of user:** Customer 
  * **Description:** If I am a fan of a certain artist, I want to look and be able to find merchandise for that artist. 

* **US-5:** 
  * **Type of user:** Customer
  * **Description:** I want to be able to buy gift cards for this website for my other friends that enjoy music. 

* **US-6:** 
  * **Type of user:** Admin
  * **Description:** I want to be able to create a website that any music lover can find what they need, and I want to be able to recommend them with music that is close to their taste. I also want to give them the option to find merchandise on the artists that they love. 

US1
  Customer
  Description: Customer wants to buy the new A boogie album that just dropped. He goes on to the website and while about to buy the album he thens sees A boogie merch. He buys both merch and album.

US-8 
  Customer
  Description: Customer buys a Taylor Swift album. The recommended function tells her about adele and she buys a album from her as well.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** album
  * **Definition:** a collection of songs/tracks on a medium

  * **Term:** audio file
  * **Definition:** file that contains audio 

  * **Term:** merchandise
  * **Definition:** anything the artist would be selling. Doesn't have to be music exacltly.
