---
declaration: section
origin: cited
lean: Stacks.Cohomology.OlssonLaszloSituation, Stacks.Cohomology.OlssonLaszlo.truncGETower_presentation, Stacks.Cohomology.isIso_to_isDerivedLimit_truncGETower_of_derivedCategoryB, Stacks.Cohomology.isIso_cohomologyToEventuallyConstantValue, Stacks.Cohomology.OlssonLaszlo.derivedCategoryB_derivedPushforward_obj_of_ringedToposHom, Stacks.Cohomology.OlssonLaszlo.isIso_homology_derivedPushforward_truncGEπ_of_ringedToposHom, Stacks.Cohomology.OlssonLaszloPrimeSituation, Stacks.Cohomology.OlssonLaszlo.isIso_homology_derivedPushforward_truncGEπ_of_relativeSituation_general
statement: formalized
proof: formalized
---

# 21.25 Bounded cohomological dimension

Section 21.25 of the Stacks Project, [Tag 0D6Q](https://stacks.math.columbia.edu/tag/0D6Q). 6 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0D6R, a situation

[Tag 0D6R](https://stacks.math.columbia.edu/tag/0D6R) in the Stacks Project.

**`Stacks.Cohomology.OlssonLaszloSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/OlssonLaszloSituation.lean, line 99](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/OlssonLaszloSituation.lean#L99).

> **Stacks 0D6R.** The standing Olsson--Laszlo situation: a weak Serre subcategory of
> modules on a site, together with a locally covering class of objects admitting cofinal
> systems of coverings on whose members higher cohomology vanishes uniformly in the module.

```lean
structure OlssonLaszloSituation
```

## Tag 0D6S, a lemma

[Tag 0D6S](https://stacks.math.columbia.edu/tag/0D6S) in the Stacks Project.

**`Stacks.Cohomology.OlssonLaszlo.truncGETower_presentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/PushforwardBoundedCohomologicalDimension.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/PushforwardBoundedCohomologicalDimension.lean#L199). The attribute's comment: “the conclusion with the derived limit, its defining distinguished triangle and the canonical map of Remark 0H72 constructed: for `K` in `D_A(O)` (hK) the truncation tower has a product and a presented derived limit, and the canonical map to it is an isomorphism”.

> In the Olsson--Laszlo situation, the tower of truncations from below of an object of
> `D_A(O)` has a derived limit, presented by its defining distinguished triangle, and the
> canonical map from the object to that derived limit is an isomorphism.

```lean
theorem truncGETower_presentation
    (S : OlssonLaszloSituation.{v, u, wRing, wModule})
    (K : DerivedCategory (SheafOfModules.{wModule} S.O))
    (hK : DerivedCategoryB.derivedCategoryB S.A K) :
    ∃ (_hprod : HasProduct fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩)
      (L : DerivedCategory (SheafOfModules.{wModule} S.O))
      (c : K ⟶ L)
      (p : L ⟶ ∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩)
      (δ : (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩) ⟶
          L⟦(1 : ℤ)⟧),
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩) n -
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower
            (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩) (n + 1) ≫
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).map
          (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{wModule} S.O)) ∧
      (∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) K).obj ⟨n⟩) n =
        (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app K) ∧ IsIso c
```

**`Stacks.Cohomology.isIso_to_isDerivedLimit_truncGETower_of_derivedCategoryB`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceWeakSerre.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/TruncationConvergenceWeakSerre.lean#L115).

> **Stacks Project, Tag 0D6S.** In the Olsson--Laszlo situation, for an object `E` of the
> derived category whose cohomology sheaves all lie in the weak Serre subcategory `A`, the
> canonical map from `E` to a derived limit of its tower of truncations `τ_{≥ -n} E` from below is
> an isomorphism.

```lean
theorem isIso_to_isDerivedLimit_truncGETower_of_derivedCategoryB
    (S : OlssonLaszloSituation.{v, u, wRing, wModule})
    (E : DerivedCategory (SheafOfModules.{wModule} S.O))
    (hE : DerivedCategoryB.derivedCategoryB S.A E)
    (L : DerivedCategory (SheafOfModules.{wModule} S.O))
    (q : L ⟶ ∏ᶜ fun n : ℕ ↦
      (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) E).obj ⟨n⟩)
    (hL : ∃ δ :
      (∏ᶜ fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) E).obj ⟨n⟩) ⟶
          L⟦(1 : ℤ)⟧,
      Triangle.mk q (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦
          (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) E).obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦
            (Stacks.DerivedLimit.truncGETower
              (SheafOfModules.{wModule} S.O) E).obj ⟨n⟩) (n + 1) ≫
            (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) E).map
              (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{wModule} S.O)))
    (c : E ⟶ L)
    (hc : ∀ n : ℕ, c ≫ q ≫ Pi.π
      (fun n : ℕ ↦
        (Stacks.DerivedLimit.truncGETower (SheafOfModules.{wModule} S.O) E).obj ⟨n⟩) n =
      (DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app E) :
    IsIso c
```

## Tag 0D6T, a lemma

[Tag 0D6T](https://stacks.math.columbia.edu/tag/0D6T) in the Stacks Project.

**`Stacks.Cohomology.isIso_cohomologyToEventuallyConstantValue`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/EventuallyConstantDerivedLimit.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/EventuallyConstantDerivedLimit.lean#L229).

> **Stacks Project, Tag 0D6T.** If an inverse system in `D^+_A` has eventually
> constant cohomology sheaves with values `ℋʲ`, then the canonical map from the cohomology
> of any presented derived inverse limit to `ℋʲ` is an isomorphism, for every `j`.

```lean
theorem isIso_cohomologyToEventuallyConstantValue
    (S : OlssonLaszloSituation.{v, u, wRing, wModule})
    (K : ℕᵒᵖ ⥤ DerivedCategory (SheafOfModules.{wModule} S.O))
    (hK : ∀ n : ℕ, DerivedCategoryB.derivedCategoryBPlus S.A (K.obj ⟨n⟩))
    [HasProduct fun n : ℕ ↦ K.obj ⟨n⟩]
    (L : DerivedCategory (SheafOfModules.{wModule} S.O))
    (p : L ⟶ ∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩)
    (hL : ∃ δ : (∏ᶜ fun n : ℕ ↦ K.obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧,
      Triangle.mk p (Pi.lift fun n : ℕ ↦
        Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) n -
          Pi.π (fun n : ℕ ↦ K.obj ⟨n⟩) (n + 1) ≫
            K.map (homOfLE (Nat.le_succ n)).op) δ ∈
        distTriang (DerivedCategory (SheafOfModules.{wModule} S.O)))
    (ℋ : ℤ → SheafOfModules.{wModule} S.O)
    (e : ∀ j : ℤ, EventuallyConstantValue
      (K ⋙ DerivedCategory.homologyFunctor (SheafOfModules.{wModule} S.O) j) (ℋ j)) :
    ∀ j : ℤ, IsIso (cohomologyToEventuallyConstantValue S K L p j (ℋ j) (e j))
```

## Tag 0D6U, a lemma

[Tag 0D6U](https://stacks.math.columbia.edu/tag/0D6U) in the Stacks Project.

**`Stacks.Cohomology.OlssonLaszlo.derivedCategoryB_derivedPushforward_obj_of_ringedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ToposHomBoundedCohomologicalDimension.lean, line 125](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ToposHomBoundedCohomologicalDimension.lean#L125). The attribute's comment: “part (a)”.

> **Stacks Project, Tag 0D6U, part (a).** Let `f : (Sh(C), O) ⟶ (Sh(C'), O')` be a morphism
> of ringed topoi and let `A ⊂ Mod(O)`, `A' ⊂ Mod(O')` be weak Serre subcategories such that
> `C, O, A` and `C', O', A'` satisfy the assumption of the Olsson--Laszlo situation (Stacks 0D6R),
> `Rᵖf_*F` lies in `A'` for `p ≥ 0` and `F` in `A`, and `Rᵖf_*F = 0` for `p > N` and `F` in `A`.
> Then `Rf_*K` lies in `D_{A'}(O')` for every `K` in `D_A(O)`.

```lean
theorem derivedCategoryB_derivedPushforward_obj_of_ringedToposHom
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : DerivedCategoryB.derivedCategoryB A K) :
    DerivedCategoryB.derivedCategoryB A'
      ((Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := X) (Y := Y) f).obj K)
```

**`Stacks.Cohomology.OlssonLaszlo.isIso_homology_derivedPushforward_truncGEπ_of_ringedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ToposHomBoundedCohomologicalDimension.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/ToposHomBoundedCohomologicalDimension.lean#L148). The attribute's comment: “part (b)”.

> **Stacks Project, Tag 0D6U, part (b).** In the situation of part (a)
> (`derivedCategoryB_derivedPushforward_obj_of_ringedToposHom`), for every `K` in `D_A(O)` the
> canonical map `Hʲ(Rf_*K) ⟶ Hʲ(Rf_*(τ_{≥ -n}K))` induced by the truncation `K ⟶ τ_{≥ -n}K` is an
> isomorphism for every `j ≥ N - n`.

```lean
theorem isIso_homology_derivedPushforward_truncGEπ_of_ringedToposHom
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : DerivedCategoryB.derivedCategoryB A K)
    (n : ℕ) (j : ℤ) (hj : N - (n : ℤ) ≤ j) :
    IsIso ((DerivedCategory.homologyFunctor
      (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) j).map
      ((Stacks.Cohomology.DerivedPushforward.derivedPushforward (X := X) (Y := Y) f).map
        ((DerivedCategory.TStructure.t.truncGEπ (-(n : ℤ))).app K)))
```

## Tag 0D6V, a situation

[Tag 0D6V](https://stacks.math.columbia.edu/tag/0D6V) in the Stacks Project.

**`Stacks.Cohomology.OlssonLaszloPrimeSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/OlssonLaszloSituation.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/OlssonLaszloSituation.lean#L194).

> **Stacks 0D6V.** The relative Olsson--Laszlo situation for a morphism of ringed sites:
> the target has a locally covering collection of objects carrying cofinal systems of
> coverings on whose members the cohomology, on the source site, of the modules of the chosen
> weak Serre subcategory vanishes above an object-dependent integer bound.

```lean
public structure OlssonLaszloPrimeSituation
```

## Tag 0D6W, a lemma

[Tag 0D6W](https://stacks.math.columbia.edu/tag/0D6W) in the Stacks Project.

**`Stacks.Cohomology.OlssonLaszlo.isIso_homology_derivedPushforward_truncGEπ_of_relativeSituation_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/BoundedCohomologicalDimensionPushforwardGeneral.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedLimit/BoundedCohomologicalDimensionPushforwardGeneral.lean#L197). The attribute's comment: “for a morphism of ringed sites, with Rᵖf\_*F read as Hᵖ(Rf\_*(F[0])) and the identification Hʲ(V', Rf\_*K) = Hʲ(u(V'), K) taken from Stacks 0D6I”.

> **Stacks Project, Tag 0D6W.** Let `f : (C, O) ⟶ (C', O')` be a morphism of ringed sites, let
> `A ⊂ Mod(O)` be a weak Serre subcategory and let `N` be an integer such that
>
> * `C, O, A` satisfy the standing hypothesis of Stacks 0D6R: a class `B` of objects covering every
>   object of `C`, each `V ∈ B` carrying an integer bound `d_V` and a cofinal system of coverings of
>   `V` on whose members the cohomology of every module of `A` vanishes above `d_V`;
> * `f` and `A` satisfy the standing hypothesis of Stacks 0D6V: a class `B'` of objects covering
>   every object of `C'`, each `V' ∈ B'` carrying an integer bound `d_{V'}` and a cofinal system of
>   coverings of `V'` on the images under `f` of whose members the cohomology, computed on `C`, of
>   every module of `A` vanishes above `d_{V'}`;
> * `Rᵖf_*F = 0` for every `p > N` and every `F` of `A`.
>
> Then for every `K` of `D_A(O)` the canonical map `Hʲ(Rf_*K) ⟶ Hʲ(Rf_*(τ_{≥ -n}K))` induced by the
> truncation `K ⟶ τ_{≥ -n}K` is an isomorphism for every integer `n` and every `j ≥ N - n`.

```lean
theorem isIso_homology_derivedPushforward_truncGEπ_of_relativeSituation_general
    (K : DerivedCategory (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)))
    (hK : DerivedCategoryB.derivedCategoryB A K)
    (n : ℤ) (j : ℤ) (hj : N - n ≤ j) :
    IsIso ((DerivedCategory.homologyFunctor
        (SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) j).map
      ((derivedPushforward.{u} f.toRingedToposSiteHom).map
        ((DerivedCategory.TStructure.t.truncGEπ (-n)).app K)))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 21.25, Tag 0D6Q](https://stacks.math.columbia.edu/tag/0D6Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
