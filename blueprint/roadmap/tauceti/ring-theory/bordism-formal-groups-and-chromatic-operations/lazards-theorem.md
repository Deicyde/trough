---
declaration: def
origin: cited
lean: TauCeti.LazardRing.mvPolynomialEquiv, TauCeti.LazardRing.adjoin_range_generator, TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff, TauCeti.LazardRing.algebraicIndependent_generator
statement: formalized
---

# Lazard's theorem

the Lazard ring is the polynomial ring `ℤ[x₁, x₂, …]` on the generators
`xₙ = TauCeti.LazardRing.generator n`. The isomorphism is evaluation at the generators.

```lean
TauCeti.LazardRing.mvPolynomialEquiv : MvPolynomial ℕ+ ℤ ≃ₐ[ℤ] TauCeti.LazardRing
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The graded Nakayama lemma for generators](../other-results/part-01/the-graded-nakayama-lemma-for-generators.md)
- [Lazard's computation of the indecomposables of the Lazard ring](lazards-computation-of-the-indecomposables-of-th.md)
- [Nakayama's lemma over `ℤ`](../other-results/part-01/nakayamas-lemma-over-z.md)
- [TauCeti.FormalCoordinate](../formal-laurent-fields-puiseux-expansions-and-con/tauceti-formalcoordinate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.mvPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv).

## Other forms

**Lazard's theorem, generation.** Formalized in Tau Ceti as [`TauCeti.LazardRing.adjoin_range_generator`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.adjoin_range_generator).

```lean
TauCeti.LazardRing.adjoin_range_generator :
  Algebra.adjoin ℤ (Set.range TauCeti.LazardRing.generator) = ⊤
```

**Lazard's theorem, graded.** Formalized in Tau Ceti as [`TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff).

```lean
TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff {p : MvPolynomial ℕ+ ℤ} {n : ℕ} :
  TauCeti.LazardRing.mvPolynomialEquiv p ∈ TauCeti.LazardRing.grading n ↔
    MvPolynomial.IsWeightedHomogeneous (fun k => 2 * ↑k) p n
```

**Lazard's theorem, integral independence.** Formalized in Tau Ceti as [`TauCeti.LazardRing.algebraicIndependent_generator`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Independence.html#TauCeti.LazardRing.algebraicIndependent_generator).

```lean
TauCeti.LazardRing.algebraicIndependent_generator :
  AlgebraicIndependent ℤ TauCeti.LazardRing.generator
```

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.mvPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv)
- [Source of `TauCeti.LazardRing.mvPolynomialEquiv` in TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean#L106)
