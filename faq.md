# Frequently Asked Questions (FAQ)

This FAQ addresses common questions related to FedRAMP, authorization boundaries, and the use of platform technologies in U.S. federal environments.

The answers are intentionally concise and focus on clarifying common misconceptions rather than providing implementation guidance.

For background and detailed explanations, see:
- [FedRAMP Explained](fedramp.md)
- [Repository Overview](README.md)

---

## Is Red Hat “FedRAMP approved”?

No.

FedRAMP authorization is **service-specific**, not vendor-wide. A company or product is not “FedRAMP approved” in the abstract.

Certain managed services offered by Red Hat maintain FedRAMP authorizations depending on the service configuration and deployment environment. Other Red Hat products are commonly approved for use **within** FedRAMP-authorized systems but are not themselves authorized services.

---

## Is Red Hat Enterprise Linux (RHEL) FedRAMP authorized?

No.

Red Hat Enterprise Linux is not a FedRAMP-authorized service. It is, however, widely deployed within FedRAMP-authorized systems and commonly approved by federal security teams as a foundational operating system component.

---

## Is Ansible FedRAMP authorized?

No.

Automation platforms such as Ansible are typically used within authorized boundaries to support configuration management, patching, and compliance enforcement. They are not authorization boundaries themselves.

---

## Does using FedRAMP-authorized infrastructure make my system FedRAMP authorized?

No.

Using FedRAMP-authorized infrastructure may allow a system to **inherit security controls**, but the system itself must still define an authorization boundary and undergo an authorization process.

---

## What is an authorization boundary?

An authorization boundary defines which components are included in a system’s FedRAMP assessment and which components are external dependencies.

Only components inside the boundary are assessed as part of the authorization. Components outside the boundary may still be approved for use but are not themselves authorized services.

---

## What is control inheritance?

Control inheritance allows a system to reuse security controls that are already implemented and assessed by another authorized service.

This reduces duplication while maintaining accountability for system-specific controls.

---

## Where can FedRAMP authorization status be verified?

FedRAMP authorization status and details are publicly available through the FedRAMP Marketplace.

Authorization details should always be verified per service and per environment.

---

## Does this repository represent official authorization guidance?

No.

This repository provides informational and explanatory guidance only. It does not replace official security documentation, authorization artifacts, or agency determinations.
