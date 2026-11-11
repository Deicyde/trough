---
declaration: corollary
origin: cited
lean: ProbabilityTheory.ent_of_cond_indep
statement: formalized
proof: formalized
---

# Entropy of conditionally independent variables

If $X, Y$ are conditionally independent over $Z$, then

$$
\mathbb{H}[X,Y,Z] =\mathbb{H}[X,Z] + \mathbb{H}[Y,Z] - \mathbb{H}[Z].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Vanishing conditional mutual information](conditional-vanish.md)
- [Alternate formula for conditional mutual information](conditional-mutual-alt.md)

## Proof

Immediate from [Vanishing conditional mutual information](conditional-vanish.md) and [Alternate formula for conditional mutual information](conditional-mutual-alt.md).

## Lean

Formalized as [`ProbabilityTheory.ent_of_cond_indep`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.ent_of_cond_indep).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 322](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L322)
