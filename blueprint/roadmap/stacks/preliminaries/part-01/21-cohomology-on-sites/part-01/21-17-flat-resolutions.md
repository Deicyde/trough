---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.Tensor.statement1, Stacks.SheafOfModules.Tensor.statement2, Stacks.SheafOfModules.KFlat.KFlat, Stacks.SheafOfModules.IsKFlat, Stacks.SheafOfModules.IsKFlat.tensorRight_preserves_quasiIso, Stacks.SheafOfModules.IsKFlat.tensorLeft_preserves_quasiIso, Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_map_app, Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_obj_map
statement: formalized
proof: formalized
---

# 21.17 Flat resolutions

Section 21.17 of the Stacks Project, [Tag 06YL](https://stacks.math.columbia.edu/tag/06YL). 17 tags here are carried by 51 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06YM, a lemma

[Tag 06YM](https://stacks.math.columbia.edu/tag/06YM) in the Stacks Project.

**`Stacks.SheafOfModules.Tensor.statement1`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean#L58). The attribute's comment: “the functor F ↦ Tot(G ⊗_O F), the fixed complex on the left”. References: SGA 4 XVII (4.1.6), “comm. O, G fixed, left”; SGA 4½ Etat 0 (1.3.3), “special case”.

> **Statement 1.**  Fix a complex `G^•` of `O`-modules.  The functor
> `F^• ↦ Tot(G^• ⊗_O F^•)` on the homotopy category `K(Mod(O))` is an exact functor
> of triangulated categories (Definition 5).
>
> Concretely: there is a functor `Φ : K(Mod(O)) ⥤ K(Mod(O))` together with a
> functorial isomorphism `ξ` (a `CommShift ℤ` structure, incorporating the Koszul
> signs of tag 0FLG) such that
> * `Φ` is additive;
> * `Φ` lifts the complex-level functor `F^• ↦ Tot(G^• ⊗_O F^•)` through the
>   homotopy quotient -- i.e. `quotF ⋙ Φ ≅ leftTensorComplex ⋙ quotF` -- so it is
>   well defined on `K(Mod(O))` (sends homotopic maps to homotopic maps); and
> * `Φ`, equipped with the commutation-with-shift datum `ξ`, is a triangulated
>   functor: it commutes with the shift up to `ξ` and sends distinguished triangles
>   to distinguished triangles.

```lean
theorem statement1
    (G : HomologicalComplex (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ)) :
    ∃ (Φ : HomotopyCategory (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ) ⥤
            HomotopyCategory (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ))
      (ξ : Φ.CommShift ℤ),
      Φ.Additive ∧
        Nonempty (quotF R ⋙ Φ ≅ leftTensorComplex R G ⋙ quotF R) ∧
          (letI := ξ; Φ.IsTriangulated)
```

**`Stacks.SheafOfModules.Tensor.statement2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/BifunctorReductionMachinery/TensorIsTriangulated.lean#L84). The attribute's comment: “the functor F ↦ Tot(F ⊗_O G), the fixed complex on the right”. References: SGA 4 XVII (4.1.6), “comm. O, G fixed, right”; SGA 4½ Etat 0 (1.3.3), “special case”.

> **Statement 2.**  Fix a complex `G^•` of `O`-modules.  The functor
> `F^• ↦ Tot(F^• ⊗_O G^•)` on the homotopy category `K(Mod(O))` is an exact functor
> of triangulated categories (Definition 5).
>
> Concretely: there is a functor `Φ : K(Mod(O)) ⥤ K(Mod(O))` together with a
> functorial isomorphism `ξ` (a `CommShift ℤ` structure, incorporating the Koszul
> signs) such that
> * `Φ` is additive;
> * `Φ` lifts the complex-level functor `F^• ↦ Tot(F^• ⊗_O G^•)` through the
>   homotopy quotient -- i.e. `quotF ⋙ Φ ≅ rightTensorComplex ⋙ quotF`; and
> * `Φ`, equipped with the commutation-with-shift datum `ξ`, is a triangulated
>   functor.

```lean
theorem statement2
    (G : HomologicalComplex (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ)) :
    ∃ (Φ : HomotopyCategory (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ) ⥤
            HomotopyCategory (SheafOfModules (ringSheaf R)) (ComplexShape.up ℤ))
      (ξ : Φ.CommShift ℤ),
      Φ.Additive ∧
        Nonempty (quotF R ⋙ Φ ≅ rightTensorComplex R G ⋙ quotF R) ∧
          (letI := ξ; Φ.IsTriangulated)
```

## Tag 06YN, a definition

[Tag 06YN](https://stacks.math.columbia.edu/tag/06YN) in the Stacks Project.

**`Stacks.SheafOfModules.KFlat.KFlat`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/KFlatComplexesDefinition.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/KFlatComplexesDefinition.lean#L97).

> A cochain complex `K` of sheaves of `O`-modules on a ringed site `(C, O)` is **K-flat**
> when the total tensor complex `Tot(F ⊗_O K)` is acyclic for every acyclic cochain complex `F`
> of sheaves of `O`-modules.

```lean
abbrev KFlat
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ) :
      Prop
```

Declarations registered for the tag:

- [`Stacks.SheafOfModules.IsKFlat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Defs.lean#L66), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/KFlatComplexes.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/KFlatComplexes.lean#L38) (StacksFrontier).

## Tag 06YP, a lemma

[Tag 06YP](https://stacks.math.columbia.edu/tag/06YP) in the Stacks Project.

**`Stacks.SheafOfModules.IsKFlat.tensorRight_preserves_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L204). The attribute's comment: “the K-flat complex as right tensor factor”.

> Tensoring with a K-flat complex on the right and totalising preserves
> quasi-isomorphisms of the homotopy category.

```lean
theorem IsKFlat.tensorRight_preserves_quasiIso
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K) :
    HomotopyCategory.quasiIso
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) (ComplexShape.up ℤ) ≤
      MorphismProperty.inverseImage
        (HomotopyCategory.quasiIso
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) (ComplexShape.up ℤ))
        (Stacks.SheafOfModules.Tensor.Reduction.bifunctorPhiR
          (Stacks.SheafOfModules.Tensor.sheafTensor R) K)
```

**`Stacks.SheafOfModules.IsKFlat.tensorLeft_preserves_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L219). The attribute's comment: “the K-flat complex as left tensor factor”.

> Tensoring with a K-flat complex on the left and totalising preserves
> quasi-isomorphisms of the homotopy category.

```lean
theorem IsKFlat.tensorLeft_preserves_quasiIso
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K) :
    HomotopyCategory.quasiIso
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) (ComplexShape.up ℤ) ≤
      MorphismProperty.inverseImage
        (HomotopyCategory.quasiIso
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) (ComplexShape.up ℤ))
        (Stacks.SheafOfModules.Tensor.Reduction.bifunctorPhi
          (Stacks.SheafOfModules.Tensor.sheafTensor R) K)
```

**`Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_map_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L305). The attribute's comment: “for complexes, the K-flat complex as right tensor factor”.

> For `K` K-flat and `f` a quasi-isomorphism, the total tensor product `Tot(f ⊗ 1_K)` is a
> quasi-isomorphism.

```lean
theorem IsKFlat.quasiIso_tensorComplex_map_app
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K)
    {A B : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : A ⟶ B) (hf : QuasiIso f) :
    QuasiIso (((Stacks.SheafOfModules.Tensor.tensorComplex R).map f).app K)
```

**`Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_obj_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L323). The attribute's comment: “for complexes, the K-flat complex as left tensor factor”.

> For `K` K-flat and `g` a quasi-isomorphism, the total tensor product `Tot(1_K ⊗ g)` is a
> quasi-isomorphism.

```lean
theorem IsKFlat.quasiIso_tensorComplex_obj_map
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K)
    {A B : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (g : A ⟶ B) (hg : QuasiIso g) :
    QuasiIso (((Stacks.SheafOfModules.Tensor.tensorComplex R).obj K).map g)
```

**`Stacks.SheafOfModules.IsKFlat.quasiIso_mapBifunctorMap_id_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L341). The attribute's comment: “for complexes, right tensor factor, mapBifunctorMap spelling”.

> The `HomologicalComplex.mapBifunctorMap` spelling of
> `Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_map_app`.

```lean
theorem IsKFlat.quasiIso_mapBifunctorMap_id_right
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K)
    {A B : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : A ⟶ B) (hf : QuasiIso f) :
    QuasiIso (HomologicalComplex.mapBifunctorMap f (𝟙 K)
      (Stacks.SheafOfModules.Tensor.sheafTensor R) (ComplexShape.up ℤ))
```

**`Stacks.SheafOfModules.IsKFlat.quasiIso_mapBifunctorMap_id_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIso.lean#L354). The attribute's comment: “for complexes, left tensor factor, mapBifunctorMap spelling”.

> The `HomologicalComplex.mapBifunctorMap` spelling of
> `Stacks.SheafOfModules.IsKFlat.quasiIso_tensorComplex_obj_map`.

```lean
theorem IsKFlat.quasiIso_mapBifunctorMap_id_left
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : IsKFlat R K)
    {A B : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (g : A ⟶ B) (hg : QuasiIso g) :
    QuasiIso (HomologicalComplex.mapBifunctorMap (𝟙 K) g
      (Stacks.SheafOfModules.Tensor.sheafTensor R) (ComplexShape.up ℤ))
```

**`Stacks.SheafOfModules.KFlatQuasiIso.quasiIso_tensorComplex_of_KFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIsoOnASite.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorPreservesQuasiIsoOnASite.lean#L102).

> Total tensor product with a K-flat complex preserves quasi-isomorphisms:
> if the maps on every cohomology sheaf are isomorphisms, so are those induced
> by tensoring with `K`.

```lean
theorem quasiIso_tensorComplex_of_KFlat
    (K : CochainComplex (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hK : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K)
    {F G : CochainComplex (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : F ⟶ G)
    (hf : ∀ n, IsIso (ShortComplex.leftHomologyMap
      ((HomologicalComplex.shortComplexFunctor _ (ComplexShape.up ℤ) n).map f))) :
    ∀ n, IsIso (ShortComplex.leftHomologyMap
      ((HomologicalComplex.shortComplexFunctor _ (ComplexShape.up ℤ) n).map
        (((Stacks.SheafOfModules.Tensor.tensorComplex R).map f).app K)))
```

## Tag 0E8K, a lemma

[Tag 0E8K](https://stacks.math.columbia.edu/tag/0E8K) in the Stacks Project.

**`Stacks.DerivedTensor.ExtensionByZero.kFlat_restrictionComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensor.lean, line 281](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensor.lean#L281).

> **Stacks Project, Tag 0E8K.** Let `(C, O)` be a ringed site and let `U` be an object of
> `C`. If `K` is a K-flat complex of `O`-modules, then `K|_U` is a K-flat complex of
> `O_U`-modules.
>
> Let `G` be an acyclic complex of `O_U`-modules. Extension by zero is exact (Stacks 03DJ), so
> `j_!G` is acyclic, and the K-flatness of `K` then makes `Tot(j_!G ⊗_O K)` acyclic. That
> complex is `j_!(Tot(G ⊗_{O_U} K|_U))` by `tensorComplexExtensionIso`, and extension by zero
> reflects exactness (Stacks 0E8G), so `Tot(G ⊗_{O_U} K|_U)` is acyclic as well.

```lean
theorem kFlat_restrictionComplex (Q : CochainComplex (Modules X.O) ℤ)
    (hQ : Stacks.SheafOfModules.KFlat.KFlat X.O Q) :
    Stacks.SheafOfModules.KFlat.KFlat (X.O.over U) ((restrictionComplex X U).obj Q)
```

**`Stacks.DerivedTensor.ExtensionByZero.OfEssentiallySmall.kFlat_restrictionComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensorOfEssentiallySmall.lean, line 435](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExtensionByZeroTensorOfEssentiallySmall.lean#L435). The attribute's comment: “for a site essentially u-small, objects in Type c, morphisms and modules in u”.

> **Stacks Project, Tag 0E8K over a site with large objects.** Let `(C, O)` be a ringed site
> whose objects form a type in an arbitrary universe `c` while its morphisms, the sections of `O`
> and the sections of its modules lie in one universe `u`, let `C` be essentially `u`-small, and
> let `U` be an object of `C`.  If `Q` is a K-flat complex of `O`-modules, then `Q|_U` is a
> K-flat complex of `O|_U`-modules.
>
> The proof is the source's.  Let `P` be an acyclic complex of `O|_U`-modules.  Extension by
> zero is exact (Stacks 03DJ), so `j_{U!}P` is acyclic, and the K-flatness of `Q` then makes
> `Tot(j_{U!}P ⊗_O Q)` acyclic.  That complex is `j_{U!}(Tot(P ⊗_{O|_U} Q|_U))` by
> `tensorComplexExtensionIso`, and extension by zero reflects exactness (Stacks 0E8G), so
> `Tot(P ⊗_{O|_U} Q|_U)` is acyclic as well.
>
> The attribute records the universe shape.  The tag is carried in full by
> `Stacks.DerivedTensor.ExtensionByZero.kFlat_restrictionComplex`, where the objects, the
> morphisms and the sections lie in a single universe — the faithful reading of the tag's ringed
> site, which this statement specializes to at `c := u`; that registration stands and this one
> does not replace it.

```lean
theorem kFlat_restrictionComplex (hQ : Stacks.SheafOfModules.IsKFlat X.O Q) :
    Stacks.SheafOfModules.IsKFlat (X.O.over U) ((restrictionComplex X U).obj Q)
```

## Tag 07A2, a lemma

[Tag 07A2](https://stacks.math.columbia.edu/tag/07A2) in the Stacks Project.

**`CochainComplex.KFlatMonoidal.KFlat.tensorObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorOfTwoKFlatComplexes.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TensorOfTwoKFlatComplexes.lean#L97).

> If `K^•` and `L^•` are K-flat complexes, then their total tensor product `Tot(K^• ⊗ L^•)`
> is K-flat.

```lean
theorem KFlat.tensorObj {K L : CochainComplex A ℤ} (hK : KFlat K) (hL : KFlat L) :
    KFlat (totalComplexTensor K L)
```

## Tag 07A3, a lemma

[Tag 07A3](https://stacks.math.columbia.edu/tag/07A3) in the Stacks Project.

**`Stacks.SheafOfModules.kFlat_of_second_third`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L79). The attribute's comment: “first vertex”.

> In a distinguished triangle, the first complex is K-flat if the second and
> third are K-flat.

```lean
theorem kFlat_of_second_third
    {K₁ K₂ K₃ : CochainComplex
      (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂)
    (g : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃)
    (h : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃ ⟶
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk f g h ∈ distTriang _)
    (h₂ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₂)
    (h₃ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₃) :
    CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₁
```

**`Stacks.SheafOfModules.kFlat_of_first_third`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L97). The attribute's comment: “second vertex”.

> In a distinguished triangle, the second complex is K-flat if the first
> and third are K-flat.

```lean
theorem kFlat_of_first_third
    {K₁ K₂ K₃ : CochainComplex
      (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂)
    (g : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃)
    (h : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃ ⟶
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk f g h ∈ distTriang _)
    (h₁ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₁)
    (h₃ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₃) :
    CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₂
```

**`Stacks.SheafOfModules.kFlat_of_first_second`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/DistinguishedTriangles.lean#L115). The attribute's comment: “third vertex”.

> In a distinguished triangle, the third complex is K-flat if the first
> and second are K-flat.

```lean
theorem kFlat_of_first_second
    {K₁ K₂ K₃ : CochainComplex
      (SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ}
    (f : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂)
    (g : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₂ ⟶
      (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃)
    (h : (HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₃ ⟶
      ((HomotopyCategory.quotient _ (ComplexShape.up ℤ)).obj K₁)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk f g h ∈ distTriang _)
    (h₁ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₁)
    (h₂ : CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₂) :
    CochainComplex.KFlatBifunctor.KFlat (Stacks.SheafOfModules.Tensor.sheafTensor R) K₃
```

**`Stacks.SheafOfModules.kFlatObjects_isTriangulated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TriangulatedSubcategory.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TriangulatedSubcategory.lean#L185). The attribute's comment: “two out of three in a distinguished triangle”.

> The K-flat complexes form a pre-triangulated subcategory of the homotopy category: the
> zero complex is K-flat, K-flatness is stable under shifts, and in a distinguished triangle
> two K-flat vertices force the third. The last assertion is Stacks 07A3.

```lean
theorem kFlatObjects_isTriangulated : (kFlatObjects.{u, v, w} R).IsTriangulated
```

## Tag 0G7B, a lemma

[Tag 0G7B](https://stacks.math.columbia.edu/tag/0G7B) in the Stacks Project.

**`Stacks.SheafOfModules.isKFlat_two_out_of_three`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThree.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThree.lean#L337).

> **Stacks 0G7B.** In a short exact sequence of complexes of sheaves of modules on a ringed
> site whose third term has flat terms, if two out of the three complexes are K-flat, so is the
> third.

```lean
theorem isKFlat_two_out_of_three
    (h : (IsKFlat X.O S.X₁ ∧ IsKFlat X.O S.X₂) ∨ (IsKFlat X.O S.X₁ ∧ IsKFlat X.O S.X₃) ∨
      (IsKFlat X.O S.X₂ ∧ IsKFlat X.O S.X₃)) :
    IsKFlat X.O S.X₁ ∧ IsKFlat X.O S.X₂ ∧ IsKFlat X.O S.X₃
```

**`Stacks.SheafOfModules.KFlatTwoOutOfThree.kFlat_left_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean#L343). The attribute's comment: “left complex”.

> **Stacks 0G7B, left complex.**  In a short exact sequence of complexes of `O`-modules whose
> right complex has flat terms, K-flatness of the middle and of the right complex implies
> K-flatness of the left complex.

```lean
theorem kFlat_left_of_shortExact (hS : S.ShortExact)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (S.X₃.X i))
    (h₂ : Stacks.SheafOfModules.KFlat.KFlat R S.X₂) (h₃ : Stacks.SheafOfModules.KFlat.KFlat R S.X₃)
      :
    Stacks.SheafOfModules.KFlat.KFlat R S.X₁
```

**`Stacks.SheafOfModules.KFlatTwoOutOfThree.kFlat_middle_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean, line 354](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean#L354). The attribute's comment: “middle complex”.

> **Stacks 0G7B, middle complex.**  In a short exact sequence of complexes of `O`-modules
> whose right complex has flat terms, K-flatness of the two outer complexes implies K-flatness of
> the middle complex.

```lean
theorem kFlat_middle_of_shortExact (hS : S.ShortExact)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (S.X₃.X i))
    (h₁ : Stacks.SheafOfModules.KFlat.KFlat R S.X₁) (h₃ : Stacks.SheafOfModules.KFlat.KFlat R S.X₃)
      :
    Stacks.SheafOfModules.KFlat.KFlat R S.X₂
```

**`Stacks.SheafOfModules.KFlatTwoOutOfThree.kFlat_right_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/TwoOutOfThreeShortExact.lean#L365). The attribute's comment: “right complex”.

> **Stacks 0G7B, right complex.**  In a short exact sequence of complexes of `O`-modules whose
> right complex has flat terms, K-flatness of the left and of the middle complex implies
> K-flatness of the right complex.

```lean
theorem kFlat_right_of_shortExact (hS : S.ShortExact)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (S.X₃.X i))
    (h₁ : Stacks.SheafOfModules.KFlat.KFlat R S.X₁) (h₂ : Stacks.SheafOfModules.KFlat.KFlat R S.X₂)
      :
    Stacks.SheafOfModules.KFlat.KFlat R S.X₃
```

## Tag 06YQ, a lemma

[Tag 06YQ](https://stacks.math.columbia.edu/tag/06YQ) in the Stacks Project.

**`Stacks.SheafOfModules.kFlat_of_boundedAbove_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/BoundedAboveFlatComplexes.lean, line 328](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/BoundedAboveFlatComplexes.lean#L328).

> **Stacks 06YQ.** A bounded above cochain complex of flat sheaves of modules is K-flat.

```lean
theorem kFlat_of_boundedAbove_of_flat
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf R)) ℤ)
    (hbound : ∃ n : ℤ, K.IsStrictlyLE n)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w}
      (O := R) (K.X i)) :
    IsKFlat R K
```

**`Stacks.Cohomology.LocallyBoundedKFlat.kFlat_of_isLocallyBounded_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/LocallyBoundedIsKFlat.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/LocallyBoundedIsKFlat.lean#L156). The attribute's comment: “with the boundedness hypothesis localized: a complex of flat O_W-modules which is merely LOCALLY bounded — bounded on each member of some open cover of W, which a complex with no global bound above can be — is K-flat. The source states it for a complex bounded above, which is this statement at the one-member cover W = W”.

> **A locally bounded complex of flat `𝒪_W`-modules is K-flat.**  This is [Stacks, Tag 06YQ]
> with its boundedness hypothesis localized: the complex is only assumed bounded on each member
> of some open cover of `W`, which is strictly weaker than being bounded above.
>
> For an acyclic `L^•`, the total complex `Tot(L^• ⊗_{𝒪_W} ℱ^•)` has to be acyclic, and by
> `acyclic_of_acyclic_restrict` it is enough that each of its restrictions be.  On an open `V` on
> which `ℱ^•` is bounded, `restrictTotalTensorIso` identifies that restriction with
> `Tot(L^•|_V ⊗_{𝒪_V} ℱ^•|_V)`; there `ℱ^•|_V` is bounded above with flat terms
> (`Stacks.Cohomology.TorAmplitude.isFlat_restrictModules`, [Stacks, Tag 0E8J] on an open
> subspace) hence K-flat by [Stacks, Tag 06YQ], and `L^•|_V` is acyclic because restriction is
> exact.

```lean
theorem kFlat_of_isLocallyBounded_of_flat
    (F : CochainComplex (RingedSpace.KFlatDerivedPullback.Modules W) ℤ)
    (hF : Stacks.SheafOfModules.OnSpace.IsLocallyBounded W F)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u}
      (O := W.sheaf) (F.X i)) :
    KFlat W F
```

## Tag 06YR, a lemma

[Tag 06YR](https://stacks.math.columbia.edu/tag/06YR) in the Stacks Project.

**`colim_of_system_KFlat_isKFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/FilteredColimitOfKFlatComplexes.lean, line 449](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/FilteredColimitOfKFlatComplexes.lean#L449).

> **Statement 1 (Stacks Lemma 21.17.9 / Tag 06YR).**
>
> Let `(C, O)` be a ringed site and let `D : K_1 → K_2 → K_3 → …` be a system of complexes
> of `O`-modules which are K-flat for the tensor product `⊗_O` of Definition 1.  Then the
> termwise colimit `colim_i K_i` is K-flat.
>
> The two structural facts of the proof are the two hypotheses of
> `colim_of_system_KFlat_isKFlat_of_bifunctor`, and both are theorems here: `⊗_O` commutes
> with colimits in each variable because `Mod(O)` is monoidal closed, so `ℱ ⊗_O -` is a left
> adjoint (`SheafOfModules.preservesColimitsOfSize_sheafTensor_obj`); and colimits over `ℕ`
> are exact in `Mod(O)` by AB5
> (`SheafOfModules.DifferentialGradedModule.hasExactColimitsOfShape_nat`), so a colimit of
> acyclic complexes is acyclic (`CochainComplex.KFlat.acyclic_colimit`).

```lean
theorem colim_of_system_KFlat_isKFlat (D : SystemOfComplexes (ringSheaf O))
    (hD : ∀ i, IsKFlat (ringSheaf O) (sheafTensor O) (D.obj i)) :
    IsKFlat (ringSheaf O) (sheafTensor O) (systemColimit (ringSheaf O) D)
```

## Tag 077J, a lemma

[Tag 077J](https://stacks.math.columbia.edu/tag/077J) in the Stacks Project.

**`Stacks.SheafOfModules.exists_resolutionByDirectSumsExtensionsByZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ResolutionByExtensionsByZero.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ResolutionByExtensionsByZero.lean#L358).

> A complex of modules on a ringed site admits a compatible resolution by direct
> sums of extensions by zero, whose colimit is quasi-isomorphic to the complex.

```lean
theorem exists_resolutionByDirectSumsExtensionsByZero
    (G : CochainComplex (SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ℤ) :
    Nonempty (ResolutionByDirectSumsExtensionsByZero X G)
```

## Tag 06YS, a lemma

[Tag 06YS](https://stacks.math.columbia.edu/tag/06YS) in the Stacks Project.

**`Stacks.SheafOfModules.exists_kFlat_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/Resolution.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/Resolution.lean#L94). The attribute's comment: “existence of a K-flat resolution”.

> Every cochain complex of sheaves of modules on a ringed site receives a quasi-isomorphism
> from a K-flat complex. This is the existence assertion of Stacks 06YS.

```lean
theorem exists_kFlat_quasiIso
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    ∃ (P : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) (p :
      P ⟶ G),
      IsKFlat X.O P ∧ QuasiIso p
```

**`Stacks.SheafOfModules.KFlatResolution.exists_kFlatResolution_ofSize`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionsOfSize.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionsOfSize.lean#L299). The attribute's comment: “with the object and morphism universes of the site independent of the module universe, so that it applies at a site whose objects lie above the module universe”.

> **Stacks Tag 06YS with the module universe free of the site.** Every complex of `O`-modules
> on a ringed site admits a termwise surjective quasi-isomorphism from a K-flat complex whose
> terms are flat: the colimit of the ladder of Stacks 077J, resolved by flat modules.
>
> The object universe `u`, the morphism universe `v` and the module universe `w` are
> independent, so the statement applies at a site whose objects lie above the module universe,
> such as the small étale site of an algebraic space, a `RingedTopos.{u, u + 1, u}`.

```lean
theorem exists_kFlatResolution_ofSize (G : CochainComplex (ModOfSize.{v, u, w} R) ℤ) :
    ∃ (K : CochainComplex (ModOfSize.{v, u, w} R) ℤ) (f : K ⟶ G),
      CochainComplex.KFlatBifunctor.KFlat
        (Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} R) K ∧
      (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R)
        (K.X i)) ∧
      QuasiIso f ∧ (∀ i : ℤ, Epi (f.f i))
```

**`Stacks.SheafOfModules.KFlatResolution.exists_kFlatResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionsOnARingedSite.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionsOnARingedSite.lean#L238).

> **Stacks Tag 06YS.** Every complex of `O`-modules on a ringed site admits a termwise
> surjective quasi-isomorphism from a K-flat complex whose terms are flat: the colimit of the
> ladder of 077J.

```lean
theorem exists_kFlatResolution
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} R)) ℤ)
      :
    ∃ (K : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} R)) ℤ) (f : K ⟶ G),
      CochainComplex.KFlatBifunctor.KFlat
        (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} R) K ∧
      (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := R) (K.X i)) ∧
      QuasiIso f ∧ (∀ i : ℤ, Epi (f.f i))
```

**`Stacks.SheafOfModules.exists_isKFlat_isFlat_quasiIso_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionWithFlatTermsSurjective.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionWithFlatTermsSurjective.lean#L171).

> **Stacks 06YS.** Every cochain complex `G` of modules on a ringed site receives a termwise
> surjective quasi-isomorphism from a K-flat complex whose terms are flat.
>
> The complex is the colimit of the ladder of [Stacks, Tag 077J]. It is K-flat because each rung
> is bounded above with flat terms, hence K-flat by [Stacks, Tag 06YQ], and a sequential colimit
> of K-flat complexes is K-flat by [Stacks, Tag 06YE]. Its terms are flat because they are
> filtered colimits of the flat terms of the rungs ([Stacks, Tag 05NG]), and the comparison is
> termwise surjective because each rung is termwise surjective onto a truncation of `G`.

```lean
public theorem exists_isKFlat_isFlat_quasiIso_epi
    (G : CochainComplex
      (_root_.SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ℤ) :
    ∃ (K : CochainComplex
        (_root_.SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.O))) ℤ) (s : K ⟶ G),
      IsKFlat X.O K ∧
      (∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) ∧
      QuasiIso s ∧ ∀ i : ℤ, Epi (s.f i)
```

**`Stacks.Cohomology.kFlatResolution_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean#L174). The attribute's comment: “K-flatness of the chosen resolution”.

> The chosen resolution is K-flat.

```lean
theorem kFlatResolution_kFlat
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    Stacks.SheafOfModules.IsKFlat X.O (kFlatResolution X G)
```

**`Stacks.Cohomology.kFlatResolution_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean#L181). The attribute's comment: “flatness of the terms of the chosen resolution”.

> Every term of the chosen resolution is flat.

```lean
theorem kFlatResolution_flat
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (i : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O)
      ((kFlatResolution X G).X i)
```

**`Stacks.Cohomology.kFlatResolutionHom_quasiIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean#L190). The attribute's comment: “quasi-isomorphism of the augmentation”.

> The augmentation from the chosen resolution is a quasi-isomorphism.

```lean
theorem kFlatResolutionHom_quasiIso
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    QuasiIso (kFlatResolutionHom X G)
```

**`Stacks.Cohomology.kFlatResolutionHom_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/TorsorsAndColimits/KFlatResolution.lean#L197). The attribute's comment: “termwise surjectivity of the augmentation”.

> The augmentation from the chosen resolution is epimorphic in each degree.

```lean
theorem kFlatResolutionHom_epi
    (G : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ)
    (i : ℤ) :
    Epi ((kFlatResolutionHom X G).f i)
```

## Tag 06YT, a lemma

[Tag 06YT](https://stacks.math.columbia.edu/tag/06YT) in the Stacks Project.

**`Stacks.SheafOfModules.quasiIso_mapBifunctorMap_id_of_kFlat_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L87). The attribute's comment: “the quasi-isomorphism in the right tensor factor”.

> A quasi-isomorphism `α` of K-flat complexes induces a quasi-isomorphism
> `Tot(F ⊗ α)` for every complex `F`. This is Stacks 06YT.

```lean
theorem quasiIso_mapBifunctorMap_id_of_kFlat_right
    {P Q : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (α : P ⟶ Q) (hα : QuasiIso α) (hP : IsKFlat X.O P) (hQ : IsKFlat X.O Q)
    (F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    QuasiIso (HomologicalComplex.mapBifunctorMap (𝟙 F) α (Stacks.SheafOfModules.Tensor.sheafTensor
      X.O)
      (ComplexShape.up ℤ))
```

**`Stacks.SheafOfModules.quasiIso_mapBifunctorMap_id_of_kFlat_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L107). The attribute's comment: “the quasi-isomorphism in the left tensor factor”.

> A quasi-isomorphism `α` of K-flat complexes induces a quasi-isomorphism
> `Tot(α ⊗ F)` for every complex `F`. This is the mirror image of Stacks 06YT.

```lean
theorem quasiIso_mapBifunctorMap_id_of_kFlat_left
    {P Q : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (α : P ⟶ Q) (hα : QuasiIso α) (hP : IsKFlat X.O P) (hQ : IsKFlat X.O Q)
    (F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    QuasiIso (HomologicalComplex.mapBifunctorMap α (𝟙 F) (Stacks.SheafOfModules.Tensor.sheafTensor
      X.O)
      (ComplexShape.up ℤ))
```

**`Stacks.SheafOfModules.quasiIso_tensorComplex_obj_map_of_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L130). The attribute's comment: “right tensor factor, tensorComplex spelling”.

> Stacks 06YT in the `Stacks.SheafOfModules.Tensor.tensorComplex` spelling: the quasi-isomorphism
>   `α` of
> K-flat complexes sits in the right tensor slot. The square whose cancellation gives the
> result is the naturality square of `tensorComplex.map r` at `α`, for a K-flat resolution
> `r : M ⟶ F`.

```lean
theorem quasiIso_tensorComplex_obj_map_of_kFlat
    {P Q : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (α : P ⟶ Q) (hα : QuasiIso α) (hP : IsKFlat X.O P) (hQ : IsKFlat X.O Q)
    (F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    QuasiIso (((Stacks.SheafOfModules.Tensor.tensorComplex X.O).obj F).map α)
```

**`Stacks.SheafOfModules.quasiIso_tensorComplex_map_app_of_kFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/ResolutionIndependence.lean#L145). The attribute's comment: “left tensor factor, tensorComplex spelling”.

> Stacks 06YT in the `Stacks.SheafOfModules.Tensor.tensorComplex` spelling, mirror image: the
> quasi-isomorphism `α` of K-flat complexes sits in the left tensor slot.

```lean
theorem quasiIso_tensorComplex_map_app_of_kFlat
    {P Q : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ}
    (α : P ⟶ Q) (hα : QuasiIso α) (hP : IsKFlat X.O P) (hQ : IsKFlat X.O Q)
    (F : CochainComplex (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) ℤ) :
    QuasiIso (((Stacks.SheafOfModules.Tensor.tensorComplex X.O).map α).app F)
```

## Tag 06YU, a definition

[Tag 06YU](https://stacks.math.columbia.edu/tag/06YU) in the Stacks Project.

**`Stacks.DerivedTensor.RingedSite.preservesColimitsOfShape_discrete_derivedTensorProductFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Coproducts.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Coproducts.lean#L203). The attribute's comment: “the derived tensor product commutes with arbitrary direct sums in the second variable”.

> **The derived tensor product of sheaves of modules on a ringed site commutes with arbitrary
> direct sums**, in the second variable: for an arbitrary `A` in `D(Mod(𝒪))` the functor
> `A ⊗^𝐋_𝒪 -` preserves direct sums indexed by any type of the module universe.

```lean
theorem preservesColimitsOfShape_discrete_derivedTensorProductFunctor
    (I : Type u)
    (A : DerivedCategory (Modules R)) :
    PreservesColimitsOfShape (Discrete I) ((derivedTensorProductFunctor R).obj A)
```

**`Stacks.SheafOfModules.exists_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Existence.lean, line 122](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Existence.lean#L122). The attribute's comment: “existence, for a site whose objects form a type in an arbitrary universe while its morphisms, structure sheaf and modules lie in one universe”.

> **Stacks 06YU.** The derived tensor product of sheaves of modules on a ringed site exists,
> with its canonical natural map to the ordinary total tensor product, its one-sided K-flat
> comparisons, and exactness in both variables.
>
> The objects of the site form a type in an arbitrary universe `c`, while its morphisms, the
> sections of its structure sheaf and the sections of its modules lie in one universe `u`; the
> derived category's hom universe `d` is independent of both.  That is the configuration of a
> small étale site, whose objects sit one universe above its morphisms.

```lean
theorem exists_derivedTensorProduct :
    Nonempty (DerivedTensorProduct.{c, u, u, d} X)
```

**`Stacks.SheafOfModules.canonicalDerivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Existence.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Existence.lean#L135). The attribute's comment: “the derived tensor product, at a site whose objects form a type in an arbitrary universe while its morphisms, structure sheaf and modules lie in one universe”.

> The canonical derived tensor product of sheaves of modules on a ringed site, with its
> natural map to the ordinary total tensor product, K-flat comparisons, and exactness in both
> variables.  The objects of the site live in a universe of their own.
>
> It is the construction `Stacks.SheafOfModules.derivedTensorProductOfExact`, made opaque with
> `irreducible_def`; `canonicalDerivedTensorProduct_def` is the defining equation.

```lean
irreducible_def canonicalDerivedTensorProduct : DerivedTensorProduct.{c, u, u, d} X
```

**`Stacks.DerivedTensor.RingedSite.exists_derivedTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExistenceOnARingedSite.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExistenceOnARingedSite.lean#L136). The attribute's comment: “existence and characterization”. References: SGA 4½ Etat 0 (6.2), “existence of ⊗^L”; SGA 4 XVII (4.1.7), “(i)”.

> **The derived tensor product of sheaves of modules on a ringed site exists**, with its
> canonical natural map to the ordinary total tensor product, its one-sided K-flat comparisons,
> and exactness in both variables.

```lean
theorem exists_derivedTensorProduct : Nonempty (DerivedTensorProduct R)
```

**`Stacks.DerivedTensor.RingedSite.canonicalDerivedTensorProduct`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExistenceOnARingedSite.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/ExistenceOnARingedSite.lean#L147). The attribute's comment: “the derived tensor product”. References: SGA 4½ Etat 0 (6.2), “X ⊗^L Y on a site”; SGA 4 XVII (4.1.7), “(i)”.

> The canonical derived tensor product of sheaves of modules on a ringed site, with its
> natural map to the ordinary total tensor product, its K-flat comparisons, and exactness in
> both variables. It is the construction `derivedTensorProductConstruction R`, made opaque with
> `irreducible_def` so that definitional unfolding does not reach the construction;
> `canonicalDerivedTensorProduct_def` is the defining equation.

```lean
irreducible_def canonicalDerivedTensorProduct : DerivedTensorProduct R
```

**`Stacks.DerivedTensor.derivedTensorSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/OnARingedSite.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/OnARingedSite.lean#L113). The attribute's comment: “the derived tensor product with a K-flat complex”. References: SGA 4½ Etat 0 (6.2), “⊗^L via K-flat”.

> The derived tensor product `- ⊗_O^{L} G : D(O) ⥤ D(O)` with a K-flat complex `G` of
> `O`-modules: the functor induced on derived categories by the total tensor complex
> `Tot(- ⊗_O G)`.

```lean
abbrev derivedTensorSheaf : DerivedCategory (SheafMod R) ⥤ DerivedCategory (SheafMod R)
```

**`Stacks.DerivedTensor.derivedTensorSheafQIso`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/OnARingedSite.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/OnARingedSite.lean#L119). The attribute's comment: “computed by the total tensor complex”.

> `- ⊗_O^{L} G` is the functor described by the total tensor complex: on the image of a
> complex `K` of `O`-modules in `D(O)` it is `Tot(K ⊗_O G)`, naturally in `K`.

```lean
abbrev derivedTensorSheafQIso :
    DerivedCategory.Q ⋙ derivedTensorSheaf R G ≅
      totRight (Stacks.SheafOfModules.Tensor.sheafTensor.{_, _, _, max u v w, max u v w} R) G ⋙
        DerivedCategory.Q
```

**`Stacks.SheafOfModules.DerivedMonoidal.canonicalTensor_commShift₂Int`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/CanonicalDerivedTensorCommShiftTwo.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/Monoidal/CanonicalDerivedTensorCommShiftTwo.lean#L82). The attribute's comment: “compatibility with the shifts in both variables”.

> **The canonical derived tensor product of [Stacks, Tag 06YU] commutes with the shifts in both
> variables**, with Mathlib's sign `(-1) ^ (p * q)`: the datum of
> `CochainComplex.KFlatBifunctor.derivedBifunctor`, transported along
> `Stacks.SheafOfModules.DerivedMonoidal.canonicalTensorIso`.
>
> It is a `def`, not an instance: the instance on
> `Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor R` is the structure field
> `Stacks.DerivedTensor.RingedSite.DerivedTensorProduct.commShift₂`, which
> `canonicalDerivedTensorProduct_commShift₂_eq` identifies with this datum.

```lean
def canonicalTensor_commShift₂Int :
    (Stacks.DerivedTensor.RingedSite.derivedTensorProductFunctor R).CommShift₂Int
```

**`Stacks.DerivedTensor.isTriangulated_derivedTensor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/DerivedTensor/KFlatDescent.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/DerivedTensor/KFlatDescent.lean#L199). The attribute's comment: “exact functor of triangulated categories”.

> **`- ⊗ G` is an exact functor of triangulated categories.** For sheaves of modules on a ringed
> site this is the case `F := Stacks.SheafOfModules.Tensor.sheafTensor R`.

```lean
instance isTriangulated_derivedTensor [IsKFlat F G] : (derivedTensor F G).IsTriangulated
```

## Tag 08FF, a definition

[Tag 08FF](https://stacks.math.columbia.edu/tag/08FF) in the Stacks Project.

**`Stacks.DerivedTensor.RingedSite.tor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Tor.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Tor.lean#L126). References: SGA 4 XVII (4.1.8), “modules, not complexes”.

> **The Tor's of two `O`-modules on a ringed site.** The `O`-module
> `Tor_p^O(F, G) = H^{-p}(F ⊗_O^{L} G)`.

```lean
def tor (p : ℤ) (F G : Modules R) : Modules R
```

## Tag 08FG, a lemma

[Tag 08FG](https://stacks.math.columbia.edu/tag/08FG) in the Stacks Project.

**`Stacks.DerivedTensor.RingedSite.isFlat_iff_isZero_tor_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Tor.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedTensor/Tor.lean#L386).

> **Stacks Project, Tag 08FG.** Let `(C, O)` be a ringed site and let `F` be an `O`-module.
> Then `F` is a flat `O`-module if and only if `Tor_1^O(F, G) = 0` for every `O`-module `G`.

```lean
theorem isFlat_iff_isZero_tor_one (F : Modules R) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := R) F ↔
      ∀ G : Modules R, IsZero (tor R 1 F G)
```

## Tag 0G7C, a lemma

[Tag 0G7C](https://stacks.math.columbia.edu/tag/0G7C) in the Stacks Project.

**`Stacks.SheafOfModules.KFlatCycles.isFlat_kernel_d_of_kFlat_of_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/CyclesOfAnAcyclicKFlatComplex.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/KFlat/CyclesOfAnAcyclicKFlatComplex.lean#L332).

> **Stacks Tag 0G7C.**  Let `K` be a K-flat, acyclic complex of `O`-modules on a ringed site
> whose terms are flat.  Then the kernel of `d^n : K^n ⟶ K^{n + 1}` is a flat `O`-module.
>
> The hypothesis is K-flatness in the sense of Tag 06YN (`Stacks.SheafOfModules.KFlat.KFlat`, which
> is `Iff.rfl` to the bifunctor-relative predicate written here).

```lean
theorem isFlat_kernel_d_of_kFlat_of_acyclic
    (K : CochainComplex (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, v, w} R)) ℤ)
    (hK : CochainComplex.KFlatBifunctor.KFlat
      (Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} R) K)
    (hacyclic : K.Acyclic)
    (hflat : ∀ i : ℤ, AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R) (K.X i))
    (n : ℤ) :
    AlgebraicGeometry.SheafOfModules.IsFlat.{v, u, w, w} (O := R)
      (kernel (K.d n (n + 1)))
```

## Tag 0G7D, a lemma

[Tag 0G7D](https://stacks.math.columbia.edu/tag/0G7D) in the Stacks Project.

**`Stacks.SheafOfModules.exists_isKFlat_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean#L117). The attribute's comment: “the K-flat factorization”.

> **Tag 0G6V.** A map `a : K^• ⟶ L^•` of complexes of `O`-modules with `K^•` K-flat factors,
> up to homotopy, through a K-flat complex `N^•` which maps to `L^•` by a quasi-isomorphism.

```lean
theorem exists_isKFlat_factorization
    {K L : CochainComplex
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ}
    (a : K ⟶ L) (hK : IsKFlat X.O K) :
    ∃ (N : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ)
      (b : K ⟶ N) (c : N ⟶ L),
      IsKFlat X.O N ∧ QuasiIso c ∧ Nonempty (Homotopy a (b ≫ c))
```

**`Stacks.SheafOfModules.exists_isKFlat_isFlat_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/KFlat/Factorization.lean#L132). The attribute's comment: “the factorization with flat terms”.

> **Tag 0G6V, second half.** If in addition the terms of `K^•` are flat `O`-modules, then the
> intermediate complex of the factorization can be chosen with flat terms as well.

```lean
theorem exists_isKFlat_isFlat_factorization
    {K L : CochainComplex
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ}
    (a : K ⟶ L) (hK : IsKFlat X.O K)
    (hKflat : ∀ i : ℤ,
      AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (K.X i)) :
    ∃ (N : CochainComplex
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf.{u, u, u} X.O)) ℤ)
      (b : K ⟶ N) (c : N ⟶ L),
      IsKFlat X.O N ∧
        (∀ i : ℤ,
          AlgebraicGeometry.SheafOfModules.IsFlat.{u, u, u, u} (O := X.O) (N.X i)) ∧
        QuasiIso c ∧ Nonempty (Homotopy a (b ≫ c))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.17, Tag 06YL](https://stacks.math.columbia.edu/tag/06YL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
