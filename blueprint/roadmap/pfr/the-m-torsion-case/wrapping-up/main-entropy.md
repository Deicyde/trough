---
declaration: theorem
origin: cited
lean: dist_of_X_U_H_le
statement: formalized
proof: formalized
---

# Entropy form of PFR

Suppose that $G$ is a finite abelian group of torsion $m$. Suppose that $X$ is a $G$-valued random variable. Then there exists a subgroup $H \leq G$ such that

$$
d[X;U_H] \leq 64 m^3 d[X;X].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Vanishing entropy](../endgame/k-vanish.md)
- [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md)
- [$\tau$ functional](../../entropy-version-of-pfr/tau-def.md)
- [Vanishing](../multidistance/multi-zero.md)
- [$\eta$](../the-tau-functional/eta-def-multi.md)
- [Minimizer close to reference variables](../the-tau-functional/tau-ref.md)
- [Existence of $\tau$-minimizer](../the-tau-functional/tau-min-exist-multi.md)

## Proof

Set $X^0 := X$. By [Existence of $\tau$-minimizer](../the-tau-functional/tau-min-exist-multi.md), there exists a $\tau$-minimizer $X_{[m]} = (X_i)_{1 \leq i \leq m}$. By [Vanishing entropy](../endgame/k-vanish.md), we have $D[X_{[m]}]=0$. By [Minimizer close to reference variables](../the-tau-functional/tau-ref.md) and the pigeonhole principle, there exists $1 \leq i \leq m$ such that $d[X_i; X] \leq \frac{2}{\eta} d[X;X]$. By [Vanishing](../multidistance/multi-zero.md), we have $d[X_i;U_H]=0$ for some subgroup $H \leq G$, hence by [Ruzsa triangle inequality](../../entropic-ruzsa-calculus/part-01/ruzsa-triangle.md) we have $d[U_H; X] \leq \frac{2}{\eta} d[X;X]$. The claim then follows from [$\eta$](../the-tau-functional/eta-def-multi.md).

## Lean

Formalized as [`dist_of_X_U_H_le`](https://teorth.github.io/pfr/docs/find/#doc/dist_of_X_U_H_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/torsion.tex, line 874](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/torsion.tex#L874)
