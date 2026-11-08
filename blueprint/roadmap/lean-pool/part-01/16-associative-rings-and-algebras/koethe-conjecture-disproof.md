---
declaration: theorem
origin: cited
lean: Koethe.KotherConjecture.variants.general_matrix.disproof
statement: formalized
proof: formalized
---

# Disproof of the Köthe conjecture (Krempa's matrix form)

> Refutes Köthe's 1930 conjecture in Krempa's matrix form: there is a ring R (the unitization of a nil algebra of three weighted backward shifts over the algebraic closure of F_2) with a nil two-sided ideal I such that the matrix ideal M_2(I) contains a non-nilpotent matrix. The compared theorem is exactly the negation of the research-open statement `Koethe.KotherConjecture.variants.general_matrix` from Google DeepMind's Formal Conjectures, in every universe. The supporting library proves a multiprojective common-zero theorem via the Segre cone, the Nullstellensatz and Krull's height theorem, a mask-mortality theorem for one-row matrix pencils, a diagonal construction of universal mortal sequences, and a linearization theorem reducing nilness of a three-generator algebra to nilness of its root-row pencils.

*Quoted from the card [LeanPool/projects/koethe-conjecture-disproof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/koethe-conjecture-disproof.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 6 main results, each with its informal statement quoted from the card. The scan finds 6 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`Koethe.KotherConjecture.variants.general_matrix.disproof`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/Disproof.html#Koethe.KotherConjecture.variants.general_matrix.disproof) (theorem; a main declaration), declared in [LeanPool/Koethe/Disproof.lean, line 71](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/Disproof.lean#L71): “It is not the case that for every ring R, every nil two-sided ideal I of R and every finite index type n, the matrix ideal M_n(I) of M_n(R) is nil. This is the negation of Krempa's matrix form of Köthe's conjecture, stated verbatim as in Formal Conjectures.”
- [`KoetheCounterexample.counterexample`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/Counterexample.html#KoetheCounterexample.counterexample) (theorem), declared in [LeanPool/Koethe/Counterexample.lean, line 70](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/Counterexample.lean#L70): “In every universe there is a ring R with a nil two-sided ideal I such that some 2 x 2 matrix with entries in I is not nilpotent.”
- [`KoetheMultiProjective.exists_common_zero`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/MultiProjective.html#KoetheMultiProjective.exists_common_zero) (theorem), declared in [LeanPool/Koethe/MultiProjective.lean, line 752](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/MultiProjective.lean#L752): “Over an algebraically closed field, at most 2N polynomials that are multihomogeneous of a common positive degree in each of N blocks of three variables have a common zero with no block equal to zero.”
- [`KoetheCounterexample.maskMortality`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/Mortality/MaskMortality.html#KoetheCounterexample.maskMortality) (theorem), declared in [LeanPool/Koethe/Mortality/MaskMortality.lean, line 144](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/Mortality/MaskMortality.lean#L144): “Over an algebraically closed field, every one-row matrix pencil and every periodic mask with more than half of its residues free admit a mask-compatible word of nonzero letters whose forward product is the zero matrix.”
- [`KoetheCounterexample.exists_universalMortalSequence`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/MaskSequence/Universal.html#KoetheCounterexample.exists_universalMortalSequence) (theorem), declared in [LeanPool/Koethe/MaskSequence/Universal.lean, line 91](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/MaskSequence/Universal.lean#L91): “Over a countable field satisfying mask mortality there is a sequence of nonzero letter triples such that every pencil has all its windows of some fixed positive length equal to zero.”
- [`KoetheCounterexample.nil_of_all_pencils_nil`](https://leanpool.github.io/lean-pool/LeanPool/Koethe/Linearization/Nil.html#KoetheCounterexample.nil_of_all_pencils_nil) (theorem), declared in [LeanPool/Koethe/Linearization/Nil.lean, line 89](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe/Linearization/Nil.lean#L89): “If every root-row pencil lifted along three elements of an algebra is nilpotent, then the non-unital subalgebra they generate is nil.”

## Project

- Authors: Tom Adamczewski.
- Source: *A counterexample to Köthe's conjecture and a question of Rowen* by Tom Adamczewski, Bernhard Böhmler, Rene Marczinzik, [arXiv:2609.07996](https://arxiv.org/abs/2609.07996).
- Project repository: [tadamcz/koethe](https://github.com/tadamcz/koethe), at commit [a94a72ae](https://github.com/tadamcz/koethe/tree/a94a72aec957cb28d76aa30fb97a01d440990d7f).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 16N40, 16S50.
- In Lean Pool: [LeanPool/Koethe](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe), from the card [LeanPool/projects/koethe-conjecture-disproof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/koethe-conjecture-disproof.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/koethe-conjecture-disproof.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/koethe-conjecture-disproof.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Koethe](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Koethe)
