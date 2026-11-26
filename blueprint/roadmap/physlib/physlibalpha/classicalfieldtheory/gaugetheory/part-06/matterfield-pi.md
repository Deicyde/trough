---
declaration: module
origin: cited
lean: GlobalGaugeGroup.MatterField.repPi, GlobalGaugeGroup.MatterField.piMapRingHom, GlobalGaugeGroup.MatterField.piMapRingHom_apply, GlobalGaugeGroup.MatterField.continuous_piMapRingHom, GlobalGaugeGroup.MatterField.repPiUnits, GlobalGaugeGroup.MatterField.repPiUnits_apply, GlobalGaugeGroup.MatterField.pi, GlobalGaugeGroup.MatterField.pi_repLorentz
statement: formalized
proof: formalized
---

# The direct sum of a finite family of matter fields

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Pi`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean): 23 declarations, 15 with a docstring; 4 private, not shown.

> A finite family of matter fields of one mass weight and statistics as a single matter field.

## i. Overview

> `prod` sums two matter fields of the same mass weight and statistics. This file
> does the same for a finite family `M : ι → G.MatterField`, producing a single matter
> field valued in `∀ i, (M i).V`. It is the operation that turns the several species of a
> theory into one field. The fifteen fermionic multiplets of the Standard Model become one
> fermion field, carried by `GaugeFieldData.fermionMatterField`.
>
> The binary and indexed versions are the same construction with `LinearMap.prodMap`
> replaced by `LinearMap.piMap` and `jetProdEquiv` by `jetPiEquiv`, so the proofs run in
> parallel. The representation of the global gauge group is the componentwise one, built as
> a continuous homomorphism into the units of the continuous linear maps of the product, and
> the infinitesimal and jet gauge actions are derived from it. As in the binary case, the
> direct sum is represented by one `MatterField`, which has one mass weight and one
> statistic, so the summands must share both. The caller supplies the common values `w` and
> `σ`, together with proofs that every summand has them, so the direct sum of an empty family
> also has a definite weight and statistics.
>
> Finiteness of `ι` is essential and not merely convenient. `jetPiEquiv`, the
> identification of the jets of the product with the product of the jets through which the
> jet gauge action is defined, exists only for a finite index type, and finite dimensionality
> of the value space would fail for an infinite family in any case.

## ii. Key results

> - `repPiUnits` : the componentwise representation of the global gauge group.
> - `pi` : the direct sum of a finite family of matter fields of one mass weight and one
>   statistic.
> - `lieAlgebraRep_pi` : the Lie algebra acts on the direct sum index by index.
> - `pi_repAlgebra` and `pi_repJet` : the derived infinitesimal and jet gauge actions are the
>   index-by-index ones, `repAlgebraPi` and `repJetPi`.
> - `repJetPi_smul` : the jet action is fibrewise, as each summand is.
> - `lTensor_proj_repJetPi` : the projection onto a summand intertwines it with that summand's
>   own action.
> - `repCoeff_repJetPi` : its base-point Taylor coefficients are the family of those of the
>   summands.
> - `fieldDerivSpacePiEquiv` : the component space of the direct sum is the family of the
>   component spaces of the summands.
> - `fieldDerivSpacePiEquiv_symm_single` : a summand sits inside it as the pullback along
>   the projection onto that summand.

## iv. References

> * None.

## A. The direct sum of a finite family of matter fields

> The direct sum acts index by index, so its representation of the global gauge group is the
> componentwise one, built as a continuous homomorphism into the units of the continuous linear
> maps of the product.

**`GlobalGaugeGroup.MatterField.repPi`**, a def, [line 94](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L94).

> The product of a family of representations, acting index by index. This is the
> indexed analogue of `Representation.prod`, which Mathlib provides only in the binary
> case.

```lean
noncomputable def repPi {W : ι → Type} [∀ i, AddCommGroup (W i)]
    [∀ i, Module ℂ (W i)] {H : Type} [Group H] (ρ : ∀ i, Representation ℂ H (W i)) :
    Representation ℂ H (∀ i, W i)
```

**`GlobalGaugeGroup.MatterField.piMapRingHom`**, a def, [line 110](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L110).

> The family of continuous linear maps `f i` as the continuous linear map of the product acting
> index by index, a ring homomorphism.

```lean
noncomputable def piMapRingHom :
    (∀ i, (M i).V →L[ℂ] (M i).V) →+* ((∀ i, (M i).V) →L[ℂ] (∀ i, (M i).V))
```

**`GlobalGaugeGroup.MatterField.piMapRingHom_apply`**, a lemma, [line 120](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L120).

```lean
lemma piMapRingHom_apply (f : ∀ i, (M i).V →L[ℂ] (M i).V) (v : ∀ i, (M i).V) (i : ι) :
    piMapRingHom M f v i = f i (v i)
```

**`GlobalGaugeGroup.MatterField.continuous_piMapRingHom`**, a lemma, [line 124](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L124).

```lean
lemma continuous_piMapRingHom : Continuous (piMapRingHom M)
```

**`GlobalGaugeGroup.MatterField.repPiUnits`**, a def, [line 137](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L137).

> The direct sum `g ↦ (ρ_{M i}(g))ᵢ` of the representations of a family of matrix matter
> fields.

```lean
noncomputable def repPiUnits : G.group →ₜ* ((∀ i, (M i).V) →L[ℂ] (∀ i, (M i).V))ˣ
```

**`GlobalGaugeGroup.MatterField.repPiUnits_apply`**, a lemma, [line 148](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L148).

```lean
lemma repPiUnits_apply (g : G.group) :
    ((repPiUnits M g : ((∀ i, (M i).V) →L[ℂ] (∀ i, (M i).V))ˣ) :
        (∀ i, (M i).V) →L[ℂ] (∀ i, (M i).V)) =
      piMapRingHom M fun i => ((M i).rep g : (M i).V →L[ℂ] (M i).V)
```

**`GlobalGaugeGroup.MatterField.pi`**, a def, [line 157](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L157).

> The direct sum of a finite family of matter fields with common mass weight `w` and
> common statistics `σ`, given with proofs that every summand has them. It is one field
> valued in `∀ i, (M i).V`, of weight `w` and statistics `σ`, with every action acting index
> by index.

```lean
noncomputable def pi (w : ℕ) (_h : ∀ i, (M i).massWeight = w) (σ : FieldStatistic)
    (_hσ : ∀ i, (M i).statistic = σ) : G.MatterField
```

**`GlobalGaugeGroup.MatterField.pi_repLorentz`**, a lemma, [line 170](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L170).

```lean
lemma pi_repLorentz : (pi M w h σ hσ).repLorentz = repPi fun i => (M i).repLorentz
```

**`GlobalGaugeGroup.MatterField.pi_massWeight`**, a lemma, [line 174](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L174).

```lean
lemma pi_massWeight : (pi M w h σ hσ).massWeight = w
```

**`GlobalGaugeGroup.MatterField.pi_statistic`**, a lemma, [line 178](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L178).

```lean
lemma pi_statistic : (pi M w h σ hσ).statistic = σ
```

## B. Diagonal maps of an indexed product

> Every piece of data of the direct sum acts index by index, that is through
> `LinearMap.piMap`. The four facts about that construction used below — that it is
> additive, negative-preserving and multiset-sum-preserving in the family, and that it
> composes index by index — all hold because `piMap` is evaluated pointwise, so each is a
> single `LinearMap.ext`.

## C. The index-by-index gauge actions

> The jet gauge action and the infinitesimal gauge action of the direct sum are the families of
> those of the summands, and the second generates the first.

**`GlobalGaugeGroup.MatterField.repJetPi`**, a def, [line 241](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L241).

> The jet gauge action of an indexed direct sum, the family of actions read
> through the identification of the jets of `∀ i, (M i).V` with the family of jets.

```lean
noncomputable def repJetPi :
    Representation ℂ G.gaugeJetGroup (SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V))
```

**`GlobalGaugeGroup.MatterField.repJetPi_apply`**, a lemma, [line 248](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L248).

```lean
lemma repJetPi_apply (U : G.gaugeJetGroup) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V)) :
    repJetPi M U z = (jetPiEquiv fun i => (M i).V).symm
      (fun i => (M i).repJet U (jetPiEquiv (fun i => (M i).V) z i))
```

**`GlobalGaugeGroup.MatterField.repJetPi_smul`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L256).

> The jet gauge action of an indexed direct sum is fibrewise. It acts index by
> index, and each summand is fibrewise, so multiplication by a scalar jet passes through
> the splitting untouched. This is the statement `repJet_smul` for `pi`, stated
> separately so that it can be used without fixing a common mass weight.

```lean
lemma repJetPi_smul (U : G.gaugeJetGroup) (χ : SpaceTimeAlgebra)
    (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V)) :
    repJetPi M U (χ • z) = χ • repJetPi M U z
```

**`GlobalGaugeGroup.MatterField.lTensor_proj_repJetPi`**, a lemma, [line 269](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L269).

> A summand is a subrepresentation of the jet gauge action of the direct sum. The
> projection onto the value space of one summand, applied to the jets, intertwines the
> summed action with that summand's own, since the summed action is the family of the actions,
> and reading off a summand of the jets is the projection on the value factor.

```lean
lemma lTensor_proj_repJetPi (i : ι) (U : G.gaugeJetGroup) :
    (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i)).comp (repJetPi M U)
      = ((M i).repJet U).comp (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i))
```

**`GlobalGaugeGroup.MatterField.repAlgebraPi`**, a def, [line 278](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L278).

> The infinitesimal action of an indexed direct sum, the family of actions, one on
> each summand.

```lean
noncomputable def repAlgebraPi :
    G.lieSubalgebra →ₗ[ℝ] (∀ i, (M i).V) →ₗ[ℂ] (∀ i, (M i).V)
```

**`GlobalGaugeGroup.MatterField.repAlgebraPi_apply`**, a lemma, [line 292](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L292).

```lean
lemma repAlgebraPi_apply (c : G.lieSubalgebra) :
    repAlgebraPi M c = LinearMap.piMap fun i => (M i).repAlgebra c
```

**`GlobalGaugeGroup.MatterField.repCoeff_repJetPi`**, a lemma, [line 298](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L298).

> The base-point Taylor coefficients of the summed jet action are the family of the
> coefficients of the summands, since `jetOfConstant`, `jetIteratedDeriv` and `jetEval` all act
> index by index through `jetPiEquiv`.

```lean
lemma repCoeff_repJetPi (U : G.gaugeJetGroup) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GlobalGaugeGroup.repCoeff (repJetPi M) U x =
      LinearMap.piMap fun i => GlobalGaugeGroup.repCoeff (M i).repJet U x
```

**`GlobalGaugeGroup.MatterField.isInfinitesimalActionOf_repAlgebraPi`**, a lemma, [line 314](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L314).

> The index-by-index algebra action generates the index-by-index jet action. Both
> laws of `IsInfinitesimalActionOf` are the corresponding laws of the summands, read
> through `repCoeff_repJetPi`, since `piMap` is additive in the family and composes index
> by index.

```lean
lemma isInfinitesimalActionOf_repAlgebraPi :
    G.IsInfinitesimalActionOf (repAlgebraPi M) (repJetPi M)
```

## D. The derived actions of the direct sum

> The infinitesimal and jet gauge actions that the direct sum inherits from its representation
> are the index-by-index ones.

**`GlobalGaugeGroup.MatterField.lieAlgebraRep_pi`**, a lemma, [line 353](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L353).

> The Lie algebra acts on a direct sum index by index.

```lean
lemma lieAlgebraRep_pi (X : G.lieSubalgebra) :
    lieAlgebraRep (pi M w h σ hσ) X = piMapRingHom M fun i => lieAlgebraRep (M i) X
```

**`GlobalGaugeGroup.MatterField.pi_repAlgebra`**, a lemma, [line 374](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L374).

> The Lie algebra of a direct sum acts index by index.

```lean
lemma pi_repAlgebra : (pi M w h σ hσ).repAlgebra = repAlgebraPi M
```

**`GlobalGaugeGroup.MatterField.pi_repJet`**, a lemma, [line 381](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L381).

> The gauge jets act on a direct sum index by index.

```lean
lemma pi_repJet : (pi M w h σ hσ).repJet = repJetPi M
```

## E. The component space of the direct sum

> The direct sum was built so that the several species of a theory can be treated as one
> field. Nothing is lost in doing so at the level of component functions either: the
> symbols `∂_s ψ_α` and `∂_s ψ̄_α` of the summed field are exactly the families, over the
> index, of the symbols of the summands. This is the component-space image of the
> identification `jetPiEquiv` that defines the summed jet action, and it is the finite
> direct sum case of `FieldDerivSpace.piEquiv`.

**`GlobalGaugeGroup.MatterField.fieldDerivSpacePiEquiv`**, a def, [line 410](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L410).

> The component space of a direct sum of matter fields splits. A component function
> of `pi M w h σ hσ` is exactly a family, one component function per summand. Both
> halves split by `FieldDerivSpace.fstPiEquiv` and `FieldDerivSpace.sndPiEquiv`, and
> the pair of families is reassembled into a family of pairs index by index.

```lean
noncomputable def fieldDerivSpacePiEquiv :
    FieldDerivSpace (pi M w h σ hσ) ≃ₗ[ℂ] ∀ i, FieldDerivSpace (M i)
```

**`GlobalGaugeGroup.MatterField.fieldDerivSpacePiEquiv_symm_single`**, a lemma, [line 420](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L420).

> The summand of one species is the pullback along the projection onto it. A
> component function of the summand `i`, placed in the family and read back as a component
> function of the direct sum, is that function precomposed with the projection onto the
> summand. This is what identifies the splitting with the species inclusions of a direct
> sum of component spaces.

```lean
lemma fieldDerivSpacePiEquiv_symm_single (i : ι) (x : FieldDerivSpace (M i)) :
    (fieldDerivSpacePiEquiv M w h σ hσ).symm (Pi.single i x)
      = FieldDerivSpace.comap
        (LinearMap.proj (φ := fun i => (M i).V) i :
          (pi M w h σ hσ).V →ₗ[ℂ] (M i).V) x
```

## Depends on

- [The field-derivative space of a matter field](matterfield-fieldderivspace-basic.md)
- [The infinitesimal action underlying a matter representation](matterfield-infinitesimalaction.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean)
