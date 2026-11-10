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

- [Polynomial Freiman-Ruzsa blueprint: chapter/entropy.tex, line 135](https://github.com/teorth/pfr/blob/1ef23c3c5a83db690fe3b3b5c2e8299fae17b81a/blueprint/src/chapter/entropy.tex#L135)
