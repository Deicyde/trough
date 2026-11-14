---
declaration: lemma
origin: cited
lean: HaltingGameValue.SynchronousGame.toMIPRE, HaltingGameValue.SynchronousGame.toSyncStrategy, HaltingGameValue.SynchronousGame.ofSyncStrategy, HaltingGameValue.SynchronousGame.value_toSyncStrategy, HaltingGameValue.SynchronousGame.strategyValue_ofSyncStrategy, HaltingGameValue.SynchronousGame.gameValue_eq_syncValue, HaltingGameValue.SynchronousGame.gameValue_le_quantumValue, TailoredGameValue.TailoredGameData.syncGame, TailoredGameValue.TailoredGameData.game, TailoredGameValue.TailoredGameData.gameValue_le_quantumValue, TailoredGameValue.PermStrategy.isPVMIn_proj, TailoredGameValue.PermStrategy.toSync, TailoredGameValue.PermStrategy.value_toSync, TailoredGameValue.TailoredGameData.HasPerfectZPC.syncValue_eq_one, TailoredGameValue.TailoredGameData.HasPerfectZPC.gameValue_eq_one, TailoredGameValue.TailoredGameData.HasPerfectZPC.quantumValue_eq_one
statement: formalized
proof: formalized
---

# Tailored game descriptions as games of the foundations

The synchronous game of a tailored game description is a synchronous game of the foundations, with the same synchronous value, which is at most its quantum value. A ZPC strategy of a description is a synchronous strategy with the same value, its measurements being the Fourier transforms of its observables. So a perfect ZPC strategy gives synchronous and quantum value $1$.

## Depends on

- [Tailored game descriptions, standalone; II:1243, II:1279](../part-01/def-tailored-game-data.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Synchronous value lower-bounds the quantum value](../../foundations/part-01/lem-sync-le-valstar.md)
- [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)

## Proof depends on

- [Signed permutations; II:1008–1069](../part-01/def-signed-perm.md)
- [Signed permutation matrices](../part-01/lem-signed-perm.md)

## Proof

The two notions of a synchronous strategy are the same data, and so are their values. The Fourier transform of commuting self-adjoint involutions is a projective measurement (Lemma [The Fourier transform; II:974–1006](../part-01/lem-fourier-pvm.md)), and the observables of a ZPC strategy are involutive signed permutation matrices, which are self-adjoint.

## Lean

Formalized as [`HaltingGameValue.SynchronousGame.toMIPRE`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.toMIPRE), [`HaltingGameValue.SynchronousGame.toSyncStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.toSyncStrategy), [`HaltingGameValue.SynchronousGame.ofSyncStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.ofSyncStrategy), [`HaltingGameValue.SynchronousGame.value_toSyncStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.value_toSyncStrategy), [`HaltingGameValue.SynchronousGame.strategyValue_ofSyncStrategy`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.strategyValue_ofSyncStrategy), [`HaltingGameValue.SynchronousGame.gameValue_eq_syncValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.gameValue_eq_syncValue), [`HaltingGameValue.SynchronousGame.gameValue_le_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/HaltingGameValue.SynchronousGame.gameValue_le_quantumValue), [`TailoredGameValue.TailoredGameData.syncGame`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.syncGame), [`TailoredGameValue.TailoredGameData.game`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.game), [`TailoredGameValue.TailoredGameData.gameValue_le_quantumValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.gameValue_le_quantumValue), [`TailoredGameValue.PermStrategy.isPVMIn_proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.PermStrategy.isPVMIn_proj), [`TailoredGameValue.PermStrategy.toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.PermStrategy.toSync), [`TailoredGameValue.PermStrategy.value_toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.PermStrategy.value_toSync), [`TailoredGameValue.TailoredGameData.HasPerfectZPC.syncValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.HasPerfectZPC.syncValue_eq_one), [`TailoredGameValue.TailoredGameData.HasPerfectZPC.gameValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.HasPerfectZPC.gameValue_eq_one), [`TailoredGameValue.TailoredGameData.HasPerfectZPC.quantumValue_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.TailoredGameData.HasPerfectZPC.quantumValue_eq_one).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 699](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L699)
