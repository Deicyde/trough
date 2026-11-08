---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral
statement: formalized
proof: formalized
---

# The prime number theorem for arithmetic progressions

At every nonzero level `m`, the
number of primes of `𝒪 ℚ` whose norms are congruent to an invertible residue `a` modulo `m`
is asymptotic to `Li(x) / φ(m)`.
This is the logarithmic-integral form of equidistribution among the invertible residue classes.

```lean
NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral (m a : ℕ) [NeZero m]
  (ha : IsUnit ↑a) :
  Asymptotics.IsEquivalent Filter.atTop
    (fun x => TauCeti.primeCount ℚ {p | Ideal.absNorm p.asIdeal % m = a % m} x) fun x =>
    1 / ↑m.totient * TauCeti.Real.logIntegral x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Boundary data for the prime Dirichlet series of `S`](../arithmetic-dirichlet-series-and-tauberian-method/boundary-data-for-the-prime-dirichlet-series-of.md)
- [Prime-number-theorem transfer from exact boundary data](../arithmetic-dirichlet-series-and-tauberian-method/prime-number-theorem-transfer-from-exact-boundar.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/PrimesCongruent.html#NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/PrimesCongruent.html#NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral)
- [Source of `NumberField.Chebotarev.primeCount_primesCongruent_isEquivalent_logIntegral` in TauCeti/NumberTheory/Chebotarev/PrimeCounting/PrimesCongruent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/PrimeCounting/PrimesCongruent.lean#L46)
