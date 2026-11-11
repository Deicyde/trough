---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.fixedField_frobenius_fiber_card
statement: formalized
proof: formalized
---

# The fixed-field Frobenius fiber count

Let `sigma` represent the conjugacy class `C`, and
let `p` be an unramified prime with Artin class `C`.  The number of primes of
`L ^ <sigma>` above `p` whose relative Artin class in `L / L ^ <sigma>` is represented by
`sigma.toFixedFieldAlgEquiv` is

```text
#Gal(L/K) / (#C * orderOf sigma).
```

The division is exact by `ConjClasses.card_carrier_mul_orderOf_dvd`.

```lean
NumberField.Chebotarev.fixedField_frobenius_fiber_card.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) (sigma : Gal(L/K)) (hsigma : sigma ∈ C.carrier)
  (p : IsDedekindDomain.HeightOneSpectrum (NumberField.RingOfIntegers K))
  (hp : p ∈ NumberField.Chebotarev.frobeniusPrimeSet K L C) :
  Nat.card
      { P //
        IsDedekindDomain.HeightOneSpectrum.under (NumberField.RingOfIntegers K) P = p ∧
          P ∈
            NumberField.Chebotarev.frobeniusPrimeSet
              (↥(IntermediateField.fixedField (Subgroup.zpowers sigma))) L
              (ConjClasses.mk sigma.toFixedFieldAlgEquiv) } =
    Nat.card Gal(L/K) / (Nat.card ↑C.carrier * orderOf sigma)
```

## Depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.fixedField_frobenius_fiber_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/FixedField/FiberCount.html#NumberField.Chebotarev.fixedField_frobenius_fiber_card).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.fixedField_frobenius_fiber_card`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/FixedField/FiberCount.html#NumberField.Chebotarev.fixedField_frobenius_fiber_card)
- [Source of `NumberField.Chebotarev.fixedField_frobenius_fiber_card` in TauCeti/NumberTheory/Chebotarev/FixedField/FiberCount.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Chebotarev/FixedField/FiberCount.lean#L405)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Chebotarev/STATUS.md)
