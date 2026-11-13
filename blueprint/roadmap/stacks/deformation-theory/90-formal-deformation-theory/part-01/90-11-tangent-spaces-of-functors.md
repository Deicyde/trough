---
declaration: section
origin: cited
lean: CategoryTheory.Functor.Additive, CategoryTheory.Functor.Linear, CategoryTheory.Functor.mapLinearMap, preservesFiniteProductsOfAdditive, map_isZero, fgModuleCat_linearFunctorLift_unique, Deformation.linearFunctorLift_unique, Deformation.fgModuleCat_linearFunctorLift_unique
statement: formalized
proof: formalized
---

# 90.11 Tangent spaces of functors

Section 90.11 of the Stacks Project, [Tag 06I2](https://stacks.math.columbia.edu/tag/06I2). 14 tags here are carried by 39 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06I3, a definition

[Tag 06I3](https://stacks.math.columbia.edu/tag/06I3) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.Additive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Additive#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch90.lean#L17) (StacksFrontier): “additivity on Hom\_R(M, N)”. References: EGA III (7.2.6); SGA 4 XVII (1.1.11); SGA 4 XVII (2.2.13.1); SGA 4½ Etat 0 (1.3.3), “partial”; SGA 5 V (2.3.4); SGA 6 I (1.1.3), “partial”.
- [`CategoryTheory.Functor.Linear`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.Linear#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch90.lean#L18) (StacksFrontier): “R-homogeneity: L(r • f) = r • L(f)”. References: EGA III (7.1.2).
- [`CategoryTheory.Functor.mapLinearMap`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.mapLinearMap#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch90.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch90.lean#L19) (StacksFrontier): “L on Hom\_R(M, N) as a map of R-modules”.

## Tag 06I5, a remark

[Tag 06I5](https://stacks.math.columbia.edu/tag/06I5) in the Stacks Project.

Declarations registered for the tag:

- [`preservesFiniteProductsOfAdditive`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preservesFiniteProductsOfAdditive#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 675](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L675) (StacksFrontier): “preservation of finite products”.
- [`map_isZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=map_isZero#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 677](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L677) (StacksFrontier): “zero modules are sent to zero modules”.
- [`fgModuleCat_linearFunctorLift_unique`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=fgModuleCat_linearFunctorLift_unique#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 679](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L679) (StacksFrontier): “unique linear lift”.

## Tag 06I6, a lemma

[Tag 06I6](https://stacks.math.columbia.edu/tag/06I6) in the Stacks Project.

**`Deformation.linearFunctorLift_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L613). The attribute's comment: “arbitrary linear source category”.

> **Stacks Project, Tag 06I6, general source category.** A finite-product-preserving
> set-valued functor on any preadditive `R`-linear category with a terminal object, binary
> products and a zero object has a unique `R`-linear lift to `R`-modules. The two cases of the
> source are the instances of this for the category of all modules and for the category of
> finitely generated ones; it is also what applies to the full subcategories of the module
> category that arise as the domain of a tangent functor.

```lean
theorem linearFunctorLift_unique
    (R : Type uR) [CommRing R]
    {C : Type uC} [Category.{vC} C] [Preadditive C] [Linear R C]
    [HasTerminal C] [HasBinaryProducts C] [HasZeroObject C]
    (F : C ⥤ Type uM) [PreservesFiniteProducts F] :
    Nonempty (Unique (LinearFunctorLift R F))
```

**`Deformation.fgModuleCat_linearFunctorLift_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L634). The attribute's comment: “finitely generated modules”.

> **Stacks Project, Tag 06I6, finitely generated case.** A finite-product-preserving
> set-valued functor on finitely generated `R`-modules which takes the zero module to a singleton
> has a unique `R`-linear lift to `R`-modules.

```lean
theorem fgModuleCat_linearFunctorLift_unique
    (R : Type uR) [CommRing R] (F : FGModuleCat.{vM} R ⥤ Type uM)
    [PreservesFiniteProducts F] [Unique (F.obj (FGModuleCat.of R PUnit))] :
    Nonempty (Unique (LinearFunctorLift R F))
```

**`Deformation.moduleCat_linearFunctorLift_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 654](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L654). The attribute's comment: “all modules”.

> **Stacks Project, Tag 06I6, unrestricted case.** A finite-product-preserving set-valued
> functor on `R`-modules which takes the zero module to a singleton has a unique `R`-linear lift
> to `R`-modules.

```lean
theorem moduleCat_linearFunctorLift_unique
    (R : Type uR) [CommRing R] (F : ModuleCat.{vM} R ⥤ Type uM)
    [PreservesFiniteProducts F] [Unique (F.obj (ModuleCat.of R PUnit))] :
    Nonempty (Unique (LinearFunctorLift R F))
```

## Tag 06I7, a lemma

[Tag 06I7](https://stacks.math.columbia.edu/tag/06I7) in the Stacks Project.

**`Deformation.fgModuleCat_linearFunctorLift_natTrans`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 746](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L746).

> **Stacks Project, Tag 06I7.** A natural transformation between product-preserving
> set-valued functors on finitely generated modules uniquely lifts to a natural transformation
> between their canonical linear lifts. Its underlying natural transformation is the original
> one.

```lean
theorem fgModuleCat_linearFunctorLift_natTrans
    (R : Type uR) [CommRing R]
    (F G : FGModuleCat.{vM} R ⥤ Type uM)
    [PreservesFiniteProducts F] [Unique (F.obj (FGModuleCat.of R PUnit))]
    [PreservesFiniteProducts G] [Unique (G.obj (FGModuleCat.of R PUnit))]
    (t : F ⟶ G) :
    ∃! τ : (fgModuleCatLinearFunctorLift R F).functor ⟶
        (fgModuleCatLinearFunctorLift R G).functor,
      Functor.whiskerRight τ (forget (ModuleCat.{uM} R)) =
        eqToHom (fgModuleCatLinearFunctorLift R F).forget_comp ≫
          t ≫
            eqToHom (fgModuleCatLinearFunctorLift R G).forget_comp.symm
```

## Tag 06I8, a lemma

[Tag 06I8](https://stacks.math.columbia.edu/tag/06I8) in the Stacks Project.

**`Deformation.linearFunctor_iso_tensorLeft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean, line 910](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/LinearFunctor.lean#L910).

> **Stacks Project, Tag 06I8.** A linear functor from finite-dimensional vector spaces over
> a field to vector spaces is naturally isomorphic to tensoring with its value on the ground
> field.

```lean
theorem linearFunctor_iso_tensorLeft (K : Type u) [Field K]
    (L : FGModuleCat.{u} K ⥤ ModuleCat.{u} K) [L.Additive] [L.Linear K] :
    Nonempty
      (((forget₂ (FGModuleCat.{u} K) (ModuleCat.{u} K)) ⋙
          MonoidalCategory.tensorLeft (L.obj (FGModuleCat.of K K))) ≅ L)
```

## Tag 06I9, a lemma

[Tag 06I9](https://stacks.math.columbia.edu/tag/06I9) in the Stacks Project.

**`Deformation.trivSqZeroExtFunctor_preservesFiniteProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L179). References: SGA 7 VI (1.3(c)), “more general”.

> The trivial square-zero extension functor from `R`-modules to
> `S`-algebras over `R` preserves finite products.

```lean
theorem trivSqZeroExtFunctor_preservesFiniteProducts :
    PreservesFiniteProducts (trivSqZeroExtFunctor S R)
```

## Tag 06IA, a lemma

[Tag 06IA](https://stacks.math.columbia.edu/tag/06IA) in the Stacks Project.

**`Deformation.tangentSpaceModuleStructure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L345). References: SGA 3 XI (1.9), “partial”.

> **Stacks Project, Tag 06IA.** A set-valued functor on a strictly full
> subcategory of `S`-algebras over `R` which takes the zero square-zero extension
> and products of square-zero extensions to the corresponding products of sets
> has a natural `R`-linear module-valued lift on all finitely generated
> `R`-modules.

```lean
noncomputable def tangentSpaceModuleStructure
    (P : ObjectProperty (Over (CommAlgCat.of S R))) [P.IsClosedUnderIsomorphisms]
    (hP : ∀ M : FGModuleCat.{u} R, P ((squareZeroExtensionFunctor S R).obj M))
    (F : P.FullSubcategory ⥤ Type v)
    (hF : TangentSpaceFunctorConditions S R P hP F) :
    LinearFunctorLift R (tangentSpaceSetFunctor S R P hP F)
```

## Tag 06IB, a definition

[Tag 06IB](https://stacks.math.columbia.edu/tag/06IB) in the Stacks Project.

**`Deformation.TangentSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 429](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L429). References: SGA 7 VI (1.15), “special case”.

> **Stacks Project, Tag 06IB.** The tangent space of a set-valued functor is its value on the
> dual numbers.

```lean
abbrev TangentSpace
    (P : ObjectProperty (Over (CommAlgCat.of S R)))
    (hε : P (dualNumbersOver S R))
    (F : P.FullSubcategory ⥤ Type w) : Type w
```

## Tag 06SR, an example

[Tag 06SR](https://stacks.math.columbia.edu/tag/06SR) in the Stacks Project.

**`Deformation.artinianTangentSpace`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L625). The attribute's comment: “Definition 06IB applied to the category of augmented Artinian local algebras”.

> The tangent space of a functor on `𝒞_Λ`, through its canonical augmented-algebra model.

```lean
noncomputable abbrev artinianTangentSpace
    (F : ArtinianLocalAlgCat.{s, u, u} Λ k ⥤ Type w) : Type w
```

**`Deformation.artinianTangentSpace_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 633](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L633). The attribute's comment: “Definition 06IB applied to the category of augmented Artinian local algebras”.

> Evaluation on the Artinian square-zero object agrees with the Over-model tangent space.

```lean
theorem artinianTangentSpace_eq
    (F : ArtinianLocalAlgCat.{s, u, u} Λ k ⥤ Type w) :
    artinianTangentSpace Λ k F =
      F.obj ((artinianSquareZeroExtensionFunctor Λ k).obj (FGModuleCat.of k k))
```

## Tag 06IC, an example

[Tag 06IC](https://stacks.math.columbia.edu/tag/06IC) in the Stacks Project.

**`Deformation.isProrepresentable_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Predeformation/ProrepresentableLimits.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Predeformation/ProrepresentableLimits.lean#L201). The attribute's comment: “prorepresentable\_preserves\_limits”.

> **Stacks Project, Tag 06IC.** A prorepresentable functor on Artinian local
> `Λ`-algebras preserves finite limits.

```lean
theorem isProrepresentable_preservesFiniteLimits
    (F : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type v) (hF : IsProrepresentable F) :
    PreservesFiniteLimits F
```

**`Deformation.tangentSpaceDerivationsLinearEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 146](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L146). The attribute's comment: “the bijection TF = Der\_Λ(S, k), f ↦ f - q”.

> A tangent vector corresponds to the downlifted square-zero component: the bijection is
> `f ↦ f - q`.

```lean
theorem tangentSpaceDerivationsLinearEquiv_apply
    (S : CompleteLocalAlgCat.{u, max v w, w} Λ k)
    (f : tangentSpaceArtinian Λ k (restrictedCoyoneda S)) (s : S) :
    letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
    tangentSpaceDerivationsLinearEquiv S f s = (f.hom s).snd.down
```

**`Deformation.tangentSpaceDerivationsLinearEquiv_precomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L179). The attribute's comment: “the bijection TF = Der\_Λ(S, k), f ↦ f - q”.

> The identification commutes with precomposition by morphisms of representing
> algebras.

```lean
theorem tangentSpaceDerivationsLinearEquiv_precomp
    (T S : CompleteLocalAlgCat.{u, max v w, w} Λ k) (g : T ⟶ S)
    (f : tangentSpaceArtinian Λ k (restrictedCoyoneda S)) (t : T) :
    tangentSpaceDerivationsLinearEquiv T (g ≫ f) t =
      tangentSpaceDerivationsLinearEquiv S f (g.hom t)
```

**`Deformation.prorepresented_tangentSpaceFunctorConditions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L346). The attribute's comment: “the prorepresented functor satisfies the hypotheses of Lemma 06IA”.

> **Stacks Project, Tag 06IC.** The functor prorepresented by `S` satisfies the hypotheses
> of Lemma 06IA: its value on `k[0] = k` is a singleton and it takes `k[M × N]` to the product
> of its values on `k[M]` and `k[N]`.

```lean
theorem prorepresented_tangentSpaceFunctorConditions :
    TangentSpaceFunctorConditions Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
```

**`Deformation.tangentSpaceModuleStructureDerivationsLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 426](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L426). The attribute's comment: “F(k[V]) = Der\_Λ(S, V) as vector spaces, for the canonical structure of 06IA”.

> **Stacks Project, Tag 06IC.** For the functor `F` prorepresented by `S` and a
> finite-dimensional `k`-vector space `V`, the bijection `F(k[V]) = Der_Λ(S, V)`,
> `f ↦ f - q`, is `k`-linear for the canonical module structure on `F(k[V])` of Lemma 06IA
> (the one coming from `F` preserving finite products), so it is a `k`-linear equivalence.

```lean
noncomputable def tangentSpaceModuleStructureDerivationsLinearEquiv (V : FGModuleCat.{w} k) :
    (tangentSpaceModuleStructure Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
      (prorepresented_tangentSpaceFunctorConditions S)).functor.obj V ≃ₗ[k]
        Derivation Λ S V
```

**`Deformation.tangentSpaceModuleStructureDerivationsLinearEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L449). The attribute's comment: “F(k[V]) = Der\_Λ(S, V) as vector spaces, for the canonical structure of 06IA”.

> The linear equivalence is the bijection `f ↦ f - q`: it sends `f` to its square-zero
> component.

```lean
theorem tangentSpaceModuleStructureDerivationsLinearEquiv_apply (V : FGModuleCat.{w} k)
    (x : (tangentSpaceModuleStructure Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
      (prorepresented_tangentSpaceFunctorConditions S)).functor.obj V) (s : S) :
    tangentSpaceModuleStructureDerivationsLinearEquiv S V x s =
      ((cast (tangentSpaceModuleStructure_prorepresented_carrier S V) x).hom s).snd
```

**`Deformation.tangentSpaceModuleStructureRankOneDerivationsLinearEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 491](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L491). The attribute's comment: “TF = Der\_Λ(S, k) as vector spaces, for the canonical structure of 06IA/06IB”.

> **Stacks Project, Tag 06IC.** For the functor `F` prorepresented by `S`, the tangent space
> `TF = F(k[ε]) = Der_Λ(S, k)`, and the `k`-vector space structure on `TF` of Lemma 06IA and
> Definition 06IB (the canonical one, coming from `F` preserving finite products) corresponds
> to the one on `Der_Λ(S, k)`: the bijection `f ↦ f - q` is a `k`-linear equivalence.

```lean
noncomputable def tangentSpaceModuleStructureRankOneDerivationsLinearEquiv :
    letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
    (tangentSpaceModuleStructure Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
      (prorepresented_tangentSpaceFunctorConditions S)).functor.obj (FGModuleCat.of k k) ≃ₗ[k]
        Derivation Λ S k
```

**`Deformation.tangentSpaceModuleStructureRankOneDerivationsLinearEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 503](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L503). The attribute's comment: “TF = Der\_Λ(S, k) as vector spaces, for the canonical structure of 06IA/06IB”.

> The identification sends a tangent vector `f : S → k[ε]` to its `ε`-component.

```lean
theorem tangentSpaceModuleStructureRankOneDerivationsLinearEquiv_apply
    (x : (tangentSpaceModuleStructure Λ k (artinianLocalOver Λ k)
      (squareZeroExtension_mem_artinianLocalOver Λ k)
      (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
      (prorepresented_tangentSpaceFunctorConditions S)).functor.obj (FGModuleCat.of k k))
    (s : S) :
    letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
    tangentSpaceModuleStructureRankOneDerivationsLinearEquiv S x s =
      ((cast (tangentSpaceModuleStructure_prorepresented_carrier_rankOne S) x).hom s).snd
```

**`Deformation.tangentSpaceModuleStructure_prorepresented_finiteDimensional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Derivations.lean, line 518](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L518). The attribute's comment: “dim\_k TF < ∞ for the canonical structure of 06IA/06IB”.

> **Stacks Project, Tag 06IC.** The tangent space of a prorepresentable functor, with its
> canonical vector space structure of Lemma 06IA and Definition 06IB, is finite-dimensional
> (by Lemma 06SC), under the chapter's standing assumption that `Λ → k` is finite.

```lean
theorem tangentSpaceModuleStructure_prorepresented_finiteDimensional [Module.Finite Λ k] :
    FiniteDimensional k
      ((tangentSpaceModuleStructure Λ k (artinianLocalOver Λ k)
        (squareZeroExtension_mem_artinianLocalOver Λ k)
        (artinianLocalOverToArtinian Λ k ⋙ restrictedCoyoneda S)
        (prorepresented_tangentSpaceFunctorConditions S)).functor.obj (FGModuleCat.of k k))
```

**`Deformation.squareZeroPointsDerivationsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L219). The attribute's comment: “square\_zero\_points\_derivations”.

```lean
noncomputable def squareZeroPointsDerivationsEquiv
    (S : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V] :
    SquareZeroPoint S V ≃ Derivations S V
```

**`Deformation.squareZeroPointsDerivationsEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L227). The attribute's comment: “square\_zero\_points\_derivations”.

> In the forward identification, the derivation associated to `f` is the square-zero
> component of `f`, i.e. `s ↦ f(s) - q(s)`.

```lean
theorem squareZeroPointsDerivationsEquiv_apply
    (S : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (f : SquareZeroPoint S V) (s : S) :
    squareZeroPointsDerivationsEquiv S V f s = (f.1 s).snd
```

**`Deformation.squareZeroPointsDerivationsEquiv_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L236). The attribute's comment: “square\_zero\_points\_derivations”.

> In the inverse identification, a derivation `D` is sent to the map
> `s ↦ q(s) + D(s)` into `k[V]`.

```lean
theorem squareZeroPointsDerivationsEquiv_symm_apply
    (S : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (D : Derivations S V) (s : S) :
    ((squareZeroPointsDerivationsEquiv S V).symm D).1 s =
      (residueHom S s, D s)
```

**`Deformation.squareZeroPointsDerivationsEquiv_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L245). The attribute's comment: “square\_zero\_points\_derivations”.

> The canonical identification is functorial in the finite-dimensional vector space.

```lean
theorem squareZeroPointsDerivationsEquiv_naturality
    (S : CompleteLocalAlgCat.{u, v, w} Λ k)
    {V : Type x} {W : Type y} [AddCommGroup V] [Module k V]
    [AddCommGroup W] [Module k W] (l : V →ₗ[k] W)
    (f : SquareZeroPoint S V) (s : S) :
    squareZeroPointsDerivationsEquiv S W (f.map S l) s =
      l (squareZeroPointsDerivationsEquiv S V f s)
```

**`Deformation.squareZeroPointsDerivationsEquiv_precomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 258](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L258). The attribute's comment: “square\_zero\_points\_derivations”.

> The canonical identification is natural under precomposition in the representing
> complete local algebra.

```lean
theorem squareZeroPointsDerivationsEquiv_precomp
    (S : CompleteLocalAlgCat.{u, v, w} Λ k)
    (T : CompleteLocalAlgCat.{u, y, w} Λ k)
    (g : T →ₐ[Λ] S) (hg : (residueHom S).comp g = residueHom T)
    (V : Type x) [AddCommGroup V] [Module k V]
    (f : SquareZeroPoint S V) (t : T) :
    squareZeroPointsDerivationsEquiv T V (f.precomp S T g hg V) t =
      squareZeroPointsDerivationsEquiv S V f (g t)
```

**`Deformation.squareZeroExtensionObject`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 360](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L360). The attribute's comment: “square\_zero\_points\_derivations”.

> A finite-dimensional trivial square-zero extension, as an object of the category
> of complete local `Λ`-algebras, with its algebra coordinates and residue augmentation.

```lean
noncomputable def squareZeroExtensionObject
    (V : Type x) [AddCommGroup V] [Module k V] [FiniteDimensional k V] :
    { A : CompleteLocalAlgCat.{u, max w x, w} Λ k //
      ∃ e : A ≃+* TrivSqZeroExt k V,
        (∀ r : Λ, e (algebraMap Λ A r) = (algebraMap Λ k r, 0)) ∧
        (∀ a : A, (e a).fst = residueHom A a) }
```

**`Deformation.squareZeroPointsDerivationsEquivHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L431). The attribute's comment: “square\_zero\_points\_derivations”.

> The identification for the actual morphism type of the category of complete local
> `Λ`-algebras. The equivalence `e` identifies the chosen object `A` with `k[V]`, and
> `he` says that its residue map is the square-zero augmentation.

```lean
noncomputable def squareZeroPointsDerivationsEquivHom
    (S A : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (e : A ≃+* TrivSqZeroExt k V)
    (hΛ : ∀ r : Λ, e (algebraMap Λ A r) = (algebraMap Λ k r, 0))
    (he : ∀ a : A, (e a).fst = residueHom A a) :
    (S ⟶ A) ≃ Derivations S V
```

**`Deformation.squareZeroPointsDerivationsEquivHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 444](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L444). The attribute's comment: “square\_zero\_points\_derivations”.

> A categorical morphism `f : S ⟶ k[V]` determines the derivation given by its
> square-zero component.

```lean
theorem squareZeroPointsDerivationsEquivHom_apply
    (S A : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (e : A ≃+* TrivSqZeroExt k V)
    (hΛ : ∀ r : Λ, e (algebraMap Λ A r) = (algebraMap Λ k r, 0))
    (he : ∀ a : A, (e a).fst = residueHom A a)
    (f : S ⟶ A) (s : S) :
    squareZeroPointsDerivationsEquivHom S A V e hΛ he f s =
      (e (f.hom s)).snd
```

**`Deformation.squareZeroPointsDerivationsEquivHom_symm_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 458](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L458). The attribute's comment: “square\_zero\_points\_derivations”.

> Conversely, the categorical morphism determined by `D` is `s ↦ q(s) + D(s)`
> in square-zero coordinates.

```lean
theorem squareZeroPointsDerivationsEquivHom_symm_apply
    (S A : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (e : A ≃+* TrivSqZeroExt k V)
    (hΛ : ∀ r : Λ, e (algebraMap Λ A r) = (algebraMap Λ k r, 0))
    (he : ∀ a : A, (e a).fst = residueHom A a)
    (D : Derivations S V) (s : S) :
    e (((squareZeroPointsDerivationsEquivHom S A V e hΛ he).symm D).hom s) =
      (residueHom S s, D s)
```

**`Deformation.squareZeroPointsDerivationsEquivHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L476). The attribute's comment: “square\_zero\_points\_derivations”.

> The categorical identification commutes with maps between square-zero extensions.

```lean
theorem squareZeroPointsDerivationsEquivHom_naturality
    (S A B : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) (W : Type y)
    [AddCommGroup V] [Module k V] [AddCommGroup W] [Module k W]
    (eA : A ≃+* TrivSqZeroExt k V)
    (hΛA : ∀ r : Λ, eA (algebraMap Λ A r) = (algebraMap Λ k r, 0))
    (heA : ∀ a : A, (eA a).fst = residueHom A a)
    (eB : B ≃+* TrivSqZeroExt k W)
    (hΛB : ∀ r : Λ, eB (algebraMap Λ B r) = (algebraMap Λ k r, 0))
    (heB : ∀ b : B, (eB b).fst = residueHom B b)
    (g : A ⟶ B) (l : V →ₗ[k] W)
    (hg : ∀ a : A, (eB (g.hom a)).snd = l (eA a).snd)
    (f : S ⟶ A) (s : S) :
    squareZeroPointsDerivationsEquivHom S B W eB hΛB heB (f ≫ g) s =
      l (squareZeroPointsDerivationsEquivHom S A V eA hΛA heA f s)
```

**`Deformation.squareZeroPointsDerivationsEquivHom_precomp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/SquareZero.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L497). The attribute's comment: “square\_zero\_points\_derivations”.

> The categorical identification is natural in the representing algebra.

```lean
theorem squareZeroPointsDerivationsEquivHom_precomp
    (T S A : CompleteLocalAlgCat.{u, v, w} Λ k)
    (V : Type x) [AddCommGroup V] [Module k V]
    (e : A ≃+* TrivSqZeroExt k V)
    (hΛ : ∀ r : Λ, e (algebraMap Λ A r) = (algebraMap Λ k r, 0))
    (he : ∀ a : A, (e a).fst = residueHom A a)
    (g : T ⟶ S) (f : S ⟶ A) (t : T) :
    squareZeroPointsDerivationsEquivHom T A V e hΛ he (g ≫ f) t =
      squareZeroPointsDerivationsEquivHom S A V e hΛ he f (g.hom t)
```

## Tag 06SS, an example

[Tag 06SS](https://stacks.math.columbia.edu/tag/06SS) in the Stacks Project.

**`Deformation.existsUnique_derivationRelativeCotangentDualEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean#L274). The attribute's comment: “derivations are the dual of the relative cotangent space”. References: SGA 3 VIIA (1.3.1), “special case”.

> **Stacks 06SS.** For a base `Λ` whose residue field `k₀` has `k` separable over it, the
> `Λ`-derivations from an object `S` of `\widehat{𝒞_Λ}` to `k` are the `k`-linear dual of the
> relative cotangent space of `S` over `Λ`, by the unique `k`-linear equivalence that restricts
> a derivation to the maximal ideal of `S`.

```lean
theorem existsUnique_derivationRelativeCotangentDualEquiv
    {k₀ : Type*} [Field k₀] [Algebra Λ k₀] [Algebra k₀ k] [IsScalarTower Λ k₀ k]
    [IsLocalRing Λ] [Algebra.IsSeparable k₀ k]
    (hbase : Function.Surjective (algebraMap Λ k₀))
    (S : CompleteLocalAlgCat.{u, v, w} Λ k) :
    ∃ hlocal : IsLocalHom (algebraMap Λ S),
      letI := hlocal
      letI : Module k (relativeCotangentSpace (algebraMap Λ S)) :=
        Module.compHom _ S.residueEquiv.symm.toRingHom
      letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
      ∃! e : Derivation Λ S k ≃ₗ[k]
          (relativeCotangentSpace (algebraMap Λ S) →ₗ[k] k),
        ∀ (D : Derivation Λ S k) (x : IsLocalRing.maximalIdeal S),
          e D (Submodule.Quotient.mk x) = D (x : S)
```

**`Deformation.existsUnique_tangentSpaceRelativeCotangentDualEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean#L342). The attribute's comment: “the tangent space is the relative tangent space”.

> **Stacks 06SS.** The tangent space of the functor prorepresented by `S` is the relative
> tangent space of `S` over `Λ`, that is the `k`-linear dual of the relative cotangent space.
> The equivalence is characterized by taking the coefficient of the square-zero coordinate of
> the image of an element of the maximal ideal, and is unique with that property.

```lean
theorem existsUnique_tangentSpaceRelativeCotangentDualEquiv
    {k₀ : Type*} [Field k₀] [Algebra Λ k₀] [Algebra k₀ k] [IsScalarTower Λ k₀ k]
    [IsLocalRing Λ] [Algebra.IsSeparable k₀ k]
    (hbase : Function.Surjective (algebraMap Λ k₀))
    (S : CompleteLocalAlgCat.{u, max v w, w} Λ k) :
    ∃ hlocal : IsLocalHom (algebraMap Λ S),
      letI := hlocal
      letI : Module k (relativeCotangentSpace (algebraMap Λ S)) :=
        Module.compHom _ S.residueEquiv.symm.toRingHom
      ∃! e : tangentSpaceArtinian Λ k (restrictedCoyoneda S) ≃ₗ[k]
          (relativeCotangentSpace (algebraMap Λ S) →ₗ[k] k),
        ∀ (t : tangentSpaceArtinian Λ k (restrictedCoyoneda S))
          (x : IsLocalRing.maximalIdeal S),
          e t (Submodule.Quotient.mk x) = (t.hom (x : S)).snd.down
```

**`Deformation.existsUnique_tangentSpaceRelativeCotangentDualEquiv_of_isClassical`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean, line 377](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/RelativeCotangentDual.lean#L377). The attribute's comment: “classical case”.

> **Stacks 06SS.** The classical case: when `Λ` is a Noetherian complete local ring with
> residue field `k`, the tangent space of the functor prorepresented by `S` is the `k`-linear
> dual of the relative cotangent space of `S` over `Λ`. Separability is automatic here, the
> residue extension being trivial.

```lean
theorem existsUnique_tangentSpaceRelativeCotangentDualEquiv_of_isClassical
    (hΛ : IsClassical Λ k) (S : CompleteLocalAlgCat.{u, max v w, w} Λ k) :
    letI : IsLocalRing Λ := (Classical.choose hΛ).isLocal
    ∃ hlocal : IsLocalHom (algebraMap Λ S),
      letI := hlocal
      letI : Module k (relativeCotangentSpace (algebraMap Λ S)) :=
        Module.compHom _ S.residueEquiv.symm.toRingHom
      ∃! e : tangentSpaceArtinian Λ k (restrictedCoyoneda S) ≃ₗ[k]
          (relativeCotangentSpace (algebraMap Λ S) →ₗ[k] k),
        ∀ (t : tangentSpaceArtinian Λ k (restrictedCoyoneda S))
          (x : IsLocalRing.maximalIdeal S),
          e t (Submodule.Quotient.mk x) = (t.hom (x : S)).snd.down
```

## Tag 06ID, a lemma

[Tag 06ID](https://stacks.math.columbia.edu/tag/06ID) in the Stacks Project.

**`Deformation.naturalTransformation_linearMapOnSquareZeroExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 686](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L686).

> **Stacks Project, Tag 06ID.** A natural transformation between functors
> satisfying the tangent-space hypotheses is `R`-linear on every trivial
> square-zero extension `R[M]`, with respect to the natural module structures of
> Tag 06IA.  The case `M = R` is the induced linear map on tangent spaces.

```lean
theorem naturalTransformation_linearMapOnSquareZeroExtensions
    (P : ObjectProperty (Over (CommAlgCat.of S R))) [P.IsClosedUnderIsomorphisms]
    (hP : ∀ M : FGModuleCat.{u} R,
      P ((squareZeroExtensionFunctor S R).obj M))
    (F G : P.FullSubcategory ⥤ Type v)
    (hF : TangentSpaceFunctorConditions S R P hP F)
    (hG : TangentSpaceFunctorConditions S R P hP G)
    (t : F ⟶ G) (M : FGModuleCat.{u} R) :
    let LF := tangentSpaceModuleStructure S R P hP F hF
    let LG := tangentSpaceModuleStructure S R P hP G hG
    let eF := congrArg (fun H : FGModuleCat.{u} R ⥤ Type v ↦ H.obj M) LF.forget_comp
    let eG := congrArg (fun H : FGModuleCat.{u} R ⥤ Type v ↦ H.obj M) LG.forget_comp
    ∃ l : LF.functor.obj M ⟶ LG.functor.obj M, ∀ x : LF.functor.obj M,
      cast eG (l x) =
        t.app ((squareZeroExtensionRestriction S R P hP).obj M) (cast eF x)
```

## Tag 06ST, an example

[Tag 06ST](https://stacks.math.columbia.edu/tag/06ST) in the Stacks Project.

**`Deformation.tangentSpaceMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L60). The attribute's comment: “linear tangent map”.

> The `k`-linear map on tangent spaces induced contravariantly by a morphism `f : R ⟶ S` of
> complete local `Λ`-algebras, written on derivation spaces: it sends a `Λ`-derivation `S → k` to
> its restriction along `f`.

```lean
noncomputable def tangentSpaceMap
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S) :
    letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
    letI : Algebra R k := (residueHom R).toRingHom.toAlgebra
    Derivation Λ S k →ₗ[k] Derivation Λ R k
```

**`Deformation.tangentSpaceMap_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 76](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L76). The attribute's comment: “action on derivations”.

> Under the canonical identification of the tangent space with a space of derivations, the
> induced tangent map is precomposition with the morphism of representing algebras.

```lean
theorem tangentSpaceMap_apply
    {R S : CompleteLocalAlgCat.{u, v, w} Λ k} (f : R ⟶ S)
    (d : letI : Algebra S k := (residueHom S).toRingHom.toAlgebra
      Derivation Λ S k) (r : R) :
    tangentSpaceMap f d r = d (f.hom r)
```

**`Deformation.tangentSpaceMapArtinian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L86). The attribute's comment: “linear tangent map on Artinian tangent spaces”.

> The induced map on the tangent spaces themselves, the values of the two restricted
> representable functors at the dual numbers: `tangentSpaceMap` transported along the canonical
> identification with derivation spaces.

```lean
noncomputable def tangentSpaceMapArtinian
    {R S : CompleteLocalAlgCat.{u, max v w, w} Λ k} (f : R ⟶ S) :
    tangentSpaceArtinian Λ k (restrictedCoyoneda S) →ₗ[k]
      tangentSpaceArtinian Λ k (restrictedCoyoneda R)
```

**`Deformation.tangentSpaceMapArtinian_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L96). The attribute's comment: “action on Artinian tangent vectors”.

> On a tangent vector, that is on a `k[ε]`-point of the functor represented by `S`, the
> induced tangent map is precomposition with the morphism of representing algebras.

```lean
theorem tangentSpaceMapArtinian_apply
    {R S : CompleteLocalAlgCat.{u, max v w, w} Λ k} (f : R ⟶ S)
    (x : tangentSpaceArtinian Λ k (restrictedCoyoneda S)) :
    tangentSpaceMapArtinian f x = f ≫ x
```

Declarations registered for the tag:

- [`Deformation.restrictedCoyonedaMap`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RestrictedRepresentable.lean#L48), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L47) (StacksFrontier): “the transformation of functors induced by a map of representing algebras”.
- [`Deformation.squareZeroPointsDerivationsEquiv_precomp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/SquareZero.lean#L258), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L50) (StacksFrontier): “naturality of the square-zero-point description of the tangent space”.
- [`Deformation.tangentSpaceDerivationsLinearEquiv_precomp`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Derivations.lean#L179), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/TangentSpace/FunctorMap.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/FunctorMap.lean#L53) (StacksFrontier): “naturality of the identification of the tangent space with derivations”.

## Tag 06IE, a lemma

[Tag 06IE](https://stacks.math.columbia.edu/tag/06IE) in the Stacks Project.

**`Deformation.tangentSpaceFunctor_iso_tensorLeft`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/TangentSpace/Functor.lean, line 740](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/TangentSpace/Functor.lean#L740).

> **Stacks Project, Tag 06IE.** Over a field, the functor
> `V ↦ F(K[V])`, with its natural linear structure, is naturally isomorphic
> to tensoring `V` with the tangent space `F(K[ε])`.

```lean
theorem tangentSpaceFunctor_iso_tensorLeft
    (S : Type s) (K : Type u) [CommRing S] [Field K] [Algebra S K]
    (P : ObjectProperty (Over (CommAlgCat.of S K)))
    [P.IsClosedUnderIsomorphisms]
    (hP : ∀ V : FGModuleCat.{u} K,
      P ((squareZeroExtensionFunctor S K).obj V))
    (F : P.FullSubcategory ⥤ Type u)
    (hF : TangentSpaceFunctorConditions S K P hP F) :
    let L := (tangentSpaceModuleStructure S K P hP F hF).functor
    Nonempty
      (L ≅
        (forget₂ (FGModuleCat.{u} K) (ModuleCat.{u} K) ⋙
          MonoidalCategory.tensorLeft (L.obj (FGModuleCat.of K K))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.11, Tag 06I2](https://stacks.math.columbia.edu/tag/06I2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
