---
declaration: theorem
origin: cited
lean: Lean4LPD.PauliString.pauliNorm_layerStep_error_le_model_of_source_regime
statement: formalized
proof: formalized
---

# Low-weight Pauli dynamics and truncation error

> Derives a normalized Pauli 2-norm truncation-error bound for concrete circuits of disjoint-support Hermitian Pauli rotations, with explicit locality, angle, step-count, and cutoff hypotheses. Develops a faithful matrix representation, Pauli coefficient reconstruction, finite Schur bounds, and reusable scalar multi-jump ladder estimates. Also proves a combinatorial light-cone bound and exact counterexamples showing why repeated product-formula layers must count toward the layer exponent. This is the norm-level analysis, not a formalization of expectation-value accuracy, Hamiltonian approximation, or the paper's full algorithm.

*Quoted from the card [LeanPool/projects/low-weight-pauli-dynamics.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/low-weight-pauli-dynamics.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Lean4LPD.PauliString.pauliNorm_layerStep_error_le_model_of_source_regime`](https://leanpool.github.io/lean-pool/LeanPool/LowWeightPauliDynamics/Pauli/LayerError.html#Lean4LPD.PauliString.pauliNorm_layerStep_error_le_model_of_source_regime) (theorem; a main declaration), declared in [LeanPool/LowWeightPauliDynamics/Pauli/LayerError.lean, line 591](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics/Pauli/LayerError.lean#L591): “For an observable supported on Pauli weights at most ko, a block of Γ positive-many disjoint-support layers of Hermitian rotations of weight at most kh, kh ≥ 2, and |sin θ| ≤ a ≤ αt/r with α > 0 and t ≥ 0, truncation to weight ko + m(kh - 1) after each of r blocks has Pauli 2-norm error at most (2Γ(kh - 1)αt)^(m+1) (e(m+1))^(ko/(kh-1)) times the input norm. The conditions include m ≥ 1, r ≥ 5, m ≤ r, rΓ ≥ 8(m+1)^2, and r ≥ 8e^2(ko+kh-1)αt. Γ counts every layer of the actual block, including repeated product-formula layers.” Its source, as the card gives it: “Upstream STATEMENTS.md and Pauli/LayerError.lean at the pinned commit; norm-level counterpart of the revised supplement's truncation bound.”
- [`Lean4LPD.l2_opNorm_le_schur`](https://leanpool.github.io/lean-pool/LeanPool/LowWeightPauliDynamics/SchurCore.html#Lean4LPD.l2_opNorm_le_schur) (theorem), declared in [LeanPool/LowWeightPauliDynamics/SchurCore.lean, line 113](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics/SchurCore.lean#L113): “A finite rectangular matrix over any RCLike field, with absolute row sums bounded by nonnegative R and absolute column sums bounded by nonnegative C, has Euclidean operator norm at most sqrt(RC).” Its source, as the card gives it: “Upstream Schur.lean, finite-dimensional Schur test.”
- [`Lean4LPD.PauliString.reachable_weight_le`](https://leanpool.github.io/lean-pool/LeanPool/LowWeightPauliDynamics/Pauli/LayerWitness.html#Lean4LPD.PauliString.reachable_weight_le) (theorem), declared in [LeanPool/LowWeightPauliDynamics/Pauli/LayerWitness.lean, line 411](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics/Pauli/LayerWitness.lean#L411): “Every Pauli string reachable through a list of disjoint-support kh-local layers, kh ≥ 1, has weight at most its initial weight times kh raised to the number of layers. Reachability is combinatorial; this theorem does not assert that a reachable coefficient is nonzero.” Its source, as the card gives it: “Upstream Pauli/LayerWitness.lean, effective-layer light cone.”
- [`Lean4LPD.LayerCounterexample.actual_discard_exceeds_gamma_bound`](https://leanpool.github.io/lean-pool/LeanPool/LowWeightPauliDynamics/Pauli/LayerCounterexample.html#Lean4LPD.LayerCounterexample.actual_discard_exceeds_gamma_bound) (theorem), declared in [LeanPool/LowWeightPauliDynamics/Pauli/LayerCounterexample.lean, line 592](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics/Pauli/LayerCounterexample.lean#L592): “For the explicit eight-qubit second-order word L1,L2,L2,L1 and angles 0 < θ < π/2, truncating the evolved weight-one input at weight one discards a nonzero coefficient of weight greater than four. Thus the two distinct layer types give an invalid bound 1\*2^2; repetitions must be counted.” Its source, as the card gives it: “Upstream Pauli/LayerCounterexample.lean, exact symbolic witness.”

## Project

- Authors: Jue Xu.
- Source: *Classical Simulation of Noiseless Quantum Dynamics without Randomness*, [arXiv:2601.15770](https://arxiv.org/abs/2601.15770).
- Project repository: [Jue-Xu/Lean4LPD](https://github.com/Jue-Xu/Lean4LPD), at commit [ad056166](https://github.com/Jue-Xu/Lean4LPD/tree/ad0561661c46ca4c331d21104468e5dc65b2a028).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 81P68, 65L70, 47A30.
- In Lean Pool: [LeanPool/LowWeightPauliDynamics](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics), from the card [LeanPool/projects/low-weight-pauli-dynamics.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/low-weight-pauli-dynamics.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/low-weight-pauli-dynamics.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/low-weight-pauli-dynamics.yaml)
- [Lean Pool at 701389c0: LeanPool/LowWeightPauliDynamics](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/LowWeightPauliDynamics)
