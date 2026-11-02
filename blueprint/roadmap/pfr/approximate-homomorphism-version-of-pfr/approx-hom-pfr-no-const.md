---
declaration: corollary
origin: cited
lean: approx_hom_pfr'
statement: formalized
proof: formalized
---

# Approximate homomorphism form of PFR, no constant term

Let $G,G'$ be finite abelian $2$-groups. Let $f: G \to G'$ be a function, and suppose that there are at least $|G|^2 / K$ pairs $(x,y) \in G^2$ such that

$$
f(x+y) = f(x) + f(y).
$$

Then there exists a homomorphism $\phi'': G \to G'$ such that $f(x) = \phi''(x)$ for at least $(|G| / (2 ^ {144} * K ^ {122}) - 1)/2$ values of $x \in G$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Approximate homomorphism form of PFR](approx-hom-pfr.md)
- [Slicing](gslice.md)

## Proof

By Theorem [Approximate homomorphism form of PFR](approx-hom-pfr.md), there exists a homomorphism $\phi: G \to G'$ and a constant $c \in G'$ such that the set $A := \{ x \in G: f(x) = \phi(x) + c\}$ has cardinality at least $|G| / (2 ^ {144} * K ^ {122})$. By Lemma [Slicing](gslice.md), there exists a homomorphism $\phi': G \to \mathbb{Z}/2\mathbb{Z}$ such that

$$
|A \cap \phi'^{-1}(1)| \geq (|A|-1)/2 \geq (|G| / (2 ^ {144} * K ^ {122}) - 1)/2.
$$

Then the claim follows by taking $\phi'' = \phi + \phi' \bullet c$ (where we view $G'$ as a $\mathbb{Z}/2\mathbb{Z}$-module).

## Lean

Formalized as [`approx_hom_pfr'`](https://teorth.github.io/pfr/docs/find/#doc/approx_hom_pfr').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/approx_hom_pfr.tex, line 124](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/approx_hom_pfr.tex#L124)
