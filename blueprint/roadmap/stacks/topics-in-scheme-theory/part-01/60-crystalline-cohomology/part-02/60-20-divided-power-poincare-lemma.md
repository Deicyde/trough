---
declaration: section
origin: cited
lean: Crystalline.CompletedPoincare.completedDeRham_tensor_augmentation_injective, Crystalline.CompletedPoincare.completedDeRham_tensor_exact_augmentation, Crystalline.CompletedPoincare.completedDeRham_tensor_exact, Crystalline.dividedPowerPolynomialDeRham_tensor_augmentation_injective, Crystalline.dividedPowerPolynomialDeRham_tensor_exact, Crystalline.CompletedPoincare.exists_continuousDividedPowers, Crystalline.CompletedPoincare.continuousDividedPowers_unique, Crystalline.DividedPowerPolynomial.stacks07LD
statement: formalized
proof: formalized
---

# 60.20 Divided power Poincaré lemma

Section 60.20 of the Stacks Project, [Tag 07LB](https://stacks.math.columbia.edu/tag/07LB). 2 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07LC, a lemma

[Tag 07LC](https://stacks.math.columbia.edu/tag/07LC) in the Stacks Project.

**`Crystalline.CompletedPoincare.completedDeRham_tensor_augmentation_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean, line 802](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean#L802). The attribute's comment: “completed\_exactness”.

> **Stacks Project, Tag 07LC, completed case.**  The first map `M → M ⊗̂_A D` of the
> completed divided power de Rham complex of `P = A⟨x_w⟩` with coefficients in a `p`-adically
> complete `A`-module `M` is injective.

```lean
public theorem completedDeRham_tensor_augmentation_injective
    (hM : IsAdicComplete (pAdicIdeal (A := A) p) M) :
    Function.Injective (augmentation p A W (canonicalCompletedDividedPowers p A W) M)
```

**`Crystalline.CompletedPoincare.completedDeRham_tensor_exact_augmentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean, line 817](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean#L817). The attribute's comment: “completed\_exactness”.

> **Stacks Project, Tag 07LC, completed case.**  The completed divided power de Rham complex
> of `P = A⟨x_w⟩` with coefficients in a `p`-adically complete `A`-module `M` is exact at
> `M ⊗̂_A D`.

```lean
public theorem completedDeRham_tensor_exact_augmentation
    (hM : IsAdicComplete (pAdicIdeal (A := A) p) M) :
    Function.Exact (augmentation p A W (canonicalCompletedDividedPowers p A W) M)
      (differential p A W (canonicalCompletedDividedPowers p A W) M 0)
```

**`Crystalline.CompletedPoincare.completedDeRham_tensor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean, line 828](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedExactness.lean#L828). The attribute's comment: “completed\_exactness”.

> **Stacks Project, Tag 07LC, completed case.**  The completed divided power de Rham complex
> of `P = A⟨x_w⟩` with coefficients in a `p`-adically complete `A`-module `M` is exact at
> `M ⊗̂_A Ω^{i+1}_D` for every `i`.

```lean
public theorem completedDeRham_tensor_exact
    (_hM : IsAdicComplete (pAdicIdeal (A := A) p) M) (i : ℕ) :
    Function.Exact (differential p A W (canonicalCompletedDividedPowers p A W) M i)
      (differential p A W (canonicalCompletedDividedPowers p A W) M (i + 1))
```

**`Crystalline.dividedPowerPolynomialDeRham_tensor_augmentation_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean#L71). The attribute's comment: “ordinary\_exactness”.

> **The divided power Poincaré lemma, exactness at the coefficient module.**  For a ring `A`,
> a family of variables `W` and the divided power polynomial algebra `P = A⟨x_w : w ∈ W⟩` with its
> canonical divided powers, the first map `M → M ⊗[A] P` of the complex
>
> `0 → M → M ⊗[A] P → M ⊗[A] Ω¹_{P/A,δ} → M ⊗[A] Ω²_{P/A,δ} → ⋯`
>
> is injective for every `A`-module `M`; the degree-zero term of the complex is identified with
> `M` by `Crystalline.coefficientLinearEquiv`.

```lean
public theorem dividedPowerPolynomialDeRham_tensor_augmentation_injective
    (A : Type u) [CommRing A] (W : Type w)
    (M : Type v) [AddCommGroup M] [Module A M] :
    Function.Injective
      ((augmentedDividedPowerDeRhamDifferential A W 0).hom.lTensor M)
```

**`Crystalline.dividedPowerPolynomialDeRham_tensor_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean#L106). The attribute's comment: “ordinary\_exactness”.

> **The divided power Poincaré lemma.**  For a ring `A`, a family of variables `W` and the
> divided power polynomial algebra `P = A⟨x_w : w ∈ W⟩` with its canonical divided powers, the
> complex
>
> `0 → M → M ⊗[A] P → M ⊗[A] Ω¹_{P/A,δ} → M ⊗[A] Ω²_{P/A,δ} → ⋯`
>
> is exact at every term after the first, for every `A`-module `M`.  Injectivity of the first map
> is `Crystalline.dividedPowerPolynomialDeRham_tensor_augmentation_injective`.

```lean
public theorem dividedPowerPolynomialDeRham_tensor_exact
    (A : Type u) [CommRing A] (W : Type w)
    (M : Type v) [AddCommGroup M] [Module A M] (n : ℕ) :
    Function.Exact
      ((augmentedDividedPowerDeRhamDifferential A W n).hom.lTensor M)
      ((augmentedDividedPowerDeRhamDifferential A W (n + 1)).hom.lTensor M)
```

**`Crystalline.CompletedPoincare.exists_continuousDividedPowers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean, line 698](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean#L698). The attribute's comment: “completed\_exactness”.

> The canonical divided powers of `P` admit a continuous extension to the closure of its
> augmentation ideal in `D`.

```lean
public theorem exists_continuousDividedPowers :
    Nonempty (ContinuousDividedPowers p A W)
```

**`Crystalline.CompletedPoincare.continuousDividedPowers_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean, line 739](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/DividedPowerPoincare/CompletedRing.lean#L739). The attribute's comment: “completed\_exactness”.

> The continuous extension of the canonical divided powers is unique.

```lean
public theorem continuousDividedPowers_unique
    (δ ε : ContinuousDividedPowers p A W) : δ = ε
```

## Tag 07LD, a lemma

[Tag 07LD](https://stacks.math.columbia.edu/tag/07LD) in the Stacks Project.

**`Crystalline.DividedPowerPolynomial.stacks07LD`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincareModuleQuasiIso.lean, line 710](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/Differentials/RelativePoincareModuleQuasiIso.lean#L710). The attribute's comment: “both clauses: the comparison of de Rham complexes for P = B⟨x\_w⟩ on any family of variables is a quasi-isomorphism, for a B-module with integrable connection and, over the p-adic completions D and D', for a D-module with integrable connection”.

> **[Stacks, Lemma 60.19.2, Tag 07LD].**
>
> Let `A` be a ring, let `(B, I, δ)` be a divided power ring which is an `A`-algebra, and let
> `P = B⟨x_w : w ∈ W⟩` be the divided power polynomial ring over `B` on an arbitrary family `W` of
> variables, with divided power ideal `J = IP + B⟨x_w⟩₊`.
>
> 1. For every `B`-module `M` with an integrable connection `∇ : M → M ⊗_B Ω¹_{B/A,δ}`, the map of
>    de Rham complexes `M ⊗_B Ω^*_{B/A,δ} ⟶ M ⊗_P Ω^*_{P/A,δ}` is a quasi-isomorphism
>    (`Crystalline.DividedPowerPolynomial.quasiIso_polyDeRhamComparison`).
> 2. Let `D`, resp. `D'`, be the `p`-adic completion of `B`, resp. `P`, and `Ω̂^i_D`, resp.
>    `Ω̂^i_{D'}`, the `p`-adic completion of `Ω^i_{B/A,δ}`, resp. `Ω^i_{P/A,δ}`.  For every
>    `D`-module `M` with an integrable connection `∇ : M → M ⊗̂_D Ω̂¹_D` (the composite
>    `M → M ⊗̂_D Ω̂¹_D → M ⊗̂_D Ω̂²_D` vanishes), the map of de Rham complexes
>    `M ⊗̂_D Ω̂^*_D ⟶ M ⊗̂_D Ω̂^*_{D'}` is a quasi-isomorphism
>    (`Crystalline.DividedPowerPolynomial.quasiIso_completedDeRhamComparison`).
>
> The second clause holds without the source's hypothesis that `M` is `p`-adically complete, so it
> is not made.  The variables, and the ring `A`, live in the universe of `B`.

```lean
public theorem stacks07LD (A : Type u) [CommRing A] (B : DividedPowerRing.{u}) [Algebra A B]
    (W : Type u) :
    (∀ (M : Type w) [AddCommGroup M] [Module (B : Type u) M]
        (nabla : Connection A (B : Type u) (oneVariableBaseProjection A B) M)
        (hint : Connection.IsIntegrable (oneVariableBaseSource A B)
          (oneVariableBaseProjection A B) (Submodule.mkQ_surjective _)
          (oneVariableBaseGenerationHypothesis A B) nabla),
        QuasiIso (polyDeRhamComparison A B W nabla hint)) ∧
      ∀ (p : ℕ) (M : Type w) [AddCommGroup M]
        [Module (completedDividedPowerRing p (B := (B : Type u))) M]
        (nabla : CompletedConnection p (completedDividedPowerRing p (B := (B : Type u)))
          (completedDividedPowerForms p A B.dividedPowers 1)
          (completedFormsDifferential p A B.dividedPowers) M)
        (hint : CompletedDeRham.HasIntegrableConnection p
          (completedDividedPowerRing p (B := (B : Type u)))
          (completedDividedPowerForms p A B.dividedPowers)
          (completedDividedPowerWedge p A B.dividedPowers)
          (completedDividedPowerDeRham p A B.dividedPowers) M nabla
          (isGradedLeibniz_completedDividedPower p A B.dividedPowers)),
        QuasiIso (completedDeRhamComparison A B W p M nabla hint)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.20, Tag 07LB](https://stacks.math.columbia.edu/tag/07LB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
