---
declaration: module
origin: cited
lean: StandardModel.LeptonDoublet, StandardModel.LeptonDoublet.valEquiv, StandardModel.LeptonDoublet.valLinEquiv, StandardModel.LeptonDoublet.valLinEquiv_apply, StandardModel.LeptonDoublet.valLinEquiv_symm_apply, StandardModel.LeptonDoublet.val_add, StandardModel.LeptonDoublet.val_smul, StandardModel.LeptonDoublet.repLorentzGroup
statement: formalized
proof: formalized
---

# Lepton doublets (Physlib)

The module `Physlib.Particles.StandardModel.Fermions.LeptonDoublet`, [Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean): 18 declarations (2 instances with no name), 12 with a docstring.

## i. Overview

> The Standard Model lepton doublet is a left-handed Weyl spinor in the `(1, 2)_{-3}`
> representation. Here charges are normalized as `6Y`, so `-3` is the usual hypercharge
> `Y = -1/2`.
>
> `LeptonDoublet` is the target vector space of one lepton multiplet. Its Weyl factor
> carries the Lorentz index and its two-dimensional factor carries the weak index.
> The absence of a colour factor makes it an `SU(3)` singlet.
>
> The Lorentz and gauge actions are first defined separately. The gauge action is then
> computed on a basis, used to identify its kernel, and descended to each supported global
> form of the Standard Model gauge group.

## ii. Key results

> - `LeptonDoublet` : the target space of the `(1, 2)_{-3}` multiplet.
> - `repLorentzGroup` : the left-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_tmul_basis_eq_sum` : the gauge action in a tensor-product basis.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.

## A. The lepton-doublet space

> The Weyl factor carries the left-handed Lorentz index, while
> `EuclideanSpace ℂ (Fin 2)` carries the weak index.

**`StandardModel.LeptonDoublet`**, a structure, [line 65](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L65).

> The target vector space of one Standard Model lepton doublet.
> It carries the `(1, 2)_{-3}` representation of the gauge group.

```lean
structure LeptonDoublet where
  /-- The left-handed Weyl spinor with its weak-doublet index. -/
  val : Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

## B. Linear structure

> The wrapper distinguishes lepton doublets from other isomorphic vector spaces.
> The following equivalences transfer the linear structure of the tensor product and expose
> that model when defining representations.

**`StandardModel.LeptonDoublet.valEquiv`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L81).

> Identifies a lepton doublet with its underlying tensor-product value.

```lean
def valEquiv : LeptonDoublet ≃ Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

**An instance with no name**, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L85).

```lean
instance : AddCommGroup LeptonDoublet
```

**An instance with no name**, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L87).

```lean
instance : Module ℂ LeptonDoublet
```

**`StandardModel.LeptonDoublet.valLinEquiv`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L90).

> The linear identification with the underlying tensor product.

```lean
def valLinEquiv : LeptonDoublet ≃ₗ[ℂ]
    Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

**`StandardModel.LeptonDoublet.valLinEquiv_apply`**, a lemma, [line 98](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L98).

```lean
lemma valLinEquiv_apply (l : LeptonDoublet) : valLinEquiv l = l.val
```

**`StandardModel.LeptonDoublet.valLinEquiv_symm_apply`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L100).

```lean
lemma valLinEquiv_symm_apply
    (m : Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 2)) :
    valLinEquiv.symm m = ⟨m⟩
```

**`StandardModel.LeptonDoublet.val_add`**, a lemma, [line 105](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L105).

```lean
lemma val_add (l₁ l₂ : LeptonDoublet) : (l₁ + l₂).val = l₁.val + l₂.val
```

**`StandardModel.LeptonDoublet.val_smul`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L108).

```lean
lemma val_smul (r : ℂ) (l : LeptonDoublet) : (r • l).val = r • l.val
```

## C. Lorentz action

> The Lorentz group acts on the left-handed Weyl factor and leaves the weak index fixed.

**`StandardModel.LeptonDoublet.repLorentzGroup`**, a def, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L121).

> The left-handed Lorentz representation on lepton doublets.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) LeptonDoublet
```

## D. Gauge action

> The colour factor acts trivially, while `SU(2)` acts on the weak index. The `U(1)` action
> is `star z ^ 3`; since `z` is unitary, `star z = z⁻¹`, so this represents charge `-3`.
>
> The tensor and basis formulas below expose the coefficients used to compare actions and
> compute the kernel.

**`StandardModel.LeptonDoublet.repGaugeGroupI`**, a def, [line 145](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L145).

> The `(1, 2)_{-3}` action of the unquotiented Standard Model gauge group.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI LeptonDoublet
```

**`StandardModel.LeptonDoublet.repGaugeGroupI_tmul`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L161).

> The gauge action on a pure spinor–weak tensor.

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (v : Fermion.LeftHandedWeyl)
    (w : EuclideanSpace ℂ (Fin 2)) :
    repGaugeGroupI g ⟨v ⊗ₜ w⟩ =
      ⟨(star g.toU1.1 ^ 3) • v ⊗ₜ (g.toSU2.1.toEuclideanLin w)⟩
```

**`StandardModel.LeptonDoublet.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 168](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L168).

> Expands the gauge action in the spinor–weak basis.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k j : Fin 2) :
    repGaugeGroupI g ⟨LeftHandedWeyl.basis k ⊗ₜ[ℂ]
      EuclideanSpace.basisFun (Fin 2) ℂ j⟩ =
      ∑ j' : Fin 2, (star g.toU1.1 ^ 3 * g.toSU2.1 j' j)
      • (⟨LeftHandedWeyl.basis k ⊗ₜ[ℂ]
          EuclideanSpace.basisFun (Fin 2) ℂ j'⟩ : LeptonDoublet)
```

**`StandardModel.LeptonDoublet.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L189).

> Two gauge elements induce the same action exactly when their weak-basis coefficients agree.

```lean
lemma repGaugeGroupI_eq_iff_mul_eq {g₁ g₂ : GaugeGroupI} :
    repGaugeGroupI g₁ = repGaugeGroupI g₂ ↔ ∀ j j',
    star g₁.toU1.1 ^ 3 * g₁.toSU2.1 j' j =
      star g₂.toU1.1 ^ 3 * g₂.toSU2.1 j' j
```

## E. Kernel of the gauge action

> An element acts trivially when its weak action is scalar and that scalar cancels its
> `U(1)` phase. Its colour component is unrestricted because the lepton doublet is an
> `SU(3)` singlet.

**`StandardModel.LeptonDoublet.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 227](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L227).

> Characterizes the full-group elements acting trivially on the lepton doublet.

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ ∃ a : ℂ, g.toSU2.1 = a • 1 ∧
      a * star g.toU1.1 ^ 3 = 1
```

## F. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its
> kernel. For the central `ℤ₆`, the weak central phase and charge `-3` phase combine to a
> sixth power and therefore act trivially.

**`StandardModel.LeptonDoublet.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L269).

> The central `ℤ₆` subgroup acts trivially on `(1, 2)_{-3}`.

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoublet.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 283](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L283).

> Every supported quotient subgroup acts trivially on the lepton doublet.

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonDoublet.repGaugeGroup`**, a def, [line 289](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean#L289).

> The `(1, 2)_{-3}` representation for every supported global form of the
> Standard Model gauge group.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) LeptonDoublet
```

## Depends on

- [The Standard Model Gauge Group](gaugegroup/basic.md)
- [Left handed Weyl fermions](../../relativity/fermions/weyl/lefthanded.md)

## Sources

- [Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonDoublet.lean)
