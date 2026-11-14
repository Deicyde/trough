---
declaration: lemma
origin: cited
lean: MIPRE.CommutingOperatorStrategy.correlation_nonneg, MIPRE.CommutingOperatorStrategy.correlation_sum, MIPRE.commutingOperatorValue_nonneg, MIPRE.commutingOperatorValue_le_one, MIPRE.TensorProductStrategy.correlation_toCommuting, MIPRE.Cq_subset_Cqc, MIPRE.quantumValue_le_commutingOperatorValue, MIPRE.payoff_le_quantumValue_of_mem_Cqa, MIPRE.payoff_le_commutingOperatorValue_of_mem_Cqc, MIPRE.Cqa_subset_Cqc_of_isClosed
statement: formalized
proof: formalized
---

# Basic properties of the correlation sets

Commuting-operator correlations are nonnegative and sum to one for each question pair, so $0 \leq {\omega^{\mathrm{co}}}(\mathfrak{G}) \leq 1$. A tensor-product strategy is a commuting-operator strategy with the same correlation, so $C_q \subseteq C_{qc}$ and $\mathrm{val}^*(\mathfrak{G}) \leq {\omega^{\mathrm{co}}}(\mathfrak{G})$. The payoff of every correlation in $C_{qa}$ is at most $\mathrm{val}^*(\mathfrak{G})$, and that of every correlation in $C_{qc}$ at most ${\omega^{\mathrm{co}}}(\mathfrak{G})$. If $C_{qc}$ is closed then $C_{qa} \subseteq C_{qc}$.

## Depends on

- [Correlation sets](def-correlation-sets.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)

## Proof

$E^x_a F^y_b$ is the product of two commuting positive operators, hence positive, which gives nonnegativity; the sum over $a, b$ is $\langle \psi, \psi \rangle = 1$. On $\mathbb{C}^{d_A} \otimes \mathbb{C}^{d_B}$ the operators $A^x_a \otimes {I}$ and ${I} \otimes B^y_b$ are commuting projections with the same Born probabilities. The payoff is linear, hence continuous, so the bound $\mathrm{val}^*(\mathfrak{G})$ on $C_q$ passes to its closure.

## Lean

Formalized as [`MIPRE.CommutingOperatorStrategy.correlation_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_nonneg), [`MIPRE.CommutingOperatorStrategy.correlation_sum`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.correlation_sum), [`MIPRE.commutingOperatorValue_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue_nonneg), [`MIPRE.commutingOperatorValue_le_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commutingOperatorValue_le_one), [`MIPRE.TensorProductStrategy.correlation_toCommuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TensorProductStrategy.correlation_toCommuting), [`MIPRE.Cq_subset_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cq_subset_Cqc), [`MIPRE.quantumValue_le_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.quantumValue_le_commutingOperatorValue), [`MIPRE.payoff_le_quantumValue_of_mem_Cqa`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.payoff_le_quantumValue_of_mem_Cqa), [`MIPRE.payoff_le_commutingOperatorValue_of_mem_Cqc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.payoff_le_commutingOperatorValue_of_mem_Cqc), [`MIPRE.Cqa_subset_Cqc_of_isClosed`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cqa_subset_Cqc_of_isClosed).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 374](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L374)
