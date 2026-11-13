---
declaration: module
origin: cited
lean: Complex.ofReal_hasDerivAt, Complex.deriv_ofReal, Complex.differentiableAt_ofReal, QuantumMechanics.OneDimension.HarmonicOscillator, QuantumMechanics.OneDimension.HarmonicOscillator.m_pos, QuantumMechanics.OneDimension.HarmonicOscillator.m_nonneg, QuantumMechanics.OneDimension.HarmonicOscillator.m_ne_zero, QuantumMechanics.OneDimension.HarmonicOscillator.ω_pos
statement: formalized
proof: formalized
---

# 1d Harmonic Oscillator

The module `Physlib.QuantumMechanics.HarmonicOscillator.OneDimension.Basic`, [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean): 25 declarations, 7 with a docstring.

> The quantum harmonic oscillator in 1d.
> This file contains
> - the definition of the Schrodinger operator
> - the definition of eigenfunctions and eigenvalues of the Schrodinger operator in terms
>   of Hermite polynomials
> - proof that eigenfunctions and eigenvalues are indeed eigenfunctions and eigenvalues.

## Some preliminary results about Complex.ofReal .

> To be moved.

**`Complex.ofReal_hasDerivAt`**, a lemma, [line 36](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L36).

```lean
lemma Complex.ofReal_hasDerivAt : HasDerivAt Complex.ofReal 1 x
```

**`Complex.deriv_ofReal`**, a lemma, [line 44](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L44).

```lean
lemma Complex.deriv_ofReal : deriv Complex.ofReal x = 1
```

**`Complex.differentiableAt_ofReal`**, a lemma, [line 48](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L48).

```lean
lemma Complex.differentiableAt_ofReal : DifferentiableAt ℝ Complex.ofReal x
```

> The 1d Harmonic Oscillator

**`QuantumMechanics.OneDimension.HarmonicOscillator`**, a structure, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L63).

> A quantum harmonic oscillator specified by a three
> real parameters: the mass of the particle `m`, a value of Planck's constant `ℏ`, and
> an angular frequency `ω`. All three of these parameters are assumed to be positive.

```lean
structure HarmonicOscillator where
  /-- The mass of the particle. -/
  m : ℝ
  /-- The angular frequency of the harmonic oscillator. -/
  ω : ℝ
  hω : 0 < ω
  hm : 0 < m
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.m_pos`**, a lemma, [line 79](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L79).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.m_nonneg`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L82).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.m_ne_zero`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L85).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ω_pos`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L88).

```lean
lemma ω_pos : 0 < Q.ω
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ω_nonneg`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L91).

```lean
lemma ω_nonneg : 0 ≤ Q.ω
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ω_ne_zero`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L94).

```lean
lemma ω_ne_zero : Q.ω ≠ 0
```

## The characteristic length

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L104).

> The characteristic length `ξ` of the harmonic oscillator is defined
> as `√(ℏ /(m ω))`.

```lean
noncomputable def ξ : ℝ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_nonneg`**, a lemma, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L106).

```lean
lemma ξ_nonneg : 0 ≤ Q.ξ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_pos`**, a lemma, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L109).

```lean
lemma ξ_pos : 0 < Q.ξ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_ne_zero`**, a lemma, [line 117](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L117).

```lean
lemma ξ_ne_zero : Q.ξ ≠ 0
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_sq`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L119).

```lean
lemma ξ_sq : Q.ξ^2 = ℏ / (Q.m * Q.ω)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_abs`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L127).

```lean
lemma ξ_abs : abs Q.ξ = Q.ξ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.one_over_ξ`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L129).

```lean
lemma one_over_ξ : 1/Q.ξ = √(Q.m * Q.ω / ℏ)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.ξ_inverse`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L135).

```lean
lemma ξ_inverse : Q.ξ⁻¹ = √(Q.m * Q.ω / ℏ)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.one_over_ξ_sq`**, a lemma, [line 139](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L139).

```lean
lemma one_over_ξ_sq : (1/Q.ξ)^2 = Q.m * Q.ω / ℏ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L153).

> For a harmonic oscillator, the Schrodinger Operator corresponding to it
> is defined as the function from `ℝ → ℂ` to `ℝ → ℂ` taking
>
> `ψ ↦ - ℏ^2 / (2 * m) * ψ'' + 1/2 * m * ω^2 * x^2 * ψ`.

```lean
noncomputable def schrodingerOperator (ψ : ℝ → ℂ) : ℝ → ℂ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_eq`**, a lemma, [line 156](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L156).

```lean
lemma schrodingerOperator_eq (ψ : ℝ → ℂ) :
    Q.schrodingerOperator ψ = (- ℏ ^ 2 / (2 * Q.m)) •
    (deriv (deriv ψ)) + (1/2 * Q.m * Q.ω^2) • ((fun x => Complex.ofReal x ^2) * ψ)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_eq_ξ`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L166).

> The schrodinger operator written in terms of `ξ`.

```lean
lemma schrodingerOperator_eq_ξ (ψ : ℝ → ℂ) : Q.schrodingerOperator ψ =
    fun x => (ℏ ^2 / (2 * Q.m)) * (- (deriv (deriv ψ) x) + (1/Q.ξ^2)^2 * x^2 * ψ x)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_parity`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L177).

> The Schrodinger operator commutes with the parity operator.

```lean
lemma schrodingerOperator_parity (ψ : ℝ → ℂ) :
    Q.schrodingerOperator (parityOperator ψ) = parityOperator (Q.schrodingerOperator ψ)
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_add`**, a lemma, [line 186](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L186).

> The Schrodinger operator is additive.

```lean
lemma schrodingerOperator_add (ψ φ : ℝ → ℂ)
    (hψ : Differentiable ℝ ψ) (hψ' : Differentiable ℝ (deriv ψ))
    (hφ : Differentiable ℝ φ) (hφ' : Differentiable ℝ (deriv φ)) :
    Q.schrodingerOperator (ψ + φ) = Q.schrodingerOperator ψ + Q.schrodingerOperator φ
```

**`QuantumMechanics.OneDimension.HarmonicOscillator.schrodingerOperator_smul`**, a lemma, [line 201](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean#L201).

> The Schrodinger operator is homogeneous.

```lean
lemma schrodingerOperator_smul (c : ℂ) (ψ : ℝ → ℂ)
    (hψ : Differentiable ℝ ψ) (hψ' : Differentiable ℝ (deriv ψ)) :
    Q.schrodingerOperator (c • ψ) = c • Q.schrodingerOperator ψ
```

## Depends on

- [Parity operator](../operators/onedimension-parity.md)
- [Planck's constant](../planckconstant.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/OneDimension/Basic.lean)
