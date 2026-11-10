---
declaration: lemma
origin: cited
lean: goursat
statement: formalized
proof: formalized
---

# Goursat type theorem

Let $H$ be a subgroup of $G \times G'$. Then there exists a subgroup $H_0$ of $G$, a subgroup $H_1$ of $G'$, and a homomorphism $\phi: G \to G'$ such that

$$
H := \{ (x, \phi(x) + y): x \in H_0, y \in H_1 \}.
$$

In particular, $|H| = |H_0| |H_1|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Hahn-Banach type theorem](hb-thm.md)

## Proof

We can take $H_0$ to be the projection of $H$ to $G$, and $H_1$ to be the slice $H_1 := \{ y: (0,y) \in H \}$. One can construct $\phi$ on $H_0$ one generator at a time by the greedy algorithm, and then extend to $G$ by [Hahn-Banach type theorem](hb-thm.md). The cardinality bound is clear from direct counting.

## Lean

Formalized as [`goursat`](https://teorth.github.io/pfr/docs/find/#doc/goursat).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/hom_pfr.tex, line 11](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/hom_pfr.tex#L11)
