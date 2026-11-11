---
declaration: theorem
origin: cited
lean: TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one
statement: formalized
proof: formalized
---

# An exponent criterion for Schwarz--Christoffel univalence

If the total absolute
turning exponent is at most one, the primitive is injective on the upper half-plane, including
when positive exponents produce reentrant corners. No hypothesis on the boundary curve is
needed.

```lean
TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one.{u_1} {ι : Type u_1} [Fintype ι]
  (a e : ι → ℝ) (z₀ : UpperHalfPlane) (he : ∑ i, |e i| ≤ 1) :
  Set.InjOn (TauCeti.schwarzChristoffelPrimitive a e z₀) UpperHalfPlane.upperHalfPlaneSet
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Noshiro--Warschawski criterion](../../part-02/calculus/part-02/noshiro-warschawski-criterion.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Univalence.html#TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one).

## Sources

- [Tau Ceti documentation: `TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Univalence.html#TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one)
- [Source of `TauCeti.injOn_schwarzChristoffelPrimitive_of_sum_abs_le_one` in TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Univalence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/SchwarzChristoffel/Univalence.lean#L74)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/ConformalMapping/STATUS.md)
