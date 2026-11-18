---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.radialPot, PhyslibAlpha.Hydrogen.regCoeff, PhyslibAlpha.Hydrogen.regCoeff_zero, PhyslibAlpha.Hydrogen.radialRec_regCoeff, PhyslibAlpha.Hydrogen.entireCoeff_regCoeff, PhyslibAlpha.Hydrogen.radial_ode_of_radialRec, PhyslibAlpha.Hydrogen.regSol_near_zero, PhyslibAlpha.Hydrogen.exists_const_of_hasDerivAt_zero
statement: formalized
proof: formalized
---

# Completeness of the regular radial solutions of hydrogen

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.RadialCompleteness`, [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean): 15 declarations, 12 with a docstring.

> Every solution of the radial equation of hydrogen that vanishes at the origin is of the power
> series form assumed in `RadialQuantization`. Together with `radial_quantization` this shows,
> without any ansatz, that a square integrable solution vanishing at the origin exists only for the
> Bohr levels.

## i. Overview

> In Rydberg units the reduced radial function of a state of energy `-κ²` and angular momentum `l`
> solves `u'' = q u` on `(0, ∞)` with `q(ρ) = l(l+1)/ρ² - 2/ρ + κ²` (`radialPot`). The origin is a
> regular singular point with indicial exponents `l + 1` and `-l`.
>
> - The Frobenius solution for the exponent `l + 1` is built explicitly: the coefficients
>   `regCoeff κ l` solve the recursion `RadialRec` with `c_0 = 1` and define an everywhere
>   convergent series (ratio test), and `radialSeries κ l (regCoeff κ l)` solves the radial equation
>   (`radial_ode_of_radialRec`). It behaves like `ρ^(l+1)` near `0`.
> - The second solution is never constructed. Instead, for any solution `u` the Wronskian
>   `u u₁' - u' u₁` with the regular solution `u₁` is constant; if it were non-zero, `u` would grow
>   like `ρ^(-l)` at `0` (and tend to a non-zero constant for `l = 0`). So `u → 0` forces the
>   Wronskian to vanish, and `u` is a multiple of `u₁` near `0`.
> - Uniqueness for the first-order system `(u, u')` (`ODE_solution_unique_of_mem_Ioo`) extends this
>   to all of `(0, ∞)`.
>
> The boundary condition `u(ρ) → 0` as `ρ → 0⁺` is the physical one: for `l = 0` the second solution
> tends to a non-zero constant, so `u₂(r)/r ~ 1/r` near the origin, which lies in `L²(ℝ³)` but not in
> the domain of the Hamiltonian.

## ii. Key results

> - `entireCoeff_regCoeff`, `radial_ode_of_radialRec`: the regular solution.
> - `wronskian_eq_zero_of_tendsto`: a solution tending to `0` has vanishing Wronskian with it.
> - `eqOn_zero_of_eqOn_Ioo`: a solution vanishing near `0` vanishes on `(0, ∞)`.
> - `radial_regular_solution`: every solution vanishing at `0` is `radialSeries κ l c` for an
>   everywhere convergent `c` satisfying the recursion.
> - `radial_quantization_of_tendsto`: the quantisation of the hydrogen levels without the power
>   series ansatz.

## iv. References

> - J. J. Sakurai and J. Napolitano, *Modern Quantum Mechanics*, 3rd ed., Cambridge University
>   Press (2020), section 3.7.

## A. The regular solution

**`PhyslibAlpha.Hydrogen.radialPot`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L80).

> The radial potential term `q(ρ) = l(l+1)/ρ² - 2/ρ + κ²`, so that the radial equation reads
> `u'' = q u`.

```lean
def radialPot (κ : ℝ) (l : ℕ) (ρ : ℝ) : ℝ
```

**`PhyslibAlpha.Hydrogen.regCoeff`**, a def, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L84).

> The coefficients of the regular solution: `c_0 = 1` and
> `c_{k+1} = (2κ(k + l + 1) - 2) / ((k + 1)(k + 2l + 2)) c_k`.

```lean
def regCoeff (κ : ℝ) (l : ℕ) : ℕ → ℝ
```

**`PhyslibAlpha.Hydrogen.regCoeff_zero`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L89).

```lean
lemma regCoeff_zero : regCoeff κ l 0 = 1
```

**`PhyslibAlpha.Hydrogen.radialRec_regCoeff`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L91).

```lean
lemma radialRec_regCoeff : RadialRec κ l (regCoeff κ l)
```

**`PhyslibAlpha.Hydrogen.entireCoeff_regCoeff`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L97).

```lean
lemma entireCoeff_regCoeff : EntireCoeff (regCoeff κ l)
```

**`PhyslibAlpha.Hydrogen.radial_ode_of_radialRec`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L129).

> **Converse of `recursion_of_radial_ode`.** If the coefficients satisfy the recursion, the
> ansatz solves the radial equation on `(0, ∞)`.

```lean
lemma radial_ode_of_radialRec {c : ℕ → ℝ} (hc : EntireCoeff c) (hrec : RadialRec κ l c) {ρ : ℝ}
    (hρ : 0 < ρ) :
    HasDerivAt (radialSeriesD κ l c) (radialPot κ l ρ * radialSeries κ l c ρ) ρ
```

## B. The regular solution near the origin and the Wronskian

**`PhyslibAlpha.Hydrogen.regSol_near_zero`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L159).

> Near the origin the regular solution is comparable to `ρ^(l+1)`.

```lean
lemma regSol_near_zero : ∃ δ > 0, ∃ a > 0, ∃ b > 0, ∀ ρ ∈ Ioc 0 δ,
    a * ρ ^ (l + 1) ≤ radialSeries κ l (regCoeff κ l) ρ ∧
      radialSeries κ l (regCoeff κ l) ρ ≤ b * ρ ^ (l + 1)
```

**`PhyslibAlpha.Hydrogen.exists_const_of_hasDerivAt_zero`**, a lemma, [line 193](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L193).

> A function with vanishing derivative on an open preconnected set is constant there.

```lean
lemma exists_const_of_hasDerivAt_zero {f : ℝ → ℝ} {s : Set ℝ} (hs : IsOpen s)
    (hs' : IsPreconnected s) (h : ∀ x ∈ s, HasDerivAt f 0 x) : ∃ a, ∀ x ∈ s, f x = a
```

**`PhyslibAlpha.Hydrogen.wronskian_const`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L199).

> The Wronskian of two solutions of `u'' = q u` on `(0, ∞)` is constant.

```lean
lemma wronskian_const {q u u' v v' : ℝ → ℝ}
    (hu : ∀ ρ, 0 < ρ → HasDerivAt u (u' ρ) ρ) (hu' : ∀ ρ, 0 < ρ → HasDerivAt u' (q ρ * u ρ) ρ)
    (hv : ∀ ρ, 0 < ρ → HasDerivAt v (v' ρ) ρ) (hv' : ∀ ρ, 0 < ρ → HasDerivAt v' (q ρ * v ρ) ρ) :
    ∃ W : ℝ, ∀ ρ, 0 < ρ → u ρ * v' ρ - u' ρ * v ρ = W
```

## C. Solutions vanishing at the origin

**`PhyslibAlpha.Hydrogen.wronskian_nonpos_of_tendsto`**, a lemma, [line 216](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L216).

> One sign of the Wronskian: if it were positive, `u/u₁ - K ρ^(-(2l+1))` would be antitone near
> `0`, so `u(ρ) ≥ K a - |M| b ρ` for small `ρ`, contradicting `u → 0`.

```lean
lemma wronskian_nonpos_of_tendsto {u u' : ℝ → ℝ}
    (hu : ∀ ρ, 0 < ρ → HasDerivAt u (u' ρ) ρ)
    (hu' : ∀ ρ, 0 < ρ → HasDerivAt u' (radialPot κ l ρ * u ρ) ρ)
    (h0 : Tendsto u (𝓝[>] 0) (𝓝 0)) {ρ₀ : ℝ} (hρ₀ : 0 < ρ₀) :
    u ρ₀ * radialSeriesD κ l (regCoeff κ l) ρ₀ -
      u' ρ₀ * radialSeries κ l (regCoeff κ l) ρ₀ ≤ 0
```

**`PhyslibAlpha.Hydrogen.wronskian_eq_zero_of_tendsto`**, a lemma, [line 306](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L306).

> A solution tending to `0` at the origin has vanishing Wronskian with the regular solution.

```lean
lemma wronskian_eq_zero_of_tendsto {u u' : ℝ → ℝ}
    (hu : ∀ ρ, 0 < ρ → HasDerivAt u (u' ρ) ρ)
    (hu' : ∀ ρ, 0 < ρ → HasDerivAt u' (radialPot κ l ρ * u ρ) ρ)
    (h0 : Tendsto u (𝓝[>] 0) (𝓝 0)) {ρ : ℝ} (hρ : 0 < ρ) :
    u ρ * radialSeriesD κ l (regCoeff κ l) ρ - u' ρ * radialSeries κ l (regCoeff κ l) ρ = 0
```

**`PhyslibAlpha.Hydrogen.exists_eqOn_near_zero_of_tendsto`**, a lemma, [line 318](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L318).

> A solution tending to `0` at the origin is a multiple of the regular solution near `0`.

```lean
lemma exists_eqOn_near_zero_of_tendsto {u u' : ℝ → ℝ}
    (hu : ∀ ρ, 0 < ρ → HasDerivAt u (u' ρ) ρ)
    (hu' : ∀ ρ, 0 < ρ → HasDerivAt u' (radialPot κ l ρ * u ρ) ρ)
    (h0 : Tendsto u (𝓝[>] 0) (𝓝 0)) :
    ∃ δ > 0, ∃ A : ℝ, ∀ ρ ∈ Ioo 0 δ, u ρ = A * radialSeries κ l (regCoeff κ l) ρ
```

## D. Uniqueness away from the origin

**`PhyslibAlpha.Hydrogen.eqOn_zero_of_eqOn_Ioo`**, a lemma, [line 346](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L346).

> A solution of `w'' = q w` with continuous `q` that vanishes on `(0, δ)` vanishes on `(0, ∞)`.

```lean
lemma eqOn_zero_of_eqOn_Ioo {q w w' : ℝ → ℝ} (hq : ContinuousOn q (Ioi 0))
    (hw : ∀ ρ, 0 < ρ → HasDerivAt w (w' ρ) ρ) (hw' : ∀ ρ, 0 < ρ → HasDerivAt w' (q ρ * w ρ) ρ)
    {δ : ℝ} (hδ : 0 < δ) (h : ∀ ρ ∈ Ioo 0 δ, w ρ = 0) :
    ∀ ρ, 0 < ρ → w ρ = 0
```

## E. Completeness and quantisation

**`PhyslibAlpha.Hydrogen.radial_regular_solution`**, a lemma, [line 401](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L401).

> **Completeness of the regular radial solutions.** Every solution of the radial equation
> `u'' = (l(l+1)/ρ² - 2/ρ + κ²) u` on `(0, ∞)` with `u(ρ) → 0` as `ρ → 0⁺` is of the form
> `ρ^(l+1) e^(-κρ) Σ_k c_k ρ^k` with an everywhere convergent series whose coefficients satisfy the
> recursion; if `u` is not identically zero on `(0, ∞)`, then `c_0 ≠ 0`.

```lean
lemma radial_regular_solution {u : ℝ → ℝ}
    (hd : ∀ ρ, 0 < ρ → DifferentiableAt ℝ u ρ ∧ DifferentiableAt ℝ (deriv u) ρ)
    (hode : ∀ ρ, 0 < ρ → deriv (deriv u) ρ =
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + κ ^ 2) * u ρ)
    (h0 : Tendsto u (𝓝[>] 0) (𝓝 0)) :
    ∃ c : ℕ → ℝ, EntireCoeff c ∧ RadialRec κ l c ∧ (∀ ρ, 0 < ρ → u ρ = radialSeries κ l c ρ) ∧
      ((∃ ρ, 0 < ρ ∧ u ρ ≠ 0) → c 0 ≠ 0)
```

**`PhyslibAlpha.Hydrogen.radial_quantization_of_tendsto`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean#L441).

> **Quantisation of the hydrogen levels without ansatz.** A non-zero square integrable solution
> of the radial equation on `(0, ∞)` with energy `-κ²`, `κ > 0`, and `u(ρ) → 0` as `ρ → 0⁺` exists
> only for `κ = 1/ν` with a natural number `ν > l`, and is then a multiple of `u_{νl}`.

```lean
lemma radial_quantization_of_tendsto (hκ : 0 < κ) {u : ℝ → ℝ}
    (hd : ∀ ρ, 0 < ρ → DifferentiableAt ℝ u ρ ∧ DifferentiableAt ℝ (deriv u) ρ)
    (hode : ∀ ρ, 0 < ρ → deriv (deriv u) ρ =
      ((l : ℝ) * (l + 1) / ρ ^ 2 - 2 / ρ + κ ^ 2) * u ρ)
    (h0 : Tendsto u (𝓝[>] 0) (𝓝 0)) (hint : IntegrableOn (fun ρ => u ρ ^ 2) (Ioi 0))
    (hne : ∃ ρ, 0 < ρ ∧ u ρ ≠ 0) :
    ∃ ν : ℕ, l < ν ∧ κ = 1 / (ν : ℝ) ∧ ∃ C : ℝ, ∀ ρ, 0 < ρ → u ρ = C * radialU ν l ρ
```

## Depends on

- [Quantisation of the hydrogen levels](radialquantization.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/QuantumMechanics/Hydrogen/RadialCompleteness.lean)
