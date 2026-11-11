---
declaration: corollary
origin: cited
lean: ProbabilityTheory.entropy_triple_add_entropy_le
statement: formalized
proof: formalized
---

# Alternate form of submodularity

With three random variables $X,Y,Z$, one has

$$
\mathbb{H}[X,Y,Z] + \mathbb{H}[Z] \leq \mathbb{H}[X,Z] + \mathbb{H}[Y,Z].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Submodularity](../part-01/submodularity.md)
- [Chain rule](../part-01/chain-rule.md)

## Proof

Apply [Submodularity](../part-01/submodularity.md) and [Chain rule](../part-01/chain-rule.md).

## Lean

Formalized as [`ProbabilityTheory.entropy_triple_add_entropy_le`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.entropy_triple_add_entropy_le).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 232](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L232)
