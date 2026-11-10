---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_span_baseChange_iso, AlgebraicGeometry.Space.exists_isIso_smallBaseChange_map_of_isClosedImmersion, Stacks.Etale.exists_etale_openCover_isomorphic_pullback_of_isClosedImmersion, AlgebraicGeometry.stalkPushforwardIso, AlgebraicGeometry.stalkPushforwardIso_germ, AlgebraicGeometry.smallEtalePushforward_stalk_unique_of_not_mem_range, AlgebraicGeometry.smallEtalePushforwardStalkIsoAb, AlgebraicGeometry.smallEtaleAdjunction_counit_isIso_abelian
statement: formalized
proof: formalized
---

# 59.46 Closed immersions and pushforward

Section 59.46 of the Stacks Project, [Tag 04E1](https://stacks.math.columbia.edu/tag/04E1). 4 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04FV, a lemma

[Tag 04FV](https://stacks.math.columbia.edu/tag/04FV) in the Stacks Project.

**`AlgebraicGeometry.exists_span_baseChange_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/LiftingMorphisms.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/LiftingMorphisms.lean#L83).

> **Stacks Project, Tag 04FV.** A morphism over a closed subscheme between the
> base changes of two étale schemes is induced by a span over the original scheme,
> and the left leg of that span becomes an isomorphism after base change.

```lean
theorem exists_span_baseChange_iso
    {X Z U U' : Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    (f : U ⟶ X) (g : U' ⟶ X) [Etale f] [Etale g]
    (h : pullback f i ⟶ pullback g i)
    (h_over : h ≫ pullback.snd g i = pullback.snd f i) :
    ∃ (W : Scheme.{u}) (a : W ⟶ U) (b : W ⟶ U')
      (hab : a ≫ f = b ≫ g) (_hW : Etale (a ≫ f)),
      let aZ : pullback (a ≫ f) i ⟶ pullback f i :=
        pullback.lift (pullback.fst (a ≫ f) i ≫ a) (pullback.snd (a ≫ f) i) (by
          rw [Category.assoc]
          exact pullback.condition)
      let bZ : pullback (a ≫ f) i ⟶ pullback g i :=
        pullback.lift (pullback.fst (a ≫ f) i ≫ b) (pullback.snd (a ≫ f) i) (by
          rw [Category.assoc, ← hab]
          exact pullback.condition)
      ∃ e : pullback (a ≫ f) i ≅ pullback f i,
        e.hom = aZ ∧ h = e.inv ≫ bZ
```

**`AlgebraicGeometry.Space.exists_isIso_smallBaseChange_map_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartLocalFullness.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ClosedImmersionChartLocalFullness.lean#L345). The attribute's comment: “for algebraic spaces”.

> **Stacks 04FV** for algebraic spaces. Let `i : Z ⟶ X` be a closed immersion of algebraic
> spaces over a scheme `S`, let `U` and `U'` be étale scheme charts of `X`, and let `φ` be a
> morphism over `Z` between their base changes along `i`. Then there is an étale scheme chart `W`
> of `X` and a morphism of charts `a : W ⟶ U` whose base change along `i` is an isomorphism and
> which lies in the image sieve of `φ`: the base change of `a` followed by `φ` is the base change
> of a morphism of charts `W ⟶ U'`.
>
> The chart `W` is an open subscheme of `U ×_X U'` containing the image of the graph of `φ`.

```lean
theorem exists_isIso_smallBaseChange_map_of_isClosedImmersion
    {Z X : AlgebraicSpaces B S hS} (i : Z ⟶ X) (hi : IsClosedImmersion B S hS i.hom)
    (U U' : SmallEtale B S hS X.1)
    (φ : (smallBaseChange B S hS i hi.rep).obj U ⟶ (smallBaseChange B S hS i hi.rep).obj U') :
    ∃ (W : SmallEtale B S hS X.1) (a : W ⟶ U),
      IsIso ((smallBaseChange B S hS i hi.rep).map a) ∧
        ((smallBaseChange B S hS i hi.rep).imageSieve φ).arrows a
```

## Tag 04FW, a lemma

[Tag 04FW](https://stacks.math.columbia.edu/tag/04FW) in the Stacks Project.

**`Stacks.Etale.exists_etale_openCover_isomorphic_pullback_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/LiftAcrossClosedImmersion.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/LiftAcrossClosedImmersion.lean#L219).

> **Stacks Project, Tag 04FW.** If `i : Z ⟶ X` is a closed immersion and `p : V ⟶ Z` is
> étale, then `V` has a Zariski open cover whose members are, over `Z`, base changes along `i`
> of étale schemes over `X`.

```lean
theorem exists_etale_openCover_isomorphic_pullback_of_isClosedImmersion
    {X Z V : AlgebraicGeometry.Scheme.{u}} (i : Z ⟶ X) [IsClosedImmersion i]
    (p : V ⟶ Z) [Etale p] :
    ∃ (W : Scheme.OpenCover.{max u v, u} V)
      (U : W.I₀ → AlgebraicGeometry.Scheme.{u}) (f : ∀ j, U j ⟶ X),
      (∀ j, Etale (f j)) ∧
        ∀ j, ∃ e : W.X j ≅ pullback (f j) i,
          e.hom ≫ pullback.snd (f j) i = W.f j ≫ p
```

## Tag 04FX, a lemma

[Tag 04FX](https://stacks.math.columbia.edu/tag/04FX) in the Stacks Project.

**`AlgebraicGeometry.stalkPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkInside.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkInside.lean#L504). The attribute's comment: “stalk_pushforward_inside”.

> At a geometric point of the closed subscheme, direct image on the small
> étale site does not change the stalk. This is natural in the sheaf.

```lean
public noncomputable def stalkPushforwardIso (B : BigEtaleSite.{u})
    {S T : B.Scheme} (i : T ⟶ S) [IsClosedImmersion (B.inclusion.map i)]
    (s : GeometricPoint T.1) :
    (smallEtaleBaseChange B i).sheafPushforwardContinuous (Type (u + 1))
        (SmallEtale.topology B S.1 S.property) (SmallEtale.topology B T.1 T.property) ⋙
      sheafToPresheaf (SmallEtale.topology B S.1 S.property) (Type (u + 1)) ⋙
      etaleStalkPresheafFunctor B S.1 S.property
        (s.map (B.inclusion.map i)) (Type (u + 1)) ≅
      sheafToPresheaf (SmallEtale.topology B T.1 T.property) (Type (u + 1)) ⋙
      etaleStalkPresheafFunctor B T.1 T.property s (Type (u + 1))
```

**`AlgebraicGeometry.stalkPushforwardIso_germ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkInside.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkInside.lean#L563). The attribute's comment: “stalk_pushforward_inside”.

> The canonical comparison takes the germ of a section over an étale
> neighborhood of the image point to the germ of the same section over its
> base change. The compatibility of the two chosen lifts is expressed by the
> first pullback projection.

```lean
public theorem stalkPushforwardIso_germ (B : BigEtaleSite.{u})
    {S T : B.Scheme} (i : T ⟶ S) [IsClosedImmersion (B.inclusion.map i)]
    (s : GeometricPoint T.1)
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (Type (u + 1)))
    (N : (geometricPointFiber B S.1 S.property
      (s.map (B.inclusion.map i))).Elements)
    (q : (geometricPointFiber B T.1 T.property s).obj
      ((smallEtaleBaseChange B i).obj N.1))
    (hq : q.1 ≫ B.inclusion.map (pullback.fst N.1.obj.hom i) = N.2.1)
    (σ : (((smallEtaleBaseChange B i).sheafPushforwardContinuous
        (Type (u + 1)) (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).obj F).obj.obj (Opposite.op N.1)) :
    ((stalkPushforwardIso B i s).hom.app F).hom
      ((colimit.ι
        ((Functor.Elements.π (geometricPointFiber B S.1 S.property
          (s.map (B.inclusion.map i)))).op ⋙
          (((smallEtaleBaseChange B i).sheafPushforwardContinuous
            (Type (u + 1)) (SmallEtale.topology B S.1 S.property)
            (SmallEtale.topology B T.1 T.property)).obj F).obj)
        (Opposite.op N)).hom σ) =
      (colimit.ι
        ((Functor.Elements.π (geometricPointFiber B T.1 T.property s)).op ⋙
          F.obj)
        (Opposite.op (Functor.elementsMk _ ((smallEtaleBaseChange B i).obj N.1) q))).hom σ
```

**`AlgebraicGeometry.smallEtalePushforward_stalk_unique_of_not_mem_range`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkOutside.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/StalkOutside.lean#L142). The attribute's comment: “stalk_pushforward_outside”.

> The stalk of the direct image from a closed subscheme is a singleton
> outside that subscheme.

```lean
public theorem smallEtalePushforward_stalk_unique_of_not_mem_range
    (B : BigEtaleSite.{u}) {Z X : B.Scheme}
    (i : Z ⟶ X) [IsClosedImmersion (B.inclusion.map i)]
    (G : Sheaf (SmallEtale.topology B Z.1 Z.property)
      (Type (max (u + 1) v)))
    (s : GeometricPoint X.1)
    (hs : s.hom default ∉ Set.range (B.inclusion.map i).base) :
    ∃! _ : (etaleStalk B X.1 X.property s
      (((smallEtaleBaseChange B i).sheafPushforwardContinuous
        (Type (max (u + 1) v))
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property)).obj G).obj), True
```

**`AlgebraicGeometry.smallEtalePushforwardStalkIsoAb`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/SupportedDerivedEquivalence.lean#L202). The attribute's comment: “stalk of a direct image inside the closed subscheme, abelian sheaves”.

> **Stacks 04FX for abelian sheaves.** At a geometric point of the closed subscheme, direct
> image of abelian sheaves along a closed immersion does not change the stalk, naturally in the
> sheaf: base change of pointed étale neighbourhoods is initial, so the two colimits agree.

```lean
public def smallEtalePushforwardStalkIsoAb (s : GeometricPoint Z.1) :
    (smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property) ⋙
      sheafToPresheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1} ⋙
      etaleStalkPresheafFunctor B X.1 X.property
        (s.map (B.inclusion.map i)) AddCommGrpCat.{u + 1} ≅
      sheafToPresheaf (SmallEtale.topology B Z.1 Z.property) AddCommGrpCat.{u + 1} ⋙
      etaleStalkPresheafFunctor B Z.1 Z.property s AddCommGrpCat.{u + 1}
```

## Tag 04CA, a proposition

[Tag 04CA](https://stacks.math.columbia.edu/tag/04CA) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleAdjunction_counit_isIso_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean#L255). The attribute's comment: “left inverse, abelian sheaves”.

> **Stacks 04CA.** The counit of the inverse image/direct image adjunction along a closed
> immersion is an isomorphism on every abelian sheaf.

```lean
public theorem smallEtaleAdjunction_counit_isIso_abelian
    (F : Sheaf (SmallEtale.topology B Z.1 Z.property) AddCommGrpCat.{u + 1}) :
    IsIso (((smallEtaleBaseChange B i).sheafAdjunctionContinuous AddCommGrpCat.{u + 1}
      (SmallEtale.topology B X.1 X.property)
      (SmallEtale.topology B Z.1 Z.property)).counit.app F)
```

**`AlgebraicGeometry.smallEtalePushforwardCompPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean#L265). The attribute's comment: “left inverse, abelian sheaves”.

> **Stacks 04CA.** Inverse image along a closed immersion is a left inverse to direct image
> on abelian sheaves: the counit of the adjunction is a natural isomorphism.

```lean
public def smallEtalePushforwardCompPullbackIso :
    (smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property) ⋙
      (smallEtaleBaseChange B i).sheafPullback AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property) ≅
      𝟭 (Sheaf (SmallEtale.topology B Z.1 Z.property) AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.smallEtalePushforward_essImage_iff_abelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean, line 422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean#L422). The attribute's comment: “part (2): essential image”.

> **Stacks 04CA, part (2).** An abelian sheaf on the small étale site of `X` lies in the
> essential image of direct image along a closed immersion `i : Z ⟶ X` exactly when its support
> is contained in `Z`, that is, exactly when its stalk vanishes at every geometric point of `X`
> whose image misses `Z`.

```lean
public theorem smallEtalePushforward_essImage_iff_abelian
    (F : Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1}) :
    ((smallEtaleBaseChange B i).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallEtale.topology B X.1 X.property)
        (SmallEtale.topology B Z.1 Z.property)).essImage F ↔
      SmallEtale.supportSheaf B X.1 X.property F ⊆
        Set.range (B.inclusion.map i).base
```

**`Stacks.EtaleCohomology.smallEtalePushforwardFullyFaithful`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean#L148). The attribute's comment: “part (1): fully faithful”.

> Direct image of sheaves of sets along a closed immersion is fully faithful.

```lean
public def smallEtalePushforwardFullyFaithful {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] :
    ((smallEtaleBaseChange i).sheafPushforwardContinuous (Type (max (u + 1) v))
      (Scheme.smallEtaleTopology X) (Scheme.smallEtaleTopology Z)).FullyFaithful
```

**`Stacks.EtaleCohomology.smallEtalePushforwardCompInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean#L156). The attribute's comment: “left inverse, sheaves of sets”.

> The counit `i^{-1} i_* ⟶ 𝟭` of the adjunction is an isomorphism.

```lean
public def smallEtalePushforwardCompInverseImageIso {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] :
    (smallEtaleBaseChange i).sheafPushforwardContinuous (Type (max (u + 1) v))
        (Scheme.smallEtaleTopology X) (Scheme.smallEtaleTopology Z) ⋙
      smallEtaleInverseImage.{u, v} i ≅
      𝟭 (Sheaf (Scheme.smallEtaleTopology Z) (Type (max (u + 1) v)))
```

**`Stacks.EtaleCohomology.smallEtalePushforward_essImage_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/SetSheafEssentialImage.lean#L318). The attribute's comment: “part (1): essential image”.

> A sheaf of sets on `X_étale` lies in the essential image of direct image along a closed
> immersion `i : Z ⟶ X` exactly when its restriction to the open complement of `Z` is the
> singleton sheaf.

```lean
public theorem smallEtalePushforward_essImage_iff {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsClosedImmersion i] (F : Sheaf (Scheme.smallEtaleTopology X) (Type (max (u + 1) v))) :
    ((smallEtaleBaseChange i).sheafPushforwardContinuous (Type (max (u + 1) v))
        (Scheme.smallEtaleTopology X) (Scheme.smallEtaleTopology Z)).essImage F ↔
      Nonempty (IsTerminal ((smallEtaleInverseImage.{u, v} (openComplement i).ι).obj F))
```

**`Stacks.EtaleCohomology.smallEtalePushforwardAb_essImage_iff_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/IntegralUniversallyInjectivePushforwardEssImage.lean#L59). The attribute's comment: “part (2): essential image”.

> An abelian sheaf on `W_étale` is a direct image along a closed immersion `j : Z ⟶ W` exactly
> when its restriction to an open subscheme `U` complementary to the image of `j` vanishes, that
> is, exactly when its support is contained in `j(Z)`.

```lean
public theorem smallEtalePushforwardAb_essImage_iff_of_isClosedImmersion {Z W : Scheme.{u}}
    (j : Z ⟶ W) [IsClosedImmersion j] (U : W.Opens) (hU : (U : Set W) = (Set.range j.base)ᶜ)
    (G : Sheaf (smallEtaleTopology W) Ab.{u + 1}) :
    (smallEtalePushforwardAb j).essImage G ↔
      IsZero (((smallEtaleBaseChange U.ι).sheafPullback Ab.{u + 1}
        (smallEtaleTopology W) (smallEtaleTopology U.toScheme)).obj G)
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.IsCoverDense.full_sheafPushforwardContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsCoverDense.full_sheafPushforwardContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean#L245) (StacksFrontier): “part (2): fully faithful”. References: SGA 4 III (4.1), “i) ⇒ ii)”.
- [`CategoryTheory.Functor.IsCoverDense.faithful_sheafPushforwardContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.IsCoverDense.faithful_sheafPushforwardContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ClosedImmersionsPushforward/AbelianSheafEssentialImage.lean#L249) (StacksFrontier): “part (2): fully faithful”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.46, Tag 04E1](https://stacks.math.columbia.edu/tag/04E1)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
