---
declaration: section
origin: cited
lean: preservesFiniteLimits_sheafToPresheaf_comp_stalk, StacksStalk.nbh_isCofiltered, StacksStalk.sheafStalkFunctor_preservesFiniteLimits, CategoryTheory.GrothendieckTopology.Point.ofPreservesFiniteLimits, CategoryTheory.GrothendieckTopology.Point.equivFiber, CategoryTheory.GrothendieckTopology.SitePoint.exists_fiber_eq_iff, CategoryTheory.GrothendieckTopology.SitePoint.equivFiber, CategoryTheory.WeakPullbacksNotPoint.exists_site_weakly_left_exact_not_point
statement: formalized
proof: formalized
---

# 7.33 Constructing points

Section 7.33 of the Stacks Project, [Tag 05UZ](https://stacks.math.columbia.edu/tag/05UZ). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0F4E, a lemma

[Tag 0F4E](https://stacks.math.columbia.edu/tag/0F4E) in the Stacks Project.

**`preservesFiniteLimits_sheafToPresheaf_comp_stalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkIso.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkIso.lean#L33). The attribute's comment: “The stalk functor is written as `sheafToPresheaf` followed by the colimit over the opposite of the category of neighbourhoods `u.Elements`; `u` is any functor with `IsCofiltered u.Elements`.”.

> **Stacks 0F4E.** Let `(C, J)` be a site and `u : C ⥤ Type u` a functor whose category of
> neighbourhoods `u.Elements` (pairs `(U, x)` with `x ∈ u(U)`) is cofiltered. Then the stalk functor
> `Sh(C) ⥤ Set`, sending a sheaf `𝓕` to `colim_{(U, x) ∈ u.Elementsᵒᵖ} 𝓕(U)` (Stacks 04EH), is left
> exact, i.e. it preserves finite limits. Exactly the Stacks hypotheses: `u` is an arbitrary functor
> with cofiltered category of neighbourhoods, and no covering condition on `u` is required.

```lean
theorem preservesFiniteLimits_sheafToPresheaf_comp_stalk
    {C : Type u} [SmallCategory C] (J : GrothendieckTopology C)
    (u : C ⥤ Type u) [IsCofiltered u.Elements] :
    Limits.PreservesFiniteLimits (sheafToPresheaf J (Type u) ⋙
      (Functor.whiskeringLeft _ _ (Type u)).obj (CategoryOfElements.π u).op ⋙ Limits.colim)
```

## Tag 00YB, a lemma

[Tag 00YB](https://stacks.math.columbia.edu/tag/00YB) in the Stacks Project.

**`StacksStalk.nbh_isCofiltered`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean#L70). The attribute's comment: “(1)”. References: SGA 4 IV (6.8.2), “special case”; SGA 4 IV (6.8.5), “partial”.

> Statement 1 (Main, tag `00YB`): under the hypotheses, the category of
> neighbourhoods `Nbh(p)` of `p` is cofiltered.

```lean
theorem nbh_isCofiltered [HasTerminal C] [HasPullbacks C]
    (u : C ⥤ Type w) (hu : IsPoint u) : IsCofiltered u.Elements
```

**`StacksStalk.sheafStalkFunctor_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean, line 106](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/NeighbourhoodsCofiltered.lean#L106). The attribute's comment: “(2)”.

> Statement 2 (Consequence, tag `00YB`): under the hypotheses, the stalk
> functor on sheaves commutes with finite limits, i.e. it is left exact.

```lean
theorem sheafStalkFunctor_preservesFiniteLimits
    [HasTerminal C] [HasPullbacks C] (J : GrothendieckTopology C)
    (u : C ⥤ Type w) (hu : IsPoint u) :
    PreservesFiniteLimits
      (sheafToPresheaf J (Type w) ⋙ CategoryTheory.elementColimit u (Type w))
```

## Tag 00YC, a proposition

[Tag 00YC](https://stacks.math.columbia.edu/tag/00YC) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.ofPreservesFiniteLimits`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean#L110). The attribute's comment: “the direction (1) and (2) ⇒ point, for Mathlib's points; the equivalence for the points of 00Y5 is `SitePoint.exists_fiber_eq_iff`”. References: SGA 4 IV (6.3), “left exact ⇒ point”.

> On a site in which finite limits exist, the point with fiber functor `u : C ⥤ Type w`, for
> `u` commuting with finite limits, with initially small category of elements, and jointly
> surjective on covering sieves.
>
> This is the direction "(1) and (2) imply a point" of Stacks 00YC for points in Mathlib's sense;
> the equivalence for the points of Stacks 00Y5 is
> `GrothendieckTopology.SitePoint.exists_fiber_eq_iff`.

```lean
def ofPreservesFiniteLimits (u : C ⥤ Type w) [PreservesFiniteLimits u]
    [InitiallySmall.{w} u.Elements] (hu : u.CoveringJointlySurjective J) :
    Point.{w} J
```

**`CategoryTheory.GrothendieckTopology.Point.equivFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OfPreservesFiniteLimits.lean#L133). The attribute's comment: “the bijection, for Mathlib's points (with initially small category of elements)”. References: SGA 4 IV (6.3), “characterization”.

> Let `C` be a site in which finite limits exist. Then the points of `C`
> correspond bijectively to the functors `u : C ⥤ Type w` such that
>
> 1. `u` commutes with finite limits, and
> 2. `∐ u(U_i) → u(U)` is surjective for every covering `{U_i → U}`
>    (in the sieve form `Functor.CoveringJointlySurjective`), and whose category of elements is
>    initially small,
>
> the bijection being `Φ ↦ Φ.fiber` in one direction and `ofPreservesFiniteLimits` in the
> other. This is Stacks 00YC for points in Mathlib's sense; for the points of Stacks 00Y5 see
> `GrothendieckTopology.SitePoint.exists_fiber_eq_iff` and
> `GrothendieckTopology.SitePoint.equivFiber`.

```lean
noncomputable def equivFiber :
    Point.{w} J ≃ {u : C ⥤ Type w //
      InitiallySmall.{w} u.Elements ∧ PreservesFiniteLimits u ∧
        u.CoveringJointlySurjective J}
```

**`CategoryTheory.GrothendieckTopology.SitePoint.exists_fiber_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePointOfPreservesFiniteLimits.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePointOfPreservesFiniteLimits.lean#L95). The attribute's comment: “the equivalence, for the points of Stacks 00Y5”.

> **Stacks 00YC.** Let `C` be a site in which finite limits exist. A functor
> `u : C ⥤ Type w` is a point of `C` (Stacks 00Y5) if and only if
>
> 1. `u` commutes with finite limits, and
> 2. for every covering `{U_i → U}` the map `∐ u(U_i) → u(U)` is surjective.

```lean
theorem exists_fiber_eq_iff (u : C ⥤ Type w) :
    (∃ p : J.SitePoint, p.fiber = u) ↔
      PreservesFiniteLimits u ∧
        ∀ {I : Type w} {U : C} {Ui : I → C} (f : ∀ i, Ui i ⟶ U),
          Sieve.ofArrows Ui f ∈ J U → ∀ x : u.obj U,
            ∃ (i : I) (y : u.obj (Ui i)), u.map (f i) y = x
```

**`CategoryTheory.GrothendieckTopology.SitePoint.equivFiber`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePointOfPreservesFiniteLimits.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePointOfPreservesFiniteLimits.lean#L118). The attribute's comment: “the bijection between points and the functors satisfying (1) and (2)”.

> **Stacks 00YC.** On a site in which finite limits exist, the points of Stacks 00Y5
> correspond bijectively, by `p ↦ u`, to the functors `u : C ⥤ Type w` which commute with finite
> limits and for which `∐ u(U_i) → u(U)` is surjective for every covering `{U_i → U}`.

```lean
noncomputable def equivFiber :
    J.SitePoint ≃ {u : C ⥤ Type w // PreservesFiniteLimits u ∧
        ∀ {I : Type w} {U : C} {Ui : I → C} (f : ∀ i, Ui i ⟶ U),
          Sieve.ofArrows Ui f ∈ J U → ∀ x : u.obj U,
            ∃ (i : I) (y : u.obj (Ui i)), u.map (f i) y = x}
```

## Tag 00YD, a remark

[Tag 00YD](https://stacks.math.columbia.edu/tag/00YD) in the Stacks Project.

**`CategoryTheory.WeakPullbacksNotPoint.exists_site_weakly_left_exact_not_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/WeakPullbacksNotPoint.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/WeakPullbacksNotPoint.lean#L326). The attribute's comment: “the remark's assertion. The source's example (two objects `U → X`, `u(U)` with two elements) fails (2) at `U ×_X U = U`; corrected example: finite sets with the trivial topology and `u` the nonempty-subsets functor”.

> **Stacks 00YD.** There is a site `C` with a final object and fibre products, and a functor
> `u : C ⥤ Set` such that
>
> 1. `u(⊤) = {*}` is a singleton,
> 2. for every pair `U → W ← V` the map `u(U ×_W V) → u(U) ×_{u(W)} u(V)` is surjective,
> 3. for every covering `{U_i → U}` the map `∐ u(U_i) → u(U)` is surjective,
>
> but `u` is not a point: no point of `C` (Stacks 00Y5) has fiber functor `u`, and the stalk
> functor `Sh(C) ⥤ Set`, `F ↦ F_p` (Stacks 04EH), is not left exact.
>
> The example is the skeleton of the category of finite sets with the trivial topology and `u` the
> nonempty-subsets functor; the example given in the source fails (2).

```lean
theorem exists_site_weakly_left_exact_not_point :
    ∃ (C : Type) (_ : SmallCategory C) (J : GrothendieckTopology C) (_ : HasTerminal C)
      (_ : HasPullbacks C) (u : C ⥤ Type),
      Nonempty (Unique (u.obj (⊤_ C))) ∧
      (∀ {U V W : C} (f : U ⟶ W) (g : V ⟶ W), Function.Surjective (pullbackComparison u f g)) ∧
      (∀ {I : Type} {U : C} {Ui : I → C} (f : ∀ i, Ui i ⟶ U), Sieve.ofArrows Ui f ∈ J U →
        ∀ x : u.obj U, ∃ (i : I) (y : u.obj (Ui i)), u.map (f i) y = x) ∧
      (¬ ∃ Φ : J.Point.{0}, Nonempty (Φ.fiber ≅ u)) ∧
      ¬ PreservesFiniteLimits (sheafToPresheaf J Type ⋙ presheafStalk u)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.33, Tag 05UZ](https://stacks.math.columbia.edu/tag/05UZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
