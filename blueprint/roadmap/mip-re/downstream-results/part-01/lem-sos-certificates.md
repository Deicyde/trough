---
declaration: lemma
origin: cited
lean: MIPRE.Tsirelson.Dominant, MIPRE.Tsirelson.re_inner_eval_ge, MIPRE.Tsirelson.commutingOperatorValue_lt_of_certificate, MIPRE.Tsirelson.exists_certificate_of_lt, MIPRE.Tsirelson.exists_certificate_iff
statement: formalized
proof: formalized
---

# Exact sum-of-squares certificates

Call $z \in P$ *dominant* if the real part of its constant coefficient exceeds the sum of $\left\vert {\mathrm{Re}\, z_w} \right\vert + \left\vert {\mathrm{Im}\, z_w} \right\vert$ over the nonempty words $w$. Let $\kappa > 0$ and suppose the answer sets are nonempty. Then ${\omega^{\mathrm{co}}}(\mathfrak{G}) < r$ if and only if there are $N \geq 1$, finitely many pairs $(g_i, s_i)$ with $g_i \in \{1, e_{xa}, f_{yb}\}$ and $s_i \in P$, and finitely many $(c_t, w_t, \rho_t, w'_t)$ with $c_t \in \mathbb{C}$, words $w_t, w'_t$ and relations $\rho_t$, all coefficients Gaussian integers, such that $T + T^*$ is dominant, where $T = N^2 \kappa (r \cdot 1 - W_\mathfrak{G}) - \sum_i s_i^* g_i s_i - \sum_t c_t w_t \rho_t w'_t$.

## Depends on

- [Positivstellensatz for the commuting-operator value](thm-nc-positivstellensatz.md)

## Proof

Soundness: every word acts as a contraction, so on every strategy $2 N^2 \kappa (r - \text{value}) \geq \mathrm{Re} \langle \psi, (T + T^*)\psi \rangle$ is at least the dominance margin of $T + T^*$, uniformly over strategies. Completeness: take ${\omega^{\mathrm{co}}}(\mathfrak{G}) < r' < r$; Theorem [Positivstellensatz for the commuting-operator value](thm-nc-positivstellensatz.md) writes $\kappa(r \cdot 1 - W_\mathfrak{G}) = \varepsilon \cdot 1 + \sum_i \sigma_i^* g_i \sigma_i + \sum_t c_t w_t \rho_t w'_t + a$ with $\varepsilon = \kappa(r - r') > 0$ and $a$ anti-hermitian, which symmetrization removes. Rounding the coefficients of the $\sigma_i$ at scale $N$ and the $c_t$ at scale $N^2$ changes $T + T^*$ by $O(N)$ in the $\ell^1$ norm of coefficients (submultiplicative and star-invariant), against a constant term $2N^2\varepsilon$.

## Lean

Formalized as [`MIPRE.Tsirelson.Dominant`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.Dominant), [`MIPRE.Tsirelson.re_inner_eval_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.re_inner_eval_ge), [`MIPRE.Tsirelson.commutingOperatorValue_lt_of_certificate`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.commutingOperatorValue_lt_of_certificate), [`MIPRE.Tsirelson.exists_certificate_of_lt`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.exists_certificate_of_lt), [`MIPRE.Tsirelson.exists_certificate_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tsirelson.exists_certificate_iff).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 266](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L266)
