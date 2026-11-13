---
declaration: section
origin: cited
lean: Stacks.Chow.isProper_and_relativeDimension_and_flatPullback_properPushforward, Stacks.Chow.properPushforward_flatPullback_of_isFiniteLocallyFreeOfRank, Stacks.Morphisms.isProper_of_isFiniteLocallyFreeOfRank, Stacks.Morphisms.flat_of_isFiniteLocallyFreeOfRank, Stacks.Morphisms.relativeDimension_zero_of_isFiniteLocallyFreeOfRank
statement: formalized
proof: formalized
---

# 42.15 Push and pull

Section 42.15 of the Stacks Project, [Tag 02RF](https://stacks.math.columbia.edu/tag/02RF). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02RG, a lemma

[Tag 02RG](https://stacks.math.columbia.edu/tag/02RG) in the Stacks Project.

**`Stacks.Chow.isProper_and_relativeDimension_and_flatPullback_properPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeGenuine.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/ProperPushforwardChowBaseChangeGenuine.lean#L159). The attribute's comment: “all three assertions, under the source's hypotheses: f' is proper, g' is flat of relative dimension r, and g^* f\_* alpha = f'\_* (g')^* alpha in Z\_\{k+r}(Y') for every k and every k-cycle alpha on X”.

> **Proper pushforward and flat pullback across a fibre product square.** Let
>
>       X' --g'--> X
>       |          |
>       f'         f
>       v          v
>       Y' --g-->  Y
>
> be a fibre product diagram of schemes locally of finite type over the base of chapter 42, with
> `f` proper and `g` flat of relative dimension `r`. Then `f'` is proper, `g'` is flat of relative
> dimension `r` (flat, locally of finite type, and of relative dimension `r` in the sense of
> Stacks 02NJ), and for every `k` and every `α ∈ Z_k(X)`,
>
> `g^* f_* α = f'_* (g')^* α`  in  `Z_{k+r}(Y')`.
>
> The first assertion is stability of properness under base change, the second is Stacks 02NK and
> stability of flatness and of local finite type under base change, and the third is
> `Stacks.Chow.flatPullback_properPushforward_unconditional`.

```lean
theorem isProper_and_relativeDimension_and_flatPullback_properPushforward
    (C : ChowSituation.{u}) {X Y X' Y' : Scheme.{u}}
    (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S) [LocallyOfFiniteType sY]
    (sX' : X' ⟶ C.S) [LocallyOfFiniteType sX'] (sY' : Y' ⟶ C.S) [LocallyOfFiniteType sY']
    (f : X ⟶ Y) [IsProper f] (g : Y' ⟶ Y) [LocallyOfFiniteType g] [Flat g]
    (g' : X' ⟶ X) (f' : X' ⟶ Y') (hsq : IsPullback g' f' f g)
    (hf : f ≫ sY = sX) (hg : g ≫ sY = sY') (hg' : g' ≫ sX = sX')
    (r : ℕ) (hgr : AlgebraicGeometry.RelativeDimension g r) :
    IsProper f' ∧ Flat g' ∧ LocallyOfFiniteType g' ∧
      @AlgebraicGeometry.RelativeDimension _ _ g'
        (MorphismProperty.of_isPullback hsq.flip inferInstance) r ∧
      ∀ (k : ℤ) (α : CycleGroup C sX k),
        letI : IsProper f' := MorphismProperty.of_isPullback hsq inferInstance
        letI : LocallyOfFiniteType g' := MorphismProperty.of_isPullback hsq.flip inferInstance
        letI : Flat g' := MorphismProperty.of_isPullback hsq.flip inferInstance
        flatPullback C sY' sY g hg r hgr k (properPushforward C sX sY f hf k α) =
          properPushforward C sX' sY' f'
            (comp_structureMorphism_of_isPullback sX sY sX' sY' f g g' f' hsq hf hg hg')
            (k + (r : ℤ))
            (flatPullback C sX' sX g' hg' r
              (AlgebraicGeometry.RelativeDimension.of_isPullback hsq.flip hgr) k α)
```

## Tag 02RH, a lemma

[Tag 02RH](https://stacks.math.columbia.edu/tag/02RH) in the Stacks Project.

**`Stacks.Chow.properPushforward_flatPullback_of_isFiniteLocallyFreeOfRank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFreeFibreDegree.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFreeFibreDegree.lean#L141). The attribute's comment: “push-pull formula”.

> **Stacks 02RH, the second assertion.** For `f : X ⟶ Y` finite locally free of degree `d` over
> the base,
>
>   `f_* f^* α = d α`   in `Z_k(Y)`.
>
> The statement transports the left hand side along the equality `k + 0 = k` of delta-dimensions,
> which is the degree that pullback and pushforward along `f` produce; that equality is taken as a
> hypothesis so that the statement typechecks, exactly as in
> `Stacks.Chow.properPushforward_flatPullback`.
>
> This is `Stacks.Chow.properPushforward_flatPullback` with its fibre-degree hypothesis discharged
> by `Stacks.Chow.fibreDegreeIsRank_of_isFiniteLocallyFreeOfRank`.

```lean
theorem properPushforward_flatPullback_of_isFiniteLocallyFreeOfRank (C : ChowSituation.{u})
    {X Y : Scheme.{u}} (sX : X ⟶ C.S) [LocallyOfFiniteType sX] (sY : Y ⟶ C.S)
    [LocallyOfFiniteType sY] (f : X ⟶ Y) (d : ℕ)
    [Stacks.Morphisms.IsFiniteLocallyFreeOfRank f d] (hbase : f ≫ sY = sX) (k : ℤ)
    (hcast : k + ((0 : ℕ) : ℤ) = k) (α : CycleGroup C sY k) :
    letI : LocallyOfFiniteType f :=
      Stacks.Morphisms.locallyOfFiniteType_of_isFiniteLocallyFreeOfRank f d
    letI : Flat f := Stacks.Morphisms.flat_of_isFiniteLocallyFreeOfRank f d
    letI : IsProper f := Stacks.Morphisms.isProper_of_isFiniteLocallyFreeOfRank f d
    (hcast ▸ properPushforward C sX sY f hbase (k + ((0 : ℕ) : ℤ))
          (flatPullback C sX sY f hbase 0
            (Stacks.Morphisms.relativeDimension_zero_of_isFiniteLocallyFreeOfRank f d) k α) :
        CycleGroup C sY k) = (d : ℤ) • α
```

Declarations registered for the tag:

- [`Stacks.Morphisms.isProper_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L84), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L126) (StacksFrontier): “properness”.
- [`Stacks.Morphisms.flat_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L127) (StacksFrontier): “flatness”.
- [`Stacks.Morphisms.relativeDimension_zero_of_isFiniteLocallyFreeOfRank`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeProper.lean#L98), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/FlatPullback/FiniteLocallyFree.lean#L128) (StacksFrontier): “relative dimension zero”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 42.15, Tag 02RF](https://stacks.math.columbia.edu/tag/02RF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
