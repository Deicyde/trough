---
declaration: section
origin: cited
lean: MathlibExt.Analysis.Series.Tauberian.tauber_tendsto_partial_sums, MathlibExt.Analysis.Series.Tauberian.hardy_littlewood_tendsto_partial_sums
statement: formalized
proof: formalized
---

# Tauberian theorems for power series

2 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/tauberian-theorems-for-power-series/index.html).

## Tauber's theorem

**Tauber's theorem** (1897). If the power series `∑ aₙ rⁿ` converges (in the
Abel sense) to `A` as `r → 1⁻` and `n * aₙ → 0`, then the partial sums of `a`
converge to `A`.

Formalized by `MathlibExt.Analysis.Series.Tauberian.tauber_tendsto_partial_sums`, a theorem declared in [MathlibExt/Analysis/Series/Tauberian.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/Tauberian.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/tauberian-theorems-for-power-series/index.html#tauber-tendsto-partial-sums).

## Hardy–Littlewood Tauberian theorem

**Hardy–Littlewood Tauberian theorem** (1914). If `aₙ ≥ 0` and the power series
`∑ aₙ rⁿ` converges for every `r ∈ (0, 1)` with Abel limit `A` as `r → 1⁻`, then
the partial sums of `a` converge to `A`.

Formalized by `MathlibExt.Analysis.Series.Tauberian.hardy_littlewood_tendsto_partial_sums`, a theorem declared in [MathlibExt/Analysis/Series/Tauberian.lean, line 317](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Analysis/Series/Tauberian.lean#L317). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/tauberian-theorems-for-power-series/index.html#hardy-littlewood-tendsto-partial-sums).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Tauberian theorems for power series](https://deicyde.github.io/atlas-lean/roadmap/Analysis/sequences-and-series/summability/tauberian-theorems-for-power-series/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Analysis/sequences-and-series/summability/tauberian-theorems-for-power-series)
