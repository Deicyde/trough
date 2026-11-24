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

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 49](https://github.com/teorth/pfr/blob/1899ce8ed95fc310cce53d4c7ecfa2beb20ebec4/blueprint/src/chapter/distance.tex#L49)
