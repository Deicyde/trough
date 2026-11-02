---
declaration: lemma
origin: cited
lean: card_of_slice
statement: formalized
proof: formalized
---

# Slicing

Let $G$ be a finite abelian $2$-group, and let $A$ be a subset of $G$. Then there exists a homomorphism $\phi: G \to \mathbb{Z}/2\mathbb{Z}$ such that $|A \cap \phi^{-1}(1)| \geq (|A|-1)/2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Duality](gdual.md)
- [Counting](gcount.md)

## Proof

We have

$$
\sum_{\phi \in \mathrm{Hom}(G,\mathbb{Z}/2\mathbb{Z})} |A \cap \phi^{-1}(1)| = \sum_{x \in A} |\{ \phi \in \mathrm{Hom}(G,\mathbb{Z}/2\mathbb{Z}): \phi(x) = 1 \}|
$$

$$
\geq (|A|-1) |G|/2
$$

thanks to Lemma [Counting](gcount.md). The claim now follows from Lemma [Duality](gdual.md) and the pigeonhole principle.

## Lean

Formalized as [`card_of_slice`](https://teorth.github.io/pfr/docs/find/#doc/card_of_slice).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 115](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/approx_hom_pfr.tex#L115)
