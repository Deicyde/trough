---
declaration: section
origin: cited
lean: CategoryTheory.Limits.IsLimit.nonempty_unique_iso, LimitCone, IsLimit.uniqueUpToIso, limit, CategoryTheory.Limits.IsColimit.nonempty_unique_iso, ColimitCocone, colimit, IsColimit.uniqueUpToIso
statement: formalized
proof: formalized
---

# 4.14 Limits and colimits

Section 4.14 of the Stacks Project, [Tag 002D](https://stacks.math.columbia.edu/tag/002D). 11 tags here are carried by 20 declarations of the repository (2 in StacksCore and 18 in StacksFrontier) and 36 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 002E, a definition

[Tag 002E](https://stacks.math.columbia.edu/tag/002E) in the Stacks Project.

**`CategoryTheory.Limits.IsLimit.nonempty_unique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/UniqueUpToUniqueIso.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/UniqueUpToUniqueIso.lean#L31). The attribute's comment: “limits are unique up to unique isomorphism”.

> Two limit cones over the same diagram are isomorphic by exactly one isomorphism of cones:
> the isomorphism `IsLimit.uniqueUpToIso hs ht`, and any other is equal to it.

```lean
theorem IsLimit.nonempty_unique_iso {s t : Cone F} (hs : IsLimit s) (ht : IsLimit t) :
    Nonempty (Unique (s ≅ t))
```

Declarations registered for the tag:

- [`LimitCone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LimitCone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L16) (StacksCore): “Structure for bundled limiting cones”.
- [`IsLimit.uniqueUpToIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLimit.uniqueUpToIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L17) (StacksCore): “uniqueness”.
- [`limit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=limit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L18) (StacksCore): “an arbitrary choice of limit, when one exists”.

## Tag 002F, a definition

[Tag 002F](https://stacks.math.columbia.edu/tag/002F) in the Stacks Project.

**`CategoryTheory.Limits.IsColimit.nonempty_unique_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/UniqueUpToUniqueIso.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/UniqueUpToUniqueIso.lean#L39). The attribute's comment: “colimits are unique up to unique isomorphism”.

> Two colimit cocones under the same diagram are isomorphic by exactly one isomorphism of
> cocones: the isomorphism `IsColimit.uniqueUpToIso hs ht`, and any other is equal to it.

```lean
theorem IsColimit.nonempty_unique_iso {s t : Cocone F} (hs : IsColimit s) (ht : IsColimit t) :
    Nonempty (Unique (s ≅ t))
```

Declarations registered for the tag:

- [`ColimitCocone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ColimitCocone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L20) (StacksCore): “Structure for bundled colimiting cocones”.
- [`colimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colimit#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 21](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L21) (StacksCore): “an arbitrary choice of colimit, when one exists”.
- [`IsColimit.uniqueUpToIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsColimit.uniqueUpToIso#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 22](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L22) (StacksCore): “uniqueness”.

## Tag 002H, a remark

[Tag 002H](https://stacks.math.columbia.edu/tag/002H) in the Stacks Project.

**`CategoryTheory.Limits.IsLimit.mapConeCoyoneda`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean#L43). The attribute's comment: “part 1, for any diagram `M : I ⥤ C` and any limit cone of `M`”.

> If `c` is a limit cone of `M : I ⥤ C`, then for every `W : C` the image of `c` under
> `Hom(W, -)` is a limit cone in sets: `Hom(W, lim M) = lim_i Hom(W, M i)`.

```lean
noncomputable def IsLimit.mapConeCoyoneda {c : Cone M} (hc : IsLimit c) (W : C) :
    IsLimit ((coyoneda.obj (Opposite.op W)).mapCone c)
```

**`CategoryTheory.Limits.IsColimit.mapConeOpYoneda`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean#L51). The attribute's comment: “part 2, for any diagram `M : I ⥤ C` and any colimit cocone; limit over `Iᵒᵖ`”.

> If `c` is a colimit cocone of `M : I ⥤ C`, then for every `W : C` the image of the opposite
> cone `c.op` (over `M.op : Iᵒᵖ ⥤ Cᵒᵖ`) under `Hom(-, W)` is a limit cone in sets:
> `Hom(colim M, W) = lim_{i ∈ Iᵒᵖ} Hom(M i, W)`.

```lean
noncomputable def IsColimit.mapConeOpYoneda {c : Cocone M} (hc : IsColimit c) (W : C) :
    IsLimit ((yoneda.obj W).mapCone c.op)
```

Declarations registered for the tag:

- [`coyoneda_preservesLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=coyoneda_preservesLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L24) (StacksCore): “part 1”.
- [`yoneda_preservesLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=yoneda_preservesLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L25) (StacksCore): “part 2”.
- [`Cone.isLimitCoyonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cone.isLimitCoyonedaEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean#L55) (StacksFrontier): “part 1 determines the limit”.
- [`Cocone.isColimitYonedaEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cocone.isColimitYonedaEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/HomOfLimit.lean#L56) (StacksFrontier): “part 2 determines the colimit”.

## Tag 0G2U, a remark

[Tag 0G2U](https://stacks.math.columbia.edu/tag/0G2U) in the Stacks Project.

Declarations registered for the tag:

- [`Cone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L27) (StacksCore): “structure for cones on a functor”.
- [`Cone.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cone.category#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L28) (StacksCore): “the category structure on cones”.
- [`Cone.isLimitEquivIsTerminal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cone.isLimitEquivIsTerminal#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L29) (StacksCore): “cones are limiting iff they are terminal”.
- [`Cocone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cocone#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L30) (StacksCore): “structure for cocones on a functor”.
- [`Cocone.category`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cocone.category#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L31) (StacksCore): “the category structure on cocones”.
- [`Cocone.isColimitEquivIsInitial`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Cocone.isColimitEquivIsInitial#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L32) (StacksCore): “cocones are limiting iff they are initial”.

## Tag 002I, a definition

[Tag 002I](https://stacks.math.columbia.edu/tag/002I) in the Stacks Project.

Declarations registered for the tag:

- [`Discrete.functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Discrete.functor#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L68) (StacksCore): “The functor that a product of a family of objects is a limit of”.
- [`HasProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasProduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L70) (StacksCore): “Prop-valued typeclass stating that a product exists”.
- [`piObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=piObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L71) (StacksCore): “A choice of product, when one exists”.

## Tag 002J, a definition

[Tag 002J](https://stacks.math.columbia.edu/tag/002J) in the Stacks Project.

Declarations registered for the tag:

- [`Discrete.functor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Discrete.functor#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L73) (StacksCore): “The functor that a coproduct of a family of objects is a colimit of”.
- [`HasCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasCoproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L75) (StacksCore): “Prop-valued typeclass stating that a coproduct exists”.
- [`sigmaObj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=sigmaObj#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/SpecificLimits.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/SpecificLimits.lean#L76) (StacksCore): “A choice of coproduct, when one exists”.

## Tag 002K, a lemma

[Tag 002K](https://stacks.math.columbia.edu/tag/002K) in the Stacks Project.

**`CategoryTheory.Limits.IsColimit.map_unique`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Limits.lean, line 39](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L39). The attribute's comment: “uniqueness”.

```lean
lemma CategoryTheory.Limits.IsColimit.map_unique {J C : Type*} [Category* J] [Category* C]
    (F G : J ⥤ C) {s : Cocone F} (P : IsColimit s) (t : Cocone G) (α : F ⟶ G) {f : s.pt ⟶ t.pt}
    (hf : ∀ i, s.ι.app i ≫ f = α.app i ≫ t.ι.app i) : f = map P t α
```

**`CategoryTheory.Limits.colimit.existsUnique_ι_comp_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/LimitMapAlongFunctor.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/LimitMapAlongFunctor.lean#L50).

> Given diagrams `M : I ⥤ C` and `N : J ⥤ C` with colimits, a functor `H : I ⥤ J` and a
> natural transformation `t : M ⟶ H ⋙ N`, there is a unique morphism
> `θ : colimit M ⟶ colimit N` such that `colimit.ι M i ≫ θ = t.app i ≫ colimit.ι N (H.obj i)` for
> every `i`.

```lean
lemma colimit.existsUnique_ι_comp_eq (M : I ⥤ C) (N : J ⥤ C) [HasColimit M] [HasColimit N]
    (H : I ⥤ J) (t : M ⟶ H ⋙ N) :
    ∃! θ : colimit M ⟶ colimit N, ∀ i, colimit.ι M i ≫ θ = t.app i ≫ colimit.ι N (H.obj i)
```

Declarations registered for the tag:

- [`IsColimit.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsColimit.map#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L34) (StacksCore): “version for `IsColimit`”.
- [`colimMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colimMap#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L35) (StacksCore): “version for `colimit`”.
- [`colim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colim#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L36) (StacksCore): “the resulting functor”.

## Tag 002L, a lemma

[Tag 002L](https://stacks.math.columbia.edu/tag/002L) in the Stacks Project.

**`CategoryTheory.Limits.IsLimit.map_unique`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Limits.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L49). The attribute's comment: “uniqueness”.

```lean
lemma CategoryTheory.Limits.IsLimit.map_unique {J C : Type*} [Category* J] [Category* C]
    (F G : J ⥤ C) (s : Cone F) {t : Cone G} (P : IsLimit t) (α : F ⟶ G) {f : s.pt ⟶ t.pt}
    (hf : ∀ i, f ≫ t.π.app i = s.π.app i ≫ α.app i) : f = map s P α
```

**`CategoryTheory.Limits.limit.existsUnique_comp_π_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/LimitMapAlongFunctor.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/LimitMapAlongFunctor.lean#L35).

> Given diagrams `M : I ⥤ C` and `N : J ⥤ C` with limits, a functor `H : I ⥤ J` and a
> natural transformation `t : H ⋙ N ⟶ M`, there is a unique morphism
> `θ : limit N ⟶ limit M` such that `limit.π N (H.obj i) ≫ t.app i = θ ≫ limit.π M i` for
> every `i`.

```lean
lemma limit.existsUnique_comp_π_eq (M : I ⥤ C) (N : J ⥤ C) [HasLimit M] [HasLimit N]
    (H : I ⥤ J) (t : H ⋙ N ⟶ M) :
    ∃! θ : limit N ⟶ limit M, ∀ i, limit.π N (H.obj i) ≫ t.app i = θ ≫ limit.π M i
```

Declarations registered for the tag:

- [`IsLimit.map`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsLimit.map#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L44) (StacksCore): “version for `IsLimit`”.
- [`limMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=limMap#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 45](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L45) (StacksCore): “version for `limit`”.
- [`lim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=lim#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L46) (StacksCore): “the resulting functor”.

## Tag 002M, a lemma

[Tag 002M](https://stacks.math.columbia.edu/tag/002M) in the Stacks Project.

**`CategoryTheory.Limits.hasColimit_uncurry_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L108). The attribute's comment: “curried form: given each colim\_j, total colimit exists iff iterated one does”.

> **Stacks 002M**, curried form: if each `F.obj i` has a colimit, then `uncurry.obj F` has a
> colimit if and only if `i ↦ colim_j F(i, j)` has one.

```lean
theorem hasColimit_uncurry_iff [∀ i, HasColimit (F.obj i)] :
    HasColimit (uncurry.obj F) ↔ HasColimit (pointwiseColim F)
```

**`CategoryTheory.Limits.colimitUncurryIsoColimitPointwiseColim`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 121](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L121). The attribute's comment: “curried form: the total and iterated colimits agree”.

> **Stacks 002M**, curried form: when they exist, the colimit of `uncurry.obj F` is the
> colimit of `i ↦ colim_j F(i, j)`.

```lean
noncomputable def colimitUncurryIsoColimitPointwiseColim [∀ i, HasColimit (F.obj i)]
    [HasColimit (uncurry.obj F)] [HasColimit (pointwiseColim F)] :
    colimit (uncurry.obj F) ≅ colimit (pointwiseColim F)
```

**`CategoryTheory.Limits.hasColimit_iff_hasColimit_pointwiseColim_curry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L134). The attribute's comment: “given each colim\_j M\_\{i,j}, M has a colimit iff M\_\{-,∞} has one”.

> **Stacks 002M**: for `G : I × J ⥤ C` such that `colim_j G(i, j)` exists for every `i`, the
> functor `G` has a colimit if and only if `i ↦ colim_j G(i, j)` has one.

```lean
theorem hasColimit_iff_hasColimit_pointwiseColim_curry
    [∀ i, HasColimit ((curry.obj G).obj i)] :
    HasColimit G ↔ HasColimit (pointwiseColim (curry.obj G))
```

**`CategoryTheory.Limits.colimitIsoColimitPointwiseColimCurry`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L143). The attribute's comment: “when they exist, the colimits of M and of M\_\{-,∞} agree”.

> **Stacks 002M**: when they exist, `colim_{(i,j)} G(i, j) ≅ colim_i colim_j G(i, j)`.

```lean
noncomputable def colimitIsoColimitPointwiseColimCurry [∀ i, HasColimit ((curry.obj G).obj i)]
    [HasColimit G] [HasColimit (pointwiseColim (curry.obj G))] :
    colimit G ≅ colimit (pointwiseColim (curry.obj G))
```

**`CategoryTheory.Limits.hasColimit_pointwiseColim_curry_swap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L156). The attribute's comment: “given colimits in both variables, colim\_i colim\_j exists iff colim\_j colim\_i does”.

> **Stacks 002M**: if `colim_j G(i, j)` exists for every `i` and `colim_i G(i, j)` exists for
> every `j`, then `colim_i colim_j G(i, j)` exists if and only if `colim_j colim_i G(i, j)` does.

```lean
theorem hasColimit_pointwiseColim_curry_swap_iff [∀ i, HasColimit ((curry.obj G).obj i)]
    [∀ j, HasColimit ((curry.obj (Prod.swap J I ⋙ G)).obj j)] :
    HasColimit (pointwiseColim (curry.obj (Prod.swap J I ⋙ G))) ↔
      HasColimit (pointwiseColim (curry.obj G))
```

**`CategoryTheory.Limits.pointwiseColimCurrySwapIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L166). The attribute's comment: “colim\_j colim\_i = colim\_i colim\_j, given colimits in both variables”.

> **Stacks 002M**: when they exist, `colim_j colim_i G(i, j) ≅ colim_i colim_j G(i, j)`.

```lean
noncomputable def pointwiseColimCurrySwapIso [∀ i, HasColimit ((curry.obj G).obj i)]
    [∀ j, HasColimit ((curry.obj (Prod.swap J I ⋙ G)).obj j)]
    [HasColimit (pointwiseColim (curry.obj G))]
    [HasColimit (pointwiseColim (curry.obj (Prod.swap J I ⋙ G)))] :
    colimit (pointwiseColim (curry.obj (Prod.swap J I ⋙ G))) ≅
      colimit (pointwiseColim (curry.obj G))
```

**`CategoryTheory.Limits.hasLimit_uncurry_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L243). The attribute's comment: “limits, curried form: given each lim\_j, total limit exists iff iterated one does”.

> **Stacks 002M**, curried form for limits: if each `F.obj i` has a limit, then
> `uncurry.obj F` has a limit if and only if `i ↦ lim_j F(i, j)` has one.

```lean
theorem hasLimit_uncurry_iff [∀ i, HasLimit (F.obj i)] :
    HasLimit (uncurry.obj F) ↔ HasLimit (pointwiseLim F)
```

**`CategoryTheory.Limits.limitUncurryIsoLimitPointwiseLim`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L256). The attribute's comment: “limits, curried form: the total and iterated limits agree”.

> **Stacks 002M**, curried form for limits: when they exist, the limit of `uncurry.obj F` is
> the limit of `i ↦ lim_j F(i, j)`.

```lean
noncomputable def limitUncurryIsoLimitPointwiseLim [∀ i, HasLimit (F.obj i)]
    [HasLimit (uncurry.obj F)] [HasLimit (pointwiseLim F)] :
    limit (uncurry.obj F) ≅ limit (pointwiseLim F)
```

**`CategoryTheory.Limits.hasLimit_iff_hasLimit_pointwiseLim_curry`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L269). The attribute's comment: “limits: given each lim\_j M\_\{i,j}, M has a limit iff M\_\{-,∞} has one”.

> **Stacks 002M** for limits: for `G : I × J ⥤ C` such that `lim_j G(i, j)` exists for every
> `i`, the functor `G` has a limit if and only if `i ↦ lim_j G(i, j)` has one.

```lean
theorem hasLimit_iff_hasLimit_pointwiseLim_curry [∀ i, HasLimit ((curry.obj G).obj i)] :
    HasLimit G ↔ HasLimit (pointwiseLim (curry.obj G))
```

**`CategoryTheory.Limits.limitIsoLimitPointwiseLimCurry`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L277). The attribute's comment: “limits: when they exist, the limits of M and of M\_\{-,∞} agree”.

> **Stacks 002M** for limits: when they exist, `lim_{(i,j)} G(i, j) ≅ lim_i lim_j G(i, j)`.

```lean
noncomputable def limitIsoLimitPointwiseLimCurry [∀ i, HasLimit ((curry.obj G).obj i)]
    [HasLimit G] [HasLimit (pointwiseLim (curry.obj G))] :
    limit G ≅ limit (pointwiseLim (curry.obj G))
```

**`CategoryTheory.Limits.hasLimit_pointwiseLim_curry_swap_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L290). The attribute's comment: “limits: given limits in both variables, lim\_i lim\_j exists iff lim\_j lim\_i does”.

> **Stacks 002M** for limits: if `lim_j G(i, j)` exists for every `i` and `lim_i G(i, j)`
> exists for every `j`, then `lim_i lim_j G(i, j)` exists if and only if `lim_j lim_i G(i, j)`
> does.

```lean
theorem hasLimit_pointwiseLim_curry_swap_iff [∀ i, HasLimit ((curry.obj G).obj i)]
    [∀ j, HasLimit ((curry.obj (Prod.swap J I ⋙ G)).obj j)] :
    HasLimit (pointwiseLim (curry.obj (Prod.swap J I ⋙ G))) ↔
      HasLimit (pointwiseLim (curry.obj G))
```

**`CategoryTheory.Limits.pointwiseLimCurrySwapIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Limits/Fubini.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/Fubini.lean#L299). The attribute's comment: “limits: lim\_j lim\_i = lim\_i lim\_j, given limits in both variables”.

> **Stacks 002M** for limits: when they exist, `lim_j lim_i G(i, j) ≅ lim_i lim_j G(i, j)`.

```lean
noncomputable def pointwiseLimCurrySwapIso [∀ i, HasLimit ((curry.obj G).obj i)]
    [∀ j, HasLimit ((curry.obj (Prod.swap J I ⋙ G)).obj j)]
    [HasLimit (pointwiseLim (curry.obj G))]
    [HasLimit (pointwiseLim (curry.obj (Prod.swap J I ⋙ G)))] :
    limit (pointwiseLim (curry.obj (Prod.swap J I ⋙ G))) ≅
      limit (pointwiseLim (curry.obj G))
```

Declarations registered for the tag:

- [`Adjunction.colim_preservesColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.colim_preservesColimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 54](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L54) (StacksCore): “the colimit functor preserves colimits”.
- [`colimitIsoColimitCurryCompColim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colimitIsoColimitCurryCompColim#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L55) (StacksCore): “explicit isomorphism for uncurried functors”.
- [`Adjunction.lim_preservesLimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Adjunction.lim_preservesLimits#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L56) (StacksCore): “the limit functor preserves limits”.
- [`limitIsoLimitCurryCompLim`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=limitIsoLimitCurryCompLim#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L57) (StacksCore): “explicit isomorphism for uncurried functors”.

## Tag 002N, a lemma

[Tag 002N](https://stacks.math.columbia.edu/tag/002N) in the Stacks Project.

Declarations registered for the tag:

- [`limitConeOfEqualizerAndProduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=limitConeOfEqualizerAndProduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L59) (StacksCore).
- [`HasLimitOfHasProductsOfHasEqualizers.buildIsLimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=HasLimitOfHasProductsOfHasEqualizers.buildIsLimit#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/LimitOfProductsAndEqualizer.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/LimitOfProductsAndEqualizer.lean#L29) (StacksFrontier): “the equalizer of the two maps between the products is the limit, assuming just the two products and the one equalizer exist”.

## Tag 002P, a lemma

[Tag 002P](https://stacks.math.columbia.edu/tag/002P) in the Stacks Project.

Declarations registered for the tag:

- [`colimitCoconeOfCoequalizerAndCoproduct`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=colimitCoconeOfCoequalizerAndCoproduct#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Limits.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Limits.lean#L61) (StacksCore).
- [`CategoryTheory.Limits.HasColimitOfHasCoproductsOfHasCoequalizers.buildIsColimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasColimitOfHasCoproductsOfHasCoequalizers.buildIsColimit#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Limits/ColimitFromCoproductsCoequalizer.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Limits/ColimitFromCoproductsCoequalizer.lean#L31) (StacksFrontier): “exactly the source's hypotheses: the coequalizer of the two maps between the two given coproducts is the colimit”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.14, Tag 002D](https://stacks.math.columbia.edu/tag/002D)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
