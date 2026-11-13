---
declaration: section
origin: cited
lean: AlgebraicGeometry.AffineDiffOp.globalDiffOpEquiv, Stacks.FibreProductAffineChart.Chart.diffOpEquiv, AlgebraicGeometry.globalDiffOp_ext_of_chart_sections, AlgebraicGeometry.existsUnique_globalDiffOp_externalTensorProduct, Stacks.FibreProductAffineChart.Chart.existsUnique_boxDiffOp, Stacks.FibreProductAffineChart.Chart.boxHom_boxSectionOfTensor, AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom_add_left, AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom_add_right
statement: formalized
proof: formalized
---

# 29.34 Finite order differential operators

Section 29.34 of the Stacks Project, [Tag 0G43](https://stacks.math.columbia.edu/tag/0G43). 3 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G44, a lemma

[Tag 0G44](https://stacks.math.columbia.edu/tag/0G44) in the Stacks Project.

**`AlgebraicGeometry.AffineDiffOp.globalDiffOpEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/AffineDifferentialOperators.lean, line 1080](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/DifferentialsAndValuative/AffineDifferentialOperators.lean#L1080).

> On an affine scheme, taking global sections gives a bijection from differential operators
> of order at most `k` between sheaves to differential operators of order at most `k` between the
> corresponding modules. The source sheaf is required to be quasi-coherent; the target sheaf is
> arbitrary.

```lean
noncomputable def globalDiffOpEquiv
    {R A : Type u} [CommRing R] [CommRing A] [Algebra R A]
    (F G : (Spec (.of A)).Modules) [F.IsQuasicoherent] (k : ℕ) :
    letI _modAF : Module A Γ(F, ⊤) :=
      Module.compHom _ (Scheme.ΓSpecIso (.of A)).inv.hom
    letI _modAG : Module A Γ(G, ⊤) :=
      Module.compHom _ (Scheme.ΓSpecIso (.of A)).inv.hom
    letI _modRF : Module R Γ(F, ⊤) := Module.compHom _ (algebraMap R A)
    letI _modRG : Module R Γ(G, ⊤) := Module.compHom _ (algebraMap R A)
    letI _towerF : IsScalarTower R A Γ(F, ⊤) := IsScalarTower.of_compHom R A _
    letI _towerG : IsScalarTower R A Γ(G, ⊤) := IsScalarTower.of_compHom R A _
    {e :
      {D : DiffOp.GlobalOp F G //
        DiffOp.IsGlobalDiffOpOfOrder
          (Scheme.Hom.relativeStructureSheafMap
            (Spec.map (CommRingCat.ofHom (algebraMap R A)))) k D} ≃
        {D : Γ(F, ⊤) →ₗ[R] Γ(G, ⊤) //
          D.IsDifferentialOperatorOfOrderLE A k} //
      ∀ D x, (e D).1 x = D.1 (.op ⊤) x}
```

## Tag 0G45, a lemma

[Tag 0G45](https://stacks.math.columbia.edu/tag/0G45) in the Stacks Project.

**`Stacks.FibreProductAffineChart.Chart.diffOpEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBaseChange.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBaseChange.lean#L205). The attribute's comment: “the affine-chart reduction step of the proof: over an affine chart of `X ×_S Y`, the differential operators of order at most `k` on `X ×_S Y / Y` are the differential operators of order at most `k` relative to `B ⟶ A ⊗_R B` on the chart's sections. Neither the construction of `D'` nor its characterisation on pure tensors is included”.

> **Differential operators on an affine chart of a fibre product.** The differential operators
> of order at most `k` on `X ×_S Y / Y` between two modules on `X ×_S Y`, defined over the opens
> contained in a chart, are the differential operators of order at most `k` relative to
> `Γ(Y, V) ⟶ Γ(X, U) ⊗_{Γ(S, W)} Γ(Y, V)` between the two modules of sections on the chart.

```lean
noncomputable def diffOpEquiv (M M' : (pullback a b).Modules)
    [(Scheme.Modules.restrict M ((c.specIso hl hr).inv ≫ c.ι)).IsQuasicoherent] (k : ℕ) :
    letI _modAF : Module (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right))
        Γ(Scheme.Modules.restrict M ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      Module.compHom _ (Scheme.ΓSpecIso
        (.of (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)))).inv.hom
    letI _modAG : Module (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right))
        Γ(Scheme.Modules.restrict M' ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      Module.compHom _ (Scheme.ΓSpecIso
        (.of (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)))).inv.hom
    letI _modRF : Module Γ(Y, c.right)
        Γ(Scheme.Modules.restrict M ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      Module.compHom _ (algebraMap Γ(Y, c.right)
        (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)))
    letI _modRG : Module Γ(Y, c.right)
        Γ(Scheme.Modules.restrict M' ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      Module.compHom _ (algebraMap Γ(Y, c.right)
        (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)))
    letI _towerF : IsScalarTower Γ(Y, c.right) (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right))
        Γ(Scheme.Modules.restrict M ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      IsScalarTower.of_compHom _ _ _
    letI _towerG : IsScalarTower Γ(Y, c.right) (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right))
        Γ(Scheme.Modules.restrict M' ((c.specIso hl hr).inv ≫ c.ι), ⊤) :=
      IsScalarTower.of_compHom _ _ _
    {D : DiffOp.RawOp M M' c.ι.opensRange //
        DiffOp.IsDiffOpOfOrder (pullback.snd a b).relativeStructureSheafMap k D} ≃
      {D : Γ(Scheme.Modules.restrict M ((c.specIso hl hr).inv ≫ c.ι), ⊤) →ₗ[Γ(Y, c.right)]
          Γ(Scheme.Modules.restrict M' ((c.specIso hl hr).inv ≫ c.ι), ⊤) //
        D.IsDifferentialOperatorOfOrderLE
          (Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)) k}
```

**`AlgebraicGeometry.globalDiffOp_ext_of_chart_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBaseChange.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBaseChange.lean#L327). The attribute's comment: “the local-global step of the proof: a differential operator of order at most `k` on `X ×_S Y / Y` out of a quasi-coherent module is determined by its action on the sections over the affine charts. This is not the uniqueness clause of the tag, which is uniqueness among the operators satisfying the characterisation on pure tensors”.

> **A differential operator on a fibre product is determined by its action on the affine
> charts.** Two differential operators of order at most `k` on `X ×_S Y / Y`, out of a
> quasi-coherent module, which agree on the sections over every affine chart of `X ×_S Y`, are
> equal.

```lean
theorem globalDiffOp_ext_of_chart_sections {X Y S : Scheme.{u}} (a : X ⟶ S) (b : Y ⟶ S) (k : ℕ)
    {M M' : (pullback a b).Modules} [M.IsQuasicoherent] (D E : DiffOp.GlobalOp M M')
    (hD : DiffOp.IsGlobalDiffOpOfOrder (pullback.snd a b).relativeStructureSheafMap k D)
    (hE : DiffOp.IsGlobalDiffOpOfOrder (pullback.snd a b).relativeStructureSheafMap k E)
    (hagree : ∀ (c : Chart a b) (s : Γ(M, c.ι.opensRange)),
      D (op c.ι.opensRange) s = E (op c.ι.opensRange) s) :
    D = E
```

**`AlgebraicGeometry.existsUnique_globalDiffOp_externalTensorProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxOperatorGluing.lean, line 290](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxOperatorGluing.lean#L290).

> **Base change of a differential operator.** Let `a : X ⟶ S` and `b : Y ⟶ S` be morphisms of
> schemes, let `F`, `F'` be quasi-coherent `𝒪_X`-modules, let `G` be a quasi-coherent `𝒪_Y`-module
> and let `D : F ⟶ F'` be a differential operator of order at most `k` on `X/S`. There is a unique
> differential operator of order at most `k` on `X ×_S Y / Y` from `pr₁^*F ⊗ pr₂^*G` to
> `pr₁^*F' ⊗ pr₂^*G` which carries, for all local sections `s` of `F` and `t` of `G`, the section
> attached to `s` and `t` to the section attached to `D s` and `t`.

```lean
theorem existsUnique_globalDiffOp_externalTensorProduct {X Y S : Scheme.{u}} (a : X ⟶ S)
    (b : Y ⟶ S) (F F' : X.Modules) (G : Y.Modules)
    [F.IsQuasicoherent] [F'.IsQuasicoherent] [G.IsQuasicoherent] (k : ℕ)
    (D : DiffOp.GlobalOp F F')
    (hD : DiffOp.IsGlobalDiffOpOfOrder a.relativeStructureSheafMap k D) :
    ∃! E : DiffOp.GlobalOp (externalTensorProduct a b F G) (externalTensorProduct a b F' G),
      DiffOp.IsGlobalDiffOpOfOrder (pullback.snd a b).relativeStructureSheafMap k E ∧
        ∀ (U' : X.Opens) (V' : Y.Opens) (s : Γ(F, U')) (t : Γ(G, V'))
          (W : (pullback a b).Opens) (hW₁ : W ≤ pullback.fst a b ⁻¹ᵁ U')
          (hW₂ : W ≤ pullback.snd a b ⁻¹ᵁ V'),
          E (op W) (externalTensorSection a b F G s t W hW₁ hW₂) =
            externalTensorSection a b F' G (D (op U') s) t W hW₁ hW₂
```

**`Stacks.FibreProductAffineChart.Chart.existsUnique_boxDiffOp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxProductOperator.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxProductOperator.lean#L492). The attribute's comment: “the affine-chart step of the construction of `D'`: over ONE affine chart of `X ×_S Y` this gives the existence of `D'`, its order bound, its characterisation on pure tensors and its uniqueness, all read through the identification of the sections of `F ⊠ G` on the chart with `Γ(Spec A, F) ⊗_R Γ(Spec B, G)`. The global operator on `X ×_S Y` is NOT constructed: the chart-wise operators are not glued, and the characterisation is not expressed on the sections of `F ⊠ G` attached to a pair of local sections of `F` and of `G`”.

> **The affine-chart base change of a differential operator (Tag 0G45 on a chart).** Let
> `D : F ⟶ F'` be a differential operator of order at most `k` on `X/S` between quasi-coherent
> modules and let `G` be a quasi-coherent `𝒪_Y`-module. Over the opens of an affine chart of
> `X ×_S Y` there is exactly one differential operator of order at most `k` on `X ×_S Y / Y` from
> `F ⊠ G` to `F' ⊠ G` which, read through the identification of the sections of a box product on the
> chart with `Γ(Spec Γ(X, U), F) ⊗_{Γ(S, W)} Γ(Spec Γ(Y, V), G)`, carries `s ⊗ t` to `D s ⊗ t`.

```lean
theorem existsUnique_boxDiffOp (F' : X.Modules) [F'.IsQuasicoherent] (k : ℕ)
    (D : DiffOp.GlobalOp F F')
    (hD : DiffOp.IsGlobalDiffOpOfOrder a.relativeStructureSheafMap k D) :
    ∃! E : {E : DiffOp.RawOp (externalTensorProduct a b F G) (externalTensorProduct a b F' G)
          c.ι.opensRange //
        DiffOp.IsDiffOpOfOrder (pullback.snd a b).relativeStructureSheafMap k E},
      ∀ (s : Γ((Scheme.Modules.pullback c.fromSpecLeft).obj F, ⊤))
        (t : Γ((Scheme.Modules.pullback c.fromSpecRight).obj G, ⊤)),
        (c.boxDiffOpTensorEquiv hl hr F G F' k E).1 (s ⊗ₜ[Γ(S, c.base)] t) =
          (c.leftDiffOpEquiv hl F F' k
              ⟨D.restrict c.fromSpecLeft.opensRange, hD c.fromSpecLeft.opensRange⟩).1 s
            ⊗ₜ[Γ(S, c.base)] t
```

## Tag 0G46, a remark

[Tag 0G46](https://stacks.math.columbia.edu/tag/0G46) in the Stacks Project.

**`Stacks.FibreProductAffineChart.Chart.boxHom_boxSectionOfTensor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductAffineDescription.lean, line 395](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductAffineDescription.lean#L395). The attribute's comment: “the MORPHISM half of the affine description of the remark: on an affine chart of `X ×_S Y`, and so in particular for `X = Spec A`, `Y = Spec B`, `S = Spec R` and the chart whose three opens are everything, the operator `D ⊠ E` read on the sections of `F ⊠ G` through the identification of those sections with `M ⊗_R N` is `D ⊗ E`. Carries a chosen order bound for each of the two operators (`hD`, `hE`), which exists for every morphism of the category. The OBJECT half `(M, N) ↦ M ⊗_R N` is `Chart.boxSectionsEquiv`”.

> **The affine description of the box product on morphisms.** Read on the sections of `F ⊠ G`
> over the image of a chart, through the identification of those sections with
> `Γ(Spec A, F) ⊗_R Γ(Spec B, G)`, the operator `D ⊠ E` is the tensor product `D ⊗ E` of the
> operator attached to `D` on `Γ(Spec A, F)` and the operator attached to `E` on
> `Γ(Spec B, G)`.

```lean
theorem boxHom_boxSectionOfTensor
    (z : Γ((Scheme.Modules.pullback c.fromSpecLeft).obj F.module, ⊤) ⊗[Γ(S, c.base)]
      Γ((Scheme.Modules.pullback c.fromSpecRight).obj G.module, ⊤)) :
    (AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom D E).1
        (op (((c.specIso hl hr).inv ≫ c.ι) ''ᵁ ⊤))
        (c.boxSectionOfTensor hl hr F.module G.module z) =
      c.boxSectionOfTensor hl hr F'.module G'.module
        (TensorProduct.map
          (c.leftDiffOpEquiv hl F.module F'.module k
            ⟨D.1.restrict c.fromSpecLeft.opensRange, hD c.fromSpecLeft.opensRange⟩).1
          (c.rightDiffOpEquiv hr G.module G'.module l
            ⟨E.1.restrict c.fromSpecRight.opensRange, hE c.fromSpecRight.opensRange⟩).1 z)
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom_add_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean#L200). The attribute's comment: “half of the bilinearity on morphisms asserted by the remark: the box product `D ⊠ E` is additive in the operator `D` on `X/S`”.

> **The box product is additive in its first argument.**

```lean
theorem boxHom_add_left {F F' : FiniteOrderDifferentialOperatorCategory a}
    {G G' : FiniteOrderDifferentialOperatorCategory b} (D D' : F ⟶ F') (E : G ⟶ G') :
    boxHom (D + D') E = boxHom D E + boxHom D' E
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom_add_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean#L210). The attribute's comment: “the other half of the bilinearity on morphisms asserted by the remark: the box product `D ⊠ E` is additive in the operator `E` on `Y/S`”.

> **The box product is additive in its second argument.**

```lean
theorem boxHom_add_right {F F' : FiniteOrderDifferentialOperatorCategory a}
    {G G' : FiniteOrderDifferentialOperatorCategory b} (D : F ⟶ F') (E E' : G ⟶ G') :
    boxHom D (E + E') = boxHom D E + boxHom D E'
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxProductFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductFunctor.lean#L225). The attribute's comment: “the box product bifunctor of the remark: `(F, G) ↦ F ⊠ G` on objects and `(D, E) ↦ D ⊠ E` on morphisms, with both functor laws. NOT the notation `F ⊠ G`, and NOT the affine description `(M, N) ↦ M ⊗_R N`, `(D, D') ↦ D ⊗ D'`, which is covered by `Chart.boxSectionsEquiv` and `Chart.boxHom_boxSectionOfTensor`”.

> **The box-product bifunctor of [Stacks, Tag 0G46].** The external tensor product on objects
> and the box product of two differential operators on morphisms form a functor from the product
> of the categories of finite-order differential operators on `X/S` and on `Y/S` to the category
> of finite-order differential operators on `X ×_S Y / S`.

```lean
noncomputable def boxProductFunctor (a : X ⟶ S) (b : Y ⟶ S) :
    FiniteOrderDifferentialOperatorCategory a × FiniteOrderDifferentialOperatorCategory b ⥤
      FiniteOrderDifferentialOperatorCategory (pullback.fst a b ≫ a)
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.boxHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductRightOperator.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BoxProductRightOperator.lean#L218). The attribute's comment: “the assignment on morphisms of the box product of the remark: for `D : F ⟶ F'` on `X/S` and `E : G ⟶ G'` on `Y/S` the operator `D ⊠ E = (1 ⊠ E) ∘ (D ⊠ 1)`, a morphism `F ⊠ G ⟶ F' ⊠ G'` of the category of finite-order differential operators on `X ×_S Y / S`. The FUNCTOR of the remark is not constructed HERE: `map_id`, `map_comp` and the bilinearity on morphisms are proved in `BoxProductFunctor`, and the affine description `(M, N) ↦ M ⊗_R N`, `(D, D') ↦ D ⊗ D'` in `BoxProductAffineDescription`”.

> **The box product `D ⊠ E` of two finite-order differential operators.** For morphisms
> `D : F ⟶ F'` of the category of finite-order differential operators on `X/S` and `E : G ⟶ G'` of
> the category on `Y/S`, the composite `(1 ⊠ E) ∘ (D ⊠ 1) : F ⊠ G ⟶ F' ⊠ G'` of the category of
> finite-order differential operators on `X ×_S Y / S`.

```lean
def boxHom {F F' : FiniteOrderDifferentialOperatorCategory a}
    {G G' : FiniteOrderDifferentialOperatorCategory b} (D : F ⟶ F') (E : G ⟶ G') :
    boxProductObj F G ⟶ boxProductObj F' G'
```

**`Stacks.FibreProductAffineChart.Chart.boxSectionsEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxProductOperator.lean, line 442](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ChartBoxProductOperator.lean#L442). The attribute's comment: “the OBJECT half of the affine description of the remark: on an affine chart of `X ×_S Y`, and so in particular for `X = Spec A`, `Y = Spec B`, `S = Spec R` and the chart whose three opens are everything, the module of sections of `F ⊠ G` is `M ⊗_R N`, linearly over the ring `A ⊗_R B` of the chart. NOT the morphism half `(D, D') ↦ D ⊗ D'`, which is `Chart.boxHom_boxSectionOfTensor`”.

> **The sections of a box product on a chart.** The module of sections of `F ⊠ G` on a chart is
> the tensor product over `Γ(S, W)` of the sections of `F` on `Spec Γ(X, U)` and of `G` on
> `Spec Γ(Y, V)`, linearly over `Γ(X, U) ⊗_{Γ(S, W)} Γ(Y, V)`, which acts on the tensor product by
> `(f ⊗ g) • (s ⊗ t) = (f • s) ⊗ (g • t)`.

```lean
noncomputable def boxSectionsEquiv :
    Γ((Scheme.Modules.pullback ((c.specIso hl hr).inv ≫ c.ι)).obj
        (externalTensorProduct a b F G), ⊤)
      ≃ₗ[Γ(X, c.left) ⊗[Γ(S, c.base)] Γ(Y, c.right)]
      (Γ((Scheme.Modules.pullback c.fromSpecLeft).obj F, ⊤) ⊗[Γ(S, c.base)]
        Γ((Scheme.Modules.pullback c.fromSpecRight).obj G, ⊤))
```

**`AlgebraicGeometry.externalTensorProduct`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ExternalTensorProduct.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/ExternalTensorProduct.lean#L43). The attribute's comment: “external\_tensor\_product\_of\_modules”.

> The external tensor product of an `O_X`-module and an `O_Y`-module on the fibre
> product of two schemes `X` and `Y` over `S`.

```lean
noncomputable abbrev externalTensorProduct {X Y S : Scheme.{u}} (f : X ⟶ S) (g : Y ⟶ S)
    (F : X.Modules) (G : Y.Modules) : (pullback f g).Modules
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean#L69). The attribute's comment: “category\_of\_finite\_order\_differential\_operators”.

> A quasi-coherent module, regarded as an object of the category of finite-order
> differential operators on `X/S`.

```lean
structure FiniteOrderDifferentialOperatorCategory (a : X ⟶ S)
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.Hom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean#L131). The attribute's comment: “category\_of\_finite\_order\_differential\_operators”.

> Morphisms in the category of finite-order differential operators.

```lean
noncomputable abbrev Hom (F G : FiniteOrderDifferentialOperatorCategory a)
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.instCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean#L159). The attribute's comment: “category\_of\_finite\_order\_differential\_operators”.

> Composition of finite-order differential operators makes quasi-coherent modules
> into a category.

```lean
noncomputable instance instCategory :
    Category (FiniteOrderDifferentialOperatorCategory a)
```

**`AlgebraicGeometry.FiniteOrderDifferentialOperatorCategory.instPreadditive`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean, line 186](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteOrderCategory.lean#L186). The attribute's comment: “category\_of\_finite\_order\_differential\_operators”.

> The pointwise addition of finite-order differential operators is compatible with
> composition.

```lean
noncomputable instance instPreadditive :
    Preadditive (FiniteOrderDifferentialOperatorCategory a)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.34, Tag 0G43](https://stacks.math.columbia.edu/tag/0G43)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
