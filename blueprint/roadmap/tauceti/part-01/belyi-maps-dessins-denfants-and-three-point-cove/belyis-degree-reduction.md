---
declaration: theorem
origin: cited
lean: TauCeti.exists_polynomial_aeval_mem_range
statement: formalized
proof: formalized
---

# Belyi's degree reduction

Every finite set `S` of elements algebraic over a perfect field
`F`, such as a finite subset of `AlgebraicClosure ℚ`, is carried into `F` by a polynomial
`q ∈ F[X]` with `q′ ≠ 0`, in particular nonconstant, whose critical values in every field
extension of `F` also lie in `F`.

```lean
TauCeti.exists_polynomial_aeval_mem_range.{w, u_1, u_2} {F : Type u_1} [Field F] [PerfectField F]
  {K : Type u_2} [Field K] [Algebra F K] {S : Finset K} (hS : ∀ s ∈ S, IsIntegral F s) :
  ∃ q,
    Polynomial.derivative q ≠ 0 ∧
      (∀ s ∈ S, (Polynomial.aeval s) q ∈ Set.range ⇑(algebraMap F K)) ∧
        ∀ (L : Type w) [inst : Field L] [inst_1 : Algebra F L] (x : L),
          (Polynomial.aeval x) (Polynomial.derivative q) = 0 →
            (Polynomial.aeval x) q ∈ Set.range ⇑(algebraMap F L)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_polynomial_aeval_mem_range`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Minpoly/BelyiReduction.html#TauCeti.exists_polynomial_aeval_mem_range).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_polynomial_aeval_mem_range`](https://taucetiproject.org/docs/TauCeti/FieldTheory/Minpoly/BelyiReduction.html#TauCeti.exists_polynomial_aeval_mem_range)
- [Source of `TauCeti.exists_polynomial_aeval_mem_range` in TauCeti/FieldTheory/Minpoly/BelyiReduction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/Minpoly/BelyiReduction.lean#L215)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
