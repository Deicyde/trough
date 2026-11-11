---
declaration: corollary
origin: cited
lean: ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_mul, ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_div
statement: formalized
proof: formalized
---

# Conditional lower bound on sumset

If $X,Y$ are $G$-valued random variables on $\Omega$ and $Z$ is another random variable on $\Omega$ then

$$
\max(\mathbb{H}[X|Z], \mathbb{H}[Y|Z]) -  \mathbb{I}[X:Y|Z] \leq \mathbb{H}[X\pm Y|Z],
$$

## Depends on

- [Conditional mutual information](../../shannon-entropy-inequalities/part-02/conditional-mutual-def.md)

## Proof depends on

- [Lower bound of sumset](sumset-lower-gen.md)

## Proof

This follows from [Lower bound of sumset](sumset-lower-gen.md) by conditioning to $Z = z$ and summing over $z$ (weighted by $\mathbb{P}[Z=z]$).

## Lean

Formalized as [`ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_mul`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_mul), [`ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_div`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.max_condEntropy_sub_condMutualInfo_le_condEntropy_div).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/distance.tex, line 37](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/distance.tex#L37)
