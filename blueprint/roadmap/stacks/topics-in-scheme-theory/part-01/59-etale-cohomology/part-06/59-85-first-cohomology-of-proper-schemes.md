---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.bijective_etaleConstantCohomologyRestriction_iff, Stacks.EtaleCohomology.bijective_etaleConstantCohomologyRestriction_one_of_isProper, Stacks.EtaleCohomology.subsingleton_H_closedFibre_projectiveLine_of_injective
statement: formalized
proof: formalized
---

# 59.85 First cohomology of proper schemes

Section 59.85 of the Stacks Project, [Tag 0A5F](https://stacks.math.columbia.edu/tag/0A5F). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A5G, a lemma

[Tag 0A5G](https://stacks.math.columbia.edu/tag/0A5G) in the Stacks Project.

**`Stacks.EtaleCohomology.bijective_etaleConstantCohomologyRestriction_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperHenselianFirstCohomology.lean, line 268](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperHenselianFirstCohomology.lean#L268). The attribute's comment: “the reduction of the tag to an Ext computation, in every degree q: the canonical map H^q(X, M) -> H^q(X\_0, M) is bijective if and only if etale inverse image along the closed-fibre inclusion is bijective on Ext^q out of the constant sheaf Z. The geometric content of the tag -- that this holds in degree one for a proper morphism over a henselian local ring -- is not proved here. The inputs the source's degree-one argument needs ARE available: Stacks 03AJ as Stacks.Cohomology.Torsors.torsorIsoClassesEquivH1, Stacks 03RV as AlgebraicGeometry.finiteLocallyConstantFiniteEtaleEquivalence, and Stacks 0A48 as AlgebraicGeometry.isEquivalence\_finiteEtaleBaseChange\_of\_isProper\_of\_henselianLocalRing. What is missing is the bridge between them: no result transports an Ext^1 or Sheaf.H map along a CHANGE OF SITE into torsor language -- torsorIsoClassesEquivH1\_naturality is naturality in the coefficient sheaf on a fixed site -- and the restriction map here lives on Mathlib's Scheme.smallEtaleTopology while 03RV lives on SmallEtale.topology of a BigEtaleSite, with no comparison. Nor does anything say that a torsor under a finite constant sheaf is finite locally constant”.

> **Stacks 0A5G reduced to an `Ext` computation.** Restriction to the closed fibre is bijective
> in degree `q` exactly when the étale inverse-image functor along the closed-fibre inclusion is
> bijective on `Ext^q` out of the constant sheaf `ℤ`: the two maps differ by composition with the
> two canonical constant-sheaf comparison isomorphisms, and composing with an isomorphism is
> bijective on `Ext`.
>
> Nothing here is special to a proper morphism over a henselian local ring, and nothing here
> computes either side. What Stacks 0A5G asserts is that in degree one the right-hand side holds
> when `A` is henselian local, `f` is proper and `M` is finite; that is the geometric content, and
> it rests on Stacks 03AJ, 03RV, 0A48 and 0A0C.

```lean
theorem bijective_etaleConstantCohomologyRestriction_iff :
    Function.Bijective (etaleConstantCohomologyRestriction.{u, v, w} A f M q) ↔
      Function.Bijective
        ((etaleAbelianInverseImage.{u, v} (closedFibreInclusion A f)).mapExtAddHom.{w, w}
          ((constantSheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).obj
            (AddCommGrpCat.of (ULift ℤ)))
          (etaleConstantSheaf.{u, v} X M) q)
```

**`Stacks.EtaleCohomology.bijective_etaleConstantCohomologyRestriction_one_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperHenselianFirstCohomologyBijective.lean, line 370](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperHenselianFirstCohomologyBijective.lean#L370).

> For `A` a henselian local ring, `X` proper over `A` and `M` a finite abelian group,
> restriction `H¹(X, M) ⟶ H¹(X₀, M)` to the closed fibre is bijective.
>
> Surjectivity is `surjective_etaleConstantCohomologyRestriction_one_of_isProper`. Injectivity
> (`Stacks.EtaleCohomology.injective_etaleCohomologyRestrictionMap_constantSheaf_one`): a class on
> `X` dies on a surjective finite étale cover `π`, hence is a boundary of a section of the quotient
> `Q` of `M ⟶ π_* π⁻¹ M`; restriction to `X₀` is surjective on sections of `π_* π⁻¹ M` and injective
> on sections of `Q`, both being finite locally constant and base change to `X₀` being fully faithful
> on finite étale covers (Stacks 0A48).

```lean
theorem bijective_etaleConstantCohomologyRestriction_one_of_isProper
    (A : Type u) [CommRing A] [HenselianLocalRing A] {X : Scheme.{u}}
    (f : X ⟶ Spec (.of A)) [IsProper f] (M : Type) [AddCommGroup M] [Finite M] :
    Function.Bijective (etaleConstantCohomologyRestriction.{u, 0, u + 1} A f M 1)
```

## Tag 0A5H, a lemma

[Tag 0A5H](https://stacks.math.columbia.edu/tag/0A5H) in the Stacks Project.

Declarations registered for the tag:

- [`Stacks.EtaleCohomology.subsingleton_H_closedFibre_projectiveLine_of_injective`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ClosedFibreProjectiveLineInjective.lean#L258), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/ProperBaseChangeStacksTags.lean#L43) (StacksFrontier).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.85, Tag 0A5F](https://stacks.math.columbia.edu/tag/0A5F)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
