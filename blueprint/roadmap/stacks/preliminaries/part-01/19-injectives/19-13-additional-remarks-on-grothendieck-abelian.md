---
declaration: section
origin: cited
lean: Stacks.Injectives.isRepresentable_iff_preservesLimits, Stacks.Injectives.hasProducts_of_isGrothendieckAbelian, Stacks.Injectives.kInjectiveResolutionHomMap_bijective, Stacks.Injectives.hasDerivedCategory_of_isGrothendieckAbelian, instIsGrothendieckAbelianModuleCat, SheafOfModules.instIsGrothendieckAbelian, Stacks.Injectives.isLimit_productFanInDerivedCategory, Stacks.Injectives.derivedCategoryQ_preservesCoproducts
statement: formalized
proof: formalized
---

# 19.13 Additional remarks on Grothendieck abelian categories

Section 19.13 of the Stacks Project, [Tag 07D6](https://stacks.math.columbia.edu/tag/07D6). 12 tags here are carried by 49 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07D7, a lemma

[Tag 07D7](https://stacks.math.columbia.edu/tag/07D7) in the Stacks Project.

**`Stacks.Injectives.isRepresentable_iff_preservesLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Representability.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Representability.lean#L78). References: SGA 4 I (8.12.7), “Grothendieck abelian”.

> Let `A` be a Grothendieck abelian category and `F : Aᵒᵖ ⥤ Set` a functor. Then `F` is
> representable if and only if it commutes with colimits, that is, `F (colim_i N_i) = lim_i F (N_i)`
> for every diagram `I ⥤ A`.

```lean
theorem isRepresentable_iff_preservesLimits [Abelian C] [IsGrothendieckAbelian.{w} C]
    (F : Cᵒᵖ ⥤ Type w) : F.IsRepresentable ↔ PreservesLimitsOfSize.{w, w} F
```

## Tag 07D8, a lemma

[Tag 07D8](https://stacks.math.columbia.edu/tag/07D8) in the Stacks Project.

**`Stacks.Injectives.hasProducts_of_isGrothendieckAbelian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Abelian/GrothendieckAxioms/StacksConditions.lean#L175). References: SGA 4 V (0.1.1).

> A Grothendieck abelian category has AB3\*, that is, it has products. Mathlib's name for AB3\*
> is `CategoryTheory.Limits.HasProducts`, so there is nothing left to define here.
>
> The Stacks project deduces this from its criterion for representability of a functor on a
> Grothendieck abelian category: for a family `M_i` of objects the functor `F = ∏ h_{M_i}` commutes
> with colimits, so it is representable, and the representing object is the product of the family.
> Here we instead invoke `CategoryTheory.IsGrothendieckAbelian.hasLimits`, which gives all limits of
> size `w` at once.

```lean
theorem hasProducts_of_isGrothendieckAbelian [CategoryTheory.IsGrothendieckAbelian.{w} C] :
    HasProducts.{w} C
```

## Tag 079Q, a remark

[Tag 079Q](https://stacks.math.columbia.edu/tag/079Q) in the Stacks Project.

**`Stacks.Injectives.kInjectiveResolutionHomMap_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean#L96). The attribute's comment: “morphisms via a K-injective resolution”.

> Derived morphisms into a complex `L` are computed by homotopy classes of maps into the
> chosen K-injective resolution of `L`.

```lean
theorem kInjectiveResolutionHomMap_bijective (K L : CochainComplex C ℤ) :
    Function.Bijective (kInjectiveResolutionHomMap C K L)
```

**`Stacks.Injectives.hasDerivedCategory_of_isGrothendieckAbelian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean#L119). The attribute's comment: “existence of the derived category”.

> A Grothendieck abelian category which is locally small in the universe `w` admits a
> derived category whose morphism types lie in `w`.

```lean
noncomputable def hasDerivedCategory_of_isGrothendieckAbelian
    [inst_groth : IsGrothendieckAbelian.{w} C] :
    HasDerivedCategory.{w} C
```

Declarations registered for the tag:

- [`instIsGrothendieckAbelianModuleCat`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=instIsGrothendieckAbelianModuleCat#doc) registered with `add_to_stacks` in [StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean#L153) (StacksFrontier): “modules over a ring”.
- [`SheafOfModules.instIsGrothendieckAbelian`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.instIsGrothendieckAbelian#doc) registered with `add_to_stacks` in [StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/Existence.lean#L154) (StacksFrontier): “sheaves of modules on a ringed site”. References: SGA 3 I (3.2.1), “special case”; SGA 4 II (6.7), “special case”; SGA 6 I (1.3), “partial”.

## Tag 07D9, a lemma

[Tag 07D9](https://stacks.math.columbia.edu/tag/07D9) in the Stacks Project.

**`Stacks.Injectives.isLimit_productFanInDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/KInjectiveProducts.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/KInjectiveProducts.lean#L178). The attribute's comment: “termwise products of K-injective complexes”.

> The termwise product of K-injective representatives represents their product in the
> unbounded derived category.

```lean
theorem isLimit_productFanInDerivedCategory {I : Type w}
    (K : I → CochainComplex A ℤ) (hK : ∀ i, (K i).IsKInjective) :
    Nonempty (IsLimit (productFanInDerivedCategory K))
```

**`Stacks.Injectives.derivedCategoryQ_preservesCoproducts`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean#L109). The attribute's comment: “direct\_sums\_termwise”.

> The localization functor from complexes to the unbounded derived category preserves direct
> sums; thus the image of the termwise direct sum of any family of complexes is its direct sum in
> the derived category.

```lean
instance derivedCategoryQ_preservesCoproducts [IsGrothendieckAbelian.{w} A] (I : Type w) :
    PreservesColimitsOfShape (Discrete I) (DerivedCategory.Q (C := A))
```

**`Stacks.Injectives.hasCoproducts_derivedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean#L137). The attribute's comment: “direct\_sums\_exist”.

> The unbounded derived category of a Grothendieck abelian category has direct sums.

```lean
instance hasCoproducts_derivedCategory (A : Type u) [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{w} A] [HasDerivedCategory.{z} A] :
    HasCoproducts.{w} (DerivedCategory A)
```

**`Stacks.Injectives.hasProducts_derivedCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/ProductsAndCoproducts.lean#L190). The attribute's comment: “products\_exist”.

> The unbounded derived category of a Grothendieck abelian category has arbitrary
> products.

```lean
instance hasProducts_derivedCategory (𝒜 : Type u) [Category.{v} 𝒜] [Abelian 𝒜]
    [IsGrothendieckAbelian.{w} 𝒜] [HasDerivedCategory.{w'} 𝒜] :
    HasProducts.{w} (DerivedCategory 𝒜)
```

## Tag 08U1, a lemma

[Tag 08U1](https://stacks.math.columbia.edu/tag/08U1) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isDerivedLimit_map_derivedGlobalSectionsOverUnbounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/UnboundedGlobalSections.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalGeometry/DerivedCompletionRinged/UnboundedGlobalSections.lean#L246). The attribute's comment: “for A-linear derived global sections on a ringed site”.

> **`RΓ(𝒞, -)` over a base ring commutes with `R lim`**: `A`-linear derived global sections
> carry a derived inverse limit in `D(𝒪)` to a derived inverse limit in `D(A)`.
>
> This is [Stacks, Tag 08U1] for `derivedGlobalSectionsOverUnbounded`, through
> `Stacks.Injectives.isDerivedLimit_map_rightDerivedFunctor`: the functor is the right derived
> functor of `moduleGlobalSectionsOver` by
> `derivedGlobalSectionsOverUnbounded_isRightDerivedFunctor`, that functor preserves countable
> products, `Mod(𝒪)` is Grothendieck abelian and the countable products of `ModuleCat A` are
> exact. This is the site-and-base-ring form of [Stacks, Tag 0D6K], whose `Γ(𝒞, -)`-valued form
> is `Stacks.Cohomology.DerivedGlobalSections.isDerivedLimit_map_derivedGlobalSections`, and the
> ringed-site counterpart of [Stacks, Tag 0D60] for a ringed space,
> `Stacks.Cohomology.DerivedSectionsOverBase.isDerivedLimit_map_derivedSectionsOver`.

```lean
theorem isDerivedLimit_map_derivedGlobalSectionsOverUnbounded
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{u} (ringSheaf X.O)))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{u} (ringSheaf X.O)))
    (hL : Pretriangulated.IsDerivedLimit K L) :
    ∃ h : HasProduct
        (fun n : ℕ ↦ (derivedGlobalSectionsOverUnbounded X A ρ).obj (K.obj ⟨n⟩)),
      @Pretriangulated.IsDerivedLimit (DerivedCategory (ModuleCat.{u} A)) _ _ _ _ _ _
        (K ⋙ derivedGlobalSectionsOverUnbounded X A ρ) h
        ((derivedGlobalSectionsOverUnbounded X A ρ).obj L)
```

**`Stacks.Injectives.isDerivedLimit_map_rightDerivedFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/DerivedCategory/DerivedLimit.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/DerivedCategory/DerivedLimit.lean#L299).

> **Stacks 08U1.** The right derived functor of an additive functor from a Grothendieck
> abelian category to an abelian category with exact countable products carries every
> derived-limit triangle to a derived-limit triangle, if the functor preserves countable
> products. Its structural map is the image of the supplied `p`, followed by the canonical
> product comparison; hence its projections are `RF.map (p ≫ Pi.π _ n)`.

```lean
theorem isDerivedLimit_map_rightDerivedFunctor (X : ℕᵒᵖ ⥤ DerivedCategory A)
    [HasProduct fun n : ℕ ↦ X.obj ⟨n⟩] (K : DerivedCategory A)
    (p : K ⟶ ∏ᶜ fun n : ℕ ↦ X.obj ⟨n⟩)
    (hK : ∃ δ : (∏ᶜ fun n : ℕ ↦ X.obj ⟨n⟩) ⟶ K⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦ Pi.π (fun n : ℕ ↦ X.obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦ X.obj ⟨n⟩) (n + 1) ≫
          X.map (homOfLE (Nat.le_succ n)).op) δ ∈ distTriang (DerivedCategory A)) :
    ∃ h : HasProduct (fun n : ℕ ↦ RF.obj (X.obj ⟨n⟩)),
      letI := h
      ∃ δ : (∏ᶜ fun n : ℕ ↦ RF.obj (X.obj ⟨n⟩)) ⟶ (RF.obj K)⟦(1 : ℤ)⟧,
        Triangle.mk (RF.map p ≫ piComparison RF (fun n : ℕ ↦ X.obj ⟨n⟩))
          (Pi.lift fun n : ℕ ↦ Pi.π (fun n : ℕ ↦ RF.obj (X.obj ⟨n⟩)) n -
            Pi.π (fun n : ℕ ↦ RF.obj (X.obj ⟨n⟩)) (n + 1) ≫
              RF.map (X.map (homOfLE (Nat.le_succ n)).op)) δ ∈
          distTriang (DerivedCategory B)
```

## Tag 0BKI, a lemma

[Tag 0BKI](https://stacks.math.columbia.edu/tag/0BKI) in the Stacks Project.

**`Stacks.Injectives.exists_filtered_quasiIso_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/FilteredComplex/KInjectiveResolution.lean, line 951](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/FilteredComplex/KInjectiveResolution.lean#L951).

> **Stacks 0BKI.** A filtered complex in a Grothendieck abelian category has a
> filtered resolution which is termwise injective and K-injective before and after
> taking any filtration step or filtration quotient, and the comparison maps on all
> of these complexes are quasi-isomorphisms.

```lean
theorem exists_filtered_quasiIso_isKInjective [IsGrothendieckAbelian.{w'} A]
    (K : CochainComplex.Filtered A) :
    ∃ (J : CochainComplex.Filtered A) (j : K ⟶ J),
      (∀ n : ℤ, Injective (J.X.X n)) ∧
      (∀ p n : ℤ, Injective ((J.filtration.obj (op p)).X n)) ∧
      (∀ p n : ℤ, Injective ((cokernel (J.filtration.ι.app (op p))).X n)) ∧
      (∀ (p p' : ℤ) (h : p ≤ p') n,
        Injective ((cokernel (J.filtration.diagram.map (opHomOfLE h))).X n)) ∧
      J.X.IsKInjective ∧
      (∀ p : ℤ, (J.filtration.obj (op p)).IsKInjective) ∧
      (∀ p : ℤ, (cokernel (J.filtration.ι.app (op p))).IsKInjective) ∧
      (∀ (p p' : ℤ) (h : p ≤ p'),
        (cokernel (J.filtration.diagram.map (opHomOfLE h))).IsKInjective) ∧
      QuasiIso j.hom ∧
      (∀ p : ℤ, QuasiIso (j.natTrans.app (op p))) ∧
      (∀ p : ℤ, QuasiIso (filtrationQuotientMap j p)) ∧
      ∀ (p p' : ℤ) (h : p ≤ p'), QuasiIso (filtrationSubquotientMap j h)
```

## Tag 0G1X, a remark

[Tag 0G1X](https://stacks.math.columbia.edu/tag/0G1X) in the Stacks Project.

**`Stacks.Injectives.extSpectralSequenceInto_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean, line 407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean#L407). The attribute's comment: “ext\_spectral\_sequence\_convergence”.

> **Stacks 0G1X, boundedness.** If in every degree `Ext^n(M, F^pK^•)` vanishes for `p ≫ 0` and
> maps bijectively onto `Ext^n(M, K^•)` for `p ≪ 0`, then the Ext spectral sequence into `K^•` is
> bounded: in each total degree only finitely many terms of its first page are nonzero.

```lean
theorem extSpectralSequenceInto_isBounded
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      Subsingleton (DerivedCategory.Ext M (DerivedCategory.Q.obj (K.filtration.obj (op p))) n))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
      Function.Bijective
        (extPostcomp M n (DerivedCategory.Q.map (K.filtration.ι.app (op p))))) :
    IsBounded (extSpectralSequenceInto.{w', w} M K).1
```

**`Stacks.Injectives.extSpectralSequenceInto_hasPageInfinityAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean#L421). The attribute's comment: “ext\_spectral\_sequence\_convergence”.

> **Stacks 0G1X, the infinity page exists.** Under the same hypotheses the Ext spectral
> sequence into `K^•` stabilises at every bidegree.

```lean
theorem extSpectralSequenceInto_hasPageInfinityAt
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      Subsingleton (DerivedCategory.Ext M (DerivedCategory.Q.obj (K.filtration.obj (op p))) n))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
      Function.Bijective
        (extPostcomp M n (DerivedCategory.Q.map (K.filtration.ι.app (op p)))))
    (pq : ℤ × ℤ) :
    (extSpectralSequenceInto.{w', w} M K).1.HasPageInfinityAt pq
```

**`Stacks.Injectives.extSpectralSequenceInto_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean, line 490](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoConvergence.lean#L490). The attribute's comment: “ext\_spectral\_sequence\_convergence”.

> **Stacks 0G1X, convergence.** If in every degree `Ext^n(M, F^pK^•)` vanishes for `p ≫ 0` and
> maps bijectively onto `Ext^n(M, K^•)` for `p ≪ 0`, then the Ext spectral sequence into `K^•`
> converges to `Ext^{p + q}(M, K^•)`: the decreasing filtration
> `Stacks.Injectives.extIntoFiltration` of `Ext^n(M, K^•)` is finite, being `⊤` for `p ≪ 0` and `⊥`
> for `p ≫ 0`, the spectral sequence has an infinity page everywhere, and
> `E_∞^{p, q} ≅ F^p/F^{p + 1}` in total degree `n = p + q`.

```lean
theorem extSpectralSequenceInto_convergesToExt
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
      Subsingleton (DerivedCategory.Ext M (DerivedCategory.Q.obj (K.filtration.obj (op p))) n))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
      Function.Bijective
        (extPostcomp M n (DerivedCategory.Q.map (K.filtration.ι.app (op p))))) :
    let E := (extSpectralSequenceInto.{w', w} M K).1
    ∃ hF : ∀ n : ℤ, Antitone (extIntoFiltration M K n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ extIntoFiltration M K n a = ⊤ ∧
        extIntoFiltration M K n b = ⊥) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
        ((E.pageInfinity (p, q) : Type v) ≃+
          ((cokernel (Subobject.ofLE (extIntoFiltration M K (p + q) (p + 1))
              (extIntoFiltration M K (p + q) p)
              (hF (p + q) (by omega))) : AddCommGrpCat.{w}) : Type w))
```

**`Stacks.Injectives.extSpectralSequenceInto`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoFilteredComplex.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoFilteredComplex.lean#L107). The attribute's comment: “ext\_spectral\_sequence”. References: EGA 0 (13.7.3), “Ext functor case”.

> **Stacks 0G1X.** For a filtered complex `K^•` of a Grothendieck abelian category and an object
> `M` of `D(A)`, the cohomological spectral sequence `(E_r, d_r)_{r ≥ 1}` of the filtered Hom
> complex, bundled with the identifications `E_1^{p,q} = Ext^{p+q}(M, gr^pK)`.  Its differential on
> page `r` has bidegree `(r, -r + 1)` by the definition of `CohomologicalSpectralSequence`.

```lean
def extSpectralSequenceInto (M : DerivedCategory A) (K : CochainComplex.Filtered A) :
    Σ E : CohomologicalSpectralSequence AddCommGrpCat.{v} 1,
      ∀ p q : ℤ, ((E.page 1).X (p, q) : Type v) ≃+
        DerivedCategory.Ext M
          (DerivedCategory.Q.obj ((FilteredObject.gr p).obj K)) (p + q)
```

## Tag 0G1Y, a remark

[Tag 0G1Y](https://stacks.math.columbia.edu/tag/0G1Y) in the Stacks Project.

**`Stacks.Injectives.nonempty_canonicalExtSpectralSequenceInto_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoIndependence.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceIntoIndependence.lean#L365). The attribute's comment: “representative\_independence”.

> **Stacks 0G1Y, representative independence.**  Let `A` be a Grothendieck abelian category and
> let `M` and `K` be objects of `D(A)`.  The Ext spectral sequence of Tag 0G1X attached to the
> canonical truncation filtration `F^pK^• = τ_{≤ -p}K^•` of a complex `K^•` representing `K` does
> not depend on the choice of `K^•`: for any two complexes `K₁^•` and `K₂^•` representing `K` the
> two spectral sequences are isomorphic, so they have the same pages, differentials and
> page-turning isomorphisms from `E₁` onward.
>
> The two spectral sequences compared are the ones named
> `Stacks.Injectives.canonicalExtSpectralSequenceInto M K₁` and
> `Stacks.Injectives.canonicalExtSpectralSequenceInto M K₂`, that name being by definition the Ext
> spectral sequence of Tag 0G1X applied to the canonical truncation filtration; it is written out
> here so that this file does not depend on the module which introduces it.

```lean
theorem nonempty_canonicalExtSpectralSequenceInto_iso (M : DerivedCategory A)
    (K : DerivedCategory A) (K₁ K₂ : CochainComplex A ℤ)
    (e₁ : DerivedCategory.Q.obj K₁ ≅ K) (e₂ : DerivedCategory.Q.obj K₂ ≅ K) :
    Nonempty ((extSpectralSequenceInto.{w', w} M
        (CochainComplex.canonicalTruncationFiltration K₁)).1 ≅
      (extSpectralSequenceInto.{w', w} M
        (CochainComplex.canonicalTruncationFiltration K₂)).1)
```

**`Stacks.Injectives.canonicalExtSpectralSequenceInto`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L116). The attribute's comment: “canonical\_e1”.

> **Stacks 0G1Y.** The Ext spectral sequence into the canonical truncation filtration
> `F^pK^• = τ_{≤ -p}K^•` of a cochain complex, a cohomological spectral sequence
> `(E_r, d_r)_{r ≥ 1}`.

```lean
def canonicalExtSpectralSequenceInto (M : DerivedCategory A) (K' : CochainComplex A ℤ) :
    CohomologicalSpectralSequence AddCommGrpCat.{v} 1
```

**`Stacks.Injectives.canonicalExtSpectralSequenceIntoE₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L141). The attribute's comment: “canonical\_e1”. References: EGA 0 (11.4.3), “''E₂, T = Hom(M,-)”.

> **Stacks 0G1Y.** For a representative `K^•` of `K`, the first page of the canonical Ext
> spectral sequence into `K` is `E_1^{p, q} = Ext^{2p + q}(M, H^{-p}(K))`. The degrees `n = -p`
> and `m = 2p + q` are arguments constrained by equations.

```lean
def canonicalExtSpectralSequenceIntoE₁ (M K : DerivedCategory A) (K' : CochainComplex A ℤ)
    (e : DerivedCategory.Q.obj K' ≅ K) (p q n m : ℤ) (hn : n = -p) (hm : m = 2 * p + q) :
    ((canonicalExtSpectralSequenceInto.{w', w} M K').page 1).X (p, q) ≃+
      DerivedCategory.Ext M ((DerivedCategory.singleFunctor A 0).obj
        ((DerivedCategory.homologyFunctor A n).obj K)) m
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequenceInto`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 158](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L158). The attribute's comment: “renumbered\_e2”.

> **Stacks 0G1Y.** The canonical Ext spectral sequence into `K`, renumbered by
> `(i, j) ↦ (-j, i + 2j)` so that its first page becomes the second: a cohomological spectral
> sequence `(E'_r, d'_r)_{r ≥ 2}` whose differential on page `r` has bidegree `(r, -r + 1)`.

```lean
def renumberedCanonicalExtSpectralSequenceInto (M : DerivedCategory A)
    (K' : CochainComplex A ℤ) :
    CohomologicalSpectralSequence AddCommGrpCat.{v} 2
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequenceIntoE₂`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L166). The attribute's comment: “renumbered\_e2”.

> **Stacks 0G1Y.** For a representative `K^•` of `K`, the second page of the renumbered
> canonical Ext spectral sequence into `K` is `(E'_2)^{i, j} = Ext^i(M, H^j(K))`.

```lean
def renumberedCanonicalExtSpectralSequenceIntoE₂ (M K : DerivedCategory A)
    (K' : CochainComplex A ℤ) (e : DerivedCategory.Q.obj K' ≅ K) (i j : ℤ) :
    ((renumberedCanonicalExtSpectralSequenceInto.{w', w} M K').page 2).X (i, j) ≃+
      DerivedCategory.Ext M ((DerivedCategory.singleFunctor A 0).obj
        ((DerivedCategory.homologyFunctor A j).obj K)) i
```

**`Stacks.Injectives.stupidExtSpectralSequenceInto`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L180). The attribute's comment: “stupid\_e1”.

> **Stacks 0G1Y.** The Ext spectral sequence into the brutal truncation filtration
> `F^pK^• = σ_{≥ p}K^•` of a cochain complex, a cohomological spectral sequence
> `(E_r, d_r)_{r ≥ 1}`.

```lean
def stupidExtSpectralSequenceInto (M : DerivedCategory A) (K' : CochainComplex A ℤ) :
    CohomologicalSpectralSequence AddCommGrpCat.{v} 1
```

**`Stacks.Injectives.stupidExtSpectralSequenceIntoE₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L195). The attribute's comment: “stupid\_e1”.

> **Stacks 0G1Y.** The first page of the Ext spectral sequence of the brutal truncation
> filtration of `K^•` is `E_1^{p, q} = Ext^q(M, K^p)`.

```lean
def stupidExtSpectralSequenceIntoE₁ (M : DerivedCategory A) (K' : CochainComplex A ℤ)
    (p q : ℤ) :
    ((stupidExtSpectralSequenceInto.{w', w} M K').page 1).X (p, q) ≃+
      DerivedCategory.Ext M ((DerivedCategory.singleFunctor A 0).obj (K'.X p)) q
```

**`Stacks.Injectives.stupidExtSpectralSequenceInto_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L272). The attribute's comment: “stupid\_convergence”.

> **Stacks 0G1Y.** If `M` is bounded above in the derived category and `K^•` is bounded below,
> the Ext spectral sequence of the brutal truncation filtration of `K^•` is bounded.

```lean
theorem stupidExtSpectralSequenceInto_isBounded (M : DerivedCategory A)
    (K' : CochainComplex A ℤ) (hM : DerivedCategory.TStructure.t.minus M)
    (hK : CochainComplex.plus A K') :
    IsBounded (stupidExtSpectralSequenceInto.{w', w} M K')
```

**`Stacks.Injectives.stupidExtSpectralSequenceInto_hasPageInfinityAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L282). The attribute's comment: “stupid\_convergence”.

> **Stacks 0G1Y.** Under the same hypotheses the brutal-truncation Ext spectral sequence has an
> infinity page at every bidegree.

```lean
theorem stupidExtSpectralSequenceInto_hasPageInfinityAt (M : DerivedCategory A)
    (K' : CochainComplex A ℤ) (hM : DerivedCategory.TStructure.t.minus M)
    (hK : CochainComplex.plus A K') (pq : ℤ × ℤ) :
    (stupidExtSpectralSequenceInto.{w', w} M K').HasPageInfinityAt pq
```

**`Stacks.Injectives.stupidExtSpectralSequenceInto_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L296). The attribute's comment: “stupid\_convergence”.

> **Stacks 0G1Y, convergence of the brutal-truncation spectral sequence.** Under the same
> hypotheses it converges to `Ext^{p + q}(M, K^•)`: the decreasing filtration
> `Stacks.Injectives.extIntoFiltration` of each `Ext^n(M, K^•)` is finite and the infinity page at
> `(p, q)` is its `p`-th graded piece in total degree `p + q`.

```lean
theorem stupidExtSpectralSequenceInto_convergesToExt (M : DerivedCategory A)
    (K' : CochainComplex A ℤ) (hM : DerivedCategory.TStructure.t.minus M)
    (hK : CochainComplex.plus A K') :
    let E := stupidExtSpectralSequenceInto.{w', w} M K'
    let F := extIntoFiltration M (CochainComplex.stupidTruncationFiltration K')
    ∃ hF : ∀ n : ℤ, Antitone (F n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
        ((E.pageInfinity (p, q) : Type v) ≃+
          ((Limits.cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
              (hF (p + q) (by omega))) : AddCommGrpCat.{w}) : Type w))
```

**`Stacks.Injectives.canonicalExtSpectralSequenceInto_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 442](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L442). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G1Y, boundedness of the canonical spectral sequence.** For `M ∈ D^-(A)` and
> `K ∈ D^+(A)` the Ext spectral sequence of the canonical truncation filtration of a complex
> representing `K` is bounded: in total degree `d` its first page
> `E_1^{p, d - p} = Ext^{p + d}(M, H^{-p}(K))` vanishes unless `-a - d ≤ p ≤ -b`, where `M` lives in
> degrees `≤ a` and `K` in degrees `≥ b`.

```lean
theorem canonicalExtSpectralSequenceInto_isBounded (M K : DerivedCategory A)
    (K' : CochainComplex A ℤ) (e : DerivedCategory.Q.obj K' ≅ K)
    (hM : DerivedCategory.TStructure.t.minus M)
    (hK : DerivedCategory.TStructure.t.plus K) :
    IsBounded (canonicalExtSpectralSequenceInto.{w', w} M K')
```

**`Stacks.Injectives.canonicalExtSpectralSequenceInto_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 482](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L482). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G1Y, convergence of the canonical spectral sequence.** For `M ∈ D^-(A)` and
> `K ∈ D^+(A)` the Ext spectral sequence of the canonical truncation filtration converges to
> `Ext^{p + q}(M, K)`: the decreasing filtration `Stacks.Injectives.extIntoFiltration` of each
> `Ext^n(M, K)` is finite and the infinity page at `(p, q)` is its `p`-th graded piece in total
> degree `p + q`.

```lean
theorem canonicalExtSpectralSequenceInto_convergesToExt (M K : DerivedCategory A)
    (K' : CochainComplex A ℤ) (e : DerivedCategory.Q.obj K' ≅ K)
    (hM : DerivedCategory.TStructure.t.minus M)
    (hK : DerivedCategory.TStructure.t.plus K) :
    let E := canonicalExtSpectralSequenceInto.{w', w} M K'
    let F := extIntoFiltration M (CochainComplex.canonicalTruncationFiltration K')
    ∃ hF : ∀ n : ℤ, Antitone (F n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
        ((E.pageInfinity (p, q) : Type v) ≃+
          ((Limits.cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
              (hF (p + q) (by omega))) : AddCommGrpCat.{w}) : Type w))
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequenceInto_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L503). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G1Y, boundedness after renumbering.** For `M ∈ D^-(A)` and `K ∈ D^+(A)` the
> renumbered canonical Ext spectral sequence `(E'_r, d'_r)_{r ≥ 2}` is bounded.

```lean
theorem renumberedCanonicalExtSpectralSequenceInto_isBounded (M K : DerivedCategory A)
    (K' : CochainComplex A ℤ) (e : DerivedCategory.Q.obj K' ≅ K)
    (hM : DerivedCategory.TStructure.t.minus M)
    (hK : DerivedCategory.TStructure.t.plus K) :
    IsBounded (renumberedCanonicalExtSpectralSequenceInto.{w', w} M K')
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequenceInto_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/TruncationFiltrationSpectralSequences.lean#L516). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G1Y, convergence after renumbering.** For `M ∈ D^-(A)` and `K ∈ D^+(A)` the
> renumbered canonical Ext spectral sequence converges to `Ext^{i + j}(M, K)`: the infinity page at
> `(i, j)` is the graded piece of `Stacks.Injectives.extIntoFiltration` from `-j + 1` to `-j` in
> total degree `i + j`.

```lean
theorem renumberedCanonicalExtSpectralSequenceInto_convergesToExt (M K : DerivedCategory A)
    (K' : CochainComplex A ℤ) (e : DerivedCategory.Q.obj K' ≅ K)
    (hM : DerivedCategory.TStructure.t.minus M)
    (hK : DerivedCategory.TStructure.t.plus K) :
    let E := renumberedCanonicalExtSpectralSequenceInto.{w', w} M K'
    let F := extIntoFiltration M (CochainComplex.canonicalTruncationFiltration K')
    ∃ hF : ∀ n : ℤ, Antitone (F n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
      (∀ i j : ℤ, E.HasPageInfinityAt (i, j)) ∧
      ∀ i j : ℤ, Nonempty
        ((E.pageInfinity (i, j) : Type v) ≃+
          ((Limits.cokernel (Subobject.ofLE (F (i + j) (-j + 1)) (F (i + j) (-j))
              (hF (i + j) (by omega))) : AddCommGrpCat.{w}) : Type w))
```

## Tag 0G1Z, a remark

[Tag 0G1Z](https://stacks.math.columbia.edu/tag/0G1Z) in the Stacks Project.

**`Stacks.Injectives.extSpectralSequence_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/ExtBoundedConvergence.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/ExtBoundedConvergence.lean#L530). The attribute's comment: “boundedness”.

> **Stacks 0G1Z, boundedness.** Under eventual vanishing and eventual comparison-isomorphism
> for Ext from the filtered quotients, the Ext spectral sequence is bounded.

```lean
public theorem extSpectralSequence_isBounded
    {A : Type u} [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{w} A] [HasDerivedCategory.{w} A]
    (K : DerivedCategory A) (M : CochainComplex.Filtered A)
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p ≤ p₀ →
      IsZero (AddCommGrpCat.of (DerivedCategory.Ext
        (DerivedCategory.Q.obj ((FilteredObject.quot (op p)).obj M)) K n)))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p₁ ≤ p →
      IsIso (extFromFilteredQuotient K M p n)) :
    IsBounded (extSpectralSequence K M).1
```

**`Stacks.Injectives.extSpectralSequence_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/ExtBoundedConvergence.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/ExtBoundedConvergence.lean#L548). The attribute's comment: “convergence”.

> **Stacks 0G1Z, convergence.** Under eventual vanishing and eventual
> comparison-isomorphism for Ext from the filtered quotients, the Ext spectral sequence converges
> to the Ext groups from the underlying complex, with the canonical quotient-image filtration.
> The graded quotient at `(p,q)` is the step from `-p` to `-p + 1`.

```lean
public theorem extSpectralSequence_convergesToExt
    {A : Type u} [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{w} A] [HasDerivedCategory.{w} A]
    (K : DerivedCategory A) (M : CochainComplex.Filtered A)
    (hzero : ∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p ≤ p₀ →
      IsZero (AddCommGrpCat.of (DerivedCategory.Ext
        (DerivedCategory.Q.obj ((FilteredObject.quot (op p)).obj M)) K n)))
    (hiso : ∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p₁ ≤ p →
      IsIso (extFromFilteredQuotient K M p n)) :
    let E := (extSpectralSequence K M).1
    ∃ hF : ∀ n : ℤ, Monotone (extQuotientFiltration K M n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ extQuotientFiltration K M n a = ⊥ ∧
        extQuotientFiltration K M n b = ⊤) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
        (E.pageInfinity (p, q) ≅
          cokernel (Subobject.ofLE (extQuotientFiltration K M (p + q) (-p))
            (extQuotientFiltration K M (p + q) (-p + 1)) (hF (p + q) (by omega))))
```

**`Stacks.Injectives.extSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/SpectralSequenceOfFilteredComplex.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/SpectralSequenceOfFilteredComplex.lean#L234). The attribute's comment: “spectral\_sequence”.

> **Stacks 0G1Z.** The Ext spectral sequence associated to a filtered complex `M`, bundled with
> the identifications `E₁^{p,q} = Ext^{p+q}(gr^{-p} M, K)`.  Its differential on page `r` has
> bidegree `(r, -r + 1)` by the definition of `CohomologicalSpectralSequence`.

```lean
noncomputable def extSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A]
    [IsGrothendieckAbelian.{w} A] [HasDerivedCategory.{w} A]
    (K : DerivedCategory A) (M : CochainComplex.Filtered A) :
    Σ E : CohomologicalSpectralSequence AddCommGrpCat.{w} 1,
      ∀ p q : ℤ,
        (E.page 1).X (p, q) ≅ AddCommGrpCat.of
          (DerivedCategory.Ext
            (DerivedCategory.Q.obj
              ((FilteredObject.gr (C := (CochainComplex A ℤ)) (-p)).obj M))
            K (p + q))
```

## Tag 0G20, a remark

[Tag 0G20](https://stacks.math.columbia.edu/tag/0G20) in the Stacks Project.

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L80). The attribute's comment: “renumbered\_e2”.

> 0G20 renumbered\_e2, declaration 1.

```lean
public noncomputable def renumberedCanonicalExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e) :
    CohomologicalSpectralSequence AddCommGrpCat.{w} 2
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequence_page_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L91). The attribute's comment: “renumbered\_e2”.

> 0G20 renumbered\_e2, declaration 2.

```lean
public theorem renumberedCanonicalExtSpectralSequence_page_two
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e) (i j : ℤ) :
    Nonempty
      (((renumberedCanonicalExtSpectralSequence S).page 2).X (i, j) ≅
        AddCommGrpCat.of
          (DerivedCategory.Ext ((DerivedCategory.singleFunctor A 0).obj
            ((DerivedCategory.homologyFunctor A (-j)).obj M)) K i))
```

**`Stacks.Injectives.canonicalExtSpectralSequence_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L277). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, boundedness before renumbering.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the canonical Ext spectral sequence is bounded.

```lean
public theorem canonicalExtSpectralSequence_isBounded
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    IsBounded S.spectralSequence
```

**`Stacks.Injectives.canonicalExtSpectralSequence_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L309). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, convergence before renumbering.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the canonical Ext spectral sequence converges to `Ext^(p+q)(M, K)`, with
> filtration index `-p`.

```lean
public theorem canonicalExtSpectralSequence_convergesToExt
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    let E := S.spectralSequence
    ∃ hF : ∀ n : ℤ, Monotone (canonicalExtFiltration S n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ canonicalExtFiltration S n a = ⊥ ∧
        canonicalExtFiltration S n b = ⊤) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
      (E.pageInfinity (p, q) ≅
          cokernel (Subobject.ofLE (canonicalExtFiltration S (p + q) (-p))
            (canonicalExtFiltration S (p + q) (-p + 1)) (hF (p + q) (by omega))))
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequence_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L358). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, boundedness after renumbering.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the renumbered canonical Ext spectral sequence is bounded.

```lean
public theorem renumberedCanonicalExtSpectralSequence_isBounded
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    IsBounded
      (renumberedCanonicalExtSpectralSequence S)
```

**`Stacks.Injectives.renumberedCanonicalExtSpectralSequence_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L375). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, convergence after renumbering.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the renumbered canonical Ext spectral sequence converges to
> `Ext^(i+j)(M, K)`, with filtration index `j`.

```lean
public theorem renumberedCanonicalExtSpectralSequence_convergesToExt
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    {M K : DerivedCategory A} {M' : CochainComplex A ℤ}
    {e : DerivedCategory.Q.obj M' ≅ M}
    (S : CanonicalExtSpectralSequence M K M' e)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    let E := renumberedCanonicalExtSpectralSequence S
    ∃ hF : ∀ n : ℤ, Monotone (canonicalExtFiltration S n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ canonicalExtFiltration S n a = ⊥ ∧
        canonicalExtFiltration S n b = ⊤) ∧
      (∀ i j : ℤ, E.HasPageInfinityAt (i, j)) ∧
      ∀ i j : ℤ, Nonempty
        (E.pageInfinity (i, j) ≅
          cokernel (Subobject.ofLE (canonicalExtFiltration S (i + j) j)
            (canonicalExtFiltration S (i + j) (j + 1)) (hF (i + j) (by omega))))
```

**`Stacks.Injectives.isBounded_canonicalExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L414). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, boundedness of the canonical Ext spectral sequence.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the Ext spectral sequence of the canonical truncation filtration
> `F^p M^• = τ_{≤ -p} M^•` of a complex `M^•` representing `M` is bounded.  This is
> `canonicalExtSpectralSequence_isBounded` at the filtration itself.

```lean
public theorem isBounded_canonicalExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (M K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (e : DerivedCategory.Q.obj M' ≅ M)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    IsBounded (canonicalExtSpectralSequence M K M' e).spectralSequence
```

**`Stacks.Injectives.convergesToExt_canonicalExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L430). The attribute's comment: “canonical\_convergence”.

> **Stacks 0G20, convergence of the canonical Ext spectral sequence.** For `M ∈ D⁻(A)` and
> `K ∈ D⁺(A)`, the Ext spectral sequence of the canonical truncation filtration
> `F^p M^• = τ_{≤ -p} M^•` of a complex `M^•` representing `M` converges to `Ext^{p+q}(M, K)`,
> with filtration index `-p`.  This is `canonicalExtSpectralSequence_convergesToExt` at the
> filtration itself.

```lean
public theorem convergesToExt_canonicalExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (M K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (e : DerivedCategory.Q.obj M' ≅ M)
    (hM : (DerivedCategory.TStructure.t (C := A)).minus M)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K) :
    let S := canonicalExtSpectralSequence M K M' e
    let E := S.spectralSequence
    ∃ hF : ∀ n : ℤ, Monotone (canonicalExtFiltration S n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ canonicalExtFiltration S n a = ⊥ ∧
        canonicalExtFiltration S n b = ⊤) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
      (E.pageInfinity (p, q) ≅
          cokernel (Subobject.ofLE (canonicalExtFiltration S (p + q) (-p))
            (canonicalExtFiltration S (p + q) (-p + 1)) (hF (p + q) (by omega))))
```

**`Stacks.Injectives.stupidExtSpectralSequence_isBounded`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L548). The attribute's comment: “stupid\_convergence”.

> **Stacks 0G20, boundedness of the brutal-truncation Ext spectral sequence.** If
> `K ∈ D⁺(A)` and the cochain complex `M^•` is bounded above, the Ext spectral sequence of the
> filtration `F^p M^• = σ_{≥ p} M^•` is bounded.

```lean
public theorem stupidExtSpectralSequence_isBounded
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K)
    (hM : CochainComplex.minus A M') :
    IsBounded (stupidExtSpectralSequence K M')
```

**`Stacks.Injectives.stupidExtSpectralSequence_convergesToExt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/CanonicalExtConvergence.lean#L563). The attribute's comment: “stupid\_convergence”.

> **Stacks 0G20, convergence of the brutal-truncation Ext spectral sequence.** If
> `K ∈ D⁺(A)` and the cochain complex `M^•` is bounded above, the Ext spectral sequence of the
> filtration `F^p M^• = σ_{≥ p} M^•` converges to `Ext^{p+q}(M^•, K)`, the Ext groups of the
> object `M` of the derived category represented by `M^•`, with filtration index `-p`.

```lean
public theorem stupidExtSpectralSequence_convergesToExt
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (hK : (DerivedCategory.TStructure.t (C := A)).plus K)
    (hM : CochainComplex.minus A M') :
    let E := stupidExtSpectralSequence K M'
    ∃ hF : ∀ n : ℤ, Monotone
        (extQuotientFiltration K (CochainComplex.stupidTruncationFiltration M') n),
      (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧
        extQuotientFiltration K (CochainComplex.stupidTruncationFiltration M') n a = ⊥ ∧
        extQuotientFiltration K (CochainComplex.stupidTruncationFiltration M') n b = ⊤) ∧
      (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
      ∀ p q : ℤ, Nonempty
        (E.pageInfinity (p, q) ≅
          cokernel (Subobject.ofLE
            (extQuotientFiltration K
              (CochainComplex.stupidTruncationFiltration M') (p + q) (-p))
            (extQuotientFiltration K
              (CochainComplex.stupidTruncationFiltration M') (p + q) (-p + 1))
            (hF (p + q) (by omega))))
```

**`Stacks.Injectives.canonicalExtSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean#L142). The attribute's comment: “canonical\_e1”.

> **Stacks 0G20, the canonical truncation filtration.** Let `A` be a Grothendieck abelian
> category and let `M, K ∈ D(A)`.  Every cochain complex representing `M`, filtered by
> `F^p M^• = τ_{≤ -p} M^•`, gives a cohomological spectral sequence whose first page is
> `E₁^{p,q} = Ext^{2p+q}(H^p(M), K)`.

```lean
noncomputable def canonicalExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (M K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (e : DerivedCategory.Q.obj M' ≅ M) :
    CanonicalExtSpectralSequence M K M' e
```

**`Stacks.Injectives.exists_canonicalExtSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean#L169). The attribute's comment: “canonical\_e1”.

> **Stacks 0G20, the canonical truncation filtration.** Let `A` be a Grothendieck abelian
> category and let `M, K ∈ D(A)`.  Every cochain complex representing `M`, filtered by
> `F^p M^• = τ_{≤ -p} M^•`, gives a cohomological spectral sequence whose first page is
> `E₁^{p,q} = Ext^{2p+q}(H^p(M), K)`.  This is `canonicalExtSpectralSequence` forgetting the
> construction.

```lean
theorem exists_canonicalExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (M K : DerivedCategory A) (M' : CochainComplex A ℤ)
    (e : DerivedCategory.Q.obj M' ≅ M) :
    Nonempty (CanonicalExtSpectralSequence M K M' e)
```

**`Stacks.Injectives.stupidExtSpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean#L182). The attribute's comment: “stupid\_e1”.

> **Stacks 0G20, the brutal truncation filtration.** The Ext spectral sequence of the
> filtration `F^p M^• = σ_{≥ p} M^•` of a cochain complex `M^•`, a cohomological spectral sequence
> `(E_r, d_r)_{r ≥ 1}`.  It is definitionally the construction of Tag 0G1Z applied to that filtered
> complex, so every page, differential and page-turning isomorphism is specified.

```lean
noncomputable def stupidExtSpectralSequence
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (K : DerivedCategory A) (M' : CochainComplex A ℤ) :
    CohomologicalSpectralSequence AddCommGrpCat.{w} 1
```

**`Stacks.Injectives.stupidExtSpectralSequenceE₁`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean#L195). The attribute's comment: “stupid\_e1”.

> **Stacks 0G20, the brutal truncation filtration.** The first page of the Ext spectral
> sequence of the filtration `F^p M^• = σ_{≥ p} M^•` is `E₁^{p,q} = Ext^q(M^{-p}, K)`.
>
> The index is `-p`, not `p`: the first page at `(p, q)` is `Ext^{p+q}` of the graded piece
> `gr^{-p}M^• = M^{-p}[p]`, and the shift moves `p + q` down to `q`.

```lean
noncomputable def stupidExtSpectralSequenceE₁
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A]
    (K : DerivedCategory A) (M' : CochainComplex A ℤ) (p q : ℤ) :
    ((stupidExtSpectralSequence K M').page 1).X (p, q) ≅
      AddCommGrpCat.of (DerivedCategory.Ext
        ((DerivedCategory.singleFunctor A 0).obj (M'.X (-p))) K q)
```

**`Stacks.Injectives.canonicalExtSpectralSequence_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean, line 420](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Ext/CanonicalSpectralSequence.lean#L420). The attribute's comment: “representative\_independence”.

> The canonical-truncation Ext spectral sequence is independent of the choice of complex
> representing `M`, as a spectral sequence from `E₁` onward.

```lean
theorem canonicalExtSpectralSequence_iso
    {A : Type u} [Category.{v} A] [Abelian A] [HasDerivedCategory.{w} A]
    [IsGrothendieckAbelian.{w} A] (M K : DerivedCategory A)
    (M₁ M₂ : CochainComplex A ℤ)
    (e₁ : DerivedCategory.Q.obj M₁ ≅ M) (e₂ : DerivedCategory.Q.obj M₂ ≅ M)
    (S₁ : CanonicalExtSpectralSequence M K M₁ e₁)
    (S₂ : CanonicalExtSpectralSequence M K M₂ e₂) :
    Nonempty (S₁.spectralSequence ≅ S₂.spectralSequence)
```

## Tag 0ESJ, a lemma

[Tag 0ESJ](https://stacks.math.columbia.edu/tag/0ESJ) in the Stacks Project.

**`Stacks.Injectives.exists_filteredComplex_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/FilteredComplex/InverseSystemRepresentation.lean, line 989](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/FilteredComplex/InverseSystemRepresentation.lean#L989).

> Let `A` be a Grothendieck abelian category, `E` an object of `D(A)`, and `F` an inverse
> system of objects of `D(A)` indexed by `ℤᵒᵖ` together with a compatible family of maps `φ` from
> `F` to the constant system at `E`. Then there is a filtered cochain complex `K` whose underlying
> complex represents `E`, whose derived filtration diagram is isomorphic to `F`, and whose
> filtration inclusions induce the maps `φ`.

```lean
theorem exists_filteredComplex_representation
    (E : DerivedCategory A) (F : ℤᵒᵖ ⥤ DerivedCategory A)
    (φ : F ⟶ (Functor.const ℤᵒᵖ).obj E) :
    ∃ (K : CochainComplex.Filtered A)
      (e : DerivedCategory.Q.obj K.X ≅ E)
      (η : K.filtration.diagram ⋙ DerivedCategory.Q ≅ F),
      ∀ i : ℤᵒᵖ,
        DerivedCategory.Q.map (K.filtration.ι.app i) ≫ e.hom =
          η.hom.app i ≫ φ.app i
```

## Tag 0ESK, a lemma

[Tag 0ESK](https://stacks.math.columbia.edu/tag/0ESK) in the Stacks Project.

**`Stacks.Injectives.exists_bifilteredComplex_representation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Grothendieck/BifilteredRepresentation.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Grothendieck/BifilteredRepresentation.lean#L208).

> **Stacks 0ESK.** Two inverse systems of objects of the derived category of a Grothendieck
> abelian category, each with a compatible family of maps to one object `E`, can be represented by
> two filtrations of a single cochain complex.

```lean
theorem exists_bifilteredComplex_representation
    (E : DerivedCategory A)
    (F F' : ℤᵒᵖ ⥤ DerivedCategory A)
    (φ : F ⟶ (Functor.const ℤᵒᵖ).obj E)
    (φ' : F' ⟶ (Functor.const ℤᵒᵖ).obj E) :
    ∃ (K : CochainComplex.Filtered A)
      (filtration' : Filtration K.X ℤᵒᵖ)
      (e : DerivedCategory.Q.obj K.X ≅ E)
      (η : K.filtration.diagram ⋙ DerivedCategory.Q ≅ F)
      (η' : filtration'.diagram ⋙ DerivedCategory.Q ≅ F'),
      (∀ i : ℤᵒᵖ,
        DerivedCategory.Q.map (K.filtration.ι.app i) ≫ e.hom =
          η.hom.app i ≫ φ.app i) ∧
      (∀ i : ℤᵒᵖ,
        DerivedCategory.Q.map (filtration'.ι.app i) ≫ e.hom =
          η'.hom.app i ≫ φ'.app i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.13, Tag 07D6](https://stacks.math.columbia.edu/tag/07D6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
