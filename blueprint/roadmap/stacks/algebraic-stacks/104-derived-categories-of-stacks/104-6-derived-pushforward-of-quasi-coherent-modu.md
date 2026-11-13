---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.derivedPushforwardQuasicoherentPlus_comp_plusCohomology, AlgebraicGeometry.Stack.derivedPushforwardQuasicoherentPlus_comp_plusCohomologyDerivedCategory, AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward, AlgebraicGeometry.Stack.derivedParasiticLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward, AlgebraicGeometry.Stack.derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange, AlgebraicGeometry.Stack.derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange_comp_ι, AlgebraicGeometry.Stack.derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange, AlgebraicGeometry.Stack.derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange_comp_ι
statement: formalized
proof: formalized
---

# 104.6 Derived pushforward of quasi-coherent modules

Section 104.6 of the Stacks Project, [Tag 07BB](https://stacks.math.columbia.edu/tag/07BB). 1 tag here is carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07BC, a proposition

[Tag 07BC](https://stacks.math.columbia.edu/tag/07BC) in the Stacks Project.

**`AlgebraicGeometry.Stack.derivedPushforwardQuasicoherentPlus_comp_plusCohomology`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardCohomologyComparison.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardCohomologyComparison.lean#L211). The attribute's comment: “the final assertion of the tag: the functors Rⁱf\_QCoh of Stacks 077A are Hⁱ ∘ Rf\_(QCoh,*), read as the identification of Q\_𝒳 ⋙ Rf\_(QCoh,*) ⋙ Hⁱ with Rf\_*^LQCoh ⋙ (Q ∘ Hⁱ) over the defining identity (104.5.1.1) of Hⁱ, at the module universe u + 1 that the derived direct image of Stacks 06WE on an algebraic stack lives in”.

> **Stacks 07BC, the final assertion.** For a quasi-compact and quasi-separated 1-morphism
> `f : 𝒳 ⟶ 𝒴` of algebraic stacks, the cohomology functor `Hⁱ` of **Stacks 07B7** composed with
> the induced functor `Rf_{QCoh,*} : D⁺_QCoh(𝒪_𝒳) ⥤ D⁺_QCoh(𝒪_𝒴)` is the higher direct image of
> **Stacks 077A**: precomposed with the quotient functor of `𝒳` it is the middle vertical functor
> `Rf_*^{LQCoh}` of the diagram of **Stacks 07BC** followed by `Q ∘ Hⁱ`, which is `Q ∘ Rⁱf_*`.
>
> `Hⁱ` is taken here as any functor on `D⁺_QCoh(𝒪_𝒴)` equipped with the defining identity `α`
> (104.5.1.1); `AlgebraicGeometry.Stack.plusCohomologyDerivedCategoryQuasicoherent` is one.

```lean
def derivedPushforwardQuasicoherentPlus_comp_plusCohomology (i : ℤ)
    (H : derivedCategoryQuasicoherentPlus B E h S hS 𝒴 ⥤
      AlgebraicStacks.fppfQuasicoherentModules B S hS 𝒴)
    (α : toDerivedCategoryQuasicoherentPlus B E h S hS 𝒴 ⋙ H ≅
      plusCohomologyQuasicoherent B E h S hS 𝒴 hclosed hwp hsep i) :
    toDerivedCategoryQuasicoherentPlus B E h S hS 𝒳 ⋙
        derivedPushforwardQuasicoherentPlus B E h S hS f hf hdist hpar ⋙ H ≅
      derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange B E h S hS f hf ⋙
        plusCohomologyQuasicoherent B E h S hS 𝒴 hclosed hwp hsep i
```

**`AlgebraicGeometry.Stack.derivedPushforwardQuasicoherentPlus_comp_plusCohomologyDerivedCategory`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardCohomologyComparison.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardCohomologyComparison.lean#L230). The attribute's comment: “the final assertion of the tag for the cohomology functor Hⁱ built as the descent of Q ∘ Hⁱ through the quotient of Stacks 07B6”.

> **Stacks 07BC, the final assertion**, for the cohomology functor
> `AlgebraicGeometry.Stack.plusCohomologyDerivedCategoryQuasicoherent` built here: its defining
> identity is `AlgebraicGeometry.Stack.plusCohomologyDerivedCategoryQuasicoherentFac`.

```lean
def derivedPushforwardQuasicoherentPlus_comp_plusCohomologyDerivedCategory (i : ℤ)
    (hinv : (derivedQuasicoherentWPlus B E h S hS 𝒴).IsInvertedBy
      (plusCohomologyQuasicoherent B E h S hS 𝒴 hclosed hwp hsep i)) :
    toDerivedCategoryQuasicoherentPlus B E h S hS 𝒳 ⋙
        derivedPushforwardQuasicoherentPlus B E h S hS f hf hdist hpar ⋙
          plusCohomologyDerivedCategoryQuasicoherent B E h S hS 𝒴 hclosed hwp hsep i hinv ≅
      derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange B E h S hS f hf ⋙
        plusCohomologyQuasicoherent B E h S hS 𝒴 hclosed hwp hsep i
```

**`AlgebraicGeometry.Stack.derivedLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 294](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L294). The attribute's comment: “for a quasi-compact quasi-separated f, the clause `Rf_* carries D⁺_LQCoh^fbc(𝒪_𝒳) into D⁺_LQCoh^fbc(𝒪_𝒴)`, by the source's own argument over the spectral sequence Rⁱf\_*Hʲ(E) ⇒ Rⁱ⁺ʲf\_*E with a page in LQCoh^fbc (Stacks 0771) and the weak Serre condition on LQCoh^fbc (Stacks 0771 part (2), fppf half), neither of which this library has”.

> For a quasi-compact and quasi-separated 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, if
> `LQCoh^fbc(𝒪_𝒴)` is a weak Serre subcategory and the spectral sequence `Rⁱf_*Hʲ(K) ⇒ Rⁱ⁺ʲf_*K`
> has a page in `LQCoh^fbc(𝒪_𝒴)`, then the total derived direct image `Rf_*` carries
> `D⁺_{LQCoh^fbc}(𝒪_𝒳)` into `D⁺_{LQCoh^fbc}(𝒪_𝒴)`.

```lean
theorem derivedLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward
    [(locallyQuasicoherentFlatBaseChangeFppfModulesUnivLE.{u, w, u + 1} B E h S hS
      𝒴).IsWeakSerreClass]
    (f : 𝒳 ⟶ 𝒴)
    (hss : IsQuasiCompactMorphism B S hS f → AlgebraicStacks.IsQuasiSeparated B S hS f →
      HasPushforwardCohomologySpectralSequence B S hS f
        (derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳)
        (locallyQuasicoherentFlatBaseChangeFppfModulesUnivLE.{u, w, u + 1} B E h S hS 𝒴))
    (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (K : DerivedCategory.Plus (fppfModulesUnivLE.{u, w, u + 1} B S hS 𝒳))
    (hK : derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K) :
    derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
      ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)
```

**`AlgebraicGeometry.Stack.derivedParasiticLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L320). The attribute's comment: “for a quasi-compact quasi-separated f, the clause `Rf_* carries D⁺_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒳) into D⁺_(Parasitic ∩ LQCoh^fbc)(𝒪_𝒴)`, by the source's own argument over the same spectral sequence with a page in Parasitic ∩ LQCoh^fbc (Stacks 0775 with Stacks 0771) and the weak Serre condition on it (Stacks 0774 part (2), which this library has, with Stacks 0771 part (2), which it does not)”.

> For a quasi-compact and quasi-separated 1-morphism `f : 𝒳 ⟶ 𝒴` of algebraic stacks, if
> `Parasitic ∩ LQCoh^fbc(𝒪_𝒴)` is a weak Serre subcategory and the spectral sequence
> `Rⁱf_*Hʲ(K) ⇒ Rⁱ⁺ʲf_*K` has a page in it, then the total derived direct image `Rf_*` carries
> `D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` into `D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒴)`.

```lean
theorem derivedParasiticLocallyQuasicoherentFlatBaseChangePlus_derivedPushforward
    [(parasiticModules.{u, w, u + 1} B S hS 𝒴 .fppf ⊓
      locallyQuasicoherentFlatBaseChangeFppfModulesUnivLE.{u, w, u + 1} B E h S hS
        𝒴).IsWeakSerreClass]
    (f : 𝒳 ⟶ 𝒴)
    (hss : IsQuasiCompactMorphism B S hS f → AlgebraicStacks.IsQuasiSeparated B S hS f →
      HasPushforwardCohomologySpectralSequence B S hS f
        (derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳)
        (parasiticModules.{u, w, u + 1} B S hS 𝒴 .fppf ⊓
          locallyQuasicoherentFlatBaseChangeFppfModulesUnivLE.{u, w, u + 1} B E h S hS 𝒴))
    (hqc : IsQuasiCompactMorphism B S hS f)
    (hqs : AlgebraicStacks.IsQuasiSeparated B S hS f)
    (K : DerivedCategory.Plus (fppfModulesUnivLE.{u, w, u + 1} B S hS 𝒳))
    (hK : derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K) :
    derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
      ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)
```

**`AlgebraicGeometry.Stack.derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L346). The attribute's comment: “the middle vertical functor D⁺\_LQCoh^fbc(𝒪\_𝒳) ⥤ D⁺\_LQCoh^fbc(𝒪\_𝒴) of the diagram, over the preservation clause it restricts”.

> The restriction of `Rf_* : D⁺(𝒪_𝒳) ⥤ D⁺(𝒪_𝒴)` to a functor
> `D⁺_{LQCoh^fbc}(𝒪_𝒳) ⥤ D⁺_{LQCoh^fbc}(𝒪_𝒴)`, given that `Rf_*` carries the one into the
> other.

```lean
def derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    (derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳).FullSubcategory ⥤
      (derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴).FullSubcategory
```

**`AlgebraicGeometry.Stack.derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange_comp_ι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L362). The attribute's comment: “the middle-to-right commuting square of the diagram, READ IN D⁺(𝒪\_𝒳) AND NOT IN THE SOURCE'S UNBOUNDED D(𝒪\_𝒳): the unbounded right derived direct image is not constructed in this library”.

> The middle vertical functor followed by the inclusion of `D⁺_{LQCoh^fbc}(𝒪_𝒴)` into
> `D⁺(𝒪_𝒴)` is the inclusion of `D⁺_{LQCoh^fbc}(𝒪_𝒳)` followed by `Rf_*`.

```lean
def derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange_comp_ι (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange B E h S hS f hf ⋙
        (derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴).ι ≅
      (derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳).ι ⋙
        fppfDerivedPushforwardPlusOfStacks B S hS f
```

**`AlgebraicGeometry.Stack.derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 391](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L391). The attribute's comment: “the left vertical functor D⁺\_(Parasitic ∩ LQCoh^fbc)(𝒪\_𝒳) ⥤ D⁺\_(Parasitic ∩ LQCoh^fbc)(𝒪\_𝒴) of the diagram, over the two preservation clauses it restricts”.

> The restriction of the middle vertical functor to a functor
> `D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) ⥤ D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒴)`, given that `Rf_*` carries
> the one into the other.

```lean
def derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K))
    (hpar : ∀ K, derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    (parasiticInDerivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳).FullSubcategory ⥤
      (parasiticInDerivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴).FullSubcategory
```

**`AlgebraicGeometry.Stack.derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange_comp_ι`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 409](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L409). The attribute's comment: “the left-to-middle commuting square of the diagram”.

> The left vertical functor followed by
> the inclusion of `D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒴)` into `D⁺_{LQCoh^fbc}(𝒪_𝒴)` is the inclusion
> of `D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳)` followed by the middle vertical functor.

```lean
def derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange_comp_ι (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K))
    (hpar : ∀ K, derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    derivedPushforwardPlusParasiticLocallyQuasicoherentFlatBaseChange B E h S hS f hf hpar ⋙
        (parasiticInDerivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴).ι ≅
      (parasiticInDerivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳).ι ⋙
        derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange B E h S hS f hf
```

**`AlgebraicGeometry.Stack.derivedPushforwardQuasicoherentPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 469](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L469). The attribute's comment: “the induced functor Rf\_(QCoh,*) : D⁺\_QCoh(𝒪\_𝒳) ⥤ D⁺\_QCoh(𝒪\_𝒴) on the Verdier quotients of Stacks 07B6, over the two preservation clauses and over the triangulatedness of Rf\_* (a Mathlib TODO for rightDerivedFunctorPlus)”.

> The derived direct image
>
> `Rf_{QCoh,*} : D⁺_QCoh(𝒪_𝒳) ⥤ D⁺_QCoh(𝒪_𝒴)`
>
> that `Rf_*` induces on the bounded-below Verdier quotients of **Stacks 07B6**: the functor out of
> the localization through which `D⁺_{LQCoh^fbc}(𝒪_𝒳) ⥤ D⁺_{LQCoh^fbc}(𝒪_𝒴) ⥤ D⁺_QCoh(𝒪_𝒴)`
> factors.

```lean
def derivedPushforwardQuasicoherentPlus (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K))
    (hdist : DerivedPushforwardMapsDistinguished B S hS f)
    (hpar : ∀ K, derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    derivedCategoryQuasicoherentPlus B E h S hS 𝒳 ⥤
      derivedCategoryQuasicoherentPlus B E h S hS 𝒴
```

**`AlgebraicGeometry.Stack.toDerivedCategoryQuasicoherentPlus_comp_derivedPushforwardQuasicoherentPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/DerivedPushforwardQuasicoherent.lean#L489). The attribute's comment: “the square identifying the induced functor on quotient categories, Q\_𝒳 ⋙ Rf\_(QCoh,*) = Rf\_*^LQCoh ⋙ Q\_𝒴”.

> The functor `Rf_{QCoh,*}` on the Verdier quotients is induced by `Rf_*`: precomposing it
> with the quotient functor of `𝒳` gives the middle vertical functor followed by the quotient
> functor of `𝒴`.

```lean
theorem toDerivedCategoryQuasicoherentPlus_comp_derivedPushforwardQuasicoherentPlus
    (f : 𝒳 ⟶ 𝒴)
    (hf : ∀ K, derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K))
    (hdist : DerivedPushforwardMapsDistinguished B S hS f)
    (hpar : ∀ K, derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒳 K →
      derivedParasiticLocallyQuasicoherentFlatBaseChangePlus B E h S hS 𝒴
        ((fppfDerivedPushforwardPlusOfStacks B S hS f).obj K)) :
    toDerivedCategoryQuasicoherentPlus B E h S hS 𝒳 ⋙
        derivedPushforwardQuasicoherentPlus B E h S hS f hf hdist hpar =
      derivedPushforwardPlusLocallyQuasicoherentFlatBaseChange B E h S hS f hf ⋙
        toDerivedCategoryQuasicoherentPlus B E h S hS 𝒴
```

**`AlgebraicGeometry.Stack.sheafFlatBaseChangeDerivedPushforwardPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L145). The attribute's comment: “the middle vertical arrow Rf\_* : D⁺\_LQCoh^fbc(𝒪\_𝒳) ⥤ D⁺\_LQCoh^fbc(𝒪\_𝒴) of the diagram, for the faithful LQCoh^fbc (flat base change with the sheaf pullback, Stacks 0762), at module universe u + 1”.

> **Stacks 07BC, the middle vertical arrow** `Rf_* : D⁺_{LQCoh^fbc}(𝒪_𝒳) ⥤ D⁺_{LQCoh^fbc}(𝒪_𝒴)`
> for a quasi-compact quasi-separated `f`: the restriction of `Rf_*`.

```lean
def sheafFlatBaseChangeDerivedPushforwardPlus :
    (DerivedCategoryB.derivedCategoryBInPlus
      (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
        𝒳)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryBInPlus
        (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
          𝒴)).FullSubcategory
```

**`AlgebraicGeometry.Stack.parasiticSheafFlatBaseChangeDerivedPushforwardPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L160). The attribute's comment: “the left vertical arrow Rf\_* : D⁺\_(Parasitic ∩ LQCoh^fbc)(𝒪\_𝒳) ⥤ D⁺\_(Parasitic ∩ LQCoh^fbc)(𝒪\_𝒴) of the diagram”.

> **Stacks 07BC, the left vertical arrow**
> `Rf_* : D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒳) ⥤ D⁺_{Parasitic ∩ LQCoh^fbc}(𝒪_𝒴)` for a quasi-compact
> quasi-separated `f`: the restriction of `Rf_*` (the parasitic half is **Stacks 0775** (2)).

```lean
def parasiticSheafFlatBaseChangeDerivedPushforwardPlus :
    (DerivedCategoryB.derivedCategoryBInPlus
      (parasiticModules.{u, w, u + 1} B S hS 𝒳 .fppf ⊓
        lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
          𝒳)).FullSubcategory ⥤
      (DerivedCategoryB.derivedCategoryBInPlus
        (parasiticModules.{u, w, u + 1} B S hS 𝒴 .fppf ⊓
          lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒴)).FullSubcategory
```

**`AlgebraicGeometry.Stack.ιOfLE_comp_sheafFlatBaseChangeDerivedPushforwardPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 176](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L176). The attribute's comment: “the left square of the diagram commutes (an equality of functors)”.

> **Stacks 07BC, the left square** of the diagram commutes: the inclusion
> `D⁺_{Parasitic ∩ LQCoh^fbc} ⊆ D⁺_{LQCoh^fbc}` followed by the middle arrow is the left arrow
> followed by the inclusion.

```lean
theorem ιOfLE_comp_sheafFlatBaseChangeDerivedPushforwardPlus :
    ObjectProperty.ιOfLE (derivedCategoryBInPlus_parasiticSheafFlatBaseChange_le B E h S hS 𝒳) ⋙
        sheafFlatBaseChangeDerivedPushforwardPlus B E h S hS f hqc hqs =
      parasiticSheafFlatBaseChangeDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
        ObjectProperty.ιOfLE
          (derivedCategoryBInPlus_parasiticSheafFlatBaseChange_le B E h S hS 𝒴)
```

**`AlgebraicGeometry.Stack.sheafFlatBaseChangeDerivedPushforwardPlusCompιIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L190). The attribute's comment: “the right square of the diagram, into the unbounded D(𝒪) with the unbounded Rf\_*, commutes up to the canonical isomorphism Rf\_*⁺ ⋙ ι ≅ ι ⋙ Rf\_*”.

> **Stacks 07BC, the right square** of the diagram commutes: the middle arrow followed by the
> inclusion `D⁺_{LQCoh^fbc}(𝒪_𝒴) ⊆ D(𝒪_𝒴)` is the inclusion `D⁺_{LQCoh^fbc}(𝒪_𝒳) ⊆ D(𝒪_𝒳)` followed
> by the unbounded `Rf_* : D(𝒪_𝒳) ⥤ D(𝒪_𝒴)`, up to the canonical isomorphism identifying the
> bounded below `Rf_*` with the restriction of the unbounded one.

```lean
def sheafFlatBaseChangeDerivedPushforwardPlusCompιIso :
    sheafFlatBaseChangeDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
        (DerivedCategoryB.derivedCategoryBInPlus
          (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒴)).ι ⋙ DerivedCategory.Plus.ι ≅
      (DerivedCategoryB.derivedCategoryBInPlus
          (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒳)).ι ⋙ DerivedCategory.Plus.ι ⋙ fppfDerivedPushforwardOfStacks B S hS f
```

**`AlgebraicGeometry.Stack.quasicoherentDerivedPushforwardPlus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L218). The attribute's comment: “the induced functor Rf\_(QCoh,*) : D⁺\_QCoh(𝒪\_𝒳) ⥤ D⁺\_QCoh(𝒪\_𝒴) on the quotient categories D⁺\_LQCoh^fbc / D⁺\_(Parasitic ∩ LQCoh^fbc)”.

> **Stacks 07BC, the induced functor** `Rf_{QCoh,*} : D⁺_QCoh(𝒪_𝒳) ⥤ D⁺_QCoh(𝒪_𝒴)` on the
> quotients `D⁺_QCoh = D⁺_{LQCoh^fbc} / D⁺_{Parasitic ∩ LQCoh^fbc}` of **Stacks 07B6**, for a
> quasi-compact quasi-separated `f`.

```lean
def quasicoherentDerivedPushforwardPlus :
    (DerivedCategoryB.serreQuotientWPlus
      (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒳)
      (parasiticModules.{u, w, u + 1} B S hS 𝒳 .fppf ⊓
        lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
          𝒳)).Localization ⥤
      (DerivedCategoryB.serreQuotientWPlus
        (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒴)
        (parasiticModules.{u, w, u + 1} B S hS 𝒴 .fppf ⊓
          lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒴)).Localization
```

**`AlgebraicGeometry.Stack.toSerreQuotient_comp_quasicoherentDerivedPushforwardPlus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L236). The attribute's comment: “Rf\_(QCoh,*) is the functor induced by Rf\_* on the quotient categories: the quotient square commutes (an equality of functors)”.

> **Stacks 07BC: `Rf_{QCoh,*}` is induced by `Rf_*`** — the quotient functor of `𝒳` followed by
> `Rf_{QCoh,*}` is the middle arrow followed by the quotient functor of `𝒴`.

```lean
theorem toSerreQuotient_comp_quasicoherentDerivedPushforwardPlus :
    (DerivedCategoryB.serreQuotientWPlus
        (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒳)
        (parasiticModules.{u, w, u + 1} B S hS 𝒳 .fppf ⊓
          lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒳)).Q ⋙
        quasicoherentDerivedPushforwardPlus B E h S hS f hqc hqs =
      sheafFlatBaseChangeDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
        (DerivedCategoryB.serreQuotientWPlus
          (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒴)
          (parasiticModules.{u, w, u + 1} B S hS 𝒴 .fppf ⊓
            lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
              𝒴)).Q
```

**`AlgebraicGeometry.Stack.quasicoherentDerivedPushforwardPlusCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L301). The attribute's comment: “the final assertion: the functors Rⁱf\_QCoh of Stacks 077A are Hⁱ ∘ Rf\_(QCoh,*) with Hⁱ of Stacks 07B7, as a natural isomorphism of functors QCoh(𝒪\_𝒳) ⥤ QCoh(𝒪\_𝒴) (𝓜 placed in degree zero)”.

> **Stacks 07BC, the final assertion: `Rⁱf_QCoh = Hⁱ ∘ Rf_{QCoh,*}`.** For a quasi-coherent
> `𝓜` on `𝒳`, placed in degree zero of `D⁺_QCoh(𝒪_𝒳)`, `Hⁱ(Rf_{QCoh,*}(𝓜[0])) ≅ Rⁱf_QCoh(𝓜)`,
> naturally in `𝓜`, with `Hⁱ` the cohomology functor of **Stacks 07B7** and `Rⁱf_QCoh` the functor
> of **Stacks 077A**.

```lean
def quasicoherentDerivedPushforwardPlusCohomologyIso (i : ℕ) :
    ObjectProperty.ιOfLE
          (isQuasicoherentOnSite_le_locallyQuasicoherentSheafFlatBaseChangeFppfModules_succ
            B E h S hS 𝒳) ⋙
        sheafFlatBaseChangeSingleFunctor B E h S hS 𝒳 ⋙
        (DerivedCategoryB.serreQuotientWPlus
          (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒳)
          (parasiticModules.{u, w, u + 1} B S hS 𝒳 .fppf ⊓
            lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
              𝒳)).Q ⋙
          quasicoherentDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
            plusQuasicoherentCohomology B E h S hS i ≅
      sheafFlatBaseChangeQuasicoherentHigherDirectImage B E h S hS f hqc hqs i
```

**`AlgebraicGeometry.Stack.toSerreQuotient_comp_quasicoherentDerivedPushforwardPlusCohomologyIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean, line 324](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Quasicoherent/QuasicoherentDerivedPushforward.lean#L324). The attribute's comment: “the final assertion on D⁺\_LQCoh^fbc(𝒪\_𝒳): Hⁱ ∘ Rf\_(QCoh,*) ∘ (quotient functor) ≅ Q ∘ Hⁱ ∘ Rf\_*, the identity the source reads off the definition of Hⁱ”.

> **Stacks 07BC, the final assertion on all of `D⁺_{LQCoh^fbc}(𝒪_𝒳)`**: `Hⁱ ∘ Rf_{QCoh,*}`
> composed with the quotient functor of `𝒳` is `Q ∘ Hⁱ ∘ Rf_*`, with `Hⁱ` the cohomology functor
> of **Stacks 07B7** and `Q` the coherator of **Stacks 0778**.

```lean
def toSerreQuotient_comp_quasicoherentDerivedPushforwardPlusCohomologyIso (i : ℤ) :
    (DerivedCategoryB.serreQuotientWPlus
        (lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS 𝒳)
        (parasiticModules.{u, w, u + 1} B S hS 𝒳 .fppf ⊓
          lqcohSheafFbcFppfModules.{u, w, u + 1} B E h S hS
            𝒳)).Q ⋙
        quasicoherentDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
          plusQuasicoherentCohomology B E h S hS i ≅
      sheafFlatBaseChangeDerivedPushforwardPlus B E h S hS f hqc hqs ⋙
        sheafFlatBaseChangeHomologyFunctor B E h S hS 𝒴 i ⋙
          coherator (isQuasicoherentOnSite_moduleLowerShriekSucc_moduleInverseImage
            (isQuasicoherentOnSite_moduleLowerShriekSucc B S hS 𝒴)
            (isQuasicoherentOnSite_moduleInverseImage_of_sheafFlatBaseChangeModulesSucc
              B E h S hS 𝒴))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 104.6, Tag 07BB](https://stacks.math.columbia.edu/tag/07BB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
