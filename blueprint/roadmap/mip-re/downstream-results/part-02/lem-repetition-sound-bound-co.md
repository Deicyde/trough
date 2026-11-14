---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.repConstCo, MIPRE.Repetition.commutingOperatorValue_repeat_le_soundBound, MIPRE.Repetition.GameSoundIn, MIPRE.Repetition.GameSoundIn.mono, MIPRE.Repetition.gameSoundIn_tensor, MIPRE.Repetition.gameSoundIn_commuting
statement: formalized
proof: formalized
---

# The repetition bound in ${\omega^{\mathrm{co}}}$, for answers of bounded length

There is a universal constant $c'' > 0$ such that for every game $\mathfrak{G}$ on a nonempty question set whose answer alphabets are the strings of length at most $B$, every $\varepsilon > 0$ with ${\omega^{\mathrm{co}}}(\mathfrak{G}) \leq 1 - \varepsilon$ and every $k \geq 1$,

$$
{\omega^{\mathrm{co}}}\bigl( \mathfrak{G}^{k} \bigr) \;\leq\; \exp\Bigl( - \frac{c''\, \varepsilon^{13}\, k}{B + 1} \Bigr)\;.
$$

Say that a value model has the *repetition bound at the constant $c$* if this holds with ${\omega^{\mathrm{co}}}$ replaced by the model and $c''$ by $c$. The model $\mathrm{val}^*$ has it at the constant $c'$ of Lemma [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md), the model ${\omega^{\mathrm{co}}}$ at $c''$, and a model that has it at $c$ has it at every smaller constant.

## Depends on

- [Direct parallel repetition for commuting-operator strategies](../../parallel-repetition/thm-direct-repetition-co.md)
- [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md)
- [Value models](../part-01/def-value-model.md)

## Proof

Theorem [Direct parallel repetition for commuting-operator strategies](../../parallel-repetition/thm-direct-repetition-co.md) at $\varepsilon' = 1 - {\omega^{\mathrm{co}}}(\mathfrak{G}) \geq \varepsilon$, through the arithmetic of Lemma [The repetition bound for answers of bounded length](../../parallel-repetition/lem-repetition-sound-bound.md): its exponent is $\varepsilon'^7$, and $\varepsilon^{13} \leq \varepsilon^7 \leq \varepsilon'^7$ because $\varepsilon \leq \varepsilon' \leq 1$. Take $c'' = c / (1 + 2 \log 3)$ for the constant $c$ of Theorem [Direct parallel repetition for commuting-operator strategies](../../parallel-repetition/thm-direct-repetition-co.md). The bound decreases as the constant grows.

## Lean

Formalized as [`MIPRE.Repetition.repConstCo`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.repConstCo), [`MIPRE.Repetition.commutingOperatorValue_repeat_le_soundBound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.commutingOperatorValue_repeat_le_soundBound), [`MIPRE.Repetition.GameSoundIn`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.GameSoundIn), [`MIPRE.Repetition.GameSoundIn.mono`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.GameSoundIn.mono), [`MIPRE.Repetition.gameSoundIn_tensor`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.gameSoundIn_tensor), [`MIPRE.Repetition.gameSoundIn_commuting`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.gameSoundIn_commuting).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 1369](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L1369)
