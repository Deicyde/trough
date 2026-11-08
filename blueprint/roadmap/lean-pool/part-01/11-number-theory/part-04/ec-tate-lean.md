---
declaration: structure
origin: cited
lean: Model, Model.Field.isSingularPoint_singularPoint
statement: formalized
---

# Weierstrass models and singular points for Tate's algorithm

> Formalizes Weierstrass models of elliptic curves over a commutative ring, their b- and c-invariants and discriminant, the change-of-coordinates group action, the discriminant's membership in the Jacobian ideal, and the construction of the singular point of a singular model over a perfect field, together with the Kronecker symbol and the Kodaira type enumeration.

*Quoted from the card [LeanPool/projects/ec-tate-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ec-tate-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Model`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model) (structure; a main declaration), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 46](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L46): “Defines a Weierstrass model of a possibly singular elliptic curve by its five a-invariants.”
- [`Model.discr_identity`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model.discr_identity) (lemma), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 98](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L98): “Proves the identity relating the discriminant to the c-invariants, 1728 \* discr = c4^3 - c6^2.”
- [`Model.rst_discr`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model.rst_discr) (lemma), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 202](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L202): “Proves that the discriminant is invariant under the rst change-of-coordinates transformation.”
- [`Model.discr_in_jacobian_ideal`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model.discr_in_jacobian_ideal) (lemma), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 275](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L275): “Expresses the discriminant as an explicit combination of the Weierstrass polynomial and its partial derivatives, witnessing membership in the Jacobian ideal.”
- [`Model.discr_eq_zero_of_singular`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model.discr_eq_zero_of_singular) (lemma), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 440](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L440): “Proves that a model with a singular point has vanishing discriminant.”
- [`Model.Field.isSingularPoint_singularPoint`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.html#Model.Field.isSingularPoint_singularPoint) (lemma; a main declaration), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean, line 523](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/Model.lean#L523): “Proves that the explicitly constructed singular point of a singular model over a perfect field is indeed a singular point (Connell, Proposition 1.5.4).” Its source, as the card gives it: “Ian Connell, Elliptic Curve Handbook, February 1999, Proposition 1.5.4.”
- `Model.Field.move_singular_point_to_origin`, which the scan does not find declared in the project's files at this commit: “Proves that the change of coordinates moving the singular point places it at the origin.”
- [`Kodaira`](https://leanpool.github.io/lean-pool/LeanPool/EcTateLean/Algebra/EllipticCurve/KodairaTypes.html#Kodaira) (inductive), declared in [LeanPool/EcTateLean/Algebra/EllipticCurve/KodairaTypes.lean, line 24](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean/Algebra/EllipticCurve/KodairaTypes.lean#L24): “Enumerates the Kodaira reduction types, including the extra types arising over imperfect residue fields of characteristic 2 or 3.”

## Project

- Authors: Sacha H., Sander R. Dahmen, Anne Baanen, Alex J. Best.
- Source: *Elliptic Curve Handbook* by Ian Connell, [https://www.math.rug.nl/~top/ian.pdf](https://www.math.rug.nl/~top/ian.pdf).
- Project repository: [KisaraBlue/ec-tate-lean](https://github.com/KisaraBlue/ec-tate-lean).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 11G05, 11G07, 14H52.
- In Lean Pool: [LeanPool/EcTateLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean), from the card [LeanPool/projects/ec-tate-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ec-tate-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/ec-tate-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/ec-tate-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/EcTateLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/EcTateLean)
