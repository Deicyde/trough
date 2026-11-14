---
declaration: module
origin: cited
lean: StandardModel.QuarkDoublet, StandardModel.QuarkDoublet.valEquiv, StandardModel.QuarkDoublet.valLinEquiv, StandardModel.QuarkDoublet.valLinEquiv_apply, StandardModel.QuarkDoublet.valLinEquiv_symm_apply, StandardModel.QuarkDoublet.val_add, StandardModel.QuarkDoublet.val_smul, StandardModel.QuarkDoublet.repLorentzGroup
statement: formalized
proof: formalized
---

# The type corresponding to quark doublets (Physlib)

The module `Physlib.Particles.StandardModel.Fermions.QuarkDoublet`, [Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean): 18 declarations (2 instances with no name), 7 with a docstring.

> In this module we define the type corresponding to
> the target vector space of a quark field in the Standard Model.
>
> On this type we define a representation of the Lorentz group, and a
> representation of the Standard Model gauge group.

**`StandardModel.QuarkDoublet`**, a structure, [line 30](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L30).

> The vector space of a quark field in the Standard Model.
> These live in the (3, 2)\_\{1} representation of the gauge group.

```lean
structure QuarkDoublet where
  /-- The underlying value of the quark field in the tensor product space. -/
  val : Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

## Equivalence with the underlying tensor product space

**`StandardModel.QuarkDoublet.valEquiv`**, a def, [line 43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L43).

> The linear equivalence between `QuarkDoublet` and its underlying tensor product space.

```lean
def valEquiv : QuarkDoublet ≃
    Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

## The structure of a module

> The AddCommGroup and module instances are inherited from the underlying tensor product space.

**An instance with no name**, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L55).

```lean
instance : AddCommGroup QuarkDoublet
```

**An instance with no name**, [line 57](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L57).

```lean
instance : Module ℂ QuarkDoublet
```

**`StandardModel.QuarkDoublet.valLinEquiv`**, a def, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L60).

> The linear equivalence between `QuarkDoublet` and its underlying tensor product space.

```lean
def valLinEquiv : QuarkDoublet ≃ₗ[ℂ]
    Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2)
```

**`StandardModel.QuarkDoublet.valLinEquiv_apply`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L68).

```lean
lemma valLinEquiv_apply (q : QuarkDoublet) : valLinEquiv q = q.val
```

**`StandardModel.QuarkDoublet.valLinEquiv_symm_apply`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L70).

```lean
lemma valLinEquiv_symm_apply
    (m : Fermion.LeftHandedWeyl ⊗[ℂ] EuclideanSpace ℂ (Fin 3) ⊗[ℂ] EuclideanSpace ℂ (Fin 2)) :
    valLinEquiv.symm m = ⟨m⟩
```

**`StandardModel.QuarkDoublet.val_add`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L75).

```lean
lemma val_add (q1 q2 : QuarkDoublet) : (q1 + q2).val = q1.val + q2.val
```

**`StandardModel.QuarkDoublet.val_smul`**, a lemma, [line 78](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L78).

```lean
lemma val_smul (r : ℂ) (q : QuarkDoublet) : (r • q).val = r • q.val
```

## Lorentz group representation

**`StandardModel.QuarkDoublet.repLorentzGroup`**, a def, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L89).

> The representation of the Lorentz group on the space of quark fields.

```lean
noncomputable def repLorentzGroup : Representation ℂ (SL(2,ℂ)) QuarkDoublet
```

## The representation of the Standard Model gauge group

**`StandardModel.QuarkDoublet.repGaugeGroupI`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L110).

> The action of the full Standard Model gauge group on quark fields.

```lean
noncomputable def repGaugeGroupI : Representation ℂ GaugeGroupI QuarkDoublet
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_tmul`**, a lemma, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L127).

```lean
lemma repGaugeGroupI_tmul (g : GaugeGroupI) (ψ : Fermion.LeftHandedWeyl)
    (v : EuclideanSpace ℂ (Fin 3)) (w : EuclideanSpace ℂ (Fin 2)) :
    repGaugeGroupI g ⟨ψ ⊗ₜ v ⊗ₜ w⟩ = ⟨g.toU1 • ψ ⊗ₜ (g.toSU3.1.toEuclideanLin v) ⊗ₜ
      (g.toSU2.1.toEuclideanLin w)⟩
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_tmul_basis_eq_sum`**, a lemma, [line 135](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L135).

> The action of the full gauge group on a tensor product of basis elements, expanded as a
> sum over the columns of the `SU(3)` and `SU(2)` matrices.

```lean
lemma repGaugeGroupI_tmul_basis_eq_sum (g : GaugeGroupI) (k : Fin 2) (i : Fin 3) (j : Fin 2) :
    repGaugeGroupI g ⟨LeftHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ i
      ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 2) ℂ j⟩ =
      ∑ i' : Fin 3, ∑ j' : Fin 2, (g.toU1.1 * g.toSU3.1 i' i * g.toSU2.1 j' j)
      • (⟨LeftHandedWeyl.basis k ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 3) ℂ i'
          ⊗ₜ[ℂ] EuclideanSpace.basisFun (Fin 2) ℂ j'⟩ : QuarkDoublet)
```

**`StandardModel.QuarkDoublet.repGaugeGroupI_eq_iff_mul_eq`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L157).

```lean
lemma repGaugeGroupI_eq_iff_mul_eq {g1 g2 : GaugeGroupI} :
    repGaugeGroupI g1 = repGaugeGroupI g2 ↔ ∀ i i' j j',
    g1.toU1.1 * g1.toSU3.1 i' i * g1.toSU2.1 j' j =
    g2.toU1.1 * g2.toSU3.1 i' i * g2.toSU2.1 j' j
```

**`StandardModel.QuarkDoublet.mem_repGaugeGroupI_ker_iff_eq`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L185).

```lean
lemma mem_repGaugeGroupI_ker_iff_eq {g : GaugeGroupI} :
    g ∈ repGaugeGroupI.ker ↔ ∃ a b : ℂ, g.toSU2.1 = a • 1 ∧ g.toSU3.1 = b • 1 ∧
      a * b * g.toU1.1 = 1
```

**`StandardModel.QuarkDoublet.gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI`**, a lemma, [line 206](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L206).

```lean
lemma gaugeGroup_subgroup_ℤ₆_le_ker_repGaugeGroupI :
    GaugeGroupQuot.subgroup .ℤ₆ ≤ repGaugeGroupI.ker
```

**`StandardModel.QuarkDoublet.gaugeGroup_subgroup_le_ker_repGaugeGroupI`**, a lemma, [line 220](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L220).

```lean
lemma gaugeGroup_subgroup_le_ker_repGaugeGroupI (Q : GaugeGroupQuot) :
    Q.subgroup ≤ repGaugeGroupI.ker
```

**`StandardModel.QuarkDoublet.repGaugeGroup`**, a def, [line 226](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean#L226).

> The action of the Standard Model gauge group, potentially quotiented by
> a discrete factor on quark fields.

```lean
noncomputable def repGaugeGroup : (Q : GaugeGroupQuot) →
    Representation ℂ (GaugeGroup Q) QuarkDoublet
```

## Depends on

- [The Standard Model Gauge Group](gaugegroup/basic.md)
- [Left handed Weyl fermions](../../relativity/fermions/weyl/lefthanded.md)

## Sources

- [Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/Particles/StandardModel/Fermions/QuarkDoublet.lean)
