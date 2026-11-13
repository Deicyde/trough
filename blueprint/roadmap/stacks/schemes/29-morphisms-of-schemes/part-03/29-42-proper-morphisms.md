---
declaration: section
origin: cited
lean: AlgebraicGeometry.IsProper, AlgebraicGeometry.universallyClosed_isZariskiLocalAtTarget, AlgebraicGeometry.isProper_iff_exists_iSup_eq_top, AlgebraicGeometry.IsProper.stableUnderComposition, AlgebraicGeometry.universallyClosed_isStableUnderComposition, Stacks.ProperAlgebraBaseChange.universallyClosed_of_isPullback, Stacks.ProperAlgebraBaseChange.isProper_of_isPullback, AlgebraicGeometry.IsProper.isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 29.42 Proper morphisms

Section 29.42 of the Stacks Project, [Tag 01W0](https://stacks.math.columbia.edu/tag/01W0). 10 tags here are carried by 15 declarations of the repository (all in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01W1, a definition

[Tag 01W1](https://stacks.math.columbia.edu/tag/01W1) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsProper`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 262](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L262) (StacksFrontier). References: EGA II (5.4.1); EGA II (7.4.7).

## Tag 02K7, a lemma

[Tag 02K7](https://stacks.math.columbia.edu/tag/02K7) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.universallyClosed_isZariskiLocalAtTarget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_isZariskiLocalAtTarget#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch29.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch29.lean#L171) (StacksFrontier): “being universally closed is local on the target”.

## Tag 01W2, a lemma

[Tag 01W2](https://stacks.math.columbia.edu/tag/01W2) in the Stacks Project.

**`AlgebraicGeometry.isProper_iff_exists_iSup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L65).

> **[Stacks, Tag 01W2].** A morphism of schemes `f : X ⟶ S` is proper if and only if there is
> an open covering `S = ⋃ V j` such that every restriction `f⁻¹(V j) ⟶ V j` is proper. The index
> type of the covering may live in any universe.

```lean
theorem isProper_iff_exists_iSup_eq_top {X S : Scheme.{u}} (f : X ⟶ S) :
    IsProper f ↔ ∃ (ι : Type*) (V : ι → S.Opens), iSup V = ⊤ ∧ ∀ j, IsProper (f ∣_ V j)
```

## Tag 01W3, a lemma

[Tag 01W3](https://stacks.math.columbia.edu/tag/01W3) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.IsProper.stableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.stableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L140) (StacksFrontier): “the composition of proper morphisms is proper”. References: EGA II (5.4.2).
- [`AlgebraicGeometry.universallyClosed_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L143) (StacksFrontier): “the composition of universally closed morphisms is universally closed”. References: EGA II (5.4.9), “5.4.2(ii)”; EGA IV (2.4.3), “(ii)”.

## Tag 01W4, a lemma

[Tag 01W4](https://stacks.math.columbia.edu/tag/01W4) in the Stacks Project.

**`Stacks.ProperAlgebraBaseChange.universallyClosed_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAlgebraBaseChange/Basic.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperAlgebraBaseChange/Basic.lean#L115). The attribute's comment: “the base change of a universally closed morphism is universally closed”.

> **Stacks Project, Tag 01W4, second statement.** The base change of a universally closed
> morphism is universally closed: in a cartesian square
>
> ```
> Y' --f'--> Y
> |          |
> g'         g
> v          v
> X ---f---> S
> ```
>
> if `g` is universally closed then so is `g'`.

```lean
theorem universallyClosed_of_isPullback {X Y Y' S : Scheme.{u}} {f : X ⟶ S} {g : Y ⟶ S}
    {f' : Y' ⟶ Y} {g' : Y' ⟶ X} (sq : IsPullback f' g' g f) (hg : UniversallyClosed g) :
    UniversallyClosed g'
```

**`Stacks.ProperAlgebraBaseChange.isProper_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperAlgebraBaseChange/Basic.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperAlgebraBaseChange/Basic.lean#L133). The attribute's comment: “the base change of a proper morphism is proper”.

> **Stacks Project, Tag 01W4, first statement.** The base change of a proper morphism is
> proper: in a cartesian square
>
> ```
> Y' --f'--> Y
> |          |
> g'         g
> v          v
> X ---f---> S
> ```
>
> if `g` is proper then so is `g'`.

```lean
theorem isProper_of_isPullback {X Y Y' S : Scheme.{u}} {f : X ⟶ S} {g : Y ⟶ S}
    {f' : Y' ⟶ Y} {g' : Y' ⟶ X} (sq : IsPullback f' g' g f) (hg : IsProper g) :
    IsProper g'
```

Declarations registered for the tag:

- [`AlgebraicGeometry.IsProper.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.IsProper.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SituationBaseChange.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SituationBaseChange.lean#L63) (StacksFrontier): “the proper case”. References: EGA II (5.4.2), “more general”; EGA III (4.3.4), “more general”; EGA IV (2.7.1), “implication”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.8), “partial”; SGA 3 VIB (10.1), “partial”; SGA 6 X (7.5), “partial”.
- [`AlgebraicGeometry.universallyClosed_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.universallyClosed_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SituationBaseChange.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Curves/VanishingResults/SituationBaseChange.lean#L65) (StacksFrontier): “the universally closed case”. References: EGA II (5.4.9), “5.4.2(iii)”; EGA IV (2.4.3), “(iii)”; EGA IV (2.6.4), “(ii)”; SGA 1 IX (2.4), “partial”; SGA 1 VIII (4.7), “necessity”; SGA 3 V (6.1), “partial”.

## Tag 01W5, a lemma

[Tag 01W5](https://stacks.math.columbia.edu/tag/01W5) in the Stacks Project.

**`AlgebraicGeometry.isProper_of_isClosedImmersion`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L57). The attribute's comment: “proper”. References: EGA II (5.4.2); EGA II (5.4.9), “5.4.2(i)”.

> A closed immersion of schemes is proper: it is a finite morphism, and a finite morphism is
> separated, universally closed and locally of finite type.

```lean
lemma isProper_of_isClosedImmersion {X Y : Scheme.{u}} (f : X ⟶ Y) [IsClosedImmersion f] :
    IsProper f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.instUniversallyClosedOfIsClosedImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.instUniversallyClosedOfIsClosedImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 147](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L147) (StacksFrontier): “a closed immersion is universally closed”. References: EGA II (5.4.9), “5.4.2(i)”; EGA II (6.1.10), “closed immersions”; EGA IV (2.4.3).

## Tag 01W6, a lemma

[Tag 01W6](https://stacks.math.columbia.edu/tag/01W6) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_of_universallyClosed_of_isSeparated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L80). The attribute's comment: “(1), in the triangle form of the source”.

> **[Stacks, Tag 01W6] part (1).** Let `X ⟶ Y ⟶ S` be a commutative triangle with `Y`
> separated over `S`. If `X ⟶ S` is universally closed, then so is `X ⟶ Y`.

```lean
lemma universallyClosed_of_universallyClosed_of_isSeparated (h : g ≫ q = p) [IsSeparated q]
    [UniversallyClosed p] : UniversallyClosed g
```

**`AlgebraicGeometry.isProper_of_isProper_of_isSeparated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L88). The attribute's comment: “(2), in the triangle form of the source”.

> **[Stacks, Tag 01W6] part (2).** Let `X ⟶ Y ⟶ S` be a commutative triangle with `Y`
> separated over `S`. If `X` is proper over `S`, then `X ⟶ Y` is proper.

```lean
lemma isProper_of_isProper_of_isSeparated (h : g ≫ q = p) [IsSeparated q] [IsProper p] :
    IsProper g
```

**`AlgebraicGeometry.isClosed_range_of_universallyClosed_of_isSeparated`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L98). The attribute's comment: “the final clause: the image of X in Y is closed”.

> **The final clause of [Stacks, Tag 01W6].** In a commutative triangle `X ⟶ Y ⟶ S` with `Y`
> separated over `S` and `X` universally closed over `S`, the image of `X` in `Y` is closed: the
> morphism `X ⟶ Y` is universally closed, hence a closed map, and its image is the image of the
> whole space.

```lean
lemma isClosed_range_of_universallyClosed_of_isSeparated (h : g ≫ q = p) [IsSeparated q]
    [UniversallyClosed p] : IsClosed (Set.range g.base)
```

## Tag 03GN, a lemma

[Tag 03GN](https://stacks.math.columbia.edu/tag/03GN) in the Stacks Project.

**`AlgebraicGeometry.universallyClosed_of_universallyClosed_of_surjective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/Basic.lean#L117). The attribute's comment: “the universally closed half, in the triangle form of the source”.

> **[Stacks, Tag 03GN], the universally closed half.** Let `X ⟶ Y ⟶ S` be a commutative
> triangle with `X ⟶ Y` surjective. If `X ⟶ S` is universally closed, then so is `Y ⟶ S`: a map is
> closed as soon as its precomposition with a continuous surjection is, and surjectivity is stable
> under base change.

```lean
lemma universallyClosed_of_universallyClosed_of_surjective (h : g ≫ q = p) [Surjective g]
    [UniversallyClosed p] : UniversallyClosed q
```

**`AlgebraicGeometry.isProper_of_comp_surjective`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProperLimitStage/Basic.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperLimitStage/Basic.lean#L91). The attribute's comment: “the properness conclusion: Y is proper over S when also separated and locally of finite type”.

> **[Stacks, Tag 03GN], the properness conclusion.** Let `f : X ⟶ Y` be a morphism of schemes
> over `S`, with structure morphism `g : Y ⟶ S`. If `f` is surjective, `X` is universally closed
> over `S` and `Y` is separated and locally of finite type over `S`, then `Y` is proper over `S`.
>
> The universal closedness of `g` is the first conclusion of Stacks 03GN, which is Mathlib's
> `AlgebraicGeometry.UniversallyClosed.of_comp_surjective`, tagged just below; quasi-compactness of
> `g` is part of universal closedness, so `IsProper g` follows from the structure constructor.

```lean
lemma isProper_of_comp_surjective {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [UniversallyClosed (f ≫ g)] [Surjective f] [IsSeparated g] [LocallyOfFiniteType g] :
    IsProper g
```

Declarations registered for the tag:

- [`AlgebraicGeometry.UniversallyClosed.of_comp_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.UniversallyClosed.of_comp_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ProperLimitStage/Basic.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ProperLimitStage/Basic.lean#L97) (StacksFrontier): “the universal closedness conclusion”. References: EGA II (5.4.9), “more general”; EGA IV (2.4.3), “(v), universally closed”; SGA 3 V (7.4), “partial”.

## Tag 0AH6, a lemma

[Tag 0AH6](https://stacks.math.columbia.edu/tag/0AH6) in the Stacks Project.

**`AlgebraicGeometry.isProper_imageι_comp`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SchemeTheoreticImage.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SchemeTheoreticImage.lean#L43). The attribute's comment: “properness of the scheme-theoretic image”. References: EGA II (5.4.9), “5.4.3(ii), special case”.

> **Stacks 0AH6, properness.** The scheme-theoretic image in a separated scheme locally of
> finite type over the base of a universally closed morphism to the base is proper over the
> base.

```lean
lemma isProper_imageι_comp {X Y S : Scheme.{u}} (h : X ⟶ Y) (g : Y ⟶ S)
    [UniversallyClosed (h ≫ g)] [IsSeparated g] [LocallyOfFiniteType g] :
    IsProper (h.imageι ≫ g)
```

**`AlgebraicGeometry.surjective_toImage`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SchemeTheoreticImage.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SchemeTheoreticImage.lean#L55). The attribute's comment: “surjectivity onto the scheme-theoretic image”.

> **Stacks 0AH6, surjectivity.** Under the separatedness hypothesis, the canonical morphism
> to the scheme-theoretic image of a universally closed composite is surjective.

```lean
lemma surjective_toImage {X Y S : Scheme.{u}} (h : X ⟶ Y) (g : Y ⟶ S)
    [UniversallyClosed (h ≫ g)] [IsSeparated g] : Surjective h.toImage
```

## Tag 09MQ, a lemma

[Tag 09MQ](https://stacks.math.columbia.edu/tag/09MQ) in the Stacks Project.

**`AlgebraicGeometry.quasiSeparated_of_surjective_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/QuasiSeparated.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/QuasiSeparated.lean#L46). The attribute's comment: “quasi\_separated\_over\_s”.

> **Stacks Project, Tag 09MQ (quasi-separated over the base).**
> Quasi-separatedness over a base descends along a surjective universally
> closed morphism of schemes.

```lean
theorem quasiSeparated_of_surjective_universallyClosed {S : Scheme.{u}} {X Y : Over S}
    (f : X ⟶ Y) [Surjective f.left] [UniversallyClosed f.left] [QuasiSeparated X.hom] :
    QuasiSeparated Y.hom
```

**`AlgebraicGeometry.quasiSeparatedSpace_of_surjective_universallyClosed`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/QuasiSeparated.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/QuasiSeparated.lean#L80). The attribute's comment: “quasi\_separated\_scheme”.

> **Stacks Project, Tag 09MQ (scheme part).** The target of a surjective
> universally closed morphism from a quasi-separated scheme is
> quasi-separated.

```lean
lemma quasiSeparatedSpace_of_surjective_universallyClosed
    {X Y : Scheme.{u}} (f : X ⟶ Y) [Surjective f] [UniversallyClosed f]
    [QuasiSeparatedSpace X] : QuasiSeparatedSpace Y
```

**`AlgebraicGeometry.isSeparated_of_surjective_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SeparatedDescent.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SeparatedDescent.lean#L81). The attribute's comment: “separated\_over\_s”. References: SGA 3 V (7.4).

> **Stacks Project, Tag 09MQ (separated over the base).** Separatedness over a base descends
> along a surjective universally closed morphism of schemes.

```lean
theorem isSeparated_of_surjective_universallyClosed {S : Scheme.{u}} {X Y : Over S}
    (f : X ⟶ Y) [Surjective f.left] [UniversallyClosed f.left] [IsSeparated X.hom] :
    IsSeparated Y.hom
```

**`AlgebraicGeometry.Scheme.isSeparated_of_surjective_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SeparatedDescent.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Proper/SeparatedDescent.lean#L101). The attribute's comment: “separated\_scheme”. References: SGA 3 V (7.4), “special case”.

> **Stacks Project, Tag 09MQ (separated scheme).** A scheme receiving a surjective
> universally closed morphism from a separated scheme is itself separated.
>
> This is the absolute form of `AlgebraicGeometry.isSeparated_of_surjective_universallyClosed`,
> obtained by taking the base to be the terminal scheme.

```lean
theorem Scheme.isSeparated_of_surjective_universallyClosed {X Y : Scheme.{u}} (f : X ⟶ Y)
    [Surjective f] [UniversallyClosed f] [X.IsSeparated] : Y.IsSeparated
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.42, Tag 01W0](https://stacks.math.columbia.edu/tag/01W0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
