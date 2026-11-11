---
declaration: section
origin: cited
lean: PowerSeries.isDiscreteValuationRing_quotient_span_X_sub_C_pow_of_irreducible, PowerSeries.quotient_span_X_sub_C_pow_of_irreducible, PowerSeries.isAdicComplete_quotient_span_X_sub_C_of_irreducible
statement: formalized
proof: formalized
---

# Discrete valuation rings as power series quotients

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien/index.html).

## Power series over a DVR modulo $X - \varpi^e$ form a DVR

Modulo `X - ϖ ^ e`, a power series ring over a discrete valuation ring is a
discrete valuation ring, with uniformizer the image of `ϖ`.

Formalized by `PowerSeries.isDiscreteValuationRing_quotient_span_X_sub_C_pow_of_irreducible`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien/index.html#is-discrete-valuation-ring-quotient-span).

## Power series over a DVR modulo $X - \varpi^e$ form a local PID

Modulo `X - ϖ ^ e`, a power series ring over a discrete valuation ring
is a principal ideal ring and a local ring, and the image of `ϖ` is
irreducible.

Formalized by `PowerSeries.quotient_span_X_sub_C_pow_of_irreducible`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean, line 249](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean#L249). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien/index.html#quotient-span-x-sub-c-pow-of-irreducible).

## Power series over a DVR modulo $X - \varpi$ form a complete DVR

Modulo `X - ϖ`, a power series ring over a discrete valuation ring is a
discrete valuation ring, adically complete at its maximal ideal, with
uniformizer the image of `ϖ`.

Formalized by `PowerSeries.isAdicComplete_quotient_span_X_sub_C_of_irreducible`, a theorem declared in [MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean, line 272](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/RingTheory/PowerSeries/DVRQuotient.lean#L272). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien/index.html#is-adic-complete-quotient-span-x-sub-c-o).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Discrete valuation rings as power series quotients](https://deicyde.github.io/atlas-lean/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/RingTheory/valuation-rings/discrete-valuation-rings-as-power-series-quotien)
