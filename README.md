# Serverless FinOps Automation 💰⚡

## Project Overview
In fast-moving cloud environments, it is incredibly common for engineers to delete virtual machines but forget to delete the attached storage volumes. These "orphaned" resources sit in the background and quietly drain the IT budget. 

This project solves that problem by implementing a serverless automation that continuously hunts down and eliminates wasted cloud spend.

## The Architecture
![Architecture Diagram](finops-serverless-architecture.drawio.png)

## The Solution
I engineered a lightweight, event-driven Python script using the `boto3` SDK to act as an automated FinOps auditor. 
1. **The Trigger:** An Amazon EventBridge rule is configured to trigger on a nightly cron schedule.
2. **The Compute:** The event triggers an AWS Lambda function running my custom Python script.
3. **The Execution:** The script scans the entire AWS account, identifies any EBS (Elastic Block Store) volumes with an "available" status (meaning they are detached and unused), and automatically terminates them.

## The Business Impact
* **Immediate Cost Reduction:** Automatically stops budget bleed from unattached storage volumes.
* **Operational Efficiency:** Replaces manual billing audits with a zero-maintenance, serverless automation.

## Core Technologies
* **Cloud Provider:** AWS
* **Compute:** AWS Lambda (Serverless)
* **Scheduling:** Amazon EventBridge
* **Language:** Python
* **AWS SDK:** Boto3

## Simulated Case Study: Unattached EBS Volume Cost Optimization

**Situation:** The organization noticed a consistent month-over-month increase in AWS storage costs. A billing audit revealed this was driven primarily by developers terminating EC2 instances after testing, but forgetting to delete the attached EBS (Elastic Block Store) volumes.

**Task:** My objective was to implement a zero-maintenance, automated solution to continuously hunt down and eliminate these "orphaned" storage volumes before they could permanently bloat the monthly budget.

**Action:** I deployed this serverless Python automation script using AWS Lambda and Amazon EventBridge. I configured an EventBridge cron rule to trigger the Lambda function every night at midnight. Upon execution, the Boto3 script scanned the entire AWS account for any EBS volumes with an "available" state (indicating they were detached and unused), logged the volume IDs to CloudWatch, and automatically issued a delete command.

**Result:** During its initial execution, the script successfully identified and deleted over 50 orphaned EBS volumes, resulting in an immediate $1,200 reduction in the monthly AWS bill. The continuous nightly scans have permanently stopped this budget leak with absolutely zero manual intervention required from the engineering team.
