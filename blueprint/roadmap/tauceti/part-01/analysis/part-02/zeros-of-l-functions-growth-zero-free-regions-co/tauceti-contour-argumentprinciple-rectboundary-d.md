---
declaration: theorem
origin: cited
lean: TauCeti.Contour.argumentPrinciple_rectBoundary_divisor
statement: formalized
proof: formalized
---

# TauCeti.Contour.argumentPrinciple_rectBoundary_divisor

The integral of the logarithmic derivative around a rectangle is `2πi` times its signed
divisor count. The ambient meromorphic set need not be open or connected; isolated changes
of representative values on the frontier are allowed. The rectangle may be degenerate.

```lean
TauCeti.Contour.argumentPrinciple_rectBoundary_divisor {f : ℂ → ℂ} {U : Set ℂ} {z w : ℂ}
  (hre : z.re ≤ w.re) (him : z.im ≤ w.im) (hRU : z.Rectangle w ⊆ U) (hf : MeromorphicOn f U)
  (hfr : ∀ x ∈ frontier (z.Rectangle w), meromorphicOrderAt f x = 0) :
  ∫ (t : ℝ) in 0..4, deriv (z.rectBoundary w) t • logDeriv f (z.rectBoundary w t) =
    2 * ↑Real.pi * Complex.I * ↑(TauCeti.divisorCount f U (z.Rectangle w))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The classical residue theorem for a null-homologous contour cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/the-classical-residue-theorem-for-a-null-homolog.md)
- [Fundamental theorem for absolutely continuous curves, integrability](../../../measure-theory/function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)
- [Generalized winding number (HW Def 2.1)](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Piecewise `C¹` on the interval between `a` and `b`](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/piecewise-c1-on-the-interval-between-a-and-b.md)
- [TauCeti.Contour.Cycle](../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/tauceti-contour-cycle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Contour.argumentPrinciple_rectBoundary_divisor`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Argument/Rectangle/Divisor.html#TauCeti.Contour.argumentPrinciple_rectBoundary_divisor).

## Sources

- [Tau Ceti documentation: `TauCeti.Contour.argumentPrinciple_rectBoundary_divisor`](https://taucetiproject.org/docs/TauCeti/Analysis/Contour/Argument/Rectangle/Divisor.html#TauCeti.Contour.argumentPrinciple_rectBoundary_divisor)
- [Source of `TauCeti.Contour.argumentPrinciple_rectBoundary_divisor` in TauCeti/Analysis/Contour/Argument/Rectangle/Divisor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Contour/Argument/Rectangle/Divisor.lean#L83)
- [Tau Ceti roadmap status: Zeros of L-functions — growth, zero-free regions, counting, and the explicit formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZerosOfLFunctions/STATUS.md)
