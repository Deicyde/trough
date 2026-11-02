---
declaration: lemma
origin: cited
lean: torsion_dist_shrinking
statement: formalized
proof: formalized
---

# torsion-dist-shrinking

If $G$ is a torsion-free group and $X,Y$ are $G$-valued random variables and $\phi:G\to \mathbb{F}_2^d$ is a homomorphism then

$$
\mathbb{H}(\phi(X))\leq 10d[X;Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [fibring-ineq](../the-fibring-lemma/fibring-ineq.md)
- [torsion-free-doubling](torsion-free-doubling.md)
- [Distance from zero](../entropic-ruzsa-calculus/part-01/dist-zero.md)

## Proof

By [Corollary fibring-ineq](../the-fibring-lemma/fibring-ineq.md) and [Lemma torsion-free-doubling](torsion-free-doubling.md) we have

$$
d[\phi(X);\phi(2Y)]\leq d[X;2Y]\leq 5d[X;Y]
$$

and $\phi(2Y)=2\phi(Y)\equiv 0$ so the left-hand side is equal to $d[\phi(X);0]=\mathbb{H}(\phi(X))/2$ (using [Distance from zero](../entropic-ruzsa-calculus/part-01/dist-zero.md)).

## Lean

Formalized as [`torsion_dist_shrinking`](https://teorth.github.io/pfr/docs/find/#doc/torsion_dist_shrinking).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/weak_pfr.tex, line 41](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/weak_pfr.tex#L41)
