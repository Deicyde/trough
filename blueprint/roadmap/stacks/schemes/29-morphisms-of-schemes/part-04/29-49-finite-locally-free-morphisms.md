---
declaration: section
origin: cited
lean: Stacks.Morphisms.IsFiniteLocallyFree, Stacks.Morphisms.IsFiniteLocallyFreeOfRank, Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_locallyOfFinitePresentation, Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian, Stacks.Morphisms.isFiniteLocallyFree_comp, Stacks.Morphisms.isFiniteLocallyFree_isStableUnderBaseChange, Stacks.Morphisms.exists_isClosed_isFiniteLocallyFreeOfRank_decomposition, Stacks.Morphisms.exists_finiteLocallyFree_cover_closedImmersion
statement: formalized
proof: formalized
---

# 29.49 Finite locally free morphisms

Section 29.49 of the Stacks Project, [Tag 02K9](https://stacks.math.columbia.edu/tag/02K9). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02KA, a definition

[Tag 02KA](https://stacks.math.columbia.edu/tag/02KA) in the Stacks Project.

**`Stacks.Morphisms.IsFiniteLocallyFree`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeOfRank.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeOfRank.lean#L61). The attribute's comment: “finite locally free”. References: SGA 1 I (4.10), “more general”.

> **Stacks Project, Tag 02KA.** A morphism of schemes is finite locally free if it is affine
> and the direct image of its structure sheaf is a finite locally free module.

```lean
class IsFiniteLocallyFree {X S : Scheme.{u}} (f : X ⟶ S) : Prop
    extends IsAffineHom f,
      SheafOfModules.IsFiniteLocallyFree.{u, u, u} (pushforwardStructureSheaf.{u} f)
```

**`Stacks.Morphisms.IsFiniteLocallyFreeOfRank`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeOfRank.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFreeOfRank.lean#L68). The attribute's comment: “rank or degree”.

> **Stacks Project, Tag 02KA.** A finite locally free morphism has rank (or degree) `r` if
> the direct image of its structure sheaf is finite locally free of rank `r`.

```lean
class IsFiniteLocallyFreeOfRank {X S : Scheme.{u}} (f : X ⟶ S) (r : ℕ) : Prop
    extends IsAffineHom f,
      SheafOfModules.IsFiniteLocallyFreeOfRank.{u, u, u} (pushforwardStructureSheaf.{u} f) r
```

## Tag 02KB, a lemma

[Tag 02KB](https://stacks.math.columbia.edu/tag/02KB) in the Stacks Project.

**`Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FiniteFlat.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FiniteFlat.lean#L68). The attribute's comment: “conditions (1) and (2)”.

> **Stacks Project, Tag 02KB.** A morphism of schemes is finite locally free if and only if it
> is finite, flat, and locally of finite presentation.

```lean
theorem isFiniteLocallyFree_iff_isFinite_flat_locallyOfFinitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S) :
    IsFiniteLocallyFree f ↔
      IsFinite f ∧ Flat f ∧ LocallyOfFinitePresentation f
```

**`Stacks.Morphisms.isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FiniteFlat.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/FiniteFlat.lean#L96). The attribute's comment: “condition (3) over a locally Noetherian base”.

> **Stacks Project, Tag 02KB.** Over a locally Noetherian base, a morphism of schemes is finite
> locally free if and only if it is finite and flat.

```lean
theorem isFiniteLocallyFree_iff_isFinite_flat_of_isLocallyNoetherian
    {X S : Scheme.{u}} (f : X ⟶ S) [IsLocallyNoetherian S] :
    IsFiniteLocallyFree f ↔ IsFinite f ∧ Flat f
```

## Tag 02KC, a lemma

[Tag 02KC](https://stacks.math.columbia.edu/tag/02KC) in the Stacks Project.

**`Stacks.Morphisms.isFiniteLocallyFree_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Comp.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/Comp.lean#L38).

> **Stacks Project, Tag 02KC.** A composition of finite locally free morphisms is finite
> locally free.

```lean
theorem isFiniteLocallyFree_comp {X Y Z : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ Z)
    [IsFiniteLocallyFree f] [IsFiniteLocallyFree g] :
    IsFiniteLocallyFree (f ≫ g)
```

## Tag 02KD, a lemma

[Tag 02KD](https://stacks.math.columbia.edu/tag/02KD) in the Stacks Project.

**`Stacks.Morphisms.isFiniteLocallyFree_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/BaseChange.lean, line 40](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/BaseChange.lean#L40).

> **Stacks Project, Tag 02KD.** A base change of a finite locally free morphism is finite
> locally free.

```lean
instance isFiniteLocallyFree_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (@IsFiniteLocallyFree : MorphismProperty Scheme.{u})
```

## Tag 04MH, a lemma

[Tag 04MH](https://stacks.math.columbia.edu/tag/04MH) in the Stacks Project.

**`Stacks.Morphisms.exists_isClosed_isFiniteLocallyFreeOfRank_decomposition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/DegreeDecomposition.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FiniteLocallyFree/DegreeDecomposition.lean#L93).

> The base of a finite locally free morphism decomposes as a disjoint union of open and closed
> subschemes indexed by the degree, over the `d`-th of which the morphism is finite locally free of
> degree `d`.

```lean
theorem exists_isClosed_isFiniteLocallyFreeOfRank_decomposition {X S : Scheme.{u}} (f : X ⟶ S)
    [IsFiniteLocallyFree f] :
    ∃ Z : ℕ → S.Opens, (∀ d, IsClosed (Z d : Set S)) ∧
      (∀ d e, d ≠ e → Disjoint (Z d) (Z e)) ∧ (⨆ d : ℕ, Z d) = ⊤ ∧
      ∀ d, IsFiniteLocallyFreeOfRank (f ∣_ Z d) d
```

## Tag 03HW, a lemma

[Tag 03HW](https://stacks.math.columbia.edu/tag/03HW) in the Stacks Project.

**`Stacks.Morphisms.exists_finiteLocallyFree_cover_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/FiniteCover.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/FiniteCover.lean#L214).

> **Stacks Project, Tag 03HW.** After a surjective finite locally free base change,
> a finite morphism to an affine scheme embeds into a finite locally free scheme covered
> set-theoretically by finitely many closed sections.

```lean
theorem exists_finiteLocallyFree_cover_closedImmersion
    {Y X : Scheme.{u}} (f : Y ⟶ X) [IsFinite f] [IsAffine X] :
    ∃ (X' : Scheme.{u}) (g : X' ⟶ X),
      Surjective g ∧ IsFiniteLocallyFree g ∧
      Surjective (pullback.fst f g) ∧
      IsFiniteLocallyFree (pullback.fst f g) ∧
      ∃ (Z' : Scheme.{u}) (p : Z' ⟶ X')
        (i : pullback f g ⟶ Z'),
        IsClosedImmersion i ∧
        i ≫ p = pullback.snd f g ∧
        IsFiniteLocallyFree p ∧
        ∃ (m : ℕ) (s : Fin m → (X' ⟶ Z')),
          (∀ j, IsClosedImmersion (s j) ∧ s j ≫ p = 𝟙 X') ∧
          (∀ z : Z', ∃ j : Fin m, ∃ x : X', (s j).base x = z)
```

## Tag 03HX, a lemma

[Tag 03HX](https://stacks.math.columbia.edu/tag/03HX) in the Stacks Project.

**`Stacks.Morphisms.isNowhereDense_image_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/NowhereDense.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/NowhereDense.lean#L186). The attribute's comment: “nowhere denseness of the image”.

> **Stacks Project, Tag 03HX.** The image of a closed nowhere dense subset under a finite
> morphism of schemes is nowhere dense.

```lean
theorem isNowhereDense_image_of_isFinite {Y X : Scheme.{u}} (f : Y ⟶ X) [IsFinite f]
    {T : Set Y} (hT_closed : IsClosed T) (hT : IsNowhereDense T) :
    IsNowhereDense (f.base '' T)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.isClosedMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.Hom.isClosedMap#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/NowhereDense.lean, line 218](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/FiniteLocallyFree/NowhereDense.lean#L218) (StacksFrontier): “closedness of the image”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.49, Tag 02K9](https://stacks.math.columbia.edu/tag/02K9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
