---
declaration: lemma
origin: cited
lean: ProbabilityTheory.IsAEKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero
statement: formalized
proof: formalized
---

# IsKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero

Let $X : T \to \Omega \to E$ be a process that satisfies the Kolmogorov condition for exponents $(p,q)$ with constant $M$. Let $T'$ be a countable subset of $T$ such that for all $s, t \in T'$, $d_T(s, t) = 0$. Then

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T'} d_E(X_s, X_t)^p \right]
&= 0
\: .
\end{aligned}
$$

## Depends on

- [Kolmogorov condition](def-iskolmogorovprocess.md)

## Proof depends on

- [IsKolmogorovProcess.edist_eq_zero](lem-iskolmogorovprocess-edist-eq-zero.md)

## Proof

Since $T'$ is countable, we get from Lemma [IsKolmogorovProcess.edist_eq_zero](lem-iskolmogorovprocess-edist-eq-zero.md) that almost surely, for all $s, t \in T'$, $d_E(X_s, X_t)^p = 0$. In particular the expectation of the supremum is $0$.

## Lean

Formalized as [`ProbabilityTheory.IsAEKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.IsAEKolmogorovProcess.lintegral_sup_rpow_edist_eq_zero).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 753](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L753)
