---
declaration: lemma
origin: cited
lean: MIPRE.AnswerReduction.typedStrategy, MIPRE.AnswerReduction.typedStrategy_value_ge
statement: formalized
proof: formalized
---

# Typed soundness setup

An exterior strategy with deficit $\varepsilon_{\mathrm{out}}$ gives a typed strategy with deficit $\theta=16^{|T^{\mathrm{ar}}|}\varepsilon_{\mathrm{out}}$ on the same state. Symmetrize the typed strategy for its symmetric game; do not assume the detyped question law is symmetric. The soundness proof then works with projective, well-formatted measurements and a swap-invariant state. All type-pair conditioning costs are constants since $T^{\mathrm{ar}}$ is fixed. The Lean does not symmetrize: it keeps the two families of measurements of a projective strategy in a bipartite model (Definition [Projective strategy in a bipartite model](../../downstream-results/part-02/def-model-proj-strategy.md)), of which a tensor-product strategy is the case of its tensor-product model, and derives every relation for each ordered pair of players from the ordered type pair that carries it, the type graph being complete.

## Depends on

- [Answer-reduction construction](lem-ar-construction.md)

## Proof depends on

- [Post-processing and detyping, in a model](../../downstream-results/part-02/lem-transports-model.md)
- [Operations on projective strategies](../../downstream-results/part-03/lem-model-proj-strategy.md)

## Proof

Detyping soundness (Lemma [Same-state detyping soundness](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L841)) restricts the strategy to the typed game with the typed decider's predicate, which is the typed answer-reduced predicate at the answer cut, on the same state.

## Lean

Formalized as [`MIPRE.AnswerReduction.typedStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.typedStrategy), [`MIPRE.AnswerReduction.typedStrategy_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.AnswerReduction.typedStrategy_value_ge).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 5712](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L5712)
