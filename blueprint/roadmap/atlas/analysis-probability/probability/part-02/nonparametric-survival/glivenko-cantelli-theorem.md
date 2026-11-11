---
declaration: section
origin: cited
lean: MathlibExt.Probability.Statistics.GlivenkoCantelliWanted.empiricalCount, MathlibExt.Probability.Statistics.GlivenkoCantelliWanted.glivenko_cantelli
statement: formalized
proof: formalized
---

# Glivenko–Cantelli theorem

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/glivenko-cantelli-theorem/index.html).

## Empirical count

Let $X_0, X_1, X_2, \dots$ be real-valued functions on a set $\Omega$.
For a natural number $n$, a point $\omega \in \Omega$ and a real number $x$, the empirical count is
the number of indices $i \in \{0, 1, \dots, n\}$ with $X_i(\omega) \le x$. Divided by $n + 1$, it
is the value at $x$ of the empirical distribution function of $X_0(\omega), \dots, X_n(\omega)$.

Formalized by `MathlibExt.Probability.Statistics.GlivenkoCantelliWanted.empiricalCount`, a definition declared in [MathlibExt/Probability/Statistics/GlivenkoCantelli.lean, line 36](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GlivenkoCantelli.lean#L36). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/glivenko-cantelli-theorem/index.html#empirical-count).

## Glivenko–Cantelli theorem

Let $P$ be a probability measure on a measurable space $\Omega$,
and let $X_0, X_1, X_2, \dots$ be measurable real-valued functions on $\Omega$ that are mutually
independent under $P$ and each have the same distribution as $X_0$. Write $F(x) = P(X_0 \le x)$
for the distribution function of $X_0$, and $C_n(\omega, x)$ for the empirical count, the number
of indices $i \in \{0, 1, \dots, n\}$ with $X_i(\omega) \le x$. Then for $P$-almost every
$\omega \in \Omega$: for every $\varepsilon > 0$ there is a natural number $N$ such that for all
$n \ge N$ and all real $x$,

$$\left| \frac{C_n(\omega, x)}{n + 1} - F(x) \right| < \varepsilon.$$

That is, almost surely the empirical distribution function of $X_0, \dots, X_n$ converges to $F$
uniformly on $\mathbb{R}$.

## Sources

- V. Glivenko, Sulla determinazione empirica delle leggi di probabilita, Giorn. Ist. Ital. Attuari 4 (1933) 92–99; F. Cantelli 1933; textbook in Durrett, Probability Theory and Examples, 5th ed., Probability and Measure

Formalized by `MathlibExt.Probability.Statistics.GlivenkoCantelliWanted.glivenko_cantelli`, a theorem declared in [MathlibExt/Probability/Statistics/GlivenkoCantelli.lean, line 318](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Probability/Statistics/GlivenkoCantelli.lean#L318). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/glivenko-cantelli-theorem/index.html#glivenko-cantelli).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Glivenko–Cantelli theorem](https://deicyde.github.io/atlas-lean/roadmap/Probability/nonparametric-survival/glivenko-cantelli-theorem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Probability/nonparametric-survival/glivenko-cantelli-theorem)
