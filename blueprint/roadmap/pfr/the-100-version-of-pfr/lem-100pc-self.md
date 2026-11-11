---
declaration: lemma
origin: cited
lean: exists_isUniform_of_rdist_self_eq_zero
statement: formalized
proof: formalized
---

# Symmetric 100% inverse theorem

Suppose that $X$ is a $G$-valued random variable such that $d[X ;X]=0$. Then there exists a subgroup $H \leq G$ such that $d[X ;U_H] = 0$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Symmetry group is a group](sym-group.md)
- [Translate is uniform on symmetry group](sym-zero.md)

## Proof

Take $H$ to be the symmetry group of $X$, which is a group by [Symmetry group is a group](sym-group.md). From [Translate is uniform on symmetry group](sym-zero.md), $X-x_0$ is uniform on $H$, and $d[X ;X-x_0] = d[X ;X] \leq 0$, and the claim follows.

## Lean

Formalized as [`exists_isUniform_of_rdist_self_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/exists_isUniform_of_rdist_self_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/100_percent.tex, line 41](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/100_percent.tex#L41)
