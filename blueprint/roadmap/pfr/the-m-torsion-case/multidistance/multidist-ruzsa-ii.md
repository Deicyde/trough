---
declaration: lemma
origin: cited
lean: multidist_ruzsa_II
statement: formalized
proof: formalized
---

# Multidistance and Ruzsa distance, II

Let $m \ge 2$, and let $X_{[m]}$ be a tuple of $G$-valued random variables. Then

$$
\sum_{j=1}^m d[X_j;X_j] \leq 2 m D[X_{[m]}].
$$

## Depends on

- [Multidistance](multidist-def.md)

## Proof depends on

- [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)
- [Multidistance and Ruzsa distance, I](multidist-ruzsa-i.md)

## Proof

From [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) we have $d[X_j;X_j] \leq 2 d[X_j;-X_k]$, and applying this to every summand in [Multidistance and Ruzsa distance, I](multidist-ruzsa-i.md), we obtain the claim.

## Lean

Formalized as [`multidist_ruzsa_II`](https://teorth.github.io/pfr/docs/find/#doc/multidist_ruzsa_II).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 222](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/torsion.tex#L222)
