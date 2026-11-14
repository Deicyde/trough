---
declaration: module
origin: cited
lean: BlackBody.quantizedOscillator, BlackBody.exp_neg_lt_one, BlackBody.exp_neg_mul_nat, BlackBody.hasSum_exp_neg_levels, BlackBody.hasSum_energy_levels, BlackBody.quantizedOscillator_meanEnergy, BlackBody.classicalOscillator, BlackBody.classicalOscillator_meanEnergy
statement: formalized
proof: formalized
---

# Planck's law lies strictly below the Rayleigh–Jeans law

The module `PhyslibAlpha.QuantumMechanics.Blackbody.RayleighJeans`, [PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean): 13 declarations, 13 with a docstring.

## i. Overview

> A field mode of frequency `ν` in thermal equilibrium at temperature `T` is an oscillator.
> Treated as a canonical ensemble with continuous energies `E ≥ 0`, its mean energy is `kB T`
> (equipartition) and the spectral radiance is the Rayleigh–Jeans law `2 ν² kB T / c²`.
> Treated as a canonical ensemble with quantized energies `n h ν`, its mean energy is
> `h ν / (e^{h ν / (kB T)} - 1)` and the spectral radiance is Planck's law. Since `e^x - 1 > x`
> for `x > 0`, the quantized mean energy is strictly below `kB T` at every frequency and every
> positive temperature: no continuous Boltzmann statistics reproduces Planck's law. This is the
> starting point of Poincaré's 1911–1912 proof that the quantum is necessary.

## ii. Key results

> - `quantizedOscillator` : the canonical ensemble of levels `n ε`, `n : ℕ`.
> - `quantizedOscillator_meanEnergy` : its mean energy is `ε / (e^{β ε} - 1)`.
> - `classicalOscillator` : the canonical ensemble of energies `E > 0` with Lebesgue measure.
> - `classicalOscillator_meanEnergy` : its mean energy is `kB T`.
> - `quantizedOscillator_meanEnergy_lt` : the quantized mean energy is below `kB T`.
> - `spectralRadiance_eq_meanEnergy` : Planck's law is `2 ν² / c²` times the quantized mean energy.
> - `rayleighJeans` : the Rayleigh–Jeans spectral radiance `2 ν² kB T / c²`.
> - `spectralRadiance_lt_rayleighJeans` : Planck's law is strictly below Rayleigh–Jeans.

## iv. References

> * H. Poincaré, *Sur la théorie des quanta*, J. Phys. Théor. Appl. 2 (1912) 5–34.
> * https://en.wikipedia.org/wiki/Rayleigh%E2%80%93Jeans\_law

## A. The quantized oscillator

**`BlackBody.quantizedOscillator`**, a def, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L64).

> The quantized oscillator with level spacing `ε`: the microstates `n : ℕ` have energy `n ε`
> and are counted with unit weight.

```lean
noncomputable def quantizedOscillator (ε : ℝ) : CanonicalEnsemble ℕ
```

**`BlackBody.exp_neg_lt_one`**, a lemma, [line 71](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L71).

> For `x > 0`, the Boltzmann factor `e^{-x}` has norm below one.

```lean
lemma exp_neg_lt_one {x : ℝ} (hx : 0 < x) : ‖exp (-x)‖ < 1
```

**`BlackBody.exp_neg_mul_nat`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L76).

> The Boltzmann factor of the level `n` is the `n`-th power of that of the first level.

```lean
lemma exp_neg_mul_nat (b ε : ℝ) (n : ℕ) : exp (-b * (n * ε)) = exp (-(b * ε)) ^ n
```

**`BlackBody.hasSum_exp_neg_levels`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L81).

> The partition sum of the levels: `∑ e^{-β n ε} = (1 - e^{-β ε})⁻¹`.

```lean
lemma hasSum_exp_neg_levels {b ε : ℝ} (hb : 0 < b * ε) :
    HasSum (fun n : ℕ => exp (-b * (n * ε))) (1 - exp (-(b * ε)))⁻¹
```

**`BlackBody.hasSum_energy_levels`**, a lemma, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L86).

> The energy sum of the levels: `∑ n ε e^{-β n ε} = ε e^{-β ε} / (1 - e^{-β ε})²`.

```lean
lemma hasSum_energy_levels {b ε : ℝ} (hb : 0 < b * ε) :
    HasSum (fun n : ℕ => n * ε * exp (-b * (n * ε)))
      (ε * (exp (-(b * ε)) / (1 - exp (-(b * ε))) ^ 2))
```

**`BlackBody.quantizedOscillator_meanEnergy`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L94).

> The mean energy of the quantized oscillator is Planck's `ε / (e^{β ε} - 1)`.

```lean
lemma quantizedOscillator_meanEnergy (kB : BoltzmannConstant) {ε : ℝ} (hε : 0 < ε) {T : Temperature}
    (hT : 0 < (T : ℝ)) :
    (quantizedOscillator ε).meanEnergy kB T = ε / (exp (T.β kB * ε) - 1)
```

## B. The classical oscillator

**`BlackBody.classicalOscillator`**, a def, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L125).

> The classical oscillator: energies `E > 0` with Lebesgue measure.

```lean
noncomputable def classicalOscillator : CanonicalEnsemble ℝ
```

**`BlackBody.classicalOscillator_meanEnergy`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L132).

> Equipartition: the mean energy of the classical oscillator is `kB T`.

```lean
lemma classicalOscillator_meanEnergy (kB : BoltzmannConstant) {T : Temperature}
    (hT : 0 < (T : ℝ)) : classicalOscillator.meanEnergy kB T = (kB : ℝ) * T
```

**`BlackBody.quantizedOscillator_meanEnergy_lt`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L156).

> The quantized mean energy lies strictly below the classical one, `kB T`.

```lean
lemma quantizedOscillator_meanEnergy_lt (kB : BoltzmannConstant) {ε : ℝ} (hε : 0 < ε)
    {T : Temperature} (hT : 0 < (T : ℝ)) :
    (quantizedOscillator ε).meanEnergy kB T < classicalOscillator.meanEnergy kB T
```

## C. Planck's law and the Rayleigh–Jeans law

**`BlackBody.spectralRadiance_eq_meanEnergy`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L179).

> Planck's law is `2 ν² / c²` times the mean energy of the oscillator of spacing `h ν`.

```lean
lemma spectralRadiance_eq_meanEnergy (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    {ν : Frequency} (hν : 0 < ν.val) (hT : 0 < (B.T : ℝ)) :
    B.spectralRadiance c kB ν =
      2 * (ν.val : ℝ) ^ 2 / (c : ℝ) ^ 2
        * (quantizedOscillator (h * (ν.val : ℝ))).meanEnergy kB B.T
```

**`BlackBody.rayleighJeans`**, a def, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L193).

> The Rayleigh–Jeans spectral radiance `2 ν² kB T / c²` of a black body `B`.

```lean
noncomputable def rayleighJeans (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (ν : Frequency) : ℝ
```

**`BlackBody.rayleighJeans_eq_meanEnergy`**, a lemma, [line 198](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L198).

> The Rayleigh–Jeans law is `2 ν² / c²` times the mean energy of the classical oscillator.

```lean
lemma rayleighJeans_eq_meanEnergy (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (ν : Frequency) (hT : 0 < (B.T : ℝ)) :
    B.rayleighJeans c kB ν
      = 2 * (ν.val : ℝ) ^ 2 / (c : ℝ) ^ 2 * classicalOscillator.meanEnergy kB B.T
```

**`BlackBody.spectralRadiance_lt_rayleighJeans`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean#L207).

> Planck's law lies strictly below the Rayleigh–Jeans law at every positive frequency and
> every positive temperature.

```lean
lemma spectralRadiance_lt_rayleighJeans (B : BlackBody) (c : SpeedOfLight)
    (kB : BoltzmannConstant) {ν : Frequency} (hν : 0 < ν.val) (hT : 0 < (B.T : ℝ)) :
    B.spectralRadiance c kB ν < B.rayleighJeans c kB ν
```

## Depends on

- [Planck's Law](../../../physlib/quantummechanics/blackbody/planckslaw.md)
- [Canonical Ensemble: Core Definitions](../../../physlib/statisticalmechanics/canonicalensemble/basic.md)

## Proof depends on

- [Canonical Ensemble: Thermodynamic Identities and Relations](../../../physlib/statisticalmechanics/canonicalensemble/lemmas.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Blackbody/RayleighJeans.lean)
