---
declaration: def
origin: cited
lean: TauCeti.AdicRing.CompletedAway.completionLocEquiv
statement: formalized
---

# TauCeti.AdicRing.CompletedAway.completionLocEquiv

The **completed localisation is the rational localisation** `A⟨1/f⟩`: for an adic ring `A`
of finite ideal type and a finitely generated ideal of definition `I`, the completed localisation
`A_{f}` is isomorphic to the uniform completion of `A_f` for the localisation topology of the pair
of definition `(A, I)` with numerator `1` and denominator `f`.

```lean
TauCeti.AdicRing.CompletedAway.completionLocEquiv.{u_1, u_2} {A : Type u_1} [CommRing A]
  [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.IsAdicRing A] {f : A} {I : Ideal A}
  (hI : IsAdic I) (hfg : I.FG) (S : Type u_2) [CommRing S] [Algebra A S] [IsLocalization.Away f S]
  (hden : (TauCeti.Huber.PairOfDefinition.adic I hI hfg).HasDenominatorPower {1} f S) :
  TauCeti.AdicRing.CompletedAway A f ≃+* UniformSpace.Completion S
```

## Depends on

- [TauCeti.AdicRing.CompletedAway](tauceti-adicring-completedaway.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicRing.CompletedAway.completionLocEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicRing/CompletedAway/RationalLocalization.html#TauCeti.AdicRing.CompletedAway.completionLocEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicRing.CompletedAway.completionLocEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicRing/CompletedAway/RationalLocalization.html#TauCeti.AdicRing.CompletedAway.completionLocEquiv)
- [Source of `TauCeti.AdicRing.CompletedAway.completionLocEquiv` in TauCeti/RingTheory/AdicRing/CompletedAway/RationalLocalization.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/AdicRing/CompletedAway/RationalLocalization.lean#L79)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
