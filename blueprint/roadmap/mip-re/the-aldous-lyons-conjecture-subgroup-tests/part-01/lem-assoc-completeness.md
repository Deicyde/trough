---
declaration: lemma
origin: cited
lean: MIPRE.Tailored.Sofic.liftHom, MIPRE.Tailored.Sofic.ZStrat.toAction, MIPRE.Tailored.Sofic.ZStrat.checks_toAction, MIPRE.Tailored.Sofic.ZStrat.consMat_apply_self_eq_one, MIPRE.Tailored.Sofic.exists_value_one_of_hasPerfectZPC
statement: formalized
proof: formalized
---

# Completeness: lifting a perfect strategy; Theorem I:2126 (1)

A perfect ZPC strategy of a tailored game lifts to an action of value $1$ against the associated test: on twice the points, $J$ swapping the copies and each variable acting by its signed permutation.

## Depends on

- [The trace identity](lem-trace-identity.md)
- [Passing a challenge under Checks 1–3](lem-assoc-passes.md)
- [Tailored game descriptions, standalone; II:1243, II:1279](../../the-aldous-lyons-track-tmip-re/part-01/def-tailored-game-data.md)
- [The quotient by $J$](lem-j-quotient.md)
- [Signed permutations; II:1008–1069](../../the-aldous-lyons-track-tmip-re/part-01/def-signed-perm.md)
- [Signed permutation matrices](../../the-aldous-lyons-track-tmip-re/part-01/lem-signed-perm.md)
- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](../../the-aldous-lyons-track-tmip-re/part-01/def-fourier-forms.md)
- [The Fourier transform; II:974–1006](../../the-aldous-lyons-track-tmip-re/part-01/lem-fourier-pvm.md)

## Proof

Checks 1–3 hold at every point. By the trace identity at value $1$, every constraint word of a pair of positive weight fixes the points of its readable value, so every point passes every challenge of positive weight. Commutation along edges is not used.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.liftHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.liftHom), [`MIPRE.Tailored.Sofic.ZStrat.toAction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.toAction), [`MIPRE.Tailored.Sofic.ZStrat.checks_toAction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.checks_toAction), [`MIPRE.Tailored.Sofic.ZStrat.consMat_apply_self_eq_one`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.ZStrat.consMat_apply_self_eq_one), [`MIPRE.Tailored.Sofic.exists_value_one_of_hasPerfectZPC`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.exists_value_one_of_hasPerfectZPC).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 319](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L319)
