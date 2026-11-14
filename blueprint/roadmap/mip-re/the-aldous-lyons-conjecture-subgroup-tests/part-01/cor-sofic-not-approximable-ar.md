---
declaration: corollary
origin: cited
lean: MIPRE.Tailored.Sofic.not_sofValueApproximable, MIPRE.Tailored.not_sofValueApproximable_of_answerReduction
statement: formalized
proof: formalized
---

# The sofic value is not approximable, from tailored answer reduction

A halting reduction to tailored games makes the sofic value of subgroup tests not approximable; in particular a tailored answer reduction at input level $5$ does.

## Depends on

- [Main Theorem II; Theorem I:2126](thm-main-theorem-ii.md)
- [The sofic value is not approximable; Corollary I:2144, measure-free](thm-sofic-not-approximable.md)
- [$\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction](../../the-aldous-lyons-track-tmip-re/part-05/cor-tmip-re-from-ar.md)

## Proof

Theorem [The sofic value is not approximable; Corollary I:2144, measure-free](thm-sofic-not-approximable.md) with Theorem [Main Theorem II; Theorem I:2126](thm-main-theorem-ii.md), and Corollary [$\mathrm{TMIP}^* = \mathrm{RE}$ from tailored answer reduction](../../the-aldous-lyons-track-tmip-re/part-05/cor-tmip-re-from-ar.md) for the halting reduction.

## Lean

Formalized as [`MIPRE.Tailored.Sofic.not_sofValueApproximable`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.Sofic.not_sofValueApproximable), [`MIPRE.Tailored.not_sofValueApproximable_of_answerReduction`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.not_sofValueApproximable_of_answerReduction).

## Sources

- [MIP* = RE blueprint: content/10_subgroup_tests.tex, line 362](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/10_subgroup_tests.tex#L362)
