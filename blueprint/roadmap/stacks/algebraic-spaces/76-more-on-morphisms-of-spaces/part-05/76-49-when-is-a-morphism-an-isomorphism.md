---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isOpenSubspace_forall_factorsThrough_iff_isUnramified_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isUnramified_universallyInjective_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isClosedImmersion_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isFlat_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isSurjective_isFlat_baseChange, AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isIso_baseChange, AlgebraicGeometry.Space.koszulLocusOnBase, AlgebraicGeometry.Space.range_pointsMap_ι_koszulLocusOnBase
statement: formalized
proof: formalized
---

# 76.49 When is a morphism an isomorphism?

Section 76.49 of the Stacks Project, [Tag 05X7](https://stacks.math.columbia.edu/tag/05X7). 7 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05X8, a lemma

[Tag 05X8](https://stacks.math.columbia.edu/tag/05X8) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_forall_factorsThrough_iff_isUnramified_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean, line 291](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean#L291).

> **Stacks 05X8.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` whose source and
> target are given over a third algebraic space `Z` by morphisms `p : X ⟶ Z` and `q : Y ⟶ Z` with
> `f ≫ q = p`. If `p` is locally of finite type and closed, then there is an open subspace `W` of
> `Z` through which a morphism `Z' ⟶ Z` from an algebraic space factors exactly when the base
> change of `f` along it is unramified.
>
> The open subspace is the one cut out, through the correspondence of Stacks 03BZ, by the
> complement of the image under `p` of the set of points at which `f` is not unramified: that set
> is closed because the unramified locus of part (1) of Stacks 05W2 is open, and its image is
> closed because `p` is. Factoring through `W` is the containment of the image of the points of
> `Z'` in that complement, by Stacks 03IE, while unramifiedness of the base change is
> unramifiedness at each of its points, by Stacks 03ZK; part (2) of Stacks 05W2 identifies the
> latter with unramifiedness of `f` at each point of `X` lying over a point of the image of `Z'`,
> and the two conditions then agree by a complementation.

```lean
theorem exists_isOpenSubspace_forall_factorsThrough_iff_isUnramified_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFiniteType B S hS p) (hpc : IsClosedMorphism B S hS p) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsUnramified B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 05X9, a lemma

[Tag 05X9](https://stacks.math.columbia.edu/tag/05X9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isUnramified_universallyInjective_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UnramifiedLocusOnBase.lean#L545).

> **Stacks 05X9.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` whose source and
> target are given over a third algebraic space `Z` by morphisms `p : X ⟶ Z` and `q : Y ⟶ Z` with
> `f ≫ q = p`. If `p` is locally of finite type and closed and the morphism `X ×_Y X ⟶ Z` given by
> the first projection followed by `p` is closed, then there is an open subspace `W` of `Z`
> through which a morphism `Z' ⟶ Z` from an algebraic space factors exactly when the base change
> of `f` along it is unramified and universally injective.
>
> The open subspace is cut out, through the correspondence of Stacks 03BZ, by the point set of the
> open subspace of Stacks 05X8 intersected with the complement of the image under `X ×_Y X ⟶ Z` of
> the complement of the image of the relative diagonal of the base change of `f` over that open
> subspace; that image is an open subspace of `X ×_Y X` because the relative diagonal of an
> unramified morphism is an open immersion by part (1) of Stacks 05W1 and because `X ×_Z W₀` sits
> inside `X ×_Y X` as a base change of `W₀`. Factoring through the intersection is, by Stacks 03IE,
> the conjunction of factoring through the open subspace of Stacks 05X8 and of every point of
> `X ×_Y X` over the image of `Z'` lying in the image of the diagonal, and the second condition is
> universal injectivity of the base change.

```lean
theorem exists_isOpenSubspace_iff_isUnramified_universallyInjective_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFiniteType B S hS p) (hpc : IsClosedMorphism B S hS p)
    (hp₂ : IsClosedMorphism B S hS (pullback.fst f f ≫ p)) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsUnramified B S hS (baseChangeOverBase B S hS f p q hfq g) ∧
            UniversallyInjective B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 05XA, a lemma

[Tag 05XA](https://stacks.math.columbia.edu/tag/05XA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isClosedImmersion_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersionLocusOnBase.lean, line 82](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ClosedImmersionLocusOnBase.lean#L82).

> **Stacks 05XA.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` whose source and
> target are given over a third algebraic space `Z` by morphisms `p : X ⟶ Z` and `q : Y ⟶ Z` with
> `f ≫ q = p`. If `p` is locally of finite type and universally closed and `q` is separated, then
> there is an open subspace `W` of `Z` through which a morphism `Z' ⟶ Z` from an algebraic space
> factors exactly when the base change of `f` along it is a closed immersion.
>
> The open subspace is the one of Stacks 05X9 for the same triangle, over which the base change
> of `f` is unramified and universally injective: it is available because `p` is closed and
> because `X ×_Y X ⟶ Z` is closed, being a base change of `f` followed by `p`. Every base change
> of `f` is universally closed, since `f` is by part (1) of Stacks 04NX, so the three conditions
> of Stacks 05W8 for the base change reduce to the two cut out by that subspace.

```lean
theorem exists_isOpenSubspace_iff_isClosedImmersion_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFiniteType B S hS p) (hpuc : UniversallyClosed B S hS p)
    (hq : IsSeparated B S hS q) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsClosedImmersion B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 05XB, a lemma

[Tag 05XB](https://stacks.math.columbia.edu/tag/05XB) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusOnBase.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusOnBase.lean#L131). The attribute's comment: “the open subspace of the base over which the morphism becomes flat”.

> **Stacks 05XB.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` whose source and target are given over a third algebraic space `Z` by morphisms
> `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`.  If `p` is locally of finite presentation, flat
> and closed and `q` is locally of finite type, then there is an open subspace `W` of `Z` through
> which a morphism `Z' ⟶ Z` from an algebraic space factors exactly when the base change of `f`
> along it is flat.
>
> The open subspace is cut out, through the correspondence of Stacks 03BZ, by the complement of
> the image under `p` of the set of points of `X` at which `f` is not flat, which is closed by the
> openness half of Stacks 05X3 and whose image is closed because `p` is.  Factoring through it
> is the containment of the image of the points of `Z'` in that complement by Stacks 03IE, and
> flatness of the base change is flatness at each of its points by Stacks 03MM, which the
> base-change half of Stacks 05X3 reads off from flatness of `f` over the image of `Z'`.

```lean
theorem exists_isOpenSubspace_iff_isFlat_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFinitePresentation B S hS p) (hpflat : IsFlat B S hS p)
    (hpc : IsClosedMorphism B S hS p) (hq : IsLocallyOfFiniteType B S hS q) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsFlat B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 05XC, a lemma

[Tag 05XC](https://stacks.math.columbia.edu/tag/05XC) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isSurjective_isFlat_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusOnBase.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/FlatLocusOnBase.lean#L209). The attribute's comment: “the open subspace of the base over which the morphism becomes surjective and flat”.

> **Stacks 05XC.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` whose source and target are given over a third algebraic space `Z` by morphisms
> `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`.  If `p` is locally of finite presentation, flat
> and closed and `q` is locally of finite type and closed, then there is an open subspace `W` of
> `Z` through which a morphism `Z' ⟶ Z` from an algebraic space factors exactly when the base
> change of `f` along it is surjective and flat.
>
> The open subspace is cut out by the point set of the subspace `W₀` of Stacks 05XB intersected
> with the locus of points of `Z` whose fibre in `|Y|` lies in the image of `X ×_Z W₀ ⟶ Y`.  That
> locus is open because `q` is closed and because `X ×_Z W₀ ⟶ Y` is open on points, being the
> base change of `f` over `W₀` — flat by the choice of `W₀` and locally of finite presentation,
> hence universally open by Stacks 042S — followed by the open immersion `Y ×_Z W₀ ⟶ Y`.  Over
> `W₀` its image coincides with the image of `f`, and containment of the image of `Z'` in the
> locus is surjectivity of the base change.

```lean
theorem exists_isOpenSubspace_iff_isSurjective_isFlat_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFinitePresentation B S hS p) (hpflat : IsFlat B S hS p)
    (hpc : IsClosedMorphism B S hS p) (hq : IsLocallyOfFiniteType B S hS q)
    (hqc : IsClosedMorphism B S hS q) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsSurjective B S hS (baseChangeOverBase B S hS f p q hfq g) ∧
            IsFlat B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 05XD, a lemma

[Tag 05XD](https://stacks.math.columbia.edu/tag/05XD) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_iff_isIso_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IsomorphismLocusOnBase.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/IsomorphismLocusOnBase.lean#L125). The attribute's comment: “the open subspace of the base over which the morphism becomes an isomorphism”.

> **Stacks 05XD.**  Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` whose source and target are given over a third algebraic space `Z` by morphisms
> `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`.  If `p` is locally of finite presentation, flat
> and universally closed and `q` is locally of finite type, closed and separated, then there is an
> open subspace `W` of `Z` through which a morphism `Z' ⟶ Z` from an algebraic space factors
> exactly when the base change of `f` along it is an isomorphism.
>
> The open subspace is the intersection, formed on point sets through the correspondence of
> Stacks 03BZ, of the open subspace of Stacks 05XC over which the base change is surjective and
> flat with that of Stacks 05XA over which it is a closed immersion.  A surjective flat closed
> immersion is an isomorphism, and an isomorphism is surjective, flat and a closed immersion.

```lean
theorem exists_isOpenSubspace_iff_isIso_baseChange
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hp : IsLocallyOfFinitePresentation B S hS p) (hpflat : IsFlat B S hS p)
    (hpuc : UniversallyClosed B S hS p) (hq : IsLocallyOfFiniteType B S hS q)
    (hqc : IsClosedMorphism B S hS q) (hqsep : IsSeparated B S hS q) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsIso (baseChangeOverBase B S hS f p q hfq g)
```

## Tag 06CE, a lemma

[Tag 06CE](https://stacks.math.columbia.edu/tag/06CE) in the Stacks Project.

**`AlgebraicGeometry.Space.koszulLocusOnBase`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean#L153). The attribute's comment: “the open subspace of the base”.

> **Stacks 06CE.** The open subspace `W ⊂ Z` of a morphism `f : X ⟶ Y` of algebraic spaces
> over `S` whose source is given over `Z` by `p : X ⟶ Z`: the subspace of the base cut out by
> the complement of the image under `p` of the set of points at which `f` is not Koszul, so that
> a point of `|Z|` lies in `W` exactly when `f` is Koszul at every point of `|X|` above it.

```lean
public def koszulLocusOnBase (f : X ⟶ Y) (p : X ⟶ Z) : Subfunctor Z
```

**`AlgebraicGeometry.Space.range_pointsMap_ι_koszulLocusOnBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean#L160). The attribute's comment: “the point set of the open subspace of the base”.

> The point set of `W` is the complement of the image under `p` of the non-Koszul locus
> of `f`.

```lean
public theorem range_pointsMap_ι_koszulLocusOnBase (f : X ⟶ Y) (p : X ⟶ Z) :
    Set.range (pointsMap B S hS (koszulLocusOnBase B S hS f p).toFunctor
        (koszulLocusOnBase B S hS f p).ι) =
      (pointsMap B S hS X p '' {x : points B S hS X | KoszulAt B S hS f x}ᶜ)ᶜ
```

**`AlgebraicGeometry.Space.isOpenSubspace_koszulLocusOnBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBase.lean#L172). The attribute's comment: “the subspace of the base is open”.

> **Stacks 06CE.** `W` is an open subspace of `Z`.
>
> The non-Koszul locus of `f` is closed because the Koszul locus is open by Stacks 06CA, its
> image under `p` is closed because `p` is closed, and the complement of a closed set is open,
> hence the point set of an open subspace by Stacks 03BZ.

```lean
public theorem isOpenSubspace_koszulLocusOnBase (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y)
    (p : X ⟶ Z) (hpc : IsClosedMorphism B S hS p) :
    IsOpenSubspace B S hS (koszulLocusOnBase B S hS f p)
```

**`AlgebraicGeometry.Space.factorsThrough_koszulLocusOnBase_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean#L110). The attribute's comment: “with the open subspace named rather than quantified over”.

> **Stacks 06CE, with the open subspace named.** Let `f : X ⟶ Y` be a morphism of algebraic
> spaces over `S` whose source and target are given over a third algebraic space `Z` by morphisms
> `p : X ⟶ Z` and `q : Y ⟶ Z` with `f ≫ q = p`. If `p` is flat, locally of finite presentation and
> closed and `q` is flat and locally of finite presentation, then a morphism `Z' ⟶ Z` from an
> algebraic space factors through `AlgebraicGeometry.Space.koszulLocusOnBase` exactly when the base
> change of `f` along it is a local complete intersection morphism.

```lean
theorem factorsThrough_koszulLocusOnBase_iff
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hpflat : IsFlat B S hS p) (hplfp : IsLocallyOfFinitePresentation B S hS p)
    (hpc : IsClosedMorphism B S hS p) (hqflat : IsFlat B S hS q)
    (hqlfp : IsLocallyOfFinitePresentation B S hS q)
    (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hZ' : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z) :
    (∃ r : Z' ⟶ (koszulLocusOnBase B S hS f p).toFunctor,
        r ≫ (koszulLocusOnBase B S hS f p).ι = g) ↔
      IsLocalCompleteIntersection B S hS (baseChangeOverBase B S hS f p q hfq g)
```

**`AlgebraicGeometry.Space.exists_isOpenSubspace_factorsThrough_iff_isLocalCompleteIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/LocalCompleteIntersection/KoszulLocusOnBaseUnconditional.lean#L135).

> **Stacks 06CE.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` whose source and
> target are given over a third algebraic space `Z` by morphisms `p : X ⟶ Z` and `q : Y ⟶ Z` with
> `f ≫ q = p`. If `p` is flat, locally of finite presentation and closed and `q` is flat and
> locally of finite presentation, then there is an open subspace `W` of `Z` through which a
> morphism `Z' ⟶ Z` from an algebraic space factors exactly when the base change
> `f_{Z'} : X_{Z'} ⟶ Y_{Z'}` of `f` along it is a local complete intersection morphism.
>
> The open subspace is `AlgebraicGeometry.Space.koszulLocusOnBase`: the complement of the image
> under `p` of the non-Koszul locus of `f`.

```lean
theorem exists_isOpenSubspace_factorsThrough_iff_isLocalCompleteIntersection
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z) (hfq : f ≫ q = p)
    (hpflat : IsFlat B S hS p) (hplfp : IsLocallyOfFinitePresentation B S hS p)
    (hpc : IsClosedMorphism B S hS p) (hqflat : IsFlat B S hS q)
    (hqlfp : IsLocallyOfFinitePresentation B S hS q) :
    ∃ W : Subfunctor Z, IsOpenSubspace B S hS W ∧
      ∀ (Z' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (_ : IsAlgebraicSpace B S hS Z') (g : Z' ⟶ Z),
        (∃ r : Z' ⟶ W.toFunctor, r ≫ W.ι = g) ↔
          IsLocalCompleteIntersection B S hS (baseChangeOverBase B S hS f p q hfq g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.49, Tag 05X7](https://stacks.math.columbia.edu/tag/05X7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
