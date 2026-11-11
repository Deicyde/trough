---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet, NumberField.Chebotarev.frobeniusPsi_asymptotic, NumberField.Chebotarev.tendsto_frobeniusPsi
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
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [The continued L-function of a unitary weight, defined by partial summation](../arithmetic-dirichlet-series-and-tauberian-method/the-continued-l-function-of-a-unitary-weight-def.md)
- [The crossing constant](the-crossing-constant.md)
- [Euler's product formula for the elements of order divisible by `f`](../../../group-theory/other-results/eulers-product-formula-for-the-elements-of-order.md)
- [The fixed-field Frobenius fiber count](the-fixed-field-frobenius-fiber-count.md)
- [The ideal-theoretic Artin map](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-ideal-theoretic-artin-map.md)
- [Weighted Chebotarev for abelian extensions](weighted-chebotarev-for-abelian-extensions.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.html#NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet).

## Other forms

**The Chebotarev density theorem, for Chebyshev's `ψ`.** Formalized in Tau Ceti as [`NumberField.Chebotarev.frobeniusPsi_asymptotic`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.html#NumberField.Chebotarev.frobeniusPsi_asymptotic).

```lean
NumberField.Chebotarev.frobeniusPsi_asymptotic.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) :
  (fun x =>
      NumberField.Chebotarev.frobeniusPsi K L C x -
        ↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K)) * x) =o[Filter.atTop]
    fun x => x
```

**The Chebotarev density theorem, for Chebyshev's `ψ`, as a limit.** Formalized in Tau Ceti as [`NumberField.Chebotarev.tendsto_frobeniusPsi`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.html#NumberField.Chebotarev.tendsto_frobeniusPsi).

```lean
NumberField.Chebotarev.tendsto_frobeniusPsi.{u_1, u_2} (K : Type u_1) (L : Type u_2) [Field K]
  [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (C : ConjClasses Gal(L/K)) :
  Filter.Tendsto (fun x => NumberField.Chebotarev.frobeniusPsi K L C x / x) Filter.atTop
    (nhds (↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K))))
```

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.html#NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet)
- [Source of `NumberField.Chebotarev.hasDirichletDensity_frobeniusPrimeSet` in TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Chebotarev/Density/Chebotarev.lean#L48)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Chebotarev/STATUS.md)
