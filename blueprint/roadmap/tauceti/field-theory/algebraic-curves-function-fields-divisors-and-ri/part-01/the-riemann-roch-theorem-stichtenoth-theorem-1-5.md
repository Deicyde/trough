---
declaration: theorem
origin: cited
lean: TauCeti.isRiemannRochDivisor_weilDifferentialDivisor, TauCeti.isRiemannRochDivisor_of_isGreatest_mem_weilDifferentialFiltration, TauCeti.exists_isRiemannRochDivisor
statement: formalized
proof: formalized
---

# The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself

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

## Proof depends on

- [The duality theorem, in dimensions](the-duality-theorem-in-dimensions.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isRiemannRochDivisor_weilDifferentialDivisor`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.isRiemannRochDivisor_weilDifferentialDivisor).

## Other forms

**The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15).** Formalized in Tau Ceti as [`TauCeti.isRiemannRochDivisor_of_isGreatest_mem_weilDifferentialFiltration`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.isRiemannRochDivisor_of_isGreatest_mem_weilDifferentialFiltration).

```lean
TauCeti.isRiemannRochDivisor_of_isGreatest_mem_weilDifferentialFiltration.{u_1, u_2} {k : Type u_1}
  {F : Type u_2} [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)} (hω : ω ≠ 0)
  {W : TauCeti.Divisor k F} (hW : IsGreatest {D | ω ∈ TauCeti.weilDifferentialFiltration D} W) :
  W.IsRiemannRochDivisor (TauCeti.genus k F)
```

**The Riemann–Roch theorem, existence form (Stichtenoth, Theorem 1.5.15).** Formalized in Tau Ceti as [`TauCeti.exists_isRiemannRochDivisor`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.exists_isRiemannRochDivisor).

```lean
TauCeti.exists_isRiemannRochDivisor.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k] [Field F]
  [Algebra k F] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F) :
  ∃ W, W.IsRiemannRochDivisor (TauCeti.genus k F)
```

## Sources

- [Tau Ceti documentation: `TauCeti.isRiemannRochDivisor_weilDifferentialDivisor`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.isRiemannRochDivisor_weilDifferentialDivisor)
- [Source of `TauCeti.isRiemannRochDivisor_weilDifferentialDivisor` in TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean#L413)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
