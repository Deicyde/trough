---
declaration: theorem
origin: cited
lean: OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq, Orthonormal.norm_starProjection_sq_eq_sum, HilbertBasis.hasSum_norm_diagonalPMap_apply_sq, HilbertBasis.tsum_enorm_sq_inner, HilbertBasis.hasSum_norm_sq_inner, HilbertBasis.tsum_norm_sq_inner
statement: formalized
proof: formalized
---

# Parseval's identity for a functional

The squared values of a continuous linear functional
on a finite orthonormal basis sum to the square of its operator norm: by the Riesz representation,
they are the squared coordinates of the representing vector.

```lean
OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2}
  {E : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι]
  (b : OrthonormalBasis ι 𝕜 E) (A : E →L[𝕜] 𝕜) : ∑ i, ‖A (b i)‖ ^ 2 = ‖A‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq).

## Other forms

**Parseval's identity on the span `U` of a finite orthonormal family.** Formalized in Tau Ceti as [`Orthonormal.norm_starProjection_sq_eq_sum`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Orthonormal/Family.html#Orthonormal.norm_starProjection_sq_eq_sum).

```lean
Orthonormal.norm_starProjection_sq_eq_sum.{u_1, u_2, u_3} {𝕜 : Type u_1} {E : Type u_2}
  {ι : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [Fintype ι] {v : ι → E}
  (hv : Orthonormal 𝕜 v) {U : Submodule 𝕜 E} [U.HasOrthogonalProjection]
  (hU : Submodule.span 𝕜 (Set.range v) = U) (x : E) :
  ‖U.starProjection x‖ ^ 2 = ∑ i, ‖inner 𝕜 (v i) x‖ ^ 2
```

**Parseval's identity for a diagonal operator.** Formalized in Tau Ceti as [`HilbertBasis.hasSum_norm_diagonalPMap_apply_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/LinearPMap/Diagonal.html#HilbertBasis.hasSum_norm_diagonalPMap_apply_sq).

```lean
HilbertBasis.hasSum_norm_diagonalPMap_apply_sq.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2}
  {E : Type u_3} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E)
  (c : ι → 𝕜) (x : ↥(b.diagonalPMap c).domain) :
  HasSum (fun i => ‖c i * inner 𝕜 (b i) ↑x‖ ^ 2) (‖↑(b.diagonalPMap c) x‖ ^ 2)
```

**Parseval's identity, extended-nonnegative form.** Formalized in Tau Ceti as [`HilbertBasis.tsum_enorm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.tsum_enorm_sq_inner).

```lean
HilbertBasis.tsum_enorm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  ∑' (i : ι), ‖inner 𝕜 (b i) x‖ₑ ^ 2 = ‖x‖ₑ ^ 2
```

**Parseval's identity, norm-square form.** Formalized in Tau Ceti as [`HilbertBasis.hasSum_norm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.hasSum_norm_sq_inner).

```lean
HilbertBasis.hasSum_norm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  HasSum (fun i => ‖inner 𝕜 (b i) x‖ ^ 2) (‖x‖ ^ 2)
```

**Parseval's identity, norm-square form (`tsum` version of `HilbertBasis.hasSum_norm_sq_inner`).** Formalized in Tau Ceti as [`HilbertBasis.tsum_norm_sq_inner`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#HilbertBasis.tsum_norm_sq_inner).

```lean
HilbertBasis.tsum_norm_sq_inner.{u_1, u_2, u_3} {ι : Type u_1} {𝕜 : Type u_2} {E : Type u_3}
  [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] (b : HilbertBasis ι 𝕜 E) (x : E) :
  ∑' (i : ι), ‖inner 𝕜 (b i) x‖ ^ 2 = ‖x‖ ^ 2
```

## Sources

- [Tau Ceti documentation: `OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Parseval.html#OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq)
- [Source of `OrthonormalBasis.sum_sq_norm_apply_eq_norm_sq` in TauCeti/Analysis/InnerProductSpace/Parseval.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Parseval.lean#L72)
