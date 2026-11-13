---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence', CategoryTheory.Sheaf.resolutionPrincipalPartsShortComplex_shortExact, CategoryTheory.Sheaf.sheafAtiyahTriangle_distinguished, CategoryTheory.Sheaf.atiyahClass, CategoryTheory.Sheaf.sheafAtiyahClass
statement: formalized
proof: formalized
---

# 92.19 The Atiyah class of a sheaf of modules

Section 92.19 of the Stacks Project, [Tag 09DF](https://stacks.math.columbia.edu/tag/09DF). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09DG, an equation

[Tag 09DG](https://stacks.math.columbia.edu/tag/09DG) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean, line 1178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean#L1178). The attribute's comment: “the sequence for a term of the standard resolution”. References: SGA 6 II (AppII.1.2.4), “n = 1”.

> **The sequence of principal parts is a short exact sequence.**

```lean
theorem exists_shortExact_principalPartsSequence' :
    ∃ h : (principalPartsInclusion.{v, u, w, m} φ).app F ≫
        (principalPartsProjection.{v, u, w, m}
          (underlyingRingSheafMapOfSite φ) 1).app F = 0,
      (ShortComplex.mk ((principalPartsInclusion.{v, u, w, m} φ).app F)
        ((principalPartsProjection.{v, u, w, m}
          (underlyingRingSheafMapOfSite φ) 1).app F) h).ShortExact
```

**`CategoryTheory.Sheaf.resolutionPrincipalPartsShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean#L148).

> **Stacks 09DG.** The extension of principal parts of a term of the standard resolution is
> short exact: `0 ⟶ Ω_{P_n/A} ⊗_{P_n} F ⟶ P¹_{P_n/A}(F) ⟶ F ⟶ 0`.

```lean
theorem resolutionPrincipalPartsShortComplex_shortExact (n : SimplexCategoryᵒᵖ)
    (F : targetModules J B) :
    (resolutionPrincipalPartsShortComplex J f n F).ShortExact
```

## Tag 09DH, an equation

[Tag 09DH](https://stacks.math.columbia.edu/tag/09DH) in the Stacks Project.

**`CategoryTheory.Sheaf.sheafAtiyahTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean#L287). The attribute's comment: “the distinguished triangle `L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ ⟶ Lπ_!(P¹_{𝒫/𝒜}(ℱ)) ⟶ ℱ ⟶ (L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ)[1]` in `D(ℬ)`, for any homomorphism of sheaves of commutative rings on a site and any sheaf of `ℬ`-modules, with the outer terms identified by the constructed isomorphisms `atiyahTriangleFirstTermIso` and `atiyahTriangleThirdTermIso`”.

> **[Stacks, Tag 09DH], Equation 92.19.0.2.** For a homomorphism `f : 𝒜 ⟶ ℬ` of sheaves of
> commutative rings on a site and a sheaf of `ℬ`-modules `ℱ`,
>
> `L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ ⟶ Lπ_!(P¹_{𝒫/π^{-1}𝒜}(ℱ)) ⟶ ℱ ⟶ (L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ)[1]`
>
> is a distinguished triangle in `D(ℬ)`.

```lean
theorem sheafAtiyahTriangle_distinguished (F : SheafOfModules.{u} (targetRing J (B := B))) :
    sheafAtiyahTriangle J f F ∈ distinguishedTriangles
```

## Tag 09DI, a definition

[Tag 09DI](https://stacks.math.columbia.edu/tag/09DI) in the Stacks Project.

**`CategoryTheory.Sheaf.atiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean, line 276](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean#L276). The attribute's comment: “the Atiyah class `ℱ ⟶ (L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ)[1]` of a sheaf of `ℬ`-modules, the last arrow of the triangle of Tag 09DH, for any homomorphism of sheaves of commutative rings on a site”.

> **[Stacks, Tag 09DI], Definition 92.19.1: the Atiyah class of a sheaf of modules.** For a
> homomorphism `f : 𝒜 ⟶ ℬ` of sheaves of commutative rings on a site and a sheaf of `ℬ`-modules `ℱ`,
> the *Atiyah class* of `ℱ` is the morphism
>
> `ℱ ⟶ (L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ)[1]`
>
> of `D(ℬ)`, the last arrow of the triangle (92.19.0.2) of [Stacks, Tag 09DH]. It is
> `atiyahClassOfIso` at the library's constructions: the functor `Lπ_!` of Tag 09D3
> (`CategoryTheory.Sheaf.resolutionLowerShriek`), the short exact sequence of first principal parts
> of the standard resolution as simplicial `P_•`-modules
> (`CategoryTheory.Sheaf.simplicialPrincipalPartsShortComplex_shortExact`, Tag 09DG), and the
> identifications of the outer terms with `L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ` and `ℱ`
> (`CategoryTheory.Sheaf.atiyahTriangleFirstTermIso` and
> `CategoryTheory.Sheaf.atiyahTriangleThirdTermIso`).

```lean
def atiyahClass (F : SheafOfModules.{u} (targetRing J (B := B))) :
    DerivedCategory.Q.obj
        ((HomologicalComplex.single (SheafOfModules.{u} (targetRing J (B := B)))
          (ComplexShape.up ℤ) 0).obj F) ⟶
      (((derivedTensorProductFunctor B).obj
          (DerivedCategory.Q.obj (cotangentComplex.{u, u, u} J f))).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single (Stacks.DerivedTensor.RingedSite.Modules B)
            (ComplexShape.up ℤ) 0).obj F)))⟦(1 : ℤ)⟧
```

**`CategoryTheory.Sheaf.sheafAtiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean#L254).

> **[Stacks, Tag 09DI], Definition 92.19.1: the Atiyah class of a sheaf of modules.** For a
> homomorphism `f : 𝒜 ⟶ ℬ` of sheaves of commutative rings on a site and a sheaf of `ℬ`-modules `ℱ`,
> the *Atiyah class* of `ℱ` is the morphism
>
> `ℱ ⟶ (L_{ℬ/𝒜} ⊗^𝐋_ℬ ℱ)[1]`
>
> of `D(ℬ)` which is the last arrow of the triangle (92.19.0.2) of [Stacks, Tag 09DH]: the image
> under the `Lπ_!` of Remark 09D3 of the short exact sequence of first principal parts of the
> standard resolution (Tag 09DG), read through the identifications
> `CategoryTheory.Sheaf.atiyahTriangleFirstTermIso` and
> `CategoryTheory.Sheaf.atiyahTriangleThirdTermIso` of its outer terms.

```lean
def sheafAtiyahClass (F : SheafOfModules.{u} (targetRing J (B := B))) :
    DerivedCategory.Q.obj
        ((HomologicalComplex.single (SheafOfModules.{u} (targetRing J (B := B)))
          (ComplexShape.up ℤ) 0).obj F) ⟶
      (((derivedTensorProductFunctor B).obj
          (DerivedCategory.Q.obj (cotangentComplex.{u, u, u} J f))).obj
        (DerivedCategory.Q.obj
          ((HomologicalComplex.single (Stacks.DerivedTensor.RingedSite.Modules B)
            (ComplexShape.up ℤ) 0).obj F)))⟦(1 : ℤ)⟧
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 92.19, Tag 09DF](https://stacks.math.columbia.edu/tag/09DF)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
