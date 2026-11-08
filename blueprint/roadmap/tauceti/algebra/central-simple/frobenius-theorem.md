---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_algEquiv_real_or_quaternion
statement: formalized
proof: formalized
---

# Frobenius' theorem

A finite-dimensional division algebra over `ℝ` with centre `ℝ` is
`ℝ`-isomorphic either to `ℝ` or to the Hamilton quaternions `ℍ[ℝ]`.

This is the classification to use when nothing is known about `D` beyond the hypotheses. If
`finrank ℝ D = 4` is already in hand, `TauCeti.nonempty_algEquiv_quaternion_of_finrank_eq_four`
gives the quaternion isomorphism directly, with no disjunction to discharge.

```lean
TauCeti.nonempty_algEquiv_real_or_quaternion.{u_1} (D : Type u_1) [DivisionRing D] [Algebra ℝ D]
  [Algebra.IsCentral ℝ D] [FiniteDimensional ℝ D] :
  Nonempty (D ≃ₐ[ℝ] ℝ) ∨ Nonempty (D ≃ₐ[ℝ] Quaternion ℝ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Artin--Wedderburn over a separably closed field](artin-wedderburn-over-a-separably-closed-field.md)
- [The dimension count behind the centralizer theorem, asking only for what it uses](the-dimension-count-behind-the-centralizer-theor.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_algEquiv_real_or_quaternion`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Real.html#TauCeti.nonempty_algEquiv_real_or_quaternion).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_algEquiv_real_or_quaternion`](https://taucetiproject.org/docs/TauCeti/Algebra/CentralSimple/Real.html#TauCeti.nonempty_algEquiv_real_or_quaternion)
- [Source of `TauCeti.nonempty_algEquiv_real_or_quaternion` in TauCeti/Algebra/CentralSimple/Real.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/CentralSimple/Real.lean#L368)
