---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt
statement: formalized
proof: formalized
---

# The Riesz identity at a good zero

Let `u` be row compact, put `C = 1 - a • u`, and
suppose `ΔʲH_u(a) = 0` for `j < h` while `c = ΔʰH_u(a)` is a unit, so that `a` is a good zero
of order `h` of the Fredholm determinant. Then `b = c⁻¹ • ΔʰV(a)` satisfies
`C ^ (h + 1) b = C ^ h`, that is, `C ^ h (C b - 1) = 0`. This is the identity from which the
Riesz projector `1 - (C b) ^ h` at `a` and its complementary projector `(C b) ^ h` are built.

```lean
ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt.{u_1,
    u_2}
  {I : Type u_1} {R : Type u_2} [TopologicalSpace I] [DiscreteTopology I] [DecidableEq I]
  [NormedCommRing R] [TauCeti.NormedRing.IsTate R] [IsUltrametricDist R] [CompleteSpace R]
  {u : ZeroAtInftyContinuousMap I R →L[R] ZeroAtInftyContinuousMap I R} (hu : u.IsRowCompact)
  {a : R} {h : ℕ}
  (hH : ∀ j < h, ((PowerSeries.hasseDeriv j) u.matrixCoeff.charPowerSeries).evalAt a = 0)
  (hc : IsUnit (((PowerSeries.hasseDeriv h) u.matrixCoeff.charPowerSeries).evalAt a)) :
  (1 - a • u) ^ (h + 1) *
      Ring.inverse (((PowerSeries.hasseDeriv h) u.matrixCoeff.charPowerSeries).evalAt a) •
        u.resolventHasseDerivAt h a =
    (1 - a • u) ^ h
```

## Depends on

- [ContinuousLinearMap.IsRowCompact](continuouslinearmap-isrowcompact.md)

## Proof depends on

- [The Fredholm determinant is entire](the-fredholm-determinant-is-entire.md)

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.html#ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.html#ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt)
- [Source of `ContinuousLinearMap.IsRowCompact.one_sub_smul_pow_succ_mul_inverse_smul_resolventHasseDerivAt` in TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Normed/Operator/Nonarchimedean/Resolvent.lean#L588)
