# Serverless FinOps Automation 💰⚡

## Project Overview
In fast-moving cloud environments, it is incredibly common for engineers to delete virtual machines but forget to delete the attached storage volumes. These "orphaned" resources sit in the background and quietly drain the IT budget. 

This project solves that problem by implementing a serverless automation that continuously hunts down and eliminates wasted cloud spend.

## The Architecture
![Architecture Diagram](finops-serverless-architecture.png)

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
