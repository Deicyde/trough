---
declaration: lemma
origin: cited
lean: RelaxedWeakCentralGroupoid.strictify
statement: formalized
---

# Reversing the claims

Let $G$ be a directed graph, with some paths of length two in the graph designated as “good”, in such a way that Claims 1-4 hold. Then there is a weak central groupoid structure on the vertices of $G$ such that the good paths are precisely the paths of the form $x \to x \diamond y \to y$.

## Depends on

- [Claim 4](claim-4.md)

## Proof

Define an operation $\diamond: G \times G \to G$ by defining $x \diamond y$ to be the unique vertex $z$ for which one has a good path $x \to z \to y$; this is well-defined by Claim 1, and by Claims 2-3, the property $x \to y$ holds if and only if $y = x \diamond z$ for some $z$, and also if and only if $x = w \diamond y$ for some $w$. In particular, for all $x,y,z$, we have a $5$-cycle

$$
y \to y \diamond x \to x \to x \diamond (z \diamond y) \to (z \diamond y) \to y
$$

with $y \to y \diamond x \to x$ and $x \to x \diamond (z \diamond y) \to (z \diamond y)$ good, hence by Claim 4 we have 1485 as required.

## Lean

Formalized as [`RelaxedWeakCentralGroupoid.strictify`](https://teorth.github.io/equational_theories/docs/find/#doc/RelaxedWeakCentralGroupoid.strictify).

## Sources

- [Equational Theories blueprint: chapter/weak_central_groupoids.tex, line 57](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/weak_central_groupoids.tex#L57)
