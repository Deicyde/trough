---
declaration: def
origin: cited
lean: TauCeti.LazardRing.mvPolynomialEquiv
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

- [Lazard's theorem, graded](lazards-theorem-graded.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LazardRing.mvPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.LazardRing.mvPolynomialEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.html#TauCeti.LazardRing.mvPolynomialEquiv)
- [Source of `TauCeti.LazardRing.mvPolynomialEquiv` in TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/LazardRing/Polynomial.lean#L106)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
