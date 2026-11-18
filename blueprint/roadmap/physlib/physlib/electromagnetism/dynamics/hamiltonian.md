---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential.canonicalMomentum, Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq_gradient_kineticTerm, Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq, Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq_electricField, Electromagnetism.ElectromagneticPotential.hamiltonian, Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_vectorPotential, Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_scalarPotential, Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_magneticField
statement: formalized
proof: formalized
---

# The Hamiltonian in electromagnetism

The module `Physlib.Electromagnetism.Dynamics.Hamiltonian`, [Physlib/Electromagnetism/Dynamics/Hamiltonian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean): 8 declarations, 2 with a docstring.

## i. Overview

> In this module we define the canonical momentum and the Hamiltonian for the
> electromagnetic field in presence of a current density. We prove properties of these
> quantities, and express the Hamiltonian in terms of the electric and magnetic fields
> in the case of three spatial dimensions.

## ii. Key results

> - `canonicalMomentum` : The canonical momentum for the electromagnetic field in presence of a
>   Lorentz current density.
> - `hamiltonian` : The Hamiltonian for the electromagnetic field in presence of a
>   Lorentz current density.
> - `hamiltonian_eq_electricField_magneticField` : The Hamiltonian expressed
>   in terms of the electric and magnetic fields.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]
> * https://ph.qmul.ac.uk/sites/default/files/EMT10new.pdf. [ref: qmul\_emt10\_notes]

## A. The canonical momentum

> We define the canonical momentum for the lagrangian
> `L(A, ∂ A)` as gradient of `v ↦ L(A + t v, ∂ (A + t v)) - t * L(A + v, ∂(A + v))` at `v = 0`
> This is equivalent to `∂ L/∂ (∂_0 A)`.

**`Electromagnetism.ElectromagneticPotential.canonicalMomentum`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L78).

> The canonical momentum associated with the lagrangian of an electromagnetic potential
> and a Lorentz current density.

```lean
noncomputable def canonicalMomentum (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) :
    SpaceTime d → Lorentz.Vector d
```

### A.1. The canonical momentum in terms of the kinetic term

**`Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq_gradient_kineticTerm`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L91).

```lean
lemma canonicalMomentum_eq_gradient_kineticTerm {d}
    {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (J : LorentzCurrentDensity d) :
    A.canonicalMomentum 𝓕 J = fun x =>
    gradient (fun (v : Lorentz.Vector d) =>
    kineticTerm 𝓕 ⟨fun x => A x + x (Sum.inl 0) • v⟩ x) 0
```

### A.2. The canonical momentum in terms of the field strength tensor

**`Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L129).

```lean
lemma canonicalMomentum_eq {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (J : LorentzCurrentDensity d) :
    A.canonicalMomentum 𝓕 J = fun x => fun μ =>
      (1/𝓕.μ₀) * η μ μ • toScalar {A.toFieldStrength x | [μ] [Sum.inl 0]}ᵀ
```

### A.3. The canonical momentum in terms of the electric field

**`Electromagnetism.ElectromagneticPotential.canonicalMomentum_eq_electricField`**, a lemma, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L159).

```lean
lemma canonicalMomentum_eq_electricField {d} {𝓕 : FreeSpace} (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (J : LorentzCurrentDensity d) :
    A.canonicalMomentum 𝓕 J = fun x => fun μ =>
      match μ with
      | Sum.inl 0 => 0
      | Sum.inr i => - (1/(𝓕.μ₀ * 𝓕.c)) * A.electricField 𝓕.c (x.time 𝓕.c) x.space i
```

## B. The Hamiltonian

**`Electromagnetism.ElectromagneticPotential.hamiltonian`**, a def, [line 184](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L184).

> The Hamiltonian associated with an electromagnetic potential
> and a Lorentz current density.

```lean
noncomputable def hamiltonian (𝓕 : FreeSpace) (A : ElectromagneticPotential d)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) : ℝ
```

### B.1. The hamiltonian in terms of the vector potential

**`Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_vectorPotential`**, a lemma, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L195).

```lean
lemma hamiltonian_eq_electricField_vectorPotential {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (hA : ContDiff ℝ 2 A)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) :
    A.hamiltonian 𝓕 J x =
      - (1/ 𝓕.c.val^2 * 𝓕.μ₀⁻¹) * ∑ i, A.electricField 𝓕.c (x.time 𝓕.c) x.space i *
      (∂ₜ (A.vectorPotential 𝓕.c · x.space) (x.time 𝓕.c) i) - lagrangian 𝓕 A J x
```

**`Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_scalarPotential`**, a lemma, [line 218](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L218).

```lean
lemma hamiltonian_eq_electricField_scalarPotential {d} {𝓕 : FreeSpace}
    (A : ElectromagneticPotential d) (hA : ContDiff ℝ 2 A)
    (J : LorentzCurrentDensity d) (x : SpaceTime d) :
    A.hamiltonian 𝓕 J x =
      (1/ 𝓕.c.val^2 * 𝓕.μ₀⁻¹) * (‖A.electricField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2
      + ⟪A.electricField 𝓕.c (x.time 𝓕.c) x.space,
        Space.grad (A.scalarPotential 𝓕.c (x.time 𝓕.c) ·) x.space⟫_ℝ)
        - lagrangian 𝓕 A J x
```

### B.2. The hamiltonian in terms of the electric and magnetic fields

**`Electromagnetism.ElectromagneticPotential.hamiltonian_eq_electricField_magneticField`**, a lemma, [line 247](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean#L247).

```lean
lemma hamiltonian_eq_electricField_magneticField (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ 2 A) (J : LorentzCurrentDensity d) (x : SpaceTime d) :
    A.hamiltonian 𝓕 J x = 1/2 * 𝓕.ε₀ * (‖A.electricField 𝓕.c (x.time 𝓕.c) x.space‖ ^ 2
      + 𝓕.c ^ 2 / 2 * ∑ i, ∑ j, ‖A.magneticFieldMatrix 𝓕.c (x.time 𝓕.c) x.space (i, j)‖ ^ 2)
      + 𝓕.ε₀ * ⟪A.electricField 𝓕.c (x.time 𝓕.c) x.space,
        Space.grad (A.scalarPotential 𝓕.c (x.time 𝓕.c) ·) x.space⟫_ℝ
      + A.scalarPotential 𝓕.c (x.time 𝓕.c) x.space * J.chargeDensity 𝓕.c (x.time 𝓕.c) x.space
      - ∑ i, A.vectorPotential 𝓕.c (x.time 𝓕.c) x.space i *
        J.currentDensity 𝓕.c (x.time 𝓕.c) x.space i
```

## Depends on

- [The Lagrangian in electromagnetism (Electromagnetism/Dynamics/Lagrangian)](lagrangian.md)

## Sources

- [Physlib/Electromagnetism/Dynamics/Hamiltonian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Dynamics/Hamiltonian.lean)
