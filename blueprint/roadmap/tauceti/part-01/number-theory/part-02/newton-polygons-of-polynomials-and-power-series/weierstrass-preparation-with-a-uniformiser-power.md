---
declaration: theorem
origin: cited
lean: PowerSeries.exists_pow_mul_distinguished_mul_unit
statement: formalized
proof: formalized
---

# Weierstrass preparation with a uniformiser power

Over a discrete valuation ring complete
for its maximal ideal, a nonzero power series `f` factors as `C (π ^ μ(f)) * u * P` with `u` a
unit and `P` a distinguished polynomial of degree `λ(f)`.

```lean
PowerSeries.exists_pow_mul_distinguished_mul_unit.{u_1} {O : Type u_1} [CommRing O] [IsDomain O]
  [IsDiscreteValuationRing O] [IsAdicComplete (IsLocalRing.maximalIdeal O) O] {π : O}
  (hπ : Irreducible π) {f : PowerSeries O} (hf : f ≠ 0) :
  ∃ m P u,
    f.muInvariant = ↑m ∧
      P.natDegree = f.lambdaInvariant ∧
        P.IsDistinguishedAt (IsLocalRing.maximalIdeal O) ∧ f = PowerSeries.C (π ^ m) * ↑u * ↑P
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`PowerSeries.exists_pow_mul_distinguished_mul_unit`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscreteValuationRing.html#PowerSeries.exists_pow_mul_distinguished_mul_unit).

## Sources

- [Tau Ceti documentation: `PowerSeries.exists_pow_mul_distinguished_mul_unit`](https://taucetiproject.org/docs/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscreteValuationRing.html#PowerSeries.exists_pow_mul_distinguished_mul_unit)
- [Source of `PowerSeries.exists_pow_mul_distinguished_mul_unit` in TauCeti/RingTheory/PowerSeries/Weierstrass/DiscreteValuationRing.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/PowerSeries/Weierstrass/DiscreteValuationRing.lean#L229)
- [Tau Ceti roadmap status: Newton polygons of polynomials and power series](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NewtonPolygons/STATUS.md)
