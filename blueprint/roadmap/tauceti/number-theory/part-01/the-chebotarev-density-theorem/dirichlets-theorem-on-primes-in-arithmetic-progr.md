---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasDirichletDensity_primesCongruent
statement: formalized
proof: formalized
---

# Dirichlet's theorem on primes in arithmetic progressions, with Dirichlet density

For
`m ≠ 0` and `a` a unit modulo `m`, the primes of `𝓞 ℚ` whose absolute norm is congruent to `a`
modulo `m` have Dirichlet density `1 / φ(m)`.

```lean
NumberField.Chebotarev.hasDirichletDensity_primesCongruent (m a : ℕ) [NeZero m] (ha : IsUnit ↑a) :
  NumberField.Set.HasDirichletDensity {𝔭 | Ideal.absNorm 𝔭.asIdeal % m = a % m} (1 / ↑m.totient)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A one-sided Abel bound](../../part-02/arithmetic-dirichlet-series/a-one-sided-abel-bound.md)
- [The analytic Euler product](../arithmetic-dirichlet-series-and-tauberian-method/the-analytic-euler-product.md)
- [Boundary data for the prime Dirichlet series of `S`](../arithmetic-dirichlet-series-and-tauberian-method/boundary-data-for-the-prime-dirichlet-series-of.md)
- [The prime ideal theorem](../arithmetic-dirichlet-series-and-tauberian-method/the-prime-ideal-theorem.md)
- [Prime-number-theorem transfer from exact boundary data](../arithmetic-dirichlet-series-and-tauberian-method/prime-number-theorem-transfer-from-exact-boundar.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasDirichletDensity_primesCongruent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.html#NumberField.Chebotarev.hasDirichletDensity_primesCongruent).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasDirichletDensity_primesCongruent`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.html#NumberField.Chebotarev.hasDirichletDensity_primesCongruent)
- [Source of `NumberField.Chebotarev.hasDirichletDensity_primesCongruent` in TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Density/PrimesCongruent.lean#L116)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
