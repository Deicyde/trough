---
declaration: section
origin: cited
lean: AlgebraicGeometry.not_exists_cover_zariskiFiniteEtale_lift
statement: formalized
proof: formalized
---

# 110.57 The étale topology vs Zariski and finite étale Covers

Section 110.57 of the Stacks Project, [Tag 0HAQ](https://stacks.math.columbia.edu/tag/0HAQ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0HAR, a lemma

[Tag 0HAR](https://stacks.math.columbia.edu/tag/0HAR) in the Stacks Project.

**`AlgebraicGeometry.not_exists_cover_zariskiFiniteEtale_lift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Sites/EtaleNotZariskiFiniteEtale.lean, line 942](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sites/EtaleNotZariskiFiniteEtale.lean#L942).

> **Stacks Project, Tag 0HAR.** Let `X` be a smooth connected affine curve over `ℂ` and
> `g : Y ⟶ X` a finite morphism of degree `3` from a smooth connected curve `Y` over `ℂ`, such that
> for some point `x` of `X` the fibre `g⁻¹(x) = {u, y}` consists of an unramified point `u`
> (ramification index `1`) and a ramified point `y` (ramification index `2`), and such that `g` is
> unramified everywhere except at `y`. Put `U = Y ∖ {y}`. Then the étale cover `U ⟶ X` cannot be
> refined by any finite composition of open immersions and finite étale morphisms: there is no
> family of finite compositions `W i ⟶ X` of open immersions and finite étale morphisms, each
> factoring through `U`, which is jointly surjective.
>
> The degree of `g` is `deg(Y/X)` of [Stacks, Tag 02NY] (`AlgebraicGeometry.degreeOver`), the
> ramification indices are those of the local rings
> (`Stacks.DiscreteValuationRing.Ramification.ramificationIdx`), and "unramified away from `y`" is
> formal unramifiedness of the restriction of `g` to `U`. The finite compositions are the
> multiplicative closure of the class of open immersions and finite étale morphisms.

```lean
theorem not_exists_cover_zariskiFiniteEtale_lift {X Y : Scheme.{0}} (πX : X ⟶ Spec (.of ℂ))
    (πY : Y ⟶ Spec (.of ℂ)) [IsCurve ℂ πX] [Smooth πX] [IsAffine X] [IsCurve ℂ πY] [Smooth πY]
    (g : Y ⟶ X) (hg : g ≫ πX = πY) [IsFinite g] [IsDominant g] (_hdeg : degreeOver g = 3)
    (x : X) (u y : Y) (huy : u ≠ y) (hfib : g ⁻¹' {x} = {u, y})
    (_hu1 : letI := (g.stalkMap u).hom.toAlgebra
      Stacks.DiscreteValuationRing.Ramification.ramificationIdx (X.presheaf.stalk (g u))
        (Y.presheaf.stalk u) = 1)
    (hy2 : letI := (g.stalkMap y).hom.toAlgebra
      Stacks.DiscreteValuationRing.Ramification.ramificationIdx (X.presheaf.stalk (g y))
        (Y.presheaf.stalk y) = 2)
    (U : Y.Opens) (hU : (U : Set Y) = {y}ᶜ) (hunr : FormallyUnramified (U.ι ≫ g)) :
    ¬ ∃ (ι : Type) (W : ι → Scheme.{0}) (p : ∀ i, W i ⟶ X),
      (∀ i, (@IsOpenImmersion ⊔ (@IsFinite ⊓ @Etale) :
        MorphismProperty Scheme.{0}).multiplicativeClosure (p i)) ∧
      (∀ i, ∃ s : W i ⟶ U, s ≫ U.ι ≫ g = p i) ∧ ⋃ i, Set.range (p i) = Set.univ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.57, Tag 0HAQ](https://stacks.math.columbia.edu/tag/0HAQ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
