---
declaration: module
origin: cited
lean: StandardModel.UpSinglet, StandardModel.UpSinglet.valEquiv, StandardModel.UpSinglet.valLinEquiv, StandardModel.UpSinglet.valLinEquiv_apply, StandardModel.UpSinglet.valLinEquiv_symm_apply, StandardModel.UpSinglet.val_add, StandardModel.UpSinglet.val_smul, StandardModel.UpSinglet.repLorentzGroup
statement: formalized
proof: formalized
---

# Up-type singlets

The module `Physlib.Particles.StandardModel.Fermions.UpSinglet`, [Physlib/Particles/StandardModel/Fermions/UpSinglet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean): 18 declarations (2 instances with no name), 7 with a docstring.

> In this module we define the type corresponding to
> the target vector space of an up-type singlet quark field in the Standard Model.
>
> On this type we define a representation of the Lorentz group, and a
> representation of the Standard Model gauge group.

**`StandardModel.UpSinglet`**, a structure, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L30).

> The vector space of an up-type singlet quark field in the Standard Model.
> These live in the (3, 1)\_\{4} representation of the gauge group.

```lean
structure UpSinglet where
  /-- The underlying value of the up-type quark field in the tensor product space. -/
  val : Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

## Equivalence with the underlying tensor product space

**`StandardModel.UpSinglet.valEquiv`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L43).

> The linear equivalence between `UpSinglet` and its underlying tensor product space.

```lean
def valEquiv : UpSinglet ≃ Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

## The structure of a module

> The AddCommGroup and module instances are inherited from the underlying tensor product space.

**An instance with no name**, [line 54](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L54).

```lean
instance : AddCommGroup UpSinglet
```

**An instance with no name**, [line 56](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L56).

```lean
instance : Module ℂ UpSinglet
```

**`StandardModel.UpSinglet.valLinEquiv`**, a def, [line 59](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L59).

> The linear equivalence between `UpSinglet` and its underlying tensor product space.

```lean
def valLinEquiv : UpSinglet ≃ₗ[ℂ]
    Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)
```

**`StandardModel.UpSinglet.valLinEquiv_apply`**, a lemma, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L67).

```lean
lemma valLinEquiv_apply (q : UpSinglet) : valLinEquiv q = q.val
```

**`StandardModel.UpSinglet.valLinEquiv_symm_apply`**, a lemma, [line 69](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L69).

```lean
lemma valLinEquiv_symm_apply (m : Fermion.RightHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3)) :
    valLinEquiv.symm m = ⟨m⟩
```

**`StandardModel.UpSinglet.val_add`**, a lemma, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L73).

```lean
lemma val_add (q1 q2 : UpSinglet) : (q1 + q2).val = q1.val + q2.val
```

**`StandardModel.UpSinglet.val_smul`**, a lemma, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L76).

```lean
lemma val_smul (r : ℂ) (q : UpSinglet) : (r • q).val = r • q.val
```

## Lorentz group representation

**`StandardModel.UpSinglet.repLorentzGroup`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L87).

> The representation of the Lorentz group on the space of up-type quark fields.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) UpSinglet
```

## The representation of the Standard Model gauge group

**`StandardModel.UpSinglet.repGaugeGroupI`**, a def, [line 106](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L106).

> The action of the full Standard Model gauge group on up-type quark fields.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI UpSinglet
```

**`StandardModel.UpSinglet.repGaugeGroupI_tmul`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L121).

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (ψ : Fermion.RightHandedWeyl)
    (v : EuclideanSpace ℂ (Fin 3)) :
    repGaugeGroupI g ⟨ψ ⊗ₜ v⟩ = ⟨g.toU1 ^ 4 • ψ ⊗ₜ (g.toSU3.1.toEuclideanLin v)⟩
```

**`StandardModel.UpSinglet.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L128).

> The action of the full gauge group on a tensor product of basis elements, expanded as a
> sum over the columns of the `SU(3)` matrix.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k : Fin 2) (i : Fin 3) :
    repGaugeGroupI g ⟨RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ i⟩ =
      ∑ i' : Fin 3, (g.toU1.1 ^ 4  * g.toSU3.1 i' i)
      • (⟨RightHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ i'⟩ : UpSinglet)
```

**`StandardModel.UpSinglet.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 146](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L146).

```lean
lemma repGaugeGroupI_eq_iff_mul_eq {g1 g2 : GaugeGroupI} :
    repGaugeGroupI g1 = repGaugeGroupI g2 ↔ ∀ i i',
    g1.toU1.1 ^ 4 * g1.toSU3.1 i' i = g2.toU1.1 ^ 4 * g2.toSU3.1 i' i
```

**`StandardModel.UpSinglet.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L167).

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ ∃ a : ℂ, g.toSU3.1 = a • 1 ∧  a * g.toU1.1 ^ 4 = 1
```

**`StandardModel.UpSinglet.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L185).

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.UpSinglet.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L197).

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.UpSinglet.repGaugeGroup`**, a def, [line 203](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean#L203).

> The action of the Standard Model gauge group, potentially quotiented by
> a discrete factor on quark fields.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) UpSinglet
```

## Depends on

- [The Standard Model Gauge Group](gaugegroup/basic.md)
- [Right handed Weyl fermions](../../relativity/fermions/weyl/righthanded.md)

## Sources

- [Physlib/Particles/StandardModel/Fermions/UpSinglet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/UpSinglet.lean)
