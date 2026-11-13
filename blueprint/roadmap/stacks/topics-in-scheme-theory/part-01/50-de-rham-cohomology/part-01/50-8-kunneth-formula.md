---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.deRhamBoxTotalIso, AlgebraicGeometry.Scheme.Hom.deRhamBoxTotalDegreeIso, Stacks.Cohomology.BoxKunneth.deRhamGlobalKunnethMap, Stacks.Cohomology.BoxKunneth.isIso_deRhamGlobalKunnethMap_canonical, Stacks.Cohomology.BoxKunneth.deRhamRelativeKunnethMap, Stacks.Cohomology.BoxKunneth.isIso_deRhamRelativeKunnethMap_of_smooth
statement: formalized
proof: formalized
---

# 50.8 Künneth formula

Section 50.8 of the Stacks Project, [Tag 0FM9](https://stacks.math.columbia.edu/tag/0FM9). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FMA, a lemma

[Tag 0FMA](https://stacks.math.columbia.edu/tag/0FMA) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.deRhamBoxTotalIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Kunneth.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/Kunneth.lean#L65).

> For two morphisms of schemes `a : X ⟶ S` and `b : Y ⟶ S` there is a canonical isomorphism of
> complexes
>
> `Tot(Ω^•_{X/S} ⊠ Ω^•_{Y/S}) ≅ Ω^•_{X ×_S Y / S}`
>
> between the total complex of the box product of the two relative de Rham complexes and the
> relative de Rham complex of the fibre product. In degree `n` it is the isomorphism assembled from
> the splitting of `Ω_{X ×_S Y/S}` of [Stacks, Tag 01V1], the Künneth decomposition of an exterior
> power of a direct sum and the comparison of [Stacks, Tag 01CI], which on the `(p, q)` summand is
> `ω ⊗ η ↦ pr₁^*ω ∧ pr₂^*η`; the compatibility with the differentials is the graded Leibniz
> rule.

```lean
noncomputable def deRhamBoxTotalIso :
    deRhamBoxTotal a b ≅ deRhamDiffOpComplex (pullback.fst a b ≫ a)
```

**`AlgebraicGeometry.Scheme.Hom.deRhamBoxTotalDegreeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/KunnethDegreewise.lean, line 250](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/KunnethDegreewise.lean#L250). The attribute's comment: “the degreewise isomorphism: in each degree `n` an isomorphism `Tot(Ω^•_{X/S} ⊠ Ω^•_{Y/S})^n ≅ Ω^n_{X ×_S Y/S}`. NOT compatibility with the differentials, and so NOT the isomorphism of complexes”.

> **Stacks Project, Tag 0FMA, the degreewise isomorphism.** In each degree `n` the total
> complex `Tot(Ω^•_{X/S} ⊠ Ω^•_{Y/S})` of the box product of the two relative de Rham complexes is
> canonically isomorphic to `Ω^n_{X ×_S Y / S}`, as objects of the category of finite-order
> differential operators on `X ×_S Y / S`.
>
> **Compatibility with the differentials is not included**: this is an isomorphism of the terms in
> each fixed degree, not a morphism of complexes.

```lean
noncomputable def deRhamBoxTotalDegreeIso (n : ℕ) :
    (deRhamBoxTotal a b).X n ≅ (deRhamDiffOpComplex (pullback.fst a b ≫ a)).X n
```

## Tag 0FMB, a lemma

[Tag 0FMB](https://stacks.math.columbia.edu/tag/0FMB) in the Stacks Project.

**`Stacks.Cohomology.BoxKunneth.deRhamGlobalKunnethMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/KunnethFormula.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/KunnethFormula.lean#L605). The attribute's comment: “the map: the global Künneth map of Tag 0FLR at the two de Rham complexes, read as ℤ-indexed complexes by extension by zero, followed by derived global sections of the Tag 0FMA isomorphism; it carries the one parameter of the Tag 0FLR map, the global cup product on the base, and the map of the source is this at the canonical global cup product globalCupProductCanonical of Section 0FKU. The step-(5) comparison is not carried, being constructed”.

> **The de Rham Künneth map of [Stacks, Tag 0FMB]**
>
> `RΓ(X, Ω^•_{X/S}) ⊗^𝐋_A RΓ(Y, Ω^•_{Y/S}) ⟶ RΓ(X ×_S Y, Ω^•_{X ×_S Y/S})`
>
> in `D(A)` for `A = Γ(S, 𝒪_S)`: the global Künneth map of [Stacks, Tag 0FLR] at the two relative
> de Rham complexes, read as `ℤ`-indexed complexes by extension by zero, followed by derived global
> sections of the isomorphism `Tot(Ω^•_{X/S} ⊠ Ω^•_{Y/S}) ≅ Ω^•_{X ×_S Y/S}` of
> [Stacks, Tag 0FMA]. The complexes whose derived global sections are taken are the complexes of
> inverse-image modules underlying the de Rham complexes; the global cup product `κ` is the one
> parameter that the map of [Stacks, Tag 0FLR] carries, its step-(5) comparison being constructed
> as `Stacks.Cohomology.BoxKunneth.boxTotalComparison`. The map of the source is this one at the
> canonical global cup product `Stacks.Cohomology.GlobalKunneth.globalCupProductCanonical` of
> [Stacks, Section 0FKU].

```lean
def deRhamGlobalKunnethMap (κ : GlobalCupProduct S.toRingedSpace) :
    ((tensorBase S.toRingedSpace).obj
          ((sectionsOverBase (inverseImageBaseProjection a)).obj
            (DerivedCategory.Q.obj (leftComplex a (deRhamDiffOpCochainComplex a))))).obj
        ((sectionsOverBase (inverseImageBaseProjection b)).obj
          (DerivedCategory.Q.obj (rightComplex b (deRhamDiffOpCochainComplex b)))) ⟶
      (sectionsOverBase (inverseImageBaseProjection (pullback.fst a b ≫ a))).obj
        (DerivedCategory.Q.obj
          (((toInverseImageModules (pullback.fst a b ≫ a)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj ((deRhamDiffOpComplex (pullback.fst a b ≫ a)).extend
              ComplexShape.embeddingUpNat)))
```

**`Stacks.Cohomology.BoxKunneth.isIso_deRhamGlobalKunnethMap_canonical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/KunnethFormulaAffineSmooth.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/KunnethFormulaAffineSmooth.lean#L68). The attribute's comment: “the isomorphism at the source's hypotheses (S affine; X, Y smooth and quasi-compact with affine diagonal over S), for the map built from the canonical global cup product of Section 0FKU; nothing is assumed”.

> **[Stacks, Tag 0FMB].** Let `S = Spec(A)` be affine and let `a : X ⟶ S` and `b : Y ⟶ S` be
> smooth and quasi-compact with affine diagonal over `S`. Then the de Rham Künneth map
>
> `RΓ(X, Ω^•_{X/S}) ⊗^𝐋_A RΓ(Y, Ω^•_{Y/S}) ⟶ RΓ(X ×_S Y, Ω^•_{X ×_S Y/S})`
>
> is an isomorphism in `D(A)`. The map is `deRhamGlobalKunnethMap` at the canonical global cup
> product of [Stacks, Section 0FKU]. Nothing is assumed: the relative isomorphism of
> [Stacks, Tag 0FMC] holds at these hypotheses, and over the affine base it gives the global one.

```lean
theorem isIso_deRhamGlobalKunnethMap_canonical [IsAffine S]
    [AlgebraicGeometry.Smooth a] [AlgebraicGeometry.Smooth b] [QuasiCompact a] [QuasiCompact b]
    [IsAffineHom (pullback.diagonal a)] [IsAffineHom (pullback.diagonal b)] :
    IsIso (deRhamGlobalKunnethMap a b (globalCupProductCanonical S.toRingedSpace))
```

## Tag 0FMC, a lemma

[Tag 0FMC](https://stacks.math.columbia.edu/tag/0FMC) in the Stacks Project.

**`Stacks.Cohomology.BoxKunneth.deRhamRelativeKunnethMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethFormula.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethFormula.lean#L175). The attribute's comment: “the relative cup product whose invertibility the tag asserts”.

> **The relative cup product of [Stacks, Tag 0FMC]**
>
> `Ra_*Ω^•_{X/S} ⊗^𝐋_{𝒪_S} Rb_*Ω^•_{Y/S} ⟶ Rf_*Ω^•_{X ×_S Y/S}`
>
> in `D(𝒪_S)`: the relative Künneth map of [Stacks, Tag 0G4B] at the two relative de Rham
> complexes, read as `ℤ`-indexed complexes by extension by zero, followed by `Rf_*` of the
> isomorphism `Tot(Ω^•_{X/S} ⊠ Ω^•_{Y/S}) ≅ Ω^•_{X ×_S Y/S}` of [Stacks, Tag 0FMA]. The complexes
> pushed forward are the complexes of inverse-image modules underlying the de Rham complexes. The
> map of [Stacks, Tag 0G4B] carries no parameter: its step-(5) comparison is constructed, as
> `Stacks.Cohomology.BoxKunneth.boxTotalComparison`, and is unique by
> `Stacks.Cohomology.BoxKunneth.BoxTotalComparison.hom_unique`.

```lean
def deRhamRelativeKunnethMap :
    ((derivedTensorProductFunctor.{u, u + 1} (SheafedSpace.sheaf S.toRingedSpace)).obj
          ((derivedPushforward.{u, u + 1, u + 1} (inverseImageBaseProjection a)).obj
            (DerivedCategory.Q.obj (leftComplex a (deRhamDiffOpCochainComplex a))))).obj
        ((derivedPushforward.{u, u + 1, u + 1} (inverseImageBaseProjection b)).obj
          (DerivedCategory.Q.obj (rightComplex b (deRhamDiffOpCochainComplex b)))) ⟶
      (derivedPushforward.{u, u + 1, u + 1}
          (inverseImageBaseProjection (pullback.fst a b ≫ a))).obj
        (DerivedCategory.Q.obj
          (((toInverseImageModules (pullback.fst a b ≫ a)).mapHomologicalComplex
            (ComplexShape.up ℤ)).obj ((deRhamDiffOpComplex (pullback.fst a b ≫ a)).extend
              ComplexShape.embeddingUpNat)))
```

**`Stacks.Cohomology.BoxKunneth.isIso_deRhamRelativeKunnethMap_of_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethFormulaSmooth.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DeRham/RelativeKunnethFormulaSmooth.lean#L187).

> **[Stacks, Tag 0FMC]: the relative Künneth formula for de Rham complexes.** Let `a : X ⟶ S`
> and `b : Y ⟶ S` be smooth and quasi-compact morphisms of schemes with affine diagonals. Then the
> relative cup product
> `Ra_*Ω^•_{X/S} ⊗^𝐋_{𝒪_S} Rb_*Ω^•_{Y/S} ⟶ Rf_*Ω^•_{X ×_S Y/S}`
> is an isomorphism in `D(𝒪_S)`. The relative Künneth map of [Stacks, Tag 0G4B] is invertible at
> two flat modules in single degrees, by [Stacks, Tag 0FLQ] through the change of rings
> (`isIso_relativeBoxKunnethMap_single`); hence at bounded complexes with flat terms, by the
> dévissage of [Stacks, Tag 0FLT] (`isIso_relativeBoxKunnethMap_of_isIso_single`); hence at the
> locally bounded de Rham complexes, by truncation
> (`isIso_relativeBoxKunnethMap_of_isIso_stupidTrunc`).

```lean
theorem isIso_deRhamRelativeKunnethMap_of_smooth {Y : Scheme.{u}} (b : Y ⟶ S) [Smooth a]
    [Smooth b] [QuasiCompact a] [QuasiCompact b] [IsAffineHom (pullback.diagonal a)]
    [IsAffineHom (pullback.diagonal b)] :
    IsIso (deRhamRelativeKunnethMap a b)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.8, Tag 0FM9](https://stacks.math.columbia.edu/tag/0FM9)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
