---
declaration: section
origin: cited
lean: IsAdicComplete.of_module_finite_free_span_natCast, IsLocalRing.two_le_ringKrullDim_adicCompletion_of_two_le, IsLocalRing.isAdicComplete_of_module_finite, IsAdicComplete.of_isNilpotent, AdicCompletion.isNoetherianRing_of_isNoetherianRing, MvPowerSeries.isAdicComplete_maximalIdeal
statement: formalized
proof: formalized
---

# Adic completion: its own results

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html).

## Finite free modules over adically complete rings are complete

If `𝓞` is adically complete at `(p)` and `R` is finite free over `𝓞`,
then `R` is adically complete at `(p)`.

Formalized by `IsAdicComplete.of_module_finite_free_span_natCast`, a theorem declared in [MathlibExt/RingTheory/AdicCompletion/FiniteFree.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/AdicCompletion/FiniteFree.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#of-module-finite-free-span-nat-cast).

## Adic completion preserves Krull dimension at least two

A Noetherian local ring of Krull dimension at least two has an adic
completion of Krull dimension at least two.

Formalized by `IsLocalRing.two_le_ringKrullDim_adicCompletion_of_two_le`, a theorem declared in [MathlibExt/RingTheory/AdicCompletion/KrullDimension.lean, line 48](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/AdicCompletion/KrullDimension.lean#L48). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#two-le-ring-krull-dim-adic-completion-of).

## Finite local extensions of adically complete rings are complete

A finite local extension of an adically complete local ring is adically
complete at its maximal ideal.

Formalized by `IsLocalRing.isAdicComplete_of_module_finite`, a theorem declared in [MathlibExt/RingTheory/AdicCompletion/ModuleFinite.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/AdicCompletion/ModuleFinite.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#is-adic-complete-of-module-finite).

## Adic completeness at a nilpotent ideal

A ring is adically complete at a nilpotent ideal.

Formalized by `IsAdicComplete.of_isNilpotent`, a theorem declared in [MathlibExt/RingTheory/AdicCompletion/Nilpotent.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/AdicCompletion/Nilpotent.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#of-is-nilpotent).

## Adic completion of a Noetherian ring is Noetherian

The adic completion of a Noetherian ring is Noetherian.

Formalized by `AdicCompletion.isNoetherianRing_of_isNoetherianRing`, a theorem declared in [MathlibExt/RingTheory/AdicCompletion/Noetherian.lean, line 169](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/AdicCompletion/Noetherian.lean#L169). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#is-noetherian-ring-of-is-noetherian-ring).

## Adic completeness of multivariate power series

If `R` is adically complete at its maximal ideal, then `MvPowerSeries σ R`
is adically complete at its maximal ideal.

Formalized by `MvPowerSeries.isAdicComplete_maximalIdeal`, a theorem declared in [MathlibExt/RingTheory/MvPowerSeries/AdicComplete.lean, line 286](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/MvPowerSeries/AdicComplete.lean#L286). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html#is-adic-complete-maximal-ideal).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Adic completion](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/local-rings/adic-completion/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/local-rings/adic-completion)
