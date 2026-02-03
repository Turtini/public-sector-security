# Public Sector Security

This repository provides clear, audit-safe guidance on how public sector security and compliance are commonly evaluated and implemented, with a focus on practical alignment to U.S. federal requirements such as FedRAMP environments.

The intent is to support informed discussions with:
- Federal customers
- General Services (GS) personnel
- System owners, ISSOs, and security teams
- Integrators and audit partners

## Repository Contents

- **[FedRAMP Explained](fedramp.md)**  
  A plain-language overview of FedRAMP, authorization boundaries, impact levels, and shared responsibility models.

- **[Frequently Asked Questions](faq.md)**  
  Concise answers to common FedRAMP and compliance questions encountered in federal security and audit discussions.

This content is informational and explanatory in nature. It does not replace formal authorization artifacts, security documentation, or agency-specific compliance determinations.

---

## Why This Repository Exists

Security and compliance conversations in the public sector are often slowed by ambiguity around:
- What is actually authorized vs. what is approved for use
- Where authorization boundaries begin and end
- How shared responsibility models work in practice
- Which components inherit controls versus implement them directly

This repository exists to clarify those distinctions in plain language, using patterns that reflect how federal systems are evaluated in the real world.

---

## FedRAMP: Foundational Context

FedRAMP authorization is **service-specific**, not vendor-wide.

- Authorization applies to a specific service
- In a specific environment
- At a defined impact level
- With a documented authorization boundary

No vendor, platform, or product is “FedRAMP approved” in the abstract. Understanding this distinction is essential for accurate security and procurement discussions.

---

## Red Hat Alignment with FedRAMP

Red Hat aligns with FedRAMP requirements through a combination of managed services, platform security controls, and long-standing alignment with federal security frameworks.

Rather than asserting blanket authorization, Red Hat’s approach reflects how FedRAMP is implemented in practice:

- Certain managed OpenShift services maintain FedRAMP authorizations depending on cloud environment and configuration
- Foundational platforms such as operating systems and automation tooling are commonly approved for use within FedRAMP-authorized boundaries
- Platform security controls align closely with NIST SP 800-53 requirements and federal hardening guidance

This model enables agencies to inherit controls where appropriate, reuse approved components, and avoid duplicative compliance work while maintaining accountability.

Key takeaway:
Red Hat supports FedRAMP-aligned architectures by enabling control inheritance and repeatable security patterns, rather than treating authorization as a one-time or vendor-wide designation.

---

## Managed OpenShift Services

Select managed OpenShift offerings maintain FedRAMP authorizations depending on service configuration and cloud environment. These services typically leverage:

- FedRAMP-authorized cloud infrastructure
- Platform-level security controls provided by Red Hat
- Continuous monitoring and vulnerability management processes

**Key takeaway:**  
Managed platform services allow agencies to inherit controls rather than implement the full FedRAMP control set independently.

---

## Foundational Platforms Within Authorized Boundaries

### Red Hat Enterprise Linux (RHEL)

Red Hat Enterprise Linux is not a FedRAMP-authorized service on its own. It is, however:

- Commonly deployed within FedRAMP-authorized systems
- Frequently included inside authorization boundaries
- Widely accepted by federal security teams

RHEL supports:
- NIST 800-53 control alignment
- STIG-based hardening
- FIPS-validated cryptography

**Key takeaway:**  
RHEL functions as a trusted foundational component rather than the authorization boundary itself.

---

### Red Hat Ansible Automation Platform

Automation platforms such as Ansible are typically used within an authorized boundary to:

- Enforce configuration baselines
- Remediate drift
- Support patching and vulnerability management
- Enable repeatable, auditable changes

From a compliance perspective, automation reduces operational risk by increasing consistency and traceability.

---

## Shared Responsibility in Practice

Public sector systems rarely rely on a single authorization boundary. Instead, they use layered responsibility models that include:

- Cloud service providers
- Platform services
- Operating systems
- Automation and operational tooling
- Agency-specific configurations and controls

This layered approach enables reuse, inheritance, and scalability while maintaining accountability.

---

## Verification and Due Diligence

- FedRAMP authorizations for managed services are publicly listed in the FedRAMP Marketplace
- Authorization details should always be validated per service and environment
- This repository does not assert authorization status for any specific deployment

---

## How to Use This Repository

This repository is intended to:
- Support security and procurement conversations
- Provide shared language for compliance discussions
- Clarify common points of confusion for auditors and stakeholders

It is not intended to:
- Replace official security documentation
- Serve as an authorization artifact
- Provide implementation-specific guidance

---

## Licensing and Reuse

This content is published under the Creative Commons Zero (CC0) license and may be reused without restriction.

---

## Maintained By

**Turtini LLC**  
Public sector–focused technology consultancy and reseller  

https://turtini.github.io
