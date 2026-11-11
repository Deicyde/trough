---
declaration: section
origin: cited
lean: TopologicalRing.flat_isLocalNoetherian, TopologicalRing.flat_isLocalNoetherian', TopologicalRing.flat_isStableUnderBaseChangeByFiniteTypeOnReductions, TopologicalRing.flatAdicFiniteType_isStableUnderBaseChange, TopologicalRing.flat_isStableUnderBaseChangeByFiniteTypeOnReductions', TopologicalRing.flatAdicFiniteType_isStableUnderBaseChange', TopologicalRing.flat_isStableUnderCompositionNoetherian, TopologicalRing.flat_isStableUnderCompositionNoetherian'
statement: formalized
proof: formalized
---

# 88.13 Flat morphisms

Section 88.13 of the Stacks Project, [Tag 0GC8](https://stacks.math.columbia.edu/tag/0GC8). 8 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GC9, a lemma

[Tag 0GC9](https://stacks.math.columbia.edu/tag/0GC9) in the Stacks Project.

**`TopologicalRing.flat_isLocalNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalProperty.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalProperty.lean#L311). References: SGA 3 VIIB (1.3.4), “Flatness clause”.

> **Flatness is a local property of morphisms of Noetherian adic topological rings**
> (Stacks 0GC9): it ascends along completed étale localization diagrams, descends along faithfully
> flat ones, and is preserved by finite products of targets.

```lean
public theorem flat_isLocalNoetherian :
    PropertyIsLocalNoetherian
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
```

**`TopologicalRing.flat_isLocalNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalPropertyRefined.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalPropertyRefined.lean#L71). References: SGA 3 VIIB (1.3.4), “Flatness clause”.

> **Flatness is a local property of morphisms of Noetherian adic topological rings**: it is
> independent of the presentations of the source and the target, ascends along completed étale
> localization diagrams, descends along faithfully flat ones, and is preserved by finite products
> of targets.

```lean
public theorem flat_isLocalNoetherian' :
    PropertyIsLocalNoetherian'
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
```

## Tag 0GCA, a lemma

[Tag 0GCA](https://stacks.math.columbia.edu/tag/0GCA) in the Stacks Project.

**`TopologicalRing.flat_isStableUnderBaseChangeByFiniteTypeOnReductions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatBaseChange.lean, line 797](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/FlatBaseChange.lean#L797). The attribute's comment: “part (1)”.

> **Stacks 0GCA, part (1).** Flatness of morphisms of Noetherian adic topological rings
> (Stacks 0GC9) is stable under completed tensor-product base change along morphisms of finite
> type on reductions (Stacks 0GC2), in the sense of Remark 0GBG.

```lean
public theorem flat_isStableUnderBaseChangeByFiniteTypeOnReductions :
    IsStableUnderBaseChangeBy
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
      FiniteTypeOnReductionsProperty
```

**`TopologicalRing.flatAdicFiniteType_isStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatBaseChange.lean, line 905](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/FlatBaseChange.lean#L905). The attribute's comment: “part (2)”.

> **Stacks 0GCA, part (2).** Flatness (Stacks 0GC9) together with the property of Stacks
> 0GBW, being adic and topologically of finite type, is stable under base change in the sense of
> Remark 0GBF: for continuous homomorphisms `B → A` and `B → C` of Noetherian adic topological
> rings with `B → A` flat, adic and topologically of finite type, the completed tensor product
> `A ⊗̂_B C` is Noetherian adic and `C → A ⊗̂_B C` is again flat, adic and topologically of finite
> type. No condition is imposed on `B → C`.

```lean
public theorem flatAdicFiniteType_isStableUnderBaseChange :
    IsStableUnderBaseChangeNoetherian
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        φ.Flat ∧ RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

**`TopologicalRing.flat_isStableUnderBaseChangeByFiniteTypeOnReductions'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatBaseChangeRefined.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/FlatBaseChangeRefined.lean#L113). The attribute's comment: “part (1)”.

> **Stacks 0GCA, part (1).** Flatness of morphisms of Noetherian adic topological rings
> (Stacks 0GC9) is stable under completed tensor-product base change along morphisms of finite
> type on reductions (Stacks 0GC2), in the sense of Remark 0GBG.

```lean
public theorem flat_isStableUnderBaseChangeByFiniteTypeOnReductions' :
    IsStableUnderBaseChangeBy'
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
      FiniteTypeOnReductionsProperty
```

**`TopologicalRing.flatAdicFiniteType_isStableUnderBaseChange'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Rig/FlatBaseChangeRefined.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Rig/FlatBaseChangeRefined.lean#L170). The attribute's comment: “part (2)”.

> **Stacks 0GCA, part (2).** Flatness (Stacks 0GC9) together with the property of Stacks
> 0GBW, being adic and topologically of finite type, is stable under base change in the sense of
> Remark 0GBF: for continuous homomorphisms `B → A` and `B → C` of Noetherian adic topological
> rings with `B → A` flat, adic and topologically of finite type, the completed tensor product
> `A ⊗̂_B C` is Noetherian adic and `C → A ⊗̂_B C` is again flat, adic and topologically of finite
> type. No condition is imposed on `B → C`.

```lean
public theorem flatAdicFiniteType_isStableUnderBaseChange' :
    IsStableUnderBaseChangeNoetherian'
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦
        φ.Flat ∧ RingHom.IsAdic φ ∧ IsTopologicallyOfFiniteType φ)
```

## Tag 0GCB, a lemma

[Tag 0GCB](https://stacks.math.columbia.edu/tag/0GCB) in the Stacks Project.

**`TopologicalRing.flat_isStableUnderCompositionNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalProperty.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalProperty.lean#L323).

> **Stacks 0GCB.** Flatness, as a local property of morphisms of Noetherian adic topological
> rings (Stacks 0GC9), is stable under composition: the composite of two flat ring homomorphisms
> is flat.

```lean
public theorem flat_isStableUnderCompositionNoetherian :
    PropertyIsStableUnderCompositionNoetherian
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
```

**`TopologicalRing.flat_isStableUnderCompositionNoetherian'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalPropertyRefined.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Algebra/AdicTopology/FlatLocalPropertyRefined.lean#L84).

> Flatness, as a local property of morphisms of Noetherian adic topological rings, is stable
> under composition: the composite of two flat ring homomorphisms is flat.

```lean
public theorem flat_isStableUnderCompositionNoetherian' :
    PropertyIsStableUnderCompositionNoetherian'
      (fun {B A : Type u} [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
        [CommRing A] [TopologicalSpace A] [IsTopologicalRing A] (φ : B →+* A) ↦ φ.Flat)
```

## Tag 0GCC, a definition

[Tag 0GCC](https://stacks.math.columbia.edu/tag/0GCC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Flat.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Flat.lean#L87).

> **Stacks 0GCC.** A morphism of formal algebraic spaces over `S` is *flat* when every
> morphism between affine, representable, étale charts of its source and target is induced by a
> flat continuous homomorphism of adic Noetherian topological rings.

```lean
abbrev IsFlat (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0GCD, a lemma

[Tag 0GCD](https://stacks.math.columbia.edu/tag/0GCD) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFlat_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatCharacterization.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatCharacterization.lean#L165). The attribute's comment: “conditions (1) and (2) agree by Definition 0GCC, as the source's proof states; Stacks 0AJ3, the covering refinement of Stacks 0AJ2 and the locality axioms of Stacks 0GC9 read through Stacks 0AN8 and Stacks 0AN9 are carried as the hypotheses `hpb`, `href`, `hasc` and `hdesc`”.

> **Stacks 0GCD.** For a morphism `f : X ⟶ Y` of locally Noetherian formal algebraic spaces
> over `S`, flatness of `f` in the sense of Definition 0GCC, the condition that every affine
> representable étale square over `f` carry a flat map of Noetherian adic topological rings, the
> existence of an affine étale covering of `Y` together with affine étale coverings of the fibre
> products of its members with `X` on which that condition holds, and the existence of an affine
> étale covering of `X` whose members factor flatly through affine representable étale charts of
> `Y`, are all equivalent.
>
> The first two conditions agree by Definition 0GCC, as in the source's own proof; the last three
> are the three conditions of Stacks 0ANG for the class of Noetherian adic topological rings and
> flatness, which is a local property of such arrows by Stacks 0GC9. The hypotheses `hpb`,
> `href`, `hasc` and `hdesc` carry Stacks 0AJ3, the covering refinement of Stacks 0AJ2, and the
> locality axioms of Situation 0CBA read through Stacks 0AN8 and Stacks 0AN9.

```lean
theorem isFlat_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hpb : ∀ (V : FppfSheaf B S hS) (v : V ⟶ Y), IsAffineFormalAlgebraicSpace B S hS V →
      IsRepresentableEtale B S hS v → IsFormalAlgebraicSpace B S hS (pullback v f))
    (hasc : ChartPropertyAscendsAlongAffineEtale B S hS
      TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom)
    (hdesc : ChartPropertyDescendsAlongFiniteAffineEtaleCover B S hS
      TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom)
    (href : HasEtaleRefinementOfSourceCover B S hS f) :
    List.TFAE
      [IsFlat B S hS f,
        HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f,
        HasPropertyAfterTargetCover B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f,
        HasPropertyAfterSourceCover B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f]
```

**`AlgebraicGeometry.FormalSpace.isFlat_tfae_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatCharacterizationLocallyNoetherian.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatCharacterizationLocallyNoetherian.lean#L97).

> **Stacks 0GCD.** For a morphism `f : X ⟶ Y` of locally Noetherian formal algebraic spaces
> over `S` the following are equivalent:
>
> 1. `f` is flat in the sense of Definition 0GCC;
> 2. every commutative square with affine formal algebraic spaces `U`, `V` and representable
>    étale maps `U ⟶ X`, `V ⟶ Y` carries a flat map of Noetherian adic topological rings on
>    `U ⟶ V`;
> 3. there are an affine étale covering `{Yⱼ ⟶ Y}` and affine étale coverings `{Xⱼᵢ ⟶ Yⱼ ×_Y X}`
>    with each `Xⱼᵢ ⟶ Yⱼ` corresponding to a flat map of Noetherian adic topological rings;
> 4. there are an affine étale covering `{Xᵢ ⟶ X}` and factorizations `Xᵢ ⟶ Yᵢ ⟶ Y` through
>    affine formal algebraic spaces representable étale over `Y` with each `Xᵢ ⟶ Yᵢ`
>    corresponding to a flat map of Noetherian adic topological rings.
>
> As in the source, (1) and (2) agree by Definition 0GCC, and (2), (3), (4) are the three
> conditions of the Noetherian variant of Stacks 0ANG (Remark 0ANI) for flatness, a local property
> of arrows of `WAdm^{Noeth}` by Stacks 0GC9.

```lean
theorem isFlat_tfae_of_isLocallyNoetherian {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y) :
    List.TFAE
      [IsFlat B S hS f,
        HasPropertyOnEveryAffineEtaleDiagram B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f,
        HasPropertyAfterTargetCover B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f,
        HasPropertyAfterSourceCover B S hS
          TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom f]
```

## Tag 0GCE, a lemma

[Tag 0GCE](https://stacks.math.columbia.edu/tag/0GCE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFlat_pullback_snd_of_isLocallyOfFiniteTypeOnReductions_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeLocallyNoetherian.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeLocallyNoetherian.lean#L108). The attribute's comment: “part (1)”.

> **Stacks 0GCE, part (1).** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally
> Noetherian formal algebraic spaces over `S`. If `f` is flat (Definition 0GCC) and the morphism
> of reductions `g_red : Z_red ⟶ Y_red` is locally of finite type, then the base change
> `X ×_Y Z ⟶ Z` is flat.
>
> Flatness of arrows of `WAdm^{Noeth}` is stable under base change by arrows of finite type on
> reductions (Stacks 0GCA, part (1)); the hypothesis on `g_red` gives that property on every affine
> étale chart map of `g` by the implication (4) ⟹ (1) of Stacks 0GC7, and Stacks 0GBG transfers
> flatness to the second projection.

```lean
theorem isFlat_pullback_snd_of_isLocallyOfFiniteTypeOnReductions_of_isLocallyNoetherian
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y) (hX : IsLocallyNoetherian B S hS X)
    (hY : IsLocallyNoetherian B S hS Y) (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsFlat B S hS f) (hg : IsLocallyOfFiniteTypeOnReductions B S hS g) :
    IsFlat B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isFlat_and_isLocallyOfFiniteType_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeLocallyNoetherian.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeLocallyNoetherian.lean#L138). The attribute's comment: “part (2)”.

> **Stacks 0GCE, part (2).** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally
> Noetherian formal algebraic spaces over `S`. If `f` is flat (Definition 0GCC) and locally of
> finite type (Stacks 0AM4), then the base change `X ×_Y Z ⟶ Z` is flat and locally of finite
> type.
>
> Flatness together with being adic and topologically of finite type is stable under arbitrary
> base change of arrows of `WAdm^{Noeth}` (Stacks 0GCA, part (2)); the hypotheses on `f` give that
> property on every affine étale chart map of `f` (Stacks 0GC0 read at `WAdm^{Noeth}`), Stacks 0GBF
> transfers it to the second projection, and flatness is read off its first conjunct. The second
> conclusion is Stacks 0AQ5, which needs neither flatness nor the Noetherian hypotheses.

```lean
theorem isFlat_and_isLocallyOfFiniteType_pullback_snd {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hX : IsLocallyNoetherian B S hS X)
    (hY : IsLocallyNoetherian B S hS Y) (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsFlat B S hS f) (hft : IsLocallyOfFiniteType B S hS f) :
    IsFlat B S hS (pullback.snd f g) ∧ IsLocallyOfFiniteType B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isFlat_pullback_snd_of_isLocallyOfFiniteTypeOnReductions'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeRefined.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeRefined.lean#L78). The attribute's comment: “part (1), on the 0GBG transfer inputs and the 0GC7 (4) implies (1) inputs”.

> **Stacks 0GCE, part (1).** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of locally
> Noetherian formal algebraic spaces over `S`. If `f` is flat in the sense of Definition 0GCC and
> the morphism of reductions `g_red : Z_red ⟶ Y_red` is locally of finite type, then the base
> change `X ×_Y Z ⟶ Z` is flat.
>
> Flatness of arrows of `WAdm^{Noeth}` is stable under base change by arrows of finite type on
> reductions by part (1) of Stacks 0GCA, which the library proves outright; Remark 0GBG transfers
> that to the second projection of the fibre product, on the two inputs `h31` and `hcover` it
> carries — the invariance of flatness under isomorphism of targets is read off the locality
> field of the stability bundle, whose first axiom it is; and the hypothesis on `g_red` becomes the chart condition the transfer
> consumes by the implication (4) ⟹ (1) of Stacks 0GC7, on the two inputs `hbridge` and
> `hredsquare`. Nothing about flatness is assumed in any of the five.

```lean
theorem isFlat_pullback_snd_of_isLocallyOfFiniteTypeOnReductions'
    (h31 : SourceCoverImpliesEveryAffineEtaleDiagram B S hS
      TopologicalRing.IsNoetherianAdic TopologicalRing.IsFlatHom)
    (hbridge : ChartPropertyIsFiniteTypeOnReductions B S hS)
    (hredsquare : IsLocallyOfFiniteTypeOnReductionsOnEveryAffineEtaleSquare B S hS)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Z ⟶ Y)
    (hcover : HasBaseChangeCoverOverPullbackSnd B S hS f g)
    (hZ : IsLocallyCountablyIndexed B S hS Z) (hY : IsLocallyCountablyIndexed B S hS Y)
    (hf : IsFlat B S hS f) (hg : IsLocallyOfFiniteTypeOnReductions B S hS g) :
    IsFlat B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_pullback_snd_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeRefined.lean, line 253](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/Restricted/FlatBaseChangeRefined.lean#L253). The attribute's comment: “part (2), locally of finite type, from Stacks 0AQ5 alone -- the second projection is a base change of `f`. No input of Remark 0GBF and no comparison of Stacks 0GC0 is used, and flatness of `f` is not used”.

> **Stacks 0GCE, part (2), locally of finite type.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be
> morphisms of locally Noetherian formal algebraic spaces over `S`. If `f` is locally of finite
> type in the sense of Stacks 0AM4, then the base change `X ×_Y Z ⟶ Z` is locally of finite type.
>
> The second projection of the fibre product is a base change of `f`, and a base change of a
> morphism locally of finite type is locally of finite type by **Stacks 0AQ5**, which the library
> proves outright as `IsLocallyOfFiniteType.of_isPullback`. Nothing else is needed, so neither
> flatness of `f` nor the locally Noetherian hypotheses of the source nor the inputs of the
> transfer of Remark 0GBF appear: the conclusion holds at every morphism of fppf sheaves, which is
> at least as general as part (2) of the source.

```lean
theorem isLocallyOfFiniteType_pullback_snd_of_isLocallyOfFiniteType {X Y Z : FppfSheaf B S hS}
    (f : X ⟶ Y) (g : Z ⟶ Y) (hft : IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS (pullback.snd f g)
```

## Tag 0GCF, a lemma

[Tag 0GCF](https://stacks.math.columbia.edu/tag/0GCF) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFlat_comp_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatComposition.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatComposition.lean#L58).

> **Stacks 0GCF.** If `f : X ⟶ Y` and `g : Y ⟶ Z` are flat morphisms of locally Noetherian
> formal algebraic spaces over `S`, then `g ∘ f` is flat.
>
> Flatness is condition (1) of Stacks 0ANG for Noetherian adic rings and flat ring maps, a local
> property stable under composition (Stacks 0GCB), so Remark 0GBK applies.

```lean
theorem isFlat_comp_of_isLocallyNoetherian {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hZ : IsLocallyNoetherian B S hS Z)
    (hf : IsFlat B S hS f) (hg : IsFlat B S hS g) :
    IsFlat B S hS (f ≫ g)
```

## Tag 0GCG, a lemma

[Tag 0GCG](https://stacks.math.columbia.edu/tag/0GCG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFlat_of_hasPropertyULift_flatPropertyULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/FlatOfBootstrapFlat.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/FlatOfBootstrapFlat.lean#L223).

> **Stacks 0GCG.** A morphism `f : X ⟶ Y` of formal algebraic spaces over `S` which is
> representable by algebraic spaces and flat in the Bootstrap sense of Stacks 03XZ is flat in the
> sense of Definition 0GCC.
>
> On an affine representable étale square over `f`, the homomorphism `φ` presenting the chart map
> is taut because `f` is representable. Bootstrap flatness of `f` makes `φ` flat modulo every
> weak ideal of definition of its source, and Stacks 0912 concludes that `φ` is flat. The source
> assumes `X` and `Y` locally Noetherian; the proof does not use this.

```lean
theorem isFlat_of_hasPropertyULift_flatPropertyULift {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS f.hom)
    (hflat : Space.HasPropertyULift.{u + 1} B S hS (Space.flatPropertyULift.{u + 1} B S hS)
      f.hom hrep) :
    IsFlat B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.13, Tag 0GC8](https://stacks.math.columbia.edu/tag/0GC8)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
