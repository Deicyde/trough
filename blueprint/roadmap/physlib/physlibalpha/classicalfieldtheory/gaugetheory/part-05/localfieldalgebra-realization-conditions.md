---
declaration: module
origin: cited
lean: GlobalGaugeGroup.isCompact_unitaryGroup, GlobalGaugeGroup.compactSpace_ofSubmonoid, GlobalGaugeGroup.continuous_prodGroupHom, GlobalGaugeGroup.compactSpace_prod, GlobalGaugeGroup.MatterField.continuous_rep_apply, GlobalGaugeGroup.MatterField.LorentzContinuous, GlobalGaugeGroup.MatterField.ofMatrixRep_gaugeLorentzCommute, GlobalGaugeGroup.MatterField.ofMatrixRep_lorentzContinuous
statement: formalized
proof: formalized
---

# Conditions for the reduction of invariants

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.LocalFieldAlgebra.Realization.Conditions`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean): 16 declarations (4 instances with no name), 12 with a docstring.

> Compactness of the gauge group, continuity of the Lorentz representations and commutation of the
> gauge and Lorentz actions.

## i. Overview

> Invariants of a realization of the covariant field algebra descend to invariants of the
> covariant field algebra itself when both symmetry groups can be averaged over. This needs three
> conditions on a gauge theory.
>
> The gauge group must be compact, so that it has a normalized Haar measure. This is
> `CompactSpace G.group`, for the topology of `G.group` as a subspace of `GL(κ, ℂ)`. A global
> gauge group made of unitary matrices is compact, being closed in the compact unitary group, and
> this covers `SU(n)`, `U(1)`, `SO(n)` and `Sp(n)`. The product of two compact global gauge groups
> is compact, being the continuous image of the product of the two groups. So the gauge group of
> the Standard Model is compact by these instances.
>
> The Lorentz representation of every species must be continuous, in the sense that its matrix
> coefficients `Λ ↦ φ (ρ(Λ) v)` are continuous on `SL(2,ℂ)`. The gauge representation of a matter
> field is continuous by definition, and its matrix coefficients are continuous too.
>
> The gauge and Lorentz representations of every species must commute,
> `GaugeFieldData.GaugeLorentzCommute`. This implies the infinitesimal condition
> `GaugeFieldData.GaugeLorentzCompatible` used by the covariant derivative, but not conversely,
> since the infinitesimal action does not determine the action of a disconnected gauge group. For
> a matter field built as a tensor product of a gauge multiplet and a Lorentz multiplet the two
> actions commute.

## ii. Key results

> - `GlobalGaugeGroup.compactSpace_ofSubmonoid` : a global gauge group of unitary matrices is
>   compact.
> - `GlobalGaugeGroup.compactSpace_prod` : the product of compact global gauge groups is compact.
> - `GlobalGaugeGroup.MatterField.LorentzContinuous` : continuity of the Lorentz representation of
>   a matter field.
> - `GlobalGaugeGroup.MatterField.continuous_rep_apply` : continuity of the matrix coefficients of
>   the gauge representation of a matter field.
> - `GlobalGaugeGroup.MatterField.ofMatrixRep_lorentzContinuous`,
>   `GlobalGaugeGroup.MatterField.ofMatrixRep_gaugeLorentzCommute` : both conditions hold for the
>   matter field of a matrix representation, given continuity of the Lorentz representation on the
>   Lorentz factor.
> - `Fermion.LeftHandedWeyl.continuous_rep_apply`, `Fermion.RightHandedWeyl.continuous_rep_apply` :
>   continuity of the Weyl representations.
> - `GaugeFieldData.LorentzContinuous` : the continuity condition on every species of a field
>   datum.

## iv. References

> - The compact classical groups, see for example
>   T. Bröcker and T. tom Dieck, *Representations of Compact Lie Groups*.

## A. Compact global gauge groups

### A.1. Global gauge groups of unitary matrices

**`GlobalGaugeGroup.isCompact_unitaryGroup`**, a lemma, [line 103](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L103).

> The unitary matrices form a compact set, being closed with entries of modulus at most one.

```lean
lemma isCompact_unitaryGroup : IsCompact (unitaryGroup κ ℂ : Set (Matrix κ κ ℂ))
```

**`GlobalGaugeGroup.compactSpace_ofSubmonoid`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L111).

> The global gauge group of a closed submonoid of unitary matrices is compact.

```lean
lemma compactSpace_ofSubmonoid {S : Submonoid (Matrix κ κ ℂ)}
    (hS : IsClosed (S : Set (Matrix κ κ ℂ))) (hU : S ≤ unitaryGroup κ ℂ) :
    CompactSpace (ofSubmonoid S hS).group
```

### A.2. The groups SU(n), U(1), SO(n) and Sp(n)

**An instance with no name**, [line 123](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L123).

```lean
instance (n : ℕ) : CompactSpace (SU n).group
```

**An instance with no name**, [line 125](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L125).

```lean
instance : CompactSpace U1.group
```

**An instance with no name**, [line 127](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L127).

```lean
instance (n : ℕ) : CompactSpace (SO n).group
```

**An instance with no name**, [line 130](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L130).

```lean
instance (n : ℕ) : CompactSpace (Sp n).group
```

### A.3. Products

**`GlobalGaugeGroup.continuous_prodGroupHom`**, a lemma, [line 145](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L145).

> The pair `(g₁, g₂)` depends continuously on its factors as the block-diagonal matrix
> `diag(g₁, g₂)` of the product.

```lean
lemma continuous_prodGroupHom : Continuous (prodGroupHom G₁ G₂)
```

**`GlobalGaugeGroup.compactSpace_prod`**, an instance, [line 164](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L164).

> The product of two compact global gauge groups is compact.

```lean
instance compactSpace_prod [CompactSpace G₁.group] [CompactSpace G₂.group] :
    CompactSpace (G₁.prod G₂).group
```

## B. Conditions on matter fields

### B.1. Continuity of the gauge representation

**`GlobalGaugeGroup.MatterField.continuous_rep_apply`**, a lemma, [line 184](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L184).

> The matrix coefficients `g ↦ φ (ρ(g) v)` of the gauge representation of a matter field are
> continuous.

```lean
lemma continuous_rep_apply (v : M.V) (φ : Module.Dual ℂ M.V) :
    Continuous fun g : G.group => φ ((M.rep g : M.V →L[ℂ] M.V) v)
```

### B.2. Continuity of the Lorentz representation

**`GlobalGaugeGroup.MatterField.LorentzContinuous`**, a def, [line 198](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L198).

> The Lorentz representation of a matter field is continuous, meaning that its matrix coefficients
> `Λ ↦ φ (ρ(Λ) v)` are continuous on `SL(2,ℂ)`. As the value space is finite-dimensional, this is
> continuity of `Λ ↦ ρ(Λ)` for the unique vector space topology on its linear maps.

```lean
def LorentzContinuous : Prop
```

### B.3. Matter fields of matrix representations

**`GlobalGaugeGroup.MatterField.ofMatrixRep_gaugeLorentzCommute`**, a lemma, [line 214](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L214).

> The gauge and Lorentz representations of the matter field of a matrix representation
> commute, since they act on different tensor factors.

```lean
lemma ofMatrixRep_gaugeLorentzCommute : (ofMatrixRep e ρ repL w σ).GaugeLorentzCommute
```

**`GlobalGaugeGroup.MatterField.ofMatrixRep_lorentzContinuous`**, a lemma, [line 219](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L219).

> The Lorentz representation of the matter field of a matrix representation is continuous
> when the representation on the Lorentz factor has continuous matrix coefficients.

```lean
lemma ofMatrixRep_lorentzContinuous
    (h : ∀ (s : S) (ψ : Module.Dual ℂ S), Continuous fun Λ : SL(2,ℂ) => ψ (repL Λ s)) :
    (ofMatrixRep e ρ repL w σ).LorentzContinuous
```

### B.4. Continuity of the Weyl representations

**`continuous_specialLinearGroup_apply`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L248).

> The entries of an element of `SL(2,ℂ)` are continuous.

```lean
lemma continuous_specialLinearGroup_apply (i j : Fin 2) :
    Continuous fun Λ : SL(2,ℂ) => (Λ : Matrix (Fin 2) (Fin 2) ℂ) i j
```

**`Fermion.LeftHandedWeyl.continuous_rep_apply`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L256).

> The matrix coefficients `Λ ↦ ψ (ρ(Λ) s)` of the left-handed Weyl representation are
> continuous.

```lean
lemma LeftHandedWeyl.continuous_rep_apply (s : LeftHandedWeyl) (ψ : Module.Dual ℂ LeftHandedWeyl) :
    Continuous fun Λ : SL(2,ℂ) => ψ (LeftHandedWeyl.rep Λ s)
```

**`Fermion.RightHandedWeyl.continuous_rep_apply`**, a lemma, [line 271](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L271).

> The matrix coefficients `Λ ↦ ψ (ρ(Λ) s)` of the right-handed Weyl representation are
> continuous.

```lean
lemma RightHandedWeyl.continuous_rep_apply (s : RightHandedWeyl)
    (ψ : Module.Dual ℂ RightHandedWeyl) :
    Continuous fun Λ : SL(2,ℂ) => ψ (RightHandedWeyl.rep Λ s)
```

## C. Conditions on a field datum

**`GaugeFieldData.LorentzContinuous`**, a def, [line 299](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean#L299).

> The Lorentz representation of every species of the datum is continuous.

```lean
def LorentzContinuous : Prop
```

## Depends on

- [Left handed Weyl fermions](../../../../physlib/relativity/fermions/weyl/lefthanded.md)
- [Right handed Weyl fermions](../../../../physlib/relativity/fermions/weyl/righthanded.md)
- [The field data of a gauge theory](../part-01/gaugefielddata-basic.md)
- [The product of global gauge groups](../part-02/globalgaugegroup-prod.md)
- [The global gauge group SO(n)](../part-02/globalgaugegroup-so.md)
- [The global gauge group Sp(n)](../part-02/globalgaugegroup-sp.md)
- [The global gauge group SU(n)](../part-02/globalgaugegroup-su.md)
- [The global gauge group U(1)](../part-02/globalgaugegroup-u1.md)
- [Matter fields from matrix representations of a global gauge group](../part-06/matterfield-ofmatrixrep.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/LocalFieldAlgebra/Realization/Conditions.lean)
