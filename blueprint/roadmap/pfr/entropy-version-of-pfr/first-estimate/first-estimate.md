---
declaration: lemma
origin: cited
lean: first_estimate
statement: formalized
proof: formalized
---

# First estimate

We have $I_1 \leq 2 \eta k$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Fibring identity for first estimate](first-fibre.md)
- [Lower bound on distances](first-dist-sum.md)
- [Lower bound on conditional distances](first-cond.md)
- [Upper bound on distance differences](first-upper.md)

## Proof

Take a suitable linear combination of [Fibring identity for first estimate](first-fibre.md), [Lower bound on distances](first-dist-sum.md), [Lower bound on conditional distances](first-cond.md), and [Upper bound on distance differences](first-upper.md).

## Lean

Formalized as [`first_estimate`](https://teorth.github.io/pfr/docs/find/#doc/first_estimate).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy_pfr.tex, line 129](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy_pfr.tex#L129)
