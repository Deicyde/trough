---
declaration: theorem
origin: cited
lean: TauCeti.Divisor.two_mul_dim_le_degree_add_two
statement: formalized
proof: formalized
---

# Clifford's theorem (Stichtenoth, Theorem 1.6.13), over an arbitrary exact field of constants

a divisor of degree between `0` and `2g - 2` satisfies

`2 * ℓ(D) ≤ deg D + 2`.

The bound includes the nonspecial and empty-linear-system edge cases.

```lean
TauCeti.Divisor.two_mul_dim_le_degree_add_two.{u_1, u_2} {k : Type u_1} {F : Type u_2} [Field k]
  [Field F] [Algebra k F] (hF : TauCeti.IsFunctionField k F) (hex : IsIntegrallyClosedIn k F)
  {D : TauCeti.Divisor k F} (hDnonneg : 0 ≤ TauCeti.Divisor.degree D)
  (hDle : TauCeti.Divisor.degree D ≤ 2 * ↑(TauCeti.genus k F) - 2) :
  2 * ↑D.dim ≤ TauCeti.Divisor.degree D + 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The fundamental inequality (Stichtenoth, Theorem 3.1.11)](../algebraic-curves-function-fields-divisors-and-ri/part-01/the-fundamental-inequality-stichtenoth-theorem-3.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/part-01/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Divisor.two_mul_dim_le_degree_add_two`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Clifford.html#TauCeti.Divisor.two_mul_dim_le_degree_add_two).

## Sources

- [Tau Ceti documentation: `TauCeti.Divisor.two_mul_dim_le_degree_add_two`](https://taucetiproject.org/docs/TauCeti/FieldTheory/FunctionField/Consequences/Clifford.html#TauCeti.Divisor.two_mul_dim_le_degree_add_two)
- [Source of `TauCeti.Divisor.two_mul_dim_le_degree_add_two` in TauCeti/FieldTheory/FunctionField/Consequences/Clifford.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/FunctionField/Consequences/Clifford.lean#L311)
