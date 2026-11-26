---
declaration: module
origin: cited
lean: PhyslibAlpha.Hydrogen.laplacian_regBoundState, PhyslibAlpha.Hydrogen.boundState_eq_regG, PhyslibAlpha.Hydrogen.contDiff_regBoundState, PhyslibAlpha.Hydrogen.integral_regBoundState_mul_sum_deriv_deriv, PhyslibAlpha.Hydrogen.momentumOperator_apply_schwartzEquiv, PhyslibAlpha.Hydrogen.momentumSqOperator_apply_schwartzEquiv, PhyslibAlpha.Hydrogen.momentumCLM_momentumCLM_apply, PhyslibAlpha.Hydrogen.kineticOperator_apply_of_eq_schwartzEquiv
statement: formalized
proof: formalized
---

# The weak eigenvalue equation of the hydrogen bound states

The module `PhyslibAlpha.QuantumMechanics.Hydrogen.BoundStatesAdjoint`, [PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean): 24 declarations, 24 with a docstring.

> Green's identity for a hydrogen bound state and the weak eigenvalue equation.

## i. Overview

> The bound states are not smooth at the nucleus, so they do not lie in the domain of
> `H.hamiltonianOperator` (whose kinetic part is defined on Schwartz maps). To move the
> Hamiltonian from a Schwartz map onto a bound state `ψ`, one works with the regularised bound
> states `ψ_ε(y) = R(√(‖y‖² + ε²)) P(y)` of `GreenIdentity` and lets `ε → 0`.
>
> With Green's identity for the kinetic term (`integral_boundState_mul_sum_deriv_deriv`) and the
> Coulomb term, the Hamiltonian moves from a Schwartz map onto the bound state
> (`integral_boundState_mul_hamiltonian`), which gives the weak eigenvalue equation
> `⟪E ψ, φ⟫ = ⟪ψ, H φ⟫` for all `φ` in the domain of `H` (`inner_boundStateHS_hamiltonianOperator`).

## ii. Key results

> - `laplacian_regBoundState` : the Laplacian of `ψ_ε` away from the origin.
> - `boundState_eq_regG` : the bound state is `ψ_0`.
> - `integral_regBoundState_mul_sum_deriv_deriv` : Green's identity for `ψ_ε`, `ε ≠ 0`.
> - `kineticOperator_apply_of_eq_schwartzEquiv`, `potentialOperator_apply_ae`: the kinetic and
>   potential operators on their domains.
> - `hamiltonianOperator_apply_ae` : on its domain the Hamiltonian is
>   `-ℏ²/(2m) Σᵢ ∂ᵢ∂ᵢ f + V f` almost everywhere, for a Schwartz representative `f`.
> - `exists_abs_laplacian_regBoundState_le` : a bound on `|Δψ_ε|` uniform in `|ε| ≤ 1`.
> - `integral_boundState_mul_sum_deriv_deriv` : Green's identity `∫ ψ Σᵢ ∂ᵢ∂ᵢ f = ∫ (Δψ) f` for a
>   bound state `ψ`, the limit `ε → 0` by dominated convergence
>   (`tendsto_integral_regBoundState_mul_sum_deriv_deriv`,
>   `tendsto_integral_laplacian_regBoundState_mul`).
> - `integral_boundState_mul_hamiltonian` : Green's identity `∫ ψ H f = ∫ (H ψ) f` for a bound state
>   `ψ` and a Schwartz map `f`.
> - `inner_boundStateHS_hamiltonianOperator` : the weak eigenvalue equation
>   `⟪E ψ, φ⟫ = ⟪ψ, H φ⟫` for `φ` in the domain of the Hamiltonian.

## iv. References

> - None.

## A. Regularised bound states

**`PhyslibAlpha.Hydrogen.laplacian_regBoundState`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L76).

> Away from the origin, `Δψ_ε = ((4l + 2d) G_ε' + 4‖y‖² G_ε'') P` for a homogeneous harmonic `P`
> of degree `l` (also for `ε = 0`, where `ψ_0` is the bound state).

```lean
lemma laplacian_regBoundState {d : ℕ} (κ : ℝ) (N α : ℕ) {l : ℕ}
    {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l) (ε : ℝ) {y : Space d}
    (hy : y ≠ 0) :
    Δ (fun y => regG (radialFactor κ N α) ε (‖y‖ ^ 2) * toFun P y) y =
      ((4 * l + 2 * d) * regG' (radialFactor' κ N α) ε (‖y‖ ^ 2) +
        4 * ‖y‖ ^ 2 * regG'' (radialFactor' κ N α) (radialFactor'' κ N α) ε (‖y‖ ^ 2)) *
          toFun P y
```

**`PhyslibAlpha.Hydrogen.boundState_eq_regG`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L98).

> The bound state is the regularised bound state at `ε = 0`.

```lean
lemma boundState_eq_regG (H : QuantumMechanics.HydrogenAtom d) (N l : ℕ)
    (P : MvPolynomial (Fin d) ℝ) :
    boundState H N l (toFun P) = fun y =>
      regG (radialFactor (boundKappa H (N + l)) N (2 * l + d - 2)) 0 (‖y‖ ^ 2) *
        toFun P y
```

**`PhyslibAlpha.Hydrogen.contDiff_regBoundState`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L108).

> The regularised bound state `ψ_ε(y) = R(√(‖y‖² + ε²)) P(y)` is twice continuously
> differentiable for `ε ≠ 0`.

```lean
lemma contDiff_regBoundState {d : ℕ} (κ : ℝ) (N α : ℕ) (P : MvPolynomial (Fin d) ℝ) {ε : ℝ}
    (hε : ε ≠ 0) :
    ContDiff ℝ 2 (fun y : Space d => regG (radialFactor κ N α) ε (‖y‖ ^ 2) * toFun P y)
```

**`PhyslibAlpha.Hydrogen.integral_regBoundState_mul_sum_deriv_deriv`**, a lemma, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L123).

> **Green's identity for the regularised bound state** `ψ_ε(y) = R(√(‖y‖² + ε²)) P(y)`,
> `R = radialFactor κ N α` with `κ ≥ 0`.

```lean
lemma integral_regBoundState_mul_sum_deriv_deriv {d : ℕ} {κ : ℝ} (hκ : 0 ≤ κ) (N α : ℕ)
    (P : MvPolynomial (Fin d) ℝ) {ε : ℝ} (hε : ε ≠ 0) (f : 𝓢(Space d, ℂ)) :
    ∫ y, ((regG (radialFactor κ N α) ε (‖y‖ ^ 2) * toFun P y : ℝ) : ℂ) *
        ∑ i, ∂[i] (∂[i] ⇑f) y =
      ∫ y, ((∑ i, ∂[i] (∂[i] (fun y => regG (radialFactor κ N α) ε (‖y‖ ^ 2) * toFun P y)) y :
        ℝ) : ℂ) * f y
```

## B. The weak eigenvalue equation

**`PhyslibAlpha.Hydrogen.momentumOperator_apply_schwartzEquiv`**, a lemma, [line 182](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L182).

> On (the class of) a Schwartz map `g`, the momentum operator acts as `𝐩ᵢ g`.

```lean
lemma momentumOperator_apply_schwartzEquiv {d : ℕ} (i : Fin d) (g : 𝓢(Space d, ℂ)) :
    𝓟 i (schwartzEquiv volume g) = schwartzEquiv volume (𝐩 i g)
```

**`PhyslibAlpha.Hydrogen.momentumSqOperator_apply_schwartzEquiv`**, a lemma, [line 187](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L187).

> On (the class of) a Schwartz map `f`, the momentum squared acts as `Σᵢ 𝐩ᵢ 𝐩ᵢ f`.

```lean
lemma momentumSqOperator_apply_schwartzEquiv {d : ℕ} (f : 𝓢(Space d, ℂ))
    (h : ((schwartzEquiv volume f : SchwartzSubmodule d) : SpaceDHilbertSpace d) ∈
      (momentumSqOperator (d := d)).domain) :
    momentumSqOperator ⟨_, h⟩ =
      ((schwartzEquiv volume (∑ i, 𝐩 i (𝐩 i f)) : SchwartzSubmodule d) : SpaceDHilbertSpace d)
```

**`PhyslibAlpha.Hydrogen.momentumCLM_momentumCLM_apply`**, a lemma, [line 204](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L204).

> Applying the momentum operator twice in the direction `i` to a Schwartz map gives
> `-ℏ² ∂ᵢ∂ᵢ f`.

```lean
lemma momentumCLM_momentumCLM_apply {d : ℕ} (i : Fin d) (f : 𝓢(Space d, ℂ)) (y : Space d) :
    (𝐩 i (𝐩 i f)) y = -((Constants.ℏ : ℝ) : ℂ) ^ 2 * ∂[i] (∂[i] ⇑f) y
```

**`PhyslibAlpha.Hydrogen.kineticOperator_apply_of_eq_schwartzEquiv`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L217).

> On (the class of) a Schwartz map `f`, the kinetic operator acts as `(2m)⁻¹ Σᵢ 𝐩ᵢ 𝐩ᵢ f`.

```lean
lemma kineticOperator_apply_of_eq_schwartzEquiv (H : HydrogenAtom d)
    (x : H.kineticOperator.domain) (f : 𝓢(Space d, ℂ))
    (hx : (x : SpaceDHilbertSpace d) = (schwartzEquiv volume f : SchwartzSubmodule d)) :
    H.kineticOperator x = ((2 * H.m : ℝ)⁻¹ : ℂ) •
      ((schwartzEquiv volume (∑ i, 𝐩 i (𝐩 i f)) : SchwartzSubmodule d) :
        SpaceDHilbertSpace d)
```

**`PhyslibAlpha.Hydrogen.potentialOperator_apply_ae`**, a lemma, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L241).

> The potential operator of the hydrogen atom acts by multiplication with `V`, almost
> everywhere.

```lean
lemma potentialOperator_apply_ae (H : HydrogenAtom d) (x : H.potentialOperator.domain) :
    (H.potentialOperator x : SpaceDHilbertSpace d) =ᵐ[volume]
      fun y => (H.potential y : ℂ) * (x : SpaceDHilbertSpace d) y
```

**`PhyslibAlpha.Hydrogen.hamiltonianOperator_apply_ae`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L256).

> A vector `φ` in the domain of the Hamiltonian is (the class of) a Schwartz map `f`, and
> `H φ = -ℏ²/(2m) Σᵢ ∂ᵢ∂ᵢ f + V f` almost everywhere.

```lean
lemma hamiltonianOperator_apply_ae (H : HydrogenAtom d) (φ : H.hamiltonianOperator.domain) :
    ∃ f : 𝓢(Space d, ℂ), (φ : SpaceDHilbertSpace d) =ᵐ[volume] f ∧
      H.hamiltonianOperator φ =ᵐ[volume] fun y =>
        (-((Constants.ℏ : ℝ) : ℂ) ^ 2 / (2 * H.m)) * ∑ i, ∂[i] (∂[i] ⇑f) y +
          (H.potential y : ℂ) * f y
```

**`PhyslibAlpha.Hydrogen.abs_radialLaplacianCoeff_le`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L293).

> An elementary bound for the coefficient of the radial Laplacian: for `0 < r ≤ ρ` and `c ≥ 0`,
> `|c a₁/(2ρ) + 4r² (a₂ - a₁/ρ)/(4ρ²)| ≤ (c + 1) B₁/r + B₂` whenever `|a₁| ≤ B₁` and `|a₂| ≤ B₂`.

```lean
lemma abs_radialLaplacianCoeff_le {r ρ c a₁ a₂ B₁ B₂ : ℝ} (hr : 0 < r) (hrρ : r ≤ ρ)
    (hc : 0 ≤ c) (h₁ : |a₁| ≤ B₁) (h₂ : |a₂| ≤ B₂) :
    |c * (a₁ / (2 * ρ)) + 4 * r ^ 2 * ((a₂ - a₁ / ρ) / (4 * ρ ^ 2))| ≤
      (c + 1) * B₁ * r⁻¹ + B₂
```

**`PhyslibAlpha.Hydrogen.exists_abs_laplacian_regBoundState_le`**, a lemma, [line 322](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L322).

> A bound `|Δψ_ε(y)| ≤ (A (1 + ‖y‖)^k₁ ‖y‖⁻¹ + C (1 + ‖y‖)^k₂) |P(y)|` away from the origin,
> uniform in `|ε| ≤ 1` (including the bound state itself at `ε = 0`).

```lean
lemma exists_abs_laplacian_regBoundState_le {d : ℕ} {κ : ℝ} (hκ : 0 ≤ κ) (N α : ℕ) {l : ℕ}
    {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l) :
    ∃ (A C : ℝ) (k₁ k₂ : ℕ), 0 ≤ A ∧ 0 ≤ C ∧ ∀ ε : ℝ, |ε| ≤ 1 → ∀ y : Space d, y ≠ 0 →
      |Δ (fun y => regG (radialFactor κ N α) ε (‖y‖ ^ 2) * toFun P y) y| ≤
        (A * (1 + ‖y‖) ^ k₁ * ‖y‖⁻¹ + C * (1 + ‖y‖) ^ k₂) * |toFun P y|
```

**`PhyslibAlpha.Hydrogen.ae_ne_zero_of_two_le`**, a lemma, [line 355](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L355).

> For `d ≥ 2`, almost every point of `Space d` is nonzero.

```lean
lemma ae_ne_zero_of_two_le {d : ℕ} (hd : 2 ≤ d) : ∀ᵐ y ∂(volume : Measure (Space d)), y ≠ 0
```

**`PhyslibAlpha.Hydrogen.integrable_laplacianBound_mul`**, a lemma, [line 362](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L362).

> The dominating function `‖y‖⁻¹ |A (1 + ‖y‖)^k₁ P(y)| ‖f(y)‖ + |C (1 + ‖y‖)^k₂ P(y)| ‖f(y)‖` of
> the Laplacians of the regularised bound states is integrable for `d ≥ 2`.

```lean
lemma integrable_laplacianBound_mul {d : ℕ} (hd : 2 ≤ d) (P : MvPolynomial (Fin d) ℝ)
    (A C : ℝ) (k₁ k₂ : ℕ) (f : 𝓢(Space d, ℂ)) :
    Integrable (fun y : Space d => ‖y‖⁻¹ * (|A * (1 + ‖y‖) ^ k₁ * toFun P y| * ‖f y‖) +
      |C * (1 + ‖y‖) ^ k₂ * toFun P y| * ‖f y‖)
```

**`PhyslibAlpha.Hydrogen.norm_mul_le_laplacianBound`**, a lemma, [line 383](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L383).

> A pointwise bound `|g(y)| ≤ (A (1 + ‖y‖)^k₁ ‖y‖⁻¹ + C (1 + ‖y‖)^k₂) |P(y)|` gives the bound of
> `g f` by the dominating function of `integrable_laplacianBound_mul`.

```lean
lemma norm_mul_le_laplacianBound {d : ℕ} {g : Space d → ℝ} {A C : ℝ} {k₁ k₂ : ℕ} (hA : 0 ≤ A)
    (hC : 0 ≤ C) (P : MvPolynomial (Fin d) ℝ) (f : 𝓢(Space d, ℂ)) {y : Space d}
    (hb : |g y| ≤ (A * (1 + ‖y‖) ^ k₁ * ‖y‖⁻¹ + C * (1 + ‖y‖) ^ k₂) * |toFun P y|) :
    ‖((g y : ℝ) : ℂ) * f y‖ ≤ ‖y‖⁻¹ * (|A * (1 + ‖y‖) ^ k₁ * toFun P y| * ‖f y‖) +
      |C * (1 + ‖y‖) ^ k₂ * toFun P y| * ‖f y‖
```

**`PhyslibAlpha.Hydrogen.tendsto_integral_regBoundState_mul_sum_deriv_deriv`**, a lemma, [line 398](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L398).

> Along a sequence `εₙ → 0` with `|εₙ| ≤ 1`,
> `∫ ψ_{εₙ} Σᵢ ∂ᵢ∂ᵢ f → ∫ ψ_0 Σᵢ ∂ᵢ∂ᵢ f`, by dominated convergence.

```lean
lemma tendsto_integral_regBoundState_mul_sum_deriv_deriv {d : ℕ} {κ : ℝ} (hκ : 0 ≤ κ) (N α : ℕ)
    (P : MvPolynomial (Fin d) ℝ) {εs : ℕ → ℝ} (hεs_le : ∀ n, |εs n| ≤ 1)
    (hεs : Filter.Tendsto εs Filter.atTop (nhds 0)) (f : 𝓢(Space d, ℂ)) :
    Filter.Tendsto (fun n => ∫ y, ((regG (radialFactor κ N α) (εs n) (‖y‖ ^ 2) * toFun P y : ℝ) :
        ℂ) * ∑ i, ∂[i] (∂[i] ⇑f) y) Filter.atTop
      (nhds (∫ y, ((regG (radialFactor κ N α) 0 (‖y‖ ^ 2) * toFun P y : ℝ) : ℂ) *
        ∑ i, ∂[i] (∂[i] ⇑f) y))
```

**`PhyslibAlpha.Hydrogen.tendsto_laplacian_regBoundState`**, a lemma, [line 442](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L442).

> Away from the origin, `Δψ_{εₙ}(y) → Δψ_0(y)` along a sequence `εₙ → 0`.

```lean
lemma tendsto_laplacian_regBoundState {d : ℕ} (κ : ℝ) (N α : ℕ) {l : ℕ}
    {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l) {εs : ℕ → ℝ}
    (hεs : Filter.Tendsto εs Filter.atTop (nhds 0)) {y : Space d} (hy : y ≠ 0) :
    Filter.Tendsto
      (fun n => Δ (fun y => regG (radialFactor κ N α) (εs n) (‖y‖ ^ 2) * toFun P y) y)
      Filter.atTop (nhds (Δ (fun y => regG (radialFactor κ N α) 0 (‖y‖ ^ 2) * toFun P y) y))
```

**`PhyslibAlpha.Hydrogen.tendsto_integral_laplacian_regBoundState_mul`**, a lemma, [line 468](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L468).

> Along a sequence `εₙ → 0` with `|εₙ| ≤ 1`, `∫ (Δψ_{εₙ}) f → ∫ (Δψ_0) f`, by dominated
> convergence with the bound `exists_abs_laplacian_regBoundState_le`.

```lean
lemma tendsto_integral_laplacian_regBoundState_mul {d : ℕ} (hd : 2 ≤ d) {κ : ℝ} (hκ : 0 ≤ κ)
    (N α : ℕ) {l : ℕ} {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l)
    {εs : ℕ → ℝ} (hεs_le : ∀ n, |εs n| ≤ 1) (hεs : Filter.Tendsto εs Filter.atTop (nhds 0))
    (f : 𝓢(Space d, ℂ)) :
    Filter.Tendsto (fun n => ∫ y, ((Δ (fun y => regG (radialFactor κ N α) (εs n) (‖y‖ ^ 2) *
        toFun P y) y : ℝ) : ℂ) * f y) Filter.atTop
      (nhds (∫ y, ((Δ (fun y => regG (radialFactor κ N α) 0 (‖y‖ ^ 2) * toFun P y) y : ℝ) :
        ℂ) * f y))
```

**`PhyslibAlpha.Hydrogen.integral_boundState_mul_sum_deriv_deriv`**, a lemma, [line 495](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L495).

> **Green's identity for the kinetic term**: `∫ ψ Σᵢ ∂ᵢ∂ᵢ f = ∫ (Δψ) f` for a bound state `ψ`,
> the limit `ε → 0` of `integral_regBoundState_mul_sum_deriv_deriv`.

```lean
lemma integral_boundState_mul_sum_deriv_deriv (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k)
    (N l : ℕ) {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l)
    (f : 𝓢(Space d, ℂ)) :
    ∫ y, (boundState H N l (toFun P) y : ℂ) * ∑ i, ∂[i] (∂[i] ⇑f) y =
      ∫ y, ((Δ (boundState H N l (toFun P)) y : ℝ) : ℂ) * f y
```

**`PhyslibAlpha.Hydrogen.isPolyBounded_boundState`**, a lemma, [line 522](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L522).

> A hydrogen bound state is polynomially bounded.

```lean
lemma isPolyBounded_boundState (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k) (N l : ℕ)
    (P : MvPolynomial (Fin d) ℝ) : IsPolyBounded (boundState H N l (toFun P))
```

**`PhyslibAlpha.Hydrogen.integrable_boundState_mul_potential_mul`**, a lemma, [line 536](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L536).

> The Coulomb term `ψ V f` of a bound state `ψ` and a Schwartz map `f` is integrable.

```lean
lemma integrable_boundState_mul_potential_mul (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k)
    (N l : ℕ) (P : MvPolynomial (Fin d) ℝ) (f : 𝓢(Space d, ℂ)) :
    Integrable fun y => (boundState H N l (toFun P) y : ℂ) * ((H.potential y : ℂ) * f y)
```

**`PhyslibAlpha.Hydrogen.integrable_laplacian_boundState_mul`**, a lemma, [line 558](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L558).

> The kinetic term `(Δψ) f` of a bound state `ψ` and a Schwartz map `f` is integrable.

```lean
lemma integrable_laplacian_boundState_mul (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k)
    (N l : ℕ) {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l)
    (f : 𝓢(Space d, ℂ)) :
    Integrable fun y => ((Δ (boundState H N l (toFun P)) y : ℝ) : ℂ) * f y
```

**`PhyslibAlpha.Hydrogen.integral_boundState_mul_hamiltonian`**, a lemma, [line 579](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L579).

> **Green's identity for a bound state.** Moving the Hamiltonian from a Schwartz map `f` onto
> the bound state `ψ`, which is smooth away from the nucleus:
> `∫ ψ (-ℏ²/(2m) Σᵢ ∂ᵢ∂ᵢ f + V f) = ∫ (-ℏ²/(2m) Δψ + V ψ) f`.

```lean
lemma integral_boundState_mul_hamiltonian (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k)
    (N l : ℕ) {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l)
    (f : 𝓢(Space d, ℂ)) :
    ∫ y, (boundState H N l (toFun P) y : ℂ) *
        ((-((Constants.ℏ : ℝ) : ℂ) ^ 2 / (2 * H.m)) * ∑ i, ∂[i] (∂[i] ⇑f) y +
          (H.potential y : ℂ) * f y) =
      ∫ y, ((-((Constants.ℏ : ℝ) ^ 2 / (2 * H.m)) * Δ (boundState H N l (toFun P)) y +
          H.potential y * boundState H N l (toFun P) y : ℝ) : ℂ) * f y
```

**`PhyslibAlpha.Hydrogen.inner_boundStateHS_hamiltonianOperator`**, a lemma, [line 629](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean#L629).

> The weak eigenvalue equation `⟪E ψ, φ⟫ = ⟪ψ, H φ⟫` of a bound state `ψ` of the level `N + l`,
> for every `φ` in the domain of the Hamiltonian.

```lean
lemma inner_boundStateHS_hamiltonianOperator (H : HydrogenAtom d) (hd : 2 ≤ d) (hk : 0 < H.k)
    (N l : ℕ) {P : MvPolynomial (Fin d) ℝ} (hP : P ∈ harmonicSubmodule d l)
    (φ : H.hamiltonianOperator.domain) :
    ⟪(H.energyLevel (N + l) : ℂ) • boundStateHS H hd hk N l P, (φ : SpaceDHilbertSpace d)⟫_ℂ =
      ⟪boundStateHS H hd hk N l P, H.hamiltonianOperator φ⟫_ℂ
```

## Depends on

- [The hydrogen bound states in `L²`](boundstatesl2.md)
- [Green's identity and regularised radial functions](greenidentity.md)

## Sources

- [PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/QuantumMechanics/Hydrogen/BoundStatesAdjoint.lean)
