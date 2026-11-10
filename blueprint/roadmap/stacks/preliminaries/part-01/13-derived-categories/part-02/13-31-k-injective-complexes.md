---
declaration: section
origin: cited
lean: CochainComplex.IsKInjective, CochainComplex.isKInjective_iff_rightOrthogonal, CochainComplex.isKInjective_tfae, CochainComplex.isKInjective_two_out_of_three_of_distTriang, CochainComplex.isKInjective_of_injective, Stacks.Injectives.KInjectiveProduct.product_isKInjective, Stacks.Injectives.KInjectiveProduct.product_repr_derived, CategoryTheory.Functor.exists_isRightDerivedValueAt_and_isIso_of_isKInjective
statement: formalized
proof: formalized
---

# 13.31 K-injective complexes

Section 13.31 of the Stacks Project, [Tag 070G](https://stacks.math.columbia.edu/tag/070G). 9 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 070H, a definition

[Tag 070H](https://stacks.math.columbia.edu/tag/070H) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.IsKInjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.IsKInjective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L15) (StacksFrontier): “definition: every chain map from an acyclic complex is null-homotopic”.
- [`CochainComplex.isKInjective_iff_rightOrthogonal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.isKInjective_iff_rightOrthogonal#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L17) (StacksFrontier): “Hom_{K(A)}(M, I) = 0 for every acyclic M”.

## Tag 070I, a lemma

[Tag 070I](https://stacks.math.columbia.edu/tag/070I) in the Stacks Project.

**`CochainComplex.isKInjective_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean, line 549](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean#L549).

> **Stacks 070I.** Let `A` be an abelian category and `I` a cochain complex in `A`. The
> following are equivalent: (1) `I` is K-injective; (2) for every quasi-isomorphism `M ⟶ N` in
> `K(A)`, precomposition `Hom_{K(A)}(N, I) → Hom_{K(A)}(M, I)` is bijective; (3) for every `N` in
> `K(A)`, the localization map `Hom_{K(A)}(N, I) → Hom_{D(A)}(N, I)` is bijective.

```lean
public theorem isKInjective_tfae {A : Type u} [Category.{v} A] [Abelian A]
    [HasDerivedCategory.{w} A] (I : CochainComplex A ℤ) :
    List.TFAE
      [I.IsKInjective,
        (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)).isLocal
          ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj I),
        ∀ N : HomotopyCategory A (ComplexShape.up ℤ),
          Function.Bijective (DerivedCategory.Qh.map :
            (N ⟶ (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj I) → _)]
```

## Tag 090X, a lemma

[Tag 090X](https://stacks.math.columbia.edu/tag/090X) in the Stacks Project.

**`CochainComplex.isKInjective_two_out_of_three_of_distTriang`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean, line 569](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean#L569).

> **Stacks 090X.** Let `A` be an abelian category and let `(K, L, M, f, g, h)` be a
> distinguished triangle of the homotopy category `K(A)` of cochain complexes in `A`, where `K`,
> `L`, `M` are cochain complexes. If two out of `K`, `L`, `M` are K-injective, then so is the
> third.

```lean
public theorem isKInjective_two_out_of_three_of_distTriang
    {A : Type u} [Category.{v} A] [Abelian A] {K L M : CochainComplex A ℤ}
    (f : (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K ⟶
      (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj L)
    (g : (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj L ⟶
      (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj M)
    (h : (HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj M ⟶
      ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj K)⟦(1 : ℤ)⟧)
    (hT : Triangle.mk f g h ∈ distTriang (HomotopyCategory A (ComplexShape.up ℤ))) :
    (L.IsKInjective → M.IsKInjective → K.IsKInjective) ∧
      (K.IsKInjective → M.IsKInjective → L.IsKInjective) ∧
      (K.IsKInjective → L.IsKInjective → M.IsKInjective)
```

## Tag 070J, a lemma

[Tag 070J](https://stacks.math.columbia.edu/tag/070J) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.isKInjective_of_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CochainComplex.isKInjective_of_injective#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch13.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch13.lean#L20) (StacksFrontier).

## Tag 0BK6, a lemma

[Tag 0BK6](https://stacks.math.columbia.edu/tag/0BK6) in the Stacks Project.

**`Stacks.Injectives.KInjectiveProduct.product_isKInjective`**, an alias in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean#L345).

> Statement 1. A product of K-injective complexes is K-injective.

```lean
alias product_isKInjective
```

**`Stacks.Injectives.KInjectiveProduct.product_repr_derived`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean, line 409](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean#L409).

> Statement 2. The product complex `∏ᶜ X` represents the product of the family `(I_t)`
> in the derived category `D(A)`: for every complex `K`, the natural comparison map
> `Hom_{D(A)}(K, ∏ᶜ X) → ∏ₜ Hom_{D(A)}(K, I_t)` induced by the projections is a bijection
> (hence an isomorphism of abelian groups).

```lean
theorem product_repr_derived [HasDerivedCategory C]
    {T : Type} (X : T → CochainComplex C ℤ)
    [∀ n : ℤ, HasProduct fun t => (X t).X n] [HasProduct X]
    (hX : ∀ t, (X t).IsKInjective) (K : CochainComplex C ℤ) :
    Function.Bijective (derivedHomComparison X K)
```

## Tag 070Y, a lemma

[Tag 070Y](https://stacks.math.columbia.edu/tag/070Y) in the Stacks Project.

**`CategoryTheory.Functor.exists_isRightDerivedValueAt_and_isIso_of_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean#L386).

> **Stacks 070Y.** Let `A` be an abelian category and `F : K(A) ⥤ H` a functor on the homotopy
> category of `ℤ`-indexed cochain complexes. Let `I` be a K-injective complex. Then:
>
> * `I` computes the right derived functor `RF` relative to the quasi-isomorphisms of `K(A)`: the
>   ind-object `I/Qis(A) ⥤ H`, `(s : I ⟶ N) ↦ F(N)`, is essentially constant, and the canonical
>   map `F(I) ⟶ RF(I)`, i.e. the coprojection of its value cocone at the index `𝟙 I`, is an
>   isomorphism;
> * `RF` is defined at every object `X` of `K(A)` that is quasi-isomorphic to `I`, i.e. admits a
>   quasi-isomorphism to or from `I` in `K(A)`.
>
> The source assumes `F` exact between triangulated categories; neither conclusion uses this.

```lean
public theorem exists_isRightDerivedValueAt_and_isIso_of_isKInjective
    {A : Type u₁} [Category.{v₁} A] [Abelian A] {H : Type u₂} [Category.{v₂} H]
    (F : HomotopyCategory A (ComplexShape.up ℤ) ⥤ H)
    (I : CochainComplex A ℤ) [I.IsKInjective] :
    (∃ c, F.IsRightDerivedValueAt (HomotopyCategory.quasiIso A (.up ℤ))
        ((HomotopyCategory.quotient A (.up ℤ)).obj I) c ∧
        IsIso (c.ι.app (MorphismProperty.Under.mk ⊤
          (𝟙 ((HomotopyCategory.quotient A (.up ℤ)).obj I))
          (MorphismProperty.id_mem _ _)))) ∧
      ∀ X : HomotopyCategory A (.up ℤ),
        ((∃ s : X ⟶ (HomotopyCategory.quotient A (.up ℤ)).obj I,
            HomotopyCategory.quasiIso A (.up ℤ) s) ∨
          (∃ s : (HomotopyCategory.quotient A (.up ℤ)).obj I ⟶ X,
            HomotopyCategory.quasiIso A (.up ℤ) s)) →
        ∃ c, F.IsRightDerivedValueAt (HomotopyCategory.quasiIso A (.up ℤ)) X c
```

## Tag 070K, a lemma

[Tag 070K](https://stacks.math.columbia.edu/tag/070K) in the Stacks Project.

**`CategoryTheory.Functor.hasPointwiseRightDerivedFunctor_and_isIso_app_of_exists_quasiIso_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean, line 423](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/Locality.lean#L423).

> **Stacks 070K.** Let `A` be an abelian category such that every complex admits a
> quasi-isomorphism towards a K-injective complex, and let `F : K(A) ⥤ D'` be a functor on the
> homotopy category of `ℤ`-indexed cochain complexes. Then:
>
> * `F` has a pointwise right derived functor with respect to the quasi-isomorphisms `Qis(A)` of
>   `K(A)`; in particular `F.HasRightDerivedFunctor Qis(A)` holds, i.e. `F` has a right derived
>   functor `RF : D(A) ⥤ D'`, a left Kan extension of `F` along the localization `K(A) ⥤ D(A)`;
> * every K-injective complex `I` computes `RF`: for any localization functor `L` for `Qis(A)` and
>   any right derived functor `RF` of `F` with unit `α : F ⟶ L ⋙ RF`, the canonical map
>   `α.app I : F(I) ⟶ RF(I)` is an isomorphism, which is the source's `RF(I) = F(I)`.
>
> The source assumes `F` exact between triangulated categories; neither conclusion uses this.

```lean
public theorem hasPointwiseRightDerivedFunctor_and_isIso_app_of_exists_quasiIso_isKInjective
    {A : Type u₁} [Category.{v₁} A] [Abelian A] {H : Type u₂} [Category.{v₂} H]
    (F : HomotopyCategory A (ComplexShape.up ℤ) ⥤ H)
    (hA : ∀ K : CochainComplex A ℤ, ∃ (I : CochainComplex A ℤ) (f : K ⟶ I),
      I.IsKInjective ∧ QuasiIso f) :
    F.HasPointwiseRightDerivedFunctor (HomotopyCategory.quasiIso A (ComplexShape.up ℤ)) ∧
      ∀ {D : Type u₃} [Category.{v₃} D] (L : HomotopyCategory A (ComplexShape.up ℤ) ⥤ D)
        [L.IsLocalization (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))]
        (RF : D ⥤ H) (α : F ⟶ L ⋙ RF)
        [RF.IsRightDerivedFunctor α (HomotopyCategory.quasiIso A (ComplexShape.up ℤ))]
        (I : CochainComplex A ℤ), I.IsKInjective →
          IsIso (α.app ((HomotopyCategory.quotient A (ComplexShape.up ℤ)).obj I))
```

## Tag 070L, a lemma

[Tag 070L](https://stacks.math.columbia.edu/tag/070L) in the Stacks Project.

**`isKInjective_limit_of_inverseSystem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/InverseLimit.lean, line 533](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/InverseLimit.lean#L533).

> **Stacks Tag 070L (Lemma 13.31.8).** Let `A` be an abelian category and let
> `F : ℕᵒᵖ ⥤ CochainComplex A ℤ` be an inverse system of complexes (transition maps
> go from larger to smaller index). Assume:
> 1. each complex `F.obj (op n)` is K-injective;
> 2. each transition map `F_{n+1} ⟶ F_n` is a split surjection in every degree `m`;
> 3. the limit complex `limit F` exists (the degreewise limits exist in `A`).
> Then the limit complex `limit F` is K-injective.
>
> The proof reduces (via `exists_cylinder_extension_limit`, then
> `exists_compatible_homotopy_family`) to the Mittag–Leffler construction of a compatible
> family of null-homotopies; the final step postcomposes the canonical cylinder homotopy
> `cylinder.ι₀ ≃ cylinder.ι₁` with the assembled extension.

```lean
theorem isKInjective_limit_of_inverseSystem
    (F : ℕᵒᵖ ⥤ CochainComplex A ℤ) [HasLimit F]
    (hKInj : ∀ n : ℕ, (F.obj (op n)).IsKInjective)
    (hSplit : ∀ (n : ℕ) (m : ℤ),
      IsSplitEpi ((F.map (homOfLE (Nat.le_succ n)).op).f m)) :
    (limit F).IsKInjective
```

## Tag 08BJ, a lemma

[Tag 08BJ](https://stacks.math.columbia.edu/tag/08BJ) in the Stacks Project.

**`CochainComplex.isKInjective_mapHomologicalComplex_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/KInjective/AdjointAndProducts.lean#L171).

> **Stacks 08BJ.** Adjoint criterion for K-injectivity, exactness form: let `u : A ⥤ B` and
> `v : B ⥤ A` be additive functors between abelian categories such that `u` is right adjoint to `v`
> and `v` is exact. Then `u` carries K-injective cochain complexes to K-injective cochain
> complexes.

```lean
theorem isKInjective_mapHomologicalComplex_of_exact
    (u : A ⥤ B) (v : B ⥤ A) [u.Additive] [v.Additive] (adj : v ⊣ u)
    [PreservesFiniteLimits v] [PreservesFiniteColimits v]
    (I : CochainComplex A ℤ) [I.IsKInjective] :
    CochainComplex.IsKInjective ((u.mapHomologicalComplex (ComplexShape.up ℤ)).obj I)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.31, Tag 070G](https://stacks.math.columbia.edu/tag/070G)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
