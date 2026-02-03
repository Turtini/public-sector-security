# Authorization Boundaries Explained

This document provides a conceptual explanation of authorization boundaries in U.S. federal systems, with a focus on how boundaries are defined and evaluated under the Federal Risk and Authorization Management Program (FedRAMP).

It is intended to clarify common points of confusion for security, audit, and procurement stakeholders.

This document is informational only and does not define or represent the authorization boundary of any specific system.

---

## What Is an Authorization Boundary?

An authorization boundary defines the scope of a system that is assessed and authorized under FedRAMP.

The boundary identifies:
- Which components are included in the authorization
- Which components are external dependencies
- Which security controls are implemented directly
- Which controls are inherited from other authorized services

Only components inside the authorization boundary are assessed as part of the FedRAMP authorization.

---

## Why Authorization Boundaries Matter

Authorization boundaries are central to FedRAMP because they determine:
- The scope of security assessment
- The responsibilities of the system owner
- Which controls can be inherited
- How changes impact authorization status

Unclear boundaries increase audit risk and often slow down authorization reviews.

---

## Common Boundary Layers in Federal Systems

Most federal cloud systems include multiple layers that may fall inside or outside an authorization boundary, such as:

- Cloud infrastructure (e.g., compute, storage, networking)
- Platform services (e.g., container platforms, managed databases)
- Operating systems
- Applications and workloads
- Identity, logging, and monitoring services

Not all layers are necessarily included inside the same authorization boundary.

---

## Inside vs. Outside the Boundary

### Components Inside the Boundary

Components inside the authorization boundary:
- Are assessed during the authorization process
- Must meet all applicable FedRAMP control requirements
- Are subject to continuous monitoring

### Components Outside the Boundary

Components outside the authorization boundary:
- Are not assessed as part of the system authorization
- May still be approved for use
- Often provide inherited controls or external services

Clear documentation is required to show how external dependencies are managed.

---

## Boundary Changes and Impact

Changes to components inside the authorization boundary may:
- Require reassessment
- Trigger documentation updates
- Impact authorization status

Changes outside the boundary may still require review if they affect inherited controls or system risk.

---

## Common Misconceptions

- **“Everything in the stack is authorized.”**  
  Authorization applies only to components within the defined boundary.

- **“Using authorized infrastructure makes my system authorized.”**  
  Authorization requires a defined boundary and assessment, even when controls are inherited.

- **“Boundaries are static.”**  
  Boundaries may evolve as systems change.

---

## Summary

Authorization boundaries define what is assessed, what is inherited, and who is responsible. Clear boundary definitions support efficient audits, accurate risk assessments, and scalable system design.

This document exists to explain the concept—not to define any specific system boundary.

---

## Related Resources

- [FedRAMP Explained](fedramp.md)
- [Frequently Asked Questions](faq.md)
- [Repository Overview](README.md)
