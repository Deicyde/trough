---
declaration: lemma
origin: cited
lean: KLDiv_add_le_KLDiv_of_indep
statement: formalized
proof: formalized
---

# Kullback–Leibler and sums

If $X, Y, Z$ are independent $G$-valued random variables, then

$$
D_{KL}(X+Z\Vert Y+Z) \leq D_{KL}(X\Vert Y).
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Kullback–Leibler and injections](kl-div-inj.md)
- [Convexity of Kullback–Leibler](kl-div-convex.md)

## Proof

For each $z$, $D_{KL}(X+z\Vert Y+z)=D_{KL}(X\Vert Y)$ by [Kullback–Leibler and injections](kl-div-inj.md). Then apply [Convexity of Kullback–Leibler](kl-div-convex.md) with $w_z=\mathbf{P}(Z=z)$.

## Lean

Formalized as [`KLDiv_add_le_KLDiv_of_indep`](https://teorth.github.io/pfr/docs/find/#doc/KLDiv_add_le_KLDiv_of_indep).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 56](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L56)
