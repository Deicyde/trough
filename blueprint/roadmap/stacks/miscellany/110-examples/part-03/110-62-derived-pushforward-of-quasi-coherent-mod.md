---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_isDerivedLimit_truncGETower_of_lqcohSheafFbc_algebraicStack, AlgebraicGeometry.Stack.isIso_coproductToProduct_shiftedSingleFamily_algebraicStack, Stacks.Examples.UnboundedDerivedPushforward.not_forall_derivedPushforward_mem_derivedLocallyQuasicoherentFlatBaseChange, Stacks.Examples.UnboundedDerivedPushforward.exists_not_derivedCategoryB_lqcFbcFppf_derivedPushforward, Stacks.Examples.UnboundedDerivedPushforward.exists_isQuasiCompact_isQuasiSeparated_not_derivedCategoryB_derivedPushforward
statement: formalized
proof: formalized
---

# 110.62 Derived pushforward of quasi-coherent modules

Section 110.62 of the Stacks Project, [Tag 07DC](https://stacks.math.columbia.edu/tag/07DC). 3 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08IY, a lemma

[Tag 08IY](https://stacks.math.columbia.edu/tag/08IY) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_isDerivedLimit_truncGETower_of_lqcohSheafFbc_algebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafLqcFbcDerivedLimitOfTruncations.lean, line 97](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/SheafLqcFbcDerivedLimitOfTruncations.lean#L97). The attribute's comment: “K is the derived limit of its canonical truncations from below: the distinguished triangle K → ∏ τ\_\{≥ -n}K → ∏ τ\_\{≥ -n}K → K[1] in D(𝒪\_𝒳), for an algebraic stack 𝒳 and a complex of fppf 𝒪\_𝒳-modules whose cohomology sheaves are locally quasi-coherent with the flat base change property of 0762, read with the inverse image of sheaves of modules”.

> **Stacks 08IY.** Let `𝒳` be an algebraic stack and let `K` be an object of `D(𝒪_𝒳)`, the
> derived category of the sheaves of `𝒪_𝒳`-modules on the fppf site of `𝒳`, whose cohomology
> sheaves are locally quasi-coherent (**Stacks 06WJ**) and have the flat base change property of
> **Stacks 0762**, read with the inverse image of sheaves of modules.  Then there is a distinguished
> triangle
>
> `K ⟶ ∏_{n ≥ 0} τ_{≥ -n}K ⟶ ∏_{n ≥ 0} τ_{≥ -n}K ⟶ K[1]`
>
> in `D(𝒪_𝒳)`: the product of the tower `n ↦ τ_{≥ -n}K` exists and `K` is its derived limit
> (`CategoryTheory.Pretriangulated.IsDerivedLimit`, **Stacks 08TC**), the second arrow being
> `1 - shift`.
>
> As in the source: the higher cohomology of a module in `LQCoh^fbc(𝒪_𝒳)` vanishes over the
> objects lying over an affine scheme
> (`AlgebraicGeometry.Stack.isZero_rightDerived_evaluation_of_sheafFlatBaseChange_algebraicStack`),
> those objects cover `𝒳_fppf`
> (`AlgebraicGeometry.Stack.hasEnoughObjects_isAffineOver_of_essentiallySmall`), and the
> convergence criterion of **Stacks 0D6P** with `d = 0` applies
> (`Stacks.Cohomology.AcyclicCover.isIso_to_isDerivedLimit_truncGETower_of_acyclic`).

```lean
theorem exists_isDerivedLimit_truncGETower_of_lqcohSheafFbc_algebraicStack
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (K : DerivedCategory (fppfSiteModules B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids))
    (hK : ∀ i : ℤ, IsLocallyQuasicoherentWithSheafFlatBaseChange.{u, _, _, u} B E h S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids
      ((DerivedCategory.homologyFunctor
        (fppfSiteModules B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids) i).obj K).val) :
    ∃ _ : HasProduct fun n : ℕ ↦
        (fppfTruncGETower B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids K).obj ⟨n⟩,
      IsDerivedLimit (fppfTruncGETower B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids K) K
```

## Tag 08IZ, a lemma

[Tag 08IZ](https://stacks.math.columbia.edu/tag/08IZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isIso_coproductToProduct_shiftedSingleFamily_algebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ShiftedSumOfModulesAlgebraicStack.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/ShiftedSumOfModulesAlgebraicStack.lean#L108). The attribute's comment: “for an algebraic stack 𝒳 and a family (ℱ\_n)\_\{n ≥ 0} of locally quasi-coherent fppf 𝒪\_𝒳-modules with the flat base change property of 0762 (read with the inverse image of sheaves of modules), the canonical map ⊕\_n ℱ\_n[n] → ∏\_n ℱ\_n[n] is an isomorphism in D(𝒪\_𝒳); the index n runs over n ≥ 0, the case the section applies”.

> **Stacks 08IZ.** Let `𝒳` be an algebraic stack and let `ℱ_n`, `n ≥ 0`, be sheaves of
> `𝒪_𝒳`-modules on its big fppf site which are locally quasi-coherent (**Stacks 06WJ**) and have
> the flat base change property of **Stacks 0762**, read with the inverse image of sheaves of
> modules.  Then the canonical map
>
> `⊕_n ℱ_n[n] ⟶ ∏_n ℱ_n[n]`
>
> is an isomorphism in `D(𝒪_𝒳)`.
>
> As in the source, this is **Stacks 08IY** for the sum: the higher cohomology of each `ℱ_n`
> vanishes over the objects lying over an affine scheme
> (`AlgebraicGeometry.Stack.isZero_rightDerived_evaluation_of_sheafFlatBaseChange_algebraicStack`),
> those objects cover `𝒳_fppf`
> (`AlgebraicGeometry.Stack.hasEnoughObjects_isAffineOver_of_essentiallySmall`), and
> `AlgebraicGeometry.Stack.isIso_coproductToProduct_shiftedSingleFamily_of_isZero_rightDerived`
> concludes.

```lean
theorem isIso_coproductToProduct_shiftedSingleFamily_algebraicStack
    (𝒳 : AlgebraicStacks.{u, w} B S hS)
    (F : ℕ → fppfSiteModules B S hS 𝒳.val.val.p 𝒳.val.isFiberedInGroupoids)
    (hF : ∀ n : ℕ, IsLocallyQuasicoherentWithSheafFlatBaseChange.{u, _, _, u} B E h S hS
      𝒳.val.val.p 𝒳.val.isFiberedInGroupoids (F n).val) :
    IsIso (Pi.lift (Sigma.π (shiftedSingleFamily B S hS 𝒳.val.val.p
      𝒳.val.isFiberedInGroupoids F)))
```

## Tag 07DD, a lemma

[Tag 07DD](https://stacks.math.columbia.edu/tag/07DD) in the Stacks Project.

**`Stacks.Examples.UnboundedDerivedPushforward.not_forall_derivedPushforward_mem_derivedLocallyQuasicoherentFlatBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardCounterexample.lean, line 348](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardCounterexample.lean#L348). The attribute's comment: “D\_QCoh is read through the subcategory D\_LQCoh^fbc of D(O) whose Verdier quotient it is (Tag 07B6), and Rf\_* is the unbounded total derived direct image; the witness is the counterexample of Tag 07DC with p = 2”.

> **Stacks 07DD.** A quasi-compact, quasi-separated morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks
> need not send `D_{LQCoh^fbc}(𝒪_𝒳)` into `D_{LQCoh^fbc}(𝒪_𝒴)` under the unbounded derived direct
> image `Rf_*`, read at module universe `u + 1`. The counterexample is the discussion of
> **Stacks 07DC** with `p = 2`: `k = 𝔽₂`, `S = Spec k[x]`, `f : B(ℤ/2)_S ⟶ S` the structure
> morphism and `E = ∏_{m ≥ 0} 𝒪_𝒳[m]`. The object `E` lies in `D_{LQCoh^fbc}(𝒪_𝒳)`
> (`shiftedStructureSheafProduct_mem`), `Rf_*𝒪_𝒳` is computed by the cochain complex of `ℤ/2` with
> coefficients `𝒪_S`
> (`AlgebraicGeometry.Stack.ClassifyingZModTwo.derivedPushforwardStructureModuleIso` and
> `AlgebraicGeometry.Stack.ClassifyingZModTwo.cechCosimplicialIso`), and then `H⁰(Rf_*E)` is a
> countable product of copies of `𝒪_S`, which is not locally quasi-coherent
> (`not_mem_derivedPushforward_of_iso`).

```lean
theorem not_forall_derivedPushforward_mem_derivedLocallyQuasicoherentFlatBaseChange :
    ¬ ∀ (B : BigFppfSite.{u}) (E : BigEtaleSite.{u}) (h : E.cutoff = B.cutoff) (S : Scheme.{u})
        (hS : B.Contains S) (𝒳 𝒴 : AlgebraicStacks.{u, w} B S hS)
        [HasDerivedCategory.{u + 2} (fppfModulesUnivLE.{u, w, u + 1} B S hS 𝒳)]
        [HasDerivedCategory.{u + 2} (fppfModulesUnivLE.{u, w, u + 1} B S hS 𝒴)] (f : 𝒳 ⟶ 𝒴),
        IsQuasiCompactMorphism B S hS f → AlgebraicStacks.IsQuasiSeparated B S hS f →
        ∀ K, derivedLocallyQuasicoherentFlatBaseChangeUnivLE.{u, w, u + 1} B E h S hS 𝒳 K →
          derivedLocallyQuasicoherentFlatBaseChangeUnivLE.{u, w, u + 1} B E h S hS 𝒴
            ((fppfDerivedPushforwardOfStacks B S hS f).obj K)
```

**`Stacks.Examples.UnboundedDerivedPushforward.exists_not_derivedCategoryB_lqcFbcFppf_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardStacks.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardStacks.lean#L113). The attribute's comment: “for the source's example: f : [Spec k[x]/(Z/pZ)] -> Spec k[x] with char k = p, over any big fppf site containing Spec k[x], E = sum of O\_X[m] in D\_LQCoh^fbc(O\_X) and Rf\_*E not in D\_LQCoh^fbc(O\_S), with LQCoh^fbc the class of the Verdier quotient D\_QCoh of 07B6 and Rf\_* the unbounded total derived direct image”.

> **Stacks 07DD**, for the source's own example. Let `k` be a field of characteristic `p > 0`,
> `S = Spec k[x]`, and let `𝒞` be any big fppf site containing `S`. The classifying stack
> `𝒳 = [S/(ℤ/pℤ)]` and `S` itself are algebraic stacks over `S`, the structure morphism
> `f : 𝒳 ⟶ S` is quasi-compact and quasi-separated, and for every choice of derived categories
> the object `E = ⊕_{m ≥ 0} 𝒪_𝒳[m]` lies in `D_{LQCoh^fbc}(𝒪_𝒳)` while `Rf_*E` does not lie in
> `D_{LQCoh^fbc}(𝒪_S)`. So `Rf_*` does not carry `D_{LQCoh^fbc}(𝒪_𝒳)` into `D_{LQCoh^fbc}(𝒪_S)`
> and does not induce a functor `D_QCoh(𝒪_𝒳) ⟶ D_QCoh(𝒪_S)` on the Verdier quotients of
> **Stacks 07B6** (`AlgebraicGeometry.Stack.derivedCategoryQuasicoherentSheaf`, whose subcategory
> `LQCoh^fbc` is `AlgebraicGeometry.Stack.lqcFbcFppf`).
>
> `Rf_*` is the total right derived functor of the direct image of **Stacks 06WE** on the
> unbounded derived categories of fppf modules
> (`AlgebraicGeometry.Stack.fppfModulesDerivedPushforward`).
> The proof is the discussion of **Stacks 07DC**: see the module documentation.

```lean
theorem exists_not_derivedCategoryB_lqcFbcFppf_derivedPushforward (p : ℕ) [Fact p.Prime]
    {k : Type u} [Field k] [CharP k p] (𝒞 : BigFppfSite.{u})
    (hS : 𝒞.Contains (Spec (.of (Polynomial k)))) :
    ∃ (𝒳 𝒴 : AlgebraicStacks.{u, w} 𝒞 (Spec (.of (Polynomial k))) hS) (f : 𝒳 ⟶ 𝒴),
      IsQuasiCompactMorphism 𝒞 _ hS f ∧ AlgebraicStacks.IsQuasiSeparated 𝒞 _ hS f ∧
      ∀ [HasDerivedCategory.{t} (fppfModules 𝒞 _ hS 𝒳)]
        [HasDerivedCategory.{t} (fppfModules 𝒞 _ hS 𝒴)],
        ∃ E : DerivedCategory (fppfModules 𝒞 _ hS 𝒳),
          DerivedCategoryB.derivedCategoryB (lqcFbcFppf 𝒞 _ hS 𝒳) E ∧
            ¬ DerivedCategoryB.derivedCategoryB (lqcFbcFppf 𝒞 _ hS 𝒴)
              ((fppfModulesDerivedPushforward 𝒞 _ hS f).obj E)
```

**`Stacks.Examples.UnboundedDerivedPushforward.exists_isQuasiCompact_isQuasiSeparated_not_derivedCategoryB_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardStacks.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Examples/UnboundedDerivedPushforwardStacks.lean#L154). The attribute's comment: “Rf\_* does not carry D\_LQCoh^fbc(O\_X) into D\_LQCoh^fbc(O\_Y) for some qcqs f of algebraic stacks, so it does not induce D\_QCoh(O\_X) -> D\_QCoh(O\_Y) on the Verdier quotients of 07B6; Rf\_* is the unbounded total derived direct image”.

> **Stacks 07DD.** A quasi-compact and quasi-separated morphism `f : 𝒳 ⟶ 𝒴` of algebraic
> stacks need not induce a functor `Rf_* : D_QCoh(𝒪_𝒳) ⟶ D_QCoh(𝒪_𝒴)`: there are a big fppf site
> `𝒞`, a scheme `S` in it, algebraic stacks `𝒳`, `𝒴` over `S` and a quasi-compact and
> quasi-separated `f : 𝒳 ⟶ 𝒴` such that, for every choice of derived categories, some object `E` of
> `D_{LQCoh^fbc}(𝒪_𝒳)` has `Rf_*E` outside `D_{LQCoh^fbc}(𝒪_𝒴)`. The witness is the source's, with
> `p = 2`: `exists_not_derivedCategoryB_lqcFbcFppf_derivedPushforward`.

```lean
theorem exists_isQuasiCompact_isQuasiSeparated_not_derivedCategoryB_derivedPushforward :
    ∃ (𝒞 : BigFppfSite.{u}) (S : Scheme.{u}) (hS : 𝒞.Contains S)
      (𝒳 𝒴 : AlgebraicStacks.{u, w} 𝒞 S hS) (f : 𝒳 ⟶ 𝒴),
      IsQuasiCompactMorphism 𝒞 S hS f ∧ AlgebraicStacks.IsQuasiSeparated 𝒞 S hS f ∧
      ∀ [HasDerivedCategory.{t} (fppfModules 𝒞 S hS 𝒳)]
        [HasDerivedCategory.{t} (fppfModules 𝒞 S hS 𝒴)],
        ∃ E : DerivedCategory (fppfModules 𝒞 S hS 𝒳),
          DerivedCategoryB.derivedCategoryB (lqcFbcFppf 𝒞 S hS 𝒳) E ∧
            ¬ DerivedCategoryB.derivedCategoryB (lqcFbcFppf 𝒞 S hS 𝒴)
              ((fppfModulesDerivedPushforward 𝒞 S hS f).obj E)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.62, Tag 07DC](https://stacks.math.columbia.edu/tag/07DC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
