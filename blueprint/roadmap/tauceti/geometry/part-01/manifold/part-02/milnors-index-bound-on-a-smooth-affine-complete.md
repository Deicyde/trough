---
declaration: theorem
origin: cited
lean: TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le
statement: formalized
proof: formalized
---

# Milnor's index bound on a smooth affine complete intersection

On the common zero set in
`ℂ^σ` of a polynomial family with surjective Jacobian at every common zero, every critical point of
the Euclidean squared distance from a point `a` has real Morse index at most the complex dimension
`|σ| - |ι|` of the zero set.

```lean
TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le.{u_1, u_2} {σ : Type u_1}
  {ι : Type u_2} [Fintype σ] [Fintype ι] {p : ι → MvPolynomial σ ℂ}
  (hp : ∀ x ∈ TauCeti.affineZeroLocus p, Function.Surjective (TauCeti.jacobiMatrixAt p x).mulVec)
  (a : EuclideanSpace ℂ σ) (x : ↑(TauCeti.affineZeroLocus p))
  (hcrit : (d% fun y => ‖WithLp.toLp 2 ↑y - a‖ ^ 2) x = 0) :
  TauCeti.manifoldMorseIndex (modelWithCornersSelf ℝ (Fin (Fintype.card σ - Fintype.card ι) → ℂ))
      (fun y => ‖WithLp.toLp 2 ↑y - a‖ ^ 2) x ≤
    Fintype.card σ - Fintype.card ι
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The index bound for strongly `q`-pseudoconvex functions on a complex manifold](../../../../analysis/part-01/complex-morse-theory-affine-topology-and-weak-le/the-index-bound-for-strongly-q-pseudoconvex-func.md)
- [TauCeti.leviForm](../../../../analysis/part-01/complex-morse-theory-affine-topology-and-weak-le/tauceti-leviform.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/Polynomial.html#TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le).

## Sources

- [Tau Ceti documentation: `TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/RegularValue/Polynomial.html#TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le)
- [Source of `TauCeti.manifoldMorseIndex_norm_sq_sub_toLp_affineZeroLocus_le` in TauCeti/Geometry/Manifold/RegularValue/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/RegularValue/Polynomial.lean#L193)
