---
declaration: section
origin: cited
lean: Stacks.Cohomology.FilteredComplex.spectralSequence_of_filteredKInjectiveResolution, Stacks.Cohomology.FilteredComplex.exists_spectralSequence_of_filteredComplex, Stacks.Cohomology.FilteredComplex.exists_spectralSequence_of_boundedBelowFilteredComplex, Stacks.Cohomology.FilteredComplex.exists_canonicalTruncationSpectralSequence, Stacks.Cohomology.FilteredComplex.exists_boundedBelowTruncationSpectralSequence, Stacks.Cohomology.FilteredComplex.hypercohomologySpectralSequence, Stacks.Cohomology.FilteredComplex.hypercohomologySpectralSequence_e₂, Stacks.Cohomology.FilteredComplex.exists_boundedBelowHypercohomologySpectralSequence
statement: formalized
proof: formalized
---

# 20.29 Cohomology of filtered complexes

Section 20.29 of the Stacks Project, [Tag 0FLJ](https://stacks.math.columbia.edu/tag/0FLJ). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0BKK, a lemma

[Tag 0BKK](https://stacks.math.columbia.edu/tag/0BKK) in the Stacks Project.

**`Stacks.Cohomology.FilteredComplex.spectralSequence_of_filteredKInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/FilteredKInjectiveResolution.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/FilteredKInjectiveResolution.lean#L523). The attribute's comment: “computation by a supplied filtered K-injective resolution”.

> The spectral sequence of a filtered complex of module sheaves, computed by a supplied filtered
> K-injective resolution: its pages are presented by the cycle and boundary subobjects of the
> filtered complex of global sections, its first page is the hypercohomology of the graded pieces,
> and under the boundedness hypotheses it converges to the hypercohomology of the complex.

```lean
theorem spectralSequence_of_filteredKInjectiveResolution
    (hRΓ : RΓ.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)))
    (j : K ⟶ J)
    (hj : QuasiIso j.hom)
    (hjStep : ∀ p : ℤ, QuasiIso (j.natTrans.app (op p)))
    (hjGraded : ∀ p : ℤ, QuasiIso ((FilteredObject.gr p).map j))
    (hStepInjective : ∀ p n : ℤ, Injective ((J.filtration.obj (op p)).X n))
    (hKInjective : J.X.IsKInjective)
    (hStepKInjective : ∀ p : ℤ, (J.filtration.obj (op p)).IsKInjective)
    (hGradedKInjective : ∀ p : ℤ, ((FilteredObject.gr p).obj J).IsKInjective) :
    let E := CochainComplex.Filtered.spectralSequenceFunctor.obj
      (globalSectionsFilteredComplex X J)
    ∃ (F : ∀ (_p n : ℤ), Subobject ((globalSectionsFilteredComplex X J).X.X n))
        (Z D : ∀ (_r _p n : ℤ),
          Subobject ((globalSectionsFilteredComplex X J).X.X n)),
        (∀ p n : ℤ, F p n = Subobject.mk
          (((globalSectionsFilteredComplex X J).filtration.ι.app (op p)).f n)) ∧
        (∀ r p n : ℤ, Z r p n = F p n ⊓
          (Subobject.pullback ((globalSectionsFilteredComplex X J).X.d n (n + 1))).obj
            (F (p + r) (n + 1))) ∧
        (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» ((globalSectionsFilteredComplex X J).X.d (n - 1) n)).obj
            (Z (r - 1) (p - r + 1) (n - 1))) ∧
        (∃ e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q),
            (E.page r hr).X (p, q) ≅ cokernel
              (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)),
          ∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
            ∃ δ : (Z r p n : ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) ⟶
                (Z r (p + r) (n + 1) : ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))),
              δ ≫ (Z r (p + r) (n + 1)).arrow =
                  (Z r p n).arrow ≫ (globalSectionsFilteredComplex X J).X.d n (n + 1) ∧
              cokernel.π (Subobject.ofLE _ _
                  (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
                    (e r p q n hr hn).inv ≫
                    (E.page r hr).d (p, q) (p + r, q - r + 1) =
                δ ≫ cokernel.π (Subobject.ofLE _ _
                    (inf_le_right : D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤
                      Z r (p + r) (n + 1))) ≫
                  (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) ∧
        (∀ p q : ℤ, Nonempty
          ((E.page 1 (by omega)).X (p, q) ≅
            hypercohomology X RΓ ((FilteredObject.gr p).obj K) (p + q))) ∧
        ((∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
            IsZero (hypercohomology X RΓ (K.filtration.obj (op p)) n)) →
          (∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
            IsIso (hypercohomologyMap X RΓ (K.filtration.ι.app (op p)) n)) →
          (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
            ∃ (F : ∀ n : ℤ, ℤ → Subobject (hypercohomology X RΓ K.X n))
              (hF : ∀ n : ℤ, Antitone (F n)),
              (∀ n p : ℤ, F n p = imageSubobject
                (hypercohomologyMap X RΓ (K.filtration.ι.app (op p)) n)) ∧
              (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
              (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
              ∀ p q : ℤ, Nonempty
                (E.pageInfinity (p, q) ≅
                  cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
                    (hF (p + q) (by omega)))))
```

**`Stacks.Cohomology.FilteredComplex.exists_spectralSequence_of_filteredComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/FilteredKInjectiveResolution.lean, line 598](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/FilteredKInjectiveResolution.lean#L598).

> A filtered complex of modules on a ringed space has a cohomological spectral sequence whose
> first page is the hypercohomology of its graded pieces. If the hypercohomology of the filtration
> steps eventually vanishes on the right and maps isomorphically to that of the whole complex on the
> left, the spectral sequence is bounded and converges to the hypercohomology of the complex.

```lean
theorem exists_spectralSequence_of_filteredComplex :
    ∃ (RΓ : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
        DerivedCategory (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))))
      (α : homotopySections (structureSheafRing X) (⊤ : Opens X.carrier) ⟶ DerivedCategory.Qh ⋙ RΓ),
      RΓ.IsRightDerivedFunctor α
          (HomotopyCategory.quasiIso
            (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)) ∧
      ∃ (J : CochainComplex.Filtered (SheafOfModules.{u} (structureSheafRing X))) (j : K ⟶ J),
      QuasiIso j.hom ∧
      (∀ p : ℤ, QuasiIso (j.natTrans.app (op p))) ∧
      (∀ p : ℤ, QuasiIso ((FilteredObject.gr p).map j)) ∧
      (∀ n : ℤ, Injective (J.X.X n)) ∧
      (∀ p n : ℤ, Injective ((J.filtration.obj (op p)).X n)) ∧
      (∀ p n : ℤ, Injective (((FilteredObject.gr p).obj J).X n)) ∧
      ∃ (E : CohomologicalSpectralSequence
          (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) 0)
        (F : ∀ (_p n : ℤ), Subobject ((globalSectionsFilteredComplex X J).X.X n))
        (Z D : ∀ (_r _p n : ℤ),
          Subobject ((globalSectionsFilteredComplex X J).X.X n)),
        (∀ p n : ℤ, F p n = Subobject.mk
          (((globalSectionsFilteredComplex X J).filtration.ι.app (op p)).f n)) ∧
        (∀ r p n : ℤ, Z r p n = F p n ⊓
          (Subobject.pullback ((globalSectionsFilteredComplex X J).X.d n (n + 1))).obj
            (F (p + r) (n + 1))) ∧
        (∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» ((globalSectionsFilteredComplex X J).X.d (n - 1) n)).obj
            (Z (r - 1) (p - r + 1) (n - 1))) ∧
        (∃ e : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q),
            (E.page r hr).X (p, q) ≅ cokernel
              (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)),
          ∀ (r p q n : ℤ) (hr : 0 ≤ r) (hn : n = p + q),
            ∃ δ : (Z r p n : ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) ⟶
                (Z r (p + r) (n + 1) : ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))),
              δ ≫ (Z r (p + r) (n + 1)).arrow =
                  (Z r p n).arrow ≫ (globalSectionsFilteredComplex X J).X.d n (n + 1) ∧
              cokernel.π (Subobject.ofLE _ _
                  (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n)) ≫
                    (e r p q n hr hn).inv ≫
                    (E.page r hr).d (p, q) (p + r, q - r + 1) =
                δ ≫ cokernel.π (Subobject.ofLE _ _
                    (inf_le_right : D r (p + r) (n + 1) ⊓ Z r (p + r) (n + 1) ≤
                      Z r (p + r) (n + 1))) ≫
                  (e r (p + r) (q - r + 1) (n + 1) hr (by omega)).inv) ∧
        (∀ p q : ℤ, Nonempty
          ((E.page 1 (by omega)).X (p, q) ≅
            hypercohomology X RΓ ((FilteredObject.gr p).obj K) (p + q))) ∧
        ((∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
            IsZero (hypercohomology X RΓ (K.filtration.obj (op p)) n)) →
          (∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
            IsIso (hypercohomologyMap X RΓ (K.filtration.ι.app (op p)) n)) →
          (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
            ∃ (F : ∀ n : ℤ, ℤ → Subobject (hypercohomology X RΓ K.X n))
              (hF : ∀ n : ℤ, Antitone (F n)),
              (∀ n p : ℤ, F n p = imageSubobject
                (hypercohomologyMap X RΓ (K.filtration.ι.app (op p)) n)) ∧
              (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
              (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
              ∀ p q : ℤ, Nonempty
                (E.pageInfinity (p, q) ≅
                  cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
                    (hF (p + q) (by omega)))))
```

## Tag 0BKL, a remark

[Tag 0BKL](https://stacks.math.columbia.edu/tag/0BKL) in the Stacks Project.

**`Stacks.Cohomology.FilteredComplex.exists_spectralSequence_of_boundedBelowFilteredComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 800](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L800). References: EGA 0 (13.7.3), “ringed space, bdd below”.

> **Stacks 0BKL.** Let `(X, O_X)` be a ringed space and let `K^•` be a filtered complex of
> `O_X`-modules which is bounded below and whose filtration is finite in each degree. Then the
> spectral sequence of [Stacks, Tag 0BKK] can be built without a filtered K-injective resolution:
> a filtered quasi-isomorphism `i : K^• ⟶ I^•` as in [Stacks, Tag 05TW], with `I^•` bounded below,
> the filtration on each `I^n` finite and each `gr^pI^n` injective, gives the filtered complex
> `Γ(X, I^•)` with `F^pΓ(X, I^•) = Γ(X, F^pI^•)`, whose spectral sequence has first page
> `E_1^{p, q} = H^{p + q}(X, gr^pK^•)` and is bounded and converges to `H^*(X, K^•)` with a finite
> induced filtration.

```lean
theorem exists_spectralSequence_of_boundedBelowFilteredComplex (X : RingedSpace.{u, u})
    (RΓ : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))))
    (α : homotopySections (structureSheafRing X) (⊤ : Opens X.carrier) ⟶ DerivedCategory.Qh ⋙ RΓ)
    (hRΓ : RΓ.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)))
    (K : CochainComplex.Filtered (SheafOfModules.{u} (structureSheafRing X))) (a : ℤ)
    (hK : K.X.IsStrictlyGE a) (hKfin : K.filtration.IsDegreewiseFinite) :
    ∃ (I : CochainComplex.Filtered (SheafOfModules.{u} (structureSheafRing X))) (i : K ⟶ I),
      I.X.IsStrictlyGE a ∧
      I.filtration.IsDegreewiseFinite ∧
      (∀ n : ℤ, (CochainComplex.evalFil I n).IsFilteredInjective) ∧
      (∀ p : ℤ, QuasiIso ((FilteredObject.gr p).map i)) ∧
      (∀ p : ℤ, QuasiIso (i.natTrans.app (op p))) ∧
      QuasiIso i.hom ∧
      (∀ p : ℤᵒᵖ, (globalSectionsFilteredComplex X I).filtration.obj p =
        (globalSectionsComplexFunctor X).obj (I.filtration.obj p)) ∧
      (∀ p q : ℤ, Nonempty
        (((globalSectionsSpectralSequence X I).page 1 (by omega)).X (p, q) ≅
          hypercohomology X RΓ ((FilteredObject.gr p).obj K) (p + q))) ∧
      (∀ n : ℤ, {p : ℤ | ¬ IsZero
        (((globalSectionsSpectralSequence X I).page 1 (by omega)).X (p, n - p))}.Finite) ∧
      ∃ (F : ∀ n : ℤ, ℤ → Subobject (hypercohomology X RΓ K.X n))
        (hF : ∀ n : ℤ, Antitone (F n)),
        (∀ n p : ℤ, F n p = imageSubobject
          (hypercohomologyMap X RΓ (K.filtration.ι.app (op p)) n)) ∧
        (∀ n : ℤ, ∃ b c : ℤ, b ≤ c ∧ F n b = ⊤ ∧ F n c = ⊥) ∧
        (∀ p q : ℤ, (globalSectionsSpectralSequence X I).HasPageInfinityAt (p, q)) ∧
        ∀ p q : ℤ, Nonempty
          ((globalSectionsSpectralSequence X I).pageInfinity (p, q) ≅
            cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
              (hF (p + q) (by omega))))
```

## Tag 0BKM, an example

[Tag 0BKM](https://stacks.math.columbia.edu/tag/0BKM) in the Stacks Project.

**`Stacks.Cohomology.FilteredComplex.exists_canonicalTruncationSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L210). The attribute's comment: “truncation\_e1\_page”.

> **Stacks 0BKM.** For every complex of modules on a ringed space, the canonical truncation
> filtration gives a spectral sequence with
> `E_1^{p, q} = H^{p + q}(X, H^{-p}(K^•)[p]) = H^{2p + q}(X, H^{-p}(K^•))`.

```lean
theorem exists_canonicalTruncationSpectralSequence (X : RingedSpace.{u, u})
    (K : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ) :
    Nonempty (CanonicalTruncationSpectralSequence X K)
```

**`Stacks.Cohomology.FilteredComplex.exists_boundedBelowTruncationSpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L877). The attribute's comment: “truncation\_e1\_page”. References: EGA 0 (11.4.3), “''E₂, T = RΓ”; EGA 0 (12.4.1), “''E2, absolute case”.

> **Stacks 0BKM, through Remark 0BKL.** For a bounded-below complex the canonical truncation
> spectral sequence can also be built from a bounded-below filtered replacement whose filtration is
> finite in every degree and whose graded terms are injective; the first-page formula is the
> same.

```lean
theorem exists_boundedBelowTruncationSpectralSequence (X : RingedSpace.{u, u})
    (K : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (hK : ∃ a : ℤ, K.IsStrictlyGE a) :
    ∃ (S : CanonicalTruncationSpectralSequence X K) (a : ℤ),
      S.injectiveReplacement.X.IsStrictlyGE a ∧
      S.injectiveReplacement.filtration.IsDegreewiseFinite ∧
      ∀ p q : ℤ, Nonempty
        (((globalSectionsSpectralSequence X S.injectiveReplacement).page 1
            (by omega)).X (p, q) ≅
          (DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) (2 * p + q)).obj
              (S.RΓ.obj ((DerivedCategory.singleFunctor
                (SheafOfModules.{u} (structureSheafRing X)) 0).obj
                  ((DerivedCategory.homologyFunctor
                    (SheafOfModules.{u} (structureSheafRing X)) (-p)).obj
                      (DerivedCategory.Q.obj K)))))
```

**`Stacks.Cohomology.FilteredComplex.hypercohomologySpectralSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 958](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L958). The attribute's comment: “hypercohomology\_e2\_page”.

> **Stacks 0BKM.** The hypercohomology spectral sequence of an object of the derived category
> of module sheaves on a ringed space: take a representative, filter it by its canonical
> truncations, apply derived global sections, and renumber the resulting spectral sequence.

```lean
def hypercohomologySpectralSequence (X : RingedSpace.{u, u})
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) :
    HypercohomologySpectralSequence X K
```

**`Stacks.Cohomology.FilteredComplex.hypercohomologySpectralSequence_e₂`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 968](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L968). The attribute's comment: “hypercohomology\_e2\_page”.

> **Stacks 0BKM.** The second page of the hypercohomology spectral sequence is the
> hypercohomology of the cohomology objects of `K`: `E_2^{i, j} = H^i(X, H^j(K))`.

```lean
theorem hypercohomologySpectralSequence_e₂ (X : RingedSpace.{u, u})
    (K : DerivedCategory (SheafOfModules.{u} (structureSheafRing X))) (i j : ℤ) :
    Nonempty (((hypercohomologySpectralSequence X K).spectralSequence.page 2).X (i, j) ≅
      (DerivedCategory.homologyFunctor
          (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) i).obj
        ((hypercohomologySpectralSequence X K).truncation.RΓ.obj
          ((DerivedCategory.singleFunctor (SheafOfModules.{u} (structureSheafRing X)) 0).obj
            ((DerivedCategory.homologyFunctor
              (SheafOfModules.{u} (structureSheafRing X)) j).obj K))))
```

**`Stacks.Cohomology.FilteredComplex.exists_boundedBelowHypercohomologySpectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean, line 1009](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HypercohomologySpectralSequence.lean#L1009). The attribute's comment: “bounded below: the renumbered sequence is bounded and converges to H^\{i+j}(X, K)”. References: EGA 0 (11.4.3), “T = RΓ, bounded below”; EGA III (6.2.1), “absolute case, Y=point”; EGA 0 (12.4.1), “abutment, absolute case”.

> **Stacks 0BKM, the closing clause.**  If `K^•` is bounded below, the renumbered spectral
> sequence -- the one whose second page is `H^i(X, H^j(K^•))` -- is **bounded**, and it **converges
> to `H^{i + j}(X, K^•)`**: some finite decreasing filtration of `H^n(X, K^•)` has the terms
> `E_∞^{i, n - i}` of its infinity page as graded pieces.
>
> The spectral sequence is the one of
> `exists_boundedBelowTruncationSpectralSequence`, i.e. the one built through Remark
> [Stacks, Tag 0BKL] from a bounded-below filtered replacement; boundedness and convergence of that
> sequence *before* the renumbering are `boundedReplacement_convergence`, which needs no hypothesis
> beyond degreewise finiteness of the replacement's filtration, and they are carried across the
> bidegree change `(i, j) ↦ (-j, i + 2j)` by
> `CategoryTheory.SpectralSequence.truncationRenumber_finite_not_isZero_page_two` and
> `CategoryTheory.SpectralSequence.AbutsTo.truncationRenumberRestrictPages`.  The abutment is read
> on `K^•` itself rather than on the underlying complex of the filtration by
> `CategoryTheory.SpectralSequence.AbutsTo.of_iso`.

```lean
theorem exists_boundedBelowHypercohomologySpectralSequence (X : RingedSpace.{u, u})
    (K : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (hK : ∃ a : ℤ, K.IsStrictlyGE a) :
    ∃ S : HypercohomologySpectralSequence X (DerivedCategory.Q.obj K),
      IsBounded S.spectralSequence ∧
        SpectralSequence.AbutsTo S.spectralSequence
          (fun n => hypercohomology X S.truncation.RΓ K n)
```

## Tag 0FLK, an example

[Tag 0FLK](https://stacks.math.columbia.edu/tag/0FLK) in the Stacks Project.

**`Stacks.Cohomology.FilteredComplex.exists_filteredKInjectiveResolution_stupidTruncation_iso_cartanEilenbergFirst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/CartanEilenbergComparison.lean, line 326](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/CartanEilenbergComparison.lean#L326). The attribute's comment: “bounded below: the 0BKK spectral sequence of a filtered K-injective resolution of (F, σ\_\{≥p}F) built via Remark 0BKL has E\_1^\{p, q} = H^\{p + q}(X, F^p[-p]) = H^q(X, F^p), is bounded, converges to H^\{p + q}(X, F), and is isomorphic to the first spectral sequence (Tag 015J) of every Cartan-Eilenberg resolution of F”.

> **Stacks 0FLK, the bounded below case.** Let `F^•` be a bounded below complex of
> `O_X`-modules. Then
>
> 1. the spectral sequence of [Stacks, Tag 0BKK] for the brutal truncation filtration
>    `σ_{≥ p}F^•` can be constructed through Remark [Stacks, Tag 0BKL]: there is a filtered
>    K-injective resolution `R` of `σ_{≥ •}F^•` which is bounded below, has a filtration finite in
>    every degree and is filtered injective in every degree;
> 2. its spectral sequence `R.spectralSequence` (the 0BKK spectral sequence) has
>    `E_1^{p, q} = H^{p + q}(X, F^p[-p]) = H^q(X, F^p)`, is bounded and converges to
>    `H^{i + j}(X, F^•)`;
> 3. it is isomorphic to the first spectral sequence of [Stacks, Tag 015J] of every
>    Cartan-Eilenberg resolution of `F^•`.
>
> Clause 2 holds for every filtered K-injective resolution of `σ_{≥ •}F^•`, by
> `stupidTruncation_filteredKInjectiveResolution_spectralSequence`, and is restated here for the
> resolution of clause 1.

```lean
theorem exists_filteredKInjectiveResolution_stupidTruncation_iso_cartanEilenbergFirst
    (F : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ) (a : ℤ)
    (hF : F.IsStrictlyGE a)
    (RΓ : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))))
    (α : Stacks.Cohomology.HypercohomologyEdge.HomologyComparison.homotopySections
      (structureSheafRing X) (⊤ : Opens X.carrier) ⟶ DerivedCategory.Qh ⋙ RΓ)
    (hRΓ : RΓ.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ))) :
    ∃ R : FilteredKInjectiveResolution X (CochainComplex.stupidTruncationFiltration F),
      R.obj.X.IsStrictlyGE a ∧ R.obj.filtration.IsDegreewiseFinite ∧
      (∀ n : ℤ, (CochainComplex.evalFil R.obj n).IsFilteredInjective) ∧
      (∀ p q : ℤ, Nonempty ((R.spectralSequence.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) (p + q)).obj
          (RΓ.obj (((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X)) 0).obj (F.X p))⟦(-p : ℤ)⟧)))) ∧
      (∀ p q : ℤ, Nonempty ((R.spectralSequence.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) q).obj
          (RΓ.obj ((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X)) 0).obj (F.X p))))) ∧
      IsBounded R.spectralSequence ∧
      SpectralSequence.AbutsTo R.spectralSequence (fun n => hypercohomology X RΓ F n) ∧
      ∀ I : F.CartanEilenbergResolution,
        Nonempty (R.spectralSequence ≅ cartanEilenbergFirstSpectralSequence X I)
```

**`Stacks.Cohomology.FilteredComplex.stupidTruncation_filteredKInjectiveResolution_spectralSequence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/StupidTruncationSpectralSequence.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/StupidTruncationSpectralSequence.lean#L353). The attribute's comment: “for the spectral sequence of 0BKK computed by any filtered K-injective resolution of (F, σ\_\{≥p}F): existence of the resolution, E\_1^\{p, q} = H^\{p + q}(X, F^p[-p]) = H^q(X, F^p), and, for F bounded below, boundedness and convergence to H^\{p + q}(X, F). The construction via Remark 0BKL and the comparison with Tag 015J are exists\_filteredKInjectiveResolution\_stupidTruncation\_iso\_cartanEilenbergFirst”.

> **Stacks 0FLK.** Let `F^•` be a complex of `O_X`-modules on a ringed space `X`, filtered by
> its brutal truncations `F^pF^• = σ_{≥ p}F^•`. This filtered complex has a filtered K-injective
> resolution, and for *every* filtered K-injective resolution `R` of it the spectral sequence of
> [Stacks, Tag 0BKK] it computes (`R.spectralSequence`) has
> `E_1^{p, q} = H^{p + q}(X, F^p[-p]) = H^q(X, F^p)`, the cohomology being taken with respect to any
> right-derived global-sections functor `RΓ`. If `F^•` is bounded below, this spectral sequence is
> bounded and converges to `H^{i + j}(X, F^•)`.
>
> The remaining bounded below assertions of the tag, that the sequence can be built through Remark
> [Stacks, Tag 0BKL] and that it is the first spectral sequence of [Stacks, Tag 015J], are
> `exists_filteredKInjectiveResolution_stupidTruncation_iso_cartanEilenbergFirst`.

```lean
theorem stupidTruncation_filteredKInjectiveResolution_spectralSequence (X : RingedSpace.{u, u})
    (F : CochainComplex (SheafOfModules.{u} (structureSheafRing X)) ℤ)
    (RΓ : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))))
    (α : homotopySections (structureSheafRing X) (⊤ : Opens X.carrier) ⟶ DerivedCategory.Qh ⋙ RΓ)
    (hRΓ : RΓ.IsRightDerivedFunctor α
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ))) :
    Nonempty (FilteredKInjectiveResolution X (CochainComplex.stupidTruncationFiltration F)) ∧
    ∀ R : FilteredKInjectiveResolution X (CochainComplex.stupidTruncationFiltration F),
      (∀ p q : ℤ, Nonempty ((R.spectralSequence.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) (p + q)).obj
          (RΓ.obj (((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X)) 0).obj (F.X p))⟦(-p : ℤ)⟧)))) ∧
      (∀ p q : ℤ, Nonempty ((R.spectralSequence.page 1 (by omega)).X (p, q) ≅
        (DerivedCategory.homologyFunctor
            (ModuleCat.{u} ((structureSheafRing X).obj.obj (op ⊤))) q).obj
          (RΓ.obj ((DerivedCategory.singleFunctor
            (SheafOfModules.{u} (structureSheafRing X)) 0).obj (F.X p))))) ∧
      ∀ a : ℤ, F.IsStrictlyGE a →
        IsBounded R.spectralSequence ∧
        SpectralSequence.AbutsTo R.spectralSequence (fun n => hypercohomology X RΓ F n)
```

## Tag 0FLL, a lemma

[Tag 0FLL](https://stacks.math.columbia.edu/tag/0FLL) in the Stacks Project.

**`Stacks.Cohomology.FilteredComplex.relativeSpectralSequence_of_filteredKInjectiveResolution`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HigherDirectImageSpectralSequence.lean, line 552](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HigherDirectImageSpectralSequence.lean#L552). The attribute's comment: “computation by a supplied filtered K-injective resolution”.

> **Stacks 0FLL**, the first page and the conditional bounded convergence, for a supplied
> filtered K-injective resolution. The right-derived pushforward, its unit and the resolution are
> fixed inputs, so all of the conclusions concern these same data.

```lean
theorem relativeSpectralSequence_of_filteredKInjectiveResolution
    (hRf : Rf.IsRightDerivedFunctor η
      (HomotopyCategory.quasiIso (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)))
    (j : K ⟶ J)
    (hj : QuasiIso j.hom)
    (hjStep : ∀ p : ℤ, QuasiIso (j.natTrans.app (op p)))
    (hjGraded : ∀ p : ℤ, QuasiIso ((FilteredObject.gr p).map j))
    (hStepInjective : ∀ p n : ℤ, Injective ((J.filtration.obj (op p)).X n))
    (hKInjective : J.X.IsKInjective)
    (hStepKInjective : ∀ p : ℤ, (J.filtration.obj (op p)).IsKInjective)
    (hGradedKInjective : ∀ p : ℤ, ((FilteredObject.gr p).obj J).IsKInjective) :
    let E := pushforwardSpectralSequence f J
    (∀ p q : ℤ, Nonempty
      ((E.page 1 (by omega)).X (p, q) ≅
        higherDirectImage (X := X) (Y := Y) Rf ((FilteredObject.gr p).obj K) (p + q))) ∧
      ((∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
          IsZero (higherDirectImage Rf (K.filtration.obj (op p)) n)) →
        (∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
          IsIso (higherDirectImageMap Rf (K.filtration.ι.app (op p)) n)) →
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 1 (by omega)).X (p, n - p))}.Finite) ∧
          ∃ (F : ∀ n : ℤ, ℤ → Subobject (higherDirectImage Rf K.X n))
            (hF : ∀ n : ℤ, Antitone (F n)),
            (∀ n p : ℤ, F n p = imageSubobject
              (higherDirectImageMap Rf (K.filtration.ι.app (op p)) n)) ∧
            (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
            (∀ p q : ℤ, E.HasPageInfinityAt (p, q)) ∧
            ∀ p q : ℤ, Nonempty
              (E.pageInfinity (p, q) ≅
                cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
                  (hF (p + q) (by omega)))))
```

**`Stacks.Cohomology.FilteredComplex.exists_relativeSpectralSequence_of_filteredComplex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HigherDirectImageSpectralSequence.lean, line 594](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Cohomology/FilteredComplexSpectralSequence/HigherDirectImageSpectralSequence.lean#L594).

> **Stacks 0FLL.** A filtered complex of `O_X`-modules has a canonical cohomological spectral
> sequence of `O_Y`-modules, with `d_r` of bidegree `(r, -r + 1)`, whose first page is
> `E_1^{p, q} = R^{p + q}f_*gr^pF^•`. If for every `n` the higher direct image
> `R^nf_*F^pF^•` vanishes for `p ≫ 0` and maps isomorphically to `R^nf_*F^•` for `p ≪ 0`, the
> spectral sequence is bounded and converges to `R^*f_*F^•`.

```lean
theorem exists_relativeSpectralSequence_of_filteredComplex :
    ∃ (Rf : DerivedCategory (SheafOfModules.{u} (structureSheafRing X)) ⥤
        DerivedCategory (SheafOfModules.{u} (structureSheafRing Y)))
      (η : homotopyPushforward f ⟶ DerivedCategory.Qh ⋙ Rf),
      Rf.IsRightDerivedFunctor η
          (HomotopyCategory.quasiIso
            (SheafOfModules.{u} (structureSheafRing X)) (ComplexShape.up ℤ)) ∧
      ∃ (J : CochainComplex.Filtered (SheafOfModules.{u} (structureSheafRing X))) (j : K ⟶ J),
      QuasiIso j.hom ∧
      (∀ p : ℤ, QuasiIso (j.natTrans.app (op p))) ∧
      (∀ p : ℤ, QuasiIso ((FilteredObject.gr p).map j)) ∧
      (∀ n : ℤ, Injective (J.X.X n)) ∧
      (∀ p n : ℤ, Injective ((J.filtration.obj (op p)).X n)) ∧
      (∀ p n : ℤ, Injective (((FilteredObject.gr p).obj J).X n)) ∧
      (∀ p q : ℤ, Nonempty
        (((pushforwardSpectralSequence f J).page 1 (by omega)).X (p, q) ≅
          higherDirectImage (X := X) (Y := Y) Rf ((FilteredObject.gr p).obj K) (p + q))) ∧
      ((∀ n : ℤ, ∃ p₀ : ℤ, ∀ p : ℤ, p₀ ≤ p →
          IsZero (higherDirectImage Rf (K.filtration.obj (op p)) n)) →
        (∀ n : ℤ, ∃ p₁ : ℤ, ∀ p : ℤ, p ≤ p₁ →
          IsIso (higherDirectImageMap Rf (K.filtration.ι.app (op p)) n)) →
        (∀ n : ℤ, {p : ℤ | ¬ IsZero
          (((pushforwardSpectralSequence f J).page 1 (by omega)).X (p, n - p))}.Finite) ∧
          ∃ (F : ∀ n : ℤ, ℤ → Subobject (higherDirectImage Rf K.X n))
            (hF : ∀ n : ℤ, Antitone (F n)),
            (∀ n p : ℤ, F n p = imageSubobject
              (higherDirectImageMap Rf (K.filtration.ι.app (op p)) n)) ∧
            (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ F n a = ⊤ ∧ F n b = ⊥) ∧
            (∀ p q : ℤ, (pushforwardSpectralSequence f J).HasPageInfinityAt (p, q)) ∧
            ∀ p q : ℤ, Nonempty
              ((pushforwardSpectralSequence f J).pageInfinity (p, q) ≅
                cokernel (Subobject.ofLE (F (p + q) (p + 1)) (F (p + q) p)
                  (hF (p + q) (by omega)))))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.29, Tag 0FLJ](https://stacks.math.columbia.edu/tag/0FLJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
