# FedRAMP Explained

This document provides a practical, plain-language explanation of the Federal Risk and Authorization Management Program (:contentReference[oaicite:0]{index=0}) and how it is commonly applied in real federal environments.

It is intended to support security, procurement, and audit conversations by clarifying common points of confusion.

This document is informational only and does not assert authorization status for any specific system or deployment.

---

## What FedRAMP Is — and Is Not

FedRAMP is a U.S. government program that standardizes the assessment, authorization, and continuous monitoring of cloud services used by federal agencies.

FedRAMP:
- Applies to **cloud services**, not organizations
- Authorizes **specific service offerings**
- Is tied to **defined environments and impact levels**
- Requires **ongoing continuous monitoring**

FedRAMP is **not**:
- A blanket approval for a vendor
- A one-time certification
- A guarantee that all uses of a product are authorized

---

## Authorization Is Service-Specific

A FedRAMP authorization applies only when **all** of the following are true:

- The service offering matches the authorized configuration
- The deployment environment matches the authorized boundary
- The impact level aligns with the authorized designation
- Required controls are implemented and monitored continuously

Changes to service architecture, deployment model, or environment may invalidate authorization inheritance.

---

## Impact Levels

FedRAMP authorizations are issued at defined impact levels based on FIPS 199 categorizations:

- **Low** — Limited adverse effect
- **Moderate** — Serious adverse effect
- **High** — Severe or catastrophic adverse effect

Each impact level carries an increasing number of required security controls derived from NIST SP 800-53.

---

## Authorization Boundaries

A FedRAMP authorization includes a clearly defined **authorization boundary**, which identifies:

- What components are inside the authorized system
- What components are external dependencies
- Which controls are inherited versus implemented directly

Understanding the boundary is critical. Components *inside* the boundary are assessed as part of the authorization. Components *outside* the boundary may still be approved for use but are not themselves authorized services.

---

## Shared Responsibility Models

Most federal cloud systems rely on shared responsibility across multiple layers, including:

- Cloud infrastructure providers
- Platform services
- Operating systems
- Application layers
- Agency-specific configurations and processes

FedRAMP assessments evaluate how responsibilities are divided and how controls are inherited, implemented, or supplemented across these layers.

---

## Control Inheritance in Practice

Control inheritance allows agencies to reuse approved security controls rather than re-implementing them independently.

Common examples include:
- Inheriting physical and environmental controls from cloud providers
- Inheriting platform-level controls from managed services
- Implementing agency-specific controls at the application or data layer

Inheritance reduces duplication while maintaining accountability.

---

## Verification and Transparency

FedRAMP authorization details are publicly available through the FedRAMP Marketplace, including:

- Authorized services
- Impact levels
- Sponsoring agencies
- Authorization status

Agencies and partners should always verify authorization details directly rather than relying on secondary claims.

---

## Summary

FedRAMP enables secure, scalable cloud adoption by standardizing authorization and continuous monitoring. Accurate understanding requires attention to service scope, authorization boundaries, and shared responsibility models.

This document exists to support that understanding.
