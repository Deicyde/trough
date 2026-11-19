---
declaration: lemma
origin: cited
lean: Pairwise.countable_of_isOpen_disjoint
statement: formalized
proof: formalized
---

# Disjoint family countable

In a doubling metric measure space $(X,\rho,\mu, a)$, every disjoint family of balls $B_j = B(x_j, r_j)$, $j\in J$, is countable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Choose an arbitrary $x\in X$ as reference point. For $q, Q\in{\mathbb{Q}}_+$, let $J_{q,Q}$ denote the set of all $j\in J$ such that $B_j\subset B(x, Q)$ and $r_j \ge q$. It suffices to show that all the $J_{q,Q}$ are finite. Indeed, for all $j\in J_{q,Q}$,

$$
\mu(B(x, Q)) \le \mu(B(x_j, 2Q)) = \mu(B(x_j, \frac{2 Q}{r_j} r_j))
\le 2^{a\log_2{\lceil \frac{2 Q}{r_j}\rceil}} \mu(B_j).
$$

Since the $B_j$ are disjoint,

$$
|J_{q,Q}| \mu(B(x, Q)) \le 2^{a\log_2{\lceil\frac{2Q}{q}\rceil}} \sum_{j\in J_{q,Q}} \mu(B_j) \le 2^{a\log_2{\lceil\frac{2Q}{q}\rceil}} \mu(B(x,Q))
$$

and hence $|J_{q,Q}| \le 2^{a\log_2{\lceil\frac{2Q}{q}\rceil}}$.

## Lean

Formalized as [`Pairwise.countable_of_isOpen_disjoint`](https://fpvandoorn.github.io/carleson/docs/find/#doc/Pairwise.countable_of_isOpen_disjoint).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 7594](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L7594)
