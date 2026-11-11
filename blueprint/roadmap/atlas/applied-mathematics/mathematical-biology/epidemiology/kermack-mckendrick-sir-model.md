---
declaration: section
origin: cited
lean: MathlibExt.Biology.Epidemiology.SIR.IsSolution, MathlibExt.Biology.Epidemiology.SIR.IsSolution.total_eq, MathlibExt.Biology.Epidemiology.SIR.IsSolution.deriv_infected_pos_iff, MathlibExt.Biology.Epidemiology.SIR.IsSolution.susceptible_mul_exp_eq, MathlibExt.Biology.Epidemiology.SIR.IsSolution.final_size, MathlibExt.Biology.Epidemiology.SIR.IsSolution.final_size_eq
statement: formalized
proof: formalized
---

# Kermack–McKendrick SIR model

6 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html).

## SIR

## Solution of the Kermack–McKendrick SIR system

`(S, I, R)` solves the Kermack–McKendrick SIR system with transmission rate `β`, removal
rate `γ` and population size `N` for all times `t ≥ 0`:
`S' = -β S I / N`, `I' = β S I / N - γ I`, `R' = γ I`.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution`, a structure declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#is-solution).

## Conservation of the population

Along a solution, `S + I + R` is constant on
`[0, ∞)`.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution.total_eq`, a theorem declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 86](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L86). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#total-eq).

## Threshold theorem (Kermack–McKendrick 1927)

If initially `I(0) > 0`, with `γ > 0` and
`N > 0`, the number of infectives initially increases, `I'(0) > 0`, iff
`R₀ S(0) / N > 1` with `R₀ = β / γ`.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution.deriv_infected_pos_iff`, a theorem declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 96](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L96). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#deriv-infected-pos-iff).

## Conserved quantity behind the final-size relation

For `γ ≠ 0`, the quantity
`S(t) e^{R₀ R(t) / N}` (`R₀ = β / γ`) is constant along a solution on `[0, ∞)`.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution.susceptible_mul_exp_eq`, a theorem declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 105](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L105). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#susceptible-mul-exp-eq).

## Final-size relation (Kermack–McKendrick 1927)

If along a solution (`γ ≠ 0`)
`S(t) → S∞` and `R(t) → R∞` as `t → ∞`, then `S∞ = S(0) e^{-R₀ (R∞ - R(0)) / N}` with
`R₀ = β / γ`. See `final_size_eq` for the classical form.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution.final_size`, a theorem declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 117](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L117). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#final-size).

## Final-size equation (Kermack–McKendrick 1927)

If the population is `N = S + I + R`,
nobody is removed initially (`R(0) = 0`), `γ ≠ 0`, `S(t) → S∞` and the epidemic dies out
(`I(t) → 0`), then `S∞ = S(0) e^{-R₀ (N - S∞) / N}` with `R₀ = β / γ`.

Formalized by `MathlibExt.Biology.Epidemiology.SIR.IsSolution.final_size_eq`, a theorem declared in [MathlibExt/Biology/Epidemiology/SIR.lean, line 135](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Epidemiology/SIR.lean#L135). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html#final-size-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Kermack–McKendrick SIR model](https://deicyde.github.io/atlas-lean/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/epidemiology/kermack-mckendrick-sir-model)
