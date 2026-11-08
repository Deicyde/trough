---
declaration: theorem
origin: cited
lean: TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow
statement: formalized
proof: formalized
---

# High powers of a transcendental function have pole divisors whose section ring is generated in degree one

over an exact constant field, if `z` is transcendental over `k`, `e ≥ 1` and
`e ≥ 2g`, then every section of `n (zᵉ)∞` is a sum of products of `n` sections of `(zᵉ)∞`.

```lean
TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  {z : Fˣ} (hz : Transcendental k ↑z) {e : ℕ} (he₀ : 0 < e) (he : 2 * TauCeti.genus k F ≤ e)
  (n : ℕ) :
  TauCeti.riemannRochSpace (n • TauCeti.Divisor.poles hF (z ^ e)) ≤
    TauCeti.riemannRochSpace (TauCeti.Divisor.poles hF (z ^ e)) ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [TauCeti.Divisor.sectionRing](tauceti-divisor-sectionring.md)
- [The weak approximation theorem](../function-field/part-01/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Pencil.html#TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow).

## Sources

- [Tau Ceti documentation: `TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/RiemannRoch/Pencil.html#TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow)
- [Source of `TauCeti.riemannRochSpace_nsmul_poles_pow_le_pow` in TauCeti/FieldTheory/FunctionField/RiemannRoch/Pencil.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/RiemannRoch/Pencil.lean#L206)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
