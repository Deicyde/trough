---
declaration: lemma
origin: cited
lean: ProbabilityTheory.chain_rule, ProbabilityTheory.chain_rule'
statement: formalized
proof: formalized
---

# Chain rule

If $X: \Omega \to S$ and $Y: \Omega \to T$ are random variables, then

$$
\mathbb{H}[X, Y] = \mathbb{H}[Y] + \mathbb{H}[X|Y].
$$

## Depends on

- [Conditional entropy](conditional-entropy-def.md)

## Proof

Direct computation.

## Lean

Formalized as [`ProbabilityTheory.chain_rule`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.chain_rule), [`ProbabilityTheory.chain_rule'`](https://teorth.github.io/pfr/docs/find/#doc/ProbabilityTheory.chain_rule').

## Sources

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 135](https://github.com/teorth/pfr/blob/7e7fadf0c4d000fdb21b68505f3fd0e29a6e4a2f/blueprint/src/chapter/entropy.tex#L135)
