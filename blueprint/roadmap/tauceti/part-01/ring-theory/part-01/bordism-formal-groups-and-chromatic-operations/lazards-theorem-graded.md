---
declaration: theorem
origin: cited
lean: TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff, TauCeti.LazardRing.adjoin_range_generator, TauCeti.LazardRing.algebraicIndependent_generator
statement: formalized
proof: formalized
---

# Lazard's theorem, graded

giving the variable `xₖ` the degree `2k`, the isomorphism
`ℤ[x₁, x₂, …] ≃ₐ[ℤ] L` carries the polynomials that are homogeneous of degree `n` exactly onto
the degree-`n` part `Lₙ` of the Lazard ring.

```lean
TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff {p : MvPolynomial ℕ+ ℤ} {n : ℕ} :
  TauCeti.LazardRing.mvPolynomialEquiv p ∈ TauCeti.LazardRing.grading n ↔
    MvPolynomial.IsWeightedHomogeneous (fun k => 2 * ↑k) p n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The graded Nakayama lemma for generators](../../part-02/other-results/part-01/the-graded-nakayama-lemma-for-generators.md)
- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Informally uses

- [Lazard's theorem](lazards-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff).

## Other forms

**Lazard's theorem, generation.** Formalized in Tau Ceti as [`TauCeti.LazardRing.adjoin_range_generator`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.adjoin_range_generator).

```lean
TauCeti.LazardRing.adjoin_range_generator :
  Algebra.adjoin ℤ (Set.range TauCeti.LazardRing.generator) = ⊤
```

**Lazard's theorem, integral independence.** Formalized in Tau Ceti as [`TauCeti.LazardRing.algebraicIndependent_generator`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Independence.html#TauCeti.LazardRing.algebraicIndependent_generator).

```lean
TauCeti.LazardRing.algebraicIndependent_generator :
  AlgebraicIndependent ℤ TauCeti.LazardRing.generator
```

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff)
- [Source of `TauCeti.LazardRing.mvPolynomialEquiv_mem_grading_iff` in TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean#L145)
