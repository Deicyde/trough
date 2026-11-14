---
declaration: module
origin: cited
lean: BlackBody, BlackBody.spectralRadiance, BlackBody.spectralRadiance_pos, BlackBody.spectralRadiance_nonneg, BlackBody.spectralRadiance_absZero, BlackBody.spectralRadiance_zeroFreq, BlackBody.spectralRadiance_eq_zero_of_nonpos_freq, BlackBody.spectralRadianceWave
statement: formalized
proof: formalized
---

# Planck's Law

The module `Physlib.QuantumMechanics.Blackbody.PlancksLaw`, [Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean): 21 declarations, 21 with a docstring.

> In this module we define Planck's law for blackbody radiation: The spectral density of
> electromagnetic radiation emitted by a black body in thermal equilibrium at a given
> temperature T, when there is no net flow of matter or energy between the body and
> its environment.

## i. Overview

> According to Planck's distribution law, the spectral energy radiance
> (per unit frequency) for a black body at given temperature `T` as a function of frequency `ν`
> is given by
>
>     `B(ν, T) = 2 h ν³ / c² · 1 / (e^{h ν / (k_B T)} - 1)`
>
> where `h` is Planck's constant, `c` the speed of light, and `k_B` the Boltzmann constant.
>
> and per unit wavelength `λ`, given by
>
>     `B(λ, T) = 2 h c² / λ⁵ · 1 / (e^{h c / (λ k_B T)} - 1)`
>
> The two forms are related by `B(λ, T) = (c / λ²) B(ν = c/λ, T)`
> (see `spectralRadianceWave_eq_spectralRadiance`), where the frequency `c / λ`
> is given by `Frequency.ofWavelength`. The frequency and wavelength are taken to be
> of the types `Frequency` and `Wavelength` from `Physlib.Optics`, i.e. nonnegative
> quantities carrying the dimensions of inverse time and of length respectively.

## ii. Key results

> - `BlackBody` : Structure representing an idealized black body in thermal equilibrium.
> - `spectralRadiance` : The spectral radiance per unit frequency of blackbody radiation,
>   as a function of a `Frequency`.
> - `spectralRadiance_pos` : The spectral radiance is positive for positive frequency and temperature.
> - `spectralRadiance_absZero` : The spectral radiance is 0 at absolute zero.
> - `spectralRadianceWave` : Spectral radiance per unit wavelength, as a function of a `Wavelength`.
> - `spectralRadianceWave_eq_spectralRadiance` : Correspondence between the two forms,
>   via `Frequency.ofWavelength`.
> - `firstRadiationConstant` / `secondRadiationConstant` : Radiation constants `c₁L` and `c₂`.
> - `spectralRadianceWave_eq_constants` : Planck's law in terms of radiation constants.

## iv. References

> * https://en.wikipedia.org/wiki/Planck%27s\_law
> * M. Planck, "Ueber das Gesetz der Energieverteilung im Normalspectrum",
>   Ann. Phys. 309 (3), 553–563 (1901).

## A. The BlackBody structure

**`BlackBody`**, a structure, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L78).

> An idealized black body in thermal equilibrium at temperature `T`.

```lean
structure BlackBody where
  /-- The temperature of the black body. -/
  T : Temperature
```

## B. Spectral radiance per unit frequency

**`BlackBody.spectralRadiance`**, a def, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L100).

> The spectral radiance per unit frequency of blackbody radiation at frequency `ν`
> for a black body `B`, speed of light `c` and Boltzmann constant `kB`:
>
> `B(ν, T) = 2 h ν³ / c² · 1 / (e^{h ν / (k_B T)} - 1)`
>
> By the homogeneity and isotropy of blackbody radiation, the spectral radiance
> is independent of position and direction, so it depends only on frequency
> and temperature.
>
> Extended by zero outside the physical domain `0 < ν`.

```lean
noncomputable def spectralRadiance (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (ν : Frequency) : ℝ
```

**`BlackBody.spectralRadiance_pos`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L109).

> The spectral radiance of blackbody radiation is positive for positive frequency
> and positive temperature.

```lean
lemma spectralRadiance_pos (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (ν : Frequency) (hν : 0 < ν.val) (hT : 0 < (B.T : ℝ)) : 0 < B.spectralRadiance c kB ν
```

**`BlackBody.spectralRadiance_nonneg`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L121).

> The spectral radiance per unit frequency is non-negative on the physical domain.

```lean
lemma spectralRadiance_nonneg (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (ν : Frequency) (hν : 0 < ν.val) (hT : 0 < (B.T : ℝ)) : 0 ≤ B.spectralRadiance c kB ν
```

**`BlackBody.spectralRadiance_absZero`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L126).

> The spectral radiance vanishes at absolute zero temperature.

```lean
lemma spectralRadiance_absZero (c : SpeedOfLight) (kB : BoltzmannConstant) (ν : Frequency) :
    spectralRadiance ⟨0⟩ c kB ν = 0
```

**`BlackBody.spectralRadiance_zeroFreq`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L134).

> The spectral radiance vanishes at zero frequency.

```lean
lemma spectralRadiance_zeroFreq (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant) :
    B.spectralRadiance c kB 0 = 0
```

**`BlackBody.spectralRadiance_eq_zero_of_nonpos_freq`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L139).

> The spectral radiance vanishes when frequency is non-positive.

```lean
lemma spectralRadiance_eq_zero_of_nonpos_freq (B : BlackBody) (c : SpeedOfLight)
    (kB : BoltzmannConstant) (ν : Frequency) (hν : ν.val ≤ 0) :
    B.spectralRadiance c kB ν = 0
```

## C. Spectral radiance per unit wavelength

**`BlackBody.spectralRadianceWave`**, a def, [line 154](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L154).

> Spectral radiance per unit wavelength of blackbody radiation at wavelength
> `λ` for a black body `B`, speed of light `c` and Boltzmann constant `kB`:
>
>   `B(λ, T) = 2 h c² / λ⁵ · 1 / (e ^ (h c / (λ kB T)) - 1)`,
>
> extended by zero outside the physical domain `0 < λ`.

```lean
noncomputable def spectralRadianceWave (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (lam : Wavelength) : ℝ
```

**`BlackBody.spectralRadianceWave_pos`**, a lemma, [line 163](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L163).

> The spectral radiance per unit wavelength is positive for positive wavelength
> and positive temperature.

```lean
lemma spectralRadianceWave_pos (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (lam : Wavelength) (hlam : 0 < lam.val) (hT : 0 < (B.T : ℝ)) :
    0 < B.spectralRadianceWave c kB lam
```

**`BlackBody.spectralRadianceWave_nonneg`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L179).

> The spectral radiance per unit wavelength is non-negative on the physical domain.

```lean
lemma spectralRadianceWave_nonneg (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant)
    (lam : Wavelength) (hlam : 0 < lam.val) (hT : 0 < (B.T : ℝ)) :
    0 ≤ B.spectralRadianceWave c kB lam
```

**`BlackBody.spectralRadianceWave_absZero`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L185).

> The spectral radiance per unit wavelength vanishes at absolute zero.

```lean
lemma spectralRadianceWave_absZero (c : SpeedOfLight) (kB : BoltzmannConstant)
    (lam : Wavelength) : spectralRadianceWave ⟨0⟩ c kB lam = 0
```

**`BlackBody.spectralRadianceWave_zeroWave`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L193).

> The spectral radiance per unit wavelength vanishes at zero wavelength.

```lean
lemma spectralRadianceWave_zeroWave (B : BlackBody) (c : SpeedOfLight) (kB : BoltzmannConstant) :
    B.spectralRadianceWave c kB 0 = 0
```

**`BlackBody.spectralRadianceWave_eq_zero_of_nonpos_wave`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L199).

> The spectral radiance per unit wavelength vanishes when wavelength is
> non-positive.

```lean
lemma spectralRadianceWave_eq_zero_of_nonpos_wave (B : BlackBody) (c : SpeedOfLight)
    (kB : BoltzmannConstant) (lam : Wavelength) (hlam : lam.val ≤ 0) :
    B.spectralRadianceWave c kB lam = 0
```

## D. Correspondence between the two forms

> Since `B(λ, T) dλ = -B(ν(λ), T) dν` with `ν = c / λ` and `|dν / dλ| = c / λ²`,
> the wavelength form equals `c / λ²` times the frequency form evaluated at
> `ν = c / λ`.

**`BlackBody.spectralRadianceWave_eq_spectralRadiance`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L215).

> Correspondence between the wavelength and frequency forms of Planck's law:
> `B(λ, T) = (c / λ²) B(ν = c / λ, T)`, where the frequency `c / λ` is given by
> `Frequency.ofWavelength`.

```lean
lemma spectralRadianceWave_eq_spectralRadiance (B : BlackBody) (c : SpeedOfLight)
    (kB : BoltzmannConstant) (lam : Wavelength) (hlam : 0 < lam.val) (hT : 0 < (B.T : ℝ)) :
    B.spectralRadianceWave c kB lam
      = ((c : ℝ) / (lam.val : ℝ) ^ 2) * B.spectralRadiance c kB
          (Frequency.ofWavelength c.toWithDim lam hlam)
```

## E. First and second radiation constants

> The wavelength variant uses only the combinations `2 h c²` and `h c / kB`,
> called the first and second radiation constants.

**`BlackBody.firstRadiationConstant`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L239).

> The first radiation constant `c₁L = 2 h c²`.

```lean
noncomputable def firstRadiationConstant (c : SpeedOfLight) : ℝ
```

**`BlackBody.firstRadiationConstant_pos`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L243).

> The first radiation constant is positive.

```lean
lemma firstRadiationConstant_pos (c : SpeedOfLight) :
    0 < firstRadiationConstant c
```

**`BlackBody.firstRadiationConstant_eq`**, a lemma, [line 249](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L249).

> The first radiation constant equals `2 * h * c ^ 2`.

```lean
lemma firstRadiationConstant_eq (c : SpeedOfLight) :
    firstRadiationConstant c = 2 * h * (c : ℝ) ^ 2
```

**`BlackBody.secondRadiationConstant`**, a def, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L253).

> The second radiation constant `c₂ = h c / kB`.

```lean
noncomputable def secondRadiationConstant (c : SpeedOfLight) (kB : BoltzmannConstant) : ℝ
```

**`BlackBody.secondRadiationConstant_pos`**, a lemma, [line 257](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L257).

> The second radiation constant is positive.

```lean
lemma secondRadiationConstant_pos (c : SpeedOfLight) (kB : BoltzmannConstant) :
    0 < secondRadiationConstant c kB
```

**`BlackBody.secondRadiationConstant_eq`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L263).

> The second radiation constant equals `h * c / kB`.

```lean
lemma secondRadiationConstant_eq (c : SpeedOfLight) (kB : BoltzmannConstant) :
    secondRadiationConstant c kB = (h : ℝ) * (c : ℝ) / (kB : ℝ)
```

**`BlackBody.spectralRadianceWave_eq_constants`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean#L268).

> Planck's law per unit wavelength in terms of the radiation constants:
> `B(λ, T) = (c₁L / λ⁵) / (e ^ (c₂ / (λ T)) - 1)`.

```lean
lemma spectralRadianceWave_eq_constants (B : BlackBody) (c : SpeedOfLight)
    (kB : BoltzmannConstant) (lam : Wavelength) (hlam : 0 < lam.val) (hT : 0 < (B.T : ℝ)) :
    B.spectralRadianceWave c kB lam
      = firstRadiationConstant c / (lam.val : ℝ) ^ 5
        / (Real.exp (secondRadiationConstant c kB / ((lam.val : ℝ) * (B.T : ℝ))) - 1)
```

## Depends on

- [Wavelength](../../optics/wavelength.md)
- [Planck's constant](../planckconstant.md)
- [The Speed of Light](../../relativity/speedoflight.md)
- [Temperature](../../thermodynamics/temperature/basic.md)

## Sources

- [Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Blackbody/PlancksLaw.lean)
