---
declaration: theorem
origin: cited
lean: TauCeti.exists_polynomial_aeval_mem_criticalValues_subset
statement: formalized
proof: formalized
---

# Polynomial Belyification of algebraic numbers

Every finite set `S` of elements algebraic
over `ℚ` in a field `K`, such as a finite subset of `AlgebraicClosure ℚ`, is carried into
`{0, 1}` by a nonconstant polynomial `q` with rational coefficients whose critical values, in
every field of characteristic zero, lie in `{0, 1}`.

```lean
TauCeti.exists_polynomial_aeval_mem_criticalValues_subset.{u, u_1} {K : Type u_1} [Field K]
  [Algebra ℚ K] {S : Finset K} (hS : ∀ s ∈ S, IsIntegral ℚ s) :
  ∃ q,
    0 < q.natDegree ∧
      (∀ s ∈ S, (Polynomial.aeval s) q ∈ {0, 1}) ∧
        ∀ (L : Type u) [inst : Field L] [inst_1 : Algebra ℚ L],
          Polynomial.criticalValues L q ⊆ {0, 1}
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Belyi's degree reduction](belyis-degree-reduction.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_polynomial_aeval_mem_criticalValues_subset`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Belyi.html#TauCeti.exists_polynomial_aeval_mem_criticalValues_subset).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_polynomial_aeval_mem_criticalValues_subset`](https://taucetiproject.org/docs/TauCeti/Algebra/Polynomial/Belyi.html#TauCeti.exists_polynomial_aeval_mem_criticalValues_subset)
- [Source of `TauCeti.exists_polynomial_aeval_mem_criticalValues_subset` in TauCeti/Algebra/Polynomial/Belyi.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/Polynomial/Belyi.lean#L310)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
