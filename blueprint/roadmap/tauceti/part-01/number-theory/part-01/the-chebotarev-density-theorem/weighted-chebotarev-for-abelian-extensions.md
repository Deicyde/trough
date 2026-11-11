---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm
statement: formalized
proof: formalized
---

# Weighted Chebotarev for abelian extensions

If `Gal(L/K)` is abelian, then for every
`σ ∈ Gal(L/K)` the Frobenius `ψ` function of `σ` satisfies `ψ_σ(x) = x / #Gal(L/K) + o(x)`.

```lean
NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm.{u_1, u_2} {K : Type u_1} {L : Type u_2}
  [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (hab : ∀ (σ τ : Gal(L/K)), σ * τ = τ * σ) (σ : Gal(L/K)) :
  (fun x =>
      NumberField.Chebotarev.frobeniusPsi K L (ConjClasses.mk σ) x -
        1 / ↑(Nat.card Gal(L/K)) * x) =o[Filter.atTop]
    fun x => x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic Euler product](../arithmetic-dirichlet-series-and-tauberian-method/the-analytic-euler-product.md)
- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [The continued L-function of a unitary weight, defined by partial summation](../arithmetic-dirichlet-series-and-tauberian-method/the-continued-l-function-of-a-unitary-weight-def.md)
- [The crossing constant](the-crossing-constant.md)
- [The Dedekind zeta function has no zeros on the line `Re s = 1` away from its pole](../arithmetic-dirichlet-series-and-tauberian-method/the-dedekind-zeta-function-has-no-zeros-on-the-l.md)
- [Euler's product formula for the elements of order divisible by `f`](../../../group-theory/other-results/eulers-product-formula-for-the-elements-of-order.md)
- [The fixed-field Frobenius fiber count](the-fixed-field-frobenius-fiber-count.md)
- [The ideal-theoretic Artin map](../../part-02/number-fields-ramification-frobenius-and-the-lmf/the-ideal-theoretic-artin-map.md)
- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)
- [The Wiener--Ikehara theorem](../arithmetic-dirichlet-series-and-tauberian-method/the-wiener-ikehara-theorem.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.html#NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.html#NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm)
- [Source of `NumberField.Chebotarev.frobeniusPsi_asymptotic_of_mul_comm` in TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Chebotarev/PrimeCounting/Chebotarev.lean#L178)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/Chebotarev/STATUS.md)
