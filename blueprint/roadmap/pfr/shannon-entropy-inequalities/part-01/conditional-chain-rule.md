---
declaration: lemma
origin: cited
lean: ProbabilityTheory.cond_chain_rule, ProbabilityTheory.cond_chain_rule'
statement: formalized
proof: formalized
---

# Conditional chain rule

If $X: \Omega \to S$, $Y: \Omega \to T$, $Z: \Omega \to U$ are random variables, then

$$
\mathbb{H}[X, Y | Z] = \mathbb{H}[Y | Z] + \mathbb{H}[X|Y, Z].
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Chain rule](chain-rule.md)

## Proof

For each $z \in U$, we can apply [Chain rule](chain-rule.md) to the random variables $(X|Z=z)$ and $(Y|Z=z)$ to obtain

$$
\mathbb{H}[(X|Z=z),(Y|Z=z)] = \mathbb{H}[Y|Z=z] + \mathbb{H}[(X|Z=z)|(Y|Z=z)].
$$

Now multiply by $\mathbb{P}[Z=z]$ and sum. Some helper lemmas may be needed to get to the form above. This sort of “average over conditioning” argument to get conditional entropy inequalities from unconditional ones is commonly used in this paper.

## Lean

Formalized as [`ProbabilityTheory.cond_chain_rule`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.cond_chain_rule), [`ProbabilityTheory.cond_chain_rule'`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.cond_chain_rule').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 147](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L147)
