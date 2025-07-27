# Design of Experiments (DOE) – CSE 565 Assignment

This repository contains the test design and analysis for a mobile application using Design of Experiments (DOE) techniques. The project compares the effectiveness of test case generation between a DOE tool (CAGen) and a generative AI tool (ChatGPT).

# Objective

- Apply DOE principles to generate pairwise test cases
- Use both a DOE tool and generative AI to design test cases
- Compare the structure, coverage, and usability of the test cases
- Evaluate the performance and practicality of each tool

# Component	Tool / Technology
DOE Tool	- CAGen
Generative AI Tool	- ChatGPT 4.0 mini

# Files Included

| File Name                        | Description                                             |
|----------------------------------|---------------------------------------------------------|
|  Report.pdf                      | Full project report with analysis                       |
|  Requirements.pdf                | Document specifying DOE testing goals and requirements  |

# Application Specification

The test cases are based on a mobile app requiring the following user input parameters:

Type of Phone: iPhone 14, iPhone 13, Galaxy Z, Huawei Mate, Google Pixel 7
Authentication: Fingerprint, Face recognition, Text Password, 5G Edge
Connectivity: Wireless, 3G, 4G LTE
Memory: 128 GB, 256 GB, 512 GB, 1 TB
Battery Level: <20%, 20–39%, 40–59%, 60–79%, 80–100%

# Test Case Generation

**1. Using DOE Tool (CAGen)**
Created 25 test cases using pairwise (2-way) coverage
Structured, non-redundant combinations
Easy interface with export functionality (.csv, clipboard, etc.)
**2. Using Generative AI (ChatGPT)**
Prompt-based generation using ChatGPT 4.0 mini
Produced 15 test cases covering multiple combinations
Less structured, some gaps in coverage

# Results Summary

| Metric              | CAGen (DOE Tool)       | ChatGPT (AI Tool)         |
|---------------------|------------------------|---------------------------|
| Total Test Cases    | 25                     | 15                        |
| Coverage            | High (2-way complete)  | Moderate (some missing)   |
| Structure           | Well-organized         | Mixed / Unstructured      |
| Ease of Use         | Simple UI, manual steps| Very easy, one prompt     |
| Export Options      | Multiple formats       | Copy-paste only           |




