---
declaration: section
origin: cited
lean: trdeg_eq_finrank_kaehlerDifferential_sub_finrank_h1Cotangent, jacobiZariski_exact_of_fieldExtensions, finrank_ker_sub_finrank_coker_kaehlerDifferential_map_sub_h1Cotangent_map_of_essFiniteType
statement: formalized
proof: formalized
---

# 15.35 Cartier's equality and geometric regularity

Section 15.35 of the Stacks Project, [Tag 07E0](https://stacks.math.columbia.edu/tag/07E0). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 07E1, a lemma

[Tag 07E1](https://stacks.math.columbia.edu/tag/07E1) in the Stacks Project.

**`trdeg_eq_finrank_kaehlerDifferential_sub_finrank_h1Cotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean#L342). References: EGA 0 (21.7.1); EGA 0 (21.7.2), “special case”.

> **Cartier's equality.** For a finitely generated extension of fields `K/k`, the module of
> Kähler differentials and the first homology of the naive cotangent complex are
> finite-dimensional, and their dimensions differ by the transcendence degree.

```lean
public theorem trdeg_eq_finrank_kaehlerDifferential_sub_finrank_h1Cotangent
    (k : Type u) (K : Type v) [Field k] [Field K] [Algebra k K]
    [Algebra.EssFiniteType k K] :
    FiniteDimensional K Ω[K⁄k] ∧
      FiniteDimensional K (Algebra.H1Cotangent k K) ∧
        (Cardinal.toNat (Algebra.trdeg k K) : ℤ) =
          (Module.finrank K Ω[K⁄k] : ℤ) - Module.finrank K (Algebra.H1Cotangent k K)
```

## Tag 07E2, a lemma

[Tag 07E2](https://stacks.math.columbia.edu/tag/07E2) in the Stacks Project.

**`jacobiZariski_exact_of_fieldExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean, line 480](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean#L480).

> Let `M/L/K` be a tower of field extensions. Then the canonical Jacobi--Zariski sequence
>
> `0 → H₁(L_{L/K}) ⊗[L] M → H₁(L_{M/K}) → H₁(L_{M/L}) →`
> `M ⊗[L] Ω[L⁄K] → Ω[M⁄K] → Ω[M⁄L] → 0`
>
> is exact.

```lean
public theorem jacobiZariski_exact_of_fieldExtensions
    (K : Type u₁) (L : Type u₂) (M : Type u₃)
    [Field K] [Field L] [Field M]
    [Algebra K L] [Algebra L M] [Algebra K M] [IsScalarTower K L M] :
    let i := (Algebra.H1Cotangent.map K K L M).liftBaseChange M
    let p := Algebra.H1Cotangent.map K L M M
    let δ := Algebra.H1Cotangent.δ K L M
    let d := KaehlerDifferential.mapBaseChange K L M
    let q := KaehlerDifferential.map K L M M
    Function.Injective i ∧
      Function.Exact i p ∧
      Function.Exact p δ ∧
      Function.Exact δ d ∧
      Function.Exact d q ∧
      Function.Surjective q
```

## Tag 07E3, a lemma

[Tag 07E3](https://stacks.math.columbia.edu/tag/07E3) in the Stacks Project.

**`finrank_ker_sub_finrank_coker_kaehlerDifferential_map_sub_h1Cotangent_map_of_essFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean, line 613](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/KaehlerDifferential/CartierEquality.lean#L613). References: EGA 0 (21.7.1).

> Given a commutative square of fields
> ```
> K  → K'
> ↑    ↑
> k  → k'
> ```
> whose horizontal extensions `k'/k` and `K'/K` are finitely generated field extensions (possibly
> transcendental), the kernels and cokernels of the canonical maps
> `α : K' ⊗[K] Ω[K⁄k] → Ω[K'⁄k']` and `β : K' ⊗[K] H₁(L_{K/k}) → H₁(L_{K'/k'})` are
> finite-dimensional. The alternating sum of their dimensions is the difference of the
> transcendence degrees of the horizontal extensions.
>
> A finitely generated field extension is expressed by `Algebra.EssFiniteType`, following Mathlib;
> it is equivalent to `(⊤ : IntermediateField k k').FG` by `IntermediateField.fg_top_iff`. Both
> transcendence degrees are finite, so they are written as `Cardinal.toNat` of `Algebra.trdeg`.

```lean
public theorem
    finrank_ker_sub_finrank_coker_kaehlerDifferential_map_sub_h1Cotangent_map_of_essFiniteType
    (k : Type u₁) (K : Type u₂) (k' : Type u₃) (K' : Type u₄)
    [Field k] [Field K] [Field k'] [Field K']
    [Algebra k K] [Algebra k k'] [Algebra K K'] [Algebra k' K'] [Algebra k K']
    [IsScalarTower k K K'] [IsScalarTower k k' K']
    [Algebra.EssFiniteType k k'] [Algebra.EssFiniteType K K'] :
    let α := (KaehlerDifferential.map k k' K K').liftBaseChange K'
    let β := (Algebra.H1Cotangent.map k k' K K').liftBaseChange K'
    FiniteDimensional K' (LinearMap.ker α) ∧
      FiniteDimensional K' (Ω[K'⁄k'] ⧸ LinearMap.range α) ∧
      FiniteDimensional K' (LinearMap.ker β) ∧
      FiniteDimensional K' (Algebra.H1Cotangent k' K' ⧸ LinearMap.range β) ∧
      (Module.finrank K' (LinearMap.ker α) : ℤ) -
          Module.finrank K' (Ω[K'⁄k'] ⧸ LinearMap.range α) -
          Module.finrank K' (LinearMap.ker β) +
          Module.finrank K' (Algebra.H1Cotangent k' K' ⧸ LinearMap.range β) =
      (Cardinal.toNat (Algebra.trdeg k k') : ℤ) -
          Cardinal.toNat (Algebra.trdeg K K')
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 15.35, Tag 07E0](https://stacks.math.columbia.edu/tag/07E0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
