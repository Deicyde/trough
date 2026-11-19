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

- [TauCeti.lowerConvexEnvelope](tauceti-lowerconvexenvelope.md)

## Proof depends on

- [Polynomial.newtonPolygon_mul](polynomial-newtonpolygon-mul.md)
- [TauCeti.FiniteSlopeData](tauceti-finiteslopedata.md)
- [Unique existence of the pure slope factorisation](unique-existence-of-the-pure-slope-factorisation.md)

## Lean

Formalized in Tau Ceti as [`Polynomial.splits_of_nodup_newtonSlopes`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.splits_of_nodup_newtonSlopes).

## Sources

- [Tau Ceti documentation: `Polynomial.splits_of_nodup_newtonSlopes`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NewtonPolygon/Factorization.html#Polynomial.splits_of_nodup_newtonSlopes)
- [Source of `Polynomial.splits_of_nodup_newtonSlopes` in TauCeti/NumberTheory/NewtonPolygon/Factorization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NewtonPolygon/Factorization.lean#L533)
