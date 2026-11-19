---
declaration: theorem
origin: cited
lean: MIPRE.exists_separating_functional_of_archimedean, MIPRE.Tsirelson.exists_isConeState_of_not_mem, MIPRE.Tsirelson.sub_gamePoly_mem_cone_of_lt, MIPRE.Tsirelson.commutingOperatorValue_lt_iff
statement: formalized
proof: formalized
---

# Positivstellensatz for the commuting-operator value

If ${\omega^{\mathrm{co}}}(\mathfrak{G}) < r$ then $r \cdot 1 - W_\mathfrak{G} \in M$. With nonempty answer sets, ${\omega^{\mathrm{co}}}(\mathfrak{G}) < r$ holds exactly when $r' \cdot 1 - W_\mathfrak{G} \in M$ for some $r' < r$.

## Depends on

- [Cone states are the states of commuting-operator strategies](lem-cone-state-gns.md)

## Proof depends on

- [Basic properties of the correlation sets](lem-correlation-sets-basic.md)

## Proof

If $h = r \cdot 1 - W_\mathfrak{G} \notin M$, the Riesz extension theorem applied to the cone $M + \mathbb{R}_{\geq 0}(-h)$, with the functional $t \cdot 1 \mapsto t$ on the span of $1$, gives a real functional $L_0 \geq 0$ on $M$ with $L_0(1) = 1$ and $L_0(h) \leq 0$; the Archimedean property supplies both hypotheses. Its complexification $L_0(z) - i L_0(iz)$ is a cone state, and Lemma [Cone states are the states of commuting-operator strategies](lem-cone-state-gns.md) turns it into a strategy of value $L_0(W_\mathfrak{G}) \geq r > {\omega^{\mathrm{co}}}(\mathfrak{G})$, a contradiction. The converse is Lemma [The cone is Archimedean and positive on strategies](lem-cone-archimedean.md), with a strategy supplied by the deterministic one.

## Lean

Formalized as [`MIPRE.exists_separating_functional_of_archimedean`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_separating_functional_of_archimedean), [`MIPRE.Tsirelson.exists_isConeState_of_not_mem`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.exists_isConeState_of_not_mem), [`MIPRE.Tsirelson.sub_gamePoly_mem_cone_of_lt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.sub_gamePoly_mem_cone_of_lt), [`MIPRE.Tsirelson.commutingOperatorValue_lt_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.commutingOperatorValue_lt_iff).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 243](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L243)
