---
declaration: section
origin: cited
lean: CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction, CategoryTheory.Functor.sheafPullbackCocontinuousIsoLan, morphismOfTopoiPushforwardIso, CategoryTheory.Adjunction.isCocontinuous_leftAdjoint_of_isContinuous, CategoryTheory.Adjunction.isMorphismOfSites_of_isLeftAdjoint
statement: formalized
proof: formalized
---

# 7.22 Cocontinuous functors which have a right adjoint

Section 7.22 of the Stacks Project, [Tag 00XW](https://stacks.math.columbia.edu/tag/00XW). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00XX, a lemma

[Tag 00XX](https://stacks.math.columbia.edu/tag/00XX) in the Stacks Project.

**`CategoryTheory.Functor.sheafPushforwardCocontinuousIsoRestriction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L229). The attribute's comment: “(1)”.

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

**`CategoryTheory.Functor.sheafPullbackCocontinuousIsoLan`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CoverLifting.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CoverLifting.lean#L249). The attribute's comment: “(2)”.

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

**`morphismOfTopoiPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfSites.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/CocontinuousRightAdjointMorphismOfSites.lean#L85). The attribute's comment: “Equality of the two morphisms of topoi is recorded as an isomorphism of their pushforwards; that the continuous right adjoint `v` does define a morphism of sites is the hypothesis `h`.”.

> **Stacks 00XY.** Let `(C, J)` and `(D, K)` be sites, let `u : C ⥤ D` be cocontinuous with
> right adjoint `v : D ⥤ C`, and let `g : Sh(C) → Sh(D)` be the morphism of topoi attached to `u`
> (Stacks 00XO), so that `g_* = {}_su` is `u.sheafPushforwardCocontinuous`.
>
> If `v` is continuous it defines a morphism of sites `f : C → D` (Stacks 00X1), the hypothesis
> `h`, and the morphism of topoi attached to `f` (Stacks 00XC) is `g`: the two pushforwards
> `f_* = v^s` and `g_*` are isomorphic.

```lean
public noncomputable def morphismOfTopoiPushforwardIso
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D}
    {u : C ⥤ D} {v : D ⥤ C} (adj : u ⊣ v) [u.IsCocontinuous J K]
    (h : v.IsMorphismOfSites K J) :
    h.morphismOfTopoi.pushforward ≅ u.sheafPushforwardCocontinuous (Type u) J K
```

## Tag 09VR, a lemma

[Tag 09VR](https://stacks.math.columbia.edu/tag/09VR) in the Stacks Project.

**`CategoryTheory.Adjunction.isCocontinuous_leftAdjoint_of_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean, line 43](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean#L43). References: SGA 4 III (2.5), “(i) ⇒ (ii)”.

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

**`CategoryTheory.Adjunction.isMorphismOfSites_of_isLeftAdjoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExistence.lean#L57). References: SGA 4 III (2.5), “u^s left exact”.

> **Stacks 09VR, final assertion.** A continuous functor `v : D ⥤ C` which admits a left adjoint
> defines a morphism of sites `f : C → D`, i.e. `v` is continuous and the induced pullback
> `v_s = f⁻¹` on sheaves of sets is exact.
>
> Indeed a right adjoint is representably flat (`RepresentablyFlat.of_isRightAdjoint`: the comma
> category `StructuredArrow X v` has an initial object, namely the unit of the adjunction), so this
> is the criterion of Stacks 00X5 recorded as
> `CategoryTheory.Functor.isMorphismOfSites_of_representablyFlat`.

```lean
theorem isMorphismOfSites_of_isLeftAdjoint (adj : u ⊣ v) [v.IsContinuous K J] :
    v.IsMorphismOfSites K J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.22, Tag 00XW](https://stacks.math.columbia.edu/tag/00XW)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
