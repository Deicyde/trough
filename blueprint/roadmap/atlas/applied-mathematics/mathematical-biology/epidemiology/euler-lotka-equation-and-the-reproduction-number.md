---
declaration: section
origin: cited
lean: MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber, MathlibExt.Biology.Epidemiology.EulerLotka.ConvexOrderLE, MathlibExt.Biology.Epidemiology.EulerLotka.renewal_exp_iff, MathlibExt.Biology.Epidemiology.EulerLotka.renewal_exp_iff_reproductionNumber, MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_pos, MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_dirac, MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_gammaMeasure, MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_expMeasure
statement: formalized
proof: formalized
---

# Euler–Lotka equation and the reproduction number

10 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html).

## Reproductive number from growth rate and generation interval

The **reproductive number** implied by growth rate `r` and generation-interval law `g`:
`R = 1 / M_g(-r)` (Wallinga–Lipsitch 2007, eq. 2.9).

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber`, a definition declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number).

## Convex order

`g₁ ≤cx g₂` if `∫ φ dg₁ ≤ ∫ φ dg₂` for every convex `φ : ℝ → ℝ` that is
integrable under both laws (Shaked–Shanthikumar 2007, §3.A).

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.ConvexOrderLE`, a definition declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 73](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L73). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#convex-order-le).

## Renewal equation for exponential growth

For `c ≠ 0`, the exponential
`b(t) = c e^{r t}` solves `b(t) = R ∫ b(t - a) g(da)` for every `t` iff `R M_g(-r) = 1`.
This is meaningful when `a ↦ e^{-r a}` is `g`-integrable; otherwise Lean's integral and
`M_g(-r)` are both `0` and both sides of the equivalence are false.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.renewal_exp_iff`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 81](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L81). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#renewal-exp-iff).

## Euler–Lotka

Under the hypotheses of `renewal_exp_iff`, exponential growth at rate
`r` solves the renewal equation iff `R = 1 / M_g(-r)`.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.renewal_exp_iff_reproductionNumber`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#renewal-exp-iff-reproduction-number).

## Positivity of the reproductive number

The reproductive number is positive when `M_g(-r)` is finite.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_pos`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 112](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L112). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-pos).

## Fixed generation interval

**Fixed generation interval** `T`: `R = e^{r T}` (for all real `r`, `T`).

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_dirac`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-dirac).

## Gamma generation interval

**Gamma generation interval** with shape `α > 0` and rate `β > 0`: for `r > -β`,
`R = (1 + r / β)^α`.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_gammaMeasure`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 124](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L124). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-gamma-measure).

## Exponential generation interval

**Exponential generation interval** with mean `T > 0` (rate `1 / T`): for `r T > -1`,
`R = 1 + r T` (Wallinga–Lipsitch 2007, eq. 3.1).

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_expMeasure`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-exp-measure).

## More spread lowers `R`

If `g₁ ≤cx g₂` and both have finite `M(-r)`, then
`R(g₂) ≤ R(g₁)` at growth rate `r` (any real `r`). In particular, among generation intervals
with a given mean, the fixed interval maximizes `R`.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_le_of_convexOrderLE`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 146](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L146). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-le-of-convex-order-l).

## Jensen bound

If the generation interval has finite mean `T̄ = ∫ a g(da)` and finite
`M_g(-r)`, then `R ≤ e^{r T̄}` (any real `r`); Wallinga and Lipsitch (2007, §3) note that the
fixed interval gives this upper bound.

Formalized by `MathlibExt.Biology.Epidemiology.EulerLotka.reproductionNumber_le_exp_mean`, a theorem declared in [MathlibExt/Biology/Epidemiology/EulerLotka.lean, line 158](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/EulerLotka.lean#L158). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html#reproduction-number-le-exp-mean).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Euler–Lotka equation and the reproduction number](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/epidemiology/euler-lotka-equation-and-the-reproduction-number)
