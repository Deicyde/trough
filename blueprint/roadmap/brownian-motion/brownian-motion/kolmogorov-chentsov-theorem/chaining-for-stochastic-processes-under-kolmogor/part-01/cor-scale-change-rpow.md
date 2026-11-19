---
declaration: corollary
origin: cited
lean: iSup_edist_rpow_le_iSup_edist_chainingSeq
statement: formalized
proof: formalized
---

# scale_change_rpow

Let $X : T \to E$. Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers, $C_n$ a finite $\varepsilon_n$-cover of $J \subseteq T$ with $C_n \subseteq J$. For $m \le k$,

$$
\begin{aligned}
\sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_s, X_t)^p
&\le 2^p \sup_{s, t \in C_k; d_T(s, t) \le \delta} d_E(X_{\bar{s}_m}, X_{\bar{t}_m})^p
+ 4^p \sup_{s \in C_k} d_E(X_s, X_{\bar{s}_m})^p
\: .
\end{aligned}
$$

## Depends on

- [Chaining sequence](../../chaining/part-01/def-chainingsequence.md)

## Proof depends on

- [scale_change](lem-scale-change.md)

## Proof

This is Lemma [scale_change](lem-scale-change.md), together with the fact that for $a, b \ge 0$,

$$
\begin{aligned}
(a + b)^p \le (2\max(a,b))^p = 2^p \max(a^p,b^p) \le 2^p (a^p + b^p)
\: .
\end{aligned}
$$

## Lean

Formalized as [`iSup_edist_rpow_le_iSup_edist_chainingSeq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/iSup_edist_rpow_le_iSup_edist_chainingSeq).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 922](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L922)
