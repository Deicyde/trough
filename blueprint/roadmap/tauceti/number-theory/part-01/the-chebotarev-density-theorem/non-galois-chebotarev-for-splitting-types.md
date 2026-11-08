---
declaration: theorem
origin: cited
lean: NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq
statement: formalized
proof: formalized
---

# Non-Galois Chebotarev for splitting types

The primes with residue-degree multiset `μ`
in `E` have density the total proportion of elements whose action on `Gal(L/K) ⧸ Gal(L/E)`
has full cycle type `μ`, expressed as a sum of conjugacy-class proportions. No normality of
`E/K` or realizability hypothesis on `μ` is needed.

```lean
NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq.{u_1, u_2} (K : Type u_1)
  (L : Type u_2) [Field K] [NumberField K] [Field L] [NumberField L] [Algebra K L] [IsGalois K L]
  (E : IntermediateField K L) (μ : Multiset ℕ) :
  NumberField.Set.HasDirichletDensity
    {𝔭 | Multiset.map (fun P => (↑P).inertiaDeg (NumberField.RingOfIntegers K)) Finset.univ.val = μ}
    (∑ C with (MulAction.toPerm (Quotient.out C)).fullCycleType = μ,
      ↑(Nat.card ↑C.carrier) / ↑(Nat.card Gal(L/K)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The analytic Euler product](../arithmetic-dirichlet-series-and-tauberian-method/part-01/the-analytic-euler-product.md)
- [The Chebotarev density theorem](the-chebotarev-density-theorem.md)
- [The primes of `K` with Artin class `C` in `L`](the-primes-of-k-with-artin-class-c-in-l.md)

## Lean

Formalized in Tau Ceti as [`NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/SplittingType.html#NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq).

## Sources

- [Tau Ceti documentation: `NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Chebotarev/Density/SplittingType.html#NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq)
- [Source of `NumberField.Chebotarev.hasDirichletDensity_setOf_map_inertiaDeg_eq` in TauCeti/NumberTheory/Chebotarev/Density/SplittingType.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Chebotarev/Density/SplittingType.lean#L95)
- [Tau Ceti roadmap status: The Chebotarev density theorem](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/Chebotarev/STATUS.md)
