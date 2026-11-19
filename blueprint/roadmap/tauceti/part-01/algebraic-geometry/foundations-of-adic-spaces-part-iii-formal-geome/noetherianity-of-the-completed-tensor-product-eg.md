---
declaration: theorem
origin: cited
lean: TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing
statement: formalized
proof: formalized
---

# Noetherianity of the completed tensor product (EGA I, Ch. I, 10.13.5)

Let `A` carry the
`I`-adic topology for a finitely generated ideal `I`. If `B` is strictly topologically of finite
type over `A`, that is, an open quotient of some `A⟨X₁, …, Xₖ⟩`, and `C` is noetherian, then
`B ⊗̂_A C` is noetherian. Neither `A` nor `B` needs to be noetherian here.

```lean
TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing.{u_1, u_2, u_3} {A : Type u_1}
  (B : Type u_2) (C : Type u_3) [CommRing A] [CommRing B] [TopologicalSpace B] [IsTopologicalRing B]
  [TauCeti.IsAdicRing B] [Algebra A B] [CommRing C] [TopologicalSpace C] [IsTopologicalRing C]
  [TauCeti.IsAdicRing C] [Algebra A C] [TopologicalSpace A] [NonarchimedeanRing A]
  [IsNoetherianRing C] {I : Ideal A} (hI : IsAdic I) (hfg : I.FG)
  (hB : TauCeti.Huber.IsStrictlyTopologicallyFiniteType (algebraMap A B)) :
  IsNoetherianRing (TauCeti.AdicRing.CompletedTensorProduct A B C)
```

## Depends on

- [TauCeti.AdicRing.CompletedTensorProduct](tauceti-adicring-completedtensorproduct.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicRing/CompletedTensorProduct/Noetherian.html#TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing).

## Sources

- [Tau Ceti documentation: `TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/AdicRing/CompletedTensorProduct/Noetherian.html#TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing)
- [Source of `TauCeti.AdicRing.CompletedTensorProduct.isNoetherianRing` in TauCeti/RingTheory/AdicRing/CompletedTensorProduct/Noetherian.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/AdicRing/CompletedTensorProduct/Noetherian.lean#L89)
- [Tau Ceti roadmap status: Foundations of adic spaces, part III — formal geometry, formal models and coherent sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIII/STATUS.md)
