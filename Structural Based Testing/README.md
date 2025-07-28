# Structural-Based Testing Assignment – CSE 565

# Overview

This project is part of the coursework for CSE 565: Software Verification and Validation. It is divided into two parts, each designed to build practical understanding of structural-based testing techniques in Java applications.

- **Part 1:** Focuses on analyzing code coverage using statement and decision coverage criteria on the `VendingMachine.java` class. Test cases are developed using JUnit, and JaCoCo is used to measure and report coverage.
- **Part 2:** Concentrates on identifying data flow anomalies in `StaticAnalysis.java` using a static analysis tool. PMD is used to detect issues such as uninitialized variables and improper data handling.

# Tools and Technologies Used

- Java 
- Maven (Build Automation Tool)
- JUnit (Unit Testing Framework)
- JaCoCo (Code Coverage Tool)
- PMD (Static Code Analysis Tool)

# Installation 
brew install maven 
mvn -version
mvn archetype:generate -DgroupId=com.example -DartifactId=structural-based-testing -DarchetypeArtifactId=maven-archetype-quickstart -DinteractiveMode=false

Add Jacoco and PMD plugin to pom.xml file in the structure and place main files in sources and test file in test folder.


## Project Structure

structural-based-testing/
├── pom.xml
├── src/
│ ├── main/
│ │ └── java/
│ │ └── com/example/
│ │ ├── VendingMachine.java
│ │ └── StaticAnalysis.java
│ └── test/
│ └── java/
│ └── com/example/
│ └── VendingMachineTest.java


# Part 1: Code Coverage Analysis with JaCoCo

# Requirements

- Accept an integer input from the user.
- Allow users to select between three products: Candy (20 cents), Coke (25 cents), and Coffee (45 cents).
- Return the selected product and any remaining change.
- Display the additional amount needed if the user has insufficient funds.

# Procedure

1. Test cases were developed in the `VendingMachineTest.java` file under the `src/test/java` directory.
2. The Maven JaCoCo plugin was used to generate statement and decision coverage reports.
3. Tests were executed using the following command:

mvn clean test jacoco:report

4. Coverage results can be found in the generated HTML report at:

target/site/jacoco/index.html

# Target Coverage

- 100% statement coverage
- At least 90% decision (branch) coverage

# Part 2: Static Analysis with PMD

# Objective

To detect data flow anomalies and assess the effectiveness of static code analysis tools on Java source code.

# Procedure

1. The PMD plugin was integrated into the Maven configuration.
2. The code in `StaticAnalysis.java` was analyzed for potential data flow issues.
3. Static analysis was executed using the following command:

mvn clean verify

4. The PMD report is generated at:

target/site/pmd.html

# Expected Output

- Detection of two known anomalies built into the `StaticAnalysis.java` file.
- Evaluation of PMD’s report.

# Build and Execution Instructions

To build the project, run tests, and generate all reports, execute the following commands from the root directory:

mvn clean test jacoco:report verify