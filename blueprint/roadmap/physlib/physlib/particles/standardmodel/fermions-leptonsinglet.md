---
declaration: module
origin: cited
lean: StandardModel.LeptonSinglet, StandardModel.LeptonSinglet.valEquiv, StandardModel.LeptonSinglet.valLinEquiv, StandardModel.LeptonSinglet.valLinEquiv_apply, StandardModel.LeptonSinglet.valLinEquiv_symm_apply, StandardModel.LeptonSinglet.val_add, StandardModel.LeptonSinglet.val_smul, StandardModel.LeptonSinglet.repLorentzGroup
statement: formalized
proof: formalized
---

# Charged-lepton singlets (Physlib)

The module `Physlib.Particles.StandardModel.Fermions.LeptonSinglet`, [Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean): 18 declarations (2 instances with no name), 12 with a docstring.

## i. Overview

> The Standard Model charged-lepton singlet is a right-handed Weyl spinor in the `(1, 1)_{-6}`
> representation. Here charges are normalized as `6Y`, so `-6` is the usual hypercharge
> `Y = -1`.
>
> `LeptonSinglet` is the target vector space of one charged-lepton singlet. Its only index is
> the Lorentz index carried by the Weyl spinor.
>
> The Lorentz and gauge actions are first defined separately. The gauge action is then computed
> on an arbitrary spinor, used to identify its kernel, and descended to each supported global
> form of the Standard Model gauge group.

## ii. Key results

> - `LeptonSinglet` : the target space of the `(1, 1)_{-6}` multiplet.
> - `repLorentzGroup` : the right-handed Lorentz action.
> - `repGaugeGroupI` : the action of the unquotiented gauge group.
> - `repGaugeGroupI_apply` : the gauge action on a spinor.
> - `mem_repGaugeGroupI_ker_iff_eq` : the kernel of the full-group action.
> - `gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI` : triviality of the central `ℤ₆`.
> - `repGaugeGroup` : the action descended to every supported gauge-group quotient.

## A. The charged-lepton-singlet space

> The Weyl spinor carries the right-handed Lorentz index, and it is the whole of the multiplet:
> a charged-lepton singlet has no colour index and no weak-isospin index.

**`StandardModel.LeptonSinglet`**, a structure, [line 62](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L62).

> The target vector space of one Standard Model charged-lepton singlet.
> It carries the `(1, 1)_{-6}` representation of the gauge group.

```lean
structure LeptonSinglet where
  /-- The right-handed Weyl spinor. -/
  val : Fermion.RightHandedWeyl
```

## B. Linear structure

> The wrapper distinguishes charged-lepton singlets from other isomorphic vector spaces.
> The following equivalences transfer the linear structure of the Weyl-spinor space and expose
> that model when defining representations.

**`StandardModel.LeptonSinglet.valEquiv`**, a def, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L78).

> Identifies a charged-lepton singlet with its underlying Weyl spinor.

```lean
def valEquiv : LeptonSinglet ≃ Fermion.RightHandedWeyl
```

**An instance with no name**, [line 82](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L82).

```lean
instance : AddCommGroup LeptonSinglet
```

**An instance with no name**, [line 84](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L84).

```lean
instance : Module ℂ LeptonSinglet
```

**`StandardModel.LeptonSinglet.valLinEquiv`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L87).

> The linear identification with the underlying Weyl-spinor space.

```lean
def valLinEquiv : LeptonSinglet ≃ₗ[ℂ] Fermion.RightHandedWeyl
```

**`StandardModel.LeptonSinglet.valLinEquiv_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L94).

```lean
lemma valLinEquiv_apply (l : LeptonSinglet) : valLinEquiv l = l.val
```

**`StandardModel.LeptonSinglet.valLinEquiv_symm_apply`**, a lemma, [line 96](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L96).

```lean
lemma valLinEquiv_symm_apply (m : Fermion.RightHandedWeyl) :
    valLinEquiv.symm m = ⟨m⟩
```

**`StandardModel.LeptonSinglet.val_add`**, a lemma, [line 100](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L100).

```lean
lemma val_add (l₁ l₂ : LeptonSinglet) : (l₁ + l₂).val = l₁.val + l₂.val
```

**`StandardModel.LeptonSinglet.val_smul`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L103).

```lean
lemma val_smul (r : ℂ) (l : LeptonSinglet) : (r • l).val = r • l.val
```

## C. Lorentz action

> The Lorentz group acts through the right-handed Weyl representation, transported along the
> identification of a charged-lepton singlet with its spinor.

**`StandardModel.LeptonSinglet.repLorentzGroup`**, a def, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L116).

> The right-handed Lorentz representation on charged-lepton singlets.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) LeptonSinglet
```

## D. Gauge action

> The colour and weak factors act trivially, so the gauge group acts only through hypercharge.
> The `U(1)` action is `star z ^ 6`; since `z` is unitary, `star z = z⁻¹`, so this represents
> charge `-6`.
>
> The formulas below expose the scalar used to compare actions and compute the kernel.

**`StandardModel.LeptonSinglet.repGaugeGroupI`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L137).

> The `(1, 1)_{-6}` action of the unquotiented Standard Model gauge group.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI LeptonSinglet
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_apply`**, a lemma, [line 150](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L150).

> The gauge group acts on a charged-lepton singlet by the hypercharge scalar alone.

```lean
lemma repGaugeGroupI_apply (g : GaugeGroupI) (ψ : Fermion.RightHandedWeyl) :
    repGaugeGroupI g ⟨ψ⟩ = ⟨(star g.toU1.1 ^ 6) • ψ⟩
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_basis`**, a lemma, [line 155](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L155).

> The gauge action is diagonal in the standard Weyl basis.

```lean
lemma repGaugeGroupI_basis (g : GaugeGroupI) (k : Fin 2) :
    repGaugeGroupI g ⟨RightHandedWeyl.basis k⟩ =
      (star g.toU1.1 ^ 6) • (⟨RightHandedWeyl.basis k⟩ : LeptonSinglet)
```

**`StandardModel.LeptonSinglet.repGaugeGroupI_eq_iff`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L161).

> Two gauge elements induce the same action exactly when their hypercharge scalars agree.

```lean
lemma repGaugeGroupI_eq_iff {g₁ g₂ : GaugeGroupI} :
    repGaugeGroupI g₁ = repGaugeGroupI g₂ ↔
      star g₁.toU1.1 ^ 6 = star g₂.toU1.1 ^ 6
```

## E. Kernel of the gauge action

> An element acts trivially exactly when its hypercharge scalar is one. Its colour and weak
> components are unrestricted, since neither appears in the action.

**`StandardModel.LeptonSinglet.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L185).

> Characterizes the full-group elements acting trivially on the charged-lepton singlet.

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ star g.toU1.1 ^ 6 = 1
```

## F. Descent to quotient gauge groups

> A representation descends through a quotient when the quotient subgroup lies in its kernel.
> The `U(1)` component of a central element is a sixth root of unity, so conjugating and raising
> to the sixth power gives one, and charge `-6` therefore acts trivially.

**`StandardModel.LeptonSinglet.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 200](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L200).

> The central `ℤ₆` subgroup acts trivially on `(1, 1)_{-6}`.

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonSinglet.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 211](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L211).

> Every supported quotient subgroup acts trivially on the charged-lepton singlet.

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.LeptonSinglet.repGaugeGroup`**, a def, [line 217](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean#L217).

> The `(1, 1)_{-6}` representation for every supported global form of the
> Standard Model gauge group.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) LeptonSinglet
```

## Depends on

- [The Standard Model Gauge Group](gaugegroup/basic.md)
- [Right handed Weyl fermions](../../relativity/fermions/weyl/righthanded.md)

## Sources

- [Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/LeptonSinglet.lean)
