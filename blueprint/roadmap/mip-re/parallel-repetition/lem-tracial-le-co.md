---
declaration: lemma
origin: cited
lean: MIPRE.TracialState.im_star_mul_self, MIPRE.TracialState.map_star, MIPRE.TracialState.toState, MIPRE.TracialCo.form_mulRight_left, MIPRE.TracialCo.form_mulRight_self, MIPRE.TracialCo.bdd_mulRight, MIPRE.TracialCo.lift_mulRight_isPositive, MIPRE.TracialCo.bdd_mulLeft, MIPRE.TracialCo.lift_mulLeft_isPositive, MIPRE.CommutingStrategy.toCommutingOperatorStrategy, MIPRE.CommutingStrategy.correlation_toCommutingOperatorStrategy, MIPRE.CommutingStrategy.value_toCommutingOperatorStrategy, MIPRE.commValue_le_commutingOperatorValue
statement: formalized
proof: formalized
---

# Tracial strategies are commuting-operator strategies

[[$\uparrow$ QuantumLib](https://github.com/Timeroot/Lean-QuantumInfo)] For every synchronous game $\mathfrak{G}$, ${\mathrm{val}^{\mathrm{co}}}(\mathfrak{G}) \leq {\omega^{\mathrm{co}}}(\mathfrak{G})$. The Lean proof of the main theorem does not use this lemma; it serves the downstream $\mathrm{MIP}^{\mathrm{co}} = \mathrm{coRE}$ chapter only.

## Depends on

- [Synchronous game](../foundations/part-01/def-sync-game.md)
- [Commuting strategy](../foundations/part-01/def-commuting-strategy.md)
- [Commuting value](../foundations/part-01/def-commuting-value.md)
- [Commuting-operator value](def-co-value-bipartite.md)
- [Basic properties of the correlation sets](../downstream-results/part-01/lem-correlation-sets-basic.md)

## Proof

Let $({\mathscr{A}}, \tau, M)$ be a commuting strategy (Definition [Commuting strategy](../foundations/part-01/def-commuting-strategy.md)) and let $\mathcal{H}$ be the completion of ${\mathscr{A}}$ for the semi-inner product $\langle a, b \rangle = \tau(a^* b)$, with the class of $1$ as the unit vector $\xi$. A tracial state is Hermitian, $\tau(a^*) = \overline{\tau(a)}$, by polarization of its positivity at $1 + a$ and $1 + ia$. Left multiplication $\pi(p) : b \mapsto pb$ and right multiplication $\rho(p) : b \mapsto bp$ by a projection $p$ are contractions for the semi-norm, hence extend to $\mathcal{H}$. For $\rho$ this uses the trace: $\tau((bp)^*(bp)) = \tau(b^* b p)$ and $\tau(b^* b) - \tau(b^* b p) = \tau((b(1-p))^*(b(1-p))) \geq 0$. Both are symmetric and positive for the form; for $\rho$, $\tau((bp)^* c) = \tau(b^* c p)$ and $\tau(b^* b p) = \tau((bp)^*(bp))$. Left and right multiplications commute, by associativity, and each family sums to the identity. Setting $E^x_a = \pi(M^x_a)$ and $F^y_b = \rho(M^y_b)$ gives a commuting-operator strategy with $\langle\xi| E^x_a F^y_b |\xi\rangle = \tau(1^* M^x_a M^y_b) = \tau(M^x_a M^y_b)$, hence with the same value as $({\mathscr{A}}, \tau, M)$. Taking suprema yields the claim. No norm on ${\mathscr{A}}$ is used.

## Lean

Formalized as [`MIPRE.TracialState.im_star_mul_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialState.im_star_mul_self), [`MIPRE.TracialState.map_star`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialState.map_star), [`MIPRE.TracialState.toState`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialState.toState), [`MIPRE.TracialCo.form_mulRight_left`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.form_mulRight_left), [`MIPRE.TracialCo.form_mulRight_self`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.form_mulRight_self), [`MIPRE.TracialCo.bdd_mulRight`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.bdd_mulRight), [`MIPRE.TracialCo.lift_mulRight_isPositive`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.lift_mulRight_isPositive), [`MIPRE.TracialCo.bdd_mulLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.bdd_mulLeft), [`MIPRE.TracialCo.lift_mulLeft_isPositive`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.TracialCo.lift_mulLeft_isPositive), [`MIPRE.CommutingStrategy.toCommutingOperatorStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingStrategy.toCommutingOperatorStrategy), [`MIPRE.CommutingStrategy.correlation_toCommutingOperatorStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingStrategy.correlation_toCommutingOperatorStrategy), [`MIPRE.CommutingStrategy.value_toCommutingOperatorStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.CommutingStrategy.value_toCommutingOperatorStrategy), [`MIPRE.commValue_le_commutingOperatorValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.commValue_le_commutingOperatorValue).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 99](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L99)
