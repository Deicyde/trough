---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.eq_of_isReducedStack_of_range_pointsMap_eq, AlgebraicGeometry.Stack.existsUnique_reducedClosedSubstack, AlgebraicGeometry.Stack.eq_top_of_isClosedSubstack_of_isReducedStack, AlgebraicGeometry.Stack.factorsThroughSubstack_iff_range_pointsMap_subset, AlgebraicGeometry.Stack.IsAlgebraicStackStructure, AlgebraicGeometry.Stack.IsReducedInducedStackStructure, AlgebraicGeometry.Stack.IsReducedInducedStackStructure.unique, AlgebraicGeometry.Stack.IsReduction
statement: formalized
proof: formalized
---

# 100.10 Reduced algebraic stacks

Section 100.10 of the Stacks Project, [Tag 0508](https://stacks.math.columbia.edu/tag/0508). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0509, a lemma

[Tag 0509](https://stacks.math.columbia.edu/tag/0509) in the Stacks Project.

**`AlgebraicGeometry.Stack.eq_of_isReducedStack_of_range_pointsMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedClosedSubstack.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedClosedSubstack.lean#L91). The attribute's comment: “uniqueness”.

> **The uniqueness assertion of Stacks 0509.** Two reduced closed substacks
> of an algebraic stack `𝒳` over `S`
> with the same set of points are equal: each is contained in the other by
> `AlgebraicGeometry.Stack.le_of_isReducedStack_of_range_pointsMap_subset`.

```lean
theorem eq_of_isReducedStack_of_range_pointsMap_eq {𝒳 : AlgebraicStacks.{u, w} B S hS}
    {P Q : ObjectProperty 𝒳.val.val.obj}
    (hP : IsClosedSubstack 𝒳 P) (hQ : IsClosedSubstack 𝒳 Q)
    (hAP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (hAQ : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 Q))
    (hPred : IsReducedStack B S hS (fullSubcategoryAlgebraicStack 𝒳 P hAP))
    (hQred : IsReducedStack B S hS (fullSubcategoryAlgebraicStack 𝒳 Q hAQ))
    (hpoints :
      Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 P hAP)) =
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 Q hAQ))) :
    P = Q
```

**`AlgebraicGeometry.Stack.existsUnique_reducedClosedSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedClosedSubstackExistence.lean, line 520](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedClosedSubstackExistence.lean#L520).

> Let `𝒳` be an algebraic stack over `S` and let `T` be a closed subset of its space of points
> `|𝒳|`. There exists a unique closed substack `𝒵 ⊆ 𝒳` such that (a) `|𝒵| = T` and (b) `𝒵` is
> reduced.
>
> A closed substack is a property of the objects of `𝒳` cutting out a strictly full subcategory
> which is an algebraic stack with closed immersion inclusion
> (`AlgebraicGeometry.Stack.IsClosedSubstack`); its set of points is the image of the map on points
> of its inclusion. Both clauses are stated for every proof that the full subcategory is an
> algebraic stack.

```lean
theorem existsUnique_reducedClosedSubstack :
    ∃! P : ObjectProperty 𝒳.val.val.obj, IsClosedSubstack 𝒳 P ∧
      (∀ hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P),
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 P hP)) = T) ∧
      ∀ hP : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P),
        IsReducedStack B S hS (fullSubcategoryAlgebraicStack 𝒳 P hP)
```

## Tag 050A, a lemma

[Tag 050A](https://stacks.math.columbia.edu/tag/050A) in the Stacks Project.

**`AlgebraicGeometry.Stack.eq_top_of_isClosedSubstack_of_isReducedStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedStackClosedSubstack.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedStackClosedSubstack.lean#L223).

> **Stacks 050A.** Let `𝒳` be an algebraic stack over `S` and let `P` cut out a closed substack
> of `𝒳`. If `𝒳` is reduced and the inclusion of the substack is surjective on points, then the
> substack is the whole of `𝒳`.
>
> Every scheme chart of a reduced algebraic stack is reduced, and the chart supplied by the
> algebraic-stack condition is locally essentially surjective; so
> `AlgebraicGeometry.Stack.prop_of_isReduced_fiber` puts the image of the tautological object of
> that chart in the substack, `AlgebraicGeometry.Stack.prop_of_isHomLift` puts the image of every
> object of the chart there, and membership of a substack being local on the big fppf site puts
> every object of `𝒳` there.

```lean
theorem eq_top_of_isClosedSubstack_of_isReducedStack {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (P : ObjectProperty 𝒳.val.val.obj) (hclosed : IsClosedSubstack 𝒳 P)
    (hpoints : IsSurjective B S hS (fullSubcategoryInclusion 𝒳 P hclosed.2.choose))
    (hred : IsReducedStack B S hS 𝒳) :
    P = ⊤
```

## Tag 050B, a lemma

[Tag 050B](https://stacks.math.columbia.edu/tag/050B) in the Stacks Project.

**`AlgebraicGeometry.Stack.factorsThroughSubstack_iff_range_pointsMap_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedStackFactorization.lean, line 73](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedStackFactorization.lean#L73).

> Let `𝒳` and `𝒴` be algebraic stacks over `S`, let `P` cut out a closed
> substack of `𝒳` and let `𝒴` be reduced. A 1-morphism `f : 𝒴 ⟶ 𝒳` factors through the substack
> if and only if the image of the induced map on points is contained in the points of the
> substack.

```lean
theorem factorsThroughSubstack_iff_range_pointsMap_subset
    {𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS} (f : 𝒴 ⟶ 𝒳)
    {P : ObjectProperty 𝒳.val.val.obj} (hP : IsClosedSubstack 𝒳 P)
    (hA : IsAlgebraicStack.{u, w} B S hS (fullSubcategoryBased 𝒳 P))
    (hred : IsReducedStack B S hS 𝒴) :
    FactorsThroughSubstack f P ↔
      Set.range (AlgebraicStacks.pointsMap B S hS f) ⊆
        Set.range (AlgebraicStacks.pointsMap B S hS (fullSubcategoryInclusion 𝒳 P hA))
```

## Tag 050C, a definition

[Tag 050C](https://stacks.math.columbia.edu/tag/050C) in the Stacks Project.

**`AlgebraicGeometry.Stack.IsAlgebraicStackStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean, line 94](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean#L94). The attribute's comment: “algebraic stack structure on a closed set of points”.

> **Stacks 050C, an algebraic stack structure on a closed set of points.** Let `𝒳` be an
> algebraic stack over `S` and let `Z` be a set of points of `𝒳`. An *algebraic stack structure* on
> `Z` is a closed substack of `𝒳` whose set of points is `Z`, that is, a property `P` of the
> objects of `𝒳` cutting out a closed substack the canonical inclusion of which has range `Z` on
> points.

```lean
def IsAlgebraicStackStructure {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (Z : Set (AlgebraicStacks.points B S hS 𝒳)) (P : ObjectProperty 𝒳.val.val.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsReducedInducedStackStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean#L131). The attribute's comment: “the reduced induced algebraic stack structure”.

> **Stacks 050C, the reduced induced algebraic stack structure.** The *reduced induced
> algebraic stack structure* on a set `Z` of points of `𝒳` is the algebraic stack structure on `Z`
> which is reduced. There is at most one,
> `AlgebraicGeometry.Stack.IsReducedInducedStackStructure.unique`, which is the content of the
> uniqueness half of **Stacks 0509**.

```lean
def IsReducedInducedStackStructure {𝒳 : AlgebraicStacks.{u, w} B S hS}
    (Z : Set (AlgebraicStacks.points B S hS 𝒳)) (P : ObjectProperty 𝒳.val.val.obj) : Prop
```

**`AlgebraicGeometry.Stack.IsReducedInducedStackStructure.unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean#L159). The attribute's comment: “uniqueness of the reduced induced structure”.

> **Stacks 050C, uniqueness of the reduced induced structure.** Two reduced induced algebraic
> stack structures on the same set of points are equal. This is the uniqueness half of
> **Stacks 0509**, and it is what makes the definite article of the source legitimate.

```lean
theorem IsReducedInducedStackStructure.unique {𝒳 : AlgebraicStacks.{u, w} B S hS}
    {Z : Set (AlgebraicStacks.points B S hS 𝒳)} {P Q : ObjectProperty 𝒳.val.val.obj}
    (hP : IsReducedInducedStackStructure B S hS Z P)
    (hQ : IsReducedInducedStackStructure B S hS Z Q) :
    P = Q
```

**`AlgebraicGeometry.Stack.IsReduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Reduction.lean#L171). The attribute's comment: “the reduction”.

> **Stacks 050C, the reduction.** The *reduction* `𝒳_red` of an algebraic stack `𝒳` over `S` is
> the reduced induced algebraic stack structure on the whole of its space of points. It is unique,
> `AlgebraicGeometry.Stack.IsReduction.unique`.

```lean
def IsReduction {𝒳 : AlgebraicStacks.{u, w} B S hS} (P : ObjectProperty 𝒳.val.val.obj) : Prop
```

## Tag 06FK, a remark

[Tag 06FK](https://stacks.math.columbia.edu/tag/06FK) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_reducedInducedSubstack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ReducedInducedSubstackLocallyClosed.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/ReducedInducedSubstackLocallyClosed.lean#L123). The attribute's comment: “a locally closed T in |X|: the open substack U with |U| = |X| minus the boundary of T, the reduced induced closed substack Z of U on the points of T (Stacks 050C), the immersion Z -> U -> X, Z reduced, and |Z| = T in |X|”.

> **The reduced induced substack structure on a locally closed set of points.**
> Let `𝒳` be an algebraic stack over `S` and let `T` be a locally closed subset of its space of
> points, with boundary `∂T = T̄ \ T`. Then there are
>
> * an open substack `𝒰` of `𝒳` with `|𝒰| = |𝒳| \ ∂T` (Mathlib's `coborder T`), and
> * a reduced induced algebraic stack structure `𝒵` (**Stacks 050C**) on the part of `T` inside
>   `|𝒰|`, that is, a reduced closed substack of `𝒰` with that set of points,
>
> such that the composite `𝒵 ⟶ 𝒰 ⟶ 𝒳` of the two inclusions is an immersion, `𝒵` is reduced, and
> the image of `|𝒵|` in `|𝒳|` is exactly `T`.

```lean
theorem exists_reducedInducedSubstack
    (T : Set (AlgebraicStacks.points B S hS 𝒳))
    (hT : @IsLocallyClosed _ (pointTopology B S hS 𝒳.val) T) :
    ∃ (𝒰 : OpenSubstack 𝒳)
      (P : ObjectProperty
        (fullSubcategoryAlgebraicStack 𝒳 𝒰.property 𝒰.isAlgebraic).val.val.obj)
      (hP : IsAlgebraicStack.{u, w} B S hS
        (fullSubcategoryBased (fullSubcategoryAlgebraicStack 𝒳 𝒰.property 𝒰.isAlgebraic) P)),
      𝒰.pointSet B S hS = @coborder _ (pointTopology B S hS 𝒳.val) T ∧
      IsReducedInducedStackStructure B S hS
        (AlgebraicStacks.pointsMap B S hS 𝒰.inclusion ⁻¹' T) P ∧
      AlgebraicStacks.IsImmersion B S hS
        (fullSubcategoryInclusion (fullSubcategoryAlgebraicStack 𝒳 𝒰.property 𝒰.isAlgebraic)
          P hP ≫ 𝒰.inclusion) ∧
      IsReducedStack B S hS
        (fullSubcategoryAlgebraicStack (fullSubcategoryAlgebraicStack 𝒳 𝒰.property 𝒰.isAlgebraic)
          P hP) ∧
      Set.range (AlgebraicStacks.pointsMap B S hS
        (fullSubcategoryInclusion (fullSubcategoryAlgebraicStack 𝒳 𝒰.property 𝒰.isAlgebraic)
          P hP ≫ 𝒰.inclusion)) = T
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.10, Tag 0508](https://stacks.math.columbia.edu/tag/0508)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
