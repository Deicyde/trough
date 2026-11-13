---
declaration: theorem
origin: cited
lean: PalomarCrouzeixPalencia.crouzeix_palencia
statement: formalized
proof: formalized
---

# Unitary dilation and the Crouzeix–Palencia bound

> Proves unitary power dilation for Hilbert-space contractions, von Neumann’s polynomial inequality, and the Crouzeix–Palencia polynomial spectral-set estimate for the closed numerical range.

*Quoted from the card [LeanPool/projects/lean-operator-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-operator-theory.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PalomarCrouzeixPalencia.exists_unitary_power_dilation`](https://leanpool.github.io/lean-pool/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.html#PalomarCrouzeixPalencia.exists_unitary_power_dilation) (theorem), declared in [LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean, line 49](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean#L49): “Every contraction on a complex Hilbert space admits a unitary power dilation.”
- [`PalomarCrouzeixPalencia.vonNeumann_inequality`](https://leanpool.github.io/lean-pool/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.html#PalomarCrouzeixPalencia.vonNeumann_inequality) (theorem), declared in [LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean, line 58](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean#L58): “Polynomial evaluation on a contraction is bounded by the polynomial supremum on the closed unit disk.”
- [`PalomarCrouzeixPalencia.crouzeix_palencia`](https://leanpool.github.io/lean-pool/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.html#PalomarCrouzeixPalencia.crouzeix_palencia) (theorem; a main declaration), declared in [LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean, line 64](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OperatorTheory/CrouzeixPalenciaSolution.lean#L64): “The closure of the numerical range is a polynomial spectral set with constant 1 + √2.”

## Project

- Authors: Ezzeri Esa.
- Project repository: [savarin/lean-operator-theory](https://github.com/savarin/lean-operator-theory), at commit [6f90bb7e](https://github.com/savarin/lean-operator-theory/tree/6f90bb7e6b056b54f56005e0416d77d6d7c2a478).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 47A12, 47A20, 47A25.
- In Lean Pool: [LeanPool/OperatorTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OperatorTheory), from the card [LeanPool/projects/lean-operator-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-operator-theory.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/lean-operator-theory.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/lean-operator-theory.yaml)
- [Lean Pool at 701389c0: LeanPool/OperatorTheory](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/OperatorTheory)
