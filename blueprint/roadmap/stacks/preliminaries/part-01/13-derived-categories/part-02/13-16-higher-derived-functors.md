---
declaration: section
origin: cited
lean: CategoryTheory.Functor.isGE_and_isIso_homologyFunctor_map_of_isRightDerivedValueAt, CategoryTheory.Functor.rightDerivedOfIsRightDerivable, CategoryTheory.Functor.isZero_and_preservesFiniteLimits_and_isIso_iff_of_isRightDerivable, CategoryTheory.Functor.rightAcyclic_iff_isIso_and_isZero_totalRightDerivedPlusHomology, CategoryTheory.Functor.rightAcyclic_and_shortExact_map_of_shortExact_of_isRightDerivable, CategoryTheory.Functor.isDeltaFunctor_and_isUniversal_of_isRightDerivable, CategoryTheory.Functor.isIso_ι_app_of_computesRightDerived_single_of_isRightDerivedValueAt, CategoryTheory.Functor.hasDerivedFunctors_of_enough_acyclic_objects
statement: formalized
proof: formalized
---

# 13.16 Higher derived functors

Section 13.16 of the Stacks Project, [Tag 05TB](https://stacks.math.columbia.edu/tag/05TB). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05TC, a lemma

[Tag 05TC](https://stacks.math.columbia.edu/tag/05TC) in the Stacks Project.

**`CategoryTheory.Functor.isGE_and_isIso_homologyFunctor_map_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/DeltaFunctor.lean, line 940](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/DeltaFunctor.lean#L940).

> **Right derived functors move to the right**, [StackProject 05TC].
> Let `F : A ⥤ B` be an additive functor between abelian categories, let `K` be a cochain complex
> of objects of `A`, let `a : ℤ`, and let `RF` be the right derived functor of
> `K(A) ⥤ K(B) ⥤ D(B)` with respect to the quasi-isomorphisms. Assume `RF` is defined at `K`,
> with value `RF(K) = c.pt` (Stacks 05S9: the ind-object `(s : K ⟶ L) ↦ F(L)` of `D(B)` is
> essentially constant with value `c.pt`).
> 1. If `H^i(K) = 0` for all `i < a`, then `H^i(RF(K)) = 0` for all `i < a`.
> 2. If moreover `RF` is defined at `τ_{≤ a}K`, with value `RF(τ_{≤ a}K) = d.pt`, then there is a
>    unique morphism `φ : RF(τ_{≤ a}K) ⟶ RF(K)` compatible with the coprojections of the two
>    values along the canonical monomorphism `K.ιTruncLE a : τ_{≤ a}K ⟶ K` — that is, with
>    `d.ι.app s ≫ φ = F(g) ≫ c.ι.app t` for every pair of indices `s`, `t` and every
>    `g : s.right ⟶ t.right` with `ιTruncLE ≫ t.hom = s.hom ≫ g`, the morphism `RF(ιTruncLE)`
>    of Stacks 05SA — and `H^i(φ)` is an isomorphism for all `i ≤ a`.

```lean
public theorem isGE_and_isIso_homologyFunctor_map_of_isRightDerivedValueAt
    {A B : Type*} [Category* A] [Category* B] [Abelian A] [Abelian B]
    [HasDerivedCategory B] (F : A ⥤ B) [F.Additive]
    (K : CochainComplex A ℤ) (a : ℤ)
    (c : Cocone (MorphismProperty.Under.forget (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))
        ⊤ ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K) ⋙
      Under.forget ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K) ⋙
      F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh))
    (hc : (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
      (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))
      ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K) c) :
    (K.IsGE a → c.pt.IsGE a) ∧
    ∀ (d : Cocone (MorphismProperty.Under.forget
          (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ⊤
          ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj (K.truncLE a)) ⋙
        Under.forget ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj (K.truncLE a)) ⋙
        F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh)),
      (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).IsRightDerivedValueAt
        (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))
        ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj (K.truncLE a)) d →
      ∃ φ : d.pt ⟶ c.pt,
        (∀ ψ : d.pt ⟶ c.pt,
          (∀ (s : (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).Under ⊤
                ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj (K.truncLE a)))
             (t : (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).Under ⊤
                ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K))
             (g : s.right ⟶ t.right),
            (HomotopyCategory.quotient A (ComplexShape.up ℤ)).map (K.ιTruncLE a) ≫ t.hom =
                s.hom ≫ g →
              d.ι.app s ≫ ψ =
                (F.mapHomotopyCategory (ComplexShape.up ℤ) ⋙ DerivedCategory.Qh).map g ≫
                  c.ι.app t) ↔ ψ = φ) ∧
        ∀ i ≤ a, IsIso ((DerivedCategory.homologyFunctor B i).map φ)
```

## Tag 015A, a definition

[Tag 015A](https://stacks.math.columbia.edu/tag/015A) in the Stacks Project.

**`CategoryTheory.Functor.rightDerivedOfIsRightDerivable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/EverywhereDefined.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/EverywhereDefined.lean#L110).

> **Stacks 015A.** The `i`-th right derived functor `R ⁱ F = H ⁱ ∘ RF : 𝒜 ⥤ ℬ` of an additive
> functor `F : 𝒜 ⥤ ℬ` between abelian categories, assuming that `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is everywhere
> defined (`h`). Here `RF` is `CategoryTheory.Functor.rightDerivedFunctorPlusOfIsRightDerivable`,
> an object `A` of `𝒜` is sent to the complex `A[0]` concentrated in degree `0`, and `H ⁱ` is the
> `i`-th cohomology functor `D⁺(ℬ) ⥤ ℬ`.

```lean
noncomputable def rightDerivedOfIsRightDerivable
    (h : (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).IsRightDerivable
      (HomotopyCategory.Plus.quasiIso C)) (i : ℤ) : C ⥤ D
```

## Tag 05TD, a lemma

[Tag 05TD](https://stacks.math.columbia.edu/tag/05TD) in the Stacks Project.

**`CategoryTheory.Functor.isZero_and_preservesFiniteLimits_and_isIso_iff_of_isRightDerivable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedPlusEverywhereDefined.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedPlusEverywhereDefined.lean#L404).

> **Right deriving is for left exact functors**, [Stacks, Tag 05TD].
> Let `F : 𝒜 ⥤ ℬ` be an additive functor between abelian categories and assume that the right
> derived functor `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is everywhere defined: for every bounded below complex `K`
> the ind-object `(s : K ⟶ L) ↦ F(L)` over the quasi-isomorphisms `s` out of `K` is essentially
> constant ([Stacks, Tag 05SV]). Let `RF`, with unit `α`, be the right derived functor, so that
> `R ⁱ F = H ⁱ ∘ RF ∘ (·[0])`. Then
> 1. `R ⁱ F = 0` for `i < 0`,
> 2. `R ⁰ F` is left exact, and
> 3. the canonical map `F ⟶ R ⁰ F`, that is `H ⁰(α)` at the complexes `X[0]`, is an
>    isomorphism if and only if `F` is left exact.

```lean
public theorem isZero_and_preservesFiniteLimits_and_isIso_iff_of_isRightDerivable
    {A B : Type*} [Category* A] [Category* B] [Abelian A] [Abelian B]
    [HasDerivedCategory A] [HasDerivedCategory B] (F : A ⥤ B) [F.Additive]
    (hF : (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).IsRightDerivable
      (HomotopyCategory.Plus.quasiIso A))
    (RF : DerivedCategory.Plus A ⥤ DerivedCategory.Plus B)
    (α : F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶
      DerivedCategory.Plus.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α (HomotopyCategory.Plus.quasiIso A)] :
    (∀ i < 0, IsZero (DerivedCategory.Plus.singleFunctor A 0 ⋙ RF ⋙
        DerivedCategory.Plus.homologyFunctor B i)) ∧
      PreservesFiniteLimits (DerivedCategory.Plus.singleFunctor A 0 ⋙ RF ⋙
        DerivedCategory.Plus.homologyFunctor B 0) ∧
      ((∀ X : A, IsIso ((DerivedCategory.Plus.homologyFunctor B 0).map
          (α.app ((HomotopyCategory.Plus.singleFunctor A 0).obj X)))) ↔
        PreservesFiniteLimits F)
```

## Tag 015C, a lemma

[Tag 015C](https://stacks.math.columbia.edu/tag/015C) in the Stacks Project.

**`CategoryTheory.Functor.rightAcyclic_iff_isIso_and_isZero_totalRightDerivedPlusHomology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightAcyclicEverywhereDefined.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightAcyclicEverywhereDefined.lean#L387). The attribute's comment: “`RF` everywhere defined is `Functor.IsRightDerivable` of `K⁺(F) ⋙ Q⁺` (Tag 05SV); `R ⁱ F` is `Functor.totalRightDerivedPlusHomology`, and `F(A) ⟶ R ⁰ F(A)` is `H ⁰` of the unit of `RF` at `A[0]`”.

> **Characterization of right acyclic objects**, [StacksProject 015C].
> Let `F : 𝒜 ⥤ ℬ` be an additive functor between abelian categories and assume that
> `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is everywhere defined, that is, `K⁺(F) ⋙ Q⁺` is right derivable with
> respect to the quasi-isomorphisms of `K⁺(𝒜)` ([Stacks, Tag 05SV]); `RF` is its right derived
> functor, with unit `α`, and `R ⁱ F = H ⁱ ∘ RF ∘ (·[0])`. Let `A` be an object of `𝒜`. Then
> 1. `A` is right acyclic for `F` if and only if the canonical map `F(A) ⟶ R ⁰ F(A)`, that is
>    `H ⁰(α)` at `A[0]`, is an isomorphism and `R ⁱ F(A) = 0` for all `i > 0`, and
> 2. if `F` is left exact, then `A` is right acyclic for `F` if and only if `R ⁱ F(A) = 0` for
>    all `i > 0`.
>
> The instance `HasRightDerivedFunctor` follows from `hF`
> (`Functor.hasPointwiseRightDerivedFunctor_of_isRightDerivable`); it names `RF` and the predicate
> `Functor.rightAcyclic`. No injective objects are assumed; with enough injectives this is
> `Functor.rightAcyclic_iff_isIso_and_isZero_rightDerivedPlus`.

```lean
public theorem rightAcyclic_iff_isIso_and_isZero_totalRightDerivedPlusHomology
    (hF : (F.mapHomotopyCategoryPlus ⋙ Plus.Qh).IsRightDerivable
      (HomotopyCategory.Plus.quasiIso C)) (A : C) :
    (F.rightAcyclic A ↔
        (IsIso ((Plus.homologyFunctor D 0).map
            (((F.mapHomotopyCategoryPlus ⋙ Plus.Qh).totalRightDerivedUnit Plus.Qh
              (HomotopyCategory.Plus.quasiIso C)).app
                ((HomotopyCategory.Plus.singleFunctor C 0).obj A))) ∧
          ∀ i > 0, IsZero ((F.totalRightDerivedPlusHomology i).obj A))) ∧
      (PreservesFiniteLimits F →
        (F.rightAcyclic A ↔ ∀ i > 0, IsZero ((F.totalRightDerivedPlusHomology i).obj A)))
```

## Tag 015D, a lemma

[Tag 015D](https://stacks.math.columbia.edu/tag/015D) in the Stacks Project.

**`CategoryTheory.Functor.rightAcyclic_and_shortExact_map_of_shortExact_of_isRightDerivable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightAcyclicEverywhereDefinedShortExact.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightAcyclicEverywhereDefinedShortExact.lean#L217). The attribute's comment: “`RF` everywhere defined is `Functor.IsRightDerivable` of `K⁺(F) ⋙ Q⁺` (Tag 05SV); surjectivity of `F(B) ⟶ F(C)` is `Epi (F.map S.g)`”.

> **Right acyclicity in a short exact sequence**, [StacksProject 015D].
> Let `F : 𝒜 ⥤ ℬ` be a left exact functor between abelian categories and assume that
> `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is everywhere defined, that is, `K⁺(F) ⋙ Q⁺` is right derivable with
> respect to the quasi-isomorphisms of `K⁺(𝒜)` ([Stacks, Tag 05SV]). Let
> `S : 0 ⟶ A ⟶ B ⟶ C ⟶ 0` be a short exact sequence of `𝒜`. Then
> 1. if `A` and `C` are right acyclic for `F`, so is `B`,
> 2. if `A` and `B` are right acyclic for `F`, so is `C`, and
> 3. if `B` and `C` are right acyclic for `F` and `F(B) ⟶ F(C)` is surjective, then so is `A`,
> and in each of the three cases `0 ⟶ F(A) ⟶ F(B) ⟶ F(C) ⟶ 0` is a short exact sequence of `ℬ`.
>
> The instance `HasRightDerivedFunctor` follows from `hF`
> (`Functor.hasPointwiseRightDerivedFunctor_of_isRightDerivable`); it names `RF` and the predicate
> `Functor.rightAcyclic`. No injective objects are assumed; with enough injectives this is
> `Functor.rightAcyclic_and_shortExact_map_of_shortExact`.

```lean
public theorem rightAcyclic_and_shortExact_map_of_shortExact_of_isRightDerivable
    {C D : Type*} [Category* C] [Category* D] [Abelian C] [Abelian D]
    [HasDerivedCategory C] [HasDerivedCategory D] (F : C ⥤ D) [F.Additive]
    [PreservesFiniteLimits F]
    [(F.mapHomotopyCategoryPlus ⋙ Plus.Qh).HasRightDerivedFunctor
      (HomotopyCategory.Plus.quasiIso C)]
    (hF : (F.mapHomotopyCategoryPlus ⋙ Plus.Qh).IsRightDerivable
      (HomotopyCategory.Plus.quasiIso C))
    (S : ShortComplex C) (hS : S.ShortExact) :
    (F.rightAcyclic S.X₁ → F.rightAcyclic S.X₃ →
        F.rightAcyclic S.X₂ ∧ (S.map F).ShortExact) ∧
      (F.rightAcyclic S.X₁ → F.rightAcyclic S.X₂ →
        F.rightAcyclic S.X₃ ∧ (S.map F).ShortExact) ∧
      (F.rightAcyclic S.X₂ → F.rightAcyclic S.X₃ → Epi (F.map S.g) →
        F.rightAcyclic S.X₁ ∧ (S.map F).ShortExact)
```

## Tag 05TE, a lemma

[Tag 05TE](https://stacks.math.columbia.edu/tag/05TE) in the Stacks Project.

**`CategoryTheory.Functor.isDeltaFunctor_and_isUniversal_of_isRightDerivable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedDeltaFunctor.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedDeltaFunctor.lean#L128).

> **The higher right derived functors form a universal `δ`-functor**, [Stacks, Tag 05TE].
> Let `F : 𝒜 ⥤ ℬ` be an additive functor between abelian categories and assume that
> `RF : D⁺(𝒜) ⥤ D⁺(ℬ)` is everywhere defined: the right derived functor of
> `K⁺(F) ⋙ Q : K⁺(𝒜) ⥤ D⁺(ℬ)` with respect to the quasi-isomorphisms is defined at every object
> ([Stacks, Tag 05SV]). Let `(RF, α)` be the right derived functor, so that
> `R ⁱ F = H ⁱ ∘ RF ∘ (·[0])`. Let `h` be a `δ`-functor structure on `A ↦ RF(A[0]) : 𝒜 ⥤ D⁺(ℬ)`
> (the canonical one, `CategoryTheory.Functor.derivedDeltaFunctorStructureOfIsRightDerivable`, is
> `Stacks.DerivedIndexing.singleDeltaFunctorStructure` composed with the exact functor `RF`; the
> statement holds for every such structure), and let `δ` be the connecting
> morphism `R ⁱ F(C) ⟶ R ⁱ⁺¹ F(A)` that the homology sequence of its distinguished triangles
> attaches to a short exact sequence `0 ⟶ A ⟶ B ⟶ C ⟶ 0` of `𝒜`. Then
> 1. `{R ⁱ F, δ}_{i ≥ 0}` is a cohomological `δ`-functor from `𝒜` to `ℬ`: the `R ⁱ F` are additive,
>    the long sequence `0 ⟶ R ⁰ F(A) ⟶ R ⁰ F(B) ⟶ R ⁰ F(C) ⟶ R ¹ F(A) ⟶ ⋯` is exact, and `δ` is
>    natural in the short exact sequence; and
> 2. if every object of `𝒜` is a subobject of an object right acyclic for `F` — an object `I` such
>    that `I[0]` computes `RF` ([Stacks, Tag 0157], [Stacks, Tag 05SX]) — then `{R ⁱ F, δ}_{i ≥ 0}`
>    is a universal `δ`-functor: for every `δ`-functor `{G ⁱ, δ_G}_{i ≥ 0}` from `𝒜` to `ℬ` and
>    every `t₀ : R ⁰ F ⟶ G ⁰` there is a unique family `t ⁱ : R ⁱ F ⟶ G ⁱ` commuting with `δ` and
>    `δ_G` and with `t ⁰ = t₀`.

```lean
public theorem isDeltaFunctor_and_isUniversal_of_isRightDerivable (F : C ⥤ D) [F.Additive]
    (hF : (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).IsRightDerivable
      (HomotopyCategory.Plus.quasiIso C))
    (RF : DerivedCategory.Plus C ⥤ DerivedCategory.Plus D)
    (α : F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh ⟶ DerivedCategory.Plus.Qh ⋙ RF)
    [RF.IsRightDerivedFunctor α (HomotopyCategory.Plus.quasiIso C)]
    (h : DeltaFunctorStructure C (DerivedCategory.Plus D)
      (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF))
    (δ : ∀ {S : ShortComplex C}, S.ShortExact → ∀ i : ℕ,
      (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
          DerivedCategory.Plus.homologyFunctor D i).obj S.X₃ ⟶
        (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
          DerivedCategory.Plus.homologyFunctor D (i + 1)).obj S.X₁)
    (hδ : ∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ), δ hS i =
      (DerivedCategory.Plus.homologyFunctor D 0).homologySequenceδ
        (Pretriangulated.Triangle.mk ((DerivedCategory.Plus.singleFunctor C 0 ⋙ RF).map S.f)
          ((DerivedCategory.Plus.singleFunctor C 0 ⋙ RF).map S.g) (h.δ hS)) i (i + 1) rfl) :
    ((∀ i : ℕ, (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
          DerivedCategory.Plus.homologyFunctor D i).Additive) ∧
      (∀ {S : ShortComplex C}, S.ShortExact →
        Mono ((DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
          DerivedCategory.Plus.homologyFunctor D 0).map S.f)) ∧
      (∀ {S : ShortComplex C} (_ : S.ShortExact) (i : ℕ),
        ∃ hz : (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
              DerivedCategory.Plus.homologyFunctor D i).map S.f ≫
            (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
              DerivedCategory.Plus.homologyFunctor D i).map S.g = 0,
          (ShortComplex.mk _ _ hz).Exact) ∧
      (∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ),
        ∃ hz : (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
            DerivedCategory.Plus.homologyFunctor D i).map S.g ≫ δ hS i = 0,
          (ShortComplex.mk _ _ hz).Exact) ∧
      (∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ),
        ∃ hz : δ hS i ≫ (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
            DerivedCategory.Plus.homologyFunctor D (i + 1)).map S.f = 0,
          (ShortComplex.mk _ _ hz).Exact) ∧
      (∀ {S S' : ShortComplex C} (hS : S.ShortExact) (hS' : S'.ShortExact) (φ : S ⟶ S') (i : ℕ),
        (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
            DerivedCategory.Plus.homologyFunctor D i).map φ.τ₃ ≫ δ hS' i =
          δ hS i ≫ (DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
            DerivedCategory.Plus.homologyFunctor D (i + 1)).map φ.τ₁)) ∧
    ((∀ A : C, ∃ (I : C) (u : A ⟶ I), Mono u ∧
        (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
          (HomotopyCategory.Plus.quasiIso C) ((HomotopyCategory.Plus.singleFunctor C 0).obj I)) →
      ∀ (G : ℕ → C ⥤ D) (_ : ∀ i, (G i).Additive)
        (δG : ∀ {S : ShortComplex C}, S.ShortExact → ∀ i : ℕ,
          (G i).obj S.X₃ ⟶ (G (i + 1)).obj S.X₁),
        (∀ {S : ShortComplex C}, S.ShortExact → Mono ((G 0).map S.f)) →
        (∀ {S : ShortComplex C} (_ : S.ShortExact) (i : ℕ),
          ∃ hz : (G i).map S.f ≫ (G i).map S.g = 0, (ShortComplex.mk _ _ hz).Exact) →
        (∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ),
          ∃ hz : (G i).map S.g ≫ δG hS i = 0, (ShortComplex.mk _ _ hz).Exact) →
        (∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ),
          ∃ hz : δG hS i ≫ (G (i + 1)).map S.f = 0, (ShortComplex.mk _ _ hz).Exact) →
        (∀ {S S' : ShortComplex C} (hS : S.ShortExact) (hS' : S'.ShortExact) (φ : S ⟶ S')
          (i : ℕ), (G i).map φ.τ₃ ≫ δG hS' i = δG hS i ≫ (G (i + 1)).map φ.τ₁) →
        ∀ t₀ : DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
            DerivedCategory.Plus.homologyFunctor D 0 ⟶ G 0,
          ∃! t : ∀ i : ℕ, DerivedCategory.Plus.singleFunctor C 0 ⋙ RF ⋙
              DerivedCategory.Plus.homologyFunctor D i ⟶ G i,
            t 0 = t₀ ∧ ∀ {S : ShortComplex C} (hS : S.ShortExact) (i : ℕ),
              (t i).app S.X₃ ≫ δG hS i = δ hS i ≫ (t (i + 1)).app S.X₁)
```

## Tag 015E, a lemma

[Tag 015E](https://stacks.math.columbia.edu/tag/015E) in the Stacks Project.

**`CategoryTheory.Functor.isIso_ι_app_of_computesRightDerived_single_of_isRightDerivedValueAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/AcyclicResolutions.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/AcyclicResolutions.lean#L486). The attribute's comment: “`RF` defined at `K` in the sense of Tag 05S9, terms right `F`-acyclic in the sense of Tag 0157; conclusion: the canonical map `F(K) ⟶ RF(K)` is an isomorphism”.

> **Leray's acyclicity lemma**, [Stacks, Tag 015E], in Stacks' generality: `RF` is assumed to be
> defined at `K` alone; no global existence of `RF` and no injectives are assumed.
>
> Let `F : 𝒜 ⥤ ℬ` be an additive functor between abelian categories, and write
> `G : K⁺(𝒜) ⥤ D⁺(ℬ)` for `F` applied termwise followed by the localization, and `W` for the
> quasi-isomorphisms of `K⁺(𝒜)`. Let `K` be a bounded below complex all of whose terms `Kⁿ` are
> right `F`-acyclic in the sense of [Stacks, Tag 0157]: `RF` is defined at `Kⁿ[0]` and `Kⁿ[0]`
> computes `RF` ([Stacks, Tag 05SX]). Suppose `RF` is defined at `K` ([Stacks, Tag 05S9]: the
> ind-object `(s : K ⟶ K') ↦ G(K')` is essentially constant). Then the canonical map
> `F(K) ⟶ RF(K)` — the coprojection at the index `𝟙 K` of any value `RF(K)` — is an isomorphism
> in `D⁺(ℬ)`; in particular `K` computes `RF`.
>
> The proof is the source's: the bounded case is the induction along stupid truncations
> (`source_computes_of_bounded`); in general, for each `i` the triangle
> `(σ_{≥ i + 2}K, K, σ_{≤ i + 1}K)` has `RF` defined at its last two vertices, hence at the first,
> with a distinguished triangle of values ([Stacks, Tag 05SC]), and `H ⁱ` of the canonical map at
> `K` is compared with that at `σ_{≤ i + 1}K`, both `σ_{≥ i + 2}F(K)` and `RF(σ_{≥ i + 2}K)` being
> concentrated in degrees `≥ i + 2`.

```lean
public theorem isIso_ι_app_of_computesRightDerived_single_of_isRightDerivedValueAt
    (F : C ⥤ D) [F.Additive] (K : CochainComplex C ℤ) (hK : CochainComplex.plus C K)
    (hacyclic : ∀ n, (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
      (HomotopyCategory.Plus.quasiIso C) ((HomotopyCategory.Plus.singleFunctor C 0).obj (K.X n)))
    (hdef : ∃ c, (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).IsRightDerivedValueAt
      (HomotopyCategory.Plus.quasiIso C) (plusObj K hK) c) :
    (∀ c, (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).IsRightDerivedValueAt
        (HomotopyCategory.Plus.quasiIso C) (plusObj K hK) c →
      IsIso (c.ι.app (MorphismProperty.Under.mk ⊤ (𝟙 (plusObj K hK))
        (MorphismProperty.id_mem _ _)))) ∧
    (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
      (HomotopyCategory.Plus.quasiIso C) (plusObj K hK)
```

## Tag 05TA, a proposition

[Tag 05TA](https://stacks.math.columbia.edu/tag/05TA) in the Stacks Project.

**`CategoryTheory.Functor.hasDerivedFunctors_of_enough_acyclic_objects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/AcyclicResolutions.lean, line 1015](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/AcyclicResolutions.lean#L1015). References: SGA 4 XVII (1.2.7).

> **Stacks 05TA.** Let `F : C ⥤ D` be an additive functor of abelian categories.
>
> 1. If every object of `C` injects into an object `Y` acyclic for `RF` — that is, `Y[0]`
>    computes the right derived functor of `K⁺(C) ⥤ D⁺(D)` in the sense of [Stacks, Tag 05SX],
>    with no global existence of `RF` assumed — then `RF` is defined on all of `K⁺(C)`, the
>    resulting functor `RF : D⁺(C) ⥤ D⁺(D)` is exact (triangulated), and every bounded below
>    complex whose terms are acyclic for `RF` computes `RF`: the unit of `RF` is invertible there.
> 2. Dually, if every object of `C` is a quotient of an object acyclic for `LF`, then `LF` is
>    defined on all of `K⁻(C)`, is exact, and is computed by bounded above complexes of objects
>    acyclic for `LF`.
>
> Part (2) is stated through opposite categories, as in [Stacks, Tag 0157]: `K⁻(C)` is `K⁺(Cᵒᵖ)`,
> `LF` is the right derived functor of `F.op`, and acyclicity for `LF` is right acyclicity for
> `F.op`.

```lean
public theorem hasDerivedFunctors_of_enough_acyclic_objects (F : C ⥤ D) [F.Additive] :
    ((∀ X : C, ∃ (Y : C) (i : X ⟶ Y), Mono i ∧
        (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
          (HomotopyCategory.Plus.quasiIso C)
          ((HomotopyCategory.Plus.singleFunctor C 0).obj Y)) →
      ∃ h : (F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasPointwiseRightDerivedFunctor
          (HomotopyCategory.Plus.quasiIso C),
        letI := h
        ((F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).totalRightDerived
            DerivedCategory.Plus.Qh (HomotopyCategory.Plus.quasiIso C)).IsTriangulated ∧
          ∀ X : HomotopyCategory.Plus C,
            (∀ n : ℤ, F.rightAcyclic (X.obj.as.X n)) →
              IsIso (((F.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).totalRightDerivedUnit
                DerivedCategory.Plus.Qh (HomotopyCategory.Plus.quasiIso C)).app X)) ∧
    ((∀ X : C, ∃ (Y : C) (p : Y ⟶ X), Epi p ∧
        (F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).ComputesRightDerived
          (HomotopyCategory.Plus.quasiIso Cᵒᵖ)
          ((HomotopyCategory.Plus.singleFunctor Cᵒᵖ 0).obj (Opposite.op Y))) →
      ∃ h : (F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).HasPointwiseRightDerivedFunctor
          (HomotopyCategory.Plus.quasiIso Cᵒᵖ),
        letI := h
        ((F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).totalRightDerived
            DerivedCategory.Plus.Qh (HomotopyCategory.Plus.quasiIso Cᵒᵖ)).IsTriangulated ∧
          ∀ X : HomotopyCategory.Plus Cᵒᵖ,
            (∀ n : ℤ, F.op.rightAcyclic (X.obj.as.X n)) →
              IsIso (((F.op.mapHomotopyCategoryPlus ⋙ DerivedCategory.Plus.Qh).totalRightDerivedUnit
                DerivedCategory.Plus.Qh (HomotopyCategory.Plus.quasiIso Cᵒᵖ)).app X))
```

## Tag 015F, a lemma

[Tag 015F](https://stacks.math.columbia.edu/tag/015F) in the Stacks Project.

**`Stacks.DerivedFunctor.HigherDerivedOfExact.everywhere_defined_plus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean#L323). The attribute's comment: “(2)”.

> **Statement (2): `RF : D⁺(A) ⥤ D⁺(B)` is everywhere defined.**
> `RF` relative to `Qis⁺(A)` is defined at every object of `K⁺(A)` (Stacks Definition 2,
> tag 05SV), and the constructed functor `RFPlus F : D⁺(A) ⥤ D⁺(B)`, together with its
> canonical comparison `canonicalPlus F`, *is* the right derived functor of
> `functorPlus F : K⁺(A) ⥤ D⁺(B)` along `Qis⁺(A)` (it satisfies the universal property
> `Functor.IsRightDerivedFunctor`).

```lean
theorem everywhere_defined_plus :
    (functorPlus F).HasPointwiseRightDerivedFunctor (qisPlus (A := A)) ∧
      (RFPlus F).IsRightDerivedFunctor (canonicalPlus F) (qisPlus (A := A))
```

**`Stacks.DerivedFunctor.HigherDerivedOfExact.everywhere_defined`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean, line 363](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean#L363). The attribute's comment: “(3)”.

> **Statement (3): `RF : D(A) ⥤ D(B)` is everywhere defined.**
> `RF` relative to `Qis(A)` is defined at every object of `K(A)` (Stacks Definition 2,
> tag 05SV), and the chosen functor `RF F = F.mapDerivedCategory`, together with its
> canonical comparison `canonical F`, *is* the right derived functor of
> `functorKtoD F : K(A) ⥤ D(B)` along `Qis(A)`.

```lean
theorem everywhere_defined :
    (functorKtoD F).HasPointwiseRightDerivedFunctor (qis (A := A)) ∧
      (RF F).IsRightDerivedFunctor (canonical F) (qis (A := A))
```

**`Stacks.DerivedFunctor.HigherDerivedOfExact.complexes_compute`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean#L436). The attribute's comment: “(4)”.

> **Statement (4), unbounded: every complex computes `RF`.**
> For every complex `K` of `A` (an object of `K(A)`), `RF` is defined at `K` and the
> canonical map `F(K) ⟶ RF(K)`, i.e. the component `(canonical F).app K` of the comparison
> transformation that exhibits `RF F` as the right derived functor, is an isomorphism in
> `D(B)`.

```lean
theorem complexes_compute (K : HomotopyCategory A shape) :
    (functorKtoD F).HasPointwiseRightDerivedFunctorAt (qis (A := A)) K ∧
      IsIso ((canonical F).app K)
```

**`Stacks.DerivedFunctor.HigherDerivedOfExact.objects_right_acyclic`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean, line 467](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean#L467). The attribute's comment: “(1)”.

> **Statement (1): Every object of `A` is right acyclic for `F` (bounded-below).**
> For every object `X` of `A`, the complex `X[0]`, viewed in `K⁺(A)`, computes
> `RF : D⁺(A) ⥤ D⁺(B)` (Stacks Definition 4, tag 0157): `RF` is defined at `X[0]` relative
> to `Qis⁺(A)` and the canonical map `F(X[0]) ⟶ RF(X[0])`, i.e. the component of the
> comparison `canonicalPlus F` exhibiting `RFPlus F` as the right derived functor, is an
> isomorphism in `D⁺(B)`.  Here `X[0]` is `(HomotopyCategory.Plus.singleFunctor A 0).obj X`,
> the single complex concentrated in degree `0` regarded in `K⁺(A)`.

```lean
theorem objects_right_acyclic (X : A) :
    (functorPlus F).HasPointwiseRightDerivedFunctorAt (qisPlus (A := A))
        ((HomotopyCategory.Plus.singleFunctor A 0).obj X) ∧
      IsIso ((canonicalPlus F).app
        ((HomotopyCategory.Plus.singleFunctor A 0).obj X))
```

**`Stacks.DerivedFunctor.HigherDerivedOfExact.higherDerived_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/HigherDerivedFunctors.lean#L488). The attribute's comment: “(5)”.

> **Statement (5a): `RⁱF = 0` for `i ≠ 0`.**
> For every integer `i ≠ 0`, the functor `RⁱF = Hⁱ ∘ RF : A ⥤ B` is the zero functor;
> equivalently `Hⁱ(RF(A[0])) = 0` for all objects `A` and all `i ≠ 0`.

```lean
theorem higherDerived_eq_zero (i : ℤ) (hi : i ≠ 0) :
    IsZero (higherDerived F i)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.16, Tag 05TB](https://stacks.math.columbia.edu/tag/05TB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
