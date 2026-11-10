---
declaration: lemma
origin: cited
lean: ProbabilityTheory.prob_ge_exp_neg_entropy
statement: formalized
proof: formalized
---

# Bounded entropy implies concentration

If $X$ is an $S$-valued random variable, then there exists $s \in S$ such that $\mathbb{P}[X=s] \geq \exp(-\mathbb{H}[X])$.

## Depends on

- [Entropy](entropy-def.md)

## Proof

We have

$$
\mathbb{H}[X] = \sum_{s \in S} \mathbb{P}[X=s] \log \frac{1}{\mathbb{P}[X=s]} \geq \min_{s \in S} \log \frac{1}{\mathbb{P}[X=s]}
$$

and the claim follows.

## Lean

Formalized as [`ProbabilityTheory.prob_ge_exp_neg_entropy`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.prob_ge_exp_neg_entropy).

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 75](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L75)
