---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsMap, AlgebraicGeometry.Scheme.Hom.deRhamAbelianPushforwardMap, Stacks.DeRhamPullback.deRhamPullbackChain, AlgebraicGeometry.Scheme.Hom.homEquiv_relativeDifferentialFormsMap, Stacks.DeRhamPullback.deRhamPullbackChain_f, AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialFormsMap_of_isPullback, AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialFormsMap_of_etale, AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsComparison
statement: formalized
proof: formalized
---

# 50.2 The de Rham complex

Section 50.2 of the Stacks Project, [Tag 07HX](https://stacks.math.columbia.edu/tag/07HX). 3 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07HX, the section

[Tag 07HX](https://stacks.math.columbia.edu/tag/07HX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean#L170). The attribute's comment: “the linearized canonical map on differential forms”.

> **Stacks Project, Tags 07HX, 0FL5 and 0FLV.** The canonical map
> `f^*Ω^n_{X/S} ⟶ Ω^n_{X'/S'}` on relative differential forms attached to a commutative square of
> schemes: the comparison of Tag 01CI followed by the degree-`n` component of the comparison of
> exterior algebras.

```lean
noncomputable def relativeDifferentialFormsMap (hcomm : f ≫ p = p' ≫ g) (n : ℤ) :
    (Scheme.Modules.pullback f).obj (relativeDifferentialForms p n) ⟶
      relativeDifferentialForms p' n
```

**`AlgebraicGeometry.Scheme.Hom.deRhamAbelianPushforwardMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Functoriality.lean#L412). The attribute's comment: “the canonical map of complexes `Ω^•_{X/S} ⟶ f_*Ω^•_{X'/S'}`”.

> **Stacks Project, Tag 07HX.** The canonical map of de Rham complexes
> `Ω^•_{X/S} ⟶ f_*Ω^•_{X'/S'}` of a commutative square of schemes, read in abelian sheaves.

```lean
noncomputable def deRhamAbelianPushforwardMap (hcomm : f ≫ p = p' ≫ g) :
    SheafOfModules.deRhamAbelianComplex (deRhamAlgebras p)
        (SheafOfModules.deRhamDifferential (deRhamAlgebras p)) ⟶
      ((Stacks.Cohomology.LerayLowDegree.abelianPushforward.{u, u}
          f.base).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        (SheafOfModules.deRhamAbelianComplex (deRhamAlgebras p')
          (SheafOfModules.deRhamDifferential (deRhamAlgebras p')))
```

**`Stacks.DeRhamPullback.deRhamPullbackChain`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplex.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplex.lean#L223). The attribute's comment: “the canonical map `f⁻¹Ω^•_{Y/S} ⟶ Ω^•_{X/S}` of a morphism of schemes over `S`, read in complexes of `(f∘g)^{-1}𝒪_S`-modules. The companion map `Ω^•_{X/S} ⟶ f_*Ω^•_{X'/S'}`, in abelian sheaves, is `AlgebraicGeometry.Scheme.Hom.deRhamAbelianPushforwardMap`.”.

> **Stacks Project, Tag 07HX.** The canonical morphism of complexes
>
> `ρ : f^{-1}Ω^•_{Y/S} ⟶ Ω^•_{X/S}`
>
> of `(f∘g)^{-1}𝒪_S`-modules on `X`, adjoint to the canonical map
> `Ω^•_{Y/S} ⟶ (relativeBase f g)_*Ω^•_{X/S}` of Tag 07HX read in `g^{-1}𝒪_S`-modules.

```lean
def deRhamPullbackChain :
    ((_root_.pullback (relativeBase f g)).mapHomologicalComplex (ComplexShape.up ℕ)).obj
        (Scheme.Hom.deRhamComplex g) ⟶
      Scheme.Hom.deRhamComplex (f ≫ g)
```

**`AlgebraicGeometry.Scheme.Hom.homEquiv_relativeDifferentialFormsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean#L94). The attribute's comment: “the linearized canonical map on forms is the transpose of the graded homomorphism”.

> **Stacks Project, Tag 07HX.** The canonical map `f^*Ω^n_{X/S} ⟶ Ω^n_{X'/S'}` on relative
> differential forms is the adjoint transpose of the degree-`n` component of the canonical
> homomorphism of sheaves of graded algebras `⋀ Ω_{X/S} ⟶ f_*(⋀ Ω_{X'/S'})`.

```lean
theorem homEquiv_relativeDifferentialFormsMap (hcomm : f ≫ p = p' ≫ g) (n : ℤ) :
    (modulePullbackPushforwardAdjunction f.toLRSHom.toShHom).homEquiv
        (relativeDifferentialForms p n) (relativeDifferentialForms p' n)
        (relativeDifferentialFormsMap f p p' g hcomm n) =
      (deRhamFormsPushforwardHom f p p' g hcomm).app n
```

**`Stacks.DeRhamPullback.deRhamPullbackChain_f`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean#L206). The attribute's comment: “the degree-n component of the canonical map f⁻¹Ω^•\_\{Y/S} ⟶ Ω^•\_\{X/S}”.

> **The degreewise factorization of the de Rham pullback map.** The degree-`n` component of
> `ρ : f^{-1}Ω^•_{Y/S} ⟶ Ω^•_{X/S}` is the comparison `f^{-1}Ω^n_{Y/S} ⟶ f^*Ω^n_{Y/S}` followed
> by the `𝒪_X`-linear canonical map `f^*Ω^n_{Y/S} ⟶ Ω^n_{X/S}` on relative differential forms,
> with coefficients restricted along `(f∘g)^{-1}𝒪_S ⟶ 𝒪_X`.

```lean
theorem deRhamPullbackChain_f (n : ℕ) :
    (deRhamPullbackChain f g).f n =
      relativeInverseImageToPullback f g (Scheme.Hom.relativeDifferentialForms g (n : ℤ)) ≫
        (_root_.pushforward (toInverseImageBase (f ≫ g))).map
          (Scheme.Hom.relativeDifferentialFormsMap f g (f ≫ g) (𝟙 S)
            ((Category.comp_id (f ≫ g)).symm) (n : ℤ))
```

## Tag 0FL5, a lemma

[Tag 0FL5](https://stacks.math.columbia.edu/tag/0FL5) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialFormsMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/BaseChange.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/BaseChange.lean#L51).

> In a cartesian square of schemes, the canonical map `f^*Ω^n_{X/S} ⟶ Ω^n_{X'/S'}` on relative
> differential forms is an isomorphism in every degree.

```lean
theorem isIso_relativeDifferentialFormsMap_of_isPullback (H : IsPullback f p' p g) (n : ℤ) :
    IsIso (relativeDifferentialFormsMap f p p' g H.w n)
```

## Tag 0FLV, a lemma

[Tag 0FLV](https://stacks.math.columbia.edu/tag/0FLV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialFormsMap_of_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/BaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/BaseChange.lean#L60). The attribute's comment: “isomorphism on each exterior power”.

> In a commutative square of schemes whose two horizontal arrows `f : X' ⟶ X` and `g : S' ⟶ S`
> are étale, the canonical map `f^*Ω^n_{X/S} ⟶ Ω^n_{X'/S'}` on relative differential forms is an
> isomorphism in every degree.

```lean
theorem isIso_relativeDifferentialFormsMap_of_etale (hcomm : f ≫ p = p' ≫ g)
    [Etale f] [Etale g] (n : ℤ) :
    IsIso (relativeDifferentialFormsMap f p p' g hcomm n)
```

**`AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsComparison`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean#L133). The attribute's comment: “canonical graded comparison”.

> **Stacks Project, Tags 0FL5 and 0FLV.** The canonical homomorphism of sheaves of graded
> algebras `⋀(f^*Ω_{X/S}) ⟶ ⋀(Ω_{X'/S'})` attached to a commutative square of schemes: the unique
> unital homomorphism extending the canonical map on relative differentials of Tag 01UV.

```lean
noncomputable def relativeDifferentialFormsComparison (hcomm : f ≫ p = p' ≫ g) :
    SheafOfModules.GradedAlgebra.UnitalHom
      (Scheme.Modules.exteriorAlgebra
        ((Scheme.Modules.pullback f).obj (relativeDifferentials p)))
      (relativeDifferentialFormsAlgebra p')
```

**`AlgebraicGeometry.Scheme.Hom.relativeDifferentialFormsComparison_generator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/Complex/DifferentialForms.lean#L146). The attribute's comment: “canonical map in degree one”.

> **Stacks Project, Tags 0FL5 and 0FLV.** In degree one the canonical comparison of exterior
> algebras is the canonical map on relative differentials of Tag 01UV.

```lean
theorem relativeDifferentialFormsComparison_generator (hcomm : f ≫ p = p' ≫ g) :
    Scheme.Modules.exteriorGenerator
          ((Scheme.Modules.pullback f).obj (relativeDifferentials p)) ≫
        (relativeDifferentialFormsComparison f p p' g hcomm).app 1 =
      relativeDifferentialsMap f p p' g hcomm ≫
        Scheme.Modules.exteriorGenerator (relativeDifferentials p')
```

**`Stacks.DeRhamPullback.deRhamPullbackChain_f_exteriorPowerPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DeRham/PullbackComplexDegreewise.lean#L225). The attribute's comment: “the degree-n component of f⁻¹Ω^•\_\{Y/S} ⟶ Ω^•\_\{X/S} factors through ⋀ⁿ(f^*Ω\_\{Y/S})”.

> **The degreewise factorization of `ρ` through `⋀^n(f^*Ω_{Y/S})`**: the comparison
> `f^{-1}Ω^n_{Y/S} ⟶ f^*Ω^n_{Y/S}`, the comparison `f^*(⋀^nΩ_{Y/S}) ≅ ⋀^n(f^*Ω_{Y/S})` of Tag
> 01CI, and the degree-`n` component of the homomorphism of exterior algebras of Tag 0FLV.

```lean
theorem deRhamPullbackChain_f_exteriorPowerPullback (n : ℕ) :
    (deRhamPullbackChain f g).f n =
      relativeInverseImageToPullback f g (Scheme.Hom.relativeDifferentialForms g (n : ℤ)) ≫
        (_root_.pushforward (toInverseImageBase (f ≫ g))).map
          (((Stacks.PullbackExteriorAlgebra.exteriorAlgebraPullbackIso f.toLRSHom.toShHom
                (Scheme.Hom.relativeDifferentialFormsAlgebra g)
                (Scheme.Modules.exteriorGenerator (Scheme.Hom.relativeDifferentials g))
                (Scheme.Modules.exteriorAlgebra
                  ((Scheme.Modules.pullback f).obj (Scheme.Hom.relativeDifferentials g)))
                (Scheme.Modules.exteriorGenerator
                  ((Scheme.Modules.pullback f).obj (Scheme.Hom.relativeDifferentials g)))
                (Scheme.Modules.isExteriorAlgebra_exteriorAlgebra
                  (Scheme.Hom.relativeDifferentials g))
                (Scheme.Modules.isExteriorAlgebra_exteriorAlgebra _)).app (n : ℤ)).hom ≫
            (Scheme.Hom.relativeDifferentialFormsComparison f g (f ≫ g) (𝟙 S)
              ((Category.comp_id (f ≫ g)).symm)).app (n : ℤ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 50.2, Tag 07HX](https://stacks.math.columbia.edu/tag/07HX)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
