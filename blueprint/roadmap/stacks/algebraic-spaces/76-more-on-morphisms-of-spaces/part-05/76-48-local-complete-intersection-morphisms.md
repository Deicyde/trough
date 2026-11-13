---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsLocalCompleteIntersection, AlgebraicGeometry.Space.KoszulAt, AlgebraicGeometry.Space.isKoszulRegularImmersion_of_isLocalCompleteIntersection, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isLocalCompleteIntersection, AlgebraicGeometry.Space.isPseudoCoherent_of_isLocalCompleteIntersection, AlgebraicGeometry.Space.isPerfect_of_isLocalCompleteIntersection, AlgebraicGeometry.Space.isLocalCompleteIntersection_pullback_snd, AlgebraicGeometry.Space.isLocalCompleteIntersection_comp
statement: formalized
proof: formalized
---

# 76.48 Local complete intersection morphisms

Section 76.48 of the Stacks Project, [Tag 06C3](https://stacks.math.columbia.edu/tag/06C3). 13 tags here are carried by 21 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06C4, a definition

[Tag 06C4](https://stacks.math.columbia.edu/tag/06C4) in the Stacks Project.

**`AlgebraicGeometry.Space.IsLocalCompleteIntersection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection.lean#L77). The attribute's comment: “part (1): local complete intersection morphisms”.

> **Stacks 06C4, part (1).** A morphism of algebraic spaces over `S` is a *local complete
> intersection morphism*, or a *Koszul morphism*, when every commuting square of étale scheme
> charts induces a local complete intersection morphism of schemes.

```lean
abbrev IsLocalCompleteIntersection (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.KoszulAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection.lean#L86). The attribute's comment: “part (2): Koszul at a point”.

> **Stacks 06C4, part (2).** A morphism of algebraic spaces over `S` is *Koszul at* a
> point `x` of its source when it is a local complete intersection morphism on an open
> subspace of the source containing `x`.

```lean
abbrev KoszulAt (f : X ⟶ Y) (x : points B S hS X) : Prop
```

## Tag 06C5, a lemma

[Tag 06C5](https://stacks.math.columbia.edu/tag/06C5) in the Stacks Project.

**`AlgebraicGeometry.Space.isKoszulRegularImmersion_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ImmersionIntoSmooth.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ImmersionIntoSmooth.lean#L236).

> **Stacks 06C5.** Let `f : X ⟶ Y` be a local complete intersection morphism of algebraic
> spaces over `S`, let `p : P ⟶ Y` be smooth, let `a : U ⟶ X` be étale and let `i : U ⟶ P` be an
> immersion over `Y`. Then `i` is a Koszul-regular immersion of algebraic spaces.

```lean
theorem isKoszulRegularImmersion_of_isLocalCompleteIntersection (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y U P : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hU : IsAlgebraicSpace B S hS U) (_hP : IsAlgebraicSpace B S hS P)
    (f : X ⟶ Y) (a : U ⟶ X) (i : U ⟶ P) (p : P ⟶ Y)
    (hf : IsLocalCompleteIntersection B S hS f) (ha : IsEtale B S hS a)
    (hi : IsImmersion B S hS i) (hp : IsSmooth B S hS p) (hcomm : a ≫ f = i ≫ p) :
    IsKoszulRegularImmersion B S hS i
```

## Tag 06C6, a lemma

[Tag 06C6](https://stacks.math.columbia.edu/tag/06C6) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean#L56). The attribute's comment: “part (1): locally of finite presentation”.

> **Stacks 06C6, part (1).** A local complete intersection morphism of algebraic spaces over
> `S` is locally of finite presentation.

```lean
theorem isLocallyOfFinitePresentation_of_isLocalCompleteIntersection (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsLocalCompleteIntersection B S hS f) :
    IsLocallyOfFinitePresentation B S hS f
```

**`AlgebraicGeometry.Space.isPseudoCoherent_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean#L66). The attribute's comment: “part (2): pseudo-coherent”.

> **Stacks 06C6, part (2).** A local complete intersection morphism of algebraic spaces over
> `S` is pseudo-coherent.

```lean
theorem isPseudoCoherent_of_isLocalCompleteIntersection (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsLocalCompleteIntersection B S hS f) :
    IsPseudoCoherent B S hS f
```

**`AlgebraicGeometry.Space.isPerfect_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Perfect.lean#L76). The attribute's comment: “part (3): perfect”.

> **Stacks 06C6, part (3).** A local complete intersection morphism of algebraic spaces over
> `S` is perfect.

```lean
theorem isPerfect_of_isLocalCompleteIntersection (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : IsLocalCompleteIntersection B S hS f) :
    IsPerfect B S hS f
```

## Tag 06C7, a lemma

[Tag 06C7](https://stacks.math.columbia.edu/tag/06C7) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/FlatBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/FlatBaseChange.lean#L110).

> A flat base change of a local complete intersection morphism of algebraic spaces is a local
> complete intersection morphism: if `f : X ⟶ Y` is Koszul and `g : Y' ⟶ Y` is flat, then the
> projection `X ×_Y Y' ⟶ Y'` is Koszul.

```lean
public theorem isLocalCompleteIntersection_pullback_snd
    {X Y Y' : AlgebraicSpaces B S hS} (f : X ⟶ Y) (g : Y' ⟶ Y)
    (hg : IsFlat B S hS g.hom)
    (hf : IsLocalCompleteIntersection B S hS f.hom) :
    IsLocalCompleteIntersection B S hS (Limits.pullback.snd f.hom g.hom)
```

## Tag 06C8, a lemma

[Tag 06C8](https://stacks.math.columbia.edu/tag/06C8) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Composition.lean, line 36](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Composition.lean#L36).

> A composition of local complete intersection morphisms of algebraic spaces over `S` is a
> local complete intersection morphism: if `f : X ⟶ Y` and `g : Y ⟶ Z` are local complete
> intersection morphisms, so is `f ≫ g`.

```lean
public theorem isLocalCompleteIntersection_comp (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocalCompleteIntersection B S hS f)
    (hg : IsLocalCompleteIntersection B S hS g) :
    IsLocalCompleteIntersection B S hS (f ≫ g)
```

## Tag 06C9, a lemma

[Tag 06C9](https://stacks.math.columbia.edu/tag/06C9) in the Stacks Project.

**`AlgebraicGeometry.Space.isSyntomic_iff_isFlat_and_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Syntomic.lean#L148).

> **Stacks 06C9.** A morphism of algebraic spaces over `S` is syntomic if and only if it is
> flat and a local complete intersection morphism.
>
> All three properties are the condition of Tag 03MJ on every commuting square of étale charts, so
> the statement is the scheme-level equivalence of Tag 069K quantified over the charts.

```lean
theorem isSyntomic_iff_isFlat_and_isLocalCompleteIntersection (f : X ⟶ Y) :
    IsSyntomic B S hS f ↔ IsFlat B S hS f ∧ IsLocalCompleteIntersection B S hS f
```

## Tag 0CHK, a lemma

[Tag 0CHK](https://stacks.math.columbia.edu/tag/0CHK) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_of_isKoszulRegularImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionLocalCompleteIntersection.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RegularImmersionLocalCompleteIntersection.lean#L73).

> **Stacks 0CHK.** A Koszul-regular immersion of algebraic spaces over `S` is a local complete
> intersection morphism.

```lean
theorem isLocalCompleteIntersection_of_isKoszulRegularImmersion (i : X ⟶ Y)
    (hi : IsKoszulRegularImmersion B S hS i) :
    IsLocalCompleteIntersection B S hS i
```

## Tag 0CHL, a lemma

[Tag 0CHL](https://stacks.math.columbia.edu/tag/0CHL) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_of_comp_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/SmoothPermanence.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/SmoothPermanence.lean#L105).

> Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over `S` with `g` smooth.
> If the composite `f ≫ g` is a local complete intersection morphism, then so is `f`.

```lean
public theorem isLocalCompleteIntersection_of_comp_of_isSmooth
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hg : IsSmooth B S hS g)
    (hfg : IsLocalCompleteIntersection B S hS (f ≫ g)) :
    IsLocalCompleteIntersection B S hS f
```

## Tag 0CHM, a lemma

[Tag 0CHM](https://stacks.math.columbia.edu/tag/0CHM) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_isLocalAtTarget_fpqc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/FpqcLocalAtTarget.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/FpqcLocalAtTarget.lean#L211).

> **Stacks 0CHM.** The property of being a local complete intersection morphism of algebraic
> spaces over `S` is local on the base for the fpqc topology of Stacks 03YH: a morphism is Koszul
> exactly when its base changes along the members of an fpqc covering of its target are.

```lean
theorem isLocalCompleteIntersection_isLocalAtTarget_fpqc :
    MorphismProperty.IsLocalAtTarget
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (f : X ⟶ Y) =>
        IsLocalCompleteIntersection B S hS f.hom)
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 0CHN, a lemma

[Tag 0CHN](https://stacks.math.columbia.edu/tag/0CHN) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocalCompleteIntersection_isLocalAtSource_syntomic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Locality.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/Locality.lean#L127).

> **Stacks 0CHN.** The property of being a local complete intersection morphism of algebraic
> spaces over `S` is local on the source for the syntomic topology of Stacks 03YH.
>
> The schemes case, Stacks 069P, is
> `AlgebraicGeometry.isLocalAtSource_syntomic_isLocalCompleteIntersectionMorphism`; the étale
> locality on source and target that the transfer also consumes needs only its étale restriction,
> `AlgebraicGeometry.isLocalCompleteIntersectionMorphism_isLocalAtSource_etale`.

```lean
public theorem isLocalCompleteIntersection_isLocalAtSource_syntomic :
    MorphismProperty.IsLocalAtSource
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) =>
        IsLocalCompleteIntersection B S hS f.hom)
      (Topology.precoverage.{u, v} .syntomic B S hS)
```

## Tag 06CA, a lemma

[Tag 06CA](https://stacks.math.columbia.edu/tag/06CA) in the Stacks Project.

**`AlgebraicGeometry.Space.koszulOpenSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean#L88). The attribute's comment: “part (1): the open subspace of Koszul points”.

> **Stacks 06CA, part (1).** The open subspace `U(f) ⊂ X` of the Koszul points of a
> morphism `f : X ⟶ Y` of algebraic spaces: the subfunctor of the source whose sections are
> those all of whose points are Koszul points of `f`.

```lean
def koszulOpenSubspace (f : X ⟶ Y) : Subfunctor X
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_koszulOpenSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean#L94). The attribute's comment: “part (1): the open subspace of Koszul points”.

> **Stacks 06CA, part (1).** The point set of `U(f)` is the set of points at which `f` is
> Koszul.

```lean
theorem range_pointsMap_ι_koszulOpenSubspace (f : X ⟶ Y) :
    Set.range (pointsMap B S hS (koszulOpenSubspace B S hS X f).toFunctor
      (koszulOpenSubspace B S hS X f).ι) = {x | KoszulAt B S hS f x}
```

**`AlgebraicGeometry.Space.isOpenSubspace_koszulOpenSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean#L101). The attribute's comment: “part (1): the open subspace of Koszul points”.

> **Stacks 06CA, part (1).** `U(f)` is an open subspace of the source.

```lean
theorem isOpenSubspace_koszulOpenSubspace (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    IsOpenSubspace B S hS (koszulOpenSubspace B S hS X f)
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_range_pointsMap_eq_setOf_koszulAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocus.lean#L110). The attribute's comment: “part (1): the open subspace of Koszul points”.

> **Stacks 06CA, part (1).** There is an open subspace of the source of a morphism of
> algebraic spaces whose point set is exactly the set of points at which the morphism is
> Koszul.

```lean
theorem exists_isOpenSubspace_range_pointsMap_eq_setOf_koszulAt
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    ∃ U : Subfunctor X, IsOpenSubspace B S hS U ∧
      Set.range (pointsMap B S hS U.toFunctor U.ι) = {x | KoszulAt B S hS f x}
```

**`AlgebraicGeometry.Space.koszulOpenSubspace_pullbackMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusBaseChange.lean, line 393](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusBaseChange.lean#L393). The attribute's comment: “part (2): base change of the Koszul open subspace”.

> **Stacks 06CA, part (2).** The open subspace `U(f')` of the Koszul points of the base change
> `f'` of `f` along an arbitrary `Z' ⟶ Z` is the inverse image of `U(f)` under the projection
> `X' ⟶ X`.
>
> The one input from the theory of schemes is that the Koszul property of morphisms of schemes is
> local on the source for the étale topology — Stacks 069P restricted to étale coverings.

```lean
theorem koszulOpenSubspace_pullbackMap
    {X Y Z Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (hZ' : IsAlgebraicSpace B S hS Z')
    (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hpq : f ≫ q = p)
    (hp : IsFlat B S hS p) (hplfp : IsLocallyOfFinitePresentation B S hS p)
    (hq : IsFlat B S hS q) (hqlfp : IsLocallyOfFinitePresentation B S hS q)
    (z : Z' ⟶ Z) :
    koszulOpenSubspace B S hS (pullback p z)
        (pullback.map p z q z f (𝟙 _) (𝟙 _)
          (by simpa only [Category.comp_id] using hpq.symm) (by simp)) =
      (koszulOpenSubspace B S hS X f).preimage (pullback.fst p z)
```

**`AlgebraicGeometry.Space.koszulLocusStableUnderBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean#L92). The attribute's comment: “part (2) in the pointwise form the hypothesis of Stacks 06CE asks for”.

> **The base-change assertion of Stacks 06CA holds.** For a commutative triangle of algebraic
> spaces over `S` with `p` and `q` flat and locally of finite presentation, the base change of `f`
> along any `Z' ⟶ Z` is Koszul at a point of `|X ×_Z Z'|` exactly when `f` is Koszul at its image
> in `|X|`.
>
> This is `AlgebraicGeometry.Space.setOf_koszulAt_pullbackMap` read at one point, its hypothesis of
> étale source locality of the Koszul property of morphisms of schemes supplied by
> `AlgebraicGeometry.isLocalCompleteIntersectionMorphism_isLocalAtSource_etale`.

```lean
theorem koszulLocusStableUnderBaseChange : KoszulLocusStableUnderBaseChange B S hS
```

## Tag 06CB, a lemma

[Tag 06CB](https://stacks.math.columbia.edu/tag/06CB) in the Stacks Project.

**`AlgebraicGeometry.Space.unramified_iff_formallyUnramified_and_isFiniteLocallyFreeOnSite_conormalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalFiniteLocallyFree.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalFiniteLocallyFree.lean#L107). The attribute's comment: “unramified iff formally unramified; then the conormal sheaf is finite locally free”.

> **Stacks 06CB.**  Let `f : X ⟶ Y` be a local complete intersection morphism of algebraic
> spaces over `S`.  Then `f` is unramified if and only if it is formally unramified, and in this
> case the conormal sheaf `𝒞_{X/Y}` is finite locally free on `X`: for every universal first order
> thickening `t` of `f` — which exists exactly when `f` is formally unramified, by Stacks 0606 —
> the conormal sheaf of Stacks 0607 is finite locally free on the small étale site of `X`.

```lean
theorem unramified_iff_formallyUnramified_and_isFiniteLocallyFreeOnSite_conormalSheaf
    {X Y : AlgebraicSpaces B S hS} {f : X ⟶ Y}
    (hf : IsLocalCompleteIntersection B S hS f.hom) :
    (IsUnramified B S hS f.hom ↔ FormallyUnramified f.hom) ∧
      ∀ t : UniversalFirstOrderThickening B S hS f,
        SheafOfModules.IsFiniteLocallyFreeOnSite (conormalSheaf B S hS t)
```

## Tag 06CC, a lemma

[Tag 06CC](https://stacks.math.columbia.edu/tag/06CC) in the Stacks Project.

**`AlgebraicGeometry.Space.conormalSequence_shortExact_of_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalShortExactUnconditional.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/ConormalShortExactUnconditional.lean#L411).

> **Stacks 06CC.**  Let `Z ⟶ Y ⟶ X` be formally unramified morphisms of algebraic spaces over a
> scheme `S`, presented by universal first-order thickenings `Z ⊂ X₁` and `Y ⊂ X₂` over `X`, let
> `g₁ : X₁ ⟶ X₂` be a morphism over `X` restricting to `f₁ : Z ⟶ Y` (by Stacks 060A it is the
> canonical one), and let `F = Y ×_{X₂} X₁ ⊆ X₁` be the fibre product, inside which `Z` sits as the
> inverse image `W` of `Z ⊆ X₁`; by Stacks 06BF it is the universal first-order thickening of `Z`
> over `Y`.  If `f₁` is a local complete intersection morphism then the conormal sequence
>
> `0 ⟶ f₁^*𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0`
>
> of Stacks 06BD, read on `W`, is short exact: its first arrow is the inverse image along
> `W ⟶ Z` of the conormal map of Stacks 04CP of the square over `g₁`, and its second arrow is the
> conormal map of the fibre product square of `W ⊆ F` over `Z ⊆ X₁`.

```lean
theorem conormalSequence_shortExact_of_isLocalCompleteIntersection
    (hZ : IsUniversalFirstOrderThickening B S hS Z.1 p₁)
    (hY : IsUniversalFirstOrderThickening B S hS Y.1 p₂) (hg : g₁ ≫ p₂ = p₁)
    (hlci : IsLocalCompleteIntersection B S hS f₁.hom) :
    ∃ h : (modulePullback B S hS
          (X := ⟨(preimageSubspace B S hS (subspaceInclusion B S hS X₁
                (preimageSubspace B S hS g₁ Y)) Z).1.toFunctor,
              (preimageSubspace B S hS (subspaceInclusion B S hS X₁
                (preimageSubspace B S hS g₁ Y)) Z).2.1⟩)
          (preimageProjection B S hS (subspaceInclusion B S hS X₁
            (preimageSubspace B S hS g₁ Y)) Z)).map (conormalMap B S hS Z Y g₁ f₁ sq₁) ≫
        conormalMap B S hS
          (preimageSubspace B S hS (subspaceInclusion B S hS X₁ (preimageSubspace B S hS g₁ Y)) Z)
          Z (subspaceInclusion B S hS X₁ (preimageSubspace B S hS g₁ Y))
          (preimageProjection B S hS (subspaceInclusion B S hS X₁
            (preimageSubspace B S hS g₁ Y)) Z)
          (conormalEtaleRestrictionSquare B S hS
            (subspaceInclusion B S hS X₁ (preimageSubspace B S hS g₁ Y)) Z) = 0,
      (ShortComplex.mk _ _ h).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.48, Tag 06C3](https://stacks.math.columbia.edu/tag/06C3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
