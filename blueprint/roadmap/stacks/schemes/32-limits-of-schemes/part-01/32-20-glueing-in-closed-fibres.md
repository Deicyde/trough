---
declaration: section
origin: cited
lean: AlgebraicGeometry.GlueingNearPoint.restrictionFunctorAtPoint_isEquivalence, AlgebraicGeometry.GlueingNearPoint.moduleRestrictionFunctorAtPoint, AlgebraicGeometry.GlueingNearPoint.moduleGlueingEquivalenceNearClosedPoint, AlgebraicGeometry.GlueingNearPoint.glueingEquivalenceNearPoint, AlgebraicGeometry.GlueingNearPoint.exists_open_isSeparated_baseChange, AlgebraicGeometry.GlueingNearPoint.exists_open_isProper_baseChange, AlgebraicGeometry.GlueingNearPoint.exists_open_isFinite_baseChange, AlgebraicGeometry.GlueingNearPoint.exists_open_etale_baseChange
statement: formalized
proof: formalized
---

# 32.20 Glueing in closed fibres

Section 32.20 of the Stacks Project, [Tag 0E8P](https://stacks.math.columbia.edu/tag/0E8P). 5 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BPA, a lemma

[Tag 0BPA](https://stacks.math.columbia.edu/tag/0BPA) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.restrictionFunctorAtPoint_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Germ.lean, line 4310](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Germ.lean#L4310).

> **Stacks Project, Tag 0BPA.** Let `s` be a closed point of a scheme `S` whose open
> complement `U = S \ {s}` has quasi-compact inclusion.  Restricting a scheme of finite
> presentation over `S` to `U` and to `Spec 𝒪_{S, s}`, together with the canonical comparison of
> the two induced restrictions to `V = Spec 𝒪_{S, s} ∩ U`, is an equivalence onto the category of
> such glueing data.

```lean
public theorem restrictionFunctorAtPoint_isEquivalence (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι) :
    (restrictionFunctorAtPoint S (puncturedOpen hs) s).IsEquivalence
```

## Tag 0F21, a lemma

[Tag 0F21](https://stacks.math.columbia.edu/tag/0F21) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.moduleRestrictionFunctorAtPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/FinitePresentationModules.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/FinitePresentationModules.lean#L365). The attribute's comment: “the canonical functor”.

> **Stacks 0F21**, the canonical functor.  A module of finite presentation on `S` goes to its
> restriction to `U`, its restriction to `Spec 𝒪_{S, s}`, and the canonical identification of the
> two restrictions to the punctured local scheme.

```lean
noncomputable def moduleRestrictionFunctorAtPoint (S : Scheme.{u}) (U : S.Opens) (s : S) :
    FinitePresentationModules S ⥤ moduleGlueingDataNearPoint S U s
```

**`AlgebraicGeometry.GlueingNearPoint.moduleGlueingEquivalenceNearClosedPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/FinitePresentationModules.lean, line 661](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/FinitePresentationModules.lean#L661).

> **Stacks 0F21.** Let `s` be a closed point of a scheme `S` whose open complement
> `U = S \ {s}` has quasi-compact inclusion, and let `V = Spec 𝒪_{S, s} ∖ {s}`.  Restricting a
> module of finite presentation on `S` to `U` and to `Spec 𝒪_{S, s}`, together with the canonical
> identification `α` of the two induced restrictions to `V`, is an equivalence onto the category
> of triples `(𝒢, ℋ, α)`.

```lean
noncomputable def moduleGlueingEquivalenceNearClosedPoint (S : Scheme.{u}) (s : S)
    (hs : IsClosed ({s} : Set S)) (hqc : QuasiCompact (puncturedOpen hs).ι) :
    FinitePresentationModules S ≌ moduleGlueingDataNearPoint S (puncturedOpen hs) s
```

## Tag 0BQ5, a lemma

[Tag 0BQ5](https://stacks.math.columbia.edu/tag/0BQ5) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.glueingEquivalenceNearPoint`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Germ.lean, line 4045](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Germ.lean#L4045).

> **Stacks Project, Tag 0BQ5.** Finite-presentation schemes on open neighbourhoods of a
> retrocompact open together with a point are equivalent, as a germ, to compatible
> finite-presentation schemes on the open and on the local scheme at the point. The natural
> identifications with base change intertwine the gluing comparison with the canonical
> iterated-pullback comparison on the overlap.

```lean
public noncomputable def glueingEquivalenceNearPoint
    (S : Scheme.{u}) (U : S.Opens) (s : S) (hs : s ∉ U)
    (hU : IsRetrocompact (U : Set S)) :
    { e : FinitePresentationGerm S U s ≌ glueingDataNearPoint S U s //
      ∃ a : (((FinitePresentationNeighborhoodModel.restrictionMorphisms
        (S := S) (U := U) (s := s)).Q ⋙ e.functor ⋙ openComponent S U s) ≅
        (neighborhoodModelToAmbient S U s ⋙ Over.pullback U.ι)),
      ∃ b : (((FinitePresentationNeighborhoodModel.restrictionMorphisms
        (S := S) (U := U) (s := s)).Q ⋙ e.functor ⋙ localComponent S U s) ≅
        (neighborhoodModelToAmbient S U s ⋙ Over.pullback (S.fromSpecStalk s))),
      overlapComparisonCompatible S U s e a b }
```

## Tag 0EY3, a lemma

[Tag 0EY3](https://stacks.math.columbia.edu/tag/0EY3) in the Stacks Project.

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isSeparated_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L348). The attribute's comment: “properties\_of\_relative\_morphism”.

> Let `U ⊆ S` be a retrocompact open, let `s` be a point of `S` outside `U` and let `a` be a
> morphism of schemes of finite presentation over an open neighbourhood `U'` of `U ∪ {s}`. If `a` is
> separated over `U` and over `Spec 𝒪_{S, s}`, then it is separated over some open neighbourhood of
> `U ∪ {s}` contained in `U'`.

```lean
theorem exists_open_isSeparated_baseChange
    (S : Scheme.{u}) (U U' : S.Opens) (s : S) (_hsU : s ∉ U) (hsU' : s ∈ U')
    (_hU : IsRetrocompact (U : Set S)) (hUU' : U ≤ U')
    (X₁ X₂ : Over U'.toScheme) (a : X₁ ⟶ X₂)
    (hX₁ : FinitePresentation X₁.hom) (hX₂ : FinitePresentation X₂.hom)
    (hsepU : IsSeparated (baseChangeMap U.ι ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a)))
    (hsepS : IsSeparated (baseChangeMap (S.fromSpecStalk s) ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ U' ∧ s ∈ V ∧
      IsSeparated (baseChangeMap V.ι ((Over.map U'.ι).obj X₁)
        ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isProper_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L371). The attribute's comment: “properties\_of\_relative\_morphism”. References: EGA IV (8.1.2), “partial”.

> Let `U ⊆ S` be a retrocompact open, let `s` be a point of `S` outside `U` and let `a` be a
> morphism of schemes of finite presentation over an open neighbourhood `U'` of `U ∪ {s}`. If `a` is
> proper over `U` and over `Spec 𝒪_{S, s}`, then it is proper over some open neighbourhood of
> `U ∪ {s}` contained in `U'`.

```lean
theorem exists_open_isProper_baseChange
    (S : Scheme.{u}) (U U' : S.Opens) (s : S) (_hsU : s ∉ U) (hsU' : s ∈ U')
    (_hU : IsRetrocompact (U : Set S)) (hUU' : U ≤ U')
    (X₁ X₂ : Over U'.toScheme) (a : X₁ ⟶ X₂)
    (hX₁ : FinitePresentation X₁.hom) (hX₂ : FinitePresentation X₂.hom)
    (hproperU : IsProper (baseChangeMap U.ι ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a)))
    (hproperS : IsProper (baseChangeMap (S.fromSpecStalk s) ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ U' ∧ s ∈ V ∧
      IsProper (baseChangeMap V.ι ((Over.map U'.ι).obj X₁)
        ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isFinite_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L394). The attribute's comment: “properties\_of\_relative\_morphism”.

> Let `U ⊆ S` be a retrocompact open, let `s` be a point of `S` outside `U` and let `a` be a
> morphism of schemes of finite presentation over an open neighbourhood `U'` of `U ∪ {s}`. If `a` is
> finite over `U` and over `Spec 𝒪_{S, s}`, then it is finite over some open neighbourhood of
> `U ∪ {s}` contained in `U'`.

```lean
theorem exists_open_isFinite_baseChange
    (S : Scheme.{u}) (U U' : S.Opens) (s : S) (_hsU : s ∉ U) (hsU' : s ∈ U')
    (_hU : IsRetrocompact (U : Set S)) (hUU' : U ≤ U')
    (X₁ X₂ : Over U'.toScheme) (a : X₁ ⟶ X₂)
    (hX₁ : FinitePresentation X₁.hom) (hX₂ : FinitePresentation X₂.hom)
    (hfiniteU : IsFinite (baseChangeMap U.ι ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a)))
    (hfiniteS : IsFinite (baseChangeMap (S.fromSpecStalk s) ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ U' ∧ s ∈ V ∧
      IsFinite (baseChangeMap V.ι ((Over.map U'.ι).obj X₁)
        ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_etale_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L419). The attribute's comment: “properties\_of\_relative\_morphism”.

> Let `U ⊆ S` be a retrocompact open, let `s` be a point of `S` outside `U` and let `a` be a
> morphism of schemes of finite presentation over an open neighbourhood `U'` of `U ∪ {s}`. If `a` is
> étale over `U` and over `Spec 𝒪_{S, s}`, then it is étale over some open neighbourhood of `U ∪ {s}`
> contained in `U'`.

```lean
theorem exists_open_etale_baseChange
    (S : Scheme.{u}) (U U' : S.Opens) (s : S) (_hsU : s ∉ U) (hsU' : s ∈ U')
    (_hU : IsRetrocompact (U : Set S)) (hUU' : U ≤ U')
    (X₁ X₂ : Over U'.toScheme) (a : X₁ ⟶ X₂)
    (hX₁ : FinitePresentation X₁.hom) (hX₂ : FinitePresentation X₂.hom)
    (hetaleU : Etale (baseChangeMap U.ι ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a)))
    (hetaleS : Etale (baseChangeMap (S.fromSpecStalk s) ((Over.map U'.ι).obj X₁)
      ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ U' ∧ s ∈ V ∧
      Etale (baseChangeMap V.ι ((Over.map U'.ι).obj X₁)
        ((Over.map U'.ι).obj X₂) ((Over.map U'.ι).map a))
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L482). The attribute's comment: “properties\_of\_glued\_morphism”.

> A scheme of finite presentation over an open neighbourhood of `U ∪ {s}` whose restrictions to
> the retrocompact open `U` and to the local scheme `Spec 𝒪_{S, s}` are separated is separated over
> some smaller open neighbourhood of `U ∪ {s}`.

```lean
theorem exists_open_isSeparated
    (S : Scheme.{u}) (U : S.Opens) (s : S) (hs : s ∉ U)
    (hU : IsRetrocompact (U : Set S))
    (X : FinitePresentationNeighborhoodModel S U s)
    (hopen : IsSeparated ((Over.pullback U.ι).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom)
    (hlocal : IsSeparated ((Over.pullback (S.fromSpecStalk s)).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ X.neighborhood.V ∧ s ∈ V ∧
      IsSeparated ((Over.pullback V.ι).obj
        ((neighborhoodModelToAmbient S U s).obj X)).hom
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L503). The attribute's comment: “properties\_of\_glued\_morphism”.

> A scheme of finite presentation over an open neighbourhood of `U ∪ {s}` whose restrictions to
> the retrocompact open `U` and to the local scheme `Spec 𝒪_{S, s}` are proper is proper over some
> smaller open neighbourhood of `U ∪ {s}`.

```lean
theorem exists_open_isProper
    (S : Scheme.{u}) (U : S.Opens) (s : S) (hs : s ∉ U)
    (hU : IsRetrocompact (U : Set S))
    (X : FinitePresentationNeighborhoodModel S U s)
    (hopen : IsProper ((Over.pullback U.ι).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom)
    (hlocal : IsProper ((Over.pullback (S.fromSpecStalk s)).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ X.neighborhood.V ∧ s ∈ V ∧
      IsProper ((Over.pullback V.ι).obj
        ((neighborhoodModelToAmbient S U s).obj X)).hom
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 524](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L524). The attribute's comment: “properties\_of\_glued\_morphism”.

> A scheme of finite presentation over an open neighbourhood of `U ∪ {s}` whose restrictions to
> the retrocompact open `U` and to the local scheme `Spec 𝒪_{S, s}` are finite is finite over some
> smaller open neighbourhood of `U ∪ {s}`.

```lean
theorem exists_open_isFinite
    (S : Scheme.{u}) (U : S.Opens) (s : S) (hs : s ∉ U)
    (hU : IsRetrocompact (U : Set S))
    (X : FinitePresentationNeighborhoodModel S U s)
    (hopen : IsFinite ((Over.pullback U.ι).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom)
    (hlocal : IsFinite ((Over.pullback (S.fromSpecStalk s)).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ X.neighborhood.V ∧ s ∈ V ∧
      IsFinite ((Over.pullback V.ι).obj
        ((neighborhoodModelToAmbient S U s).obj X)).hom
```

**`AlgebraicGeometry.GlueingNearPoint.exists_open_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean, line 547](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Properties.lean#L547). The attribute's comment: “properties\_of\_glued\_morphism”.

> A scheme of finite presentation over an open neighbourhood of `U ∪ {s}` whose restrictions to
> the retrocompact open `U` and to the local scheme `Spec 𝒪_{S, s}` are étale is étale over some
> smaller open neighbourhood of `U ∪ {s}`.

```lean
theorem exists_open_etale
    (S : Scheme.{u}) (U : S.Opens) (s : S) (hs : s ∉ U)
    (hU : IsRetrocompact (U : Set S))
    (X : FinitePresentationNeighborhoodModel S U s)
    (hopen : Etale ((Over.pullback U.ι).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom)
    (hlocal : Etale ((Over.pullback (S.fromSpecStalk s)).obj
      ((neighborhoodModelToAmbient S U s).obj X)).hom) :
    ∃ V : S.Opens, U ≤ V ∧ V ≤ X.neighborhood.V ∧ s ∈ V ∧
      Etale ((Over.pullback V.ι).obj
        ((neighborhoodModelToAmbient S U s).obj X)).hom
```

## Tag 0E8Q, a lemma

[Tag 0E8Q](https://stacks.math.columbia.edu/tag/0E8Q) in the Stacks Project.

**`AlgebraicGeometry.canonicalRestrictionFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Basic.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Basic.lean#L131). The attribute's comment: “canonical functor”.

> **Stacks Project, Tag 0E8Q**, the canonical functor.  The functor taking a scheme of finite
> presentation over `S` to the gluing datum given by its restriction to the complement of the
> closed points, its restrictions to the local schemes at them, and the base-change associativity
> isomorphism between the two restrictions to each punctured local scheme.
>
> The comparison is `AlgebraicGeometry.canonicalRestrictionComparison`, which is pinned by its
> compatibility equation, so this is the canonical functor and not merely a functor into the
> category of gluing data.

```lean
noncomputable def canonicalRestrictionFunctor :
    FinitePresentationOver S ⥤ glueingData s hs
```

**`AlgebraicGeometry.canonicalRestrictionFunctor_isEquivalence_of_isEmpty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Equivalence.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/Equivalence.lean#L115). The attribute's comment: “equivalence, special case of an empty family of points”.

> For an empty family of points, the canonical restriction functor from schemes of finite
> presentation over `S` to gluing data is an equivalence of categories.

```lean
theorem canonicalRestrictionFunctor_isEquivalence_of_isEmpty [IsEmpty I] :
    (canonicalRestrictionFunctor s hs).IsEquivalence
```

**`AlgebraicGeometry.canonicalRestrictionFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/EquivalenceGeneral.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/EquivalenceGeneral.lean#L153). The attribute's comment: “equivalence, general finite family of points”.

> **Stacks Project, Tag 0E8Q.** Let `s : I → S` be a finite family of pairwise distinct closed
> points of a scheme `S` whose open complement has quasi-compact inclusion.  Then the canonical
> restriction functor from schemes of finite presentation over `S` to glueing data near the family
> — a scheme of finite presentation over the open complement, a family of schemes of finite
> presentation over the local schemes at the points, and an isomorphism of the two restrictions to
> each punctured local scheme — is an equivalence of categories.

```lean
theorem canonicalRestrictionFunctor_isEquivalence {S : Scheme.{u}} {I : Type u} [Finite I]
    (s : I → S) (hs : ∀ i, s i ∈ closedPoints S) (hinj : Function.Injective s)
    (hqc : QuasiCompact (complementOfClosedPoints s hs).ι) :
    (canonicalRestrictionFunctor s hs).IsEquivalence
```

**`AlgebraicGeometry.canonicalRestrictionFunctor_isEquivalence_of_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/EquivalenceSinglePoint.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/GlueingNearClosedPoints/EquivalenceSinglePoint.lean#L164). The attribute's comment: “equivalence, special case of a one-element family of points”.

> **Stacks Project, Tag 0E8Q**, for a family of closed points indexed by a type with a unique
> element: the canonical restriction functor from schemes of finite presentation over `S` to gluing
> data near the family is an equivalence of categories.
>
> The family is a single closed point whose open complement has quasi-compact inclusion, so this is
> [Stacks, Tag 0BPA] after evaluating the one-index gluing data at its unique index.

```lean
theorem canonicalRestrictionFunctor_isEquivalence_of_unique [Unique I]
    (hqc : QuasiCompact (complementOfClosedPoints s hs).ι) :
    (canonicalRestrictionFunctor s hs).IsEquivalence
```

**`AlgebraicGeometry.canonicalRestrictionComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/RestrictionComparison/Basic.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/RestrictionComparison/Basic.lean#L219). The attribute's comment: “canonical comparison”.

> **Stacks Project, Tag 0E8Q**, the canonical comparison. The base-change associativity
> isomorphism identifying the two ways of restricting a scheme of finite presentation over `S`
> to every punctured local scheme, together with the equation saying that it commutes with the
> projections down to the scheme being restricted.

```lean
noncomputable def canonicalRestrictionComparison {S : Scheme.{u}} {I : Type u} [Finite I]
    (s : I → S) (hs : ∀ i, s i ∈ closedPoints S) :
    { e : restrictToComplementOfClosedPoints s hs ⋙ restrictOpenToPuncturedLocals s hs ≅
        restrictToLocalSchemes s ⋙ restrictLocalsToPuncturedLocals s hs //
      ∀ (X : FinitePresentationOver S) (i : I),
        ((e.hom.app X) i).hom.left ≫
          pullback.fst
            (pullback.snd X.obj.hom (S.fromSpecStalk (s i)))
            (((S.fromSpecStalk (s i)) ⁻¹ᵁ (complementOfClosedPoints s hs)).ι) ≫
          pullback.fst X.obj.hom (S.fromSpecStalk (s i)) =
        pullback.fst
            (pullback.snd X.obj.hom (complementOfClosedPoints s hs).ι)
            ((S.fromSpecStalk (s i)) ∣_ (complementOfClosedPoints s hs)) ≫
          pullback.fst X.obj.hom (complementOfClosedPoints s hs).ι }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.20, Tag 0E8P](https://stacks.math.columbia.edu/tag/0E8P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
