---
declaration: theorem
origin: cited
lean: CompositionAlgebra.hurwitz_classification
statement: formalized
proof: formalized
---

# Hurwitz's Classification of Euclidean Composition Algebras

> Formalizes Hurwitz's classification of nontrivial finite-dimensional real Euclidean composition algebras: every such algebra has dimension 1, 2, 4, or 8 and is real-linearly equivalent to the real numbers, complex numbers, quaternions, or octonions through a map preserving the unit, multiplication, and norm form. The development also constructs the octonions from an explicit Fano multiplication table, proves Degen's eight-square identity, and shows that Cayley--Dickson doubling preserves the composition law for associative inputs.

*Quoted from the card [LeanPool/projects/composition-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/composition-algebras.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`CompositionAlgebra.hurwitz_classification`](https://leanpool.github.io/lean-pool/LeanPool/CompositionAlgebras/Composition/Classification.html#CompositionAlgebra.hurwitz_classification) (theorem; a main declaration), declared in [LeanPool/CompositionAlgebras/Composition/Classification.lean, line 341](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras/Composition/Classification.lean#L341): “Every nontrivial finite-dimensional real Euclidean composition algebra is linearly equivalent to the real numbers, complex numbers, quaternions, or octonions through a map preserving the unit, multiplication, and norm form.”
- [`CompositionAlgebra.finrank_eq_one_or_two_or_four_or_eight`](https://leanpool.github.io/lean-pool/LeanPool/CompositionAlgebras/Composition/Hurwitz.html#CompositionAlgebra.finrank_eq_one_or_two_or_four_or_eight) (theorem), declared in [LeanPool/CompositionAlgebras/Composition/Hurwitz.lean, line 354](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras/Composition/Hurwitz.lean#L354): “The real dimension of a nontrivial finite-dimensional Euclidean composition algebra is exactly 1, 2, 4, or 8.”
- [`CompositionAlgebra.CD.instCompositionAlgebra`](https://leanpool.github.io/lean-pool/LeanPool/CompositionAlgebras/Composition/CayleyDickson.html#CompositionAlgebra.CD.instCompositionAlgebra) (instance), declared in [LeanPool/CompositionAlgebras/Composition/CayleyDickson.lean, line 247](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras/Composition/CayleyDickson.lean#L247): “The Cayley--Dickson double of a nontrivial associative Euclidean composition algebra again satisfies the composition law.”
- [`Octonion.nucleus_real`](https://leanpool.github.io/lean-pool/LeanPool/CompositionAlgebras/OctonionNucleus.html#Octonion.nucleus_real) (theorem), declared in [LeanPool/CompositionAlgebras/OctonionNucleus.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras/OctonionNucleus.lean#L55): “Any octonion that associates in the third slot with every pair has zero imaginary coordinates and hence lies on the real line.”

## Project

- Authors: Bryan Ehrlich.
- Source: *Über die Composition der quadratischen Formen von beliebig vielen Variablen* by Adolf Hurwitz, [https://eudml.org/doc/58420](https://eudml.org/doc/58420).
- Project repository: [ehrlich-b/composition-algebras](https://github.com/ehrlich-b/composition-algebras), at commit [e37e22b0](https://github.com/ehrlich-b/composition-algebras/tree/e37e22b0571a170ba18a0d8db29fe2a857906b92).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 17A75, 17A35, 11E88.
- In Lean Pool: [LeanPool/CompositionAlgebras](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras), from the card [LeanPool/projects/composition-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/composition-algebras.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/composition-algebras.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/composition-algebras.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CompositionAlgebras](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CompositionAlgebras)
