---
declaration: lemma
origin: cited
lean: MIPRE.ValueApprox.rePred_lt_quantumValue, MIPRE.ValueApprox.RawStrategy, MIPRE.ValueApprox.RawStrategy.interp, MIPRE.ValueApprox.Check, MIPRE.ValueApprox.primrecPred_check, MIPRE.ValueApprox.check_iff_interp, MIPRE.ValueApprox.exists_check_iff, MIPRE.ValueApprox.REPred.of_primrecRel_exists, MIPRE.rePred_lt_quantumValue_comp, MIPRE.exists_semidecider_lt_quantumValue, MIPRE.Cost.exists_semidecider
statement: formalized
proof: formalized
---

# The value is approximable from below

Write $\mathfrak{G}_g$ for the game described by a game description $g$ (Definition [Game description](../../foundations/part-02/def-game-description.md)). The set

$$
\{ (g, p, q) : g \text{ a game description},\ p, q \in \mathbb{N},\ \mathrm{val}^*(\mathfrak{G}_g) > p/q \}
$$

is recursively enumerable.

## Depends on

- [Game description](../../foundations/part-02/def-game-description.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Exact rational strategies suffice](lem-rational-strategies-suffice.md)

## Proof

By Lemma [Exact rational strategies suffice](lem-rational-strategies-suffice.md), $\mathrm{val}^*(\mathfrak{G}_g) > p/q$ if and only if some valid exact strategy with entries in $\mathbb{Q}(i)$ has value greater than $p/q$. A *raw candidate* is a common denominator $k$, two dimensions, the Gaussian-integer numerators of the two players' operators as lists of list matrices, and the numerators of the state; it denotes the exact strategy with entries divided by $k$, and every valid exact strategy with $\mathbb{Q}(i)$ entries is denoted by one (clear a common denominator of its finitely many entries). Raw candidates are first-order data, hence enumerable. For a raw candidate the check “$k > 0$, each family of operators is Hermitian, idempotent ($M^2 = kM$) and sums to $k{I}$, the state is nonzero, and $p \cdot W \cdot k^2 \cdot \langle v, v\rangle < q \cdot \sum_{x,y} w(x,y) \sum_{a,b} D(x,y,a,b)\, \mathrm{re}\langle v, (A^x_a \otimes B^y_b) v\rangle$” is a finite conjunction of polynomial identities and one comparison in Gaussian-integer arithmetic, so it is primitive recursive, and it holds if and only if the denoted strategy is valid with value greater than $p/q$ (for $q = 0$, where $p/q = 0$, the comparison is replaced by positivity of the numerator). Dovetailing over the candidates and halting on the first that passes the check therefore halts exactly when $\mathrm{val}^*(\mathfrak{G}_g) > p/q$; the boundary case $\mathrm{val}^*(\mathfrak{G}_g) = p/q$ is correctly non-halting.

## Lean

Formalized as [`MIPRE.ValueApprox.rePred_lt_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.rePred_lt_quantumValue), [`MIPRE.ValueApprox.RawStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.RawStrategy), [`MIPRE.ValueApprox.RawStrategy.interp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.RawStrategy.interp), [`MIPRE.ValueApprox.Check`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.Check), [`MIPRE.ValueApprox.primrecPred_check`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.primrecPred_check), [`MIPRE.ValueApprox.check_iff_interp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.check_iff_interp), [`MIPRE.ValueApprox.exists_check_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.exists_check_iff), [`MIPRE.ValueApprox.REPred.of_primrecRel_exists`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.ValueApprox.REPred.of_primrecRel_exists), [`MIPRE.rePred_lt_quantumValue_comp`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.rePred_lt_quantumValue_comp), [`MIPRE.exists_semidecider_lt_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.exists_semidecider_lt_quantumValue), [`MIPRE.Cost.exists_semidecider`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Cost.exists_semidecider).

## Sources

- [MIP* = RE blueprint: content/03_background_results.tex, line 7267](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/03_background_results.tex#L7267)
