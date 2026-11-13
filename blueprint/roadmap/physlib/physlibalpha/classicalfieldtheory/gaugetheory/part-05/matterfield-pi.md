---
declaration: module
origin: cited
lean: MatterField.repPi, MatterField.repJetPi, MatterField.repJetPi_apply, MatterField.repJetPi_smul, MatterField.lTensor_proj_repJetPi, MatterField.repAlgebraPi, MatterField.repAlgebraPi_apply, MatterField.repCoeff_repJetPi
statement: formalized
proof: formalized
---

# The direct sum of a finite family of matter fields

The module `PhyslibAlpha.ClassicalFieldTheory.GaugeTheory.MatterField.Pi`, [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean): 19 declarations, 11 with a docstring; 4 private, not shown.

## i. Overview

> `MatterField.prod` sums two matter fields of the same mass weight and statistics. This file
> does the same for a finite family `M : ι → MatterField jets`, producing a single matter
> field valued in `∀ i, (M i).V`. It is the operation that turns the several species of a
> theory into one field: the fifteen fermionic multiplets of the Standard Model become one
> fermion field, carried by `GaugeFieldData.fermionMatterField`.
>
> The binary and indexed versions are the same construction with `LinearMap.prodMap`
> replaced by `LinearMap.piMap` and `jetProdEquiv` by `jetPiEquiv`, so the proofs run in
> parallel; only the diagonal-map algebra used along the way differs. As in the binary case,
> the direct sum is represented by one `MatterField`, which has one mass weight and one
> statistic, so the summands must share both. The caller supplies the common values `w` and
> `σ`, together with proofs that every summand has them, so the direct sum of an empty family
> also has a definite weight and statistics.
>
> Finiteness of `ι` is essential and not merely convenient. `jetPiEquiv` — the
> identification of the jets of the product with the product of the jets, through which the
> jet gauge action is defined — exists only for a finite index type, and finiteness of the
> value space, a field of `MatterField`, would fail for an infinite family in any case.

## ii. Key results

> - `MatterField.repJetPi` : the jet gauge action of an indexed direct sum.
> - `MatterField.repJetPi_smul` : it is fibrewise, as each summand is.
> - `MatterField.lTensor_proj_repJetPi` : the projection onto a summand intertwines it with
>   that summand's own action.
> - `MatterField.repAlgebraPi` : the infinitesimal gauge action of an indexed direct sum.
> - `MatterField.repCoeff_repJetPi` : its base-point Taylor coefficients are the family of
>   those of the summands.
> - `MatterField.pi` : the direct sum of a finite family of matter fields of one mass
>   weight and one statistic.
> - `MatterField.jetComponentSpacePiEquiv` : the component space of the direct sum is the
>   family of the component spaces of the summands.
> - `MatterField.jetComponentSpacePiEquiv_symm_single` : a summand sits inside it as the
>   pullback along the projection onto that summand.

## iv. References

> * None.

## A. Diagonal maps of an indexed product

> Every piece of data of the direct sum acts index by index, that is through
> `LinearMap.piMap`. The four facts about that construction used below — that it is
> additive, negative-preserving and multiset-sum-preserving in the family, and that it
> composes index by index — all hold because `piMap` is evaluated pointwise, so each is a
> single `LinearMap.ext`.

## B. The direct sum of a finite family of matter fields

**`MatterField.repPi`**, a def, [line 127](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L127).

> The product of a family of representations, acting index by index. This is the
> indexed analogue of `Representation.prod`, which Mathlib provides only in the binary
> case.

```lean
noncomputable def repPi {W : ι → Type} [∀ i, AddCommGroup (W i)]
    [∀ i, Module ℂ (W i)] (ρ : ∀ i, Representation ℂ GJ (W i)) :
    Representation ℂ GJ (∀ i, W i)
```

**`MatterField.repJetPi`**, a def, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L143).

> **The jet gauge action of an indexed direct sum**: the family of actions, read
> through the identification of the jets of `∀ i, (M i).V` with the family of jets.

```lean
noncomputable def repJetPi : Representation ℂ GJ (SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V))
```

**`MatterField.repJetPi_apply`**, a lemma, [line 149](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L149).

```lean
lemma repJetPi_apply (U : GJ) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V)) :
    repJetPi M U z = (jetPiEquiv fun i => (M i).V).symm
      (fun i => (M i).repJet U (jetPiEquiv (fun i => (M i).V) z i))
```

**`MatterField.repJetPi_smul`**, a lemma, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L157).

> The jet gauge action of an indexed direct sum is fibrewise. It acts index by
> index, and each summand is fibrewise, so multiplication by a scalar jet passes through
> the splitting untouched. This is the field `repJet_smul` of `MatterField.pi`, stated
> separately so that it can be used without fixing a common mass weight.

```lean
lemma repJetPi_smul (U : GJ) (χ : SpaceTimeAlgebra) (z : SpaceTimeAlgebra ⊗[ℂ] (∀ i, (M i).V)) :
    repJetPi M U (χ • z) = χ • repJetPi M U z
```

**`MatterField.lTensor_proj_repJetPi`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L169).

> A summand is a subrepresentation of the jet gauge action of the direct sum. The
> projection onto the value space of one summand, applied to the jets, intertwines the
> summed action with that summand's own: the summed action is the family of the actions,
> and reading off a summand of the jets is the projection on the value factor.

```lean
lemma lTensor_proj_repJetPi (i : ι) (U : GJ) :
    (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i)).comp (repJetPi M U)
      = ((M i).repJet U).comp (LinearMap.lTensor SpaceTimeAlgebra (LinearMap.proj i))
```

**`MatterField.repAlgebraPi`**, a def, [line 178](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L178).

> **The infinitesimal action of an indexed direct sum**: the family of actions, one on
> each summand.

```lean
noncomputable def repAlgebraPi : 𝔤 →ₗ[ℝ] (∀ i, (M i).V) →ₗ[ℂ] (∀ i, (M i).V)
```

**`MatterField.repAlgebraPi_apply`**, a lemma, [line 191](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L191).

```lean
lemma repAlgebraPi_apply (c : 𝔤) :
    repAlgebraPi M c = LinearMap.piMap fun i => (M i).repAlgebra c
```

**`MatterField.repCoeff_repJetPi`**, a lemma, [line 197](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L197).

> The base-point Taylor coefficients of the summed jet action are the family of the
> coefficients of the summands: `jetOfConstant`, `jetIteratedDeriv` and `jetEval` all act
> index by index through `jetPiEquiv`.

```lean
lemma repCoeff_repJetPi (U : GJ) (x : Multiset (Fin 1 ⊕ Fin 3)) :
    GaugeAlgebraRealization.repCoeff (repJetPi M) U x =
      LinearMap.piMap fun i => GaugeAlgebraRealization.repCoeff (M i).repJet U x
```

**`MatterField.isInfinitesimalActionOf_repAlgebraPi`**, a lemma, [line 213](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L213).

> **The index-by-index algebra action generates the index-by-index jet action**: both
> laws of `IsInfinitesimalActionOf` are the corresponding laws of the summands, read
> through `repCoeff_repJetPi`, since `piMap` is additive in the family and composes index
> by index.

```lean
lemma isInfinitesimalActionOf_repAlgebraPi :
    jets.IsInfinitesimalActionOf (repAlgebraPi M) (repJetPi M)
```

**`MatterField.pi`**, a def, [line 242](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L242).

> **The direct sum of a finite family of matter fields** with common mass weight `w` and
> common statistics `σ`, given with proofs that every summand has them. It is one field
> valued in `∀ i, (M i).V`, of weight `w` and statistics `σ`, with every action acting index
> by index.

```lean
noncomputable def pi (w : ℕ) (_h : ∀ i, (M i).massWeight = w) (σ : FieldStatistic)
    (_hσ : ∀ i, (M i).statistic = σ) : MatterField jets
```

**`MatterField.pi_V`**, a lemma, [line 256](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L256).

```lean
lemma pi_V : (pi M w h σ hσ).V = ∀ i, (M i).V
```

**`MatterField.pi_repJet`**, a lemma, [line 259](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L259).

```lean
lemma pi_repJet : (pi M w h σ hσ).repJet = repJetPi M
```

**`MatterField.pi_repAlgebra`**, a lemma, [line 262](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L262).

```lean
lemma pi_repAlgebra : (pi M w h σ hσ).repAlgebra = repAlgebraPi M
```

**`MatterField.pi_massWeight`**, a lemma, [line 265](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L265).

```lean
lemma pi_massWeight : (pi M w h σ hσ).massWeight = w
```

**`MatterField.pi_statistic`**, a lemma, [line 268](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L268).

```lean
lemma pi_statistic : (pi M w h σ hσ).statistic = σ
```

**`MatterField.pi_repLorentz_apply`**, a lemma, [line 272](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L272).

> The Lorentz action of the direct sum is the family of Lorentz actions, acting index by
> index.

```lean
lemma pi_repLorentz_apply (Λ : SL(2,ℂ)) (v : ∀ i, (M i).V) (i : ι) :
    (pi M w h σ hσ).repLorentz Λ v i = (M i).repLorentz Λ (v i)
```

## C. The component space of the direct sum

> The direct sum was built so that the several species of a theory can be treated as one
> field. Nothing is lost in doing so at the level of component functions either: the
> symbols `∂_s ψ_α` and `∂_s ψ̄_α` of the summed field are exactly the families, over the
> index, of the symbols of the summands. This is the component-space image of the
> identification `jetPiEquiv` that defines the summed jet action, and it is the finite
> direct sum case of `JetComponentSpace.piEquiv`.

**`MatterField.jetComponentSpacePiEquiv`**, a def, [line 292](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L292).

> **The component space of a direct sum of matter fields splits.** A component function
> of `MatterField.pi M w h σ hσ` is exactly a family, one component function per summand. Both
> halves split by `JetComponentSpace.fstPiEquiv` and `JetComponentSpace.sndPiEquiv`, and
> the pair of families is reassembled into a family of pairs index by index.

```lean
noncomputable def jetComponentSpacePiEquiv :
    JetComponentSpace (pi M w h σ hσ) ≃ₗ[ℂ] ∀ i, JetComponentSpace (M i)
```

**`MatterField.jetComponentSpacePiEquiv_apply`**, a lemma, [line 297](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L297).

```lean
lemma jetComponentSpacePiEquiv_apply (x : JetComponentSpace (pi M w h σ hσ)) (i : ι) :
    jetComponentSpacePiEquiv M w h σ hσ x i =
      (JetComponentSpace.fstPiEquiv (fun i => (M i).V) x.1 i,
        JetComponentSpace.sndPiEquiv (fun i => (M i).V) x.2 i)
```

**`MatterField.jetComponentSpacePiEquiv_symm_single`**, a lemma, [line 307](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean#L307).

> **The summand of one species is the pullback along the projection onto it.** A
> component function of the summand `i`, placed in the family and read back as a component
> function of the direct sum, is that function precomposed with the projection onto the
> summand. This is what identifies the splitting with the species inclusions of a direct
> sum of component spaces.

```lean
lemma jetComponentSpacePiEquiv_symm_single (i : ι) (x : JetComponentSpace (M i)) :
    (jetComponentSpacePiEquiv M w h σ hσ).symm (Pi.single i x)
      = JetComponentSpace.comap
        (LinearMap.proj (φ := fun i => (M i).V) i : (pi M w h σ hσ).V →ₗ[ℂ] (M i).V) x
```

## Depends on

- [The jet component space of a matter field](matterfield-jetcomponent-basic.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/GaugeTheory/MatterField/Pi.lean)
