---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.kineticTerm, Electromagnetism.ElectromagneticPotential.kineticTerm_equivariant, Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum, Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum_sq, Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum_potential, Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electric_magnetic, Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electric_magnetic', Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electricMatrix_magneticFieldMatrix_time_space
statement: formalized
proof: formalized
---

# The kinetic term

The module `Physlib.Electromagnetism.Dynamics.KineticTerm`, [Physlib/Electromagnetism/Dynamics/KineticTerm.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean): 23 declarations, 2 with a docstring.

## i. Overview

> The kinetic term of the electromagnetic field is `- 1/(4 μ₀) F_μν F^μν`.
> We define this, show it is invariant under Lorentz transformations,
> and show properties of its variational gradient.
>
> In particular the variational gradient `gradKineticTerm` of the kinetic term
> is directly related to Gauss's law and the Ampere law.
>
> …

## ii. Key results

> - `ElectromagneticPotential.kineticTerm` is the kinetic term of an electromagnetic potential.
> - `ElectromagneticPotential.kineticTerm_equivariant` shows that the kinetic term is
>   Lorentz invariant.
> - `ElectromagneticPotential.gradKineticTerm` is the variational gradient of the kinetic term.
> - `ElectromagneticPotential.gradKineticTerm_eq_electric_magnetic` gives a first expression for the
>   variational gradient in terms of the electric and magnetic fields.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]

## A. The kinetic term

> The kinetic term is `- 1/(4 μ₀) F_μν F^μν`. We define this and show that it is
> Lorentz invariant.

**`Electromagnetism.ElectromagneticPotential.kineticTerm`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L87).

> The kinetic energy from an electromagnetic potential.

```lean
noncomputable def kineticTerm {d} (𝓕 : FreeSpace) (A : ElectromagneticPotential d) :
    SpaceTime d → ℝ
```

### A.1. Lorentz invariance of the kinetic term

> We show that the kinetic energy is Lorentz invariant.

**`Electromagnetism.ElectromagneticPotential.kineticTerm_equivariant`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L100).

```lean
lemma kineticTerm_equivariant {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (Λ : LorentzGroup d)
    (hf : Differentiable ℝ A) (x : SpaceTime d) :
    kineticTerm 𝓕 (Λ • A) x = kineticTerm 𝓕 A (Λ⁻¹ • x)
```

### A.2. Kinetic term simplified expressions

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L116).

```lean
lemma kineticTerm_eq_sum {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    A.kineticTerm 𝓕 x =
    - 1/(4 * 𝓕.μ₀) * ∑ μ, ∑ ν, ∑ μ', ∑ ν', η μ μ' * η ν ν' *
      toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ * toScalar {A.toFieldStrength x | [μ'] [ν']}ᵀ
```

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum_sq`**, a lemma, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L162).

```lean
lemma kineticTerm_eq_sum_sq {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (x : SpaceTime d) : A.kineticTerm 𝓕 x =
    - 1/(4 * 𝓕.μ₀) * ∑ μ, ∑ ν, η μ μ * η ν ν * ‖toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ‖ ^ 2
```

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_sum_potential`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L174).

```lean
lemma kineticTerm_eq_sum_potential {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (x : SpaceTime d) :
    A.kineticTerm 𝓕 x = - 1 / (2 * 𝓕.μ₀) * ∑ μ, ∑ ν,
        (η μ μ * η ν ν * (∂_ μ A x ν) ^ 2 - ∂_ μ A x ν * ∂_ ν A x μ)
```

### A.3. The kinetic term in terms of the electric and magnetic fields

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electric_magnetic`**, a lemma, [line 215](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L215).

```lean
lemma kineticTerm_eq_electric_magnetic {𝓕 : FreeSpace} (A : ElectromagneticPotential) (t : Time)
    (x : Space) (hA : Differentiable ℝ A) :
    A.kineticTerm 𝓕 ((toTimeAndSpace 𝓕.c).symm (t, x)) =
    1/2 * (𝓕.ε₀ * ‖A.electricField 𝓕.c t x‖ ^ 2 - (1 / 𝓕.μ₀) * ‖A.magneticField 𝓕.c t x‖ ^ 2)
```

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electric_magnetic'`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L231).

```lean
lemma kineticTerm_eq_electric_magnetic' {𝓕 : FreeSpace} {A : ElectromagneticPotential}
    (hA : Differentiable ℝ A) (x : SpaceTime) :
    A.kineticTerm 𝓕 x =
    1/2 * (𝓕.ε₀ * ‖A.electricField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2 -
      (1 / 𝓕.μ₀) * ‖A.magneticField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2)
```

### A.4. The kinetic term in terms of the electric and magnetic matrix

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electricMatrix_magneticFieldMatrix_time_space`**, a lemma, [line 244](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L244).

```lean
lemma kineticTerm_eq_electricMatrix_magneticFieldMatrix_time_space {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (t : Time)
    (x : Space d) (hA : Differentiable ℝ A) :
    A.kineticTerm 𝓕 ((toTimeAndSpace 𝓕.c).symm (t, x)) =
    1/2 * (𝓕.ε₀ * ‖A.electricField 𝓕.c t x‖ ^ 2 -
    (1 / (2 * 𝓕.μ₀)) * ∑ i, ∑ j, ‖A.magneticFieldMatrix 𝓕.c t x (i, j)‖ ^ 2)
```

**`Electromagnetism.ElectromagneticPotential.kineticTerm_eq_electricMatrix_magneticFieldMatrix`**, a lemma, [line 278](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L278).

```lean
lemma kineticTerm_eq_electricMatrix_magneticFieldMatrix {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (x : SpaceTime d)
    (hA : Differentiable ℝ A) :
    A.kineticTerm 𝓕 x =
    1/2 * (𝓕.ε₀ * ‖A.electricField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2 -
    (1 / (2 * 𝓕.μ₀)) * ∑ i, ∑ j, ‖A.magneticFieldMatrix 𝓕.c (x.time 𝓕.c) x.space (i, j)‖ ^ 2)
```

### A.5. The kinetic term for constant fields

**`Electromagnetism.ElectromagneticPotential.kineticTerm_const`**, a lemma, [line 293](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L293).

```lean
lemma kineticTerm_const {d} {𝓕 : FreeSpace} (A₀ : Lorentz.Vector d) :
    kineticTerm 𝓕 ⟨fun _ : SpaceTime d => A₀⟩ = 0
```

**`Electromagnetism.ElectromagneticPotential.kineticTerm_add_const`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L298).

```lean
lemma kineticTerm_add_const {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (A₀ : Lorentz.Vector d) :
    kineticTerm 𝓕 ⟨fun x => A x + A₀⟩ = kineticTerm 𝓕 A
```

### A.6. Smoothness of the kinetic term

**`Electromagnetism.ElectromagneticPotential.kineticTerm_contDiff`**, a lemma, [line 310](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L310).

```lean
lemma kineticTerm_contDiff {d} {n : WithTop ℕ∞} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ (n + 1) A) :
    ContDiff ℝ n (A.kineticTerm 𝓕)
```

### A.7. The kinetic term shifted by time mul a constant

> This result is used in finding the canonical momentum.

**`Electromagnetism.ElectromagneticPotential.kineticTerm_add_time_mul_const`**, a lemma, [line 325](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L325).

```lean
lemma kineticTerm_add_time_mul_const {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (ha : Differentiable ℝ A)
    (c : Lorentz.Vector d) (x : SpaceTime d) :
    kineticTerm 𝓕 ⟨fun x => A x + x (Sum.inl 0) • c⟩ x = A.kineticTerm 𝓕 x +
        (-1 / (2 * 𝓕.μ₀) * ∑ ν, ((2 * c ν * η ν ν * ∂_ (Sum.inl 0) A x ν + η ν ν * c ν ^ 2 -
        2 * c ν * (∂_ ν A x (Sum.inl 0)))) + 1/(2 * 𝓕.μ₀) * c (Sum.inl 0) ^2)
```

## B. Variational gradient of the kinetic term

> We define the variational gradient of the kinetic term, which is the left-hand side
> of Gauss's law and Ampère's law in vacuum.

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm`**, a def, [line 377](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L377).

> The variational gradient of the kinetic term of an electromagnetic potential.

```lean
noncomputable def gradKineticTerm {d} (𝓕 : FreeSpace) (A : ElectromagneticPotential d) :
    SpaceTime d → Lorentz.Vector d
```

### B.1. Variational gradient in terms of fderiv

> We give a first simplification of the variational gradient in terms of the
> a complicated expression involving `fderiv`. This is not very useful in itself,
> but acts as a starting point for further simplifications.

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_sum_fderiv`**, a lemma, [line 390](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L390).

```lean
lemma gradKineticTerm_eq_sum_fderiv {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) :
    let F' : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d) → (SpaceTime d → ℝ) →
    SpaceTime d → Lorentz.Vector d := fun μν => (fun ψ x =>
    -(fderiv ℝ (fun x' => (fun x' => η μν.1 μν.1 * η μν.2 μν.2 * ψ x') x' * ∂_ μν.1 A x' μν.2) x)
              (Lorentz.Vector.basis μν.1) •
          Lorentz.Vector.basis μν.2 +
        -(fderiv ℝ (fun x' => ∂_ μν.1 A x' μν.2 *
          (fun x' => η μν.1 μν.1 * η μν.2 μν.2 * ψ x') x') x)
              (Lorentz.Vector.basis μν.1) • Lorentz.Vector.basis μν.2 +
      -(-(fderiv ℝ (fun x' => ψ x' * ∂_ μν.2 A x' μν.1) x) (Lorentz.Vector.basis μν.1) •
        Lorentz.Vector.basis μν.2 +
          -(fderiv ℝ (fun x' => ∂_ μν.1 A x' μν.2 * ψ x') x) (Lorentz.Vector.basis μν.2) •
          Lorentz.Vector.basis μν.1))
    A.gradKineticTerm 𝓕 = fun x => ∑ μν, F' μν (fun x' => -1/(2 * 𝓕.μ₀) * (fun _ => 1) x') x
```

### B.2. Writing the variational gradient as a sums over double derivatives of the potential

> We rewrite the variational gradient as a simple double sum over
> second derivatives of the potential.

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_sum_sum`**, a lemma, [line 441](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L441).

```lean
lemma gradKineticTerm_eq_sum_sum {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (x : SpaceTime d) (ha : ContDiff ℝ ∞ A) :
    A.gradKineticTerm 𝓕 x = ∑ (ν : (Fin 1 ⊕ Fin d)), ∑ (μ : (Fin 1 ⊕ Fin d)),
        (1 / (𝓕.μ₀) * (η μ μ * η ν ν * ∂_ μ (fun x' => ∂_ μ A x' ν) x -
        ∂_ μ (fun x' => ∂_ ν A x' μ) x)) • Lorentz.Vector.basis ν
```

### B.3. Variational gradient as sums over the components of the field strength tensor

> We rewrite the variational gradient as a simple double sum over the
> components of the field strength tensor.

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_fieldStrength`**, a lemma, [line 502](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L502).

```lean
lemma gradKineticTerm_eq_fieldStrength {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (ha : ContDiff ℝ ∞ A) :
    A.gradKineticTerm 𝓕 x = ∑ (ν : (Fin 1 ⊕ Fin d)), (1/𝓕.μ₀ * η ν ν) •
    (∑ (μ : (Fin 1 ⊕ Fin d)), (∂_ μ (fun x => toScalar {A.toFieldStrength x | [μ] [ν]}ᵀ) x))
    • Lorentz.Vector.basis ν
```

### B.4. Variational gradient in terms of the Gauss's and Ampère laws

> We rewrite the variational gradient in terms of the electric and magnetic fields,
> explicitly relating it to Gauss's law and Ampère's law.

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_electric_magnetic`**, a lemma, [line 546](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L546).

```lean
lemma gradKineticTerm_eq_electric_magnetic {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (ha : ContDiff ℝ ∞ A) :
    A.gradKineticTerm 𝓕 x =
    (1/(𝓕.μ₀ * 𝓕.c) * Space.div (A.electricField 𝓕.c (x.time 𝓕.c)) x.space) •
    Lorentz.Vector.basis (Sum.inl 0) +
    ∑ i, (𝓕.μ₀⁻¹ * (1 / 𝓕.c ^ 2 * ∂ₜ (fun t => A.electricField 𝓕.c t x.space) (x.time 𝓕.c) i-
      ∑ j, Space.deriv j (A.magneticFieldMatrix 𝓕.c (x.time 𝓕.c) · (j, i)) x.space)) •
      Lorentz.Vector.basis (Sum.inr i)
```

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_electric_magnetic_three`**, a lemma, [line 571](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L571).

```lean
lemma gradKineticTerm_eq_electric_magnetic_three {𝓕 : FreeSpace} (A : ElectromagneticPotential)
    (x : SpaceTime) (ha : ContDiff ℝ ∞ A) :
    A.gradKineticTerm 𝓕 x =
    (1/(𝓕.μ₀ * 𝓕.c) * Space.div (A.electricField 𝓕.c (x.time 𝓕.c)) x.space) •
      Lorentz.Vector.basis (Sum.inl 0) +
    ∑ i, (𝓕.μ₀⁻¹ * (1 / 𝓕.c ^ 2 * ∂ₜ (fun t => A.electricField 𝓕.c t x.space) (x.time 𝓕.c) i-
      Space.curl (A.magneticField 𝓕.c (x.time 𝓕.c)) x.space i)) •
      Lorentz.Vector.basis (Sum.inr i)
```

### B.5. Linearity properties of the variational gradient

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_add`**, a lemma, [line 587](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L587).

```lean
lemma gradKineticTerm_add {d} {𝓕 : FreeSpace} (A1 A2 : ElectromagneticPotential d)
    (hA1 : ContDiff ℝ ∞ A1) (hA2 : ContDiff ℝ ∞ A2) :
    (A1 + A2).gradKineticTerm 𝓕 = A1.gradKineticTerm 𝓕 + A2.gradKineticTerm 𝓕
```

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_smul`**, a lemma, [line 609](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L609).

```lean
lemma gradKineticTerm_smul {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) (c : ℝ) :
    (c • A).gradKineticTerm 𝓕 = c • A.gradKineticTerm 𝓕
```

### B.6. HasVarGradientAt for the variational gradient

**`Electromagnetism.ElectromagneticPotential.kineticTerm_hasVarGradientAt`**, a lemma, [line 641](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L641).

```lean
lemma kineticTerm_hasVarGradientAt {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ ∞ A) :
    HasVarGradientAt (fun A => kineticTerm 𝓕 ⟨A⟩) (A.gradKineticTerm 𝓕) A
```

### B.7. Gradient of the kinetic term in terms of the tensor derivative

**`Electromagnetism.ElectromagneticPotential.gradKineticTerm_eq_tensorDeriv`**, a lemma, [line 679](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean#L679).

```lean
lemma gradKineticTerm_eq_tensorDeriv {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (x : SpaceTime d)
    (hA : ContDiff ℝ ∞ A) (ν : Fin 1 ⊕ Fin d) :
    A.gradKineticTerm 𝓕 x ν = η ν ν * ((Tensorial.toTensor (M := Lorentz.Vector d)).symm
    (permT id (IsReindexing.auto) {(1/ 𝓕.μ₀ : ℝ) •
      tensorDeriv A.toFieldStrength x | κ κ ν'}ᵀ)) ν
```

## Depends on

- [Free space](basic.md)
- [The Magnetic Field](../kinematics/magneticfield.md)
- [Variational gradient](../../mathematics/variationalcalculus/hasvargradient.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/KineticTerm.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/KineticTerm.lean)
