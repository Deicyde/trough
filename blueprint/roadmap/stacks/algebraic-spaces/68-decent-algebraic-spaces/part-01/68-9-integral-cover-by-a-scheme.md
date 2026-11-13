---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_isIntegralHom_isPullback_of_isOpenImmersion, AlgebraicGeometry.Space.existsIntegralSurjectiveSchemeCover_and_refining, AlgebraicGeometry.Space.exists_integralSchemeCover_finiteEtaleOverDenseOpen_and_refining
statement: formalized
proof: formalized
---

# 68.9 Integral cover by a scheme

Section 68.9 of the Stacks Project, [Tag 0D2T](https://stacks.math.columbia.edu/tag/0D2T). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G2D, a lemma

[Tag 0G2D](https://stacks.math.columbia.edu/tag/0G2D) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isIntegralHom_isPullback_of_isOpenImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ExtendIntegralMorphism.lean, line 111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ExtendIntegralMorphism.lean#L111).

> **Stacks 0G2D.** Let `j : V ⟶ Y` be a quasi-compact open immersion of algebraic spaces over
> a scheme `S` and let `π : Z ⟶ V` be an integral morphism. Then there is an integral morphism
> `ν : Y' ⟶ Y` of algebraic spaces over `S` such that `Z` is `V`-isomorphic to the inverse image
> of `V` in `Y'`: the square formed by `π`, `j`, `ν` and the canonical morphism `Z ⟶ Y'` is
> cartesian.
>
> `Y'` is the normalization of `Y` in `Z`, and the cartesian square is obtained from the
> chart description of that normalization by the cancellation of Tag 07VZ along a surjective étale
> chart of `V`; see the implementation notes.

```lean
theorem exists_isIntegralHom_isPullback_of_isOpenImmersion
    (hZ : IsAlgebraicSpace B S hS Z) (hV : IsAlgebraicSpace B S hS V)
    (hY : IsAlgebraicSpace B S hS Y) (j : V ⟶ Y) (hj : IsOpenImmersion B S hS j)
    (hjqc : IsQuasiCompact B S hS j) (π : Z ⟶ V) (hπ : IsIntegralHom B S hS π) :
    ∃ (Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (ν : Y' ⟶ Y) (f' : Z ⟶ Y'),
      IsAlgebraicSpace B S hS Y' ∧ IsIntegralHom B S hS ν ∧ IsPullback f' π ν j
```

## Tag 09YB, a lemma

[Tag 09YB](https://stacks.math.columbia.edu/tag/09YB) in the Stacks Project.

**`AlgebraicGeometry.Space.existsIntegralSurjectiveSchemeCover_and_refining`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralSchemeCoverExistence.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralSchemeCoverExistence.lean#L185).

> **Stacks Project, Tag 09YB.** Let `X` be a quasi-compact and quasi-separated algebraic
> space over a scheme `S`. Then
>
> 1. there is a surjective integral morphism to `X` from the presheaf represented by an object of
>    the big fppf site — a scheme over `S` — and
> 2. given a surjective étale morphism `p : U ⟶ X` from an algebraic space, such a cover can be
>    chosen so that it factors through `p` on a representable open subspace neighbourhood of
>    every one of its points.
>
> **Both clauses are proved, over no hypothesis.** Clause (1) is the source's induction on a bound
> for the degree of the geometric fibres of an étale chart, performed in
> `StacksFrontier.AlgebraicGeometry.Spaces.IntegralSchemeCoverInduction`; clause (2) is deduced here
> from clause (1) by the unconditional Stacks 0CP0.

```lean
theorem existsIntegralSurjectiveSchemeCover_and_refining
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X) :
    ExistsIntegralSurjectiveSchemeCover B S hS X ∧
      ∀ (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS U →
        ∀ p : U ⟶ X, IsSurjective B S hS p → IsEtale B S hS p →
          ∃ (Y : BigFppfOver B S hS) (f : yoneda.obj Y ⟶ X),
            IsSurjective B S hS f ∧ IsIntegralHom B S hS f ∧
              FactorsZariskiLocallyThrough B S hS p Y f
```

## Tag 0GUL, a lemma

[Tag 0GUL](https://stacks.math.columbia.edu/tag/0GUL) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_integralSchemeCover_finiteEtaleOverDenseOpen_and_refining`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralSchemeCoverEtaleInduction.lean, line 1423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralSchemeCoverEtaleInduction.lean#L1423).

> **Stacks Project, Tag 0GUL.** Let `X` be a quasi-compact and quasi-separated algebraic
> space over a scheme `S` such that `|X|` has finitely many irreducible components. Then
>
> 1. there is a surjective integral morphism to `X` from the presheaf represented by an object of
>    the big fppf site — a scheme over `S` — which is finite étale over a quasi-compact open
>    subspace of `X` with dense point set, and
> 2. given a surjective étale morphism `p : V ⟶ X` from an algebraic space, such a cover can be
>    chosen so that it factors through `p` on a representable open subspace neighbourhood of
>    every one of its points.
>
> Clause (2) for a cover `p` is reduced to a chart `c : h_{V₀} ⟶ V`
> (`AlgebraicGeometry.Space.existsIntegralSchemeCoverRefining_of_comp_chart`); for the chart
> `c ≫ p` the induction gives a cover étale over a dense open
> (`AlgebraicGeometry.Space.existsIntegralSchemeCoverEtaleRefining_of_isEtale`), which is upgraded
> to one finite étale over a quasi-compact dense open
> (`AlgebraicGeometry.Space.existsIntegralSchemeCoverRefining_of_etaleRefining`). Clause (1) is
> clause (2) at the identity of `X`.

```lean
theorem exists_integralSchemeCover_finiteEtaleOverDenseOpen_and_refining
    (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hX : IsAlgebraicSpace B S hS X)
    (hXqc : IsQuasiCompactSpace B S hS X)
    (hXqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hcomp : (irreducibleComponents (points B S hS X)).Finite) :
    ExistsIntegralSchemeCoverFiniteEtaleOverDenseOpen B S hS X ∧
      ∀ (V : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u), IsAlgebraicSpace B S hS V →
        ∀ p : V ⟶ X, IsSurjective B S hS p → IsEtale B S hS p →
          ExistsIntegralSchemeCoverRefining B S hS p
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.9, Tag 0D2T](https://stacks.math.columbia.edu/tag/0D2T)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
