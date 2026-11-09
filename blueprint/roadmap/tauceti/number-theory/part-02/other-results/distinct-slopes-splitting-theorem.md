---
declaration: theorem
origin: cited
lean: Polynomial.splits_of_nodup_newtonSlopes
statement: formalized
proof: formalized
---

# Distinct-slopes splitting theorem

Over a complete ultrametric normed field, any polynomial
whose finite Newton slopes have multiplicity one splits into linear factors over the base field.

```lean
Polynomial.splits_of_nodup_newtonSlopes.{u_1} {K : Type u_1} [NormedField K] [IsUltrametricDist K]
  [CompleteSpace K] (v : AddValuation K (WithTop ℝ)) {b : ℝ} (hb : 1 < b)
  (hv : ∀ (x : K), x ≠ 0 → ‖x‖ = b ^ (-(v x).untop₀)) {f : Polynomial K}
  (hf : (f.newtonSlopes v).Nodup) : f.Splits
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Weierstrass division estimate (Bosch–Güntzer–Remmert §5.2.1, Theorem 2)](../../../ring-theory/part-01/p-adic-measures-completed-group-algebras-and-cha/part-01/the-weierstrass-division-estimate-bosch-guntzer.md)
- [Weierstrass preparation](../../../ring-theory/part-01/p-adic-measures-completed-group-algebras-and-cha/part-01/weierstrass-preparation.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.splits_of_nodup_newtonSlopes`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.splits_of_nodup_newtonSlopes).

## Sources

- [Tau Ceti documentation: `Polynomial.splits_of_nodup_newtonSlopes`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.splits_of_nodup_newtonSlopes)
- [Source of `Polynomial.splits_of_nodup_newtonSlopes` in TauCeti/NumberTheory/NewtonPolygon/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NewtonPolygon/Factorization.lean#L533)
