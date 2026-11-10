---
declaration: section
origin: cited
lean: Stacks.SheafOfModules.Tensor.sheafTensor, Stacks.SheafOfModules.TensorRingedSpace.tensorPresheaf_sections, Stacks.SheafOfModules.TensorRingedSpace.tensorPresheaf_restrict_tmul, Stacks.SheafOfModules.TensorRingedSpace.tensorSheaf_eq_sheafification, Stacks.SheafOfModules.TensorRingedSpace.tensorCorepresentableBy, Stacks.SheafOfModules.TensorRingedSpace.tensorSymmetry, Stacks.SheafOfModules.TensorRingedSpace.tensorAssociativity, Stacks.SheafOfModules.TensorStalkRingedSpace.tensorStalkIso
statement: formalized
proof: formalized
---

# 17.16 Tensor product

Section 17.16 of the Stacks Project, [Tag 01CA](https://stacks.math.columbia.edu/tag/01CA). 7 tags here are carried by 27 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01CA, the section

[Tag 01CA](https://stacks.math.columbia.edu/tag/01CA) in the Stacks Project.

**`Stacks.SheafOfModules.Tensor.sheafTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SheafificationTensor.lean#L166). The attribute's comment: “the section's definition of the tensor product sheaf `F ⊗_O G = (F ⊗_{p, O} G)^#`, the sheafification of the tensor product presheaf; over an arbitrary site, the ringed-space case being the site of opens of `X`”.

> The tensor product of module sheaves in independent section universes, obtained by
> sheafifying the canonical objectwise tensor product of their underlying presheaves.

```lean
noncomputable def sheafTensor :
    SheafOfModules.{leftUniverse} (ringSheaf R) ⥤ SheafOfModules.{rightUniverse} (ringSheaf R) ⥤
      SheafOfModules.{max leftUniverse rightUniverse} (ringSheaf R)
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorPresheaf_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L110). The attribute's comment: “the section's tensor product presheaf `F ⊗_{p, O_X} G`, the rule which assigns to `U ⊂ X` open the `O_X(U)`-module `F(U) ⊗_{O_X(U)} G(U)`: its sections”.

> **The tensor product presheaf** `ℱ ⊗_{p, 𝒪_X} 𝒢` assigns to an open `U ⊂ X` the
> `𝒪_X(U)`-module `ℱ(U) ⊗_{𝒪_X(U)} 𝒢(U)`.

```lean
theorem tensorPresheaf_sections (U : (TopologicalSpace.Opens X.carrier)ᵒᵖ) :
    ((PresheafOfModules.tensorObj (O := X.presheaf) F.val G.val).obj U : Type u) =
      (F.val.obj U ⊗[(Tensor.ringSheaf (structureSheaf X)).obj.obj U] G.val.obj U)
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorPresheaf_restrict_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L119). The attribute's comment: “the section's tensor product presheaf `F ⊗_{p, O_X} G`: its restriction maps, `x ⊗ y ↦ x|_V ⊗ y|_V`”.

> The restriction maps of the tensor product presheaf are the tensor products of the
> restriction maps of `ℱ` and `𝒢`.

```lean
theorem tensorPresheaf_restrict_tmul {U V : (TopologicalSpace.Opens X.carrier)ᵒᵖ} (f : U ⟶ V)
    (x : F.val.obj U) (y : G.val.obj U) :
    (PresheafOfModules.tensorObj (O := X.presheaf) F.val G.val).restrictₛₗ f
        (x ⊗ₜ[(Tensor.ringSheaf (structureSheaf X)).obj.obj U] y) =
      F.val.restrictₛₗ f x ⊗ₜ[(Tensor.ringSheaf (structureSheaf X)).obj.obj V]
        G.val.restrictₛₗ f y
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorSheaf_eq_sheafification`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L131). The attribute's comment: “the section's definition of the tensor product sheaf as the sheafification `F ⊗_{O_X} G = (F ⊗_{p, O_X} G)^#` of the tensor product presheaf”.

> **The tensor product sheaf** `ℱ ⊗_{𝒪_X} 𝒢` is the sheafification
> `(ℱ ⊗_{p, 𝒪_X} 𝒢)^#` of the tensor product presheaf.

```lean
theorem tensorSheaf_eq_sheafification :
    ((Tensor.sheafTensor (structureSheaf X)).obj F).obj G =
      (PresheafOfModules.sheafification (R := Tensor.ringSheaf (structureSheaf X))
        (𝟙 (Tensor.ringSheaf (structureSheaf X)).obj)).obj
        (PresheafOfModules.tensorObj (O := X.presheaf) F.val G.val)
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorCorepresentableBy`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L145). The attribute's comment: “the characterisation of `F ⊗_{O_X} G` as the sheaf of `O_X`-modules with `Hom_{O_X}(F ⊗_{O_X} G, H) = Bilin_{O_X}(F × G, H)` for every `O_X`-module `H`, naturally in `H`: the tensor product sheaf corepresents `H ↦ Bilin_{O_X}(F × G, H)`”.

> **The tensor product sheaf represents bilinear maps.** For every sheaf of `𝒪_X`-modules
> `ℋ`, morphisms `ℱ ⊗_{𝒪_X} 𝒢 ⟶ ℋ` are in natural bijection with bilinear maps
> `ℱ × 𝒢 → ℋ` of sheaves of `𝒪_X`-modules: `ℱ ⊗_{𝒪_X} 𝒢` corepresents the functor
> `ℋ ↦ Bilin_{𝒪_X}(ℱ × 𝒢, ℋ)`, which characterises it up to unique isomorphism.

```lean
noncomputable def tensorCorepresentableBy :
    (bilinFunctor (Tensor.ringSheaf (structureSheaf X)) F G).CorepresentableBy
      (((Tensor.sheafTensor (structureSheaf X)).obj F).obj G)
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorSymmetry`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L162). The attribute's comment: “the symmetry `F ⊗_{O_X} G = G ⊗_{O_X} F`, functorial in `F` and `G`: an isomorphism of the tensor bifunctor with its flip, induced by the symmetry of tensor products of modules”.

> **The symmetry of the tensor product sheaf**: the canonical isomorphism
> `ℱ ⊗_{𝒪_X} 𝒢 ≅ 𝒢 ⊗_{𝒪_X} ℱ`, functorial in `ℱ` and `𝒢`, i.e. an isomorphism between the
> tensor bifunctor and its flip. It is the sheafification of the sectionwise symmetry
> `M ⊗_R N ≅ N ⊗_R M` of the tensor product of modules.

```lean
noncomputable def tensorSymmetry :
    Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X) ≅
      (Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X)).flip
```

**`Stacks.SheafOfModules.TensorRingedSpace.tensorAssociativity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorProductRingedSpace.lean#L174). The attribute's comment: “the associativity `(F ⊗_{O_X} G) ⊗_{O_X} H = F ⊗_{O_X} (G ⊗_{O_X} H)`, functorial in `F`, `G` and `H`: an isomorphism of trifunctors, induced by the associativity of tensor products of modules”.

> **The associativity of the tensor product sheaf**: the canonical isomorphism
> `(ℱ ⊗_{𝒪_X} 𝒢) ⊗_{𝒪_X} ℋ ≅ ℱ ⊗_{𝒪_X} (𝒢 ⊗_{𝒪_X} ℋ)`, functorial in `ℱ`, `𝒢` and `ℋ`, i.e.
> an isomorphism of trifunctors. It is induced through sheafification by the associativity of
> tensor products of modules.

```lean
noncomputable def tensorAssociativity :
    bifunctorComp₁₂ (Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X))
        (Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X)) ≅
      bifunctorComp₂₃ (Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X))
        (Tensor.sheafTensor.{u, u, u, u, u} (structureSheaf X))
```

## Tag 01CB, a lemma

[Tag 01CB](https://stacks.math.columbia.edu/tag/01CB) in the Stacks Project.

**`Stacks.SheafOfModules.TensorStalkRingedSpace.tensorStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorStalkRingedSpace.lean, line 889](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorStalkRingedSpace.lean#L889). References: SGA 4 IV (13.5), “ringed spaces”.

> **The canonical `O_{X,x}`-linear isomorphism `(F ⊗_{O_X} G)_x ≅ F_x ⊗_{O_{X,x}} G_x`
> (Stacks Tag 01CB).**  It is extracted (via `Classical.choice`) from `exists_tensorStalkIso`,
> and is characterised on germs of pure tensors by `tensorStalkIso_germ` below.

```lean
noncomputable def tensorStalkIso (x : X.carrier)
    (F G : SheafOfModules.{u} (structureSheafRing X)) :
    letI := stalkModule X
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
        (⟨X.presheaf, X.IsSheaf⟩ : Sheaf (JX X) CommRingCat.{u})).obj F).obj G).val x
    (grpStalk X ((((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      (⟨X.presheaf, X.IsSheaf⟩ : Sheaf (JX X) CommRingCat.{u})).obj F).obj G)).val x) ≃ₗ[ringStalk X x]
      ((grpStalk X F.val x) ⊗[ringStalk X x] (grpStalk X G.val x))
```

## Tag 05NA, a lemma

[Tag 05NA](https://stacks.math.columbia.edu/tag/05NA) in the Stacks Project.

**`Stacks.SheafOfModules.TensorSheafification.tensorSheafifyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorSheafificationComparison.lean, line 643](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorSheafificationComparison.lean#L643).

> The canonical isomorphism of sheaves of `𝒪`-modules
> `(F' ⊗ G')^# ≅ ((F')^# ⊗ (G')^#)^#` induced by the sheafification units.

```lean
noncomputable def tensorSheafifyIso
    (F' G' : PresheafOfModules.{w} (structureRingPresheaf 𝒪)) :
    (sheafify 𝒪 h𝒪).obj (PresheafOfModules.tensorObj (O := 𝒪) F' G') ≅
      (sheafify 𝒪 h𝒪).obj
        (PresheafOfModules.tensorObj (O := 𝒪)
          ((SheafOfModules.forget (structureSheaf 𝒪 h𝒪) ⋙
              PresheafOfModules.restrictScalars (𝟙 (structureSheaf 𝒪 h𝒪).obj)).obj
            ((sheafify 𝒪 h𝒪).obj F'))
          ((SheafOfModules.forget (structureSheaf 𝒪 h𝒪) ⋙
              PresheafOfModules.restrictScalars (𝟙 (structureSheaf 𝒪 h𝒪).obj)).obj
            ((sheafify 𝒪 h𝒪).obj G')))
```

## Tag 01CC, a lemma

[Tag 01CC](https://stacks.math.columbia.edu/tag/01CC) in the Stacks Project.

**`AlgebraicGeometry.tensorSheafMap_epi_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/ExternalTensor/Basic.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/DerivedVarieties/ExternalTensor/Basic.lean#L151). The attribute's comment: “exactness at the right term, second variable”.

> Tensoring an epimorphism of `O_X`-modules on the left by an `O_X`-module gives an
> epimorphism. This is Tag 01CC in the second variable.

```lean
theorem tensorSheafMap_epi_right {G G' : SheafOfModules.{u} (structureSheafRing X)}
    (F : SheafOfModules.{u} (structureSheafRing X)) (ψ : G ⟶ G') [Epi ψ] :
    Epi (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      ⟨((X)).presheaf, ((X)).IsSheaf⟩)).map (((𝟙 F), ψ) : (F, G) ⟶ (F, G'))))
```

**`AlgebraicGeometry.SheafOfModules.tensorSheafMap_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorExactness.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorExactness.lean#L195). The attribute's comment: “exactness at the middle term”.

> Tensoring an exact pair of `O_X`-modules whose second map is an epimorphism
> on the right by an `O_X`-module gives an exact pair.

```lean
theorem tensorSheafMap_exact
    (S : ShortComplex (_root_.SheafOfModules.{u} (structureSheafRing X)))
    (G : _root_.SheafOfModules.{u} (structureSheafRing X))
    (hS : S.Exact) [Epi S.g] :
    let tensorFunctor :
        (_root_.SheafOfModules.{u} (structureSheafRing X) ×
          _root_.SheafOfModules.{u} (structureSheafRing X)) ⥤
          _root_.SheafOfModules.{u} (structureSheafRing X) :=
      Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
        ⟨X.presheaf, X.IsSheaf⟩)
    let firstMap := tensorFunctor.map ((S.f, 𝟙 G) : (S.X₁, G) ⟶ (S.X₂, G))
    let secondMap := tensorFunctor.map ((S.g, 𝟙 G) : (S.X₂, G) ⟶ (S.X₃, G))
    ∃ zeroComposite : firstMap ≫ secondMap = 0,
      (ShortComplex.mk firstMap secondMap zeroComposite).Exact
```

**`AlgebraicGeometry.SheafOfModules.tensorSheafMap_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/TensorExactness.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/TensorExactness.lean#L222). The attribute's comment: “exactness at the right term”.

> Tensoring an epimorphism of `O_X`-modules on the right by an
> `O_X`-module gives an epimorphism.

```lean
theorem tensorSheafMap_epi
    {F₂ F₃ : _root_.SheafOfModules.{u} (structureSheafRing X)}
    (G : _root_.SheafOfModules.{u} (structureSheafRing X)) (g : F₂ ⟶ F₃) [Epi g] :
    Epi (((Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      (⟨X.presheaf, X.IsSheaf⟩ : Sheaf (JX X) CommRingCat.{u}))).map
        ((g, (𝟙 G)) : (_, _) ⟶ (_, _))))
```

## Tag 01CD, a lemma

[Tag 01CD](https://stacks.math.columbia.edu/tag/01CD) in the Stacks Project.

**`Stacks.RingedSpace.comparisonBifunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensorComparisonIso.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensorComparisonIso.lean#L578).

> **Stacks 01CD**, unconditionally: pulling back the tensor product of two sheaves of modules
> on a ringed space is the tensor product of their pullbacks, naturally in both arguments.  This
> is `Stacks.RingedSpace.comparisonIso` with its hypothesis discharged, so by
> `Stacks.RingedSpace.comparison_unique` it is the only candidate.

```lean
noncomputable def comparisonBifunctorIso :
    Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
      ⟨Y.presheaf, Y.IsSheaf⟩) ⋙ pullbackFunctor f ≅
      Functor.prod (pullbackFunctor f) (pullbackFunctor f) ⋙
        Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
          ⟨X.presheaf, X.IsSheaf⟩)
```

**`Stacks.RingedSpace.comparisonBifunctorIso_hom_homEquiv_unit_tmul`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensorComparisonIso.lean, line 594](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackTensorComparisonIso.lean#L594).

> **The canonicality clause of Stacks 01CD.**  The adjoint transpose of the forward map of
> `comparisonBifunctorIso` at `(A, B)` carries the sheafification-unit image of a pure tensor to
> the image, under the corresponding unit on `X`, of the tensor of the two pullback-unit
> images.

```lean
lemma comparisonBifunctorIso_hom_homEquiv_unit_tmul
    (A B : SheafOfModules.{u} (structureRingSheaf Y)) (U : (Opens Y.carrier)ᵒᵖ)
    (a : A.val.obj U) (b : B.val.obj U) :
    Hom.app ((pullbackAdjunction f).homEquiv
          (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
            ⟨Y.presheaf, Y.IsSheaf⟩).obj A).obj B)
          (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u}
            ⟨X.presheaf, X.IsSheaf⟩).obj ((pullbackFunctor f).obj A)).obj
              ((pullbackFunctor f).obj B))
          ((comparisonBifunctorIso f).hom.app (A, B))).val U
        (Hom.app ((PresheafOfModules.sheafificationAdjunction
          (R := Stacks.SheafOfModules.Tensor.ringSheaf ⟨Y.presheaf, Y.IsSheaf⟩)
          (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf ⟨Y.presheaf, Y.IsSheaf⟩).obj)).unit.app
            (_root_.PresheafOfModules.tensorObj A.val B.val)) U (a ⊗ₜ b)) =
      Hom.app ((PresheafOfModules.sheafificationAdjunction
        (R := Stacks.SheafOfModules.Tensor.ringSheaf ⟨X.presheaf, X.IsSheaf⟩)
        (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf ⟨X.presheaf, X.IsSheaf⟩).obj)).unit.app
          (_root_.PresheafOfModules.tensorObj ((pullbackFunctor f).obj A).val
            ((pullbackFunctor f).obj B).val))
        ((opensMap f).op.obj U) (pullbackUnit f A U a ⊗ₜ pullbackUnit f B U b)
```

**`Stacks.PullbackTensorIso.pullbackTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PullbackTensorIso/Invertible.lean, line 355](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PullbackTensorIso/Invertible.lean#L355).

> Stacks 01CD. For a morphism of ringed spaces `f : X ⟶ Y`, pullback of sheaves of
> modules commutes with the tensor product: `f^*(A ⊗_{𝒪_Y} B) ≅ f^*A ⊗_{𝒪_X} f^*B`, as an
> isomorphism of bifunctors, so naturally in both module arguments. This is
> `Stacks.RingedSpace.comparisonIso` with its instance hypothesis discharged, and by
> `Stacks.RingedSpace.comparison_unique` the comparison is the only candidate.
>
> `Stacks.RingedSpace.comparisonBifunctorIso` reaches the identical statement by the other
> unconditional route — discharging the Tag 0098 stalk formula — and is the same isomorphism, both
> forward maps being `Stacks.RingedSpace.comparisonNatTrans f`.

```lean
def pullbackTensorIso :
    Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨Y.presheaf, Y.IsSheaf⟩) ⋙
        Stacks.RingedSpace.pullbackFunctor f ≅
      Functor.prod (Stacks.RingedSpace.pullbackFunctor f)
          (Stacks.RingedSpace.pullbackFunctor f) ⋙
        Functor.uncurry.obj (Stacks.SheafOfModules.Tensor.sheafTensor ⟨X.presheaf, X.IsSheaf⟩)
```

**`Stacks.WeilCohomology.pullbackTensorObjRingedSpaceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/PullbackTensor.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/WeilCohomology/ChernClasses/PullbackTensor.lean#L52). The attribute's comment: “the pullback of a tensor product of sheaves of modules on a scheme, read at the spelling of the tensor product that the Grothendieck ring of Tag 0FDK multiplies with”.

> **Stacks Tag 01CD, the pullback of a tensor product is the tensor product of the
> pullbacks**, at the spelling of the tensor product that `K₀(Vect(X))` multiplies with. The
> comparison morphism of Tag 01CD is an isomorphism, and its source and target are the two sides
> spelled through the monoidal product of Tag 01CA, which is that spelling.

```lean
def pullbackTensorObjRingedSpaceIso {X Y : Scheme.{u}} (f : X ⟶ Y) (A B : Y.Modules) :
    (Scheme.Modules.pullback f).obj (Scheme.Modules.tensorObjRingedSpace Y A B) ≅
      Scheme.Modules.tensorObjRingedSpace X ((Scheme.Modules.pullback f).obj A)
        ((Scheme.Modules.pullback f).obj B)
```

## Tag 05NB, a lemma

[Tag 05NB](https://stacks.math.columbia.edu/tag/05NB) in the Stacks Project.

**`Stacks.SheafOfModules.FlatSheafification.sheafTensorRight_preservesColimits`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatSheafification.lean#L173). The attribute's comment: “for the right-handed tensor endofunctor (sheafTensor O).flip.obj F”.

> Tensoring on the right with `F` preserves all colimits indexed in the module universe.

```lean
public lemma sheafTensorRight_preservesColimits
    {C : Type u} [Category.{v} C] (J : GrothendieckTopology C)
    [J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}]
    [HasWeakSheafify J AddCommGrpCat.{z}]
    (O : Sheaf J CommRingCat.{w})
    (F : SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf O)) :
    PreservesColimitsOfSize.{max u z, z}
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, z, z} (J := J) O).flip.obj F)
```

**`Stacks.SheafOfModules.TensorColimits.tensorLeft_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPreservesColimits.lean, line 699](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorPreservesColimits.lean#L699). References: SGA 5 V (1.2.1), “inductive limits”.

> Tensoring with a fixed sheaf of modules commutes with all small colimits, independently of
> the ring universe.

```lean
public theorem tensorLeft_preservesColimits (R : Sheaf J CommRingCat.{w})
    [J.WEqualsLocallyBijective AddCommGrpCat.{z}] [HasWeakSheafify J AddCommGrpCat.{z}]
    (F : SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf R)) :
    PreservesColimitsOfSize.{a, z}
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, z, z} R).obj F))
```

**`AlgebraicGeometry.SheafOfModules.sheafTensorLeft_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean#L265). References: SGA 5 V (1.2.1), “inductive limits”.

> **Stacks Project, Tag 05NB.** Tensoring with a fixed sheaf of modules commutes with
> all small colimits, independently of the ring universe.

```lean
theorem sheafTensorLeft_preservesColimits (R : Sheaf J CommRingCat.{w})
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf R)) :
    PreservesColimitsOfSize.{a, z} (sheafTensorLeft J R F)
```

## Tag 01CE, a lemma

[Tag 01CE](https://stacks.math.columbia.edu/tag/01CE) in the Stacks Project.

**`Stacks.TensorCoherence.isCoherent_tensorSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorCoherence.lean, line 454](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorCoherence.lean#L454). The attribute's comment: “tensor_finite_presentation_coherent, over a site, for sheafTensorRight”.

> **Stacks Project, Tag 01CE.**

```lean
theorem isCoherent_tensorSheaf
    (F G : SheafOfModules.{u} (Stacks.commRingSheafToRingSheaf O))
    [F.IsFinitePresentation] (hG : IsCoherent G) :
    IsCoherent
      (((Stacks.SheafOfModules.Tensor.sheafTensor.{u, u, u, u, u} O).flip.obj G).obj F)
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isCoherent_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean#L521). The attribute's comment: “tensor_finite_presentation_coherent”.

> On a ringed space, the tensor product of a sheaf of modules of finite presentation with a
> coherent sheaf of modules is coherent.

```lean
theorem tensorSheaf_isCoherent_of_isFinitePresentation
    (X : AlgebraicGeometry.RingedSpace.{u, u})
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [F.IsFinitePresentation] [_root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf,
        ((X)).IsSheaf⟩).obj (F)).obj (G)))
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean, line 556](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorCoherence/Basic.lean#L556). The attribute's comment: “tensor_coherent”. References: EGA 0 (5.3.5), “tensor product”; EGA I (9.1.1), “coherent tensor”.

> The tensor product of two coherent sheaves of modules is coherent.

```lean
theorem tensorSheaf_isCoherent (X : AlgebraicGeometry.RingedSpace.{u, u})
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [_root_.SheafOfModules.IsCoherent F] [_root_.SheafOfModules.IsCoherent G] :
    _root_.SheafOfModules.IsCoherent ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf,
        ((X)).IsSheaf⟩).obj (F)).obj (G)))
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_nonempty_localGeneratorsData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean#L115). The attribute's comment: “tensor_locally_generated”.

> **Stacks Project, Tag 01CE (1).** On a ringed space, the tensor product of two sheaves of
> modules which are locally generated by sections is locally generated by sections: there is an
> open covering of `X` on each member of which `F ⊗_{𝒪_X} G` is generated by global sections.
>
> This is Stacks 03L6 for local generation by sections,
> `Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isLocallyGeneratedBySectionsOnSite`,
> read at the site of opens of `X`, with Stacks 03DN moving between the covering of `X` that the
> statement speaks of and the condition at every open that the site-level predicate asserts.

```lean
theorem tensorSheaf_nonempty_localGeneratorsData
    (hF : Nonempty F.LocalGeneratorsData.{u, u, u, u})
    (hG : Nonempty G.LocalGeneratorsData.{u, u, u, u}) :
    Nonempty ((((Stacks.SheafOfModules.Tensor.sheafTensor
      ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj (G))).LocalGeneratorsData.{u, u, u, u}
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean#L142). The attribute's comment: “tensor_finite_type”.

> **Stacks Project, Tag 01CE (2).** On a ringed space, the tensor product of two sheaves of
> modules of finite type is of finite type.
>
> This is Stacks 03L6 for the finite type condition,
> `Stacks.SheafOfModules.TensorLocalProperties.tensorSheaf_isFiniteType`, read at the site of
> opens of `X`; the predicate is the same one on both sides, since Mathlib's
> `SheafOfModules.IsFiniteType` already asks for a covering of the space.

```lean
theorem tensorSheaf_isFiniteType [_root_.SheafOfModules.IsFiniteType.{u, u, u} F]
    [_root_.SheafOfModules.IsFiniteType.{u, u, u} G] :
    _root_.SheafOfModules.IsFiniteType.{u, u, u}
      ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj (G)))
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorFiniteness/RingedSpace.lean#L161). The attribute's comment: “tensor_locally_free”.

> **Stacks Project, Tag 01CE (7).** On a ringed space, the tensor product of two locally free
> sheaves of modules is locally free.
>
> Following the source: on a member of a covering trivializing both factors, `F` is free on a
> basis `B_F` and `G` on a basis `B_G`, and the tensor product is free on `B_F × B_G`. The local
> basis is `Stacks.SheafOfModules.localGeneratorsDataTensor`, which is built on the common
> refinement of the two given coverings, and its members are bases by
> `Stacks.SheafOfModules.isLocallyFreeData_localGeneratorsDataTensor`.

```lean
theorem tensorSheaf_isLocallyFree [_root_.SheafOfModules.IsLocallyFree.{u, u, u} F]
    [_root_.SheafOfModules.IsLocallyFree.{u, u, u} G] :
    _root_.SheafOfModules.IsLocallyFree.{u, u, u}
      ((((Stacks.SheafOfModules.Tensor.sheafTensor
        ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj (G)))
```

**`AlgebraicGeometry.SheafOfModules.tensorSheaf_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/TensorFinitePresentation/Basic.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/TensorFinitePresentation/Basic.lean#L132). The attribute's comment: “tensor_finite_presentation”.

> The tensor product of two finitely presented modules on a ringed space is of finite
> presentation.

```lean
theorem tensorSheaf_isFinitePresentation (X : AlgebraicGeometry.RingedSpace.{u, u})
    (F G : _root_.SheafOfModules.{u}
      (structureSheafRing X))
    [_root_.SheafOfModules.IsFinitePresentation.{u, u, u} F]
    [_root_.SheafOfModules.IsFinitePresentation.{u, u, u} G] :
    _root_.SheafOfModules.IsFinitePresentation.{u, u, u}
      ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj
        (G)))
```

**`AlgebraicGeometry.tensorSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Basic.lean, line 604](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorProduct/Basic.lean#L604). The attribute's comment: “tensor_quasicoherent”.

> **Stacks Project, Tag 01CE.** The tensor product of two quasi-coherent
> modules on a ringed space is quasi-coherent.

```lean
instance tensorSheaf_isQuasicoherent
    (X : AlgebraicGeometry.RingedSpace.{u, u})
    (F G : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf X.sheaf)))
    [F.IsQuasicoherent] [G.IsQuasicoherent] :
    ((((Stacks.SheafOfModules.Tensor.sheafTensor ⟨((X)).presheaf, ((X)).IsSheaf⟩).obj (F)).obj (G))).IsQuasicoherent
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 17.16, Tag 01CA](https://stacks.math.columbia.edu/tag/01CA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
