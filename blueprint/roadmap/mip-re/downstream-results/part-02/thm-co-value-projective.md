---
declaration: theorem
origin: cited
lean: MIPRE.CommutingOperatorStrategy.exists_isProjective_correlation_eq, MIPRE.CommutingOperatorStrategy.exists_isProjective_value_eq, MIPRE.commutingOperatorValue_eq_iSup_isProjective, MIPRE.exists_isProjective_lt_value, MIPRE.TensorProductStrategy.isProjective_toCommuting
statement: formalized
proof: formalized
---

# The commuting-operator value is attained on projective strategies

Every commuting-operator strategy for $\mathfrak{G}$ has a projective commuting-operator strategy with the same correlation, hence the same value. Consequently ${\omega^{\mathrm{co}}}(\mathfrak{G})$ is the supremum of the values of the projective commuting-operator strategies, and for every $t \geq 0$ with $t < {\omega^{\mathrm{co}}}(\mathfrak{G})$ there is a projective commuting-operator strategy of value greater than $t$. Every tensor-product strategy is a projective commuting-operator strategy.

## Depends on

- [Commutation-preserving dilation](lem-co-dilation.md)
- [Projective commuting-operator strategy](def-co-projective.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Basic properties of the correlation sets](../part-01/lem-correlation-sets-basic.md)

## Proof

Dilate the first player's questions one at a time by Lemma [Commutation-preserving dilation](lem-co-dilation.md), then the second player's. Each step keeps the correlation and every projectivity already obtained, and makes one more measurement projective. A question has an answer, since its POVM sums to ${I}$ on a nonzero space, so the lemma applies. The value is the payoff of the correlation, and it lies in $[0, 1]$, as does ${\omega^{\mathrm{co}}}(\mathfrak{G})$ (Lemma [Basic properties of the correlation sets](../part-01/lem-correlation-sets-basic.md)), which gives the supremum and the strategy of value greater than $t$. A tensor-product strategy (Definition [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)) measures $A^x_a \otimes {I}$ and ${I} \otimes B^y_b$ with $A^x_a$ and $B^y_b$ projections.

## Lean

Formalized as [`MIPRE.CommutingOperatorStrategy.exists_isProjective_correlation_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.exists_isProjective_correlation_eq), [`MIPRE.CommutingOperatorStrategy.exists_isProjective_value_eq`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.exists_isProjective_value_eq), [`MIPRE.commutingOperatorValue_eq_iSup_isProjective`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue_eq_iSup_isProjective), [`MIPRE.exists_isProjective_lt_value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_isProjective_lt_value), [`MIPRE.TensorProductStrategy.isProjective_toCommuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.isProjective_toCommuting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1154](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1154)
