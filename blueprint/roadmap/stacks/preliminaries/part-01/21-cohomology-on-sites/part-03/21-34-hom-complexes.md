---
declaration: section
origin: cited
lean: AlgebraicGeometry.RingedSite.sheafHomComplex, AlgebraicGeometry.RingedSite.sheafHomComplexSectionHomologyEquivHomotopyCategory, AlgebraicGeometry.RingedSite.sheafHomComplexHomologyEquivHomotopyCategory, AlgebraicGeometry.RingedSite.sheafHomTensorIsoConstruction, AlgebraicGeometry.RingedSite.sheafHomTensorCurryIso, AlgebraicGeometry.RingedSite.compositionConstruction, Stacks.Cohomology.compositionConstruction, AlgebraicGeometry.RingedSite.tensorHomInterchangeConstruction
statement: formalized
proof: formalized
---

# 21.34 Hom complexes

Section 21.34 of the Stacks Project, [Tag 0A8X](https://stacks.math.columbia.edu/tag/0A8X). 11 tags here are carried by 22 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A8X, the section

[Tag 0A8X](https://stacks.math.columbia.edu/tag/0A8X) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.sheafHomComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean, line 931](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean#L931).

> The canonical internal sheaf Hom complex `SheafHom•(L, M)`: in degree `n` its sections over
> an object `U` are the degree-`n` cochains from `L|_U` to `M|_U`, that is the product over the
> pairs `p + n = q` of the sections of `SheafHom(L^p, M^q)`, with the differential
> `d(f) = d_M ∘ f - (-1)^n f ∘ d_L`, together with its description on every slice site and the
> compatibility of these descriptions.

```lean
noncomputable def sheafHomComplex (X : RingedSite.{u, v, w})
    (L M : CochainComplex (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
        SheafHomComplex X L M
```

## Tag 0A8Y, an equation

[Tag 0A8Y](https://stacks.math.columbia.edu/tag/0A8Y) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.sheafHomComplexSectionHomologyEquivHomotopyCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean, line 1045](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean#L1045).

> The `n`-th cohomology of the sections over `U` of the internal Hom complex from `L` to `M`
> is the group of morphisms `L|_U ⟶ M|_U[n]` in the homotopy category of `O|_U`-modules.

```lean
def sheafHomComplexSectionHomologyEquivHomotopyCategory
    (X : RingedSite.{u, u, u})
    (L M : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (U : X.C) (n : ℤ) :
    (sectionComplex X (sheafHomComplex X L M).obj U).homology n ≃+
    ((HomotopyCategory.quotient
          (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
          (ComplexShape.up ℤ)).obj
            (restrictComplex X L U) ⟶
        (HomotopyCategory.quotient
          (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
          (ComplexShape.up ℤ)).obj
            ((restrictComplex X M U)⟦n⟧))
```

## Tag 0A8Z, an equation

[Tag 0A8Z](https://stacks.math.columbia.edu/tag/0A8Z) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.sheafHomComplexHomologyEquivHomotopyCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean, line 1023](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/HomComplex.lean#L1023).

> The `n`-th cohomology of the global sections of the internal sheaf Hom complex from `L` to
> `M` is canonically the group of morphisms from `L` to `M[n]` in the homotopy category.

```lean
noncomputable def sheafHomComplexHomologyEquivHomotopyCategory
    (X : RingedSite.{u, v, w})
    (L M : CochainComplex (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (n : ℤ) :
    (globalSectionsComplex X (sheafHomComplex X L M).obj).homology n ≃+
      ((HomotopyCategory.quotient (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ)).obj L ⟶
        (HomotopyCategory.quotient (SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
          (ComplexShape.up ℤ)).obj (M⟦n⟧))
```

## Tag 0A90, a lemma

[Tag 0A90](https://stacks.math.columbia.edu/tag/0A90) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.sheafHomTensorIsoConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CurryingForComplexesOfModules.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CurryingForComplexesOfModules.lean#L153).

> For complexes `K`, `L`, `M` of `O`-modules on a ringed site `(C, O)` there is an isomorphism
> `SheafHom•(K, SheafHom•(L, M)) ≅ SheafHom•(Tot(K ⊗_O L), M)` of complexes of `O`-modules,
> functorial in `K`, `L` and `M`.

```lean
def sheafHomTensorIsoConstruction : SheafHomTensorIsoConstruction X
```

**`AlgebraicGeometry.RingedSite.sheafHomTensorCurryIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CurryingIsomorphism.lean, line 736](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CurryingIsomorphism.lean#L736). The attribute's comment: “the currying isomorphism”.

> **Stacks 0A90.** The canonical currying isomorphism of internal Hom complexes on a ringed
> site: `SheafHom(K, SheafHom(L, M)) ≅ SheafHom(Tot(K ⊗_O L), M)`.

```lean
def sheafHomTensorCurryIso :
    (sheafHomComplex X K (sheafHomComplex X L M).obj).obj ≅
      (sheafHomComplex X (((Stacks.SheafOfModules.Tensor.tensorComplex X.O).obj K).obj L) M).obj
```

## Tag 0A91, a lemma

[Tag 0A91](https://stacks.math.columbia.edu/tag/0A91) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.compositionConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CompositionMorphism.lean, line 406](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CompositionMorphism.lean#L406).

> **Stacks 0A91.** For complexes `K`, `L`, `M` of modules on a ringed site there is a
> canonical morphism of complexes of `O`-modules
>
> `Tot(SheafHom(L, M) ⊗_O SheafHom(K, L)) ⟶ SheafHom(K, M)`,
>
> namely the one sending each homogeneous local pure tensor to the composite of its two factors,
> with no extra sign.
>
> A ringed space is a ringed site, namely the site of its opens with the open-cover topology, so
> this also gives the composition morphism for complexes of modules on a ringed space.

```lean
noncomputable def compositionConstruction : CompositionConstruction X
```

**`Stacks.Cohomology.compositionConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexComposition.lean, line 601](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexComposition.lean#L601).

> The canonical composition of internal Hom complexes of module sheaves.

```lean
noncomputable def compositionConstruction : CompositionConstruction X
```

## Tag 0BYT, a lemma

[Tag 0BYT](https://stacks.math.columbia.edu/tag/0BYT) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.tensorHomInterchangeConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/TensorHomInterchange.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/TensorHomInterchange.lean#L189). The attribute's comment: “the canonical morphism”.

> **Stacks 0BYT.** For complexes `K`, `L`, `M` of modules on a ringed site there is a
> canonical morphism of complexes of `O`-modules
>
> `Tot(K ⊗_O SheafHom(M, L)) ⟶ SheafHom(M, Tot(K ⊗_O L))`,
>
> namely the one sending each homogeneous local pure tensor `x ⊗ φ` to the local section
> `m ↦ x ⊗ φ(m)`.

```lean
noncomputable def tensorHomInterchangeConstruction : TensorHomInterchangeConstruction X
```

**`AlgebraicGeometry.RingedSite.tensorHomInterchange_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/TensorHomInterchange.lean, line 203](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/TensorHomInterchange.lean#L203). The attribute's comment: “functoriality in all three complexes”.

> **Stacks 0BYT.** The interchange morphism is functorial in all three complexes at once:
> covariant in the tensor factor `K` and in the target `L` of the internal Hom, contravariant in
> its source `M`.

```lean
theorem tensorHomInterchange_natural (f : K ⟶ K') (g : L ⟶ L') (h : M' ⟶ M) :
    tensorHomInterchange X K L M ≫ homMap X h (tensorTotalMap X f g) =
      tensorTotalMap X f (homMap X h g) ≫ tensorHomInterchange X K' L' M'
```

## Tag 0A93, a lemma

[Tag 0A93](https://stacks.math.columbia.edu/tag/0A93) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.diagonalConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DiagonalMorphism.lean, line 619](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DiagonalMorphism.lean#L619). The attribute's comment: “canonical diagonal morphism”.

> **Stacks 0A93.** For complexes `K`, `L` of modules on a ringed site there is a canonical
> morphism of complexes of `O`-modules
>
> `K ⟶ SheafHom(L, Tot(K ⊗_O L))`,
>
> namely the one sending each homogeneous local section `k` of `K` to the local section
> `l ↦ k ⊗ l` of the internal Hom complex.

```lean
noncomputable def diagonalConstruction : DiagonalConstruction X
```

**`AlgebraicGeometry.RingedSite.diagonalMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DiagonalMorphism.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/DiagonalMorphism.lean#L632). The attribute's comment: “functoriality in both complexes”.

> **Stacks 0A93.** The diagonal morphism is natural in `K` and dinatural in `L`: a morphism
> `g : L ⟶ L'` acts covariantly inside the tensor product and contravariantly in the source of
> the internal Hom.

```lean
theorem diagonalMap_natural (f : K ⟶ K') (g : L ⟶ L') :
    diagonalMap X K L ≫ homMap X (𝟙 L) (tensorTotalMap X f g) =
      f ≫ diagonalMap X K' L' ≫ homMap X g (𝟙 (tensorTotal X K' L'))
```

## Tag 0A92, a lemma

[Tag 0A92](https://stacks.math.columbia.edu/tag/0A92) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.evaluationConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationMorphism.lean, line 403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationMorphism.lean#L403). The attribute's comment: “canonical evaluation morphism”.

> **Stacks 0A92.** For complexes `K`, `L`, `M` of modules on a ringed site there is a
> canonical morphism of complexes of `O`-modules
>
> `Tot(SheafHom(L, M) ⊗_O K) ⟶ SheafHom(SheafHom(K, L), M)`,
>
> namely the one sending each homogeneous local pure tensor `φ ⊗ k` to the local section taking
> `ψ` to `φ(ψ(k))`, with the Koszul sign.

```lean
noncomputable def evaluationConstruction : EvaluationConstruction X
```

**`AlgebraicGeometry.RingedSite.evaluationMap_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationMorphism.lean, line 531](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/EvaluationMorphism.lean#L531). The attribute's comment: “functoriality in all three complexes”.

> **Stacks 0A92.** The evaluation morphism is natural in `K`, contranatural in `L` and
> natural in `M`.

```lean
theorem evaluationMap_natural (k : K ⟶ K') (l : L' ⟶ L) (m : M ⟶ M') :
    tensorTotalMap X (homMap X l m) k ≫ evaluationMap X K' L' M' =
      evaluationMap X K L M ≫ homMap X (homMap X k l) m
```

**`Stacks.Cohomology.evaluationConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexEvaluation/EvaluationMorphism.lean, line 443](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexEvaluation/EvaluationMorphism.lean#L443). The attribute's comment: “canonical evaluation morphism”.

> The canonical evaluation morphism for every three complexes of modules.

```lean
noncomputable def evaluationConstruction : EvaluationConstruction X
```

**`Stacks.Cohomology.evaluation_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexEvaluation/EvaluationMorphism.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexEvaluation/EvaluationMorphism.lean#L455). The attribute's comment: “functoriality in all three complexes”.

> Evaluation is natural in `K`, contranatural in `L`, and natural in `M`.

```lean
theorem evaluation_natural
    {K K' L L' M M' : CochainComplex (SheafOfModules.{u}
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (k : K ⟶ K') (l : L' ⟶ L) (m : M ⟶ M') :
    tensorTotalMap X (sheafHomComplexMap X l m) k ≫
        evaluation X K' L' M' =
      evaluation X K L M ≫
        sheafHomComplexMap X (sheafHomComplexMap X k l) m
```

## Tag 0A94, a lemma

[Tag 0A94](https://stacks.math.columbia.edu/tag/0A94) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.sheafHomGlobalHomologyEquivDerivedCategoryHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalHomNaturality.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/GlobalHomNaturality.lean#L270). The attribute's comment: “global sections, naturality”.

> **Stacks 0A94, global sections, naturality.** The identification of the degree-zero
> cohomology of the global sections of `SheafHom(L, I)` with `Hom_{D(O)}(L, I)` is natural in both
> variables: `homMap k m`, for `k : L' ⟶ L` and `m : I ⟶ I'`, acts on it by precomposition with `k`
> and postcomposition with `m` in the derived category.
>
> This is the global companion of
> `AlgebraicGeometry.RingedSite.sheafHomSectionHomologyEquivDerivedCategoryHom_naturality`, and it
> is what a consumer identifying two such bijections of morphism groups needs.

```lean
theorem sheafHomGlobalHomologyEquivDerivedCategoryHom_naturality
    {L L' I I' : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    [I.IsKInjective] [I'.IsKInjective] (k : L' ⟶ L) (m : I ⟶ I')
    (η : (globalSectionsComplex X (sheafHomComplex X L I).obj).homology 0) :
    sheafHomGlobalHomologyEquivDerivedCategoryHom X L' I'
        (HomologicalComplex.homologyMap (globalSectionsComplexMap X (homMap X k m)) 0 η) =
      DerivedCategory.Q.map k ≫ sheafHomGlobalHomologyEquivDerivedCategoryHom X L I η ≫
        DerivedCategory.Q.map m
```

**`AlgebraicGeometry.RingedSite.sheafHomSectionHomologyEquivDerivedCategoryHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean, line 179](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean#L179). The attribute's comment: “sections over an object”.

> **Stacks 0A94, sections over an object.** If `I` is K-injective then the degree-zero
> cohomology of the sections over `U` of the internal Hom complex from `L` to `I` is the group of
> morphisms `L|_U ⟶ I|_U` in the derived category of `O|_U`-modules.
>
> This is Stacks 0A8Y in degree `0` followed by the identification of homotopy-category with
> derived-category morphisms into a K-injective target; the restriction `I|_U` is K-injective by
> Stacks 08FI.

```lean
noncomputable def sheafHomSectionHomologyEquivDerivedCategoryHom
    (X : RingedSite.{u, u, u})
    (L I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    [I.IsKInjective] (U : X.C) :
    (sectionComplex X (sheafHomComplex X L I).obj U).homology 0 ≃+
      (DerivedCategory.Q.obj (restrictComplex X L U) ⟶
        DerivedCategory.Q.obj (restrictComplex X I U))
```

**`AlgebraicGeometry.RingedSite.sheafHomGlobalHomologyEquivDerivedCategoryHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean#L204). The attribute's comment: “global sections”.

> **Stacks 0A94, global sections.** If `I` is K-injective then the degree-zero cohomology of
> the global sections of the internal Hom complex from `L` to `I` is the group of morphisms
> `L ⟶ I` in the derived category of `O`-modules.
>
> This is Stacks 0A8Z in degree `0` followed by the same identification of homotopy-category with
> derived-category morphisms into a K-injective target.

```lean
noncomputable def sheafHomGlobalHomologyEquivDerivedCategoryHom
    (X : RingedSite.{u, v, r})
    [HasSheafify X.J AddCommGrpCat.{max u v w}]
    [X.J.WEqualsLocallyBijective AddCommGrpCat.{max u v w}]
    (L I : CochainComplex
      (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    [I.IsKInjective] :
    (globalSectionsComplex X (sheafHomComplex X L I).obj).homology 0 ≃+
      (DerivedCategory.Q.obj L ⟶ DerivedCategory.Q.obj I)
```

**`AlgebraicGeometry.RingedSite.sheafHomSectionHomologyEquivDerivedCategoryHom_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/IntoAKInjectiveComplex.lean#L398). The attribute's comment: “sections over an object, naturality”.

> **Stacks 0A94, sections over an object, naturality.** The identification of the degree-zero
> cohomology of the sections over `U` of `SheafHom(L, I)` with `Hom_{D(O|_U)}(L|_U, I|_U)` is
> natural in both variables: `homMap k m`, for `k : L' ⟶ L` and `m : I ⟶ I'`, acts on it by
> precomposition with `k|_U` and postcomposition with `m|_U` in the derived category.

```lean
theorem sheafHomSectionHomologyEquivDerivedCategoryHom_naturality
    {L L' I I' : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    [I.IsKInjective] [I'.IsKInjective] (k : L' ⟶ L) (m : I ⟶ I') (U : X.C)
    (η : (sectionComplex X (sheafHomComplex X L I).obj U).homology 0) :
    sheafHomSectionHomologyEquivDerivedCategoryHom X L' I' U
        (HomologicalComplex.homologyMap (sectionComplexMap X U (homMap X k m)) 0 η) =
      DerivedCategory.Q.map (restrictComplexMap X U k) ≫
        sheafHomSectionHomologyEquivDerivedCategoryHom X L I U η ≫
          DerivedCategory.Q.map (restrictComplexMap X U m)
```

## Tag 0A95, a lemma

[Tag 0A95](https://stacks.math.columbia.edu/tag/0A95) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.homMap_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/QuasiIsoInvariance.lean, line 169](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/QuasiIsoInvariance.lean#L169).

> **Stacks 0A95.** A quasi-isomorphism `l : L' ⟶ L` and a quasi-isomorphism `i : I' ⟶ I`
> between K-injective complexes of `O`-modules induce a quasi-isomorphism
> `SheafHom(L, I') ⟶ SheafHom(L', I)` of internal Hom complexes.
>
> This is what makes the derived internal Hom well defined. The objects of the site need not lie
> in the universe of its morphisms; at `c = u` the extra size conditions above the tag's are
> automatic, which
> is `AlgebraicGeometry.RingedSite.homMap_quasiIso_of_collapsed`.

```lean
theorem homMap_quasiIso (i : I' ⟶ I) [QuasiIso i] [I'.IsKInjective] [I.IsKInjective]
    (l : L' ⟶ L) [QuasiIso l] : QuasiIso (homMap X l i)
```

**`Stacks.Cohomology.InternalHom.sheafHomComplexMap_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexQuasiIso.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/MayerVietorisAndHom/HomComplexQuasiIso.lean#L286).

> Quasi-isomorphisms in both variables, with K-injective complexes in the
> second variable, induce a quasi-isomorphism of internal Hom complexes.

```lean
theorem sheafHomComplexMap_quasiIso
    (X : RingedSite.{u, u, u})
    {I' I L' L : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (i : I' ⟶ I) [QuasiIso i] [I'.IsKInjective] [I.IsKInjective]
    (l : L' ⟶ L) [QuasiIso l] :
    QuasiIso (sheafHomComplexMap X l i)
```

## Tag 0A96, a lemma

[Tag 0A96](https://stacks.math.columbia.edu/tag/0A96) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isKInjective_sheafHomComplex_of_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/KFlatIntoKInjectiveIsKInjective.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/KFlatIntoKInjectiveIsKInjective.lean#L68).

> **Stacks 0A96.** The internal Hom complex `SheafHom(L, I)` from a K-flat complex `L` of
> `O`-modules into a K-injective complex `I` of `O`-modules is K-injective.

```lean
theorem isKInjective_sheafHomComplex_of_isKFlat
    (L I : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (hL : Stacks.SheafOfModules.IsKFlat X.O L) [I.IsKInjective] :
    (sheafHomComplex X L I).obj.IsKInjective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.34, Tag 0A8X](https://stacks.math.columbia.edu/tag/0A8X)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
