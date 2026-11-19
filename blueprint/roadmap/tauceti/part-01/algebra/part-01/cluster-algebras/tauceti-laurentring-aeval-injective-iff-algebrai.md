---
declaration: theorem
origin: cited
lean: TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent
statement: formalized
proof: formalized
---

# TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent

Evaluation of Laurent polynomials at a family of units is injective exactly when the family
is algebraically independent over the coefficient ring.

```lean
TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent.{u_2, u_4, u_5} {K : Type u_2}
  {R : Type u_4} {A : Type u_5} [CommRing R] [CommRing A] [Algebra R A] (x : K → Aˣ) :
  Function.Injective ⇑(TauCeti.LaurentRing.aeval x) ↔ AlgebraicIndependent R fun i => ↑(x i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Laurent ring is the localization of the polynomial ring at the variables](the-laurent-ring-is-the-localization-of-the-poly.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.html#TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent`](https://taucetiproject.org/docs/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.html#TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent)
- [Source of `TauCeti.LaurentRing.aeval_injective_iff_algebraicIndependent` in TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/MvPolynomial/Laurent/Polynomial.lean#L281)
- [Tau Ceti roadmap status: Cluster algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClusterAlgebras/STATUS.md)
