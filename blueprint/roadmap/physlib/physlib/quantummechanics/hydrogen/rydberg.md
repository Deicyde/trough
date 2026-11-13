---
declaration: module
origin: cited
lean: QuantumMechanics.HydrogenAtom.levelIndex, QuantumMechanics.HydrogenAtom.levelIndex_eq, QuantumMechanics.HydrogenAtom.levelIndex_pos, QuantumMechanics.HydrogenAtom.levelIndex_nonneg, QuantumMechanics.HydrogenAtom.levelIndex_strictMono, QuantumMechanics.HydrogenAtom.levelIndex_monotone, QuantumMechanics.HydrogenAtom.rydbergEnergy, QuantumMechanics.HydrogenAtom.rydbergEnergy_eq
statement: formalized
proof: formalized
---

# The Rydberg formula and the spectral series of the hydrogen atom

The module `Physlib.QuantumMechanics.Hydrogen.Rydberg`, [Physlib/QuantumMechanics/Hydrogen/Rydberg.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean): 43 declarations, 43 with a docstring.

## i. Overview

> The bound-state energies expected for the `d`-dimensional hydrogen atom with potential `-k / r`
> are `E_n = -Ry / (n + (d - 1) / 2) ^ 2` for `n : ℕ`, with the Rydberg energy
> `Ry = m k ^ 2 / (2 ℏ ^ 2)`. This module defines these Bohr levels and derives from them, by
> algebra alone, the Rydberg formula for the energy, the frequency and the wavelength of the
> photon emitted in a transition between two levels, together with the Lyman, Balmer and Paschen
> series and their series limits.
>
> …

## ii. Key results

> Definitions:
> - `rydbergEnergy` : the Rydberg energy `Ry = m k ^ 2 / (2 ℏ ^ 2)`.
> - `levelIndex` : the effective principal quantum number `L n = n + (d - 1) / 2`.
> - `energyLevel` : the Bohr levels `E_n = -Ry / L n ^ 2`.
> - `transitionFrequency` : the frequency `ν = (E_{n₂} - E_{n₁}) / h` of the photon emitted in
>     the transition from `n₂` to `n₁`, and `wavelength` its wavelength `c / ν`.
> - `rydbergFrequency` : the Rydberg frequency `R_ν = Ry / h`.
> - `lymanFrequency`, `balmerFrequency`, `paschenFrequency` : the three classical series.
>
> Lemmas:
> - `energyLevel_strictMono` : the Bohr levels increase strictly with `n` when `2 ≤ d`
>     and `k ≠ 0`.
> - `transitionFrequency_eq` : the Rydberg formula `ν = R_ν (1 / L n₁ ^ 2 - 1 / L n₂ ^ 2)`.
> - `wavelength_inv` : its wavenumber form `1 / λ = (R_ν / c) (1 / L n₁ ^ 2 - 1 / L n₂ ^ 2)`.
> - `tendsto_transitionFrequency` : the series limit `ν → R_ν / L n₁ ^ 2` as `n₂ → ∞`.
> - `balmerFrequency_lt_lymanFrequency` : for `2 ≤ d ≤ 5`, every Balmer line lies below every
>     Lyman line.

## iv. References

> * None.

## A. The level index

**`QuantumMechanics.HydrogenAtom.levelIndex`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L80).

> The level index `n + (d - 1) / 2` of the `n`-th Bohr level; for `d = 3` it is the principal
> quantum number `n + 1`.

```lean
def levelIndex (n : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.levelIndex_eq`**, a lemma, [line 83](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L83).

> The defining formula of the level index.

```lean
lemma levelIndex_eq (n : ℕ) : levelIndex d n = n + ((d : ℝ) - 1) / 2
```

**`QuantumMechanics.HydrogenAtom.levelIndex_pos`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L88).

> The level index is positive when `2 ≤ d`.

```lean
lemma levelIndex_pos (hd : 2 ≤ d) (n : ℕ) : 0 < levelIndex d n
```

**`QuantumMechanics.HydrogenAtom.levelIndex_nonneg`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L95).

> The level index is non-negative when `d ≠ 0`.

```lean
lemma levelIndex_nonneg [NeZero d] (n : ℕ) : 0 ≤ levelIndex d n
```

**`QuantumMechanics.HydrogenAtom.levelIndex_strictMono`**, a lemma, [line 102](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L102).

> The level index is strictly increasing.

```lean
lemma levelIndex_strictMono : StrictMono (levelIndex d)
```

**`QuantumMechanics.HydrogenAtom.levelIndex_monotone`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L109).

> The level index is monotone.

```lean
lemma levelIndex_monotone : Monotone (levelIndex d)
```

## B. The Bohr levels

> The Rydberg energy `Ry = m k ^ 2 / (2 ℏ ^ 2)` sets the scale of the spectrum, and the level
> index `L n = n + (d - 1) / 2` is the effective principal quantum number in dimension `d`; for
> `d = 3` it is `n + 1`, the usual principal quantum number, with `n = 0` the ground state.

**`QuantumMechanics.HydrogenAtom.rydbergEnergy`**, a def, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L124).

> The Rydberg energy of the atom, `Ry = m k ^ 2 / (2 ℏ ^ 2)`.

```lean
def rydbergEnergy : ℝ
```

**`QuantumMechanics.HydrogenAtom.rydbergEnergy_eq`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L127).

> The defining formula of the Rydberg energy.

```lean
lemma rydbergEnergy_eq : H.rydbergEnergy = H.m * H.k ^ 2 / (2 * (ℏ : ℝ) ^ 2)
```

**`QuantumMechanics.HydrogenAtom.energyLevel`**, a def, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L134).

> The `n`-th Bohr level `E_n = -Ry / (n + (d - 1) / 2) ^ 2`.
>
> These are the bound-state energies expected for the hydrogen Hamiltonian; that they form its
> point spectrum is not proved here. For `d = 1` and `n = 0` the level index vanishes and the value
> is `0` by the convention `x / 0 = 0`.

```lean
def energyLevel (n : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.energyLevel_eq`**, a lemma, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L137).

> The defining formula of the Bohr levels.

```lean
lemma energyLevel_eq (n : ℕ) : H.energyLevel n = -H.rydbergEnergy / levelIndex d n ^ 2
```

**`QuantumMechanics.HydrogenAtom.rydbergEnergy_nonneg`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L141).

> The Rydberg energy is non-negative.

```lean
lemma rydbergEnergy_nonneg : 0 ≤ H.rydbergEnergy
```

**`QuantumMechanics.HydrogenAtom.rydbergEnergy_pos`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L146).

> The Rydberg energy is positive when `k ≠ 0`.

```lean
lemma rydbergEnergy_pos (hk : H.k ≠ 0) : 0 < H.rydbergEnergy
```

**`QuantumMechanics.HydrogenAtom.rydbergEnergy_eq_zero`**, a lemma, [line 151](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L151).

> The Rydberg energy vanishes when `k = 0`.

```lean
lemma rydbergEnergy_eq_zero (hk : H.k = 0) : H.rydbergEnergy = 0
```

**`QuantumMechanics.HydrogenAtom.energyLevel_nonpos`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L156).

> The Bohr levels are non-positive.

```lean
lemma energyLevel_nonpos (n : ℕ) : H.energyLevel n ≤ 0
```

**`QuantumMechanics.HydrogenAtom.energyLevel_neg`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L161).

> The Bohr levels are negative when `2 ≤ d` and `k ≠ 0`.

```lean
lemma energyLevel_neg (hd : 2 ≤ d) (hk : H.k ≠ 0) (n : ℕ) : H.energyLevel n < 0
```

**`QuantumMechanics.HydrogenAtom.energyLevel_eq_zero`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L166).

> The Bohr levels vanish when `k = 0`.

```lean
lemma energyLevel_eq_zero (hk : H.k = 0) (n : ℕ) : H.energyLevel n = 0
```

**`QuantumMechanics.HydrogenAtom.energyLevel_strictMono`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L170).

> The Bohr levels are strictly increasing when `2 ≤ d` and `k ≠ 0`.

```lean
lemma energyLevel_strictMono (hd : 2 ≤ d) (hk : H.k ≠ 0) : StrictMono H.energyLevel
```

**`QuantumMechanics.HydrogenAtom.energyLevel_monotone`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L179).

> The Bohr levels are monotone when `2 ≤ d`. The hypothesis on `d` cannot be dropped:
> for `d = 1` the level index of `n = 0` vanishes, so that `E_0 = 0` by the convention
> `x / 0 = 0` while every other level is negative.

```lean
lemma energyLevel_monotone (hd : 2 ≤ d) : Monotone H.energyLevel
```

## C. Transitions and the Rydberg formula

> A transition from the level `n₂` down to the level `n₁` emits a photon of energy
> `E_{n₂} - E_{n₁}`, frequency `ν = (E_{n₂} - E_{n₁}) / h` and wavelength `λ = c / ν`, with `c` the
> speed of light. The Rydberg formula expresses these through the Rydberg frequency `R_ν = Ry / h`,
> the frequency of a photon carrying the Rydberg energy.
>
> The same definitions are used for any pair of levels. When `2 ≤ d` and `k ≠ 0` and `n₂ < n₁`,
> the level `n₂` lies below `n₁`: the transition from `n₂` to `n₁` goes up and absorbs a photon, and
> the frequency and the wavelength defined here are then negative, their absolute values being
> those of the absorbed photon. For `n₁ = n₂` there is no photon and the frequency is `0`.

**`QuantumMechanics.HydrogenAtom.transitionEnergy`**, a def, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L201).

> The energy `E_{n₂} - E_{n₁}` of the transition from the level `n₂` to the level `n₁`.

```lean
def transitionEnergy (n₁ n₂ : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.transitionEnergy_eq_sub`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L204).

> The defining formula of the transition energy.

```lean
lemma transitionEnergy_eq_sub (n₁ n₂ : ℕ) :
    H.transitionEnergy n₁ n₂ = H.energyLevel n₂ - H.energyLevel n₁
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency`**, a def, [line 212](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L212).

> The frequency `(E_{n₂} - E_{n₁}) / h` of the transition from `n₂` to `n₁`. When `2 ≤ d` and
> `k ≠ 0`, it is positive for `n₁ < n₂` (`transitionFrequency_pos`): the transition emits a photon
> of this frequency. For `n₂ < n₁` it is negative (`transitionFrequency_neg`): the transition goes
> up in energy and absorbs a photon, whose frequency is the absolute value `(E_{n₁} - E_{n₂}) / h`
> (`transitionFrequency_swap`). For `n₁ = n₂` it is `0` (`transitionFrequency_self`).

```lean
def transitionFrequency (n₁ n₂ : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_eq_div`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L215).

> The defining formula of the transition frequency.

```lean
lemma transitionFrequency_eq_div (n₁ n₂ : ℕ) :
    H.transitionFrequency n₁ n₂ = H.transitionEnergy n₁ n₂ / (h : ℝ)
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_swap`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L219).

> Exchanging the two levels changes the sign of the transition frequency.

```lean
lemma transitionFrequency_swap (n₁ n₂ : ℕ) :
    H.transitionFrequency n₂ n₁ = -H.transitionFrequency n₁ n₂
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_self`**, a lemma, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L226).

> The transition frequency between a level and itself is `0`.

```lean
lemma transitionFrequency_self (n : ℕ) : H.transitionFrequency n n = 0
```

**`QuantumMechanics.HydrogenAtom.rydbergFrequency`**, an abbrev, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L231).

> The Rydberg frequency `R_ν = Ry / h`, the frequency of a photon whose energy is the Rydberg
> energy.

```lean
abbrev rydbergFrequency : ℝ
```

**`QuantumMechanics.HydrogenAtom.wavelength`**, a def, [line 238](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L238).

> The wavelength `c / ν` of the photon emitted in the transition from `n₂` to `n₁`, with `c` the
> speed of light. When `2 ≤ d` and `k ≠ 0` and `n₂ < n₁`, the frequency is negative and so is this
> wavelength; its absolute value is the wavelength of the photon absorbed in the transition from
> `n₂` up to `n₁`. For `n₁ = n₂` there is no photon: the frequency is `0` and the value `c / 0 = 0`
> is a junk value, not a wavelength.

```lean
def wavelength (c : SpeedOfLight) (n₁ n₂ : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.wavelength_eq_div`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L241).

> The defining formula of the wavelength.

```lean
lemma wavelength_eq_div (c : SpeedOfLight) (n₁ n₂ : ℕ) :
    H.wavelength c n₁ n₂ = c / H.transitionFrequency n₁ n₂
```

**`QuantumMechanics.HydrogenAtom.transitionEnergy_eq`**, a lemma, [line 246](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L246).

> The Rydberg formula for the transition energy,
> `E_{n₂} - E_{n₁} = Ry (1 / L n₁ ^ 2 - 1 / L n₂ ^ 2)`.

```lean
lemma transitionEnergy_eq (n₁ n₂ : ℕ) :
    H.transitionEnergy n₁ n₂ =
      H.rydbergEnergy * (1 / levelIndex d n₁ ^ 2 - 1 / levelIndex d n₂ ^ 2)
```

**`QuantumMechanics.HydrogenAtom.rydbergFrequency_eq`**, a lemma, [line 254](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L254).

> The Rydberg frequency in terms of the mass, the coupling constant and `ℏ`,
> `R_ν = m k ^ 2 / (4 π ℏ ^ 3)`, using `h = 2 π ℏ`.

```lean
lemma rydbergFrequency_eq : H.rydbergFrequency = H.m * H.k ^ 2 / (4 * π * (ℏ : ℝ) ^ 3)
```

**`QuantumMechanics.HydrogenAtom.rydbergFrequency_nonneg`**, a lemma, [line 260](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L260).

> The Rydberg frequency is non-negative.

```lean
lemma rydbergFrequency_nonneg : 0 ≤ H.rydbergFrequency
```

**`QuantumMechanics.HydrogenAtom.rydbergFrequency_pos`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L265).

> The Rydberg frequency is positive when `k ≠ 0`. Not `@[simp]`: since `rydbergFrequency` is an
> abbreviation, `simp` already gets this from `rydbergEnergy_pos` and `h_pos`.

```lean
lemma rydbergFrequency_pos (hk : H.k ≠ 0) : 0 < H.rydbergFrequency
```

**`QuantumMechanics.HydrogenAtom.rydbergFrequency_eq_zero`**, a lemma, [line 270](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L270).

> The Rydberg frequency vanishes when `k = 0`.

```lean
lemma rydbergFrequency_eq_zero (hk : H.k = 0) : H.rydbergFrequency = 0
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_eq`**, a lemma, [line 274](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L274).

> The Rydberg formula for the frequency, `ν = R_ν (1 / L n₁ ^ 2 - 1 / L n₂ ^ 2)`.

```lean
lemma transitionFrequency_eq (n₁ n₂ : ℕ) :
    H.transitionFrequency n₁ n₂ =
      H.rydbergFrequency * (1 / levelIndex d n₁ ^ 2 - 1 / levelIndex d n₂ ^ 2)
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_pos`**, a lemma, [line 284](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L284).

> The frequency of a transition from `n₂` down to `n₁ < n₂` is positive when `2 ≤ d` and
> `k ≠ 0`.

```lean
lemma transitionFrequency_pos (hd : 2 ≤ d) (hk : H.k ≠ 0) {n₁ n₂ : ℕ} (hn : n₁ < n₂) :
    0 < H.transitionFrequency n₁ n₂
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_neg`**, a lemma, [line 290](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L290).

> The frequency of a transition from `n₂` up to `n₁`, with `n₂ < n₁`, is negative when `2 ≤ d`
> and `k ≠ 0`: the transition absorbs a photon.

```lean
lemma transitionFrequency_neg (hd : 2 ≤ d) (hk : H.k ≠ 0) {n₁ n₂ : ℕ} (hn : n₂ < n₁) :
    H.transitionFrequency n₁ n₂ < 0
```

**`QuantumMechanics.HydrogenAtom.wavelength_inv`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L297).

> The Rydberg formula for the wavenumber,
> `1 / λ = (R_ν / c) (1 / L n₁ ^ 2 - 1 / L n₂ ^ 2)`.

```lean
lemma wavelength_inv (c : SpeedOfLight) (n₁ n₂ : ℕ) :
    (H.wavelength c n₁ n₂)⁻¹ =
      H.rydbergFrequency / c * (1 / levelIndex d n₁ ^ 2 - 1 / levelIndex d n₂ ^ 2)
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_strictMono`**, a lemma, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L305).

> For a fixed lower level, the transition frequency is strictly increasing in the upper level
> when `2 ≤ d` and `k ≠ 0`.

```lean
lemma transitionFrequency_strictMono (hd : 2 ≤ d) (hk : H.k ≠ 0) (n₁ : ℕ) :
    StrictMono (H.transitionFrequency n₁)
```

**`QuantumMechanics.HydrogenAtom.transitionFrequency_monotone`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L318).

> For a fixed lower level, the transition frequency is monotone in the upper level when
> `2 ≤ d`. The hypothesis on `k` can be dropped, but not the one on `d`: for `d = 1` the level
> index of `n = 0` vanishes and `1 / L 0 ^ 2 = 0` by the convention `x / 0 = 0`.

```lean
lemma transitionFrequency_monotone (hd : 2 ≤ d) (n₁ : ℕ) :
    Monotone (H.transitionFrequency n₁)
```

**`QuantumMechanics.HydrogenAtom.tendsto_transitionFrequency`**, a lemma, [line 326](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L326).

> The series limit: as the upper level goes to infinity, the transition frequency to the
> level `n₁` tends to `R_ν / L n₁ ^ 2`.

```lean
lemma tendsto_transitionFrequency (n₁ : ℕ) :
    Tendsto (fun n₂ : ℕ => H.transitionFrequency n₁ n₂) atTop
      (𝓝 (H.rydbergFrequency / levelIndex d n₁ ^ 2))
```

## D. The spectral series

> The Lyman, Balmer and Paschen series collect the transitions down to the levels of index `0`,
> `1` and `2`; for `d = 3` these are the levels `n = 1`, `2` and `3` of the usual numbering.

**`QuantumMechanics.HydrogenAtom.lymanFrequency`**, an abbrev, [line 347](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L347).

> The Lyman series: the transitions down to the level of index `0`.

```lean
abbrev lymanFrequency (n : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.balmerFrequency`**, an abbrev, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L350).

> The Balmer series: the transitions down to the level of index `1`.

```lean
abbrev balmerFrequency (n : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.paschenFrequency`**, an abbrev, [line 353](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L353).

> The Paschen series: the transitions down to the level of index `2`.

```lean
abbrev paschenFrequency (n : ℕ) : ℝ
```

**`QuantumMechanics.HydrogenAtom.balmerFrequency_lt_lymanFrequency`**, a lemma, [line 363](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean#L363).

> For `2 ≤ d ≤ 5`, every Balmer line has a lower frequency than every Lyman line: the Balmer
> series limit `R_ν / L 1 ^ 2` is at most the first Lyman line `R_ν (1 / L 0 ^ 2 - 1 / L 1 ^ 2)`,
> which holds exactly when `2 L 0 ^ 2 ≤ L 1 ^ 2`, that is `d ^ 2 - 6 d + 1 ≤ 0`. This fails for
> `6 ≤ d`: in dimension `6` the Balmer line `n₂ = 15` has exactly the frequency
> `96 R_ν / 1225` of the first Lyman line, and the Balmer lines above it are faster still.
>
> The Balmer lines are the transitions with `1 < n₂`, but that hypothesis is not needed here: for
> `n₂ ≤ 1` the left-hand side is non-positive while the right-hand side is positive.

```lean
lemma balmerFrequency_lt_lymanFrequency (hd₂ : 2 ≤ d) (hd₅ : d ≤ 5) (hk : H.k ≠ 0)
    {n₂ n₃ : ℕ} (h₃ : 0 < n₃) : H.balmerFrequency n₂ < H.lymanFrequency n₃
```

## Depends on

- [Hydrogen atom](basic.md)
- [The Speed of Light](../../relativity/speedoflight.md)

## Sources

- [Physlib/QuantumMechanics/Hydrogen/Rydberg.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/Hydrogen/Rydberg.lean)
