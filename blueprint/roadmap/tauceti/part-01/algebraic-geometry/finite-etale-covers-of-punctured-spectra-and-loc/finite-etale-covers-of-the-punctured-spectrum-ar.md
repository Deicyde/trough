---
declaration: def
origin: cited
lean: TauCeti.IsLocalRing.finiteNormalEquiv
statement: formalized
---

# Finite étale covers of the punctured spectrum are finite normal algebras

Over a
Noetherian integrally closed local domain `A` of dimension at least two, the category of finite
étale covers of the punctured spectrum is anti-equivalent to the category of finite normal
torsion-free `A`-algebras étale at every prime not lying over the maximal ideal. The functor
sends a cover `V` to its ring of sections `sectionsAlg hdim V` (`finiteNormalEquiv_functor_obj`)
and a morphism to restriction of sections (`finiteNormalEquiv_functor_map`), and the inverse is
`restrictPuncturedSpec`, restriction of `Spec B` to the punctured spectrum.

```lean
TauCeti.IsLocalRing.finiteNormalEquiv.{u} {A : Type u} [CommRing A] [IsLocalRing A]
  [IsNoetherianRing A] [IsDomain A] [IsIntegrallyClosed A] (hdim : 2 ≤ ringKrullDim A) :
  TauCeti.FiniteEtaleScheme ↑(TauCeti.IsLocalRing.puncturedSpectrum A) ≌
    (TauCeti.IsLocalRing.FiniteNormalPuncturedEtaleAlg A)ᵒᵖ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Algebraic Hartogs principle](../other-results/algebraic-hartogs-principle.md)
- [Algebraic Hartogs principle for fractions](../../ring-theory/part-02/other-results/part-01/algebraic-hartogs-principle-for-fractions.md)
- [Hartogs principle for `M~` on `Spec R`](../other-results/hartogs-principle-for-m-on-spec-r.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsLocalRing.finiteNormalEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/FiniteNormal.html#TauCeti.IsLocalRing.finiteNormalEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.IsLocalRing.finiteNormalEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/FiniteNormal.html#TauCeti.IsLocalRing.finiteNormalEquiv)
- [Source of `TauCeti.IsLocalRing.finiteNormalEquiv` in TauCeti/AlgebraicGeometry/FiniteEtale/FiniteNormal.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/FiniteEtale/FiniteNormal.lean#L430)
- [Tau Ceti roadmap status: Finite étale covers of punctured spectra and local purity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/LocalPurity/STATUS.md)
