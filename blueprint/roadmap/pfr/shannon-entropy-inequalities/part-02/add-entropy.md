---
declaration: corollary
origin: cited
lean: ProbabilityTheory.entropy_pair_eq_add
statement: formalized
proof: formalized
---

# Additivity of entropy

If $X,Y$ are random variables, then $\mathbb{H}[X,Y] = \mathbb{H}[X] + \mathbb{H}[Y]$ if and only if $X,Y$ are independent.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Vanishing of mutual information](vanish-entropy.md)

## Proof

Direct from [Vanishing of mutual information](vanish-entropy.md).

## Lean

Formalized as [`ProbabilityTheory.entropy_pair_eq_add`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_pair_eq_add).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 263](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L263)
