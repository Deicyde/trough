---
declaration: section
origin: cited
lean: CategoryTheory.Pretriangulated.IsDerivedLimit, Stacks.DerivedProducts.hasProductsOfShape_derivedCategory, Stacks.DerivedProducts.isLimit_productFanInDerivedCategory, Stacks.DerivedProducts.isIso_piComparison_homologyFunctor, DerivedCategory.exists_isDerivedLimit_of_forall_isGE, CochainComplex.isKInjective_limit_and_isDerivedLimit_of_isSplitEpi, CochainComplex.exists_quasiIso_isKInjective
statement: formalized
proof: formalized
---

# 13.34 Derived limits

Section 13.34 of the Stacks Project, [Tag 08TB](https://stacks.math.columbia.edu/tag/08TB). 5 tags here are carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08TC, a definition

[Tag 08TC](https://stacks.math.columbia.edu/tag/08TC) in the Stacks Project.

**`CategoryTheory.Pretriangulated.IsDerivedLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Triangulated/HomotopyLimit.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Triangulated/HomotopyLimit.lean#L72).

> An object `K` of a pre-triangulated category `D` is a **derived limit**, or **homotopy
> limit**, of an inverse system `F : ℕᵒᵖ ⥤ D` of objects of `D` whose objects have a product —
> written `K = R lim Kₙ` — if there is a distinguished triangle
> `K ⟶ ∏ Kₙ ⟶ ∏ Kₙ ⟶ K⟦1⟧` in which the middle map is the difference map
> `(kₙ) ↦ (kₙ - fₙ₊₁(kₙ₊₁))`, where `Kₙ = F.obj ⟨n⟩` and `fₙ₊₁ = F.map (homOfLE (Nat.le_succ n)).op`
> is the transition map `Kₙ₊₁ ⟶ Kₙ`. Such a `K` is unique only up to non-unique isomorphism, which
> is why this is a predicate and not a construction.

```lean
public def IsDerivedLimit (F : ℕᵒᵖ ⥤ D) [HasProduct fun n : ℕ => F.obj ⟨n⟩] (K : D) : Prop
```

## Tag 07KC, a lemma

[Tag 07KC](https://stacks.math.columbia.edu/tag/07KC) in the Stacks Project.

**`Stacks.DerivedProducts.hasProductsOfShape_derivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean, line 1170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean#L1170). The attribute's comment: “(1)”.

> **Statement 1 (Existence of products).**
> The derived category `D(A)` has countable products (Definition 5).
>
> INFORMAL ARGUMENT (sound, sanity-checked).
> `Q` is essentially surjective (`(DerivedCategory.Q).EssSurj` is an instance) and,
> by `preservesLimitsOfShape_Q`, preserves `I`-indexed products.  Given any family
> `X : I → D(A)`, choose for each `i` a complex `K i` with `Q.obj (K i) ≅ X i`
> (essential surjectivity).  Then `CochainComplex A ℤ` has the product `∏ᶜ K`
> (`HasProductsOfShape I (CochainComplex A ℤ)` infers), and `Q` carries its limit
> cone to a limit cone over `i ↦ Q.obj (K i)`; transporting along the isos
> `Q.obj (K i) ≅ X i` (`HasLimit.iso`/`Limits.HasLimit.ofIso`-style transport, or
> `hasLimitOfIso`) yields a product of `X`.  Hence `D(A)` has products of shape `I`.
>
> PROOF STRATEGY (Lean).
> `constructor; intro X` (unfold `HasProductsOfShape` to `∀ family, HasProduct`).
> Pick reps `K i := (Q.objPreimage (X i))` with `Q.objObjPreimageIso`.
> Use `preservesLimitsOfShape_Q` to get the mapped cone of `∏ᶜ K` is a limit
> (`isLimitOfPreserves`), giving `HasProduct (fun i => Q.obj (K i))`; then transport
> `HasProduct` along the natural iso `Q.obj (K ·) ≅ X` via
> `hasProduct_of_iso`/`HasLimit.ofIso` (`Discrete.natIso` of the objectwise isos).

```lean
theorem hasProductsOfShape_derivedCategory :
    HasProductsOfShape I (DerivedCategory A)
```

**`Stacks.DerivedProducts.isLimit_productFanInDerivedCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean, line 1204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean#L1204). The attribute's comment: “(2)”.

> **Statement 2 (Computation via termwise products).**
> For any countable family `K : I → CochainComplex A ℤ` of complexes (representing
> objects of `D(A)`), the image under `Q` of the termwise product complex `∏ᶜ K`,
> together with the projection chain maps `Q.map (Pi.π K i)`, is a product of the
> family `(Q.obj (K i))` in `D(A)`, i.e. the corresponding fan is a limit cone.
> In particular the product is independent, up to canonical isomorphism in `D(A)`,
> of the choice of representing complexes.

```lean
theorem isLimit_productFanInDerivedCategory (K : I → CochainComplex A ℤ) :
    Nonempty (IsLimit (productFanInDerivedCategory K))
```

**`Stacks.DerivedProducts.isIso_piComparison_homologyFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean, line 1236](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/Products.lean#L1236). The attribute's comment: “(3)”.

> **Statement 3 (Cohomology of the product).**
> For every `p ∈ ℤ` and every countable family `X : I → D(A)`, the canonical
> comparison morphism
> `H^p(∏ X_i) → ∏ H^p(X_i)`
> induced by the projections (`piComparison` of the homology functor) is an
> isomorphism in `A`.  Equivalently `H^p(∏ X_i) = ∏ H^p(X_i)` (canonical iso).

```lean
theorem isIso_piComparison_homologyFunctor
    [HasProductsOfShape I (DerivedCategory A)]
    (X : I → DerivedCategory A) (p : ℤ) :
    IsIso (piComparison (DerivedCategory.homologyFunctor A p) X)
```

## Tag 0BK7, a lemma

[Tag 0BK7](https://stacks.math.columbia.edu/tag/0BK7) in the Stacks Project.

**`DerivedCategory.exists_isDerivedLimit_of_forall_isGE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean#L273).

> Let `𝒜` be an abelian category with countable products and enough injectives. Then any
> inverse system `F : ℕᵒᵖ ⥤ D(𝒜)` of objects of `D⁺(𝒜)`, i.e. whose values `Kₙ = F.obj ⟨n⟩` are
> bounded below, has a product `∏ Kₙ` in `D(𝒜)` and a derived limit `K = R lim Kₙ`: an object
> sitting in a distinguished triangle `K ⟶ ∏ Kₙ ⟶ ∏ Kₙ ⟶ K⟦1⟧` whose middle map is
> `(kₙ) ↦ (kₙ - fₙ₊₁(kₙ₊₁))`.

```lean
public theorem exists_isDerivedLimit_of_forall_isGE (F : ℕᵒᵖ ⥤ DerivedCategory 𝒜)
    (hF : ∀ n : ℕ, ∃ a : ℤ, (F.obj ⟨n⟩).IsGE a) :
    ∃ (_ : HasProduct fun n : ℕ => F.obj ⟨n⟩) (K : DerivedCategory 𝒜), IsDerivedLimit F K
```

## Tag 070M, a lemma

[Tag 070M](https://stacks.math.columbia.edu/tag/070M) in the Stacks Project.

**`CochainComplex.isKInjective_limit_and_isDerivedLimit_of_isSplitEpi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean, line 738](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean#L738).

> Let `A` be an abelian category with countable products and let
> `𝓘 : ℕᵒᵖ ⥤ CochainComplex A ℤ` be an inverse system of K-injective complexes whose transition maps
> are degreewise split epimorphisms. Then the limit `I = lim 𝓘` exists, it is K-injective, and it
> represents the derived limit `R lim 𝓘ₙ`. Moreover, for every cochain complex `K` of `A` equipped
> with quasi-isomorphisms `f n : τ_{≥ -n} K ⟶ 𝓘ₙ` making the ladder over the canonical maps
> `K.πTruncGE (-n) : K ⟶ τ_{≥ -n} K` commute — the system produced by Stacks 070F, for which
> `R lim 𝓘ₙ` is `R lim τ_{≥ -n} K`, as the `f n` become isomorphisms in `D(A)` — the unique map
> `γ : K ⟶ I` compatible with the maps `K ⟶ τ_{≥ -n} K ⟶ 𝓘ₙ` is a quasi-isomorphism if and only if
> every map `K ⟶ R lim τ_{≥ -n} K` compatible with the projections, as in Stacks 0H72, is an
> isomorphism in `D(A)`.

```lean
public theorem isKInjective_limit_and_isDerivedLimit_of_isSplitEpi
    (𝓘 : ℕᵒᵖ ⥤ CochainComplex A ℤ) (h𝓘 : ∀ n : ℕ, (𝓘.obj ⟨n⟩).IsKInjective)
    (hsplit : ∀ (n : ℕ) (i : ℤ), IsSplitEpi ((𝓘.map (homOfLE (Nat.le_succ n)).op).f i)) :
    ∃ (_ : HasLimit 𝓘) (_ : HasProduct fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩),
      (limit 𝓘).IsKInjective ∧ IsDerivedLimit (𝓘 ⋙ Q) (Q.obj (limit 𝓘)) ∧
        ∀ (K : CochainComplex A ℤ) (f : ∀ n : ℕ, K.truncGE (-(n : ℤ)) ⟶ 𝓘.obj ⟨n⟩),
          (∀ n : ℕ, QuasiIso (f n)) →
          (∀ n : ℕ, K.πTruncGE (-((n + 1 : ℕ) : ℤ)) ≫ f (n + 1) ≫
              𝓘.map (homOfLE (Nat.le_succ n)).op = K.πTruncGE (-(n : ℤ)) ≫ f n) →
          ∃ γ : K ⟶ limit 𝓘, (∀ n : ℕ, γ ≫ limit.π 𝓘 ⟨n⟩ = K.πTruncGE (-(n : ℤ)) ≫ f n) ∧
            (QuasiIso γ ↔ ∀ (L : DerivedCategory A) (c : Q.obj K ⟶ L)
              (p : L ⟶ ∏ᶜ fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩)
              (δ : (∏ᶜ fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩) ⟶ L⟦(1 : ℤ)⟧),
              Triangle.mk p (Pi.lift fun n : ℕ =>
                  Pi.π (fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩) n -
                    Pi.π (fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩) (n + 1) ≫
                      (𝓘 ⋙ Q).map (homOfLE (Nat.le_succ n)).op) δ ∈
                distTriang (DerivedCategory A) →
              (∀ n : ℕ, c ≫ p ≫ Pi.π (fun n : ℕ => (𝓘 ⋙ Q).obj ⟨n⟩) n =
                Q.map (K.πTruncGE (-(n : ℤ)) ≫ f n)) → IsIso c)
```

## Tag 090Y, a lemma

[Tag 090Y](https://stacks.math.columbia.edu/tag/090Y) in the Stacks Project.

**`CochainComplex.exists_quasiIso_isKInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean, line 1064](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/DerivedCategory/DerivedLimits.lean#L1064).

> Let `𝒜` be an abelian category having enough injectives and exact countable
> products. Then every cochain complex `K` of objects of `𝒜` admits a quasi-isomorphism `f : K ⟶ I`
> to a K-injective complex `I`.

```lean
public theorem exists_quasiIso_isKInjective {𝒜 : Type u} [Category.{v} 𝒜] [Abelian 𝒜]
    [EnoughInjectives 𝒜] [HasProductsOfShape ℕ 𝒜] [HasExactLimitsOfShape (Discrete ℕ) 𝒜]
    (K : CochainComplex 𝒜 ℤ) :
    ∃ (I : CochainComplex 𝒜 ℤ) (f : K ⟶ I) (_ : QuasiIso f), I.IsKInjective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 13.34, Tag 08TB](https://stacks.math.columbia.edu/tag/08TB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
