---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.QuasiCoherentDescent.faithful_canonicalDescentFunctor_of_isFpqcCovering, AlgebraicGeometry.Space.QuasiCoherentDescent.isEquivalence_canonicalDescentFunctor'_of_isFpqcCovering
statement: formalized
proof: formalized
---

# 74.4 Fpqc descent of quasi-coherent sheaves

Section 74.4 of the Stacks Project, [Tag 04W7](https://stacks.math.columbia.edu/tag/04W7). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04W8, a proposition

[Tag 04W8](https://stacks.math.columbia.edu/tag/04W8) in the Stacks Project.

**`AlgebraicGeometry.Space.QuasiCoherentDescent.faithful_canonicalDescentFunctor_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FpqcChartLocalization.lean, line 537](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FpqcChartLocalization.lean#L537). The attribute's comment: “the faithfulness half of the full-faithfulness clause, for an fpqc covering of algebraic spaces: the members of an fpqc covering are flat and the covering is jointly surjective on points, so a morphism of quasi-coherent modules is determined by its inverse images along it and the canonical descent functor of Stacks 04W5 is faithful. The fullness half of that clause and the effectivity clause are separate assertions of the tag and are not proved here”.

> **The faithfulness half of the full-faithfulness clause of Stacks 04W8.**  The canonical
> descent functor of Stacks 04W5, from the quasi-coherent `𝒪_X`-modules of Stacks 03G9 to the
> descent data of Stacks 04W3 relative to an fpqc covering `(f i : X i ⟶ X)` of algebraic spaces
> in the sense of Stacks 03MQ, is faithful.
>
> The covering is the only input.  Its members are flat and it is jointly surjective on points, so
> `AlgebraicGeometry.Space.QuasiCoherentDescent.reprFpqcHomInjective` supplies the represented case
> of the reduction above.  The two data needed to form the functor are supplied, not assumed: the
> associativity coherence of the comparison of inverse images of Stacks 03LU is
> `AlgebraicGeometry.Space.modulePullbackCompIsoAssoc`, and quasi-coherence of the inverse images
> is Stacks 03GA for an arbitrary morphism of algebraic spaces.
>
> This is the faithfulness half only.  The fullness half of the full-faithfulness clause, and the
> effectivity clause of the same tag, are not proved here.

```lean
theorem faithful_canonicalDescentFunctor_of_isFpqcCovering
    (hf : IsFpqcCovering B S hS fun i => (f i).hom) :
    (canonicalDescentFunctor' B S hS Xi f).Faithful
```

**`AlgebraicGeometry.Space.QuasiCoherentDescent.isEquivalence_canonicalDescentFunctor'_of_isFpqcCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FpqcDescentTransitivity.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Descent/QuasiCoherent/FpqcDescentTransitivity.lean#L613).

> **Stacks 04W8: for an fpqc covering `(f i : X i ⟶ X)` of algebraic spaces, the canonical
> descent functor from the quasi-coherent `𝒪_X`-modules to the descent data relative to the
> covering is an equivalence.**
>
> This is the tag, both of whose clauses the equivalence carries: *the functor is fully faithful*,
> and *every descent datum on quasi-coherent sheaves for the family is effective* — which is
> essential surjectivity by
> `…essSurj_canonicalDescentFunctor'_iff_forall_isEffective`.  The full-faithfulness clause is
> `…nonempty_fullyFaithful_canonicalDescentFunctor_of_isFpqcCovering` and the effectivity clause is
> `…forall_isEffective_of_isFpqcCovering`; both are proved, and nothing is assumed beyond the
> covering.

```lean
theorem isEquivalence_canonicalDescentFunctor'_of_isFpqcCovering
    (Xi : I → AlgebraicSpaces B S hS) (f : ∀ i, Xi i ⟶ X)
    (hf : IsFpqcCovering B S hS fun i => (f i).hom) :
    (canonicalDescentFunctor' B S hS Xi f).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 74.4, Tag 04W7](https://stacks.math.columbia.edu/tag/04W7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
