---
declaration: section
origin: cited
lean: BoundedFreeComplex, exists_splitOff_elementaryComplex_of_hasInvertibleCoeff, exists_trivial_iso_of_exact, LinearMap.exists_trivialDecomposition_of_injective_of_exact, Stacks.DeterminantalRank.exteriorRank, Stacks.DeterminantalRank.detIdeal, StacksComplex.rank_eq_rIndex, StacksComplex.rank_add_rank
statement: formalized
proof: formalized
---

# 10.102 What makes a complex exact?

Section 10.102 of the Stacks Project, [Tag 00MR](https://stacks.math.columbia.edu/tag/00MR). 9 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00MS, a situation

[Tag 00MS](https://stacks.math.columbia.edu/tag/00MS) in the Stacks Project.

**`BoundedFreeComplex`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/FiniteFreeComplex/BoundedFreeComplex.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/FiniteFreeComplex/BoundedFreeComplex.lean#L35). References: SGA 4½ Rapport (4.11).

> A complex `0 → R^{n_e} → R^{n_{e-1}} → ⋯ → R^{n_0}` of finite free `R`-modules, as in
> Stacks Situation 10.102.1 (tag 00MS). The ranks are given by `n : ℕ → ℕ` with `n i = 0` for
> `i > e`, and the differential `R^{n_{i+1}} → R^{n_i}` by the matrix
> `φ i : Matrix (Fin (n i)) (Fin (n (i + 1))) R`.

```lean
structure BoundedFreeComplex (R : Type*) [CommRing R]
```

## Tag 00MT, a lemma

[Tag 00MT](https://stacks.math.columbia.edu/tag/00MT) in the Stacks Project.

**`exists_splitOff_elementaryComplex_of_hasInvertibleCoeff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/FiniteFreeComplex/SplitOffElementary.lean, line 801](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/FiniteFreeComplex/SplitOffElementary.lean#L801).

> Let `R` be a ring and `C` a complex of finite free `R`-modules `C_j = R^{n_j}`. If the
> differential `φ_i` has an invertible matrix coefficient, then `n_i ≥ 1`, `n_{i-1} ≥ 1`, and there
> is a complex of finite free `R`-modules `C'` with the ranks decremented at degrees `i` and `i-1`
> (and unchanged elsewhere) together with an isomorphism of complexes
> `C ≅ C' ⊕ T^{(i)}`, where `T^{(i)}` is the elementary identity complex of `elementaryComplex`.

```lean
theorem exists_splitOff_elementaryComplex_of_hasInvertibleCoeff {R : Type*} [CommRing R]
    (C : FreeComplex R) (i : ℤ) (h : HasInvertibleCoeff C i) :
    1 ≤ C.n i ∧ 1 ≤ C.n (i - 1) ∧
    ∃ C' : FreeComplex R,
      (∀ j, C'.n j = if j = i then C.n i - 1 else if j = i - 1 then C.n (i - 1) - 1 else C.n j) ∧
      Nonempty (C.toComplex ≅ C'.toComplex ⊞ (elementaryComplex R i).toComplex)
```

## Tag 00MY, a lemma

[Tag 00MY](https://stacks.math.columbia.edu/tag/00MY) in the Stacks Project.

**`exists_trivial_iso_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/FiniteFreeComplex/TrivialIsoOfExact.lean, line 802](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/FiniteFreeComplex/TrivialIsoOfExact.lean#L802).

> Let `R` be a Noetherian local ring whose maximal ideal `m` is an associated prime of `R`, i.e.
> `R` has depth `0`. Then every complex of finite free `R`-modules
> `0 → R^{n_e} → ⋯ → R^{n_0}` which is exact at `R^{n_e}, …, R^{n_1}` is isomorphic to a complex
> of the same length and ranks all of whose differentials are partial permutation matrices, that
> is, to a direct sum of trivial complexes.

```lean
theorem exists_trivial_iso_of_exact
    [IsNoetherianRing R] [IsLocalRing R]
    (hdepth : (IsLocalRing.maximalIdeal R) ∈ associatedPrimes R R)
    (C : BoundedFreeComplex R) (hC : C.Exact) :
    ∃ D : BoundedFreeComplex R, ∃ _ : C.Iso D,
      D.e = C.e ∧ (∀ i, D.n i = C.n i) ∧ D.IsTrivial
```

## Tag 00MU, a lemma

[Tag 00MU](https://stacks.math.columbia.edu/tag/00MU) in the Stacks Project.

**`LinearMap.exists_trivialDecomposition_of_injective_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Artinian/FreeComplex.lean, line 501](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Artinian/FreeComplex.lean#L501).

> **An exact complex of finite free modules over an Artinian local ring is a direct sum of
> trivial complexes.** Let `R` be an Artinian local ring and let
> `0 → R^{n_{e+1}} →[φ e] R^{n_e} → ⋯ → R^{n_1} →[φ 0] R^{n_0}` be a complex of finite free
> `R`-modules which is exact at `R^{n_{e+1}}, …, R^{n_1}`. Then there are multiplicities `c j` and
> `R`-linear bijections `g i : R^{n_i} ≃ R^{c_i} × R^{c_{i+1}}` in the degrees `i ≤ e + 1`, with
> `c (e + 2) = 0`, carrying each differential `φ i` to `(x, y) ↦ (0, x)`; that is, the complex is
> isomorphic to the direct sum of `c_j` copies, for each `0 ≤ j ≤ e + 1`, of the trivial complex
> with the identity map of `R` in degrees `j` and `j - 1`.

```lean
public theorem LinearMap.exists_trivialDecomposition_of_injective_of_exact
    {R : Type*} [CommRing R] [IsArtinianRing R] [IsLocalRing R] (e : ℕ) (n : ℕ → ℕ)
    (φ : ∀ i, (Fin (n (i + 1)) → R) →ₗ[R] (Fin (n i) → R))
    (hφ : ∀ k < e, φ k ∘ₗ φ (k + 1) = 0)
    (htop : Function.Injective (φ e))
    (hex : ∀ k < e, Function.Exact (φ (k + 1)) (φ k)) :
    ∃ (c : ℕ → ℕ) (g : ∀ i, (Fin (n i) → R) →ₗ[R] ((Fin (c i) → R) × (Fin (c (i + 1)) → R))),
      c (e + 2) = 0 ∧ (∀ i ≤ e + 1, Function.Bijective (g i)) ∧
        (∀ i ≤ e, g i ∘ₗ φ i = LinearMap.inr R _ _ ∘ₗ LinearMap.fst R _ _ ∘ₗ g (i + 1))
```

## Tag 00MV, a definition

[Tag 00MV](https://stacks.math.columbia.edu/tag/00MV) in the Stacks Project.

**`Stacks.DeterminantalRank.exteriorRank`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean, line 103](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean#L103). The attribute's comment: “(1)”.

> The rank of `φ = mulVecLin A`: the largest `r ≤ min m n` such that the `r`-th exterior
> power `⋀^r φ` is nonzero. Since `⋀^r φ = 0` for `r > min m n`, and `⋀^0 φ = id ≠ 0` for
> nontrivial `R`, this is the largest `r` with `⋀^r φ ≠ 0`.

```lean
noncomputable def exteriorRank (A : Matrix (Fin n) (Fin m) R) : ℕ
```

**`Stacks.DeterminantalRank.detIdeal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/ExteriorRank.lean#L109). The attribute's comment: “(2)”.

> The determinantal ideal `I(φ)`: the ideal generated by the `rank × rank` minors of `A`.
> When `rank = 0` the only minor is the empty minor `det (A.submatrix _ _) = 1`, so `I(φ) = R`.

```lean
noncomputable def detIdeal (A : Matrix (Fin n) (Fin m) R) : Ideal R
```

## Tag 00MW, a lemma

[Tag 00MW](https://stacks.math.columbia.edu/tag/00MW) in the Stacks Project.

**`StacksComplex.rank_eq_rIndex`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean, line 478](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean#L478). The attribute's comment: “(1)”.

> If the complex is isomorphic to a direct sum of trivial complexes,
> then for `1 ≤ i ≤ e` the rank of `φ_i` (which is `d (i-1)`, or equivalently `d k` with
> `k = i-1` ranging over `0 ≤ k ≤ e-1`) equals `r_i = ∑_{l=i}^e (-1)^{l-i} n_l`.

```lean
theorem rank_eq_rIndex (C : Complex R e) (hC : IsoToSumOfTrivials C)
    (k : ℕ) (hk : k < e) :
    (rank (C.d k) : ℤ) = rIndex C (k + 1)
```

**`StacksComplex.rank_add_rank`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean, line 489](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean#L489). The attribute's comment: “(2)”.

> If the complex is isomorphic to a direct sum of trivial complexes, then for `1 ≤ i ≤ e-1`,
> `rank(φ_{i+1}) + rank(φ_i) = n_i`. In the indexing `d j = φ_{j+1}`, with `k = i-1`
> ranging over `0 ≤ k ≤ e-2`, this reads `rank (d (k+1)) + rank (d k) = n (k+1)`.

```lean
theorem rank_add_rank (C : Complex R e) (hC : IsoToSumOfTrivials C)
    (k : ℕ) (hk : k + 1 < e) :
    rank (C.d (k + 1)) + rank (C.d k) = C.n (k + 1)
```

**`StacksComplex.minorIdeal_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean, line 527](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/LinearAlgebra/Matrix/DeterminantalRank/SumOfTrivials.lean#L527). The attribute's comment: “(3)”.

> If the complex is isomorphic to a direct sum of trivial complexes, then for `1 ≤ i ≤ e`,
> the ideal `I(φ_i)` is the unit ideal `R`. In the indexing `d k = φ_{k+1}` with `0 ≤ k ≤ e-1`,
> this is `I(d k) = ⊤`.

```lean
theorem minorIdeal_eq_top (C : Complex R e) (hC : IsoToSumOfTrivials C)
    (k : ℕ) :
    minorIdeal (C.d k) = ⊤
```

## Tag 00MZ, a lemma

[Tag 00MZ](https://stacks.math.columbia.edu/tag/00MZ) in the Stacks Project.

**`tag_00MZ`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Homology/FiniteFreeComplex/ReductionModNonzerodivisor.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Homology/FiniteFreeComplex/ReductionModNonzerodivisor.lean#L65).

> Let `R` be a commutative local ring with maximal ideal `m`, and let
> `φ : R^{n (•+1)} → R^{n •}` be a complex of finite free modules ending at position
> `e` (so `n (e+1) = 0`).  If the complex is exact at positions `1, ..., e` and
> `x ∈ m` is a nonzerodivisor of `R`, then the reduced complex `φ mod x` is exact at
> positions `2, ..., e`.

```lean
theorem tag_00MZ (R : Type*) [CommRing R] [IsLocalRing R]
    (e : ℕ) (n : ℕ → ℕ)
    (φ : (i : ℕ) → Matrix (Fin (n i)) (Fin (n (i + 1))) R)
    (hcomplex : IsMatrixComplex n φ)
    (x : R)
    (hxnzd : ∀ r : R, x * r = 0 → r = 0)
    (hexact : ∀ i, i < e → ExactAtSucc n φ i) :
    ∀ i, 1 ≤ i → i < e → ExactAtSucc n (reduceMat x n φ) i
```

## Tag 00N0, a lemma

[Tag 00N0](https://stacks.math.columbia.edu/tag/00N0) in the Stacks Project.

**`Module.one_le_depth_homology_of_forall_le_depth_of_isGreatest_not_exactAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/Acyclicity.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Depth/Acyclicity.lean#L205).

> **Acyclicity lemma.** Let `R` be a Noetherian local ring and let
> `0 → M_e → M_{e-1} → ⋯ → M_0` be a complex of finite `R`-modules, presented as a chain complex
> `C` of `R`-modules with `C.X j = 0` for `j > e`. Assume `depth(M_i) ≥ i` for `i ≤ e`. If `i` is
> the largest index at which `C` fails to be exact and `i > 0`, then
> `Ker(M_i → M_{i-1})/Im(M_{i+1} → M_i)` has depth at least `1`.

```lean
public theorem Module.one_le_depth_homology_of_forall_le_depth_of_isGreatest_not_exactAt
    {R : Type u} [CommRing R] [IsNoetherianRing R] [IsLocalRing R]
    (C : ChainComplex (ModuleCat.{v} R) ℕ) [∀ j, Module.Finite R (C.X j)] (e : ℕ)
    (hC : ∀ j, e < j → IsZero (C.X j))
    (hdepth : ∀ j ≤ e, (j : ℕ∞) ≤ Module.depth R (IsLocalRing.maximalIdeal R) (C.X j))
    {i : ℕ} (hi : IsGreatest {j : ℕ | ¬ C.ExactAt j} i) (hi0 : 0 < i) :
    1 ≤ Module.depth R (IsLocalRing.maximalIdeal R) (C.homology i)
```

## Tag 00N1, a proposition

[Tag 00N1](https://stacks.math.columbia.edu/tag/00N1) in the Stacks Project.

**`LinearMap.injective_and_exact_iff_forall_rank_eq_and_le_depth_minors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Depth/ExactnessCriterion/Converse.lean, line 699](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Depth/ExactnessCriterion/Converse.lean#L699).

> **Buchsbaum–Eisenbud exactness criterion.** A complex
> `0 → R^{n_{e+1}} →[φ e] R^{n_e} → ⋯ → R^{n_1} →[φ 0] R^{n_0}` of finite free modules over a
> local Noetherian ring is exact at `R^{n_{e+1}}, …, R^{n_1}` if and only if, for every `k ≤ e`,
> the rank of `φ k` — the largest `r` with `⋀^r (φ k) ≠ 0` — is the alternating sum
> `n_{k+1} - n_{k+2} + ⋯ ± n_{e+1}`, and the ideal generated by the `r × r` minors of the matrix
> of `φ k` has depth at least `k + 1`, that is, it is `R` or contains a regular sequence of
> length `k + 1`.

```lean
public theorem LinearMap.injective_and_exact_iff_forall_rank_eq_and_le_depth_minors
    {R : Type*} [CommRing R] [IsNoetherianRing R] [IsLocalRing R] (e : ℕ) (n : ℕ → ℕ)
    (φ : ∀ i, (Fin (n (i + 1)) → R) →ₗ[R] (Fin (n i) → R))
    (hφ : ∀ k < e, φ k ∘ₗ φ (k + 1) = 0) :
    (Function.Injective (φ e) ∧ ∀ k < e, Function.Exact (φ (k + 1)) (φ k)) ↔
      ∀ k ≤ e, ∃ r : ℕ,
        (r : ℤ) = ∑ t ∈ Finset.range (e + 1 - k), (-1) ^ t * (n (k + 1 + t) : ℤ) ∧
        IsGreatest {j : ℕ | exteriorPower.map j (φ k) ≠ 0} r ∧
        ((k + 1 : ℕ) : ℕ∞) ≤ Module.depth R (Ideal.span {x : R |
          ∃ (ρ : Fin r → Fin (n k)) (γ : Fin r → Fin (n (k + 1))),
            ((LinearMap.toMatrix' (φ k)).submatrix ρ γ).det = x}) R
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 10.102, Tag 00MR](https://stacks.math.columbia.edu/tag/00MR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
