# NCEA Level 3 Web and Database Project Instructions



## Introduction

You are required to design and create a web application that satisfies a particular need or problem for a person or group of people. The need / problem should be a genuine and authentic one.

You will be assessed on how skilfully and effectively you design, create, and test your system over the course of a number of 'sprints'

*Note: If you cannot identify a need / problem, [this document](ideas.md) has some that might help you.*

---

## Assessment Standards

| Standard             | Version | Level | Credits |
| -------------------- | ------- | ----- | ------- |
| [91902](as91902.pdf) | 2       | 3     | 4       |
| [91903](as91903.pdf) | 1       | 3     | 4       |


---

## Timeline

You will have 10 weeks to complete this project, broken up into a number of phases:

| Weeks | Phase                                                                       |
| ----- | --------------------------------------------------------------------------- |
| 1     | Project idea clarification, development and research                        |
| 2-3   | **Sprint 1**: DB design and working UI prototype, using DrawSQL and Figma |
| 4-7   | **Sprint 2**: Working MVP (minimum viable product), using Flask template    |
| 8-9   | **Sprint 3**: System refinement and completion                              |
| 10    | Final testing and review                                                |

A 'sprint' is a set period of time during which specific work has to be completed and made ready for review. In this project, the work for each sprint has been defined for you in the table above.

During each sprint you will develop your ideas, create suitable outcomes, present these to your end-user(s) so they can try them out, collect feedback / test data, and improve your outcomes to fix any issues.


---

## Assessment Conditions

This is an 'open book' task. You may look at previous projects that you have worked on, and you may use any notes provided (e.g. the language reference documents).

### Starter Template

A [setup guide](setup.md) and a [project template](template.md) with a minimal Flask application are provided for you. The template has very basic functionality upon which you can build your system.

### Plagiarism and the Use of AI / LLMs

This is an individual assessment activity: Beyond the starter template, all the work that you produce must be your own. Do not copy blocks of code from other people, nor use an AI code-generation tool to write blocks of code for you.

*Note: You will be asked to explain the workings of any/all of your code to assess whether you wrote and understand the code. Also, your git commits will be examined to check how your code progresses.*


---

## What You Need to Hand In

At the end of this project you will need to submit the following:

1. The **URL of your GitHub repo**

2. **A zipped copy** of the repo above

3. **The URL of your live site** - your site must be hosted externally and live for moderation purposes


---

## Achievement Criteria for the Database

Achievement standard [91902](as91902.pdf), Use complex techniques to develop a database:


| Level          | Criteria                                                    |
| -------------- | ----------------------------------------------------------- |
| **Achieve**    | Use complex techniques to develop a database.               |
| **Merit**      | Use complex techniques to develop an **informed** database. |
| **Excellence** | Use complex techniques to develop an **refined** database.  |

*To help you keep track of how successfully you are meeting the criteria, the items below are in the form of a checklist - mark them off as you work through the project*

### Achieve Criteria

Use complex techniques to develop a database means that, taking into account the problem / need and the end users:

1. You must first define the purpose of your system and the end-users' needs:
   - [x] Define the **purpose of the system** that uses the database
   - [x] Describe the **needs of the end-users**
   - [x] Define the **key functionality** of the proposed system

2. You need to design the structure of the database:
   - [x] **Tables** - at least two that are linked by a relationship
   - [x] **Data Types** - a range of data types used
   - [x] **Key Fields** - primary keys for each table, foreign keys for relationships
   - [x] **Values** - auto-generation / default values as required
   - [x] Source and structure of **Input Data** is described
   - [x] Type and format of **Output Data** is described
   - [ ] **Processing of Data** to achieve the output is described

3. You should use appropriate tools and complex techniques to organise and query the data:
   - [x] **Linking data in related tables** using queries or keys
   - [x] Writing **custom queries** to update the data (INSERT / UPDATE / DELETE)

4. You should use appropriate tools and complex techniques to present the data:
   - [x] Creating **customised data displays from multiple tables** for web pages
   - [x] **Dynamically linking data** between the database and web pages
   - [x] Applying **data access permissions** as appropriate (user accounts)

5. You must apply appropriate data integrity and testing procedures:
   - [x] Show that any **presented data is correct** (e.g. matches database values / calculations)
   - [x] Show that any input user data **updates the database as expected**

6. You need to explain and address relevant implications:
   - [x] Identify the **implications most relevant** to your project
   - [x] Explain **what the implications mean** and **why each is relevant** to your project
   - [x] Explain **how each implication will impact your specific project** (considerations / choices / designs)
   - [ ] At the end of your project, you need to **explain what you did in your project to address each implication**

*Note: You must satisfy **all** of the criteria above to pass*


### Merit Criteria

Use complex techniques to develop an informed database means **all the criteria for Achieved**, plus:

1. You should use information from testing procedures to improve the quality of your database:
   - [x] Show **evidence of your testing**, particularly with end-users
   - [x] Show the **improvements made** as a result

2. You should structure, organise and query your data logically:
   - [x] Your tables should be **normalised** (no repeating data)
   - [x] Your fields have the **appropriate data type**, **defaults**, etc.
   - [x] Your database **queries are well-written and efficient**


### Excellence Criteria

Use complex techniques to develop a refined database means **all of the criteria for Merit**, plus:

1. You have made iterative improvements throughout the design, development and testing process:
   - [x] You have refined features of the DB (the schema and the UI) over **multiple iterations**
   - [x] Each iteration is **clearly documented**, showing testing and resulting refinements

2. You must have used efficient tools and techniques in the system's production:
   - [x] You have effectively used **version control**
   - [x] Your git **commits are regular with descriptive commit messages**
   - [x] You have **effectively used tools** like DrawSQL, Figma, VS Code, Turso SQL editor, etc. to help develop the outcome

3. You present the data from the database effectively for the purpose and end users:
   - [x] Data is displayed in ways that make its **meaning clear** (e.g. using colour)
   - [x] Data is **displayed in interesting and creative ways** to meet the needs of the user and satisfy the system requirements


---

## Achievement Criteria for the Website (Media Outcome)

Achievement standard [91903](as91903.pdf), Use complex techniques to develop a digital media outcome:


| Level          | Criteria                                                     |
| -------------- | ------------------------------------------------------------ |
| **Achieve**    | Use complex techniques to develop a digital media outcome.               |
| **Merit**      | Use complex techniques to develop an **informed** digital media outcome. |
| **Excellence** | Use complex techniques to develop an **refined** digital media outcome.  |

*To help you keep track of how successfully you are meeting the criteria, the items below are in the form of a checklist - mark them off as you work through the project*

### Achieve Criteria

Use complex techniques to develop a digital media outcome means that, taking into account the problem / need and the end users:

1. You must first define the purpose of your system and the end-users' needs:
   - [x] Define the **purpose of the system** that uses the database
   - [x] Describe the **needs of the end-users**
   - [x] Define the **key functionality** of the proposed system

2. You must use appropriate complex tools and techniques, for example:
   - [x] You have used **non-core functionality** of tools / libraries (i.e. you have extended these beyond their supplied defaults)
   - [ ] You have applied **industry standards or guidelines** (e.g. PEP 8 style guide for Python)
   - [ ] Your UI uses a **responsive design** for use on multiple devices
   - [x] You have **integrated original media assets** into your work, as needed
   - [x] You **handle data dynamically**, making your system interactive
   - [x] You have **automated aspects of your system** through scripts (e.g. Python)

3. You must apply appropriate data integrity and testing procedures:
   - [x] All webpage text should be checked for **accuracy** (e.g. spell-checked)
   - [x] Any **data shown is as expected** (i.e. matches database / calculated values)

4. You have applied user experience (UX) principles relevant to the purpose of your system:
   - [x] You have **identified key UX principles** that are relevant
   - [x] You **applied these UX principles** in your system's design and development

5. You need to explain and address relevant implications:
   - [x] Identify the **implications most relevant** to your project
   - [x] Explain **what the implications mean** and **why each is relevant** to your project
   - [x] Explain **how each implication will impact your specific project** (considerations / choices / designs)
   - [ ] At the end of your project, you need to **explain what you did in your project to address each implication**


*Note: You must satisfy **all** of the criteria above to pass*


### Merit Criteria

Use complex techniques to develop an informed digital media outcome means **all the criteria for Achieved**, plus:

1. You should use information from testing procedures to improve the quality of your web site:
   - [x] Show **evidence of your testing**, particularly with end-users
   - [x] Show the **improvements made** as a result

2. You have used testing tools to help improve your web site:
   - [ ] You have used **code validation** tools for generated HTML and CSS
   - [x] You have **fixed any issues** identified

3. You have applied user experience (UX) principles to improve the quality of your web site:
   - [ ] Show evidence that you **tested your system against identified UX principles** during development
   - [ ] Show the **improvements made** as a result


### Excellence Criteria

Use complex techniques to develop a refined digital media outcome means **all of the criteria for Merit**, plus:

1. You have made iterative improvements throughout the design, development and testing process:
   - [x] You have refined features of the web site (layout, theme, etc.) over **multiple iterations**
   - [x] Each iteration is **clearly documented**, showing testing and resulting refinements

2. You have used efficient tools and techniques in the web site's production:
   - [x] You have effectively used **version control**
   - [x] You git **commits are regular with descriptive commit messages**
   - [x] You have **effectively used tools** like DrawSQL, Figma, VS Code, Turso SQL editor, etc. to help develop the outcome
   - [x] You have made good use of **templates** (Jinja) to organise and structure content
   - [ ] Your code is **commented** as needed
   - [x] You have **optimised media assets** (e.g. image sizing)


