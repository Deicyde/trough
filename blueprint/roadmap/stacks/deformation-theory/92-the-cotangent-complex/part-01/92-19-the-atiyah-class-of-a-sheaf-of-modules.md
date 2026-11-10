---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence', CategoryTheory.Sheaf.resolutionPrincipalPartsShortComplex_shortExact, CategoryTheory.Sheaf.atiyahTriangle_distinguished_of_iso, CategoryTheory.Sheaf.sheafAtiyahTriangle_distinguished, CategoryTheory.Sheaf.atiyahClass, CategoryTheory.Sheaf.sheafAtiyahClass
statement: formalized
proof: formalized
---

# 92.19 The Atiyah class of a sheaf of modules

Section 92.19 of the Stacks Project, [Tag 09DF](https://stacks.math.columbia.edu/tag/09DF). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09DG, an equation

[Tag 09DG](https://stacks.math.columbia.edu/tag/09DG) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.exists_shortExact_principalPartsSequence'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean, line 1178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/PrincipalPartsJet.lean#L1178). The attribute's comment: “the sequence for a term of the standard resolution”. References: SGA 6 II (AppII.1.2.4), “n = 1”.

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

**`CategoryTheory.Sheaf.resolutionPrincipalPartsShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean#L134).

> **Stacks 09DG.** The extension of principal parts of a term of the standard resolution is
> short exact: `0 ⟶ Ω_{P_n/A} ⊗_{P_n} F ⟶ P¹_{P_n/A}(F) ⟶ F ⟶ 0`.

```lean
theorem resolutionPrincipalPartsShortComplex_shortExact (n : SimplexCategoryᵒᵖ)
    (F : targetModules J B) :
    (resolutionPrincipalPartsShortComplex J f n F).ShortExact
```

## Tag 09DH, an equation

[Tag 09DH](https://stacks.math.columbia.edu/tag/09DH) in the Stacks Project.

**`CategoryTheory.Sheaf.atiyahTriangle_distinguished_of_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean#L194). The attribute's comment: “the distinguished triangle; `M`, `G`, `hS`, `e₁` and `e₃` carry the inputs the library does not yet have — the category of simplicial `P_•`-modules known to be abelian, the functor Lπ\_! of Tag 09D3, the simplicial short exact sequence of Tag 09DG, and the identifications of Tags 08PU and 08QE. See the implementation notes”.

> **Stacks 09DH.** The Atiyah triangle of a sheaf of `B`-modules, written with its first and
> third terms replaced by objects identified with them: for `L` identified with
> `Lπ_!(Ω_{P_•/A} ⊗_{P_•} F)` and `N` identified with `Lπ_!(F)`, the sequence
> `L ⟶ Lπ_!(P¹_{P_•/A}(F)) ⟶ N ⟶ L[1]` is a distinguished triangle in `D(B)`.

```lean
theorem atiyahTriangle_distinguished_of_iso
    (G : DerivedCategory M ⥤ DerivedCategory (targetModules J B))
    [G.CommShift ℤ] [G.IsTriangulated] {S : ShortComplex M} (hS : S.ShortExact)
    (L N : DerivedCategory (targetModules J B))
    (e₁ : (atiyahTriangle J G hS).obj₁ ≅ L) (e₃ : (atiyahTriangle J G hS).obj₃ ≅ N) :
    Triangle.mk (e₁.inv ≫ (atiyahTriangle J G hS).mor₁)
        ((atiyahTriangle J G hS).mor₂ ≫ e₃.hom)
        (e₃.inv ≫ (atiyahTriangle J G hS).mor₃ ≫
          (shiftFunctor (DerivedCategory (targetModules J B)) (1 : ℤ)).map e₁.hom) ∈
      distinguishedTriangles
```

**`CategoryTheory.Sheaf.sheafAtiyahTriangle_distinguished`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean#L280).

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

**`CategoryTheory.Sheaf.atiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClass.lean#L214). The attribute's comment: “the Atiyah class, as the last arrow of the triangle of Tag 09DH; `M`, `G`, `hS`, `e₁` and `e₃` carry the same five inputs the library does not yet have that `atiyahTriangle_distinguished_of_iso` carries, so `N` stands for `F` and `L` for `L_{B/A} ⊗_B^L F`. See the implementation notes”.

> **Stacks 09DI.** The *Atiyah class* of a sheaf of `B`-modules: the map
> `F ⟶ L_{B/A} ⊗_B^L F[1]`, realised as the last arrow `N ⟶ L[1]` of the Atiyah triangle of
> Tag 09DH, read through the identifications of its first and third terms.

```lean
def atiyahClass (G : DerivedCategory M ⥤ DerivedCategory (targetModules J B))
    [G.CommShift ℤ] [G.IsTriangulated] {S : ShortComplex M} (hS : S.ShortExact)
    (L N : DerivedCategory (targetModules J B))
    (e₁ : (atiyahTriangle J G hS).obj₁ ≅ L) (e₃ : (atiyahTriangle J G hS).obj₃ ≅ N) :
    N ⟶ L⟦(1 : ℤ)⟧
```

**`CategoryTheory.Sheaf.sheafAtiyahClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean, line 250](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Cotangent/SheavesOfRings/AtiyahClassDefinite.lean#L250).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
