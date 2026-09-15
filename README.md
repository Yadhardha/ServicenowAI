# Incident Automation Platform

An end-to-end incident automation platform that connects ServiceNow,
n8n, Ansible/AWX, and Gmail to automate incident processing,
troubleshooting, notifications, and incident updates.

---

## 🎥 Video Demo

▶️ [Watch the 60-Second Demo](YOUR_DEMO_LINK)

---

## 🎯 Problem

Traditional incident handling often requires engineers to manually:

- Review newly created incidents
- Identify the affected device or service
- Start troubleshooting
- Execute automation
- Review the automation results
- Notify the relevant team
- Update the incident with the outcome

This process can be repetitive and time-consuming.


## 💡 Solution

This project automates the incident workflow by connecting
ServiceNow, n8n, and Ansible/AWX.

When an incident is received, the workflow processes the incident,
triggers the required automation, captures the execution result,
sends a Gmail notification, and automatically updates the
corresponding ServiceNow incident.

---

## 🏗️ Architecture

```text
                    ┌──────────────────┐
                    │    ServiceNow    │
                    │     Incident     │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │       n8n        │
                    │ Workflow Engine  │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │    AWX /         │
                    │    Ansible       │
                    └────────┬─────────┘
                             │
                             ▼
                    ┌──────────────────┐
                    │   Automated      │
                    │  Troubleshooting │
                    └────────┬─────────┘
                             │
                             ▼
                       Execution Result
                             │
                    ┌────────┴─────────┐
                    │                  │
                    ▼                  ▼
              Gmail Notification   ServiceNow
                                      Update
