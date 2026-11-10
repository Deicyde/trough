---
declaration: section
origin: cited
lean: internalHom_isSheaf, Stacks.SheafOfModules.InternalHom.internalHomOverIso, Stacks.SheafOfModules.InternalHom.internalHomOverIso_hom_app, Stacks.SheafOfModules.InternalHom.pullbackInternalHomMap, Stacks.SheafOfModules.InternalHom.adjointPullbackInternalHomMap, Stacks.SheafOfModules.InternalHom.tensorEvaluation_pullbackInternalHomMap, Stacks.SheafOfModules.InternalHom.toposPullbackInternalHomMap_compOf, Stacks.SheafOfModules.InternalHom.toposPullbackInternalHomMap_comp
statement: formalized
proof: formalized
---

# 18.27 Internal Hom

Section 18.27 of the Stacks Project, [Tag 04TT](https://stacks.math.columbia.edu/tag/04TT). 12 tags here are carried by 47 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03EM, a lemma

[Tag 03EM](https://stacks.math.columbia.edu/tag/03EM) in the Stacks Project.

**`internalHom_isSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHom.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHom.lean#L625). References: EGA 0 (4.1.5), “partial”; SGA 4 IV (12.4), “sheaf property”; SGA 3 IV (4.5.13), “special case”; SGA 4 IV (12.1), “partial”; SGA 4 IV (12.2), “Hom_A(M”; SGA 4 IV (12.5), “more general”.

> Let `O` be a presheaf of commutative rings on a site `C`, let `F` be a presheaf of
> `O`-modules and let `G` be a sheaf of `O`-modules. Then the internal hom presheaf
> `𝓗om_O(F, G) = internalHom O F G` is a sheaf of `O`-modules, i.e. its underlying abelian
> presheaf is a sheaf.

```lean
theorem internalHom_isSheaf
    (hG : Presheaf.IsSheaf J G.presheaf) :
    Presheaf.IsSheaf J (internalHom O F G).presheaf
```

## Tag 0E8H, a lemma

[Tag 0E8H](https://stacks.math.columbia.edu/tag/0E8H) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.internalHomOverIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomRestriction.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomRestriction.lean#L170).

> **Stacks 0E8H.** Internal Hom commutes with restriction to the localized site over `U`.

```lean
noncomputable def internalHomOverIso
    (X : RingedSite.{u, v, w}) (U : X.C)
    (F G : _root_.SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    (restrFun X.O.obj U).obj (internalHom X.O.obj F.val G.val) ≅
      internalHom (X.O.over U).obj
        ((restrFun X.O.obj U).obj F.val)
        ((restrFun X.O.obj U).obj G.val)
```

**`Stacks.SheafOfModules.InternalHom.internalHomOverIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomRestriction.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomRestriction.lean#L203). The attribute's comment: “canonical component on sections”.

> At `V ⟶ U`, the isomorphism of Stacks 0E8H restricts a local morphism along the
> iterated-slice functor `(C/U)/V ⥤ C/V`.

```lean
theorem internalHomOverIso_hom_app
    (X : RingedSite.{u, v, w}) (U : X.C)
    (F G : _root_.SheafOfModules.{m} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (V : (Over U)ᵒᵖ)
    (α : ((restrFun X.O.obj U).obj (internalHom X.O.obj F.val G.val)).obj V)
    (W : (Over V.unop)ᵒᵖ)
    (x : ((restrFun (X.O.over U).obj V.unop).obj
      ((restrFun X.O.obj U).obj F.val)).obj W) :
    ((((internalHomOverIso X U F G).hom.app V).hom α).app W).hom x =
      (α.app ((Over.iteratedSliceForward V.unop).op.obj W)).hom x
```

## Tag 0GMX, a remark

[Tag 0GMX](https://stacks.math.columbia.edu/tag/0GMX) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.pullbackInternalHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean#L214). The attribute's comment: “the canonical map”.

> **Stacks 0GMX.** The canonical map `f^* Hom_{O_D}(F, G) ⟶ Hom_{O_C}(f^*F, f^*G)` attached
> to a morphism of ringed sites: the transpose, under the correspondence of Stacks 03EO, of the
> pullback of the evaluation morphism.

```lean
noncomputable def pullbackInternalHomMap :
    (ringedSitePullback f).obj ((internalHomSecondFunctor Y.J Y.O F).obj G) ⟶
      (internalHomSecondFunctor X.J X.O ((ringedSitePullback f).obj F)).obj
        ((ringedSitePullback f).obj G)
```

**`Stacks.SheafOfModules.InternalHom.adjointPullbackInternalHomMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean#L226). The attribute's comment: “the adjoint map”.

> **Stacks 0GMX.** The map `Hom_{O_D}(F, G) ⟶ f_* Hom_{O_C}(f^*F, f^*G)` displayed in the
> source: the adjoint of `pullbackInternalHomMap` under the adjunction `f^* ⊣ f_*` of
> Stacks 03D7.

```lean
noncomputable def adjointPullbackInternalHomMap :
    (internalHomSecondFunctor Y.J Y.O F).obj G ⟶
      (ringedSitePushforward f).obj
        ((internalHomSecondFunctor X.J X.O ((ringedSitePullback f).obj F)).obj
          ((ringedSitePullback f).obj G))
```

**`Stacks.SheafOfModules.InternalHom.tensorEvaluation_pullbackInternalHomMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomPullback.lean#L238). The attribute's comment: “compatibility of the canonical map with evaluation”.

> **Stacks 0GMX.** The canonical map is compatible with evaluation: tensoring it with `f^*F`
> and then evaluating `Hom_{O_C}(f^*F, f^*G)` gives the pulled-back evaluation of
> `Hom_{O_D}(F, G)`.

```lean
theorem tensorEvaluation_pullbackInternalHomMap :
    tensorEvaluation X.O ((ringedSitePullback f).obj F) ((ringedSitePullback f).obj G)
        (pullbackInternalHomMap f F G) =
      pullbackEvaluation f F G
```

**`Stacks.SheafOfModules.InternalHom.toposPullbackInternalHomMap_compOf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomCompData.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomCompData.lean#L171). The attribute's comment: “compatibility of the canonical map with composition, for a composite given as data”.

> **The canonical map is compatible with composition, with the composite supplied as
> data.** Let `φ : X ⟶ Y` and `ψ : Y ⟶ Z` be morphisms of ringed topoi between the
> topoi of three ringed sites, let `χ : X ⟶ Z` play the role of their composite and let `τ` be a
> comparison of the geometric direct images carrying the composite structure map to the structure
> map of `χ`. Then the canonical map
>
> `χ^* Hom_{O_Z}(F, G) ⟶ Hom_{O_X}(χ^*F, χ^*G)`
>
> is the canonical map of `ψ` pulled back along `φ`, followed by the canonical map of `φ`, read
> through the comparison of pullbacks attached to `(χ, τ)` at `Hom_{O_Z}(F, G)`, at the source of
> the internal Hom sheaf — through `internalHomPre`, the comparison in the first variable — and at
> its target.

```lean
theorem toposPullbackInternalHomMap_compOf
    (F G : SheafOfModules.{u} (Tensor.ringSheaf Z.O)) :
    toposPullbackInternalHomMap χ F G =
      toposPullbackCompComparisonOf φ ψ χ τ hτ ((internalHomSecondFunctor Z.J Z.O F).obj G) ≫
        (toposPullback φ).map (toposPullbackInternalHomMap ψ F G) ≫
          toposPullbackInternalHomMap φ ((toposPullback ψ).obj F) ((toposPullback ψ).obj G) ≫
            (internalHomPre X.O (toposPullbackCompComparisonOf φ ψ χ τ hτ F)).app
                ((toposPullback φ).obj ((toposPullback ψ).obj G)) ≫
              (internalHomSecondFunctor X.J X.O ((toposPullback χ).obj F)).map
                (toposPullbackCompComparisonInvOf φ ψ χ τ hτ G)
```

**`Stacks.SheafOfModules.InternalHom.toposPullbackInternalHomMap_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomCompMap.lean, line 413](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomCompMap.lean#L413). The attribute's comment: “compatibility of the canonical map with composition”.

> **The canonical map of Stacks 0GMX is compatible with composition.** For morphisms of ringed
> topoi `φ : X ⟶ Y` and `ψ : Y ⟶ Z` between the topoi of three ringed sites and sheaves of
> `O_Z`-modules `F`, `G`, the canonical map
>
> `(ψ ∘ φ)^* Hom_{O_Z}(F, G) ⟶ Hom_{O_X}((ψ ∘ φ)^*F, (ψ ∘ φ)^*G)`
>
> of the composite is the canonical map of `ψ` pulled back along `φ`, followed by the canonical
> map of `φ`, read through the comparison of pullbacks along a composite at `Hom_{O_Z}(F, G)`, at
> the source of the internal Hom sheaf — through `internalHomPre`, the comparison in the first
> variable — and at its target.
>
> This is the law the localization square of Stacks 04J0 reduces to, and it is proved by the route
> the source's Remark 18.27.3 indicates: `tensorEvaluation_injective` turns it into an identity
> between two morphisms out of `(ψ ∘ φ)^*Hom_{O_Z}(F, G) ⊗_{O_X} (ψ ∘ φ)^*F`, where
> `tensorEvaluation_comp` and `tensorEvaluation_comp_internalHomPre_comp_map` read the composite
> route off and `toposPullbackEvaluationExchange` assembles the four inputs — the exchange of
> tensorings `sheafTensor_exchange_three`, the pulled-back tensor--evaluation composite
> `toposPullback_tensorEvaluation`, the naturality
> `toposPullbackCompComparisonInv_naturality_pullbackTensorIso` transported along the two readings
> of the inner pulled-back evaluation, and the composition law of Stacks 03EL
> `pullbackTensorIso_inv_app_toposCompHom` with the comparison of pullbacks cancelled off it by
> `cancelWhisker`.

```lean
theorem toposPullbackInternalHomMap_comp
    (F G : SheafOfModules.{u} (Tensor.ringSheaf Z.O)) :
    toposPullbackInternalHomMap (toposCompHom φ ψ) F G =
      toposPullbackCompComparison φ ψ ((internalHomSecondFunctor Z.J Z.O F).obj G) ≫
        (toposPullback φ).map (toposPullbackInternalHomMap ψ F G) ≫
          toposPullbackInternalHomMap φ ((toposPullback ψ).obj F) ((toposPullback ψ).obj G) ≫
            (internalHomPre X.O (toposPullbackCompComparison φ ψ F)).app
                ((toposPullback φ).obj ((toposPullback ψ).obj G)) ≫
              (internalHomSecondFunctor X.J X.O ((toposPullback (toposCompHom φ ψ)).obj F)).map
                (toposPullbackCompComparisonInv φ ψ G)
```

**`Stacks.SheafOfModules.InternalHom.toposPullbackInternalHomMap_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 999](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L999). The attribute's comment: “functoriality of the canonical map in the first variable”.

> **The canonical map of Stacks 0GMX is functorial in its first variable.** For a morphism
> `c : F' ⟶ F` of sheaves of `O_Y`-modules the square built from the canonical maps at `F` and at
> `F'` and from the comparison `internalHomPre` in the first variable on the two sites commutes.
>
> This is the "functoriality of Remark 18.27.3" that the proof of Stacks 0GN2 cites. By
> `tensorEvaluation_injective` it is an identity between two morphisms out of a tensor product,
> and there it is the naturality of the comparison of Stacks 03EL in its second variable: both
> sides become the pulled-back evaluation of `Hom_{O_Y}(F, G)` precomposed with `c`.

```lean
theorem toposPullbackInternalHomMap_naturality
    {F F' : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := Y.J)) Y.O)}
    (c : F' ⟶ F) :
    toposPullbackInternalHomMap φ F G ≫
        (internalHomPre X.O ((toposPullback φ).map c)).app ((toposPullback φ).obj G) =
      (toposPullback φ).map ((internalHomPre Y.O c).app G) ≫
        toposPullbackInternalHomMap φ F' G
```

**`Stacks.SheafOfModules.InternalHom.pullbackInternalHomNatural`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 1117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L1117). The attribute's comment: “first-variable functoriality, for a morphism of ringed sites”. References: EGA 0 (4.4.6), “Functoriality of γ♯”.

> **The canonical maps of Stacks 0GMX are functorial in the first variable.** For a morphism
> `c : F' ⟶ F` of sheaves of `O_D`-modules the square built from the canonical maps at `F` and at
> `F'` and from the comparison `internalHomPre` on the two sites commutes.
>
> This is the "functoriality of Remark 18.27.3" that the proof of Stacks 0GN2 cites. It is
> `toposPullbackInternalHomMap_naturality` at the morphism of ringed topoi of `f`, the two
> readings of the canonical map agreeing by `toposPullbackInternalHomMap_ringedToposHom`.

```lean
theorem pullbackInternalHomNatural
    {F F' : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := Y.J)) Y.O)}
    (c : F' ⟶ F) :
    pullbackInternalHomMap f F G ≫
        (internalHomPre X.O ((ringedSitePullback f).map c)).app
          ((ringedSitePullback f).obj G) =
      (ringedSitePullback f).map ((internalHomPre Y.O c).app G) ≫
        pullbackInternalHomMap f F' G
```

## Tag 03EN, a lemma

[Tag 03EN](https://stacks.math.columbia.edu/tag/03EN) in the Stacks Project.

**`Stacks.PresheafOfModules.InternalHom.internalHomFunctor_preservesColimitsOfShape`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomVariance.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomVariance.lean#L326). The attribute's comment: “presheaf_first_variable”.

> For a fixed target `G`, internal Hom in the first variable sends arbitrary colimits of
> presheaves of `O`-modules to limits.

```lean
noncomputable instance internalHomFunctor_preservesColimitsOfShape
    (G : _root_.PresheafOfModules.{max u v} (Oforget O)) (I : Type w) [Category.{w} I] :
    PreservesColimitsOfShape I (internalHomFunctor O G)
```

**`Stacks.PresheafOfModules.InternalHom.internalHomSecondFunctor_preservesLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomVariance.lean, line 566](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomVariance.lean#L566). The attribute's comment: “presheaf_second_variable”.

> Internal Hom with fixed first variable commutes with arbitrary limits.

```lean
noncomputable instance internalHomSecondFunctor_preservesLimits :
    PreservesLimits (internalHomSecondFunctor.{v, u, w, m} O F)
```

**`Stacks.SheafOfModules.InternalHom.internalHomSecondFunctor_preservesLimits`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomVariance.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomVariance.lean#L89). The attribute's comment: “sheaf_second_variable”. References: SGA 4 IV (12.2), “partial”.

> **Stacks 03EN, sheaf case, second variable.** Internal Hom from a fixed sheaf of modules
> commutes with arbitrary limits.

```lean
noncomputable instance internalHomSecondFunctor_preservesLimits
    (F : _root_.SheafOfModules.{max u v w m} (Tensor.ringSheaf O)) :
    PreservesLimits (internalHomSecondFunctor.{v, u, w, m} J O F)
```

**`Stacks.SheafOfModules.InternalHom.sheafInternalHomFunctor_preservesColimitsOfShape`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariable.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariable.lean#L192). The attribute's comment: “sheaf_first_variable”. References: SGA 4 IV (12.2), “partial, special case”.

> **Stacks 03EN, sheaf case, first variable.** For a fixed target `G`, the internal Hom of
> sheaves of modules takes colimits in the first variable to limits.

```lean
public noncomputable instance sheafInternalHomFunctor_preservesColimitsOfShape
    (G : _root_.SheafOfModules.{max u v} (Tensor.ringSheaf O))
    (I : Type*) [Category I] :
    PreservesColimitsOfShape I (sheafInternalHomFunctor J O G)
```

**`Stacks.SheafOfModules.InternalHom.preservesFiniteColimits_internalHomFirstMate`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean, line 865](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/PullbackInternalHomFlat.lean#L865). The attribute's comment: “sheaf case, first variable, for the mate of the tensor comparison”. References: EGA 0 (6.7.6), “Left exactness of Hom(-”; SGA 4 IV (12.2), “partial, special case”.

> **Stacks 03EN in the first variable, for the mate.** Internal Hom into a fixed sheaf of
> modules, contravariant in its source, carries finite colimits of sheaves of modules to finite
> limits of internal Hom sheaves.
>
> This is the continuity that the proof of Stacks 0GN2 uses to pass from the structure sheaf to a
> finitely presented source, and it holds with no hypothesis: `internalHomFirstMate` is a left
> adjoint, by `internalHomFirstMateAdjunction`.

```lean
theorem preservesFiniteColimits_internalHomFirstMate :
    Limits.PreservesFiniteColimits (internalHomFirstMate O G)
```

## Tag 0GMY, a lemma

[Tag 0GMY](https://stacks.math.columbia.edu/tag/0GMY) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.ringedSite_sheafInternalHomObjMapLeft_mono_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariableLeftExact.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariableLeftExact.lean#L133). The attribute's comment: “exact_first_argument”. References: EGA 0 (4.1.5), “Injectivity of Hom(F”.

> **Stacks 0GMY, part (1).** Precomposition along an epimorphism is a monomorphism of
> internal Hom sheaves, which is the initial zero of the target sequence.

```lean
theorem ringedSite_sheafInternalHomObjMapLeft_mono_of_epi
    {F₁ F G : _root_.SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)}
    (g : F₁ ⟶ F) [Epi g] :
    Mono (sheafInternalHomObjMapLeft X.J X.O (G := G) g)
```

**`Stacks.SheafOfModules.InternalHom.ringedSite_sheafInternalHomObjMapLeft_exact_of_exact_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariableLeftExact.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/InternalHomSiteVariance/FirstVariableLeftExact.lean#L149). The attribute's comment: “exact_first_argument”.

> **Stacks 0GMY, part (1).** A right-exact sequence of sheaves of modules becomes exact at
> the middle term after applying internal Hom in the first argument.

```lean
theorem ringedSite_sheafInternalHomObjMapLeft_exact_of_exact_epi
    (S : ShortComplex (_root_.SheafOfModules.{max u v}
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (G : _root_.SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hS : S.Exact) [Epi S.g] :
    ∃ h : sheafInternalHomObjMapLeft X.J X.O (G := G) S.g ≫
        sheafInternalHomObjMapLeft X.J X.O (G := G) S.f = 0,
      (ShortComplex.mk (sheafInternalHomObjMapLeft X.J X.O (G := G) S.g)
        (sheafInternalHomObjMapLeft X.J X.O (G := G) S.f) h).Exact
```

Declarations registered for the tag:

- [`internalHomSecondFunctor_map_mono`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=internalHomSecondFunctor_map_mono#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomSecondVariable.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomSecondVariable.lean#L41) (StacksFrontier): “exact_second_argument”.
- [`internalHomSecondFunctor_exact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=internalHomSecondFunctor_exact#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomSecondVariable.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomSecondVariable.lean#L42) (StacksFrontier): “exact_second_argument”.

## Tag 03EO, a lemma

[Tag 03EO](https://stacks.math.columbia.edu/tag/03EO) in the Stacks Project.

**`Stacks.PresheafOfModules.InternalHom.presheafInternalHomTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean#L557). The attribute's comment: “presheaf_internal_hom_tensor_iso”.

> **Stacks 03EO.** The canonical currying isomorphism from internal Hom out of a tensor
> product to iterated internal Hom.

```lean
noncomputable def presheafInternalHomTensorIso :
    internalHom O (F ⊗ G) H ≅ internalHom O F (internalHom O G H)
```

**`Stacks.PresheafOfModules.InternalHom.presheafInternalHomTensorIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean#L570). The attribute's comment: “presheaf_internal_hom_tensor_iso”.

> On sections, the currying isomorphism is tensor currying: after restricting `x`, it
> evaluates the original morphism on `x ⊗ y`. This pins the isomorphism down, rather than merely
> asserting that some isomorphism exists.

```lean
theorem presheafInternalHomTensorIso_hom_app (a : (restrFun O U).obj (F ⊗ G) ⟶ (restrFun O U).obj H)
    {S : C} (p : S ⟶ U) (x : F.obj (op S)) {T : C} (q : T ⟶ S) (y : G.obj (op T)) :
    sectionOfRestr O H S q
        (((((((presheafInternalHomTensorIso O F G H).hom.app (op U)).hom a).app
            (op (Over.mk p))).hom (restrSection O F U p x)).app
              (op (Over.mk q))).hom (restrSection O G S q y)) =
      restrTensorHom O F G H U a (q ≫ p) (F.restrictₛₗ q.op x ⊗ₜ y)
```

**`Stacks.PresheafOfModules.InternalHom.presheafInternalHomTensorIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean#L636). The attribute's comment: “presheaf_internal_hom_tensor_iso”.

> **Stacks 03EO.** The currying isomorphism is natural contravariantly in its first tensor
> factor.

```lean
theorem presheafInternalHomTensorIso_natural_left
    {F' : _root_.PresheafOfModules.{max u v w} (Oforget O)} (f : F' ⟶ F) :
    (presheafInternalHomTensorIso O F G H).hom ≫
        internalHomMapLeft O f =
      internalHomMapLeft O (f ⊗ₘ 𝟙 G) ≫
        (presheafInternalHomTensorIso O F' G H).hom
```

**`Stacks.PresheafOfModules.InternalHom.presheafInternalHomTensorIso_natural_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean, line 665](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean#L665). The attribute's comment: “presheaf_internal_hom_tensor_iso”.

> **Stacks 03EO.** The currying isomorphism is natural contravariantly in its second tensor
> factor.

```lean
theorem presheafInternalHomTensorIso_natural_middle
    {G' : _root_.PresheafOfModules.{max u v w} (Oforget O)} (g : G' ⟶ G) :
    (presheafInternalHomTensorIso O F G H).hom ≫
        internalHomMapRight O F
          (internalHomMapLeft O g) =
      internalHomMapLeft O (𝟙 F ⊗ₘ g) ≫
        (presheafInternalHomTensorIso O F G' H).hom
```

**`Stacks.PresheafOfModules.InternalHom.presheafInternalHomTensorIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean, line 677](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/InternalHomTensorCurrying.lean#L677). The attribute's comment: “presheaf_internal_hom_tensor_iso”.

> **Stacks 03EO.** The currying isomorphism is natural covariantly in its target.

```lean
theorem presheafInternalHomTensorIso_natural_right
    {H' : _root_.PresheafOfModules.{max u v w} (Oforget O)} (hh : H ⟶ H') :
    internalHomMapRight O (F ⊗ G) hh ≫
        (presheafInternalHomTensorIso O F G H').hom =
      (presheafInternalHomTensorIso O F G H).hom ≫
        internalHomMapRight O F
          (internalHomMapRight O G hh)
```

**`Stacks.PresheafOfModules.InternalHom.presheafTensorHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunction.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunction.lean#L293). The attribute's comment: “presheaf_tensor_hom_adjunction”.

> **Stacks 03EO.** Tensoring on the right by `G` is left adjoint to the internal-Hom functor
> with source `G`. Packaging the canonical correspondence as an adjunction records its
> naturality in both remaining variables.

```lean
noncomputable def presheafTensorHomAdjunction :
    (tensoringRight (_root_.PresheafOfModules.{max u v w} (Oforget O))).obj G ⊣
      internalHomSecondFunctor.{v, u, max u v w, u} O G
```

**`Stacks.PresheafOfModules.InternalHom.presheafTensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunction.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunction.lean#L339). The attribute's comment: “presheaf_tensor_hom_adjunction”.

> **Stacks 03EO.** The hom-equivalence of `presheafTensorHomAdjunction` is the canonical
> currying map: on sections it sends `b` to the map taking `x` and `y` to `b (x ⊗ y)`.

```lean
theorem presheafTensorHomEquiv_apply (b : F ⊗ G ⟶ H) (U : C) (x : F.obj (op U))
    {T : C} (q : T ⟶ U) (y : G.obj (op T)) :
    sectionOfRestr O H U q
        (((((presheafTensorHomEquiv O F G H b).app (op U)).hom x).app
          (op (Over.mk q))).hom (restrSection O G U q y)) =
      globalTensorHom O F G H b T (F.restrictₛₗ q.op x ⊗ₜ y)
```

**`Stacks.PresheafOfModules.InternalHom.FreeUniverse.presheafTensorHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunctionFreeUniverse.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunctionFreeUniverse.lean#L509). The attribute's comment: “presheaf_tensor_hom_adjunction, with the universe of the sections of the structure presheaf independent of the universes of the site”.

> **Stacks 03EO.** Tensoring on the right by `G` is left adjoint to the internal-Hom functor
> with source `G`. Packaging the canonical correspondence as an adjunction records its
> naturality in both remaining variables.

```lean
noncomputable def presheafTensorHomAdjunction :
    (_root_.PresheafOfModules.tensorBifunctor O).flip.obj G ⊣
      internalHomSecondFunctor.{v, u, w, w} O G
```

**`Stacks.PresheafOfModules.InternalHom.FreeUniverse.presheafTensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunctionFreeUniverse.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/TensorHomAdjunctionFreeUniverse.lean#L557). The attribute's comment: “presheaf_tensor_hom_adjunction, with the universe of the sections of the structure presheaf independent of the universes of the site”.

> **Stacks 03EO.** The hom-equivalence of `presheafTensorHomAdjunction` is the canonical
> currying map: on sections it sends `b` to the map taking `x` and `y` to `b (x ⊗ y)`.

```lean
theorem presheafTensorHomEquiv_apply (b : F.tensorObj G ⟶ H) (U : C) (x : F.obj (op U))
    {T : C} (q : T ⟶ U) (y : G.obj (op T)) :
    sectionOfRestr O H U q
        (((((presheafTensorHomEquiv O F G H b).app (op U)).hom x).app
          (op (Over.mk q))).hom (restrSection O G U q y)) =
      globalTensorHom O F G H b T (F.restrictₛₗ q.op x ⊗ₜ y)
```

**`Stacks.SheafOfModules.InternalHom.sheafCurryIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean, line 242](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean#L242). The attribute's comment: “sheaf_internal_hom_tensor_iso”.

> **Stacks 03EO, sheaf case.** The canonical currying isomorphism for the sheafified tensor
> product and the internal Hom sheaf.

```lean
noncomputable def sheafCurryIso :
    siteSheafInternalHom J O (((Stacks.SheafOfModules.Tensor.sheafTensor O).obj F).obj G) H ≅
      siteSheafInternalHom J O F (siteSheafInternalHom J O G H)
```

**`Stacks.SheafOfModules.InternalHom.sheafCurryIso_hom_app_tmul`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean, line 287](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean#L287). The attribute's comment: “sheaf_internal_hom_tensor_iso”.

> **Stacks 03EO, sheaf case.** The canonical isomorphism is tensor currying on every local
> pure tensor.

```lean
theorem sheafCurryIso_hom_app_tmul (U : C)
    (s : (siteSheafInternalHom J O
      (((Stacks.SheafOfModules.Tensor.sheafTensor O).obj F).obj G) H).val.obj (op U))
    (f : F.val.obj (op U)) (g : G.val.obj (op U)) :
    ((((((sheafCurryIso O F G H).hom.val.app (op U)).hom s).app
        (op (Over.mk (𝟙 U)))).hom f).app (op (Over.mk (𝟙 U)))).hom g =
      (s.app (op (Over.mk (𝟙 U)))).hom
        (toSheafTensorSection O F G U (f ⊗ₜ[O.obj.obj (op U)] g))
```

**`Stacks.SheafOfModules.InternalHom.sheafCurryIso_natural_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean#L305). The attribute's comment: “sheaf_internal_hom_tensor_iso”.

> **Stacks 03EO, sheaf case.** Currying is contravariantly natural in the first tensor
> factor.

```lean
theorem sheafCurryIso_natural_left
    {F F' :
      _root_.SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) O)}
    (f : F' ⟶ F) :
    (sheafCurryIso O F G H).hom ≫ sheafInternalHomMapLeft J O f =
      sheafInternalHomMapLeft J O (sheafTensorMap O f (𝟙 G)) ≫
        (sheafCurryIso O F' G H).hom
```

**`Stacks.SheafOfModules.InternalHom.sheafCurryIso_natural_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean#L322). The attribute's comment: “sheaf_internal_hom_tensor_iso”.

> **Stacks 03EO, sheaf case.** Currying is contravariantly natural in the second tensor
> factor.

```lean
theorem sheafCurryIso_natural_middle
    {G G' :
      _root_.SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) O)}
    (g : G' ⟶ G) :
    (sheafCurryIso O F G H).hom ≫
        sheafInternalHomMapRight O (sheafInternalHomMapLeft J O g) =
      sheafInternalHomMapLeft J O (sheafTensorMap O (𝟙 F) g) ≫
        (sheafCurryIso O F G' H).hom
```

**`Stacks.SheafOfModules.InternalHom.sheafCurryIso_natural_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/InternalHomTensorCurrying.lean#L340). The attribute's comment: “sheaf_internal_hom_tensor_iso”.

> **Stacks 03EO, sheaf case.** Currying is covariantly natural in the target.

```lean
theorem sheafCurryIso_natural_right
    {H H' :
      _root_.SheafOfModules.{max u v} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := J)) O)}
    (h : H ⟶ H') :
    sheafInternalHomMapRight O h ≫ (sheafCurryIso O F G H').hom =
      (sheafCurryIso O F G H).hom ≫
        sheafInternalHomMapRight O (sheafInternalHomMapRight O h)
```

**`Stacks.SheafOfModules.InternalHom.FreeUniverse.sheafTensorRightHomAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorHomAdjunctionFreeUniverse.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorHomAdjunctionFreeUniverse.lean#L95). The attribute's comment: “sheaf_tensor_hom_adjunction, with the universe of the sections of the structure sheaf independent of the universes of the site”.

> **Stacks 03EO, sheaf case, at a free ring universe.**  Tensoring on the right by `G` is left
> adjoint to the internal-Hom functor with source `G`, for a sheaf of rings whose sections lie in
> a universe independent of those of the site.
>
> The presheaf clause
> `Stacks.PresheafOfModules.InternalHom.FreeUniverse.presheafTensorHomAdjunction` is composed
> with the sheafification adjunction and the result restricted along the fully faithful forgetful
> functor; this is legitimate because the right adjoint of the composite already takes values in
> sheaves, the internal Hom of Stacks 03EM being a sheaf as soon as its target is.

```lean
def sheafTensorRightHomAdjunction :
    (Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max u v w, max u v w} R).flip.obj G ⊣
      internalHomSecondFunctor.{v, u, w, w} J R G
```

**`Stacks.SheafOfModules.InternalHom.FreeUniverse.sheafTensorHomEquiv_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorHomAdjunctionFreeUniverse.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/TensorHomAdjunctionFreeUniverse.lean#L129). The attribute's comment: “sheaf_tensor_hom_adjunction, with the universe of the sections of the structure sheaf independent of the universes of the site”.

> **Stacks 03EO, sheaf case, at a free ring universe, on sections.**  The correspondence is
> the canonical currying map: a morphism `b` out of the sheafified tensor product is sent to the
> map taking a section `x` of `F` over `U` and a section `y` of `G` over `T ⟶ U` to the value of
> `b` on the image of the pure tensor `x|_T ⊗ y`.

```lean
theorem sheafTensorHomEquiv_apply
    (b : ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, max u v w, max u v w} R).obj
      F).obj G ⟶ H) (U : C)
    (x : F.val.obj (Opposite.op U)) {T : C} (q : T ⟶ U)
    (y : G.val.obj (Opposite.op T)) :
    FreeUniverse.sectionOfRestr R.obj H.val U q
        (((((sheafTensorHomEquiv R F G H b).val.app (Opposite.op U)).hom x).app
          (Opposite.op (Over.mk q))).hom (FreeUniverse.restrSection R.obj G.val U q y)) =
      FreeUniverse.globalTensorHom R.obj F.val G.val H.val
        ((sheafifyForgetAdjunction R).homEquiv (F.val.tensorObj G.val) H b) T
        (F.val.restrictₛₗ q.op x ⊗ₜ y)
```

## Tag 03EP, a lemma

[Tag 03EP](https://stacks.math.columbia.edu/tag/03EP) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.PresheafOfModules.tensorLeft_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean#L150). The attribute's comment: “part (1)”.

> Tensoring presheaves of modules on the left by a fixed presheaf of modules preserves all
> colimits indexed in the module universe: at each object it is a left adjoint.

```lean
theorem tensorLeft_preservesColimits {O : Cᵒᵖ ⥤ CommRingCat.{w}}
    (F : _root_.PresheafOfModules.{z} (ringPresheaf O)) :
    PreservesColimitsOfSize.{a, z} (tensorLeft F)
```

**`AlgebraicGeometry.SheafOfModules.sheafTensorLeft_preservesColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/TensorColimits.lean#L265). The attribute's comment: “part (2)”. References: SGA 5 V (1.2.1), “inductive limits”.

> **Stacks Project, Tag 05NB.** Tensoring with a fixed sheaf of modules commutes with
> all small colimits, independently of the ring universe.

```lean
theorem sheafTensorLeft_preservesColimits (R : Sheaf J CommRingCat.{w})
    (F : _root_.SheafOfModules.{z} (Stacks.SheafOfModules.Tensor.ringSheaf R)) :
    PreservesColimitsOfSize.{a, z} (sheafTensorLeft J R F)
```

## Tag 0932, a lemma

[Tag 0932](https://stacks.math.columbia.edu/tag/0932) in the Stacks Project.

**`Stacks.PresheafOfModules.CoextendScalars.restrictScalars_coextendScalars_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/RestrictScalarsCoextension.lean, line 1060](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/RestrictScalarsCoextension.lean#L1060). The attribute's comment: “the presheaf case: Hom_O(G, F) = Hom_O'(G, SheafHom_O(O', F)) for C a category and O ⟶ O' a map of presheaves of rings”.

> The adjunction `φ*_res ⊣ φ_*^coext`: restriction of scalars along `φ` is left adjoint to the
> coextension-of-scalars functor `φ_*^coext = coextendScalars φ`, with Hom-bijection `homEquiv`
> (forward `α ↦ (g ↦ a' ↦ α(a' • g))`, inverse `β ↦ (g ↦ β(g)(1))`). This is the
> presheaf-of-modules analogue of `ModuleCat.restrictCoextendScalarsAdj`.

```lean
noncomputable def restrictScalars_coextendScalars_adjunction (φ : O ⟶ O') :
    PresheafOfModules.restrictScalars.{u} φ ⊣ coextendScalars φ
```

**`Stacks.SheafOfModules.CoextendScalars.sheafRestrictCoextendAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RestrictCoextendScalarsAdjunction.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RestrictCoextendScalarsAdjunction.lean#L51). The attribute's comment: “the sheaf case: Hom_O(G, F) = Hom_O'(G, SheafHom_O(O', F)) for C a site and O ⟶ O' a map of sheaves of rings”.

> **Stacks Tag 0932 / Lemma 18.27.8, sheaf case.** For a morphism `φ : O ⟶ O'` of sheaves of
> rings on a site, restriction of scalars along `φ` is left adjoint to coextension of scalars
> `F ↦ SheafHom_O(O', F)`, i.e. `Hom_O(G_O, F) = Hom_{O'}(G, SheafHom_O(O', F))` naturally in the
> sheaf of `O'`-modules `G` and the sheaf of `O`-modules `F`. This is
> `restrictScalars_coextendScalars_adjunction`.

```lean
noncomputable def sheafRestrictCoextendAdjunction (φ : O ⟶ O') :
    SheafOfModules.restrictScalars.{u} φ ⊣ sheafCoextendScalars φ
```

## Tag 0E8I, a lemma

[Tag 0E8I](https://stacks.math.columbia.edu/tag/0E8I) in the Stacks Project.

**`Stacks.Sites.ExtensionByZero.OfEssentiallySmall.restrictionTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroTensorEssentiallySmall.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroTensorEssentiallySmall.lean#L211). The attribute's comment: “for a site essentially u-small, objects in Type c, morphisms and modules in u”.

> **Stacks 0E8I over a site with large objects.** For a sheaf of modules `F` on `X`, the
> extension by zero of `G ⊗ F|_U` is the extension by zero of `G`, tensored with `F`, naturally
> in `G`.
>
> The attribute records the shape at which this holds: the objects of `C` form a type in an
> arbitrary universe `c`, but the morphisms, the structure sheaf and the modules all lie in one
> universe `u`, and `C` is required to be essentially `u`-small. The tag is carried in full by
> `Stacks.SheafOfModules.ExtensionByZero.extensionByZeroTensorIso`, where objects, morphisms,
> ring and modules lie in a single universe — the faithful reading of the tag's ringed site, which
> this statement specializes to at `c := u`; that registration stands and this one does not
> replace it.

```lean
noncomputable def restrictionTensorIso
    (F : SheafOfModules.{u} (ringSheaf X.O)) :
    extendByZero X U ⋙ (Stacks.SheafOfModules.Tensor.sheafTensor X.O).flip.obj F ≅
      sliceSheafTensorRight X U (F.over U) ⋙ extendByZero X U
```

**`Stacks.Sites.ExtensionByZero.FreeModuleUniverse.restrictionTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroTensorFreeModuleUniverse.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/ExtensionByZeroTensorFreeModuleUniverse.lean#L183). The attribute's comment: “objects in Type u, morphisms in v, ring sections in w, modules in a free a with UnivLE v a, and no smallness assumption on the site”.

> **Stacks 0E8I at a free module universe.** For a sheaf of modules `F` on `X`, the extension
> by zero of `G ⊗ F|_U` is the extension by zero of `G`, tensored with `F`, naturally in `G`.
>
> The attribute records the shape at which this holds: the objects of `C` in `Type u`, its
> morphisms in `v`, the structure sheaf in `w` and the modules in a free `a` with `UnivLE.{v, a}`,
> and no smallness assumption on `C`. The tag is carried in full by
> `Stacks.SheafOfModules.ExtensionByZero.extensionByZeroTensorIso`, where objects, morphisms,
> ring and modules lie in a single universe; that registration stands and this one does not
> replace it, nor does it replace
> `Stacks.Sites.ExtensionByZero.OfEssentiallySmall.restrictionTensorIso`.

```lean
noncomputable def restrictionTensorIso
    (F : SheafOfModules.{a} (ringSheaf X.O)) :
    extendByZero.{a} X U ⋙ (Stacks.SheafOfModules.Tensor.sheafTensor X.O).flip.obj F ≅
      sliceSheafTensorRight.{a} X U (F.over U) ⋙ extendByZero.{a} X U
```

**`Stacks.SheafOfModules.ExtensionByZero.extensionByZeroTensorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/ExtensionByZeroTensor.lean, line 321](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/ExtensionByZeroTensor.lean#L321).

> **Stacks 0E8I.** Extension by zero commutes with tensoring by a module on the original
> site, naturally in the module on the slice site.

```lean
noncomputable def extensionByZeroTensorIso (F : _root_.SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)) :
    letI := Stacks.Sites.ExtensionByZero.sheafRestrictionIsRightAdjoint X.J (Stacks.SheafOfModules.Tensor.ringSheaf X.O) U
    let E := _root_.SheafOfModules.pullback.{u}
      (F := Over.forget U) (𝟙 ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over U))
    E ⋙ ((sheafTensor.{u, u, u, u, u} X.O).obj F) ≅
      ((sheafTensor.{u, u, u, u, u} (X.O.over U)).obj (F.over U)) ⋙ E
```

**`Stacks.SheafOfModules.ExtensionByZero.extensionTensorBifunctorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/ExtensionByZeroTensor.lean, line 469](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/ExtensionByZeroTensor.lean#L469). The attribute's comment: “bifunctorial form”.

> **Stacks 0E8I, bifunctorial form.** Extension by zero commutes with tensoring by a module
> on the original site, naturally in the module on the slice site *and* in the module on the
> original site.

```lean
noncomputable def extensionTensorBifunctorIso :
    extensionTensorBifunctor X U ≅ tensorExtensionBifunctor X U
```

## Tag 0EYY, a remark

[Tag 0EYY](https://stacks.math.columbia.edu/tag/0EYY) in the Stacks Project.

**`Stacks.Sites.Localization.jShriekUnitIsoFreeAbelianSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean#L202). The attribute's comment: “j_! ℤ = Z_F^#, in the ambient category carrying the tensor product”.

> **Stacks Project, Tag 0EYY**, part (a), in the ambient category of sheaves of
> `ULift ℤ`-modules. The extension by zero of the tensor unit along the localization morphism
> `j : Sh(C)/F ⟶ Sh(C)` is the free abelian sheaf `Z_F^#` on `F`, read through the equivalence
> between sheaves of `ULift ℤ`-modules and sheaves of abelian groups.
>
> This transports the `AddCommGrpCat`-valued statement
> `localizationShriek_constantInteger_iso_freeAbSheaf` across the bridge, using that the bridge
> commutes with extension by zero and carries the tensor unit to the constant sheaf on
> `ULift ℤ`.

```lean
def jShriekUnitIsoFreeAbelianSheaf :
    let := Sheaf.monoidalCategory (localizationTopology J F)
      (ModuleCat.{u} (ULift.{u} ℤ))
    (abelianLocalizationShriek J F).obj (𝟙_ _) ≅
      (sheafIntegerModuleEquivalence J).inverse.obj
        ((Presheaf.freeAbelianSheaf J).obj ((sheafToPresheaf J (Type u)).obj F))
```

**`Stacks.Sites.Localization.jShriekPullbackIsoShriekUnitTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean, line 233](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean#L233). The attribute's comment: “j_!(j⁻¹ H) = j_! ℤ ⊗ H, with no hypothesis beyond the data of the source”.

> **Stacks Project, Tag 0EYY**, part (b), with no hypothesis beyond the data of the source.
> For the localization morphism `j : Sh(C)/F ⟶ Sh(C)` and an abelian sheaf `H` on `C`,
>
> `j_!(j⁻¹ H) ≅ j_! ℤ ⊗_ℤ H`.
>
> This is `jShriekPullbackIsoTensor`, which is proved for a site of arbitrary size and therefore
> states sheafification of `ModuleCat`-valued presheaves on `C` and on `C/F`, the monoidality of
> the two sheafification localizers and the left Kan extensions along `C/F ⥤ C` as hypotheses.
> On a site all five are available: the monoidality of the two localizers from
> `CategoryTheory.GrothendieckTopology.W.monoidal`, the left Kan extensions from Mathlib's
> pointwise construction `CategoryTheory.Functor.pointwiseLeftKanExtension`, and the two
> sheafifications through `preservesColimitsOfShape_cover_op_forget_moduleCat` above. So part (b)
> carries no hypothesis the source does not make.

```lean
def jShriekPullbackIsoShriekUnitTensor
    (H : Sheaf J (ModuleCat.{u} (ULift.{u} ℤ))) :
    let := Sheaf.monoidalCategory J (ModuleCat.{u} (ULift.{u} ℤ))
    let := Sheaf.monoidalCategory (localizationTopology J F)
      (ModuleCat.{u} (ULift.{u} ℤ))
    (abelianLocalizationShriek J F).obj
        ((abelianLocalizationInverseImage J F).obj H) ≅
      (abelianLocalizationShriek J F).obj (𝟙_ _) ⊗ H
```

**`Stacks.Sites.Localization.jShriekPullbackIsoFreeAbelianSheafTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean, line 254](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Localization/AbelianShriekIntegerBridge.lean#L254). The attribute's comment: “j_!(j⁻¹ H) = Z_F^# ⊗ H, the two parts joined”.

> **Stacks Project, Tag 0EYY**, the conclusion. For the localization morphism
> `j : Sh(C)/F ⟶ Sh(C)` and an abelian sheaf `H` on `C`,
>
> `j_!(j⁻¹ H) ≅ Z_F^# ⊗_ℤ H`,
>
> the free abelian sheaf on `F` tensored with `H`. This combines part (b),
> `jShriekPullbackIsoTensor`, with the identification of `j_! ℤ` with `Z_F^#` of part (a).

```lean
def jShriekPullbackIsoFreeAbelianSheafTensor
    (H : Sheaf J (ModuleCat.{u} (ULift.{u} ℤ))) :
    let := Sheaf.monoidalCategory J (ModuleCat.{u} (ULift.{u} ℤ))
    (abelianLocalizationShriek J F).obj
        ((abelianLocalizationInverseImage J F).obj H) ≅
      (sheafIntegerModuleEquivalence J).inverse.obj
        ((Presheaf.freeAbelianSheaf J).obj ((sheafToPresheaf J (Type u)).obj F)) ⊗ H
```

**`Stacks.Sites.Localization.localizationShriek_constantInteger_iso_freeAbSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/LocalizationShriekInteger.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/LocalizationShriekInteger.lean#L357). The attribute's comment: “j_shriek_int”.

> For the localization morphism `j : Sh(C)/F ⟶ Sh(C)`, presented by the site of elements
> `C/F`, the abelian sheaf `j_! ℤ` is the free abelian sheaf `Z_F^#` on `F`.

```lean
noncomputable def localizationShriek_constantInteger_iso_freeAbSheaf (F : Sheaf J (Type u)) :
    (Stacks.Sites.abelianShriek (localizationProjection J F)
          (localizationTopology J F) J).obj
        ((constantSheaf (localizationTopology J F) AddCommGrpCat.{u}).obj
          (AddCommGrpCat.of (ULift.{u} ℤ))) ≅
      (Presheaf.freeAbelianSheaf J).obj ((sheafToPresheaf J (Type u)).obj F)
```

Declarations registered for the tag:

- [`jShriekPullbackIsoTensor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=jShriekPullbackIsoTensor#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/LocalizationShriekInteger.lean, line 366](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/LocalizationShriekInteger.lean#L366) (StacksFrontier): “j_!(j⁻¹ H) = j_! ℤ ⊗ H, for a site of arbitrary size: sheafification, the monoidality of the two sheafification localizers and the left Kan extensions along C/F ⥤ C are instance hypotheses here, and every one of them holds at the hypotheses of the source -- see jShriekPullbackIsoShriekUnitTensor”.

## Tag 0GMZ, a lemma

[Tag 0GMZ](https://stacks.math.columbia.edu/tag/0GMZ) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.internalHomSecondFunctor_preservesFilteredColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomFilteredColimits.lean, line 545](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomFilteredColimits.lean#L545).

> On a ringed site, internal Hom out of a module of finite presentation commutes with filtered
> colimits: the canonical map `colim_λ Hom_O(F, G_λ) ⟶ Hom_O(F, colim_λ G_λ)` is an isomorphism
> for every filtered diagram `λ ↦ G_λ`.

```lean
theorem internalHomSecondFunctor_preservesFilteredColimits
    (F : SheafOfModules.{u} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O))
    [F.IsFinitePresentation]
    (K : Type u) [Category.{u} K] [IsFiltered K] :
    PreservesColimitsOfShape K (internalHomSecondFunctor.{u, u, u, u} X.J X.O F)
```

## Tag 0GN0, a lemma

[Tag 0GN0](https://stacks.math.columbia.edu/tag/0GN0) in the Stacks Project.

**`Stacks.SheafOfModules.InternalHom.coyoneda_preservesColimitsOfShape_of_isFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomFilteredColimitsSections.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InternalHomAndFlatness/InternalHomFilteredColimitsSections.lean#L232). References: SGA 4 VI (5.8), “special case”.

> **Stacks 0GN0.** On a ringed site satisfying the hypothesis of Stacks 0GMR part (4), Hom out
> of a module `F` of finite presentation commutes with filtered colimits:
>
> `colim_λ Hom_O(F, G_λ) = Hom_O(F, colim_λ G_λ)`.
>
> The site hypothesis is the one the source attaches to the statement; it is needed already for
> `F = O`, where the assertion is that global sections commute with the colimit. Stacks 0GMS
> records sufficient conditions for it, one of which is applied in
> `coyoneda_preservesColimitsOfShape_of_coveringSet` below.

```lean
theorem coyoneda_preservesColimitsOfShape_of_isFinitePresentation
    (F : _root_.SheafOfModules.{u} (Tensor.ringSheaf X.O)) [F.IsFinitePresentation]
    (K : Type u) [Category.{u} K] [IsFiltered K]
    (hX : ∃ S : Set (Sheaf X.J (Type u)),
      (∀ H : Sheaf X.J (Type u), Sheaf.IsLocallySurjective (terminal.from H) →
          ∃ L ∈ S, Nonempty (L ⟶ H) ∧ Sheaf.IsLocallySurjective (terminal.from L)) ∧
        ∀ L ∈ S, Sheaf.IsQuasiCompact (L ⨯ L)) :
    PreservesColimitsOfShape K (coyoneda.obj (Opposite.op F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.27, Tag 04TT](https://stacks.math.columbia.edu/tag/04TT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
