---
declaration: lemma
origin: cited
lean: card_of_dual_constrained
statement: formalized
proof: formalized
---

# Counting

Let $G$ be a finite abelian $2$-group, and let $x \in G$ be non-zero. Then there are $|G|/2$ homomorphisms $\phi: G \to \mathbb{Z}/2\mathbb{Z}$ such that $\phi(x) = 1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Duality](gdual.md)

## Proof

The map $\phi \mapsto \phi(x)$ is a homomorphism from $\mathrm{Hom}(G,\mathbb{Z}/2\mathbb{Z})$ to $\mathbb{Z}/2\mathbb{Z}$, and by Lemma [Duality](gdual.md) the kernel has order equal to the order of $G / \{0,x\}$, which is $|G|/2$. Then the preimage of $1$ must also be of order $|G|/2$.

## Lean

Formalized as [`card_of_dual_constrained`](https://teorth.github.io/pfr/docs/find/#doc/card_of_dual_constrained).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 109](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/approx_hom_pfr.tex#L109)
