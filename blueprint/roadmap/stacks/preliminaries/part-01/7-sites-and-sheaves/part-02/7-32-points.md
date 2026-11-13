---
declaration: section
origin: cited
lean: PointOfTopos, CategoryTheory.Functor.presheafStalk, CategoryTheory.Functor.toPresheafStalk, CategoryTheory.Functor.toPresheafStalk_w, CategoryTheory.Functor.presheafStalkFunctor, CategoryTheory.Functor.presheafStalkEquivColimitType, CategoryTheory.GrothendieckTopology.Point.presheafFiber, CategoryTheory.GrothendieckTopology.Point.toPresheafFiber
statement: formalized
proof: formalized
---

# 7.32 Points

Section 7.32 of the Stacks Project, [Tag 00Y3](https://stacks.math.columbia.edu/tag/00Y3). 12 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00Y4, a definition

[Tag 00Y4](https://stacks.math.columbia.edu/tag/00Y4) in the Stacks Project.

**`PointOfTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Defs.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Defs.lean#L27). References: SGA 4 IV (6.1).

> A *point of the topos* `Sh(C, J)` is a morphism of topoi `p : Sh(pt) → Sh(C, J)`, where
> `Sh(pt) = Sets` is modelled by `Type w`. Concretely, a point is an adjoint pair `p⁻¹ ⊣ p_*` with
> `p⁻¹ : Sh(C, J) ⥤ Type w` (the stalk functor) and `p_* : Type w ⥤ Sh(C, J)` (the skyscraper
> functor), such that `p⁻¹` is left exact.

```lean
def PointOfTopos.{w, v, u} {C : Type u} [Category.{v} C] (J : GrothendieckTopology C) : Type _
```

## Tag 04EH, an equation

[Tag 04EH](https://stacks.math.columbia.edu/tag/04EH) in the Stacks Project.

**`CategoryTheory.Functor.presheafStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean#L57). The attribute's comment: “The stalk `F_p = colim_{{(U, x)}^opp} F(U)` of a presheaf at an arbitrary functor `p = u : C → Sets`, with no conditions on `u`; the presheaf takes values in any category `A` in which this colimit exists (the case of presheaves of sets is `A := Type _`, see `presheafStalkEquivColimitType`).”.

> The stalk `F_u = colim_{{(U, x)}ᵒᵖ} F(U)` of a presheaf `F` at an arbitrary functor
> `u : C ⥤ Type w`: the colimit of `F(U)` over the opposite of the category of neighbourhoods
> `(U, x)`, `x ∈ u(U)`, of `u`.

```lean
noncomputable def presheafStalk (F : Cᵒᵖ ⥤ A) [HasColimit ((CategoryOfElements.π u).op ⋙ F)] : A
```

**`CategoryTheory.Functor.toPresheafStalk`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean#L62). The attribute's comment: “The canonical map `F(U) → F_p` sending `s` to the class of `(U, x, s)`.”.

> The canonical map `F(U) ⟶ F_u` attached to a neighbourhood `(U, x)` of `u`.

```lean
noncomputable def toPresheafStalk (U : C) (x : u.obj U) (F : Cᵒᵖ ⥤ A)
    [HasColimit ((CategoryOfElements.π u).op ⋙ F)] : F.obj (op U) ⟶ u.presheafStalk F
```

**`CategoryTheory.Functor.toPresheafStalk_w`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean#L71). The attribute's comment: “The relation `(U, x, s) ∼ (V, y, α^* s)` for a morphism of neighbourhoods `α : (V, y) → (U, x)`.”.

> The canonical maps are compatible with morphisms of neighbourhoods: for
> `α : (V, y) ⟶ (U, x)`, i.e. `α : V ⟶ U` with `u(α)(y) = x`, the class of `(U, x, s)` equals the
> class of `(V, y, α^* s)`.

```lean
theorem toPresheafStalk_w {V U : C} (α : V ⟶ U) (y : u.obj V) (F : Cᵒᵖ ⥤ A)
    [HasColimit ((CategoryOfElements.π u).op ⋙ F)] :
    F.map α.op ≫ u.toPresheafStalk V y F = u.toPresheafStalk U (u.map α y) F
```

**`CategoryTheory.Functor.presheafStalkFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean#L87). The attribute's comment: “The stalk functor `PSh(C) → Sets`, `F ↦ F_p`, here for presheaves with values in a category `A` with colimits of shape `u.Elementsᵒᵖ`.”.

> The stalk functor `PSh(C, A) ⥤ A`, `F ↦ F_u`, at an arbitrary functor `u : C ⥤ Type w`.

```lean
noncomputable def presheafStalkFunctor [HasColimitsOfShape u.Elementsᵒᵖ A] :
    (Cᵒᵖ ⥤ A) ⥤ A
```

**`CategoryTheory.Functor.presheafStalkEquivColimitType`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean, line 114](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/StalkAtFunctor.lean#L114). The attribute's comment: “Description of the stalk of a presheaf of sets: elements are triples `(U, x, s)` modulo the equivalence relation generated by `(U, x, s) ∼ (V, y, α^* s)`.”.

> For a presheaf of sets, an element of the stalk `F_u` is the class of a triple `(U, x, s)`
> with `(U, x)` a neighbourhood of `u` and `s ∈ F(U)`, for the equivalence relation generated by
> `(U, x, s) ∼ (V, y, α^* s)`: the quotient `Functor.ColimitType` of the diagram
> `(CategoryOfElements.π u).op ⋙ F`.

```lean
noncomputable def presheafStalkEquivColimitType :
    u.presheafStalk F ≃ ((CategoryOfElements.π u).op ⋙ F).ColimitType
```

Declarations registered for the tag:

- [`CategoryTheory.GrothendieckTopology.Point.presheafFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.presheafFiber#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 28](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L28) (StacksCore): “the stalk `F_p = colim_{{(U, x)}ᵒᵖ} F(U)` of a presheaf at a point of a site”. References: SGA 4 IV (6.8.7), “special case”; SGA 4 IV (6.10), “more general”; SGA 4 VIII (7.9.3).
- [`CategoryTheory.GrothendieckTopology.Point.toPresheafFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.toPresheafFiber#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 30](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L30) (StacksCore): “the canonical map `F(U) ⟶ F_p` attached to a neighbourhood `(U, x)` of the point”.
- [`CategoryTheory.GrothendieckTopology.Point.toPresheafFiber_w`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GrothendieckTopology.Point.toPresheafFiber_w#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Sites/Point/StalkAsColimit.lean#L32) (StacksCore): “the canonical maps are compatible with morphisms of neighbourhoods”.

## Tag 00Y5, a definition

[Tag 00Y5](https://stacks.math.columbia.edu/tag/00Y5) in the Stacks Project.

**`Stacks.IsSitePoint.toPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/AbelianStalkExactSitePoints.lean#L185). The attribute's comment: “a Stacks point gives a Mathlib `GrothendieckTopology.Point` with fibre `u`”.

> **A point in the sense of Stacks 00Y5 is a point in the sense of Mathlib**, with the same
> fibre functor `u`. Its category of elements is cofiltered because the stalk functor is left
> exact (condition (3)).

```lean
def toPoint : K.toGrothendieck.Point.{w}
```

**`CategoryTheory.Functor.IsPointOfSite`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/IsPointOfSite.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/IsPointOfSite.lean#L97). The attribute's comment: “Stacks' definition, with conditions (1), (2) and (3) as fields; it is identified with Mathlib's `GrothendieckTopology.Point` by `Functor.isPointOfSite_iff_exists_point` and `Functor.pointOfSiteEquiv`.”.

> **Stacks 00Y5.** A *point* of the site `(C, J)` is a functor `u : C ⥤ Set` such that
>
> 1. for every covering `{U_i → U}` the map `∐ u(U_i) → u(U)` is surjective;
> 2. for every covering `{U_i → U}` and every morphism `V → U` the maps
>    `u(U_i ×_U V) → u(U_i) ×_{u(U)} u(V)` are bijective;
> 3. the stalk functor `Sh(C) ⥤ Set`, `F ↦ F_p`, is left exact, where `F_p` is the colimit of the
>    sections `F(U)` over the opposite of the category of neighbourhoods `(U, x)`, `x ∈ u(U)`
>    (`PresheafPushforwardStalkAdjunction.presheafStalk`, Stacks 04EH).
>
> A covering is a family `{U_i → U}` whose generated sieve is `J`-covering. That this is the same
> notion as Mathlib's `GrothendieckTopology.Point` is `Functor.isPointOfSite_iff_exists_point`.

```lean
structure Functor.IsPointOfSite (u : C ⥤ Type w) (J : GrothendieckTopology C) : Prop
```

**`CategoryTheory.Precoverage.Point`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PrecoveragePoint.lean#L88). The attribute's comment: “The source's definition, for a site given by its covering families.”.

> A *point* of the site `(C, K)` (Stacks 00Y5): a functor `u : C ⥤ Type u` such that
>
> 1. for every covering `R` of `X` the elements of `u(X)` all come from the members of `R`, i.e.
>    `∐ u(U_i) → u(X)` is surjective;
> 2. for every covering `R` of `X`, every member `f : Y ⟶ X` of `R` and every `g : Z ⟶ X`, the map
>    `u(Y ×_X Z) → u(Y) ×_{u(X)} u(Z)` is bijective;
> 3. the stalk functor `F ↦ F_p` on sheaves of sets is left exact, the stalk being the colimit
>    `PresheafPushforwardStalkAdjunction.presheafStalk u` of the sections of `F` over the opposite
>    of the category of elements of `u` (Stacks 04EH).

```lean
structure Point
```

**`CategoryTheory.GrothendieckTopology.SitePoint`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/SitePoint.lean#L101).

> **Stacks 00Y5.** A point of the site `(C, J)`: a functor `u : C ⥤ Type w` such that
>
> 1. for every covering `{U_i → U}` the map `∐ u(U_i) → u(U)` is surjective;
> 2. for every covering `{U_i → U}` and every morphism `V → U` the maps
>    `u(U_i ×_U V) → u(U_i) ×_{u(U)} u(V)` are bijective;
> 3. the stalk functor `Sh(C) ⥤ Sets`, `F ↦ F_p`, is left exact.
>
> A covering is a family of morphisms indexed by a set whose sieve covers for `J`.

```lean
structure SitePoint
```

## Tag 00Y6, a lemma

[Tag 00Y6](https://stacks.math.columbia.edu/tag/00Y6) in the Stacks Project.

**`Phi_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean#L44). The attribute's comment: “isomorphism”.

> **Stacks 00Y6.** The canonical map `Φ_U : p U ⟶ (h_U)_p` from the value of the point at `U`
> to the stalk of the representable presheaf `h_U` is bijective.

```lean
theorem Phi_bijective (p : C ⥤ Type u) (U : C) :
    Function.Bijective (theta p U)
```

**`Phi_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkFunctor.lean#L52). The attribute's comment: “functoriality”.

> **Stacks 00Y6.** The maps `Φ_U` are natural in `U`: they commute with `p.map g` on the source
> and with the stalk of `yoneda.map g` on the target.

```lean
theorem Phi_naturality (p : C ⥤ Type u) {U U' : C} (g : U ⟶ U') (x : p.obj U) :
    theta p U' (p.map g x) = (presheafStalk p).map (yoneda.map g) (theta p U x)
```

## Tag 04EI, an equation

[Tag 04EI](https://stacks.math.columbia.edu/tag/04EI) in the Stacks Project.

**`pushforwardPresheaf04EI`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PresheafPushforwardPoint.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PresheafPushforwardPoint.lean#L27). References: SGA 4 I (1.3), “special case”.

> **Stacks 04EI.** The presheaf `u^p E` attached to a functor `u : C ⥤ Type` and a type `E`:
> it sends an object `U` to the type of functions `u U → E`, and a morphism `f : V ⟶ U` to
> precomposition with `u f`.

```lean
def pushforwardPresheaf04EI {C : Type u} [Category.{v} C] (u : Functor C (Type v)) (E : Type v) :
    Functor Cᵒᵖ (Type v)
```

## Tag 00Y7, a lemma

[Tag 00Y7](https://stacks.math.columbia.edu/tag/00Y7) in the Stacks Project.

**`PresheafPushforwardStalkAdjunction.presheafStalk_adjoint_presheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkLeftAdjoint.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkLeftAdjoint.lean#L297).

> **Stacks 00Y7.** For any functor `u : C ⥤ Type w` such that the
> appropriate colimits exist, the pushforward functor `presheafPushforward u`
> is a right adjoint to the stalk functor `presheafStalk u`.

```lean
theorem presheafStalk_adjoint_presheafPushforward
    (u : C ⥤ Type w)
    [HasColimitsOfShape u.Elementsᵒᵖ (Type w)] :
    Nonempty (presheafStalk u ⊣ presheafPushforward u)
```

## Tag 00Y8, a lemma

[Tag 00Y8](https://stacks.math.columbia.edu/tag/00Y8) in the Stacks Project.

**`PresheafPushforwardStalkAdjunction.isSheaf_presheafPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean#L63). The attribute's comment: “(1): `u^p E` is a sheaf for every set `E`”.

> **Stacks 00Y8 (1).** If `u : C ⥤ Type w` satisfies conditions (a) and (b) for every covering
> of the site, then the presheaf `u^p E : U ↦ Map(u(U), E)` is a sheaf for every set `E`.

```lean
theorem isSheaf_presheafPushforward (h : StalkConditions K u) (E : Type w) :
    Presheaf.IsSheaf K.toGrothendieck ((presheafPushforward u).obj E)
```

**`PresheafPushforwardStalkAdjunction.sheafStalk_adjoint_skyscraper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean#L125). The attribute's comment: “(2): the stalk functor on sheaves is left adjoint to `u^s`”.

> **Stacks 00Y8 (2).** If `u : C ⥤ Type w` satisfies conditions (a) and (b) for every covering
> of the site, then the stalk functor `Sh(C) → Sets`, `F ↦ F_p`, is left adjoint to
> `u^s : Sets → Sh(C)`.

```lean
theorem sheafStalk_adjoint_skyscraper [Limits.HasColimitsOfShape u.Elementsᵒᵖ (Type w)]
    (h : StalkConditions K u) : Nonempty (sheafStalk K u ⊣ skyscraper h)
```

**`PresheafPushforwardStalkAdjunction.isIso_presheafStalk_map_toSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/StalkOfCoveringFunctor.lean#L133). The attribute's comment: “(3): the canonical map `F_p → (F^#)_p` is an isomorphism”.

> **Stacks 00Y8 (3).** If `u : C ⥤ Type w` satisfies conditions (a) and (b) for every covering
> of the site, then for every presheaf of sets `F` the canonical map `F_p → (F^#)_p`, the stalk of
> the sheafification map `F → F^#`, is an isomorphism.

```lean
theorem isIso_presheafStalk_map_toSheafify [Limits.HasColimitsOfShape u.Elementsᵒᵖ (Type w)]
    [HasWeakSheafify K.toGrothendieck (Type w)] (h : StalkConditions K u)
    (F : Cᵒᵖ ⥤ Type w) :
    IsIso ((presheafStalk u).map (toSheafify K.toGrothendieck F))
```

## Tag 00Y9, a definition

[Tag 00Y9](https://stacks.math.columbia.edu/tag/00Y9) in the Stacks Project.

**`pushforwardPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/PushforwardPoint.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/PushforwardPoint.lean#L27). References: EGA IV (21.9.1), “more general”.

> **Stacks 00Y9.** The pushforward `p_* E` of an object `E` along a point `p` of the site
> `(C, J)`: the skyscraper sheaf at `p` with value `E`.

```lean
noncomputable def pushforwardPoint
    {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (p : J.Point) {A : Type*} [Category A] [Limits.HasProducts A] (E : A) :
    Sheaf J A
```

## Tag 00YA, a lemma

[Tag 00YA](https://stacks.math.columbia.edu/tag/00YA) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.targetSitePoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/TargetSitePoint.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/TargetSitePoint.lean#L107). The attribute's comment: “(2), applied to the composite of a point of the source site with a morphism of ringed topoi”.

> **Stacks 00YA (2) along a morphism of ringed topoi.** The point of the target site `(D, K)`
> whose stalk functor is the inverse image along `f` followed by the stalk functor of the point
> `Φ` of the source site.

```lean
def targetSitePoint (f : RingedToposHom X Y) (Φ : X.J.Point.{w}) : Y.J.Point.{w}
```

**`CategoryTheory.GrothendieckTopology.Point.pointOfTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 303](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L303). The attribute's comment: “(1): a point of the site defines a morphism of topoi `Sh(pt) → Sh(C)`”. References: SGA 4 IV (6.8.7), “(ii)”; SGA 4 IV (7.1), “more general”.

> **Stacks 00YA (1).** Let `p` be a point of the site `C`, given by a fibre functor
> `u = Φ.fiber`. Then the pair of functors `(p\_*, p^\{-1}) = (Φ.skyscraperSheafFunctor,
> Φ.sheafFiber)` is a morphism of topoi `Sh(pt) → Sh(C)`, i.e. a point of the topos `Sh(C)` in
> the sense of Stacks 00Y4.
>
> The two functors are adjoint by `Point.skyscraperSheafAdjunction`, and `p^{-1}` is left exact
> by `Point.sheafFiber_leftExact` (Stacks 00Y5 (3)), which are exactly the two conditions in the
> definition of a morphism of topoi (Stacks 00XA).

```lean
noncomputable def pointOfTopos (Φ : Point.{w} J) : PointOfTopos.{w, v, u} J
```

**`CategoryTheory.GrothendieckTopology.Point.sheafFiberComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L381). The attribute's comment: “(2): the canonical comparison from the reconstructed stalk functor”.

> The canonical comparison from the stalk functor to `F`, induced by a natural
> transformation on the sheafified representables. On a germ `(U, x, σ)` it is
> `F(σ)(α_U(x))`, viewing the section `σ` as a map out of `h_U^#`.

```lean
noncomputable def sheafFiberComparison : Φ.sheafFiber ⟶ F
```

**`PointOfTopos.exists_sitePoint_fiber_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 532](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L532). The attribute's comment: “(2): reconstruction of the site point”.

> **Stacks 00YA (2).** Every point `p` of the topos arises from a point of the site
> whose fiber functor is `U ↦ p⁻¹(h_U^#)` on the nose.
>
> `PointOfTopos.exists_sitePoint` is the same reconstruction stated up to isomorphism of stalk
> functors; this form is the one consumers need when they have to transport along the identity of
> fibre functors with `eqToIso`.

```lean
theorem exists_sitePoint_fiber_eq {C : Type u} [Category.{v} C] {J : GrothendieckTopology C}
    (p : PointOfTopos.{max u v, v, u} J) :
    ∃ Φ : GrothendieckTopology.Point.{max u v} J,
      Φ.fiber = Sheaf.sheafifiedYoneda J ⋙ p.inverseImage
```

**`PointOfTopos.isIso_sheafFiberComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 615](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L615). The attribute's comment: “(2): the canonical inverse-image comparison is an isomorphism”.

> **Stacks 00YA (2).** The canonical comparison identifies the reconstructed stalk
> functor with `p.inverseImage`.

```lean
theorem isIso_sheafFiberComparison :
    IsIso (Φ.sheafFiberComparison p.inverseImage e.hom)
```

**`PointOfTopos.isIso_conjugate_sheafFiberComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 648](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L648). The attribute's comment: “(2): recovery of the pushforward by the adjoint mate”.

> **Stacks 00YA (2).** The adjoint mate of the canonical comparison is an isomorphism
> `p.pushforward ⟶ Φ.skyscraperSheafFunctor`, recovering the pushforward compatibly with
> the given adjunctions.

```lean
theorem isIso_conjugate_sheafFiberComparison :
    IsIso (conjugateEquiv p.adj Φ.skyscraperSheafAdjunction
      (Φ.sheafFiberComparison p.inverseImage e.hom))
```

## Tag 04EL, a lemma

[Tag 04EL](https://stacks.math.columbia.edu/tag/04EL) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.Point.exists_equivalence_isMorphismOfSites_pushforward_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Points.lean, line 586](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Points.lean#L586).

> **Stacks 04EL.** Let `Φ` be a point of a locally `w`-small site `(C, J)`, with fibre functor
> `u = Φ.fiber`. Let `ι : S ⥤ Type w` be a full subcategory of the category of sets in which some
> object `pt` is a singleton, let `K` be the topology on `S` whose covering sieves are the jointly
> surjective ones, and suppose the fibre functor factors as `u ⋙ ι` for some `u : C ⥤ S`. Then
>
> 1. there is an equivalence `i : Sh(pt) → Sh(S, K)` whose inverse image is `F ↦ F(pt)`, hence
>    whose forward functor sends a set `E` to the sheaf `V ↦ Mor(ι V, E)`;
> 2. `u : C ⥤ S` defines a morphism of sites `f : (S, K) → (C, J)`; and
> 3. the composition `Sh(pt) → Sh(S, K) → Sh(C, J)` is the morphism of topoi `(p_*, p⁻¹)` of the
>    point, in the sense that `i_* ⋙ f_*` is isomorphic to the skyscraper sheaf functor `p_*`.

```lean
public theorem exists_equivalence_isMorphismOfSites_pushforward_iso {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} [LocallySmall.{w} C] (Φ : Point.{w} J) {S : Type w}
    [SmallCategory S] (ι : S ⥤ Type w) [ι.Full] [ι.Faithful] (pt : S) (hpt : Unique (ι.obj pt))
    (K : GrothendieckTopology S)
    (hK :
      ∀ (V : S) (R : Sieve V),
        R ∈ K V ↔ ∀ x : ι.obj V, ∃ (W : S) (f : W ⟶ V) (y : ι.obj W), R.arrows f ∧ ι.map f y = x)
    (u : C ⥤ S) (hu : u ⋙ ι ≅ Φ.fiber) :
    ∃ (e : Type w ≌ Sheaf K (Type w)) (_ : _root_.IsMorphismOfSites.{w} u J K),
      e.inverse = sheafToPresheaf K (Type w) ⋙ (evaluation Sᵒᵖ (Type w)).obj (Opposite.op pt) ∧
        Nonempty
          (e.functor ⋙ u.sheafPushforwardContinuous (Type w) J K ≅
            Φ.skyscraperSheafFunctor (A := Type w))
```

## Tag 05UX, a lemma

[Tag 05UX](https://stacks.math.columbia.edu/tag/05UX) in the Stacks Project.

**`ToposPoint.epsilon_comp_eta`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Skyscraper.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Skyscraper.lean#L94).

> **Stacks 05UX.** For any set `E` there are canonical maps
> `E ⟶ (p_* E)_p ⟶ E` whose composition is the identity of `E`.
>
> Proof: apply naturality of the counit `ε` of `p⁻¹ ⊣ p_*` to the constant map
> `i_e : PUnit → E`, then evaluate at `default : p⁻¹(p_*(PUnit))`.

```lean
theorem epsilon_comp_eta (E : Type v) : p.epsilon E ∘ p.eta E = id
```

## Tag 05UY, a lemma

[Tag 05UY](https://stacks.math.columbia.edu/tag/05UY) in the Stacks Project.

**`PointOfTopos.preservesLimitsOfSize_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L225). The attribute's comment: “commutes with arbitrary limits”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos commutes with arbitrary
> limits, because it is a right adjoint.

```lean
theorem preservesLimitsOfSize_pushforward : PreservesLimitsOfSize.{w₁, w₂} p.pushforward
```

**`PointOfTopos.preservesFiniteLimits_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L230). The attribute's comment: “is left exact”. References: SGA 4 IV (3.1.2), “point; finite limits”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos is left exact.

```lean
theorem preservesFiniteLimits_pushforward : PreservesFiniteLimits p.pushforward
```

**`PointOfTopos.faithful_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L237). The attribute's comment: “is faithful”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos is faithful: the counit
> `ε_E : p^{-1}p_*E → E` is a (split) epimorphism, and `ε` is natural.

```lean
theorem faithful_pushforward : p.pushforward.Faithful
```

**`PointOfTopos.preservesEpimorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L250). The attribute's comment: “transforms surjections into surjections. The other claim of the same sentence of the source — that `p_*` commutes with coequalizers — is FALSE and is not claimed anywhere in this file; see `Point.subsingleton_fiber_of_preservesCoequalizers`”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos transforms surjections into
> surjections: every epimorphism of sets is a *split* epimorphism, and a split epimorphism is
> carried to a split epimorphism by any functor.

```lean
theorem preservesEpimorphisms_pushforward : p.pushforward.PreservesEpimorphisms
```

**`PointOfTopos.reflectsMonomorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L257). The attribute's comment: “reflects injections”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects injections.

```lean
theorem reflectsMonomorphisms_pushforward : p.pushforward.ReflectsMonomorphisms
```

**`PointOfTopos.reflectsEpimorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 263](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L263). The attribute's comment: “reflects surjections”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects surjections.

```lean
theorem reflectsEpimorphisms_pushforward : p.pushforward.ReflectsEpimorphisms
```

**`PointOfTopos.reflectsIsomorphisms_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/Topos.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/Topos.lean#L275). The attribute's comment: “reflects isomorphisms”.

> **Stacks 05UY.** The pushforward `p_*` of a point of a topos reflects isomorphisms: it
> reflects both injections and surjections, and a map of sets which is both injective and
> surjective is bijective.

```lean
theorem reflectsIsomorphisms_pushforward : p.pushforward.ReflectsIsomorphisms
```

**`PointOfTopos.preservesColimit_pushforward_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ToposCoequalizer.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ToposCoequalizer.lean#L95). The attribute's comment: “the coequalizer clause, corrected: `p_*` commutes with the coequalizer of a pair `R ⇉ E` which is an equivalence relation on `E`; for an arbitrary pair the clause is false, see `GrothendieckTopology.Point.not_preservesCoequalizers_pushforward_pointOfTopos_pointBot`”.

> **Stacks 05UY, the coequalizer clause in its corrected form.** The pushforward `p_*` of a
> point of a topos commutes with the coequalizer of `f, g : R ⇉ E` whenever the relation
> `{(f r, g r)}` on `E` is an equivalence relation, i.e. it carries the quotient `E → E / ~` by an
> equivalence relation to a coequalizer in `Sh(C)`.
>
> The clause "commutes with coequalizers" of Stacks 05UY is false for arbitrary pairs
> (`GrothendieckTopology.Point.not_preservesCoequalizers_pushforward_pointOfTopos_pointBot`), and
> this is the statement that survives (see `errata.md`, 05UY). The quotient by an equivalence
> relation is a split coequalizer (`Types.isSplitCoequalizerOfEquivalence`), and split coequalizers
> are preserved by every functor (Mathlib's `IsSplitCoequalizer.map`).

```lean
theorem preservesColimit_pushforward_of_equivalence {R E : Type w} (f g : R ⟶ E)
    (h : _root_.Equivalence (Function.Coequalizer.Rel f g)) :
    PreservesColimit (parallelPair f g) p.pushforward
```

**`CategoryTheory.GrothendieckTopology.Point.not_preservesCoequalizers_pushforward_pointOfTopos_pointBot`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/ToposCoequalizer.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/ToposCoequalizer.lean#L118). The attribute's comment: “the coequalizer clause is false: a point of the topos of presheaves on `WalkingParallelPair` whose pushforward does not commute with coequalizers; the corrected clause is `PointOfTopos.preservesColimit_pushforward_of_equivalence`”.

> **The coequalizer clause of Stacks 05UY is false.** There is a point `p` of a topos whose
> pushforward `p_* : Set ⥤ Sh(C)` does not commute with coequalizers: take
> `C = WalkingParallelPair`, `J = ⊥` (so that `Sh(C, ⊥)` is the category of presheaves,
> `sheafBotEquivalence`) and `p` the point of the topos attached to the point `pointBot zero` of
> the site, whose fibre functor is `Hom(zero, -)`, so that `u(one) = {left, right}` has two
> elements. Since `Sh(C, ⊥) ⥤ PSh(C)` is an equivalence, a preservation of coequalizers by `p_*`
> would make the skyscraper presheaf functor preserve them, which
> `subsingleton_fiber_of_preservesCoequalizers` forbids.

```lean
theorem not_preservesCoequalizers_pushforward_pointOfTopos_pointBot :
    ¬PreservesColimitsOfShape WalkingParallelPair
      (pointBot.{0} (C := WalkingParallelPair) .zero).pointOfTopos.pushforward
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.32, Tag 00Y3](https://stacks.math.columbia.edu/tag/00Y3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
