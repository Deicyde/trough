---
declaration: lemma
origin: cited
lean: TailoredGameValue.TailoredGameData.toGameData, TailoredGameValue.TailoredGameData.vecEquiv, TailoredGameValue.TailoredGameData.ansLenL, TailoredGameValue.TailoredGameData.acceptsN, TailoredGameValue.TailoredGameData.accN, TailoredGameValue.TailoredGameData.acceptsN_iff, TailoredGameValue.TailoredGameData.mem_accN, TailoredGameValue.TailoredGameData.quantumValue_toGameData, TailoredGameValue.TailoredGameData.primrec_toGameData
statement: formalized
proof: formalized
---

# A tailored game description as a game description

There is a primitive recursive map from tailored game descriptions to game descriptions (Definition [Game description](../../foundations/part-02/def-game-description.md)) that keeps the quantum value: the answers are the numbers below $2^\Lambda$, read as bit vectors of length $\Lambda$, and the acceptance table lists the tuples the canonical decider accepts.

## Depends on

- [Tailored game descriptions as games of the foundations](lem-tailored-bridge.md)
- [Game description](../../foundations/part-02/def-game-description.md)

## Proof

The two games have the same questions and the same distribution, and their answer sets are in bijection along the binary expansion, under which the two predicates agree; the quantum value is invariant under such relabelings.

## Lean

Formalized as [`TailoredGameValue.TailoredGameData.toGameData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.toGameData), [`TailoredGameValue.TailoredGameData.vecEquiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.vecEquiv), [`TailoredGameValue.TailoredGameData.ansLenL`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.ansLenL), [`TailoredGameValue.TailoredGameData.acceptsN`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.acceptsN), [`TailoredGameValue.TailoredGameData.accN`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.accN), [`TailoredGameValue.TailoredGameData.acceptsN_iff`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.acceptsN_iff), [`TailoredGameValue.TailoredGameData.mem_accN`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.mem_accN), [`TailoredGameValue.TailoredGameData.quantumValue_toGameData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.quantumValue_toGameData), [`TailoredGameValue.TailoredGameData.primrec_toGameData`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.primrec_toGameData).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 732](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L732)
