---
declaration: theorem
origin: cited
lean: Matrix.aut_mat_inner, QuantumSet, schurMul, QuantumGraph
statement: formalized
---

# Monlib4 Operator-Algebra and Quantum-Set Core

> Formalizes monlib4's finite matrix-algebra inner-automorphism theorem, unitary inner automorphisms, star-preserving linear maps, the structural core of quantum sets, the core Schur-product definition of quantum graphs, and a self-contained digit-sum divisibility theorem.

*Quoted from the card [LeanPool/projects/monlib4.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/monlib4.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 16 main results, each with its informal statement quoted from the card. The scan finds 16 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Matrix.automorphism_matrix_inner`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/RepTheory/AutMat.html#Matrix.automorphism_matrix_inner) (theorem), declared in [LeanPool/Monlib4/RepTheory/AutMat.lean, line 49](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/RepTheory/AutMat.lean#L49): “Shows that any automorphism of a finite nontrivial matrix algebra is implemented by an invertible intertwining matrix.”
- [`Matrix.aut_mat_inner`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/RepTheory/AutMat.html#Matrix.aut_mat_inner) (theorem; a main declaration), declared in [LeanPool/Monlib4/RepTheory/AutMat.lean, line 210](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/RepTheory/AutMat.lean#L210): “Packages matrix-algebra automorphisms as inner automorphisms induced by a linear equivalence of the underlying coordinate space.”
- [`Matrix.aut_mat_inner'`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/RepTheory/AutMat.html#Matrix.aut_mat_inner') (theorem), declared in [LeanPool/Monlib4/RepTheory/AutMat.lean, line 224](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/RepTheory/AutMat.lean#L224): “Packages matrix-algebra automorphisms as conjugation by an element of `GL n 𝕜`.”
- [`Matrix.aut_mat_inner_trace_preserving`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/RepTheory/AutMat.html#Matrix.aut_mat_inner_trace_preserving) (theorem), declared in [LeanPool/Monlib4/RepTheory/AutMat.lean, line 243](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/RepTheory/AutMat.lean#L243): “Proves that automorphisms of finite matrix algebras preserve trace.”
- [`Matrix.innerAut`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/InnerAut.html#Matrix.innerAut) (abbrev), declared in [LeanPool/Monlib4/LinearAlgebra/InnerAut.lean, line 180](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/InnerAut.lean#L180): “Defines the linear map induced by conjugation with a unitary matrix.”
- [`Matrix.innerAut_apply_trace_eq`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/InnerAut.html#Matrix.innerAut_apply_trace_eq) (theorem), declared in [LeanPool/Monlib4/LinearAlgebra/InnerAut.lean, line 334](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/InnerAut.lean#L334): “Proves that unitary inner automorphisms preserve matrix trace.”
- [`Matrix.innerAut.spectrum_eq`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/InnerAut.html#Matrix.innerAut.spectrum_eq) (theorem), declared in [LeanPool/Monlib4/LinearAlgebra/InnerAut.lean, line 258](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/InnerAut.lean#L258): “Proves that unitary inner automorphisms preserve the spectrum of the associated linear operator.”
- [`LinearMap.IsReal`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/IsReal.html#LinearMap.IsReal) (def), declared in [LeanPool/Monlib4/LinearAlgebra/IsReal.lean, line 24](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/IsReal.lean#L24): “Defines star-preserving, or real, function-like maps.”
- [`LinearMap.real`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/IsReal.html#LinearMap.real) (def), declared in [LeanPool/Monlib4/LinearAlgebra/IsReal.lean, line 40](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/IsReal.lean#L40): “Defines the star-conjugate involution on linear maps.”
- [`QuantumSet`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.html#QuantumSet) (class; a main declaration), declared in [LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.lean, line 123](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.lean#L123): “Defines the monlib4 quantum-set structure with modular automorphisms and a fixed orthonormal basis.”
- [`Complex.quantumSet`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.html#Complex.quantumSet) (instance), declared in [LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.lean, line 214](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/QuantumSet/Basic.lean#L214): “Instantiates the complex numbers as the base quantum set.”
- [`schurMul`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/LinearAlgebra/QuantumSet/SchurMul.html#schurMul) (def; a main declaration), declared in [LeanPool/Monlib4/LinearAlgebra/QuantumSet/SchurMul.lean, line 35](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/LinearAlgebra/QuantumSet/SchurMul.lean#L35): “Defines the Schur product of linear maps using multiplication, tensoring, and coalgebra comultiplication.”
- [`QuantumGraph`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/QuantumGraph/Basic.html#QuantumGraph) (class; a main declaration), declared in [LeanPool/Monlib4/QuantumGraph/Basic.lean, line 527](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/QuantumGraph/Basic.lean#L527): “Defines quantum graphs as Schur-idempotent endomorphisms.”
- [`QuantumGraph.Real`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/QuantumGraph/Basic.html#QuantumGraph.Real) (class), declared in [LeanPool/Monlib4/QuantumGraph/Basic.lean, line 544](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/QuantumGraph/Basic.lean#L544): “Defines real quantum graphs as Schur-idempotent, star-preserving endomorphisms.”
- [`nat_repr_mod_eq_sum_repr_mod`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/Other/Sonia.html#nat_repr_mod_eq_sum_repr_mod) (theorem), declared in [LeanPool/Monlib4/Other/Sonia.lean, line 79](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/Other/Sonia.lean#L79): “Proves that the value represented by digits in base `a + 1` has the same remainder modulo `a` as the sum of those digits.”
- [`nat_dvd_repr_iff_nat_dvd_sum_repr`](https://leanpool.github.io/lean-pool/LeanPool/Monlib4/Other/Sonia.html#nat_dvd_repr_iff_nat_dvd_sum_repr) (theorem), declared in [LeanPool/Monlib4/Other/Sonia.lean, line 104](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4/Other/Sonia.lean#L104): “Proves the generalized digit-sum divisibility criterion for base `a + 1` modulo `a`.”

## Project

- Authors: Monica Omar.
- Source: [doi:10.4169/amer.math.monthly.124.10.966](https://doi.org/10.4169/amer.math.monthly.124.10.966), [arXiv:1810.08368](https://arxiv.org/abs/1810.08368).
- Project repository: [themathqueen/monlib4](https://github.com/themathqueen/monlib4).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 15A69, 16W20.
- In Lean Pool: [LeanPool/Monlib4](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4), from the card [LeanPool/projects/monlib4.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/monlib4.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/monlib4.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/monlib4.yaml)
- [Lean Pool at 701389c0: LeanPool/Monlib4](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/Monlib4)
