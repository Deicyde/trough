---
declaration: theorem
origin: cited
lean: TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration, TauCeti.riemannRochSpaceEquivWeilDifferentialFiltration
statement: formalized
proof: formalized
---

# The duality theorem, in dimensions

`ℓ(W - D) = dim_k Ω_F(D)`.

```lean
TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)} (hω : ω ≠ 0)
  {W : TauCeti.Divisor k F} (hW : IsGreatest {D | ω ∈ TauCeti.weilDifferentialFiltration D} W)
  (D : TauCeti.Divisor k F) : (W - D).dim = Module.finrank k ↥(TauCeti.weilDifferentialFiltration D)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Riemann's theorem](riemanns-theorem.md)
- [The weak approximation theorem](../function-field/part-01/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration).

## Other forms

**The duality theorem (Stichtenoth, Theorem 1.5.14).** Formalized in Tau Ceti as [`TauCeti.riemannRochSpaceEquivWeilDifferentialFiltration`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.riemannRochSpaceEquivWeilDifferentialFiltration).

```lean
TauCeti.riemannRochSpaceEquivWeilDifferentialFiltration.{u_1, u_2} {k : Type u_1} {F : Type u_2}
  [Field k] [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F)
  (hex : IsIntegrallyClosedIn k F) {ω : Module.Dual k ↥(TauCeti.repartitionSpace k F)} (hω : ω ≠ 0)
  {W : TauCeti.Divisor k F} (hW : IsGreatest {D | ω ∈ TauCeti.weilDifferentialFiltration D} W)
  (D : TauCeti.Divisor k F) :
  ↥(TauCeti.riemannRochSpace (W - D)) ≃ₗ[k] ↥(TauCeti.weilDifferentialFiltration D)
```

## Sources

- [Tau Ceti documentation: `TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.html#TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration)
- [Source of `TauCeti.dim_sub_eq_finrank_weilDifferentialFiltration` in TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Differential/CanonicalDivisor.lean#L387)
