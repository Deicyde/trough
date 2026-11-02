---
declaration: lemma
origin: cited
lean: ProbabilityTheory.condMutualInfo_eq_zero
statement: formalized
proof: formalized
---

# Vanishing conditional mutual information

If $X,Y,Z$ are random variables, then $\mathbb{I}[X:Y|Z] = 0$ iff $X,Y$ are conditionally independent over $Z$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Vanishing of mutual information](vanish-entropy.md)
- [Conditionally independent random variables](conditional-independent-def.md)

## Proof

Immediate from [Vanishing of mutual information](vanish-entropy.md) and [Conditionally independent random variables](conditional-independent-def.md).

## Lean

Formalized as [`ProbabilityTheory.condMutualInfo_eq_zero`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.condMutualInfo_eq_zero).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 313](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L313)
