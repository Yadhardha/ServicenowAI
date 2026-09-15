# 🚨 Incident Automation Platform

An end-to-end incident automation platform that connects **ServiceNow, n8n, Ansible/AWX, and Gmail** to automate incident processing, troubleshooting, notifications, and incident updates.

The goal is to reduce repetitive manual operations by connecting incident management with infrastructure automation and creating a closed-loop workflow from incident creation to automation execution and final incident update.

---

## 🎯 Problem

Traditional infrastructure incident handling often requires engineers to manually:

- Review newly created incidents
- Identify the affected device or service
- Determine the appropriate troubleshooting procedure
- Execute troubleshooting or automation
- Review the execution result
- Notify the relevant team
- Update the incident with the final outcome

When the same process is repeated across multiple incidents, it can consume significant operational time and may lead to inconsistent incident updates.

---

## 💡 Solution

This project automates the incident workflow by integrating **ServiceNow, n8n, and Ansible/AWX**.

When an incident enters the workflow:

1. Incident information is received from ServiceNow.
2. n8n processes and orchestrates the workflow.
3. n8n triggers the required Ansible/AWX automation.
4. AWX executes the Ansible troubleshooting workflow.
5. Execution status and results are captured.
6. Gmail sends a notification containing the execution result.
7. The original ServiceNow incident is automatically updated using the ServiceNow REST API.

This creates a closed-loop incident automation workflow.

---

## 🔄 Closed-Loop Automation

```mermaid
flowchart LR
    A[ServiceNow<br/>Incident Created]
    B[n8n<br/>Workflow Engine]
    C[Ansible AWX<br/>Job / Workflow]
    D[Ansible<br/>Automation]
    E[Automated<br/>Troubleshooting]
    F[Execution<br/>Result]
    G[Gmail<br/>Notification]
    H[ServiceNow<br/>Incident Update]

    A -->|Incident Data| B
    B -->|API Trigger| C
    C --> D
    D --> E
    E --> F
    F -->|Notification| G
    F -->|PATCH / REST API| H
    H --> A


🔄 End-to-End Workflow
1. Incident Creation

A new incident is created in ServiceNow.

Example:

Incident Number : INC0012345
Priority        : High
Category        : Network
Description     : Device connectivity issue
Status          : Open

The incident becomes the starting point of the automation workflow.

2. Incident Processing

n8n acts as the workflow orchestration layer.

The workflow processes relevant incident information such as:

Incident Number
Short Description
Description
Priority
Category
Affected Device / Host
Incident Status

The required information is then passed to the automation workflow.

3. Trigger Ansible/AWX

n8n communicates with Ansible AWX through its API.

The basic flow is:

n8n
 │
 │ API Request
 ▼
AWX
 │
 ▼
Job Template / Workflow

AWX manages the execution of the corresponding Ansible automation.

4. Automated Troubleshooting

Ansible executes the predefined troubleshooting workflow.

Depending on the incident type, automation can perform activities such as:

Device reachability checks
Connectivity checks
Interface checks
Service checks
System health checks
Command execution
Configuration validation

The exact troubleshooting actions depend on the automation workflow configured for the incident.

5. Execution Result

Once the AWX job completes, the workflow captures the execution result.

Example:

AWX Job ID : 1024
Status     : Successful
Result     : Troubleshooting completed successfully

For a failed execution:

AWX Job ID : 1025
Status     : Failed
Result     : Automation execution failed

The execution result is then passed back into the n8n workflow for further processing.

6. Gmail Notification

The workflow sends an email notification containing the relevant execution information.

Example:

Subject:
Incident INC0012345 - Automation Result

Incident:
INC0012345

Automation Status:
Completed

Result:
Troubleshooting workflow completed successfully.

AWX Job:
1024

This provides visibility into the automation result without requiring the engineer to manually check the AWX execution.

7. ServiceNow Incident Update

After the automation completes, the workflow updates the original ServiceNow incident using the ServiceNow REST API.

Example:

Incident:
INC0012345

Automation Status:
Completed

Execution Result:
Troubleshooting workflow completed successfully.

AWX Job:
1024

This creates a complete feedback loop between incident management and automation.

Incident Created
       ↓
Incident Processing
       ↓
Automation Triggered
       ↓
Troubleshooting
       ↓
Execution Result
       ↓
Gmail Notification
       ↓
ServiceNow Incident Update


🧩 Technology Stack
Technology	Purpose
Python	Automation and application logic
ServiceNow	Incident management
n8n	Workflow orchestration
Ansible	Infrastructure automation
Ansible AWX	Centralized automation execution
REST APIs	System-to-system integration
Gmail	Automated notifications
Docker	Containerization
GitHub Actions	CI/CD automation
Git	Version control
