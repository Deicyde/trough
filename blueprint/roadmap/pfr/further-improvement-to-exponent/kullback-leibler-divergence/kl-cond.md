---
declaration: lemma
origin: cited
lean: condKLDiv_eq
statement: formalized
proof: formalized
---

# Kullback–Leibler and conditioning

If $X, Y$ are independent $G$-valued random variables, and $Z$ is another random variable defined on the same sample space as $X$, then

$$
D_{KL}((X|Z)\Vert Y) = D_{KL}(X\Vert Y) + \mathbb{H}[X] - \mathbb{H}[X|Z].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Compare the terms correspond to each $x\in G$ on both sides.

## Lean

Formalized as [`condKLDiv_eq`](https://teorth.github.io/pfr/docs/find/#doc/condKLDiv_eq).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/further_improvement.tex, line 70](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/further_improvement.tex#L70)
