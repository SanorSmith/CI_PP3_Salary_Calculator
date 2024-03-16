# Salary Calculator [Visit live website](https://salary-calculater-2dcdcf65c7ea.herokuapp.com//)

**Developer: Sanor Smith**

![Mockup image](docs/screenshot-home.JPG)

## About

Salary Calculator is an innovative and user-centric application developed with the objective of simplifying the complex task of salary computation for both individuals and companies. It stands as a testament to the fusion of technological advancement and financial management, aiming to transform the often daunting task of salary calculations into a straightforward, efficient process. By accommodating both individual users and businesses, the application showcases versatility, making it a suitable tool for diverse financial needs. Its robust user registration system ensures a personalized and secure experience, while the dual-mode functionality offers tailored interfaces and calculations for both single users and companies.

## Table of Contents
  - [Project Goals](#project-goals)
    - [User Goals](#user-goals)
    - [Site Owner Goals](#site-owner-goals)
  - [User Experience](#user-experience)
    - [Target Audience](#target-audience)
    - [User Requirements and Expectations](#user-requirements-and-expectations)
    - [User Manual](#user-manual)
  - [User Stories](#user-stories)
    - [Users](#users)
    - [Site Owner](#site-owner)
  - [Technical Design](#technical-design)
    - [Flowchart](#flowchart)
  - [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks & Tools](#frameworks--tools)
    - [Libraries](#libraries)
  - [Features](#features)
  - [Validation](#validation)
  - [Testing](#testing)
    - [Manual Testing](#manual-testing)
    - [Automated Testing](#automated-testing)
  - [Bugs](#bugs)
  - [Deployment](#deployment)
  - [Credits](#credits)
  - [Acknowledgements](#acknowledgements)

## Project Goals

### User Goals

- Make salary computations easy and understandable for both individuals and businesses.
- Provide precise salary and tax calculations, incorporating specific factors like VAT and regional tax rates.
- Save time and reduce the effort involved in managing and calculating salaries.
- Offer a user-friendly and intuitive interface suitable for all skill levels.
- Implement robust validation to prevent mistakes in financial calculations.
- Help users understand salary structures and deductions clearly.

### Site Owner Goals

- User Engagement: Increase the number of active users and foster user retention.
- Reliability and Accuracy: Ensure the application consistently delivers accurate salary computations.
- User Feedback Incorporation: Regularly update and improve the application based on user feedback.
- Reach a broader audience, including individuals and businesses of various sizes.
- Promote Financial Education: Educate users about salary structures and financial management.
- Data Security: Maintain the highest levels of data privacy and security for user information.

## User Experience

### Target Audience
- People seeking to calculate their daily or monthly net income after taxes and deductions.
- Entrepreneurs who need to manage payroll for a few employees but might not have a dedicated HR department.
- Those pursuing education in business or finance who require practical tools for understanding payroll management.
- Individuals or professionals who help others in preparing and filing tax returns, including salary tax calculations.
- Users comfortable with using digital tools and applications for personal finance management.

### User Requirements and Expectations

#### User Requirements

- Access to a computer or a mobile device with a compatible operating system to run the application.
- Ability to navigate basic computer or mobile applications.
- For accessing cloud-based features like data storage and real-time tax rate updates.
- Necessary information such as name, number of days worked, daily salary, and email for registration or login.

#### User Expectations

- Accuracy and Reliability: Expectation of precise calculations for net salary, taxes, and VAT.
- Ease of Use: A user-friendly interface that is easy to navigate, even for those with limited technical skills.
- Data Security: Assurance that all personal and financial information entered is securely handled and stored.
- Speed and Efficiency: Quick processing and generation of results without long waiting times.

### User Manual

<details><summary>Click here to view instructions</summary>

Using the Salary Calculator involves several steps, providing a user-friendly experience from start to finish. Here's a detailed guide on how a user would typically use the application:

#### Starting the Application

- Launch: Begin by running main.py. The application opens with the Salary Calculator logo, setting the professional tone of the tool.
- Proceed: Press Enter to move from the logo screen to the main menu.

#### Welcome and User Identification

- New or Returning User: The first prompt asks if you've used the Salary Calculator before. Answer "yes" or "no".
- Registration (for New Users): If you're new, you'll be guided to register. Input your name and email. A confirmation message will appear upon successful registration.
- Login (for Returning Users): If you're a returning user, input your email. A welcome back message is displayed for recognized emails.

#### Choosing the User Type

- Select User Type: You'll choose between an individual or a company. This tailors the experience to your needs.

#### Input Salary Details

- Data Entry for Individuals: Enter your name, the number of working days, and your daily salary.
- Data Entry for Companies: If you represent a company, input the number of employees first. Then, repeat the individual data entry process for each employee.

#### VAT and Salary Calculation

- Selection of Job Category and County: You will choose your job category and county from given lists, which are used to calculate VAT and local taxes.
- Automatic Calculations: The app calculates total salary, VAT, taxes, and net salary based on the provided information.

#### Reviewing the Results

- Result Display: A detailed breakdown of the salary calculation, including deductions, is shown.
- Printing Option (for Companies): Companies have the option to print the salary summary for record-keeping.

#### Restarting or Exiting

- Decision Point: After viewing the results, decide whether to restart the application for a new calculation or exit.
- Restart or Exit: Choose "restart" to perform another calculation or "exit" to close the application. A farewell message is displayed if you're exiting.

#### Error Handling and Correction

- Invalid Inputs: If an invalid entry is made, the application prompts for correction, guiding you to provide the valid input.
- Continued Interaction: The app ensures that you are continually guided through correct input until the desired action is completed.

Throughout this process, the Salary Calculator is designed to be intuitive and user-friendly, guiding users through each step with clear instructions and prompts, ensuring a smooth experience from beginning to end.