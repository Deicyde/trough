---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_with_preimage_maximal_locus, AlgebraicGeometry.flat_maximal_locus_warning, AlgebraicGeometry.exists_open_with_preimage_maximal_cohenMacaulayLocus, AlgebraicGeometry.exists_open_with_preimage_maximal_etaleLocus, AlgebraicGeometry.exists_open_with_preimage_maximal_flatLocus, AlgebraicGeometry.exists_open_with_preimage_maximal_quasiFiniteLocus, AlgebraicGeometry.exists_open_with_preimage_maximal_relativeDimensionLE, AlgebraicGeometry.exists_open_with_preimage_maximal_smoothLocus
statement: formalized
proof: formalized
---

# 40.6 Properties of groupoids

Section 40.6 of the Stacks Project, [Tag 02YD](https://stacks.math.columbia.edu/tag/02YD). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04LH, a lemma

[Tag 04LH](https://stacks.math.columbia.edu/tag/04LH) in the Stacks Project.

**`AlgebraicGeometry.exists_open_with_preimage_maximal_locus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/MaximalLocus.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/MaximalLocus.lean#L128).

> **Stacks Project, Tag 04LH.** Suppose `P`, `Q`, and `R` are properties of morphisms of
> schemes, `R` implies `Q`, `Q` is stable under composition and base change, and maximal open
> `P`-loci exist for `Q`-morphisms and commute with base change by `R`-morphisms.  For a groupoid
> scheme whose source and target have `R`, the maximal `P`-locus of the indicated map from the
> pullback of its arrow scheme is the inverse image of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_locus
    (P Q R : MorphismProperty Scheme.{u})
    (hRQ : R ≤ Q) [Q.IsStableUnderComposition] [Q.IsStableUnderBaseChange]
    (hmax : ∀ {X Y : Scheme.{u}} (f : X ⟶ Y), Q f →
      ∃ V : X.Opens, IsGreatest {W : X.Opens | P (W.ι ≫ f)} V)
    (hbase : ∀ {X Y X' Y' : Scheme.{u}} {f : X ⟶ Y} {f' : X' ⟶ Y'}
      {p : X' ⟶ X} {q : Y' ⟶ Y}, Q f → R q → IsPullback p f' f q →
      ∀ {V : X.Opens}, IsGreatest {W : X.Opens | P (W.ι ≫ f)} V →
        IsGreatest {W' : X'.Opens | P (W'.ι ≫ f')} (p ⁻¹ᵁ V))
    {S : Scheme.{u}} (G : GroupoidScheme S) {U' : Scheme.{u}}
    (g : U' ⟶ G.objects.left) (hs : R G.source.left) (ht : R G.target.left) (hg : Q g) :
    ∃ W : U'.Opens,
      IsGreatest
        {V : (pullback g G.target.left).Opens |
          P (V.ι ≫ pullback.snd g G.target.left ≫ G.source.left)}
        ((pullback.fst g G.target.left) ⁻¹ᵁ W)
```

## Tag 04LI, a remark

[Tag 04LI](https://stacks.math.columbia.edu/tag/04LI) in the Stacks Project.

**`AlgebraicGeometry.flat_maximal_locus_warning`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/FlatLocusWarning.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/FlatLocusWarning.lean#L124). The attribute's comment: “hypotheses (1)-(4) of 04LH for P = flat, Q = empty, R = flat and locally of finite presentation, and a morphism whose largest flat open is not its flat locus; the base change hypothesis uses Mathlib's UniversallyOpen.of\_flat (01UA)”.

> **Stacks Project, Tag 04LI.** Stacks Tag 04LH applies to `P =` flat, `Q =` every morphism
> (the empty condition) and `R =` flat and locally of finite presentation: `R` implies `Q`, `Q` is
> stable under composition and base change, every morphism of schemes has a largest open of its
> source on which it is flat, and that open commutes with base change along a morphism which is
> flat and locally of finite presentation. But this largest flat open is not the set of points at
> which the morphism is flat: for some morphism of schemes it is strictly smaller.
>
> The largest flat open is `AlgebraicGeometry.maximalFlatOpen`, the interior of the pointwise flat
> locus. The counterexample is `AlgebraicGeometry.exists_flat_locus_not_open`; openness of the
> universally open map `p` (Mathlib's `AlgebraicGeometry.UniversallyOpen.of_flat`, Stacks 01UA)
> gives the base change compatibility.

```lean
public theorem flat_maximal_locus_warning :
    ((fun _ _ q => Flat q ∧ LocallyOfFinitePresentation q : MorphismProperty Scheme.{u}) ≤ ⊤) ∧
    (⊤ : MorphismProperty Scheme.{u}).IsStableUnderComposition ∧
    (⊤ : MorphismProperty Scheme.{u}).IsStableUnderBaseChange ∧
    (∀ {X Y : Scheme.{u}} (f : X ⟶ Y), ∃ V : X.Opens,
      IsGreatest {W : X.Opens | Flat (W.ι ≫ f)} V) ∧
    (∀ {X Y X' Y' : Scheme.{u}} {f : X ⟶ Y} {f' : X' ⟶ Y'} {p : X' ⟶ X} {q : Y' ⟶ Y},
      Flat q → LocallyOfFinitePresentation q → IsPullback p f' f q → ∀ {V : X.Opens},
        IsGreatest {W : X.Opens | Flat (W.ι ≫ f)} V →
          IsGreatest {W' : X'.Opens | Flat (W'.ι ≫ f')} (p ⁻¹ᵁ V)) ∧
    ∃ (X Y : Scheme.{u}) (f : X ⟶ Y) (W : X.Opens),
      IsGreatest {V : X.Opens | Flat (V.ι ≫ f)} W ∧
        (W.1 : Set X) ⊂ {x : X | IsFlatAt f.toLRSHom.toShHom x}
```

## Tag 047W, a remark

[Tag 047W](https://stacks.math.columbia.edu/tag/047W) in the Stacks Project.

**`AlgebraicGeometry.exists_open_with_preimage_maximal_cohenMacaulayLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayLocus.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/CohenMacaulayLocus.lean#L173). The attribute's comment: “cohen\_macaulay”.

> The maximal Cohen–Macaulay locus of `h : U' ×_{g,U,t} R ⟶ U` is the
> inverse image of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_cohenMacaulayLocus
    (D : FlatLocallyFinitelyPresentedGroupoidSituation) :
    ∃ W : D.U'.Opens,
      IsGreatest
        {V : D.fiberProduct.Opens |
          ∃ hf : ∀ y : D.groupoid.objects.left,
              IsLocallyNoetherian ((V.ι ≫ D.h).fiber y),
            Scheme.Hom.IsCohenMacaulay (V.ι ≫ D.h) hf}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_etaleLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocus.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/EtaleLocus.lean#L55). The attribute's comment: “etale”.

> **Stacks Project, Tag 047W, case (8).**  In the flat, locally finitely presented groupoid
> situation the largest open of `U' ×_{g, U, t} R` on which `h` is étale is the inverse image
> along the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_etaleLocus
    (D : FlatLocallyFinitelyPresentedGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest {V : D.fiberProduct.Opens | Etale (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_flatLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/FlatLocus.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/FlatLocus.lean#L59). The attribute's comment: “flat”.

> **Stacks Project, Tag 047W, case (4).**  In the flat, locally finitely presented groupoid
> situation the largest open of `U' ×_{g, U, t} R` on which `h` is flat is the inverse image along
> the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_flatLocus
    (D : FlatLocallyFinitelyPresentedGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest {V : D.fiberProduct.Opens | Flat (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_quasiFiniteLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/QuasiFiniteLocus.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/QuasiFiniteLocus.lean#L80). The attribute's comment: “locally quasi-finite”.

> **Stacks Project, Tag 047W, case (2).**  In the groupoid situation with structure maps
> locally of finite type, the largest open of `U' ×_{g, U, t} R` on which `h` is locally
> quasi-finite is the inverse image along the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_quasiFiniteLocus
    (D : LocallyOfFiniteTypeGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest
        {V : D.fiberProduct.Opens |
          LocallyOfFiniteType (V.ι ≫ D.h) ∧ LocallyQuasiFinite (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_relativeDimensionLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/RelativeDimensionLocus.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/RelativeDimensionLocus.lean#L99). The attribute's comment: “relative dimension at most d”.

> In the locally finite type groupoid situation, the relative-dimension-at-most-`d` locus of
> `h : U' ×_{g, U, t} R ⟶ U` is the inverse image of an open of `U'`, and it is the greatest open
> on which the restriction of `h` has that dimension bound.
>
> This is **Stacks Project, Tag 047W, case (1)**.

```lean
public theorem exists_open_with_preimage_maximal_relativeDimensionLE
    (D : LocallyOfFiniteTypeGroupoidSituation) (d : ℕ) :
    let _ : LocallyOfFiniteType
        (pullback.snd D.g D.groupoid.target.left ≫ D.groupoid.source.left) := inferInstance
    ∃ W : D.U'.Opens,
      IsGreatest
        {V : (pullback D.g D.groupoid.target.left).Opens |
          RelativeDimensionLE
            (V.ι ≫ pullback.snd D.g D.groupoid.target.left ≫ D.groupoid.source.left) d}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_smoothLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/SmoothLocus.lean, line 64](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/SmoothLocus.lean#L64). The attribute's comment: “smooth”.

> **Stacks Project, Tag 047W, case (7).**  In the flat, locally finitely presented groupoid
> situation the largest open of `U' ×_{g, U, t} R` on which `h` is smooth is the inverse image
> along the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_smoothLocus
    (D : FlatLocallyFinitelyPresentedGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest {V : D.fiberProduct.Opens | Smooth (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_syntomicLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/SyntomicLocus.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/SyntomicLocus.lean#L109). The attribute's comment: “syntomic”.

> **Stacks Project, Tag 047W, case (6).**  In the flat, locally finitely presented groupoid
> situation the largest open of `U' ×_{g, U, t} R` on which `h` is syntomic is the inverse image
> along the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_syntomicLocus
    (D : FlatLocallyFinitelyPresentedGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest {V : D.fiberProduct.Opens | Syntomic (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

**`AlgebraicGeometry.exists_open_with_preimage_maximal_unramifiedLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/UnramifiedLocus.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/UnramifiedLocus.lean#L98). The attribute's comment: “unramified”.

> **Stacks Project, Tag 047W, case (3).**  In the groupoid situation with structure maps
> locally of finite type, the largest open of `U' ×_{g, U, t} R` on which `h` is unramified is the
> inverse image along the projection of an open of `U'`.

```lean
public theorem exists_open_with_preimage_maximal_unramifiedLocus
    (D : LocallyOfFiniteTypeGroupoidSituation.{u}) :
    ∃ W : D.U'.Opens,
      IsGreatest {V : D.fiberProduct.Opens | Unramified (V.ι ≫ D.h)}
        ((pullback.fst D.g D.groupoid.target.left) ⁻¹ᵁ W)
```

## Tag 03JC, a lemma

[Tag 03JC](https://stacks.math.columbia.edu/tag/03JC) in the Stacks Project.

**`AlgebraicGeometry.isInvariantOpen_largestTargetOpen_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantLargestOpen.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/InvariantLargestOpen.lean#L77).

> **Stacks Project, Tag 03JC.** For a groupoid scheme whose source and target maps are
> coverings for one of the five topologies, the largest open of the object scheme over which the
> source map has a target-local property is invariant.

```lean
theorem isInvariantOpen_largestTargetOpen_source {S : Scheme.{u}} (G : GroupoidScheme S)
    (P Q : MorphismProperty Scheme.{u})
    (hQ : (Q = (@IsOpenImmersion : MorphismProperty Scheme.{u})) ∨ IsDescentMorphismClass Q)
    [P.IsLocalAtTarget (Scheme.precoverage Q)]
    (hs : Presieve.ofArrows (fun _ : Unit => G.arrows.left)
      (fun _ => G.source.left) ∈ Scheme.precoverage Q G.objects.left)
    (ht : Presieve.ofArrows (fun _ : Unit => G.arrows.left)
      (fun _ => G.target.left) ∈ Scheme.precoverage Q G.objects.left) :
    IsInvariantOpen G (largestTargetOpen P G.source.left)
```

## Tag 06QQ, a lemma

[Tag 06QQ](https://stacks.math.columbia.edu/tag/06QQ) in the Stacks Project.

**`AlgebraicGeometry.isInvariantOpen_largestTargetOpen_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/StabilizerLargestOpen.lean, line 514](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Groupoids/More/Properties/StabilizerLargestOpen.lean#L514).

> **Stacks Project, Tag 06QQ.** For a groupoid scheme whose source and target maps are
> coverings for one of the fppf, syntomic, smooth or étale topologies, the largest open of the
> object scheme over which the stabilizer group scheme has a target-local property is
> invariant.

```lean
theorem isInvariantOpen_largestTargetOpen_stabilizer {S : Scheme.{u}} (G : GroupoidScheme S)
    (P Q : MorphismProperty Scheme.{u}) (hQ : IsDescentMorphismClass Q)
    [P.IsLocalAtTarget (Scheme.precoverage Q)]
    (hs : Presieve.ofArrows (fun _ : Unit => G.arrows.left)
      (fun _ => G.source.left) ∈ Scheme.precoverage Q G.objects.left)
    (ht : Presieve.ofArrows (fun _ : Unit => G.arrows.left)
      (fun _ => G.target.left) ∈ Scheme.precoverage Q G.objects.left) :
    IsInvariantOpen G (largestTargetOpen P (stabilizer G).hom)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.6, Tag 02YD](https://stacks.math.columbia.edu/tag/02YD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
