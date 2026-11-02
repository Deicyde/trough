---
declaration: corollary
origin: cited
lean: ProbabilityTheory.max_entropy_le_entropy_add, ProbabilityTheory.max_entropy_le_entropy_sub
statement: formalized
proof: formalized
---

# Independent lower bound on sumset

If $X,Y$ are independent $G$-valued random variables, then

$$
\max(\mathbb{H}[X], \mathbb{H}[Y]) \leq \mathbb{H}[X\pm Y].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Lower bound of sumset](sumset-lower-gen.md)
- [Vanishing of mutual information](../../shannon-entropy-inequalities/part-02/vanish-entropy.md)

## Proof

Combine [Lower bound of sumset](sumset-lower-gen.md) with [Vanishing of mutual information](../../shannon-entropy-inequalities/part-02/vanish-entropy.md).

## Lean

Formalized as [`ProbabilityTheory.max_entropy_le_entropy_add`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_entropy_le_entropy_add), [`ProbabilityTheory.max_entropy_le_entropy_sub`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_entropy_le_entropy_sub).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 49](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/distance.tex#L49)
