---
declaration: lemma
origin: cited
lean: ent_ofsum_le
statement: formalized
proof: formalized
---

# Entropy bound on quadruple sum

With the same notation, we have

$$
\mathbb{H}[X_1+X_2+\tilde X_1+\tilde X_2] \le \tfrac{1}{2} \mathbb{H}[X_1]+\tfrac{1}{2} \mathbb{H}[X_2] + (2 + \eta) k - I_1.\qquad\text{(1)}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Lower bound on conditional distances](first-cond.md)
- [Fibring identity for first estimate](first-fibre.md)
- [Upper bound on distance differences](first-upper.md)
- [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md)

## Proof

Subtracting [Lower bound on conditional distances](first-cond.md) from [Fibring identity for first estimate](first-fibre.md), and combining the resulting inequality with [Upper bound on distance differences](first-upper.md) gives the bound

$$
d[X_1+\tilde X_2;X_2+\tilde X_1] \le (1 + \eta) k - I_1,
$$

and the claim follows from [Ruzsa distance in independent case](../../entropic-ruzsa-calculus/part-01/ruz-indep.md) and the definition of $k$.

## Lean

Formalized as [`ent_ofsum_le`](https://teorth.github.io/pfr/docs/find/#doc/ent_ofsum_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 138](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy_pfr.tex#L138)
