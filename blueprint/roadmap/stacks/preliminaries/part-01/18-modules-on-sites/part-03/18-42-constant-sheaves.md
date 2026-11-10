---
declaration: section
origin: cited
lean: Stacks.ConstantSheaf.surjective_constantSections_map, Stacks.ConstantSheaf.injective_constantSections_map, Stacks.ConstantSheaf.range_constantSections_map_eq_ker, constantSheaf_shortExact_of_shortExact, constantSheaf_sections_shortExact_of_shortExact, Stacks.ConstantSheaf.bijective_tensorComparison, Stacks.ConstantSheaf.flat_constantSections, Stacks.ConstantSheaf.completedConstantSheaf
statement: formalized
proof: formalized
---

# 18.42 Constant sheaves

Section 18.42 of the Stacks Project, [Tag 093I](https://stacks.math.columbia.edu/tag/093I). 5 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 093J, a lemma

[Tag 093J](https://stacks.math.columbia.edu/tag/093J) in the Stacks Project.

**`Stacks.ConstantSheaf.surjective_constantSections_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean, line 288](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean#L288). The attribute's comment: “surjectivity”.

> **Stacks Tag 093J**, surjectivity half. If `f : M ⟶ N` is a surjection of `R`-modules then
> the induced map on the sections over `U` of the associated constant sheaves is surjective.

```lean
theorem surjective_constantSections_map {M N : ModuleCat.{x} R} (f : M ⟶ N)
    (hf : Function.Surjective f.hom) (U : C) :
    Function.Surjective ((constantSections J U).map f).hom
```

**`Stacks.ConstantSheaf.injective_constantSections_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean, line 323](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean#L323). The attribute's comment: “injectivity”.

> **Stacks Tag 093J**, injectivity half. `constantSections` takes injections of modules to
> injections.

```lean
theorem injective_constantSections_map {M N : ModuleCat.{x} R} (f : M ⟶ N)
    (hf : Function.Injective f.hom) (U : C) :
    Function.Injective ((constantSections J U).map f).hom
```

**`Stacks.ConstantSheaf.range_constantSections_map_eq_ker`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean#L388).

> **Stacks Tag 093J**. The functor of sections of a constant sheaf of modules is exact: an exact
> pair of morphisms of `R`-modules is taken to an exact pair.

```lean
theorem range_constantSections_map_eq_ker (U : C) {A B D : ModuleCat.{x} R}
    (α : A ⟶ B) (β : B ⟶ D) (h : LinearMap.range α.hom = LinearMap.ker β.hom) :
    LinearMap.range ((constantSections J U).map α).hom =
      LinearMap.ker ((constantSections J U).map β).hom
```

**`constantSheaf_shortExact_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantAbelianSheaf.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantAbelianSheaf.lean#L174). References: EGA 0 (12.1.3), “special case”; EGA IV (10.2.8), “special case”.

> **(1) Exactness as abelian sheaves.**
>
> Given a short exact sequence `0 → A → B → C → 0` of abelian groups (a short complex `S`
> with `S.ShortExact`), applying the constant sheaf functor yields a short exact sequence
> of abelian sheaves `0 → A → B → C → 0` on the site `C`.

```lean
theorem constantSheaf_shortExact_of_shortExact
    (S : ShortComplex AddCommGrpCat.{u}) (hS : S.ShortExact) :
    (S.map (constantSheaf J AddCommGrpCat.{u})).ShortExact
```

**`constantSheaf_sections_shortExact_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantAbelianSheaf.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Sheafification/ConstantAbelianSheaf.lean#L279).

> **(2) Exactness as abelian presheaves.**
>
> The same induced sequence of constant sheaves is exact as a sequence of abelian
> presheaves: for every object `U` of `C`, the sequence of abelian groups obtained by
> taking sections over `U` is short exact. In particular `B → C` is objectwise surjective
> on sections.

```lean
theorem constantSheaf_sections_shortExact_of_shortExact
    (S : ShortComplex AddCommGrpCat.{u}) (hS : S.ShortExact) (U : C) :
    ((S.map (constantSheaf J AddCommGrpCat.{u})).map
        ((sheafSections J AddCommGrpCat.{u}).obj (op U))).ShortExact
```

## Tag 093K, a lemma

[Tag 093K](https://stacks.math.columbia.edu/tag/093K) in the Stacks Project.

**`Stacks.ConstantSheaf.bijective_tensorComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean, line 560](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean#L560).

> **Stacks Tag 093K.** Tensoring with a finitely presented external module commutes with taking
> sections of a constant sheaf: the canonical comparison is bijective.

```lean
theorem bijective_tensorComparison (M : ModuleCat.{x} R) (Q : ModuleCat.{y} R)
    [Module.FinitePresentation R Q] (N : ModuleCat.{x} R)
    (e : TensorProduct R M Q ≃ₗ[R] N) (U : C) :
    Function.Bijective (tensorComparison J M Q N e U).1
```

## Tag 093L, a lemma

[Tag 093L](https://stacks.math.columbia.edu/tag/093L) in the Stacks Project.

**`Stacks.ConstantSheaf.flat_constantSections`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean, line 709](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafModules.lean#L709).

> **Stacks Tag 093L.** On every object of a site, the sections of the constant sheaf associated
> to a flat module over a coherent ring form a flat module.

```lean
instance flat_constantSections [IsCoherentRing R] (M : ModuleCat.{x} R) [Module.Flat R M]
    (U : C) : Module.Flat R ((constantSections J U).obj M)
```

## Tag 093M, a lemma

[Tag 093M](https://stacks.math.columbia.edu/tag/093M) in the Stacks Project.

**`Stacks.ConstantSheaf.completedConstantSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean#L126). The attribute's comment: “the completed constant sheaf lim (R/Iⁿ)̲”.

> The completed constant sheaf `R̲^∧ = lim (R/Iⁿ)̲`.

```lean
noncomputable def completedConstantSheaf : Sheaf J (ModuleCat.{w} R)
```

**`Stacks.ConstantSheaf.completedConstantSheafStructureMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean#L141). The attribute's comment: “the canonical map from the constant sheaf to its completion”.

> The canonical map `R̲ ⟶ R̲^∧` from the constant sheaf to its completion.

```lean
noncomputable def completedConstantSheafStructureMap :
    (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R R) ⟶ completedConstantSheaf J I
```

**`Stacks.ConstantSheaf.completedConstantIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean#L277). The attribute's comment: “the completed ideal sheaf I̲^∧ = lim (I/Iⁿ)̲”.

> The completed constant ideal sheaf `I̲^∧ = lim (I/Iⁿ)̲`.

```lean
noncomputable def completedConstantIdealSheaf : Sheaf J (ModuleCat.{w} R)
```

**`Stacks.ConstantSheaf.flat_completedConstantSheaf_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean#L384). The attribute's comment: “Γ(U, R̲^∧) is a flat R-module for every U, the first step of the flatness proof”.

> On every object of the site the sections of the completed constant sheaf form a flat
> `R`-module.

```lean
theorem flat_completedConstantSheaf_sections (U : C) :
    Module.Flat R
      (((sheafSections J (ModuleCat.{w} R)).obj (op U)).obj (completedConstantSheaf J I))
```

**`Stacks.ConstantSheaf.isFlat_completedConstantSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletion.lean#L420). The attribute's comment: “R̲^∧ is flat over R̲”.

> The completed constant sheaf `R̲^∧ = lim (R/Iⁿ)̲` is flat over the constant
> sheaf of rings `R̲`. By Tags 03ES and 03ET this follows from the objectwise flatness of
> `flat_completedConstantSheaf_sections`.

```lean
theorem isFlat_completedConstantSheaf :
    AlgebraicGeometry.SheafOfModules.IsFlat (completedConstantSheafOverConstantRing J I)
```

**`Stacks.ConstantSheaf.constantTensorAction_comp_completedConstantSheafResidueMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean#L234). The attribute's comment: “I̲ Λ̂ ⊂ Î”.

> **Stacks 093M**, the inclusion `I̲ · R̲^∧ ⊂ I̲^∧`: the canonical map `R̲^∧ ⟶ (R/I)̲`, read
> over `Osharp`, kills the multiplication `I̲ ⊗_{Osharp} R̲^∧ ⟶ R̲^∧`. Since `I̲^∧` is the kernel
> of that canonical map, this says that the product of the constant sheaf of ideals with the
> completed constant sheaf is contained in the completed constant ideal sheaf.
>
> The multiplication is killed by any map annihilating every constant multiple, and the residue
> map is such a map: an element of `I` acts as zero on `(R/I)̲`, hence `a (m)` acts as zero on its
> bridge.

```lean
theorem constantTensorAction_comp_completedConstantSheafResidueMap :
    constantTensorAction J a (ModuleCat.ofHom I.subtype) (completedConstantSheaf J I) ≫
        sheafOfModulesOfConstantRingMap J (associatedRingMap J a)
          (completedConstantSheafResidueMap J I) = 0
```

**`Stacks.ConstantSheaf.idealSmulMap_comp_of_constantTensorAction_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean#L264). The attribute's comment: “I Λ̂ ⊂ I̲ Λ̂”.

> **Stacks 093M**, the inclusion `I F ⊂ I̲ · F`: a map out of `F` over `Osharp` which kills the
> multiplication `I̲ ⊗_{Osharp} F ⟶ F` also kills the map `∐_{f ∈ I} F ⟶ F` of multiplication by
> the elements of `I`, whose image is `I F`.
>
> Multiplying by a single element of `I` is tested on the images of the sheafification unit, where
> the multiplication's value is known; the passage from the elements of `I` to the single map out
> of the coproduct is the preservation of coproducts by the bridge, read off its adjunction.

```lean
theorem idealSmulMap_comp_of_constantTensorAction_comp_eq_zero (F : Sheaf J (ModuleCat.{w} R))
    {Z : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Osharp)}
    (g : (sheafOfModulesOfConstantRingFunctor J (associatedRingMap J a)).obj F ⟶ Z)
    (hg : constantTensorAction J a (ModuleCat.ofHom I.subtype) F ≫ g = 0) :
    (sheafOfModulesOfConstantRingFunctor J (associatedRingMap J a)).map
        (idealSmulMap J I F) ≫ g = 0
```

**`Stacks.ConstantSheaf.isColimitCokernelCoforkConstantTensorAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean#L345). The attribute's comment: “Λ̂/I̲ Λ̂ = (Λ/I)̲”.

> **Stacks 093M**, the identification `R̲^∧/I̲ · R̲^∧ = (R/I)̲`: the canonical map
> `R̲^∧ ⟶ (R/I)̲`, read as a map of sheaves of modules over `Osharp`, is a cokernel of the
> multiplication `I̲ ⊗_{Osharp} R̲^∧ ⟶ R̲^∧` by the constant sheaf of ideals `I̲`.
>
> A map out of the bridge of `R̲^∧` which kills the multiplication kills the multiplications by
> the elements of `I` as well, so its transpose across the bridge adjunction factors through
> `(R/I)̲` by the identification `R̲^∧/I R̲^∧ = (R/I)̲`; transposing back gives the
> factorisation, which is unique because the canonical map is an epimorphism.

```lean
noncomputable def isColimitCokernelCoforkConstantTensorAction :
    IsColimit (CokernelCofork.ofπ
      ((sheafOfModulesOfConstantRingFunctor J (associatedRingMap J a)).map
        (completedConstantSheafResidueMap J I))
      (constantTensorAction_comp_completedConstantSheafResidueMap J a I))
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByConstantIdealSmul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean, line 393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean#L393). The attribute's comment: “Λ̂/I̲ Λ̂ = (Λ/I)̲”.

> **Stacks 093M.** The canonical isomorphism `R̲^∧/I̲ · R̲^∧ ≅ (R/I)̲` from the quotient of the
> completed constant sheaf by the product of the constant sheaf of ideals with it to the constant
> sheaf of the quotient ring, as sheaves of modules over `Osharp`.

```lean
noncomputable def completedConstantSheaf_quotientByConstantIdealSmul :
    cokernel (constantTensorAction J a (ModuleCat.ofHom I.subtype)
        (completedConstantSheaf J I)) ≅
      (sheafOfModulesOfConstantRingFunctor J (associatedRingMap J a)).obj
        ((constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I)))
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByConstantIdealSmul_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionConstantIdealAction.lean#L407). The attribute's comment: “Λ̂/I̲ Λ̂ = (Λ/I)̲”.

> **Stacks 093M.** The isomorphism `R̲^∧/I̲ · R̲^∧ ≅ (R/I)̲` intertwines the cokernel
> projection with the canonical map `R̲^∧ ⟶ (R/I)̲`, so it is the identification of Tag 093M and
> not a bare existence statement.

```lean
theorem completedConstantSheaf_quotientByConstantIdealSmul_hom_comp :
    cokernel.π (constantTensorAction J a (ModuleCat.ofHom I.subtype)
          (completedConstantSheaf J I)) ≫
        (completedConstantSheaf_quotientByConstantIdealSmul J a I).hom =
      (sheafOfModulesOfConstantRingFunctor J (associatedRingMap J a)).map
        (completedConstantSheafResidueMap J I)
```

**`Stacks.ConstantSheaf.range_sections_completedConstantIdealSheafInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean#L293). The attribute's comment: “I Λ̂(U) = Î(U) on every object”.

> On every object `U` of the site the sections of the completed constant ideal sheaf inside
> `Γ(U, R̲^∧)` are exactly `I · Γ(U, R̲^∧)`.

```lean
theorem range_sections_completedConstantIdealSheafInclusion (U : C) :
    LinearMap.range (((sheafSections J (ModuleCat.{w} R)).obj (op U)).map
        (completedConstantIdealSheafInclusion J I)).hom =
      I • (⊤ : Submodule R (((sheafSections J (ModuleCat.{w} R)).obj (op U)).obj
        (completedConstantSheaf J I)))
```

**`Stacks.ConstantSheaf.epi_completedConstantIdealSheafLift`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean, line 363](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean#L363). The attribute's comment: “I Λ̂ = Î”.

> The elements of `I` generate the completed constant ideal sheaf over the completed constant
> sheaf: the factorisation of `∐_{f ∈ I} R̲^∧ ⟶ R̲^∧` through `I̲^∧` is an epimorphism, i.e.
> `I · R̲^∧ = I̲^∧` as subsheaves of `R̲^∧`.

```lean
instance epi_completedConstantIdealSheafLift : Epi (completedConstantIdealSheafLift J I)
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByIdealSmul`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean, line 378](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean#L378). The attribute's comment: “Λ̂/IΛ̂ = (Λ/I)̲”.

> The canonical isomorphism `R̲^∧/I R̲^∧ ≅ (R/I)̲` from the quotient of the completed constant
> sheaf by the ideal it is completed at to the constant sheaf of the quotient ring.

```lean
noncomputable def completedConstantSheaf_quotientByIdealSmul :
    cokernel (idealSmulMap J I (completedConstantSheaf J I)) ≅
      (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I))
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByIdealSmul_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionIdealAction.lean#L389). The attribute's comment: “Λ̂/IΛ̂ = (Λ/I)̲”.

> The isomorphism `R̲^∧/I R̲^∧ ≅ (R/I)̲` carries the cokernel projection to the canonical map
> `R̲^∧ ⟶ (R/I)̲`.

```lean
theorem completedConstantSheaf_quotientByIdealSmul_hom_comp :
    cokernel.π (idealSmulMap J I (completedConstantSheaf J I)) ≫
        (completedConstantSheaf_quotientByIdealSmul J I).hom =
      completedConstantSheafResidueMap J I
```

**`Stacks.ConstantSheaf.completedConstantSheafResidueMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean#L337). The attribute's comment: “the canonical map from the completion to the constant sheaf of Λ/I”.

> The canonical map `R̲^∧ ⟶ (R/I)̲` from the completed constant sheaf to the constant sheaf of
> the quotient ring: the projection to the level `n = 1` of the completion, followed by the
> identification `R/I¹ = R/I`.

```lean
noncomputable def completedConstantSheafResidueMap :
    completedConstantSheaf J I ⟶
      (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I))
```

**`Stacks.ConstantSheaf.shortExact_completedConstantIdealShortComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean, line 514](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean#L514). The attribute's comment: “the completed ideal sheaf is the kernel of the map from the completion to (Λ/I)̲”.

> The sequence `0 → I̲^∧ → R̲^∧ → (R/I)̲ → 0` of sheaves of `R`-modules is short exact.

```lean
theorem shortExact_completedConstantIdealShortComplex :
    (completedConstantIdealShortComplex J I).ShortExact
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByCompletedIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean, line 522](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean#L522). The attribute's comment: “Λ̂/Î = (Λ/I)̲”.

> The canonical isomorphism `R̲^∧/I̲^∧ ≅ (R/I)̲` from the quotient of the completed constant
> sheaf by the completed constant ideal sheaf to the constant sheaf of the quotient ring.

```lean
noncomputable def completedConstantSheaf_quotientByCompletedIdeal :
    cokernel (completedConstantIdealSheafInclusion J I) ≅
      (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I))
```

**`Stacks.ConstantSheaf.completedConstantSheaf_quotientByCompletedIdeal_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean, line 531](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafCompletionQuotient.lean#L531). The attribute's comment: “Λ̂/Î = (Λ/I)̲”.

> The isomorphism `R̲^∧/I̲^∧ ≅ (R/I)̲` intertwines the cokernel projection with the canonical
> map `R̲^∧ ⟶ (R/I)̲`.

```lean
theorem completedConstantSheaf_quotientByCompletedIdeal_hom_comp :
    cokernel.π (completedConstantIdealSheafInclusion J I) ≫
        (completedConstantSheaf_quotientByCompletedIdeal J I).hom =
      completedConstantSheafResidueMap J I
```

**`Stacks.ConstantSheaf.constantSheaf_idealAction_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean#L91). The attribute's comment: “sections of the ideal subsheaf”.

> The image of the constant ideal sheaf on each object is the ideal acting on sections of the
> constant ring sheaf.

```lean
theorem constantSheaf_idealAction_sections (U : C) :
    LinearMap.range
      ((constantSheaf J (ModuleCat.{w} R) ⋙
        (sheafSections J (ModuleCat.{w} R)).obj (op U)).map
          (ModuleCat.ofHom I.subtype)).hom =
      I • (⊤ : Submodule R
        ((constantSheaf J (ModuleCat.{w} R) ⋙
          (sheafSections J (ModuleCat.{w} R)).obj (op U)).obj (ModuleCat.of R R)))
```

**`Stacks.ConstantSheaf.constantSheaf_quotientByConstantIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean#L198). The attribute's comment: “quotient by the constant ideal sheaf”.

> The canonical isomorphism from the quotient by the constant ideal sheaf to the constant sheaf
> of the quotient ring.

```lean
noncomputable def constantSheaf_quotientByConstantIdeal :
    let f := (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.subtype)
    cokernel f ≅ (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I))
```

**`Stacks.ConstantSheaf.constantSheaf_quotientByConstantIdeal_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean#L220). The attribute's comment: “quotient by the constant ideal sheaf”.

> The quotient isomorphism intertwines the cokernel projection with the constant sheaf of the
> ring quotient map.

```lean
theorem constantSheaf_quotientByConstantIdeal_hom_comp :
    let f := (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.subtype)
    cokernel.π f ≫ (constantSheaf_quotientByConstantIdeal J I).hom =
      (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.mkQ)
```

**`Stacks.ConstantSheaf.constantSheaf_quotientByIdealAction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean#L258). The attribute's comment: “quotient by the ideal subsheaf”.

> The canonical isomorphism from the quotient by the image ideal subsheaf, equivalently the
> ideal generated by `I` in the constant ring sheaf, to the constant sheaf of the quotient ring.

```lean
noncomputable def constantSheaf_quotientByIdealAction :
    let f := (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.subtype)
    cokernel (image.ι f) ≅
      (constantSheaf J (ModuleCat.{w} R)).obj (ModuleCat.of R (R ⧸ I))
```

**`Stacks.ConstantSheaf.constantSheaf_quotientByIdealAction_hom_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafQuotient.lean#L269). The attribute's comment: “quotient by the ideal subsheaf”.

> The image-ideal quotient isomorphism intertwines its quotient projection with the constant
> sheaf of the ring quotient map.

```lean
theorem constantSheaf_quotientByIdealAction_hom_comp :
    let f := (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.subtype)
    cokernel.π (image.ι f) ≫ (constantSheaf_quotientByIdealAction J I).hom =
      (constantSheaf J (ModuleCat.{w} R)).map (ModuleCat.ofHom I.mkQ)
```

## Tag 093N, a lemma

[Tag 093N](https://stacks.math.columbia.edu/tag/093N) in the Stacks Project.

**`Stacks.SheafOfModules.Constant.constantModuleSheaf_isFiniteType_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafFiniteness.lean, line 870](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafFiniteness.lean#L870). The attribute's comment: “finite_type”.

> **Stacks Project, Tag 093N, part (1).** On a site whose topos is not empty, a constant sheaf
> of modules is of finite type if and only if its value is a finitely generated module.

```lean
theorem constantModuleSheaf_isFiniteType_iff
    [∀ U : C, HasWeakSheafify (J.over U) AddCommGrpCat.{w}]
    [∀ U : C, (J.over U).WEqualsLocallyBijective AddCommGrpCat.{w}]
    (hJ : ∃ U : C, ¬ (⊥ : Sieve U) ∈ J U) (M : ModuleCat.{w} R) :
    SheafOfModules.IsFiniteType (constantModuleSheaf J M) ↔ ModuleCat.isFG R M
```

**`Stacks.SheafOfModules.Constant.constantModuleSheaf_isFinitePresentation_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafFinitePresentation.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ConstantSheafFinitePresentation.lean#L141). The attribute's comment: “finite_presentation”.

> **Stacks Project, Tag 093N, part (2).** On a site with an object that is not sheaf
> theoretically empty, a constant sheaf of modules is of finite presentation if and only if its
> value is a finitely presented module.

```lean
theorem constantModuleSheaf_isFinitePresentation_iff
    (hJ : ∃ U : C, ¬ (⊥ : Sieve U) ∈ J U) (M : ModuleCat.{w} R) :
    SheafOfModules.IsFinitePresentation (constantModuleSheaf J M) ↔
      Module.FinitePresentation R M
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.42, Tag 093I](https://stacks.math.columbia.edu/tag/093I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
