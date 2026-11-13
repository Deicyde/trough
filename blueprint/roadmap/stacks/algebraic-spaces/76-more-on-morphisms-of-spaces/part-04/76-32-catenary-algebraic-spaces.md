---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.exists_glueingSpace_factorization, AlgebraicGeometry.Space.exists_dimensionFunction_inducedDimensionValue
statement: formalized
proof: formalized
---

# 76.32 Catenary algebraic spaces

Section 76.32 of the Stacks Project, [Tag 0EDL](https://stacks.math.columbia.edu/tag/0EDL). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EDM, a lemma

[Tag 0EDM](https://stacks.math.columbia.edu/tag/0EDM) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_glueingSpace_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GlueingSpaceAway.lean, line 544](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/GlueingSpaceAway.lean#L544).

> **Stacks 0EDM.**  Let `f : X ⟶ Y` be an integral morphism of algebraic spaces over `S`, and
> let `y : Spec k ⟶ Y` be a closed immersion.  Then `f` factors as `X ⟶ X' ⟶ Y` with
>
> 1. `X' ⟶ Y` integral,
> 2. `X ⟶ X'` an isomorphism over the open complement `X' ∖ X'_y` of the fibre
>    `X'_y = |h|⁻¹ {y}`,
> 3. `X'_y` a single point `p`, which is the point of a closed immersion `x' : Spec k ⟶ X'` over
>    `y`, so that `κ(p) = k`,
>
> and moreover `X' ⟶ Y` is finite when `f` is finite and `Y` is locally Noetherian.
>
> The residue field in clause (3) is that of Stacks 0EMW: the field of a monomorphism from the
> spectrum of a field representing the point, unique up to unique isomorphism over the space
> (`AlgebraicGeometry.Space.residueFieldRepresentative_unique`).  A closed immersion is a
> monomorphism, so `x'` is such a representative of `p` and `κ(p) = k` is the statement that `x'`
> is a closed immersion with image `{p}`.
>
> The space `X'` is the quotient of the chart-level pushout over a separated étale chart of `Y`
> (`AlgebraicGeometry.Space.EtaleChartRelation.exists_of_isAlgebraicSpace`) by the étale
> equivalence relation induced by the chart's kernel pair; the sheafification it needs is
> `AlgebraicGeometry.BigFppfOver.hasSheafify_type`.  "Locally Noetherian" is the source's
> definition for algebraic spaces, a locally Noetherian surjective étale atlas
> (`AlgebraicGeometry.Space.HasEtaleLocalProperty`, Stacks 03E6), and it gives local
> Noetherianity of the chosen chart by Stacks 03E8.

```lean
theorem exists_glueingSpace_factorization {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsIntegralHom B S hS f.hom) {k : Type u} [Field k]
    (hk : B.Contains (Spec (CommRingCat.of k))) (σ : Spec (CommRingCat.of k) ⟶ S)
    (y : yoneda.obj (BigFppfOver.mk B S hS hk σ) ⟶ Y.1) (hy : IsClosedImmersion B S hS y) :
    ∃ (X' : AlgebraicSpaces B S hS) (g : X ⟶ X') (h : X' ⟶ Y),
      g ≫ h = f ∧
      IsIntegralHom B S hS h.hom ∧
      IsIso (openComplementRestriction B S hS g.hom
        (pointsMap B S hS X'.1 h.hom ⁻¹'
          Set.range (pointsMap B S hS (yoneda.obj (BigFppfOver.mk B S hS hk σ)) y))) ∧
      (∃ (x' : yoneda.obj (BigFppfOver.mk B S hS hk σ) ⟶ X'.1) (p : points B S hS X'.1),
        IsClosedImmersion B S hS x' ∧ x' ≫ h.hom = y ∧
        pointsMap B S hS X'.1 h.hom ⁻¹'
            Set.range (pointsMap B S hS (yoneda.obj (BigFppfOver.mk B S hS hk σ)) y) = {p} ∧
        Set.range (pointsMap B S hS (yoneda.obj (BigFppfOver.mk B S hS hk σ)) x') = {p}) ∧
      (IsFinite B S hS f.hom →
        HasEtaleLocalProperty B S hS Y.1
          (fun T : Scheme.{u} ↦ _root_.AlgebraicGeometry.IsLocallyNoetherian T) →
        IsFinite B S hS h.hom)
```

## Tag 0EDN, a lemma

[Tag 0EDN](https://stacks.math.columbia.edu/tag/0EDN) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dimensionFunction_inducedDimensionValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/InducedDimensionFunction.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/InducedDimensionFunction.lean#L72).

> **Stacks 0EDN.** Let `Y` be a decent, locally Noetherian, universally catenary algebraic
> space and `δ` a dimension function on `|Y|`. If `X` is a decent algebraic space and `f : X ⟶ Y`
> is locally of finite type, then `δ_X`, the value of `δ` at the image of a point plus the
> transcendence degree of the point over its image, is a dimension function on `|X|`.

```lean
theorem exists_dimensionFunction_inducedDimensionValue (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hY : IsAlgebraicSpace B S hS Y) (hYdec : IsDecentSpace B S hS Y)
    (hYN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} ↦ IsLocallyNoetherian T))
    (hYcat : IsUniversallyCatenary B S hS Y) (δ : DimensionFunction (points B S hS Y))
    (hX : IsAlgebraicSpace B S hS X) (hXdec : IsDecentSpace B S hS X) (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ d : DimensionFunction (points B S hS X), ∀ x : points B S hS X,
      d x = inducedDimensionValue B S hS δ f x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.32, Tag 0EDL](https://stacks.math.columbia.edu/tag/0EDL)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
