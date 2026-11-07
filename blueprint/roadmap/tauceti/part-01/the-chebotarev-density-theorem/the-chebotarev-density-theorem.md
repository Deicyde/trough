---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet
statement: formalized
proof: formalized
---

# The Chebotarev density theorem

For a finite Galois extension `L / K` of number fields
and a conjugacy class `C` of `Gal(L/K)`, the primes of `𝓞 K` whose Frobenius in `L` lies in `C`
have Dirichlet density `#C / #Gal(L/K)`.

```lean
NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) :
  NumberField.Set.HasDirichletDensity (NumberField.Chebotarev.frobeniusPrimeSet K L C)
    (↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K)))
```

## Depends on

- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)

## Proof depends on

- [The analytic Euler product](../arithmetic-dirichlet-series-and-tauberian-method/the-analytic-euler-product.md)
- [The crossing constant](the-crossing-constant.md)
- [The crossing constant approaches `1 / #Aut_K(L)`](the-crossing-constant-approaches-1-aut-k-l.md)
- [The fixed-field Frobenius fiber count](the-fixed-field-frobenius-fiber-count.md)
- [The ideal-theoretic Artin map](../../part-05/number-fields-ramification-frobenius-and-the-lmf/the-ideal-theoretic-artin-map.md)
- [TauCeti.continuedLFunctionOfWeight](../arithmetic-dirichlet-series-and-tauberian-method/tauceti-continuedlfunctionofweight.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.html#NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.html#NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet)
- [Source of `NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet` in TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.lean#L48)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
