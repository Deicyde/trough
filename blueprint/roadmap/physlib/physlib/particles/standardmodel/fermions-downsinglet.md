---
declaration: module
origin: cited
lean: StandardModel.DownSinglet, StandardModel.DownSinglet.valEquiv, StandardModel.DownSinglet.valLinEquiv, StandardModel.DownSinglet.valLinEquiv_apply, StandardModel.DownSinglet.valLinEquiv_symm_apply, StandardModel.DownSinglet.val_add, StandardModel.DownSinglet.val_smul, StandardModel.DownSinglet.repLorentzGroup
statement: formalized
proof: formalized
---

# Down-type singlets

The module `Physlib.Particles.StandardModel.Fermions.DownSinglet`, [Physlib/Particles/StandardModel/Fermions/DownSinglet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean): 18 declarations (2 instances with no name), 12 with a docstring.

## i. Overview

> The Standard Model down-type singlet is a right-handed Weyl spinor in the `(3, 1)_{-2}`
> representation. Here charges are normalized as `6Y`, so `-2` is the usual hypercharge
> `Y = -1/3`.
>
> `DownSinglet` is the target vector space of one down-type quark multiplet. Its Weyl factor
> carries the Lorentz index and its three-dimensional factor carries the colour index. The absence
> of a weak factor makes it an `SU(2)` singlet.
>
> The Lorentz and gauge actions are first defined separately. The gauge action is then computed on a
> basis, used to identify its kernel, and descended to each supported global form of the Standard
> Model gauge group.

## ii. Key results

> - `DownSinglet` : the target space of the `(3, 1)_{-2}` multiplet.
> - `repLorentzGroup` : the right-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_tmul_basis_eq_sum` : the gauge action in a tensor-product basis.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.

## A. The down-singlet space

> The Weyl factor carries the right-handed Lorentz index, while
> `EuclideanSpace ℂ (Fin 3)` carries the colour index.

**`StandardModel.DownSinglet`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L65).

> The target vector space of one Standard Model down-type singlet quark.
> It carries the `(3, 1)_{-2}` representation of the gauge group.

```lean
structure DownSinglet where
  /-- The right-handed Weyl spinor with its colour index. -/
  val : Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

## B. Linear structure

> `DownSinglet` wraps its tensor-product carrier as a distinct type. The equivalences below identify
> the two types and transport the additive and complex module structures to `DownSinglet`.

**`StandardModel.DownSinglet.valEquiv`**, a def, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L80).

> Identifies a down-type singlet with its underlying tensor-product value.

```lean
def valEquiv : DownSinglet ≃ Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L84).

```lean
instance : AddCommGroup DownSinglet
```

**An instance with no name**, [line 86](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L86).

```lean
instance : Module ℂ DownSinglet
```

**`StandardModel.DownSinglet.valLinEquiv`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L89).

> The linear identification with the underlying tensor product.

```lean
def valLinEquiv : DownSinglet ≃ₗ[ℂ]
    Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

**`StandardModel.DownSinglet.valLinEquiv_apply`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L97).

```lean
lemma valLinEquiv_apply (d : DownSinglet) : valLinEquiv d = d.val
```

**`StandardModel.DownSinglet.valLinEquiv_symm_apply`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L99).

```lean
lemma valLinEquiv_symm_apply
    (m : Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)) :
    valLinEquiv.symm m = ⟨m⟩
```

**`StandardModel.DownSinglet.val_add`**, a lemma, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L104).

```lean
lemma val_add (d₁ d₂ : DownSinglet) : (d₁ + d₂).val = d₁.val + d₂.val
```

**`StandardModel.DownSinglet.val_smul`**, a lemma, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L107).

```lean
lemma val_smul (r : ℂ) (d : DownSinglet) : (r • d).val = r • d.val
```

## C. Lorentz action

> The Lorentz group acts on the right-handed Weyl factor and leaves the colour index fixed.

**`StandardModel.DownSinglet.repLorentzGroup`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L120).

> The right-handed Lorentz representation on down-type singlet quarks.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) DownSinglet
```

## D. Gauge action

> The `SU(3)` component acts on the colour index, while the `SU(2)` component acts trivially. The
> `U(1)` action is `star z ^ 2`; since `z` is unitary, `star z = z⁻¹`, so this represents charge
> `-2`.
>
> The tensor and basis formulas below expose the coefficients used to compare actions and compute the
> kernel.

**`StandardModel.DownSinglet.repGaugeGroupI`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L145).

> The `(3, 1)_{-2}` action of the unquotiented Standard Model gauge group.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI DownSinglet
```

**`StandardModel.DownSinglet.repGaugeGroupI_tmul`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L161).

> The gauge action on a pure spinor–colour tensor.

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (ψ : Fermion.RightHandedWeyl)
    (v : EuclideanSpace ℂ (Fin 3)) :
    repGaugeGroupI g ⟨ψ ⊗ₜ v⟩ =
      ⟨(star g.toU1.1 ^ 2) • ψ ⊗ₜ g.toSU3.1.toEuclideanLin v⟩
```

**`StandardModel.DownSinglet.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L168).

> Expands the gauge action in the spinor–colour basis.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k : Fin 2) (i : Fin 3) :
    repGaugeGroupI g
      ⟨RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ i⟩ =
      ∑ i' : Fin 3, (star g.toU1.1 ^ 2 * g.toSU3.1 i' i) •
        (⟨RightHandedWeyl.basis k ⊗ₜ[ℂ]
          EuclideanSpace.basisFun (Fin 3) ℂ i'⟩ : DownSinglet)
```

**`StandardModel.DownSinglet.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 190](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L190).

> Two gauge elements induce the same action exactly when their hypercharge–colour coefficients
> agree.

```lean
lemma repGaugeGroupI_eq_iff_mul_eq {g₁ g₂ : GaugeGroupI} :
    repGaugeGroupI g₁ = repGaugeGroupI g₂ ↔ ∀ i i',
      star g₁.toU1.1 ^ 2 * g₁.toSU3.1 i' i =
        star g₂.toU1.1 ^ 2 * g₂.toSU3.1 i' i
```

## E. Kernel of the gauge action

> An element acts trivially when its colour action is scalar and that scalar cancels its `U(1)`
> phase. Its weak component is unrestricted because the down-type singlet is an `SU(2)` singlet.

**`StandardModel.DownSinglet.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 228](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L228).

> Characterizes the full-group elements acting trivially on the down-type singlet.

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ ∃ a : ℂ,
      g.toSU3.1 = a • 1 ∧ a * star g.toU1.1 ^ 2 = 1
```

## F. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its kernel. For
> the central `ℤ₆`, the colour phase is `x²` while the charge `-2` phase is `(star x)² = x⁻²`, so
> their product is one.

**`StandardModel.DownSinglet.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 264](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L264).

> The central `ℤ₆` subgroup acts trivially on `(3, 1)_{-2}`.

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.DownSinglet.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 277](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L277).

> Every supported quotient subgroup acts trivially on the down-type singlet.

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.DownSinglet.repGaugeGroup`**, a def, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean#L283).

> The `(3, 1)_{-2}` representation for every supported global form of the
> Standard Model gauge group.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) DownSinglet
```

## Depends on

- [The Standard Model Gauge Group](gaugegroup/basic.md)
- [Right handed Weyl fermions](../../relativity/fermions/weyl/righthanded.md)

## Sources

- [Physlib/Particles/StandardModel/Fermions/DownSinglet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/DownSinglet.lean)
