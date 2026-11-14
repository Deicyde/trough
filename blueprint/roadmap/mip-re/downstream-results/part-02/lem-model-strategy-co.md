---
declaration: lemma
origin: cited
lean: MIPRE.BipartiteModel.toCommuting, MIPRE.BipartiteModel.correlation_toCommuting, MIPRE.BipartiteModel.value_toCommuting, MIPRE.BipartiteModel.povmValue_le_commutingOperatorValue, MIPRE.IsPVMIn.of_map, MIPRE.IsPVMIn.of_isStarProjection, MIPRE.CommutingOperatorStrategy.isPVMIn_aliceMeas, MIPRE.CommutingOperatorStrategy.isPVMIn_bobMeas, MIPRE.exists_isPVMIn_lt_povmValue
statement: formalized
proof: formalized
---

# Strategies in a model, read in ${\omega^{\mathrm{co}}}$

Let $(\mathcal{H}, \psi, {\mathscr{A}}, {\mathscr{A}}_A, {\mathscr{A}}_B)$ be a bipartite model with a unit state and star-ordered player algebras, and let $\{M^x_a\}$ and $\{N^y_b\}$ be families of POVMs in ${\mathscr{A}}_A$ and ${\mathscr{A}}_B$. The operators $\pi(\pi_A(M^x_a))$ and $\pi(\pi_B(N^y_b))$ form a commuting-operator strategy whose value in any game is the model's value of the two families, so that value is at most ${\omega^{\mathrm{co}}}$. Conversely, for every $t \geq 0$ with $t < {\omega^{\mathrm{co}}}(\mathfrak{G})$ there is a commuting-operator strategy whose measurements are projective measurements in the two algebras of its own model and whose value there exceeds $t$.

## Depends on

- [Bipartite model](def-bipartite-model.md)
- [The commuting-operator value is a supremum of model values](lem-co-value-model.md)
- [The commuting-operator value is attained on projective strategies](thm-co-value-projective.md)
- [Projective commuting-operator strategy](def-co-projective.md)

## Proof

A $*$-homomorphism of star-ordered algebras preserves positivity, sums and commutation, and the model's Born probability of $(M^x_a, N^y_b)$ is the correlation of the strategy at $(x, y, a, b)$. For the converse, take a projective strategy of value above $t$ (Theorem [The commuting-operator value is attained on projective strategies](thm-co-value-projective.md)) and read its measurements in its model (Lemma [The commuting-operator value is a supremum of model values](lem-co-value-model.md)). Its operators are projections summing to ${I}$, hence mutually orthogonal: conjugating $\sum_c P_c = {I}$ by $P_a$ makes the compressions $P_a P_c P_a = (P_c P_a)^*(P_c P_a)$, $c \neq a$, positive operators summing to $0$, so each vanishes, and then $P_c P_a = 0$ by the C$^*$-identity. The equations of a projective measurement hold in the commutants because they hold in $B(\mathcal{H})$, which the inclusions reflect.

## Lean

Formalized as [`MIPRE.BipartiteModel.toCommuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.toCommuting), [`MIPRE.BipartiteModel.correlation_toCommuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.correlation_toCommuting), [`MIPRE.BipartiteModel.value_toCommuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.value_toCommuting), [`MIPRE.BipartiteModel.povmValue_le_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.BipartiteModel.povmValue_le_commutingOperatorValue), [`MIPRE.IsPVMIn.of_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVMIn.of_map), [`MIPRE.IsPVMIn.of_isStarProjection`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.IsPVMIn.of_isStarProjection), [`MIPRE.CommutingOperatorStrategy.isPVMIn_aliceMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.isPVMIn_aliceMeas), [`MIPRE.CommutingOperatorStrategy.isPVMIn_bobMeas`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingOperatorStrategy.isPVMIn_bobMeas), [`MIPRE.exists_isPVMIn_lt_povmValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_isPVMIn_lt_povmValue).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1338](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1338)
