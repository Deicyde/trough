---
declaration: definition
origin: cited
lean: MIPRE.Tailored.Sofic.ZStrat, MIPRE.Tailored.Sofic.ZStrat.proj, MIPRE.Tailored.Sofic.ZStrat.value, MIPRE.Tailored.Sofic.ZStrat.toSync, MIPRE.Tailored.Sofic.ZStrat.value_toSync, MIPRE.Tailored.Sofic.ZStrat.value_le_gameValue, MIPRE.Tailored.Sofic.ZStrat.rej, MIPRE.Tailored.Sofic.ZStrat.value_eq_sum_rej, TailoredGameValue.PermStrategy.toZStrat, TailoredGameValue.PermStrategy.value_toZStrat
statement: formalized
---

# Z-aligned signed-permutation strategies without commutation along edges

A permutation strategy for a tailored game (signed permutation observables, involutions commuting at each vertex, diagonal at the readable variables, the identity beyond each vertex's length) need not commute along edges; its Fourier-transform measurements still form a synchronous strategy, with the same value, so its value is at most the game's synchronous value.

## Depends on

- [Tailored game descriptions, standalone; II:1243, II:1279](../../the-aldous-lyons-track-tmip-re/part-01/def-tailored-game-data.md)
- [Synchronous strategy](../../foundations/part-01/def-sync-strategy.md)
- [Synchronous value](../../foundations/part-01/def-sync-value.md)
- [Signed permutations; II:1008–1069](../../the-aldous-lyons-track-tmip-re/part-01/def-signed-perm.md)
- [Signed permutation matrices](../../the-aldous-lyons-track-tmip-re/part-01/lem-signed-perm.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](../../the-aldous-lyons-track-tmip-re/part-01/def-fourier-forms.md)
- [The Fourier transform; II:974–1006](../../the-aldous-lyons-track-tmip-re/part-01/lem-fourier-pvm.md)
- [Tailored game descriptions as games of the foundations](../../the-aldous-lyons-track-tmip-re/part-02/lem-tailored-bridge.md)

## Lean

Formalized as [`MIPRE.Tailored.Sofic.ZStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat), [`MIPRE.Tailored.Sofic.ZStrat.proj`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.proj), [`MIPRE.Tailored.Sofic.ZStrat.value`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.value), [`MIPRE.Tailored.Sofic.ZStrat.toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.toSync), [`MIPRE.Tailored.Sofic.ZStrat.value_toSync`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.value_toSync), [`MIPRE.Tailored.Sofic.ZStrat.value_le_gameValue`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.value_le_gameValue), [`MIPRE.Tailored.Sofic.ZStrat.rej`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.rej), [`MIPRE.Tailored.Sofic.ZStrat.value_eq_sum_rej`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.value_eq_sum_rej), [`TailoredGameValue.PermStrategy.toZStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.PermStrategy.toZStrat), [`TailoredGameValue.PermStrategy.value_toZStrat`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/TailoredGameValue.PermStrategy.value_toZStrat).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 227](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L227)
