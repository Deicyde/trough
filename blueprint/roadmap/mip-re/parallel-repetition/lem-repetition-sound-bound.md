---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.repConst, MIPRE.Repetition.card_answers_le, MIPRE.Repetition.exp_le_soundBound, MIPRE.Repetition.quantumValue_repeat_le_soundBound
statement: formalized
proof: formalized
---

# The repetition bound for answers of bounded length

There is a universal constant $c' > 0$ such that for every game $\mathfrak{G}$ whose answer alphabets are the strings of length at most $B$, every $\varepsilon > 0$ with $\mathrm{val}^*(\mathfrak{G}) \leq 1 - \varepsilon$ and every $k \geq 1$,

$$
\mathrm{val}^*\bigl( \mathfrak{G}^{k} \bigr) \;\leq\; \exp\Bigl( - \frac{c'\, \varepsilon^{13}\, k}{B + 1} \Bigr)\;.
$$

## Depends on

- [Direct parallel repetition for entangled strategies](thm-direct-repetition-q.md)
- [Normal form verifier in the ambient model](../foundations/part-03/def-normal-verifier.md)

## Proof

Theorem [Direct parallel repetition for entangled strategies](thm-direct-repetition-q.md) at $\varepsilon' = 1 - \mathrm{val}^*(\mathfrak{G}) \geq \varepsilon$: there are at most $3^{B+1}$ strings of length at most $B$, so $\log(\left\vert {{\mathcal{A}}} \right\vert\left\vert {{\mathcal{B}}} \right\vert) \leq 2(B + 1) \log 3$, and $\varepsilon' \leq 1 \leq B + 1$, so the denominator is at most $(B + 1)(1 + 2 \log 3)$; the exponent is monotone in the gap, so the bound at $\varepsilon'$ implies the one at $\varepsilon$. Take $c' = c / (1 + 2 \log 3)$. This is the form in which the soundness clause of Theorem [Parallel repetition of normal form verifiers](../structure-of-the-proof/part-09/thm-parallel-repetition.md) consumes the theorem.

## Lean

Formalized as [`MIPRE.Repetition.repConst`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.repConst), [`MIPRE.Repetition.card_answers_le`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.card_answers_le), [`MIPRE.Repetition.exp_le_soundBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.exp_le_soundBound), [`MIPRE.Repetition.quantumValue_repeat_le_soundBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.quantumValue_repeat_le_soundBound).

## Sources

- [MIP* = RE blueprint: content/05_parallel_repetition.tex, line 275](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/05_parallel_repetition.tex#L275)
