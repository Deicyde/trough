---
declaration: module
origin: cited
lean: QuantumMechanics.HarmonicOscillator, QuantumMechanics.HarmonicOscillator.m_pos, QuantumMechanics.HarmonicOscillator.m_nonneg, QuantumMechanics.HarmonicOscillator.m_ne_zero, QuantumMechanics.HarmonicOscillator.ω_pos, QuantumMechanics.HarmonicOscillator.ω_nonneg, QuantumMechanics.HarmonicOscillator.ω_ne_zero, QuantumMechanics.HarmonicOscillator.ξ
statement: formalized
proof: formalized
---

# The quantum harmonic oscillator

The module `Physlib.QuantumMechanics.HarmonicOscillator.Basic`, [Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean): 42 declarations, 20 with a docstring.

## i. Overview

> The harmonic oscillator is one of the most important examples in non-relativistic quantum mechanics.
> It describes a particle of mass `m` subject to a positive-definite quadratic potential
> in `d` dimensions.
>
> - `Basic.lean` : Properties of the potential, definition of isotropic oscillators,
>     kinetic, potential and Hamiltonian operators.
> - `LadderOperators.lean` : Definitions of the raising/lowering/number operators
>     and their algebraic properties.
> - `NumberOperator.lean` : The number operators as unbounded operators, symmetry.

## ii. Key results

## iv. References

> * None.

**`QuantumMechanics.HarmonicOscillator`**, a structure, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L59).

> The `d`-dimensional quantum harmonic oscillator.

```lean
structure HarmonicOscillator (d : ℕ) where
  /-- The mass (positive). -/
  m : ℝ
  hm : 0 < m
  /-- The natural frequencies (positive). -/
  ω : Fin d → ℝ
  hω : ∀ i, 0 < ω i
```

## A. Basic properties

### A.1. Positive mass

**`QuantumMechanics.HarmonicOscillator.m_pos`**, a lemma, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L82).

```lean
lemma m_pos : 0 < Q.m
```

**`QuantumMechanics.HarmonicOscillator.m_nonneg`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L85).

```lean
lemma m_nonneg : 0 ≤ Q.m
```

**`QuantumMechanics.HarmonicOscillator.m_ne_zero`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L88).

```lean
lemma m_ne_zero : Q.m ≠ 0
```

### A.2. Positive natural frequencies

**`QuantumMechanics.HarmonicOscillator.ω_pos`**, a lemma, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L95).

```lean
lemma ω_pos : 0 < Q.ω i
```

**`QuantumMechanics.HarmonicOscillator.ω_nonneg`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L98).

```lean
lemma ω_nonneg : 0 ≤ Q.ω i
```

**`QuantumMechanics.HarmonicOscillator.ω_ne_zero`**, a lemma, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L101).

```lean
lemma ω_ne_zero : Q.ω i ≠ 0
```

## B. Characteristic lengths

**`QuantumMechanics.HarmonicOscillator.ξ`**, a def, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L108).

> The characteristic length `ξ i ≔ √ℏ / (√Q.m * √(Q.ω i))`.

```lean
def ξ : ℝ
```

**`QuantumMechanics.HarmonicOscillator.ξ_eq`**, a lemma, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L110).

```lean
lemma ξ_eq : Q.ξ i = √ℏ / (√Q.m * √(Q.ω i))
```

**`QuantumMechanics.HarmonicOscillator.ξ_pos`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L113).

```lean
lemma ξ_pos : 0 < Q.ξ i
```

**`QuantumMechanics.HarmonicOscillator.ξ_nonneg`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L116).

```lean
lemma ξ_nonneg : 0 ≤ Q.ξ i
```

**`QuantumMechanics.HarmonicOscillator.ξ_ne_zero`**, a lemma, [line 119](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L119).

```lean
lemma ξ_ne_zero : Q.ξ i ≠ 0
```

**`QuantumMechanics.HarmonicOscillator.ξ_ofReal_ne_zero`**, a lemma, [line 122](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L122).

> The characteristic length is nonzero as a complex number.

```lean
lemma ξ_ofReal_ne_zero : ((Q.ξ i : ℝ) : ℂ) ≠ 0
```

**`QuantumMechanics.HarmonicOscillator.ξ_sq`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L124).

```lean
lemma ξ_sq : (Q.ξ i) ^ 2 = ℏ / (Q.m * Q.ω i)
```

**`QuantumMechanics.HarmonicOscillator.ξ_inv`**, a lemma, [line 126](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L126).

```lean
lemma ξ_inv : (Q.ξ i)⁻¹ = √Q.m * √(Q.ω i) / √ℏ
```

**`QuantumMechanics.HarmonicOscillator.ξ_inv'`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L128).

```lean
lemma ξ_inv' : (Q.ξ i)⁻¹ = Q.m * Q.ω i * Q.ξ i / ℏ
```

**`QuantumMechanics.HarmonicOscillator.ξ_sq_mul_ofReal`**, a lemma, [line 131](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L131).

> `ξᵢ² m ωᵢ = ℏ`, as complex numbers.

```lean
lemma ξ_sq_mul_ofReal :
    ((Q.ξ i : ℝ) : ℂ) ^ 2 * ((Q.m : ℝ) : ℂ) * ((Q.ω i : ℝ) : ℂ) = (ℏ : ℂ)
```

### B.1. Coordinate rescaling

**`QuantumMechanics.HarmonicOscillator.ξEquiv`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L143).

> The continuous linear equivalence which rescales `xᵢ` to `ξᵢxᵢ`.

```lean
def ξEquiv : Space d ≃L[ℝ] Space d
```

**`QuantumMechanics.HarmonicOscillator.ξEquiv_apply`**, a lemma, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L152).

```lean
lemma ξEquiv_apply (x : Space d) (i : Fin d) : Q.ξEquiv x i = Q.ξ i * x i
```

**`QuantumMechanics.HarmonicOscillator.ξEquiv_symm_apply`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L155).

```lean
lemma ξEquiv_symm_apply (x : Space d) (i : Fin d) : Q.ξEquiv.symm x i = (Q.ξ i)⁻¹ * x i
```

## C. The quadratic potential function

### C.1. Positive-definite matrix

**`QuantumMechanics.HarmonicOscillator.potentialMatrix`**, a def, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L170).

> The positive-definite matrix defining the quadratic potential function.

```lean
def potentialMatrix : Matrix (Fin d) (Fin d) ℝ
```

**`QuantumMechanics.HarmonicOscillator.potentialMatrix_eq`**, a lemma, [line 172](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L172).

```lean
lemma potentialMatrix_eq : Q.potentialMatrix = diagonal ((2⁻¹ * Q.m) • Q.ω ^ 2)
```

**`QuantumMechanics.HarmonicOscillator.potentialMatrix_isHermitian`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L174).

```lean
lemma potentialMatrix_isHermitian : Q.potentialMatrix.IsHermitian
```

**`QuantumMechanics.HarmonicOscillator.potentialMatrix_mulVec`**, a lemma, [line 177](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L177).

```lean
lemma potentialMatrix_mulVec (v : Fin d → ℝ) :
    Q.potentialMatrix *ᵥ v = (2⁻¹ * Q.m) • (Q.ω ^ 2 * v)
```

### C.2. Quadratic form

**`QuantumMechanics.HarmonicOscillator.potentialQuadraticForm`**, a def, [line 187](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L187).

> The positive-definite quadratic form associated to the potential matrix.

```lean
def potentialQuadraticForm : QuadraticForm ℝ (Fin d → ℝ)
```

### C.3. Potential function

**`QuantumMechanics.HarmonicOscillator.potentialFunction`**, a def, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L194).

> The quadratic potential function, `½m · ∑ i, ωᵢ²·xᵢ²`.

```lean
def potentialFunction : Space d → ℝ
```

**`QuantumMechanics.HarmonicOscillator.potentialFunction_eq`**, a lemma, [line 196](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L196).

```lean
lemma potentialFunction_eq : Q.potentialFunction = Q.potentialQuadraticForm ∘ Space.val
```

**`QuantumMechanics.HarmonicOscillator.potentialFunction_apply`**, a lemma, [line 199](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L199).

> `V(x) = ∑ᵢ ½ m ωᵢ² xᵢ²`.

```lean
lemma potentialFunction_apply (x : Space d) :
    Q.potentialFunction x = ∑ i, 2⁻¹ * Q.m * Q.ω i ^ 2 * x i ^ 2
```

**`QuantumMechanics.HarmonicOscillator.potentialFunction_hasTemperateGrowth`**, a lemma, [line 207](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L207).

> The potential function, as a complex-valued function, has temperate growth.

```lean
lemma potentialFunction_hasTemperateGrowth :
    Function.HasTemperateGrowth (fun x : Space d => (Q.potentialFunction x : ℂ))
```

**`QuantumMechanics.HarmonicOscillator.potentialFunction_continuous`**, a lemma, [line 223](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L223).

> The potential function for the harmonic oscillator is continuous.

```lean
lemma potentialFunction_continuous : Continuous Q.potentialFunction
```

**`QuantumMechanics.HarmonicOscillator.potentialFunction_aestronglyMeasurable`**, a lemma, [line 230](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L230).

> The potential function for the harmonic oscillator is a.e. strongly measurable.

```lean
lemma potentialFunction_aestronglyMeasurable :
    MeasureTheory.AEStronglyMeasurable Q.potentialFunction MeasureTheory.volume
```

## D. Isotropic oscillators

**`QuantumMechanics.HarmonicOscillator.IsIsotropic`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L241).

> A Harmonic oscillator is isotropic if all natural frequencies are equal.

```lean
def IsIsotropic : Prop
```

**`QuantumMechanics.HarmonicOscillator.isIsotropic_def`**, a lemma, [line 243](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L243).

```lean
lemma isIsotropic_def : Q.IsIsotropic ↔ ∀ i j, Q.ω i = Q.ω j
```

**`QuantumMechanics.HarmonicOscillator.isIsotropic_of_one`**, a lemma, [line 245](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L245).

```lean
lemma isIsotropic_of_one (Q : HarmonicOscillator 1) : Q.IsIsotropic
```

## E. Hilbert space

**`QuantumMechanics.HarmonicOscillator.HS`**, an abbrev, [line 253](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L253).

> The Hilbert space for the quantum harmonic oscillator.

```lean
abbrev HS (_ : HarmonicOscillator d) : Type _
```

## F. Operators

### F.1. Kinetic energy

**`QuantumMechanics.HarmonicOscillator.kineticOperator`**, a def, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L264).

> The kinetic energy operator, `p²/2m`.

```lean
def kineticOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.kineticOperator_apply_schwartz`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L268).

> The kinetic operator on a Schwartz map, `(1/2m) ∑ᵢ pᵢ (pᵢ f)`.

```lean
lemma kineticOperator_apply_schwartz (f : 𝓢(Space d, ℂ))
    (h : (schwartzEquiv volume f : Q.HS) ∈ Q.kineticOperator.domain) :
    Q.kineticOperator ⟨schwartzEquiv volume f, h⟩
      = schwartzEquiv volume (((2 * Q.m)⁻¹ : ℝ) • ∑ i, 𝐩 i (𝐩 i f))
```

### F.2. Potential energy

**`QuantumMechanics.HarmonicOscillator.potentialOperator`**, a def, [line 305](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L305).

> The potential operator which maps `ψ` to `Q.potentialFunction • ψ`.

```lean
def potentialOperator : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.potentialOperator_apply_schwartz`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L308).

> The potential operator on a Schwartz map, almost everywhere `V f`.

```lean
lemma potentialOperator_apply_schwartz (f : 𝓢(Space d, ℂ))
    (h : (schwartzEquiv volume f : Q.HS) ∈ Q.potentialOperator.domain) :
    ⇑(Q.potentialOperator ⟨schwartzEquiv volume f, h⟩) =ᵐ[volume]
      fun x => (Q.potentialFunction x : ℂ) * f x
```

**`QuantumMechanics.HarmonicOscillator.potentialOperator_isSelfAdjoint`**, a lemma, [line 319](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L319).

> The potential operator for the harmonic oscillator is self-adjoint.

```lean
lemma potentialOperator_isSelfAdjoint : IsSelfAdjoint Q.potentialOperator
```

### F.3. Hamiltonian

**`QuantumMechanics.HarmonicOscillator.hamiltonian`**, a def, [line 331](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L331).

> The Hamiltonian for the harmonic oscillator.

```lean
def hamiltonian : Q.HS →ₗ.[ℂ] Q.HS
```

**`QuantumMechanics.HarmonicOscillator.hamiltonain_eq`**, a lemma, [line 333](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean#L333).

```lean
lemma hamiltonain_eq : Q.hamiltonian = Q.kineticOperator + Q.potentialOperator
```

## G. As a quantum system

## Depends on

- [Physlib.Meta.Informal.Basic](../../meta/informal/basic.md)
- [Momentum operators](../operators/momentum.md)
- [Multiplication operators on `SpaceDHilbertSpace`](../operators/multiplication.md)

## Sources

- [Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QuantumMechanics/HarmonicOscillator/Basic.lean)
