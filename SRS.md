# Software Requirements Specification Document

This serves as a template for each projects' Software Requirements Specification (SRS) document. When filling this out, you will be required to create user stories, use cases, requirements, and a glossary of terms relevant to your project. Each group member must contribute to every section, so it is crucial that your group's GitHub repository shows a commit history that reflects the work of each group member. It is highly recommended that you create separate branches for each member, but since this is one single document, you will need to manually merge the branches together. It is also advisable to have multiple working versions of this document (named separately) so that one person can compile the final SRS document from the multiple working versions. Ultimately, how you go about managing this is up to you, but consistent formatting, clear commit messages, and a thorough commit history with contributions from each group member are required.

Fill the document out following the guidelines listed in each section. Maintain [proper Markdown syntax](https://www.markdownguide.org/basic-syntax/) and be sure that your group has a `main` branch with this document and the entire [template repository codebase](https://github.com/david-gary/onlineStoreTemplate) either forked or downloaded and copied into your group's repository. If you have arranged to use a different codebase as a template, you do not need to have the original template included, but a `main` branch is still required.

## Group Members

* [Mekhi Washington](emailto:mwashi35@uncc.edu)
* [Name](mmailto:email@uncc.edu)
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

In this section, you should give a brief overview of what your project will be. Describe the software system you are building and what problems it solves. You should also give a short description of the stakeholders (users of the system) and what their needs are. There is no set formatting requirement, but you should maintain a consistent structure across future sections. Not all members must contribute to this section.



## Requirements

Each group member must supply at least three functional requirements for the project. Each requirement should be written in the following format:

* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement. Do not replace the word `Description` with the actual description. Put the description in the space where these instructions are written. Maintain that practice for all future sections.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.
* **ID:** A unique identifier for the requirement. This should be a number that is unique across the entire document (something like REQ-1, REQ-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Description:** A short description of the requirement. This should be a single sentence that describes the requirement.
  * **Type:** The type of requirement. Should be either `Functional` or `Non-Functional`.
  * **Priority:** The priority of the requirement. This should be a number between 1 and 5, with 1 being the highest priority and 5 being the lowest priority.
  * **Rationale:** A short description of why the requirement is important. This should be a single sentence that describes why the requirement is important.
  * **Testing:** A short description of how the requirement can be tested. This should be a single sentence that describes how the requirement can be tested.

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

In this section, you should list any constraints that you have for the project. Each group member must supply at least two constraints. These can be constraints on the project itself, the software system, or the stakeholders. Constraints can be anything that limits the scope of the project. For example, that this project's template code is written using Flask and Python constitutes a constraint on the backend of the project. Constraints can also be things like the required timeline of the project. Be creative.

  -Having 5 weeks to have this project done.
  -Not enough funding


## Use Cases

In this section, you should list use cases for the project. Use cases are a thorough description of how the system will be used. Each group member must supply at least two use cases. Each use case should be written in the following format:

* **UC-1:**
  * **Actors:** User
  * **Preconditions:** User has logged onto the the system. 
  * **Postconditions:** purchasing albums 
  * **Description:** Users can browse the website and purchase individual albums.
  
* **UC-2:**
* **Actors:** User
  * **Preconditions:** The user has selected an album.
  * **Postconditions:** The user gets recommendations based on their selection. 
  * **Description:** The system recommends albums similar to the one the user picked based on the artist or the genre. 

* **UC-3:** 
  * **Actors:** User
  * **Preconditions:** the user has logged into the system. 
  * **Description:** The user can look for merchandise on the website, for the artists they like, for purchase. 

* **UC-4:**
  * **Actors:** User
  * **Preconditions:** user has logged onto the website 
  * **Postconditions:** the user can view the information
  * **Description:** The user can do searches based on their preferred artists or genre. 

* **UC-5:**
  * **Actors:** User
  * **Preconditions:**The user is logged into the website
  * **Postconditions:** buying gift cards
  * **Description:** The user can buy gift cards to use on the website. 

* **UC-6:**
  * **Actors:** User
  * **Preconditions:** The user is logged into the website
  * **Postconditions:** creating wishlists
  * **Description:** The user can add multiple items they would like to purchase and they can keep looking at other items while those items are on their list.

## User Stories

In this section, you should list user stories for the project. User stories are a short description of how a user will be interacting with the system. Each group member must supply at least two user stories. Each user story should be written in the following format:

* **ID:** A unique identifier for the user story. This should be a number that is unique across the entire document (something like US-1, US-2, etc. but be sure to replace the word `ID` with the unique identifier).
  * **Type of User:** The type of user that the user story is for. This should be a single word that describes the type of user. For example, a user story for a customer might be `Customer` and a user story for an administrator might be `Admin`.
  * **Description:** A description of the user story that gives a narrative from that user's perspective. This can be any length, but it must paint the picture of what the user wants to do, how they intend to do it, why they want to, and what they expect to happen.

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

US2 
  Customer
  Description: Customer buys a Taylor Swift album. The recommended function tells her about adele and she buys a album from her as well.

## Glossary

In this section, you should list any terms that are used in the document that may not be immediately obvious to a naive reader. Each group member must supply at least one term. Each term should be written in the following format:

* **Term:** The term that is being defined. This should be a single word or phrase that is being defined.
  * **Definition:** A definition of the term. This should be a short description of the term that is being defined. This should be a single sentence that describes the term.
