---
declaration: lemma
origin: cited
lean: card_of_dual
statement: formalized
proof: formalized
---

# Duality

Let $G$ be a finite abelian $2$-group. Then the finite abelian $2$-group $\mathrm{Hom}(G,\mathbb{Z}/2\mathbb{Z})$ of homomorphisms from $G$ to $\mathbb{Z}/2\mathbb{Z}$ has the same order as $G$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the classification of finite abelian groups, $G$ is isomorphic to $(\mathbb{Z}/2\mathbb{Z})^n$. Then $\mathrm{Hom}(G,\mathbb{Z}/2\mathbb{Z})$ is isomorphic to $(\mathbb{Z}/2\mathbb{Z})^n$ as well, and hence has the same order.

## Lean

Formalized as [`card_of_dual`](https://teorth.github.io/pfr/docs/find/#doc/card_of_dual).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 103](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/approx_hom_pfr.tex#L103)
