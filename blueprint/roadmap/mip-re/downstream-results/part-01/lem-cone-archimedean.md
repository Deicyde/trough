---
declaration: lemma
origin: cited
lean: MIPRE.NCPoly.star_mul_mul_mem_qmod_of_mem, MIPRE.NCPoly.archimedean_of_gen, MIPRE.Tsirelson.cone_archimedean, MIPRE.NCPoly.re_inner_eval_nonneg, MIPRE.Tsirelson.strategy_nonneg, MIPRE.Tsirelson.value_le_of_mem
statement: formalized
proof: formalized
---

# The cone is Archimedean and positive on strategies

$a^* M a \subseteq M$ for every $a \in P$, and for every $y \in P$ some real $N$ has $N \cdot 1 + y \in M$. Evaluating the variables at the effects of a commuting-operator strategy gives $\mathrm{Re} \langle \psi, m(E, F) \psi \rangle \geq 0$ for every $m \in M$; in particular $r \cdot 1 - W_\mathfrak{G} \in M$ bounds the value of every strategy by $r$.

## Depends on

- [The measurement algebra and its cone](def-measurement-algebra.md)
- [Commuting-operator value](../../parallel-repetition/def-co-value-bipartite.md)

## Proof

$1 - e_{xa} = \sum_{a' \neq a} e_{xa'} - (\sum_{a'} e_{xa'} - 1) \in M$, and $e - e^2 = e(1 - e)e + (1 - e)e(1 - e) \in M$, so $1 - g^2 \in M$ for every variable $g$ and, telescoping, $1 - w^* w \in M$ for every word $w$. Then $(1 + \left\vert {\alpha} \right\vert^2) \cdot 1 + \alpha w + (\alpha w)^* = (1 + \alpha w)^*(1 + \alpha w) + \left\vert {\alpha} \right\vert^2 (1 - w^* w)$, and the anti-hermitian part of a monomial lies in $M$. On a strategy the relations evaluate to $0$, $\langle \psi, s^* g s \psi \rangle = \langle s\psi, g\, s\psi \rangle \geq 0$ for positive $g$, and anti-hermitian operators have imaginary expectations.

## Lean

Formalized as [`MIPRE.NCPoly.star_mul_mul_mem_qmod_of_mem`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.star_mul_mul_mem_qmod_of_mem), [`MIPRE.NCPoly.archimedean_of_gen`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.archimedean_of_gen), [`MIPRE.Tsirelson.cone_archimedean`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.cone_archimedean), [`MIPRE.NCPoly.re_inner_eval_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.NCPoly.re_inner_eval_nonneg), [`MIPRE.Tsirelson.strategy_nonneg`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.strategy_nonneg), [`MIPRE.Tsirelson.value_le_of_mem`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.value_le_of_mem).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 174](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L174)
