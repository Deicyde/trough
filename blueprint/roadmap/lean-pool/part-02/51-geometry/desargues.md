---
declaration: class
origin: cited
lean: Basic.ProjectiveGeometry, Basic.centralProjection, Basic.cen_proj_bij
statement: formalized
---

# Axiomatic projective geometry (Faure–Frölicher)

> Develops, following Faure and Frölicher's Modern Projective Geometry, the axiomatic theory of projective geometries given by a ternary collinearity relation, with subspaces and subgeometries, proves that the central projection between two lines is a bijection, and exhibits every Mathlib projectivization as a projective geometry. Groundwork from the upstream desargues repository — Desargues' theorem itself is not formalized.

*Quoted from the card [LeanPool/projects/desargues.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/desargues.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Basic.ProjectiveGeometry`](https://leanpool.github.io/lean-pool/LeanPool/Desargues/Basic.html#Basic.ProjectiveGeometry) (class; a main declaration), declared in [LeanPool/Desargues/Basic.lean, line 117](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Desargues/Basic.lean#L117): “Axiomatizes a projective geometry as a typeclass (axioms L₁–L₃, Faure–Frölicher p. 26) on a ternary collinearity relation.”
- [`Basic.centralProjection`](https://leanpool.github.io/lean-pool/LeanPool/Desargues/Basic.html#Basic.centralProjection) (def; a main declaration), declared in [LeanPool/Desargues/Basic.lean, line 394](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Desargues/Basic.lean#L394): “Defines the central projection of a line onto another from a center point.”
- [`Basic.cen_proj_bij`](https://leanpool.github.io/lean-pool/LeanPool/Desargues/Basic.html#Basic.cen_proj_bij) (theorem; a main declaration), declared in [LeanPool/Desargues/Basic.lean, line 657](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Desargues/Basic.lean#L657): “The headline theorem — the central projection between two lines is a bijection.”

## Project

- Authors: Abdullah Uyu.
- Source: *Modern Projective Geometry* by Claude-Alain Faure, Alfred Frölicher, [doi:10.1007/978-94-015-9590-2](https://doi.org/10.1007/978-94-015-9590-2).
- Project repository: [oneofvalts/desargues](https://github.com/oneofvalts/desargues).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 51A05, 51A30.
- In Lean Pool: [LeanPool/Desargues](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Desargues), from the card [LeanPool/projects/desargues.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/desargues.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/desargues.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/desargues.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Desargues](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Desargues)
