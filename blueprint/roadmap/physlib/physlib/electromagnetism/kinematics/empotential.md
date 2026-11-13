---
declaration: module
origin: cited
lean: Electromagnetism.ElectromagneticPotential, Electromagnetism.ElectromagneticPotential.eq_of_val_eq, Electromagnetism.ElectromagneticPotential.zero_val, Electromagnetism.ElectromagneticPotential.zero_apply, Electromagnetism.ElectromagneticPotential.add_val, Electromagnetism.ElectromagneticPotential.add_apply, Electromagnetism.ElectromagneticPotential.neg_val, Electromagnetism.ElectromagneticPotential.neg_apply
statement: formalized
proof: formalized
---

# The Electromagnetic Potential (EMPotential)

The module `Physlib.Electromagnetism.Kinematics.EMPotential`, [Physlib/Electromagnetism/Kinematics/EMPotential.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean): 59 declarations (10 instances with no name), 14 with a docstring.

## i. Overview

> The electromagnetic potential `A^μ` is the fundamental objects in
> electromagnetism. Mathematically it is related to a connection
> on a `U(1)`-bundle.
>
> We define the electromagnetic potential as a function from
> spacetime to contravariant Lorentz vectors.

## ii. Key results

> - `ElectromagneticPotential` : is the type of electromagnetic potentials.
> - `ElectromagneticPotential.deriv` : the derivative tensor `∂_μ A^ν`.
> - `ElectromagneticPotential.contDiff_deriv_deriv_component` : the second derivatives
>   `∂_μ ∂_ν A^ρ` are `C^n` if the potential is `C^{n+2}`.
> - `ElectromagneticPotential.contDiff_deriv` : the derivative tensor is `C^n` if the potential
>   is `C^{n+1}`.

## iv. References

> * https://quantummechanics.ucsd.edu/ph130a/130\_notes/node452.html. [ref: ucsd\_ph130a\_node452]
> * https://ph.qmul.ac.uk/sites/default/files/EMT10new.pdf. [ref: qmul\_emt10\_notes]

## A. The electromagnetic potential

> We define the electromagnetic potential as a function from spacetime to
> contravariant Lorentz vectors, and prove some simple results about it.

**`Electromagnetism.ElectromagneticPotential`**, a structure, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L72).

> The electromagnetic potential is a tensor `A^μ`.

```lean
structure ElectromagneticPotential (d : ℕ := 3) where
  /-- The underlying map from `SpaceTime d` to `Lorentz.Vector d` associated
    with an electromagnetic potential. -/
  val : SpaceTime d → Lorentz.Vector d
```

**`Electromagnetism.ElectromagneticPotential.eq_of_val_eq`**, a lemma, [line 88](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L88).

```lean
lemma eq_of_val_eq (A B : ElectromagneticPotential d) (h : A.val = B.val) : A = B
```

## A.1. Basic instances on the type of electromagnetic potentials

**An instance with no name**, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L97).

```lean
instance {d} : CoeFun (ElectromagneticPotential d)
    (fun _ => SpaceTime d → Lorentz.Vector d)
```

**An instance with no name**, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L101).

```lean
instance {d} : Zero (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.zero_val`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L105).

```lean
lemma zero_val {d} : (0 : ElectromagneticPotential d).val = 0
```

**`Electromagnetism.ElectromagneticPotential.zero_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L108).

```lean
lemma zero_apply {d} (x : SpaceTime d) : (0 : ElectromagneticPotential d) x = 0
```

**An instance with no name**, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L110).

```lean
instance {d} : Add (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.add_val`**, a lemma, [line 114](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L114).

```lean
lemma add_val {d} (A B : ElectromagneticPotential d) :
    (A + B).val = A.val + B.val
```

**`Electromagnetism.ElectromagneticPotential.add_apply`**, a lemma, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L118).

```lean
lemma add_apply {d} (A B : ElectromagneticPotential d) (x : SpaceTime d) :
    (A + B) x = A x + B x
```

**An instance with no name**, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L121).

```lean
instance {d} : Neg (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.neg_val`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L125).

```lean
lemma neg_val {d} (A : ElectromagneticPotential d) :
    (- A).val = - A.val
```

**`Electromagnetism.ElectromagneticPotential.neg_apply`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L129).

```lean
lemma neg_apply {d} (A : ElectromagneticPotential d) (x : SpaceTime d) :
    (- A) x = - A x
```

**An instance with no name**, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L132).

```lean
instance {d} : Sub (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.sub_val`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L136).

```lean
lemma sub_val {d} (A B : ElectromagneticPotential d) :
    (A - B).val = A.val - B.val
```

**`Electromagnetism.ElectromagneticPotential.sub_apply`**, a lemma, [line 140](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L140).

```lean
lemma sub_apply {d} (A B : ElectromagneticPotential d) (x : SpaceTime d) :
    (A - B) x = A x - B x
```

**An instance with no name**, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L143).

```lean
instance {d} : AddCommGroup (ElectromagneticPotential d)
```

**An instance with no name**, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L162).

```lean
noncomputable instance {d} : SMul ℝ (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.smul_val`**, a lemma, [line 166](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L166).

```lean
lemma smul_val {d} (r : ℝ) (A : ElectromagneticPotential d) :
    (r • A).val = r • A.val
```

**`Electromagnetism.ElectromagneticPotential.smul_apply`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L170).

```lean
lemma smul_apply {d} (r : ℝ) (A : ElectromagneticPotential d) (x : SpaceTime d) :
    (r • A) x = r • A x
```

## A.2. Basic constructors of the electromagnetic potential

**`Electromagnetism.ElectromagneticPotential.ofScalarPotential`**, a def, [line 181](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L181).

> The electromagnetic potential from a scalar potential, where
> the vector potential is set to zero.

```lean
noncomputable def ofScalarPotential {d} (c : SpeedOfLight)
    (ϕ : Time → Space d → ℝ) : ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofStaticScalarPotential`**, a def, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L189).

> The creation of an electromagnetic potential from a static scalar potential.

```lean
noncomputable def ofStaticScalarPotential {d} (c : SpeedOfLight)
    (ϕ : Space d → ℝ) : ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofVectorPotential`**, a def, [line 195](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L195).

> The electromagnetic potential from a vector potential, where
> the scalar potential is set equal to zero.

```lean
noncomputable def ofVectorPotential {d} (c : SpeedOfLight)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofStaticVectorPotential`**, a def, [line 204](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L204).

> The creation of an electromagnetic potential from a static vector potential.

```lean
noncomputable def ofStaticVectorPotential {d} (c : SpeedOfLight)
    (A : Space d → EuclideanSpace ℝ (Fin d)) : ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofPotentials`**, a def, [line 209](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L209).

> The creation of an electromagnetic potential from the non-relativistic potentials.

```lean
noncomputable def ofPotentials {d} (c : SpeedOfLight) (ϕ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofPotentials_eq_add`**, a lemma, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L217).

```lean
lemma ofPotentials_eq_add {d} (c : SpeedOfLight) (ϕ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) :
    ofPotentials c ϕ A = ofScalarPotential c ϕ + ofVectorPotential c A
```

**`Electromagnetism.ElectromagneticPotential.ofStaticPotentials`**, a def, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L227).

> The creation of of an electromagnetic potential from static potentials.

```lean
noncomputable def ofStaticPotentials {d} (c : SpeedOfLight) (ϕ : Space d → ℝ)
    (A : Space d → EuclideanSpace ℝ (Fin d)) : ElectromagneticPotential d
```

**`Electromagnetism.ElectromagneticPotential.ofStaticPotentials_eq_ofPotentials`**, a lemma, [line 231](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L231).

```lean
lemma ofStaticPotentials_eq_ofPotentials {d} (c : SpeedOfLight) (ϕ : Space d → ℝ)
    (A : Space d → EuclideanSpace ℝ (Fin d)) :
    ofStaticPotentials c ϕ A = ofPotentials c (fun _ => ϕ) (fun _ => A)
```

**`Electromagnetism.ElectromagneticPotential.ofElectromagneticField`**, a def, [line 239](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L239).

> The electromagnetic potential from an electric and a magnetic field.
> This defines the electromagnetic potential in the Poincare gauge.

```lean
noncomputable def ofElectromagneticField (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) :
    ElectromagneticPotential 3
```

## A.3. The group action on the ElectromagneticPotential

**An instance with no name**, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L256).

```lean
noncomputable instance {d} : SMul (LorentzGroup d) (ElectromagneticPotential d)
```

**`Electromagnetism.ElectromagneticPotential.action_val`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L259).

```lean
lemma action_val {d} (Λ : LorentzGroup d) (A : ElectromagneticPotential d) :
    (Λ • A).val = fun x => Λ • A (Λ⁻¹ • x)
```

**`Electromagnetism.ElectromagneticPotential.action_apply`**, a lemma, [line 263](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L263).

```lean
lemma action_apply {d} (Λ : LorentzGroup d) (A : ElectromagneticPotential d)
    (x : SpaceTime d) :
    (Λ • A) x = Λ • A (Λ⁻¹ • x)
```

**An instance with no name**, [line 267](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L267).

```lean
noncomputable instance {d} : MulAction (LorentzGroup d) (ElectromagneticPotential d)
```

**An instance with no name**, [line 275](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L275).

```lean
noncomputable instance {d} :
    DistribMulAction (LorentzGroup d) (ElectromagneticPotential d)
```

### A.4. Differentiability

> We show that the potential and its derivatives are differentiable (or smooth) if the potential
> is, in the forms `fun_prop` cannot derive on its own. Differentiability of a component
> `fun x => A x μ` of a differentiable potential is found by `fun_prop` directly.

**`Electromagnetism.ElectromagneticPotential.differentiable_action`**, a lemma, [line 296](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L296).

```lean
lemma differentiable_action {d} (Λ : LorentzGroup d) (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) : Differentiable ℝ (fun x => Λ • A (Λ⁻¹ • x))
```

**`Electromagnetism.ElectromagneticPotential.contDiff_action`**, a lemma, [line 302](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L302).

```lean
lemma contDiff_action {d} (Λ : LorentzGroup d) (A : ElectromagneticPotential d)
    (hA : ContDiff ℝ n A) : ContDiff ℝ n (fun x => Λ • A (Λ⁻¹ • x))
```

**`Electromagnetism.ElectromagneticPotential.differentiable_deriv_component_of_smooth`**, a lemma, [line 308](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L308).

```lean
lemma differentiable_deriv_component_of_smooth {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ ∞ A) (μ ν : Fin 1 ⊕ Fin d) :
    Differentiable ℝ (fun x => ∂_ μ A x ν)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_deriv_component_of_smooth`**, a lemma, [line 315](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L315).

```lean
lemma contDiff_deriv_component_of_smooth {n : ℕ} {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ ∞ A) (μ ν : Fin 1 ⊕ Fin d) :
    ContDiff ℝ n (fun x => ∂_ μ A x ν)
```

#### A.4.1. Differentiability of the derivative of the potential

> The derivatives `∂_ μ A x ν` of the potential are `C^n` if the potential is `C^{n+2}`.
> This is what is needed to make sense of second derivatives of the potential, as appear for
> example in Maxwell's equations. Differentiability for a `C^3` potential follows by `fun_prop`
> from these lemmas and `SpaceTime.differentiable_deriv`, so is not stated separately.
>
> A second derivative of a component can be written in two ways: as `∂_ μ (fun x => ∂_ ν A x ρ) x`,
> the derivative of the real-valued component `∂_ ν A x ρ` (the `_component` lemmas), or as
> `∂_ μ (∂_ ν A) x ρ`, the component of the derivative of the vector-valued `∂_ ν A`
> (the `_apply` lemmas). The two agree for a `C^2` potential by `SpaceTime.deriv_apply_eq`.
>
> The differentiability of the first-derivative components `∂_ μ A x ν` for a `C^2` (or
> `C^{n+1}`) potential is found by `fun_prop` directly, so only the smooth variants are stated.

**`Electromagnetism.ElectromagneticPotential.contDiff_deriv_deriv_component`**, a lemma, [line 342](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L342).

> The second derivatives `∂_ μ ∂_ ν A^ρ` of a `C^{n+2}` potential are `C^n`.

```lean
lemma contDiff_deriv_deriv_component {n} {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ (n + 2) A) (μ ν ρ : Fin 1 ⊕ Fin d) :
    ContDiff ℝ n (fun x => ∂_ μ (fun x => ∂_ ν A x ρ) x)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_deriv_deriv_apply`**, a lemma, [line 350](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L350).

> The `ρ` component of `∂_ μ (∂_ ν A)` is `C^n` for a `C^{n+2}` potential.

```lean
lemma contDiff_deriv_deriv_apply {n} {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ (n + 2) A) (μ ν ρ : Fin 1 ⊕ Fin d) :
    ContDiff ℝ n (fun x => ∂_ μ (∂_ ν A) x ρ)
```

**`Electromagnetism.ElectromagneticPotential.differentiable_deriv_deriv_apply_of_smooth`**, a lemma, [line 360](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L360).

```lean
lemma differentiable_deriv_deriv_apply_of_smooth {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ ∞ A) (μ ν ρ : Fin 1 ⊕ Fin d) :
    Differentiable ℝ (fun x => ∂_ μ (∂_ ν A) x ρ)
```

### A.5. Differentiability in terms of constructors

**`Electromagnetism.ElectromagneticPotential.differentiable_ofScalarPotential`**, a lemma, [line 372](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L372).

```lean
lemma differentiable_ofScalarPotential {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (hϕ : Differentiable ℝ ↿φ) : Differentiable ℝ (ofScalarPotential c φ)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_ofScalarPotential`**, a lemma, [line 380](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L380).

```lean
lemma contDiff_ofScalarPotential {n} {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (hϕ : ContDiff ℝ n ↿φ) : ContDiff ℝ n (ofScalarPotential c φ)
```

**`Electromagnetism.ElectromagneticPotential.differentiable_ofVectorPotential`**, a lemma, [line 388](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L388).

```lean
lemma differentiable_ofVectorPotential {d} (c : SpeedOfLight)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d))
    (hA : Differentiable ℝ ↿A) : Differentiable ℝ (ofVectorPotential c A)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_ofVectorPotential`**, a lemma, [line 397](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L397).

```lean
lemma contDiff_ofVectorPotential {n} {d} (c : SpeedOfLight)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d))
    (hA : ContDiff ℝ n ↿A) : ContDiff ℝ n (ofVectorPotential c A)
```

**`Electromagnetism.ElectromagneticPotential.differentiable_ofPotentials`**, a lemma, [line 406](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L406).

```lean
lemma differentiable_ofPotentials {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) (hϕ : Differentiable ℝ ↿φ)
    (hA : Differentiable ℝ ↿A) : Differentiable ℝ (ofPotentials c φ A)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_ofPotentials`**, a lemma, [line 415](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L415).

```lean
lemma contDiff_ofPotentials {n} {d} (c : SpeedOfLight) (φ : Time → Space d → ℝ)
    (A : Time → Space d → EuclideanSpace ℝ (Fin d)) (hϕ : ContDiff ℝ n ↿φ)
    (hA : ContDiff ℝ n ↿A) : ContDiff ℝ n (ofPotentials c φ A)
```

**`Electromagnetism.ElectromagneticPotential.contDiff_ofElectromagneticField`**, a lemma, [line 425](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L425).

```lean
lemma contDiff_ofElectromagneticField {n : ℕ} (c : SpeedOfLight)
    (E : Time → Space 3 → EuclideanSpace ℝ (Fin 3))
    (B : Time → Space 3 → EuclideanSpace ℝ (Fin 3)) (hE : ContDiff ℝ n ↿E)
    (hB : ContDiff ℝ n ↿B) : ContDiff ℝ n (ofElectromagneticField c E B)
```

### A.6. The action on the space-time derivatives

> Given a ElectromagneticPotential `A^μ`, we can consider its derivative `∂_μ A^ν`.
> Under a Lorentz transformation `Λ`, this transforms as
> `∂_ μ (Λ • A)`, we write an expression for this in terms of the tensor.
> `∂_ ρ A (Λ⁻¹ • x) κ`.

**`Electromagnetism.ElectromagneticPotential.spaceTime_deriv_action_eq_sum`**, a lemma, [line 473](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L473).

```lean
lemma spaceTime_deriv_action_eq_sum {d} {μ ν : Fin 1 ⊕ Fin d} {x : SpaceTime d}
    (Λ : LorentzGroup d) (A : ElectromagneticPotential d) (hA : Differentiable ℝ A) :
    ∂_ μ (Λ • A) x ν = ∑ κ, ∑ ρ, (Λ.1 ν κ * Λ⁻¹.1 ρ μ) * ∂_ ρ A (Λ⁻¹ • x) κ
```

### A.7. Variational adjoint derivative of component

> We find the variational adjoint derivative of the components of the potential.
> This will be used to find e.g. the variational derivative of the kinetic term,
> and derive the equations of motion.

**`Electromagnetism.ElectromagneticPotential.hasVarAdjDerivAt_component`**, a lemma, [line 494](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L494).

```lean
lemma hasVarAdjDerivAt_component {d : ℕ} (μ : Fin 1 ⊕ Fin d) (A : SpaceTime d → Lorentz.Vector d)
    (hA : ContDiff ℝ ∞ A) :
        HasVarAdjDerivAt (fun (A' : SpaceTime d → Lorentz.Vector d) x => A' x μ)
          (fun (A' : SpaceTime d → ℝ) x => A' x • Lorentz.Vector.basis μ) A
```

### A.8. Variational adjoint derivative of derivatives of the potential

> We find the variational adjoint derivative of the derivatives of the components of the potential.
> This will again be used to find the variational derivative of the kinetic term,
> and derive the equations of motion (Maxwell's equations).

**`Electromagnetism.ElectromagneticPotential.deriv_hasVarAdjDerivAt`**, a lemma, [line 523](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L523).

```lean
lemma deriv_hasVarAdjDerivAt {d} (μ ν : Fin 1 ⊕ Fin d) (A : SpaceTime d → Lorentz.Vector d)
    (hA : ContDiff ℝ ∞ A) :
    HasVarAdjDerivAt (fun (A : SpaceTime d → Lorentz.Vector d) x => ∂_ μ A x ν)
      (fun ψ x => - (fderiv ℝ ψ x) (Lorentz.Vector.basis μ) • Lorentz.Vector.basis ν) A
```

## B. The derivative tensor of the electromagnetic potential

> We define the derivative as a tensor in `Lorentz.CoVector ⊗[ℝ] Lorentz.Vector` for the
> electromagnetic potential `A^μ`. We then prove that this tensor transforms correctly
> under Lorentz transformations.

**`Electromagnetism.ElectromagneticPotential.deriv`**, a def, [line 547](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L547).

> The derivative of the electric potential, `∂_μ A^ν`.

```lean
noncomputable def deriv {d} (A : ElectromagneticPotential d) :
    SpaceTime d → Lorentz.CoVector d ⊗[ℝ] Lorentz.Vector d
```

**`Electromagnetism.ElectromagneticPotential.deriv_eq_tensorDeriv`**, a lemma, [line 551](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L551).

```lean
lemma deriv_eq_tensorDeriv {d} (A : ElectromagneticPotential d)
    (hA : Differentiable ℝ A) (x : SpaceTime d) :
    A.deriv x = tensorDeriv A.val x
```

### B.1. Equivariance of the derivative tensor

> We show that the derivative tensor is equivariant under the action of the Lorentz group.
> That is, `∂_μ (fun x => Λ • A (Λ⁻¹ • x)) = Λ • (∂_μ A (Λ⁻¹ • x))`, or in words:
> applying the Lorentz transformation to the potential and then taking the derivative is the same
> as taking the derivative and then applying the Lorentz transformation to the resulting tensor.

**`Electromagnetism.ElectromagneticPotential.deriv_equivariant`**, a lemma, [line 585](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L585).

```lean
lemma deriv_equivariant {d} {x : SpaceTime d} (A : ElectromagneticPotential d)
    (Λ : LorentzGroup d)
    (hf : Differentiable ℝ A) : deriv (Λ • A) x = Λ • (deriv A (Λ⁻¹ • x))
```

### B.2. The elements of the derivative tensor in terms of the basis

> We show that in the standard basis, the elements of the derivative tensor
> are just equal to `∂_ μ A x ν`.

**`Electromagnetism.ElectromagneticPotential.tensorDeriv_eval_eq`**, a lemma, [line 602](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L602).

> Evaluation of the tensor components of `∂_ μ A x ν`.

```lean
lemma tensorDeriv_eval_eq {d} {A : ElectromagneticPotential d} (hA : Differentiable ℝ A)
    (x : SpaceTime d) (μ ν : Fin 1 ⊕ Fin d) :
    toScalar {tensorDeriv A.val x | [μ] [ν]}ᵀ = ∂_ μ A x ν
```

**`Electromagnetism.ElectromagneticPotential.deriv_basis_repr_apply`**, a lemma, [line 632](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L632).

```lean
lemma deriv_basis_repr_apply {d} {μν : (Fin 1 ⊕ Fin d) × (Fin 1 ⊕ Fin d)}
    (A : ElectromagneticPotential d)
    (x : SpaceTime d) :
    (Lorentz.CoVector.basis.tensorProduct Lorentz.Vector.basis).repr (deriv A x) μν =
    ∂_ μν.1 A x μν.2
```

**`Electromagnetism.ElectromagneticPotential.toTensor_deriv_basis_repr_apply`**, a lemma, [line 640](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L640).

```lean
lemma toTensor_deriv_basis_repr_apply {d} (A : ElectromagneticPotential d)
    (x : SpaceTime d) (b : ComponentIdx (S := realLorentzTensor d)
      (Fin.append ![Color.down] ![Color.up])) :
    (Tensor.basis _).repr (Tensorial.toTensor (deriv A x)) b =
    ∂_ (b 0) A x (b 1)
```

### B.3. Differentiability of the derivative tensor

> We show that the derivative tensor `∂_μ A^ν`, as a function on spacetime, is differentiable
> (or `C^n`) if the potential is `C^2` (or `C^{n+1}`).

**`Electromagnetism.ElectromagneticPotential.differentiable_deriv`**, a lemma, [line 670](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L670).

> The derivative tensor of a `C^2` potential is differentiable.

```lean
lemma differentiable_deriv {d} {A : ElectromagneticPotential d} (hA : ContDiff ℝ 2 A) :
    Differentiable ℝ A.deriv
```

**`Electromagnetism.ElectromagneticPotential.differentiable_deriv_of_smooth`**, a lemma, [line 676](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L676).

```lean
lemma differentiable_deriv_of_smooth {d} {A : ElectromagneticPotential d}
    (hA : ContDiff ℝ ∞ A) : Differentiable ℝ A.deriv
```

**`Electromagnetism.ElectromagneticPotential.contDiff_deriv`**, a lemma, [line 682](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean#L682).

> The derivative tensor of a `C^{n+1}` potential is `C^n`.

```lean
lemma contDiff_deriv {n} {d} {A : ElectromagneticPotential d} (hA : ContDiff ℝ (n + 1) A) :
    ContDiff ℝ n A.deriv
```

## Depends on

- [Variational adjoint derivative](../../mathematics/variationalcalculus/hasvaradjderiv.md)
- [Time slice](../../spaceandtime/spacetime/timeslice.md)

## Proof depends on

- [Parametric Integration](../../mathematics/calculus/parametricintegration.md)

## Sources

- [Physlib/Electromagnetism/Kinematics/EMPotential.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Electromagnetism/Kinematics/EMPotential.lean)
