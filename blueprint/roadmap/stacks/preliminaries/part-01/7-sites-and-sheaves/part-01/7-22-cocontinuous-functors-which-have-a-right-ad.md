---
declaration: section
origin: cited
lean: CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction, CategoryTheory.Functor.sheafPullbackCocontinuousIsoLan, CategoryTheory.Adjunction.isMorphismOfSites_of_isLeftAdjoint, CategoryTheory.Adjunction.morphismOfTopoiPushforwardIsoOfIsCocontinuous, CategoryTheory.Adjunction.morphismOfTopoiInverseImageIsoOfIsCocontinuous, CategoryTheory.Adjunction.morphismOfTopoi_adj_compatible_of_isCocontinuous, CategoryTheory.Adjunction.isCocontinuous_leftAdjoint_of_isContinuous
statement: formalized
proof: formalized
---

# 7.22 Cocontinuous functors which have a right adjoint

Section 7.22 of the Stacks Project, [Tag 00XW](https://stacks.math.columbia.edu/tag/00XW). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00XX, a lemma

[Tag 00XX](https://stacks.math.columbia.edu/tag/00XX) in the Stacks Project.

**`CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L229). The attribute's comment: “(1)”.

> **Stacks 00XX (1).** Let `u : C ⥤ D` be cocontinuous with right adjoint `v : D ⥤ C`,
> and let `g : Sh(C) → Sh(D)` be the associated morphism of topoi. Then for a sheaf `F` on
> `C` the sheaf `g_*F` is the presheaf `v^p F`, in other words `(g_*F)(V) = F(v(V))`.
>
> Underlying presheaves are compared because `g_* = {}_s u` lands in sheaves on `D` while
> `v^p F = F ∘ v` is a priori only a presheaf; the isomorphism says the latter is the
> former, hence a sheaf.

```lean
noncomputable def sheafPushforwardCocontinuousIsoRestriction
    [u.IsCocontinuous J K] [∀ F : Cᵒᵖ ⥤ A, u.op.HasPointwiseRightKanExtension F] :
    u.sheafPushforwardCocontinuous A J K ⋙ sheafToPresheaf K A ≅
      sheafToPresheaf J A ⋙ (whiskeringLeft Dᵒᵖ Cᵒᵖ A).obj v.op
```

**`CategoryTheory.Functor.sheafPullbackCocontinuousIsoLan`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 249](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L249). The attribute's comment: “(2)”.

> **Stacks 00XX (2).** In the situation of `sheafPushforwardCocontinuousIsoRestriction`,
> for a sheaf `G` on `D` we have `g^{-1}G = (v_p G)^#`: the sheaf pullback
> `G ↦ (u^p G)^#` agrees with the sheafified left Kan extension along `v.op`.

```lean
noncomputable def sheafPullbackCocontinuousIsoLan
    [HasWeakSheafify J A] [∀ F : Dᵒᵖ ⥤ A, v.op.HasLeftKanExtension F] :
    u.sheafPullbackCocontinuous A J K ≅
      sheafToPresheaf K A ⋙ v.op.lan ⋙ presheafToSheaf J A
```

## Tag 00XY, a lemma

[Tag 00XY](https://stacks.math.columbia.edu/tag/00XY) in the Stacks Project.

**`CategoryTheory.Adjunction.isMorphismOfSites_of_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean#L61). The attribute's comment: “v defines a morphism of sites (cocontinuity of u is not needed)”. References: SGA 4 III (2.5), “u^s left exact”.

> **Stacks 09VR, final assertion.** A continuous functor `v : D ⥤ C` which admits a left adjoint
> defines a morphism of sites `f : C → D`, i.e. `v` is continuous and the induced pullback
> `v_s = f⁻¹` on sheaves of sets is exact.
>
> Indeed a right adjoint is representably flat (`RepresentablyFlat.of_isRightAdjoint`: the comma
> category `StructuredArrow X v` has an initial object, namely the unit of the adjunction), so this
> is the criterion of Stacks 00X5 recorded as
> `CategoryTheory.Functor.isMorphismOfSites_of_representablyFlat`.
>
> This is also the first assertion of Stacks 00XY, where the left adjoint `u` is assumed
> cocontinuous: that hypothesis is not needed for it.

```lean
theorem isMorphismOfSites_of_isLeftAdjoint (adj : u ⊣ v) [v.IsContinuous K J] :
    v.IsMorphismOfSites K J
```

**`CategoryTheory.Adjunction.morphismOfTopoiPushforwardIsoOfIsCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean#L98). The attribute's comment: “f\_* = g\_*, where f is the morphism of topoi of the morphism of sites defined by v (constructed by Adjunction.isMorphismOfSites\_of\_isLeftAdjoint) and g that of the cocontinuous u; together with morphismOfTopoiInverseImageIsoOfIsCocontinuous and morphismOfTopoi\_adj\_compatible\_of\_isCocontinuous this is the equality f = g”.

> **Stacks 00XY**, `f_* = g_*`. Let `u : C ⥤ D` be cocontinuous with continuous right adjoint
> `v : D ⥤ C`. Then `v` defines a morphism of sites `f : C → D`
> (`Adjunction.isMorphismOfSites_of_isLeftAdjoint`), and the pushforward `f_* = v^s` of its
> morphism of topoi (Stacks 00XC) is identified with the pushforward `g_* = {}_su` of the morphism
> of topoi `g` of the cocontinuous functor `u` (Stacks 00XO), by the canonical isomorphism
> `(g_*F)(V) = F(v(V))` of Stacks 00XX (1).

```lean
noncomputable def morphismOfTopoiPushforwardIsoOfIsCocontinuous :
    (adj.isMorphismOfSites_of_isLeftAdjoint (J := J) (K := K)).morphismOfTopoi.pushforward ≅
      (u.sheafMorphismOfTopoiCocontinuous J K).pushforward
```

**`CategoryTheory.Adjunction.morphismOfTopoiInverseImageIsoOfIsCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean#L110). The attribute's comment: “f^\{-1} = v\_s = g^\{-1}, the conjugate of the identification f\_* = g\_*”.

> **Stacks 00XY**, `f^{-1} = g^{-1}`. In the situation of
> `morphismOfTopoiPushforwardIsoOfIsCocontinuous`, the inverse image `g^{-1} = (u^p-)^#` of the
> morphism of topoi of `u` is identified with the inverse image `f^{-1} = v_s = (v_p-)^#` of the
> morphism of topoi of the morphism of sites defined by `v`, by the isomorphism conjugate to the
> identification `f_* ≅ g_*` of pushforwards under the adjunctions `f^{-1} ⊣ f_*` and
> `g^{-1} ⊣ g_*`.

```lean
noncomputable def morphismOfTopoiInverseImageIsoOfIsCocontinuous :
    (u.sheafMorphismOfTopoiCocontinuous J K).inverseImage ≅
      (adj.isMorphismOfSites_of_isLeftAdjoint (J := J) (K := K)).morphismOfTopoi.inverseImage
```

**`CategoryTheory.Adjunction.morphismOfTopoi_adj_compatible_of_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfTopoi.lean#L138). The attribute's comment: “f = g: the identifications of pushforwards and inverse images are compatible with the adjunctions of f and g”.

> **Stacks 00XY**, `f = g` as morphisms of topoi. Let `u : C ⥤ D` be cocontinuous with
> continuous right adjoint `v : D ⥤ C`, let `f` be the morphism of topoi of the morphism of sites
> defined by `v` and `g` that of the cocontinuous functor `u`. The identifications `f_* ≅ g_*`
> (`morphismOfTopoiPushforwardIsoOfIsCocontinuous`) and `g^{-1} ≅ f^{-1}`
> (`morphismOfTopoiInverseImageIsoOfIsCocontinuous`) identify the adjunctions as well: for sheaves
> `𝒢` on `D` and `ℱ` on `C`, the bijection `Mor(𝒢, f_*ℱ) = Mor(f^{-1}𝒢, ℱ)` of `f` corresponds to
> the bijection `Mor(𝒢, g_*ℱ) = Mor(g^{-1}𝒢, ℱ)` of `g`.

```lean
theorem morphismOfTopoi_adj_compatible_of_isCocontinuous (𝒢 : Sheaf K (Type u))
    (ℱ : Sheaf J (Type u))
    (α : 𝒢 ⟶
      (adj.isMorphismOfSites_of_isLeftAdjoint (J := J) (K := K)).morphismOfTopoi.pushforward.obj
        ℱ) :
    ((u.sheafMorphismOfTopoiCocontinuous J K).adj.homEquiv 𝒢 ℱ).symm
        (α ≫ (adj.morphismOfTopoiPushforwardIsoOfIsCocontinuous (J := J)).hom.app ℱ) =
      (adj.morphismOfTopoiInverseImageIsoOfIsCocontinuous (J := J)).hom.app 𝒢 ≫
        ((adj.isMorphismOfSites_of_isLeftAdjoint (J := J) (K := K)).morphismOfTopoi.adj.homEquiv
          𝒢 ℱ).symm α
```

## Tag 09VR, a lemma

[Tag 09VR](https://stacks.math.columbia.edu/tag/09VR) in the Stacks Project.

**`CategoryTheory.Adjunction.isCocontinuous_leftAdjoint_of_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean#L43). References: SGA 4 III (2.5), “(i) ⇒ (ii)”.

> **Stacks 09VR(1).** Let `(C, J)` and `(D, K)` be sites, let `v : D ⥤ C` be a continuous
> functor and assume `v` has a left adjoint `u : C ⥤ D`.  Then `u` is cocontinuous.
>
> Cocontinuity of a left adjoint is equivalent to cover preservation of its right adjoint
> (`Adjunction.isCocontinuous_iff_coverPreserving`), and a continuous functor preserves covering
> sieves (`CoverPreserving.of_isContinuous`).

```lean
theorem isCocontinuous_leftAdjoint_of_isContinuous (adj : u ⊣ v) [v.IsContinuous K J] :
    u.IsCocontinuous J K
```

**`CategoryTheory.Adjunction.isMorphismOfSites_of_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean#L61). References: SGA 4 III (2.5), “u^s left exact”.

> **Stacks 09VR, final assertion.** A continuous functor `v : D ⥤ C` which admits a left adjoint
> defines a morphism of sites `f : C → D`, i.e. `v` is continuous and the induced pullback
> `v_s = f⁻¹` on sheaves of sets is exact.
>
> Indeed a right adjoint is representably flat (`RepresentablyFlat.of_isRightAdjoint`: the comma
> category `StructuredArrow X v` has an initial object, namely the unit of the adjunction), so this
> is the criterion of Stacks 00X5 recorded as
> `CategoryTheory.Functor.isMorphismOfSites_of_representablyFlat`.
>
> This is also the first assertion of Stacks 00XY, where the left adjoint `u` is assumed
> cocontinuous: that hypothesis is not needed for it.

```lean
theorem isMorphismOfSites_of_isLeftAdjoint (adj : u ⊣ v) [v.IsContinuous K J] :
    v.IsMorphismOfSites K J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.22, Tag 00XW](https://stacks.math.columbia.edu/tag/00XW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
