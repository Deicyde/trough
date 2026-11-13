---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsIntegralModification, AlgebraicGeometry.Space.IsIntegralModification.exists_isIso_fromPreimage, AlgebraicGeometry.Space.IsAlteration, AlgebraicGeometry.Space.isAlteration_iff_isQuasiFiniteAt, AlgebraicGeometry.Space.exists_isClosedSubspace_isAlteration
statement: formalized
proof: formalized
---

# 72.8 Modifications and alterations

Section 72.8 of the Stacks Project, [Tag 0AD7](https://stacks.math.columbia.edu/tag/0AD7). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AD8, a definition

[Tag 0AD8](https://stacks.math.columbia.edu/tag/0AD8) in the Stacks Project.

**`AlgebraicGeometry.Space.IsIntegralModification`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralModification.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralModification.lean#L85).

> **Stacks 0AD8.** A *modification* of an integral algebraic space `X` over `S` is a
> birational proper morphism `f : X' ⟶ X` of algebraic spaces over `S` with `X'` integral.
>
> No decency hypotheses are needed: an integral algebraic space is decent, so the decency of the
> target is `hXint.isDecentSpace` and that of the source comes with its integrality.

```lean
def IsIntegralModification {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (hXint : IsIntegralSpace B S hS X) (f : X' ⟶ X) : Prop
```

## Tag 0AD9, a lemma

[Tag 0AD9](https://stacks.math.columbia.edu/tag/0AD9) in the Stacks Project.

**`AlgebraicGeometry.Space.IsIntegralModification.exists_isIso_fromPreimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralModification.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralModification.lean#L132).

> **Stacks 0AD9.** A modification of an integral algebraic space over `S` is an isomorphism
> over a nonempty open subspace of its target.

```lean
theorem IsIntegralModification.exists_isIso_fromPreimage
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {hX' : IsAlgebraicSpace B S hS X'} {hX : IsAlgebraicSpace B S hS X}
    {hXint : IsIntegralSpace B S hS X} {f : X' ⟶ X}
    (hf : IsIntegralModification B S hS hX' hX hXint f) :
    ∃ U : Subfunctor X, IsOpenSubspace B S hS U ∧
      Nonempty (points B S hS U.toFunctor) ∧ IsIso (U.fromPreimage f)
```

## Tag 0ADA, a definition

[Tag 0ADA](https://stacks.math.columbia.edu/tag/0ADA) in the Stacks Project.

**`AlgebraicGeometry.Space.IsAlteration`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralAlteration.lean, line 84](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralAlteration.lean#L84).

> **Stacks 0ADA.** An *alteration* of an integral algebraic space `X` over `S` is a proper
> dominant morphism `f : Y ⟶ X` of algebraic spaces over `S` with `Y` integral such that the
> inverse image of some nonempty open subspace `U ⊆ X` is finite over `U`.

```lean
abbrev IsAlteration (f : Y ⟶ X) : Prop
```

## Tag 0ADB, a lemma

[Tag 0ADB](https://stacks.math.columbia.edu/tag/0ADB) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlteration_iff_isQuasiFiniteAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralAlteration.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralAlteration.lean#L126). The attribute's comment: “against condition (4) of Stacks 0AD5”.

> **Stacks 0ADB.** A proper dominant morphism `f : Y ⟶ X` of integral algebraic spaces over
> `S` is an alteration exactly when it is quasi-finite at the generic point of `|Y|`, which is
> condition (4) of Stacks 0AD5 and hence equivalent to the other conditions compared there.

```lean
theorem isAlteration_iff_isQuasiFiniteAt (hY : IsAlgebraicSpace B S hS Y)
    (hX : IsAlgebraicSpace B S hS X) (hYint : IsIntegralSpace B S hS Y)
    (hXint : IsIntegralSpace B S hS X) (f : Y ⟶ X) (hp : IsProper B S hS f)
    (hdom : IsDominant B S hS f)
    {y : points B S hS Y} (hy : IsGenericPoint y (Set.univ : Set (points B S hS Y)))
    {x : points B S hS X} (hx : IsGenericPoint x (Set.univ : Set (points B S hS X))) :
    IsAlteration B S hS f ↔ IsQuasiFiniteAt B S hS f y
```

## Tag 0DMN, a lemma

[Tag 0DMN](https://stacks.math.columbia.edu/tag/0DMN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isClosedSubspace_isAlteration`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/AlterationInProperSurjection.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/AlterationInProperSurjection.lean#L164).

> Let `f : X ⟶ Y` be a proper surjective morphism of algebraic spaces over a scheme `S` with
> `Y` integral. Then `f` restricts to an alteration on some integral closed subspace of `X`.

```lean
theorem exists_isClosedSubspace_isAlteration (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hYint : IsIntegralSpace B S hS Y) (f : X ⟶ Y)
    (hp : IsProper B S hS f) (hsurj : IsSurjective B S hS f) :
    ∃ Z : Subfunctor X, IsClosedSubspace B S hS Z ∧
      IsIntegralSpace B S hS Z.toFunctor ∧ IsAlteration B S hS (Z.ι ≫ f)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.8, Tag 0AD7](https://stacks.math.columbia.edu/tag/0AD7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
