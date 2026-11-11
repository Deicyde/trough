---
declaration: section
origin: cited
lean: MathlibExt.Biology.Dynamics.GoldbeterKoshland.rateRatio, MathlibExt.Biology.Dynamics.GoldbeterKoshland.goldbeterKoshland, MathlibExt.Biology.Dynamics.GoldbeterKoshland.responseCoefficient, MathlibExt.Biology.Dynamics.GoldbeterKoshland.hill, MathlibExt.Biology.Dynamics.GoldbeterKoshland.steadyState_iff, MathlibExt.Biology.Dynamics.GoldbeterKoshland.strictMonoOn_rateRatio, MathlibExt.Biology.Dynamics.GoldbeterKoshland.goldbeterKoshland_mem_Ioo, MathlibExt.Biology.Dynamics.GoldbeterKoshland.rateRatio_goldbeterKoshland
statement: formalized
proof: formalized
---

# Goldbeter–Koshland ultrasensitivity

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html).

## Rate ratio at a given steady-state modified fraction

The value of `V₁ / V₂` for which the mole fraction `W` of modified protein is at steady
state (Goldbeter–Koshland 1981, Eq. 8): `W (1 - W + K₁) / ((1 - W) (W + K₂))`. Meaningful for
`0 < W < 1` and `K₁, K₂ > 0`; at `W = 1` Lean's `a / 0 = 0` gives the junk value `0`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.rateRatio`, a definition declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#rate-ratio).

## Goldbeter–Koshland function

The **Goldbeter–Koshland function**: the steady-state mole fraction of modified protein
when `V₁ / V₂ = v` (Goldbeter–Koshland 1981, Eq. 7, rationalized so that it also covers
`v = 1`, Eq. 9). Meaningful for `v, K₁, K₂ > 0`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.goldbeterKoshland`, a definition declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 85](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L85). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#goldbeter-koshland).

## Response coefficient of a covalent modification cycle

The **response coefficient** `R_v`: the ratio of the values of `V₁ / V₂` giving 90% and 10%
modified protein at steady state (Goldbeter–Koshland 1981).

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.responseCoefficient`, a definition declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 90](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L90). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#response-coefficient).

## Hill response function

The fraction of a Hill response `Sⁿ / (Kⁿ + Sⁿ)` with half-saturation constant `K` and
Hill coefficient `n` (meaningful for `S, K > 0`, `n > 0`).

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.hill`, a definition declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 95](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L95). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#hill).

## Steady state of the modification cycle

**Steady state of the modification cycle** (Goldbeter–Koshland 1981, Eq. 8). For
`V₂ > 0`, `K₁, K₂ > 0` and `0 < W < 1`, modification and demodification balance,
`V₁ (1 - W) / (K₁ + 1 - W) = V₂ W / (K₂ + W)`, iff `V₁ / V₂ = rateRatio K₁ K₂ W`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.steadyState_iff`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 101](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L101). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#steady-state-iff).

## Rate ratio is strictly increasing in the modified fraction

`rateRatio K₁ K₂` is strictly increasing on `(0, 1)` for `K₁, K₂ > 0`: it is the product
of the positive increasing functions `W / (W + K₂)` and `1 + K₁ / (1 - W)`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.strictMonoOn_rateRatio`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 113](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L113). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#strict-mono-on-rate-ratio).

## Goldbeter–Koshland function lies strictly between 0 and 1

For `v, K₁, K₂ > 0` the Goldbeter–Koshland function lies in `(0, 1)`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.goldbeterKoshland_mem_Ioo`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 166](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L166). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#goldbeter-koshland-mem-ioo).

## The Goldbeter–Koshland function is a steady state

**The Goldbeter–Koshland function is a steady state** (Goldbeter–Koshland 1981, Eq. 7):
for `v, K₁, K₂ > 0`, `rateRatio K₁ K₂ (goldbeterKoshland v K₁ K₂) = v`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.rateRatio_goldbeterKoshland`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 180](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L180). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#rate-ratio-goldbeter-koshland).

## Uniqueness of the steady state

**Uniqueness of the steady state** (Goldbeter–Koshland 1981, Eq. 7). For `K₁, K₂ > 0`, if
`0 < W < 1` and `rateRatio K₁ K₂ W = v` with `v > 0`, then `W` is the Goldbeter–Koshland
function.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.eq_goldbeterKoshland`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 214](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L214). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#eq-goldbeter-koshland).

## Equal maximal rates

**Equal maximal rates** (Goldbeter–Koshland 1981, Eq. 9): for `V₁ = V₂` and `K₁, K₂ > 0`
the steady-state modified fraction is `K₂ / (K₁ + K₂)`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.goldbeterKoshland_one`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#goldbeter-koshland-one).

## The response coefficient

**The response coefficient** (Goldbeter–Koshland 1981, Eq. 10): for `K₁, K₂ > -0.1`,
`R_v = 81 (K₁ + 0.1)(K₂ + 0.1) / ((K₁ + 0.9)(K₂ + 0.9))`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.responseCoefficient_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 234](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L234). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#response-coefficient-eq).

## Response coefficient exceeds 1

For `K₁, K₂ > 0` the response coefficient exceeds `1`: the switch is never infinitely
sharp.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.one_lt_responseCoefficient`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 254](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L254). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#one-lt-response-coefficient).

## Response coefficient is below the Michaelis–Menten value 81

For `K₁, K₂ > 0` the response coefficient is below the Michaelis–Menten value `81`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.responseCoefficient_lt_81`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 260](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L260). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#response-coefficient-lt-81).

## First-order limit

As both `K₁, K₂ → ∞` the response coefficient tends to `81`, the
value of a Michaelis–Menten response.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.tendsto_responseCoefficient_atTop`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 267](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L267). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#tendsto-response-coefficient-at-top).

## Zero-order ultrasensitivity

As both `K₁, K₂ → 0` the response coefficient tends to
`1`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.tendsto_responseCoefficient_zero`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 288](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L288). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#tendsto-response-coefficient-zero).

## Hill response coefficient

**Hill response coefficient** (Goldbeter–Koshland 1981, Eq. 11). For a Hill response with
`n > 0` and `K > 0`, if `S₉, S₁ > 0` give 90% and 10% response, then
`S₉ / S₁ = 81 ^ (1 / n)`.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.hill_ratio_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 308](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L308). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#hill-ratio-eq).

## Michaelis–Menten response

**Michaelis–Menten response** (`n = 1`): going from 10% to 90% of the response takes an
81-fold increase of the stimulus.

Formalized by `MathlibExt.Biology.Dynamics.GoldbeterKoshland.michaelisMenten_ratio_eq`, a theorem declared in [MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean, line 322](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/Biology/Dynamics/GoldbeterKoshland.lean#L322). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html#michaelis-menten-ratio-eq).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Goldbeter–Koshland ultrasensitivity](https://deicyde.github.io/atlas-lean/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/Biology/systems-biology/goldbeter-koshland-ultrasensitivity)
