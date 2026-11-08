---
declaration: instance
origin: cited
lean: PuiseuxSeries.isAlgClosure
statement: formalized
---

# Puiseux's theorem

> Constructs Puiseux series as the bounded-denominator subfield of rational-exponent Hahn series. Proves that this field is algebraic over Laurent series over any coefficient field, and is an algebraic closure when the coefficient field is algebraically closed of characteristic zero. The Newton-Puiseux proof includes reusable Hensel splitting and polynomial translation lemmas. Dean Cureton directed the AI formalization and subsequently simplified its proofs.

*Quoted from the card [LeanPool/projects/puiseux.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/puiseux.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`PuiseuxSeries.isAlgClosure`](https://leanpool.github.io/lean-pool/LeanPool/Puiseux/AlgClosed.html#PuiseuxSeries.isAlgClosure) (instance; a main declaration), declared in [LeanPool/Puiseux/AlgClosed.lean, line 436](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux/AlgClosed.lean#L436): “For an algebraically closed field K of characteristic zero, the field of Puiseux series over K is an algebraic closure of the Laurent series field K((t)).”
- [`PuiseuxSeries.isAlgebraic`](https://leanpool.github.io/lean-pool/LeanPool/Puiseux/Algebraic.html#PuiseuxSeries.isAlgebraic) (instance), declared in [LeanPool/Puiseux/Algebraic.lean, line 124](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux/Algebraic.lean#L124): “Over any field K, the Puiseux series field is algebraic over the Laurent series field.”
- [`PuiseuxSeries.mem_subfield_iff_support`](https://leanpool.github.io/lean-pool/LeanPool/Puiseux/Basic.html#PuiseuxSeries.mem_subfield_iff_support) (theorem), declared in [LeanPool/Puiseux/Basic.lean, line 139](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux/Basic.lean#L139): “A rational-exponent Hahn series belongs to the Puiseux subfield if and only if its support lies in (1/n) times the integers for some positive integer n.”
- [`Polynomial.Monic.exists_factorization_rootMultiplicity`](https://leanpool.github.io/lean-pool/LeanPool/Puiseux/HenselSplitting.html#Polynomial.Monic.exists_factorization_rootMultiplicity) (theorem), declared in [LeanPool/Puiseux/HenselSplitting.lean, line 116](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux/HenselSplitting.lean#L116): “A monic degree-m polynomial over K[[t]] whose reduction has a root of multiplicity k, with 0 < k < m, factors into monic polynomials of degrees k and m-k.”

## Project

- Authors: Dean Cureton.
- Source: *Puiseux's theorem in Lean 4*, [https://github.com/deancureton/Puiseux/tree/73e78681d7bb78ddb202e29cb92ab3c16b723126](https://github.com/deancureton/Puiseux/tree/73e78681d7bb78ddb202e29cb92ab3c16b723126).
- Project repository: [deancureton/Puiseux](https://github.com/deancureton/Puiseux), at commit [73e78681](https://github.com/deancureton/Puiseux/tree/73e78681d7bb78ddb202e29cb92ab3c16b723126).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 12F05, 13F25.
- In Lean Pool: [LeanPool/Puiseux](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux), from the card [LeanPool/projects/puiseux.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/puiseux.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/puiseux.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/puiseux.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Puiseux](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Puiseux)
