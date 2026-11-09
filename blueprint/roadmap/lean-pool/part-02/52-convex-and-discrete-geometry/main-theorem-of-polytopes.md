---
declaration: theorem
origin: cited
lean: MainTheoremOfPolytopes
statement: formalized
proof: formalized
---

# The main theorem of polytopes

> Formalizes the Minkowski–Weyl theorem — the equivalence between V-polytopes (convex hulls of finite point sets) and bounded H-polytopes (finite intersections of half-spaces) in a finite-dimensional real vector space.

*Quoted from the card [LeanPool/projects/main-theorem-of-polytopes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/main-theorem-of-polytopes.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MainTheoremOfPolytopes`](https://leanpool.github.io/lean-pool/LeanPool/Polytopes/MainTheorem.html#MainTheoremOfPolytopes) (theorem; a main declaration), declared in [LeanPool/Polytopes/MainTheorem.lean, line 493](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Polytopes/MainTheorem.lean#L493): “The Minkowski–Weyl theorem — a set is a V-polytope iff it is a bounded H-polytope.” Its source, as the card gives it: “G. M. Ziegler, Lectures on Polytopes, GTM 152, Springer, 1995, Theorem 1.1.”
- [`Vpolytope_of_Hpolytope`](https://leanpool.github.io/lean-pool/LeanPool/Polytopes/MainTheorem.html#Vpolytope_of_Hpolytope) (lemma), declared in [LeanPool/Polytopes/MainTheorem.lean, line 347](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Polytopes/MainTheorem.lean#L347): “Every bounded H-polytope (finite intersection of half-spaces) is the convex hull of a finite point set.”

## Project

- Authors: Jun Kwon.
- Source: *Main theorem of polytopes*.
- Project repository: [Jun2M/Main-theorem-of-polytopes](https://github.com/Jun2M/Main-theorem-of-polytopes).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 52B11, 52A20.
- In Lean Pool: [LeanPool/Polytopes](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Polytopes), from the card [LeanPool/projects/main-theorem-of-polytopes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/main-theorem-of-polytopes.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/main-theorem-of-polytopes.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/main-theorem-of-polytopes.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Polytopes](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Polytopes)
