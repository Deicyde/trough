---
declaration: def
origin: cited
lean: Demazure.Dem, CoxeterSystem.strongExchangeProperty
statement: formalized
---

# Demazure Operators and Lean

> Formalizes Demazure operators on multivariate polynomials and their nilpotence, braid, commutation, and symmetric-polynomial linearity relations, with auxiliary Coxeter-theory support including strong exchange and a conditional Matsumoto theorem.

*Quoted from the card [LeanPool/projects/demazureoperatorslean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/demazureoperatorslean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 7 main results, each with its informal statement quoted from the card. The scan finds 7 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Demazure.Dem`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/DemazureRelations.html#Demazure.Dem) (def; a main declaration), declared in [LeanPool/DemazureOperatorsLean/DemazureRelations.lean, line 109](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/DemazureRelations.lean#L109): “Defines the Demazure operator as a linear map over the subalgebra of symmetric polynomials.”
- [`Demazure.demazure_order_two`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/DemazureRelations.html#Demazure.demazure_order_two) (lemma), declared in [LeanPool/DemazureOperatorsLean/DemazureRelations.lean, line 31](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/DemazureRelations.lean#L31): “Proves that applying the Demazure operator twice gives zero.”
- [`Demazure.demazure_commutes_adjacent`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/DemazureRelations.html#Demazure.demazure_commutes_adjacent) (lemma), declared in [LeanPool/DemazureOperatorsLean/DemazureRelations.lean, line 41](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/DemazureRelations.lean#L41): “Proves the braid relation for adjacent Demazure operators.”
- [`Demazure.demazure_commutes_non_adjacent`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/DemazureRelations.html#Demazure.demazure_commutes_non_adjacent) (lemma), declared in [LeanPool/DemazureOperatorsLean/DemazureRelations.lean, line 51](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/DemazureRelations.lean#L51): “Proves that non-adjacent Demazure operators commute.”
- [`Demazure.demazure_mul_symm`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/DemazureRelations.html#Demazure.demazure_mul_symm) (lemma), declared in [LeanPool/DemazureOperatorsLean/DemazureRelations.lean, line 90](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/DemazureRelations.lean#L90): “Proves that symmetric polynomials act as scalars with respect to Demazure operators.”
- [`CoxeterSystem.strongExchangeProperty`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/StrongExchange.html#CoxeterSystem.strongExchangeProperty) (theorem; a main declaration), declared in [LeanPool/DemazureOperatorsLean/StrongExchange.lean, line 544](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/StrongExchange.lean#L544): “Proves the strong exchange property for Coxeter systems.” Its source, as the card gives it: “J. E. Humphreys, Reflection Groups and Coxeter Groups, Cambridge University Press, 1990.”
- [`CoxeterSystem.matsumoto_reduced`](https://leanpool.github.io/lean-pool/LeanPool/DemazureOperatorsLean/Matsumoto.html#CoxeterSystem.matsumoto_reduced) (theorem), declared in [LeanPool/DemazureOperatorsLean/Matsumoto.lean, line 721](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean/Matsumoto.lean#L721): “Auxiliary theorem proving, under the extra MatsumotoCondition hypothesis, that reduced words for the same Coxeter group element are connected by braid moves.” Its source, as the card gives it: “J. E. Humphreys, Reflection Groups and Coxeter Groups, Cambridge University Press, 1990.”

## Project

- Authors: Óscar Álvarez Sánchez.
- Source: *Schubert cells, and the cohomology of the spaces G/P* by I. N. Bernstein, I. M. Gelfand, S. I. Gelfand, [doi:10.1070/RM1973v028n03ABEH001557](https://doi.org/10.1070/RM1973v028n03ABEH001557).
- Project repository: [bolito2/DemazureOperatorsLean](https://github.com/bolito2/DemazureOperatorsLean).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 05E05, 13P10, 20F55.
- In Lean Pool: [LeanPool/DemazureOperatorsLean](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean), from the card [LeanPool/projects/demazureoperatorslean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/demazureoperatorslean.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/demazureoperatorslean.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/demazureoperatorslean.yaml)
- [Lean Pool at 701389c0: LeanPool/DemazureOperatorsLean](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/DemazureOperatorsLean)
