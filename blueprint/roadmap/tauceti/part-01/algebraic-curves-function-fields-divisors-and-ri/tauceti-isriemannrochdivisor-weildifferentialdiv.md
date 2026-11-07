---
declaration: theorem
origin: cited
lean: TauCeti.isRiemannRochDivisor_weilDifferentialDivisor
statement: formalized
proof: formalized
---

# TauCeti.isRiemannRochDivisor\_weilDifferentialDivisor

**The Riemann–Roch theorem** (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself:
the divisor of a nonzero Weil differential is a Riemann–Roch divisor for the genus.

```lean
TauCeti.isRiemannRochDivisor_weilDifferentialDivisor.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)}
  (hmem : ω ∈ TauCeti.weilDifferentialSpace k F) (hω : ω ≠ 0) :
  (TauCeti.weilDifferentialDivisor hF hex hmem hω).IsRiemannRochDivisor (TauCeti.genus k F)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isRiemannRochDivisor_weilDifferentialDivisor`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.isRiemannRochDivisor_weilDifferentialDivisor).

## Sources

- [Tau Ceti documentation: `TauCeti.isRiemannRochDivisor_weilDifferentialDivisor`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.isRiemannRochDivisor_weilDifferentialDivisor)
- [Source of `TauCeti.isRiemannRochDivisor_weilDifferentialDivisor` in TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean#L413)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
