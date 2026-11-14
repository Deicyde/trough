---
declaration: lemma
origin: cited
lean: MIPRE.SeededGame.tensorSound, MIPRE.SeededGame.tensorSound_value_ge, MIPRE.SeededGame.quantumValue_ge_of_oracular
statement: formalized
proof: formalized
---

# Soundness of oracularization, for bipartite strategies

Let $S$ be a seeded game with nonempty seed space and nonempty answer alphabet, let $0 \leq \varepsilon \leq 1$, and let $N$ be a tensor-product strategy for the oracularization of $S$ with value at least $1 - \varepsilon$. Let $\Sigma(N)$ be the strategy for the game of $S$, on the same state, in which Alice measures the first player's $\{N^{(\textsc{A},\, x)}_a\}$ and Bob the second player's $\{N^{(\textsc{B},\, y)}_b\}$, each relabelled so that the oracle-shaped answers are grouped into one fixed answer. Then $\Sigma(N)$ has value at least $1 - 24\sqrt{\varepsilon}$. Consequently, for every $\varepsilon > 0$, if $\mathrm{val}^*$ of the oracularization of $S$ exceeds $1 - \varepsilon$, then $\mathrm{val}^*$ of the game of $S$ is at least $1 - 24\sqrt{\varepsilon}$.

## Depends on

- [The oracularized game](def-oracular-game.md)
- [Tensor-product strategy](../../foundations/part-01/def-tensor-strategy.md)
- [Quantum value](../../foundations/part-01/def-q-value.md)
- [Soundness of oracularization, in a bipartite model](../../downstream-results/part-02/lem-oracular-soundness-model.md)

## Proof

A tensor-product strategy is projective, so no dilation is needed, and its measurements are projective measurements in the two factors of its tensor-product model (Definition [Bipartite model](../../downstream-results/part-02/def-bipartite-model.md)). The first statement is Lemma [Soundness of oracularization, in a bipartite model](../../downstream-results/part-02/lem-oracular-soundness-model.md) in that model: $\Sigma(N)$ is the strategy whose measurements are the extracted families, on the same state, and its value is their model value. The argument there is the matrix one, written once for a bipartite model: the chain of three cross-party deviations behind projective front factors, each bounded by one role pair's conditional failure, the oracle's joint marginal carrying its acceptance, the single square root of the measurement form of Lemma [Close measurements have close values](../../foundations/part-02/lem-close-measurements-close-values.md), and the average over the seed of the four role pairs used, which gives $\mathrm{val}^* \geq 1 - 9\varepsilon - 2\sqrt{54\varepsilon} \geq 1 - 24\sqrt\varepsilon$. The paper's chain `eq:oracle-1` to `eq:oracle-3` is not needed: the oracle's measurement enters only through its joint marginal, so there is no marginalization step inside a pair-indexed family, and the second player's two isolated measurements are multiplied in one order only, so there is no commutation step. For the second statement, when $\varepsilon \leq 1$ a strategy of value above $1 - \varepsilon$ exists and the first applies; when $\varepsilon > 1$ the bound is negative.

## Lean

Formalized as [`MIPRE.SeededGame.tensorSound`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.tensorSound), [`MIPRE.SeededGame.tensorSound_value_ge`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.tensorSound_value_ge), [`MIPRE.SeededGame.quantumValue_ge_of_oracular`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.SeededGame.quantumValue_ge_of_oracular).

## Sources

- [MIP* = RE blueprint: content/06_proof_structure.tex, line 4296](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/06_proof_structure.tex#L4296)
