---
declaration: theorem
origin: cited
lean: TauCeti.CircleSobolev.norm_mul_le
statement: formalized
proof: formalized
---

# The product estimate in `H^s(A)`, `s > 1/2`

```lean
TauCeti.CircleSobolev.norm_mul_le.{u_4} {s : ℝ} {A : Type u_4} [NormedRing A] [NormedAlgebra ℂ A]
  [CompleteSpace A] [hs : Fact (1 / 2 < s)] (a b : TauCeti.CircleSobolev s A) :
  ‖a * b‖ ≤ 2 ^ (s + 1) * √(∑' (n : ℤ), TauCeti.CircleSobolev.weight (-(2 * s)) n) * ‖a‖ * ‖b‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality for unconditional sums in `ℝ≥0∞`](../../analysis/part-02/other-results/holders-inequality-for-unconditional-sums-in-r0.md)
- [Young's inequality](../../analysis/part-02/normed/part-02/youngs-inequality.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.CircleSobolev.norm_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Algebra.html#TauCeti.CircleSobolev.norm_mul_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CircleSobolev.norm_mul_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Sobolev/Circle/Algebra.html#TauCeti.CircleSobolev.norm_mul_le)
- [Source of `TauCeti.CircleSobolev.norm_mul_le` in TauCeti/Analysis/Sobolev/Circle/Algebra.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Sobolev/Circle/Algebra.lean#L287)
- [Tau Ceti roadmap status: Analytic families and moduli of complex curves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexCurveModuli/STATUS.md)
