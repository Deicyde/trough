---
declaration: lemma
origin: cited
lean: Cayley.trig_err, Cayley.cos_tab_err, Cayley.sin_tab_err
statement: formalized
proof: formalized
---

# trig_table

For $k = 0, \dots, 14$, the checker's tables of $\cos(2\pi k/15)$ and $\sin(2\pi k/15)$ (dyadic numbers with denominator $2^{80}$) are within $2^{-71}$ of the true values.

## Depends on

- [theta1](lem-theta1.md)

## Proof

Let $z_k = e^{2\pi i k/15}$ and let $\hat z_k$ be the table entry. Then $|z_1 - \hat z_1| \le 2^{-79}$ by Lemma [theta1](lem-theta1.md), and $z_{k+1} = z_k z_1$, so $|z_{k+1} - \hat z_{k+1}| \le |z_k - \hat z_k| + |\hat z_k|\, 2^{-79} + |\hat z_k \hat z_1 - \hat z_{k+1}|$. The last two terms are computed exactly in $\operatorname{\mathbb{Q}}$ and are at most $2^{-75}$ for each $k$, so $|z_k - \hat z_k| \le k\, 2^{-75}$.

## Lean

Formalized as [`Cayley.trig_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.trig_err), [`Cayley.cos_tab_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.cos_tab_err), [`Cayley.sin_tab_err`](https://jcreedcmu.github.io/Noperthedron/docs/find/#doc/Cayley.sin_tab_err).

## Sources

- [Noperthedron blueprint: chapters/data.tex, line 33](https://github.com/jcreedcmu/Noperthedron/blob/434011e647523fac1a7116a77df5ac6f283e3fbb/blueprint/src/chapters/data.tex#L33)
