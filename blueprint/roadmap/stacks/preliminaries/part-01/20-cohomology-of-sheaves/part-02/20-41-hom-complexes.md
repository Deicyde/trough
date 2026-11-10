---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.sheafHomComplex, Stacks.SheafOfModules.sheafHomComplexHomologyEquiv, Stacks.SheafOfModules.sheafHomComplexHomologyEquivHomotopyCategory, Stacks.Cohomology.SheafHomComplexCurrying.sheafHomTensorIsoConstruction, AlgebraicGeometry.RingedSite.compositionConstruction, Stacks.SheafOfModules.diagonalBetterConstruction, Stacks.SheafOfModules.diagonalBetter_natural_left, Stacks.SheafOfModules.diagonalBetter_natural_right
statement: formalized
proof: formalized
---

# 20.41 Hom complexes

Section 20.41 of the Stacks Project, [Tag 0A8K](https://stacks.math.columbia.edu/tag/0A8K). 10 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0A8K, the section

[Tag 0A8K](https://stacks.math.columbia.edu/tag/0A8K) in the Stacks Project.

**`Stacks.SheafOfModules.sheafHomComplex`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexQuasiIso.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexQuasiIso.lean#L121).

> **Stacks 0A8K.** The internal Hom complex `SheafHom•(K, I)` of two complexes of
> `O_X`-modules on a ringed space: in degree `n` its sections over an open `U` are the degree-`n`
> cochains from `K|_U` to `I|_U`, that is the product over the pairs `p + n = q` of the sections
> of `SheafHom(K^p, I^q)`, with the differential `d(f) = d_I ∘ f - (-1)^n f ∘ d_K`.

```lean
abbrev sheafHomComplex (K I : CochainComplex (StructureSheafModules Rc) ℤ) :
    SheafHomComplex Rc K I
```

## Tag 0A8L, an equation

[Tag 0A8L](https://stacks.math.columbia.edu/tag/0A8L) in the Stacks Project.

**`Stacks.SheafOfModules.sheafHomComplexHomologyEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexCohomology.lean, line 99](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexCohomology.lean#L99). The attribute's comment: “H^n(Γ(U, SheafHom^•(L, M))) = Hom_{K(O_U)}(L|_U, M|_U[n]) for every open U of X and every n ∈ ℤ, with SheafHom^•(L, M) the internal Hom complex constructed in Tag 0A8K.”.

> **Stacks 0A8L.** The `n`-th cohomology of the sections over `U` of the internal Hom complex
> `SheafHom^•(L, M)` of [Stacks, Tag 0A8K] is canonically the group of morphisms from `L|_U` to
> `M|_U[n]` in the homotopy category of complexes of `O_U`-modules.

```lean
noncomputable def sheafHomComplexHomologyEquiv (U : Opens X)
    (L M : CochainComplex (StructureSheafModules Rc) ℤ) (n : ℤ) :
    (sectionComplex Rc (sheafHomComplex Rc L M).obj U).homology n ≃+
      ((HomotopyCategory.quotient
          (SheafOfModules.{u} ((structureSheaf Rc).over U))
          (ComplexShape.up ℤ)).obj (restrictComplex Rc L U) ⟶
        (HomotopyCategory.quotient
          (SheafOfModules.{u} ((structureSheaf Rc).over U))
          (ComplexShape.up ℤ)).obj ((restrictComplex Rc M U)⟦n⟧))
```

**`Stacks.SheafOfModules.sheafHomComplexHomologyEquivHomotopyCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/HomotopyCategoryHoms.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/HomotopyCategoryHoms.lean#L55).

> The `n`-th cohomology of the sections over `U` of the internal Hom complex from `L` to `M` is
> canonically the group of morphisms from `L|_U` to `M|_U[n]` in the homotopy category of complexes
> of `O_U`-modules.

```lean
noncomputable def sheafHomComplexHomologyEquivHomotopyCategory
    {X : TopCat.{u}} (Rc : TopCat.Sheaf CommRingCat.{u} X)
    (U : Opens X)
    (L M : CochainComplex (StructureSheafModules Rc) ℤ)
    (H : SheafHomComplex Rc L M) (n : ℤ) :
    (sectionComplex Rc H.obj U).homology n ≃+
      ((HomotopyCategory.quotient
          (SheafOfModules.{u} ((structureSheaf Rc).over U))
          (ComplexShape.up ℤ)).obj (restrictComplex Rc L U) ⟶
        (HomotopyCategory.quotient
          (SheafOfModules.{u} ((structureSheaf Rc).over U))
          (ComplexShape.up ℤ)).obj ((restrictComplex Rc M U)⟦n⟧))
```

## Tag 0A8M, a lemma

[Tag 0A8M](https://stacks.math.columbia.edu/tag/0A8M) in the Stacks Project.

**`Stacks.Cohomology.SheafHomComplexCurrying.sheafHomTensorIsoConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/TensorHomAdjunction.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/TensorHomAdjunction.lean#L385).

> **Stacks 0A8M.** For complexes `K`, `L`, `M` of `O_X`-modules on a ringed space there is an
> isomorphism `SheafHom•(K, SheafHom•(L, M)) ≅ SheafHom•(Tot(K ⊗_{O_X} L), M)` of complexes of
> `O_X`-modules, functorial in `K`, `L` and `M`.

```lean
def sheafHomTensorIsoConstruction : SheafHomTensorIsoConstruction Rc
```

## Tag 0A8N, a lemma

[Tag 0A8N](https://stacks.math.columbia.edu/tag/0A8N) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.compositionConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CompositionMorphism.lean, line 406](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/InternalHom/CompositionMorphism.lean#L406). The attribute's comment: “the ringed space case”.

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

## Tag 0BYR, a lemma

[Tag 0BYR](https://stacks.math.columbia.edu/tag/0BYR) in the Stacks Project.

**`Stacks.SheafOfModules.diagonalBetterConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean, line 283](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean#L283). The attribute's comment: “the canonical morphism”.

> **Stacks 0BYR.** The canonical diagonal morphisms
> `Tot(K ⊗ SheafHom(M, L)) ⟶ SheafHom(M, Tot(K ⊗ L))` for complexes of modules on a ringed
> space, sending a homogeneous local pure tensor `k ⊗ φ` to the internal Hom section
> `m ↦ k ⊗ φ(m)`.

```lean
noncomputable def diagonalBetterConstruction : DiagonalBetterConstruction Rc
```

**`Stacks.SheafOfModules.diagonalBetter_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean#L382). The attribute's comment: “functoriality in the first complex”.

> **Stacks 0BYR.** The canonical diagonal morphism is covariant in the tensor factor.

```lean
theorem diagonalBetter_natural_left
    {K K' : CochainComplex (StructureSheafModules Rc) ℤ}
    (L M : CochainComplex (StructureSheafModules Rc) ℤ) (f : K ⟶ K') :
    diagonalBetter Rc K L M ≫ sheafHomComplexMap Rc (𝟙 M) (tensorTotalMap Rc f (𝟙 L)) =
      tensorTotalMap Rc f (𝟙 (sheafHomComplex Rc M L).obj) ≫ diagonalBetter Rc K' L M
```

**`Stacks.SheafOfModules.diagonalBetter_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean, line 392](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean#L392). The attribute's comment: “functoriality in the second complex”.

> **Stacks 0BYR.** The canonical diagonal morphism is covariant in the target of the
> internal Hom complex.

```lean
theorem diagonalBetter_natural_right
    (K : CochainComplex (StructureSheafModules Rc) ℤ)
    {L L' : CochainComplex (StructureSheafModules Rc) ℤ}
    (M : CochainComplex (StructureSheafModules Rc) ℤ) (g : L ⟶ L') :
    diagonalBetter Rc K L M ≫ sheafHomComplexMap Rc (𝟙 M) (tensorTotalMap Rc (𝟙 K) g) =
      tensorTotalMap Rc (𝟙 K) (sheafHomComplexMap Rc (𝟙 M) g) ≫ diagonalBetter Rc K L' M
```

**`Stacks.SheafOfModules.diagonalBetter_natural_hom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorSheafHom.lean#L403). The attribute's comment: “functoriality in the third complex”.

> **Stacks 0BYR.** The canonical diagonal morphism is contravariant in the source of the
> internal Hom complex.

```lean
theorem diagonalBetter_natural_hom
    (K L : CochainComplex (StructureSheafModules Rc) ℤ)
    {M M' : CochainComplex (StructureSheafModules Rc) ℤ} (h : M' ⟶ M) :
    diagonalBetter Rc K L M ≫ sheafHomComplexMap Rc h (𝟙 (tensorTotal Rc K L)) =
      tensorTotalMap Rc (𝟙 K) (sheafHomComplexMap Rc h (𝟙 L)) ≫ diagonalBetter Rc K L M'
```

## Tag 0A8Q, a lemma

[Tag 0A8Q](https://stacks.math.columbia.edu/tag/0A8Q) in the Stacks Project.

**`Stacks.SheafOfModules.diagonalTensorHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean, line 573](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean#L573). The attribute's comment: “canonical diagonal morphism”.

> The diagonal morphism sends a homogeneous section `k` of `K` to the homogeneous map
> `l ↦ k ⊗ l` from `L` to the total tensor product.

```lean
noncomputable def diagonalTensorHom
    (K L : CochainComplex (StructureSheafModules Rc) ℤ) :
    K ⟶ (sheafHomComplex Rc L (tensorTotal Rc K L)).obj
```

**`Stacks.SheafOfModules.diagonalTensorHom_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean, line 581](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean#L581). The attribute's comment: “canonical characterization”.

> On local sections, the diagonal morphism is inclusion of the pure tensor in the
> appropriate summand of the total complex.

```lean
theorem diagonalTensorHom_apply
    (K L : CochainComplex (StructureSheafModules Rc) ℤ) (U : Opens X)
    (n p : ℤ) (k : (K.X n).val.obj (op U))
    (l : (L.X p).val.obj (op U)) :
    applyHomSection Rc (sheafHomComplex Rc L (tensorTotal Rc K L))
        U n p (n + p) (by omega)
        (((diagonalTensorHom Rc K L).f n).val.app (op U) k) l =
      tensorTotalSection Rc K L U n p k l
```

**`Stacks.SheafOfModules.diagonalTensorHom_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/DiagonalTensorHom.lean#L627). The attribute's comment: “functoriality in both complexes”.

> The diagonal morphism is natural in `K` and dinatural in `L`.

```lean
theorem diagonalTensorHom_natural
    {K K' L L' : CochainComplex (StructureSheafModules Rc) ℤ}
    (f : K ⟶ K') (g : L ⟶ L') :
    diagonalTensorHom Rc K L ≫
        sheafHomComplexMap Rc (𝟙 L) (tensorTotalMap Rc f g) =
      f ≫ diagonalTensorHom Rc K' L' ≫
        sheafHomComplexMap Rc g (𝟙 (tensorTotal Rc K' L'))
```

## Tag 0A8P, a lemma

[Tag 0A8P](https://stacks.math.columbia.edu/tag/0A8P) in the Stacks Project.

**`Stacks.SheafOfModules.evaluationConstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/TensorTotalEvaluation.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/TensorTotalEvaluation.lean#L65). The attribute's comment: “canonical evaluation morphism”.

> **Stacks 0A8P.** The canonical evaluation morphisms for internal Hom complexes of modules
> on a ringed space, specified on homogeneous local pure tensors by the signed formula
> `φ ⊗ k ↦ (-1)^(r + (-a) * r) (ψ ↦ φ (ψ k))`. It is the evaluation morphism of the ringed site
> of opens of the space.

```lean
noncomputable def evaluationConstruction : EvaluationConstruction Rc
```

**`Stacks.SheafOfModules.evaluateAndMore_natural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/TensorTotalEvaluation.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHomEvaluation/TensorTotalEvaluation.lean#L80). The attribute's comment: “functoriality in all three complexes”.

> **Stacks 0A8P.** Evaluation is covariant in `K` and `M` and contravariant in `L`.

```lean
theorem evaluateAndMore_natural
    {K K' L L' M M' : CochainComplex (StructureSheafModules Rc) ℤ}
    (k : K ⟶ K') (l : L' ⟶ L) (m : M ⟶ M') :
    tensorTotalMap Rc (sheafHomComplexMap Rc l m) k ≫
        evaluateAndMore Rc K' L' M' =
      evaluateAndMore Rc K L M ≫
        sheafHomComplexMap Rc (sheafHomComplexMap Rc k l) m
```

## Tag 0A8R, a lemma

[Tag 0A8R](https://stacks.math.columbia.edu/tag/0A8R) in the Stacks Project.

**`Stacks.SheafOfModules.sheafHomComplexHomologyEquivDerivedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategoryHoms.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategoryHoms.lean#L118).

> **Stacks 0A8R.** If `I` is K-injective, degree-zero cohomology over `U` of the internal
> Hom complex from `L` to `I` is canonically the group of derived morphisms between the objects
> represented by their restrictions to the open subspace `U`.

```lean
noncomputable def sheafHomComplexHomologyEquivDerivedCategory
    {X : TopCat.{u}} (Rc : TopCat.Sheaf CommRingCat.{u} X) (U : Opens X)
    (L I : CochainComplex (StructureSheafModules Rc) ℤ) [I.IsKInjective]
    (H : SheafHomComplex Rc L I)
    (LU MU : DerivedCategory
      (SheafOfModules.{u} (resRing U (structureSheaf Rc))))
    (eL : DerivedCategory.Qh.obj
      ((HomotopyCategory.quotient _ _).obj
        (restrictComplexToSubspace (structureSheaf Rc) U L)) ≅ LU)
    (eM : DerivedCategory.Qh.obj
      ((HomotopyCategory.quotient _ _).obj
        ((restrictComplexToSubspace (structureSheaf Rc) U I)⟦(0 : ℤ)⟧)) ≅ MU) :
    (sectionComplex Rc H.obj U).homology 0 ≃+
      (LU ⟶ MU)
```

**`Stacks.SheafOfModules.sheafHomComplexHomologyEquivDerivedCategory_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategoryHoms.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/DerivedCategoryHoms.lean#L161). The attribute's comment: “canonical comparison on section classes”.

> **Stacks 0A8R.** The canonical identification sends a section cohomology class first to its
> homotopy-class morphism, transports that morphism from the slice-site model to the
> open-subspace model, and then localizes it. In particular this fixes its value on the identity
> class and its behaviour under changing the two representatives.

```lean
theorem sheafHomComplexHomologyEquivDerivedCategory_apply
    {X : TopCat.{u}} (Rc : TopCat.Sheaf CommRingCat.{u} X) (U : Opens X)
    (L I : CochainComplex (StructureSheafModules Rc) ℤ) [I.IsKInjective]
    (H : SheafHomComplex Rc L I)
    (LU MU : DerivedCategory
      (SheafOfModules.{u} (resRing U (structureSheaf Rc))))
    (eL : DerivedCategory.Qh.obj
      ((HomotopyCategory.quotient _ _).obj
        (restrictComplexToSubspace (structureSheaf Rc) U L)) ≅ LU)
    (eM : DerivedCategory.Qh.obj
      ((HomotopyCategory.quotient _ _).obj
        ((restrictComplexToSubspace (structureSheaf Rc) U I)⟦(0 : ℤ)⟧)) ≅ MU)
    (z : (sectionComplex Rc H.obj U).homology 0) :
    sheafHomComplexHomologyEquivDerivedCategory Rc U L I H LU MU eL eM z =
      (let E := U.sheafOfModulesEquivOver (structureSheaf Rc)
            let Fh := E.functor.mapHomotopyCategory (ComplexShape.up ℤ)
       let K := restrictComplex Rc L U
       let J := (restrictComplex Rc I U)⟦(0 : ℤ)⟧
       let eK := (E.functor.mapHomotopyCategoryFactors (ComplexShape.up ℤ)).app K ≪≫
         (HomotopyCategory.quotient _ _).mapIso
           (eqToIso (mapHomologicalComplex_restrictComplex Rc U L))
       let eJ := (E.functor.mapHomotopyCategoryFactors (ComplexShape.up ℤ)).app J ≪≫
         (HomotopyCategory.quotient _ _).mapIso
           (eqToIso (mapHomologicalComplex_restrictComplex_shiftZero Rc U I))
       eL.inv ≫ DerivedCategory.Qh.map
         (eK.inv ≫ Fh.map
           (sheafHomComplexHomologyEquivHomotopyCategory
             Rc U L I H 0 z) ≫ eJ.hom) ≫ eM.hom)
```

## Tag 0A8S, a lemma

[Tag 0A8S](https://stacks.math.columbia.edu/tag/0A8S) in the Stacks Project.

**`Stacks.SheafOfModules.sheafHomComplexMap_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexQuasiIso.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/HomComplexAndStrictPerfection/InternalHomComplexQuasiIso.lean#L158).

> **Stacks 0A8S.** A quasi-isomorphism between K-injective complexes, together with a
> quasi-isomorphism in the contravariant variable, induces a quasi-isomorphism between the
> corresponding canonical internal Hom complexes. This is what makes the derived internal Hom
> of complexes of `O_X`-modules well defined.

```lean
theorem sheafHomComplexMap_quasiIso
    {I' I L' L : CochainComplex (StructureSheafModules Rc) ℤ}
    (i : I' ⟶ I) [QuasiIso i] [I'.IsKInjective] [I.IsKInjective]
    (l : L' ⟶ L) [QuasiIso l] :
    QuasiIso (sheafHomComplexMap Rc l i)
```

## Tag 0A8T, a lemma

[Tag 0A8T](https://stacks.math.columbia.edu/tag/0A8T) in the Stacks Project.

**`Stacks.SheafOfModules.isKInjective_sheafHomComplex_of_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/KFlatIntoKInjective.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/InternalHom/KFlatIntoKInjective.lean#L45).

> The internal Hom complex `SheafHom^•(L, I)` from a K-flat complex `L` of `O_X`-modules into a
> K-injective complex `I` of `O_X`-modules is K-injective.

```lean
theorem isKInjective_sheafHomComplex_of_isKFlat
    (L I : CochainComplex (StructureSheafModules Rc) ℤ)
    (hL : IsKFlat Rc L) [I.IsKInjective] :
    (sheafHomComplex Rc L I).obj.IsKInjective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.41, Tag 0A8K](https://stacks.math.columbia.edu/tag/0A8K)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
