---
declaration: theorem
origin: cited
lean: QuadraticIterates.section3_main
statement: formalized
proof: formalized
---

# Galois groups of quadratic polynomial iterates

> Formalizes Stoll's criterion for when the Galois group of the n-th iterate of X² + a over the rationals is the full n-fold iterated wreath product of C₂. It proves the criterion in terms of two-independence of a signed critical-orbit sequence and its pairwise-coprime Möbius factors, and derives the paper's congruence families for which maximality holds at every level. The supporting library develops reusable multiquadratic-extension, iterated wreath-product, Möbius-factor, and valuation results.

*Quoted from the card [LeanPool/projects/quadratic-iterates.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quadratic-iterates.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`QuadraticIterates.section1_equiv`](https://leanpool.github.io/lean-pool/LeanPool/QuadraticIterates/ArchMath1992/Main.html#QuadraticIterates.section1_equiv) (theorem), declared in [LeanPool/QuadraticIterates/ArchMath1992/Main.lean, line 193](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuadraticIterates/ArchMath1992/Main.lean#L193): “For each n, assuming -a is not a rational square, the Galois group of the n-th iterate of X² + a is the full n-fold iterated wreath product of C₂ exactly when either the first n terms of the signed sequence c₁ = -a, cₖ = fₖ(0) for k ≥ 2, or the first n integer Möbius factors of that sequence are independent modulo rational squares.”
- [`QuadraticIterates.section1_squarefree`](https://leanpool.github.io/lean-pool/LeanPool/QuadraticIterates/ArchMath1992/Main.html#QuadraticIterates.section1_squarefree) (theorem), declared in [LeanPool/QuadraticIterates/ArchMath1992/Main.lean, line 203](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuadraticIterates/ArchMath1992/Main.lean#L203): “If -a is not a rational square and none of the absolute Möbius factors from levels 2 through n is a rational square, then the n-th iterate has the full iterated-wreath-product Galois group.”
- [`QuadraticIterates.section3_main`](https://leanpool.github.io/lean-pool/LeanPool/QuadraticIterates/ArchMath1992/Main.html#QuadraticIterates.section3_main) (theorem; a main declaration), declared in [LeanPool/QuadraticIterates/ArchMath1992/Main.lean, line 300](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuadraticIterates/ArchMath1992/Main.lean#L300): “The Galois group is the full iterated wreath product at every positive level when a is positive and congruent to 1 or 2 modulo 4, or when a is negative and divisible by 4 with -a nonsquare.”

## Project

- Authors: Michael Stoll.
- Source: *Galois groups over ℚ of some iterated polynomials* by Michael Stoll, [doi:10.1007/BF01197321](https://doi.org/10.1007/BF01197321).
- Project repository: [MichaelStollBayreuth/QuadraticIterates](https://github.com/MichaelStollBayreuth/QuadraticIterates), at commit [b0413c17](https://github.com/MichaelStollBayreuth/QuadraticIterates/tree/b0413c173972ddf121cb4394cb06f9d2b83e501f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 11R32, 12F10, 37P05.
- In Lean Pool: [LeanPool/QuadraticIterates](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuadraticIterates), from the card [LeanPool/projects/quadratic-iterates.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quadratic-iterates.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/quadratic-iterates.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/quadratic-iterates.yaml)
- [Lean Pool at 2b205bf9: LeanPool/QuadraticIterates](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/QuadraticIterates)
