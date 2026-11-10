---
declaration: section
origin: cited
lean: CategoryTheory.Functor.isIso_iff_rightAcyclic_obj_injective, CategoryTheory.Functor.exists_spectralSequence_rightDerivedFunctorPlus_comp
statement: formalized
proof: formalized
---

# 13.22 Composition of right derived functors

Section 13.22 of the Stacks Project, [Tag 015L](https://stacks.math.columbia.edu/tag/015L). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 015M, a lemma

[Tag 015M](https://stacks.math.columbia.edu/tag/015M) in the Stacks Project.

**`CategoryTheory.Functor.isIso_iff_rightAcyclic_obj_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/CompositionOfRightDerivedFunctors.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/CompositionOfRightDerivedFunctors.lean#L205). References: SGA 4½ Etat 0 (4.3.1), “enough injectives”.

> Let `F : 𝒜 ⥤ ℬ` and `G : ℬ ⥤ 𝒞` be additive functors between abelian categories, with `𝒜`
> and `ℬ` having enough injectives. The canonical transformation `t : R(G ∘ F) ⟶ RG ∘ RF` of
> functors `D⁺(𝒜) ⥤ D⁺(𝒞)`, namely the unique one whose composite with the unit of `R(G ∘ F)` is
> the transformation `G(F(K)) ⟶ RG(F(K)) ⟶ RG(RF(K))` built from the units of `RG` and of `RF`
> (the hypothesis `ht`), is an isomorphism if and only if `F(I)` is right acyclic for `G` for every
> injective object `I` of `𝒜`.

```lean
public theorem isIso_iff_rightAcyclic_obj_injective (F : C ⥤ D) (G : D ⥤ E)
    [F.Additive] [G.Additive] [EnoughInjectives C] [EnoughInjectives D]
    (t : (F ⋙ G).rightDerivedFunctorPlus ⟶
      F.rightDerivedFunctorPlus ⋙ G.rightDerivedFunctorPlus)
    (ht : (F ⋙ G).rightDerivedFunctorPlusUnith ≫ whiskerLeft DerivedCategory.Plus.Qh t =
      whiskerRight (mapHomotopyCategoryPlusCompIso (Iso.refl (F ⋙ G))).inv
          DerivedCategory.Plus.Qh ≫
        whiskerLeft F.mapHomotopyCategoryPlus G.rightDerivedFunctorPlusUnith ≫
        whiskerRight F.rightDerivedFunctorPlusUnith G.rightDerivedFunctorPlus) :
    IsIso t ↔ ∀ I : C, Injective I → G.rightAcyclic (F.obj I)
```

## Tag 015N, a lemma

[Tag 015N](https://stacks.math.columbia.edu/tag/015N) in the Stacks Project.

**`CategoryTheory.Functor.exists_spectralSequence_rightDerivedFunctorPlus_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/SpectralSequence/Grothendieck.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/SpectralSequence/Grothendieck.lean#L72). References: SGA 4 V (0.3), “(ii) ⇒ (i)”; SGA 4 VII (1.5), “more general”; SGA 4½ Arcata (2.3.3), “more general”; SGA 4½ Arcata (2.3.4), “more general”.

> The Grothendieck spectral sequence. Let `F : 𝒜 ⥤ ℬ` and `G : ℬ ⥤ 𝒞` be additive functors
> between abelian categories, with `𝒜` and `ℬ` having enough injectives, such that `F(I)` is right
> acyclic for `G` for every injective object `I` of `𝒜`, and let `X` be an object of `D⁺(𝒜)`.
> There is a filtered complex `K` of `𝒞` with `H^n(K) ≅ H^n(R(G ∘ F)(X))` for all `n`, whose
> filtration is finite in each degree and whose spectral sequence `E`, presented by its pages
> `Z_r^{p,q}/D_r^{p,q}`, has `E_2^{p,q} ≅ R^pG(H^q(RF(X)))`, is bounded, induces a finite
> filtration on each `H^n(K)`, and converges to `H^*(K)`.

```lean
theorem exists_spectralSequence_rightDerivedFunctorPlus_comp (F : A ⥤ B) (G : B ⥤ C)
    [F.Additive] [G.Additive] [EnoughInjectives A] [EnoughInjectives B]
    (hFG : ∀ I : A, Injective I → G.rightAcyclic (F.obj I)) (X : DerivedCategory.Plus A) :
    ∃ K : FilteredObject (CochainComplex C ℤ) ℤᵒᵖ,
      (∀ n : ℤ, Nonempty (K.X.homology n ≅
        (DerivedCategory.Plus.homologyFunctor C n).obj
          ((F ⋙ G).rightDerivedFunctorPlus.obj X))) ∧
      K.filtration.IsDegreewiseFinite ∧
      ∀ (Fil : ∀ (_p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ p n : ℤ, Fil p n = Subobject.mk ((K.filtration.ι.app (op p)).f n))
        (Z : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, Z r p n =
          Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)))
        (D : ∀ (_r _p n : ℤ), Subobject (K.X.X n))
        (_ : ∀ r p n : ℤ, D r p n = Z (r - 1) (p + 1) n ⊔
          (Subobject.«exists» (K.X.d (n - 1) n)).obj (Z (r - 1) (p - r + 1) (n - 1)))
        (FH : ∀ (n _p : ℤ), Subobject (K.X.homology n))
        (_ : ∀ n p : ℤ, FH n p =
          imageSubobject (HomologicalComplex.homologyMap (K.filtration.ι.app (op p)) n)),
      ∃ (E : CohomologicalSpectralSequence C 0)
        (_ : ∀ (r p q n : ℤ) (hr : 0 ≤ r) (_ : n = p + q), (E.page r hr).X (p, q) ≅
          cokernel (Subobject.ofLE _ _ (inf_le_right : D r p n ⊓ Z r p n ≤ Z r p n))),
        (∀ p q : ℤ, Nonempty ((E.page 2 zero_le_two).X (p, q) ≅
          (G.rightDerivedPlus p).obj
            ((DerivedCategory.Plus.homologyFunctor B q).obj (F.rightDerivedFunctorPlus.obj X)))) ∧
        (∀ n : ℤ, {p : ℤ | ¬ IsZero ((E.page 0).X (p, n - p))}.Finite) ∧
        (∀ n : ℤ, ∃ a b : ℤ, a ≤ b ∧ FH n a = ⊤ ∧ FH n b = ⊥) ∧
        (∀ p q : ℤ, ∃ b : ℤ, ∀ (r : ℤ) (hr : 0 ≤ r), b ≤ r →
          (E.page r hr).d (p, q) (p + r, q - r + 1) = 0) ∧
        (∀ p n : ℤ,
          IsGLB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.pullback (K.X.d n (n + 1))).obj (Fil (p + r) (n + 1)) ⊔
                Fil (p + 1) n)
            (kernelSubobject (K.X.d n (n + 1)) ⊓ Fil p n ⊔ Fil (p + 1) n) ∧
          IsLUB (Set.range fun r : ℕ =>
              Fil p n ⊓ (Subobject.«exists» (K.X.d (n - 1) n)).obj (Fil (p - r) (n - 1)) ⊔
                Fil (p + 1) n)
            (imageSubobject (K.X.d (n - 1) n) ⊓ Fil p n ⊔ Fil (p + 1) n))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.22, Tag 015L](https://stacks.math.columbia.edu/tag/015L)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
