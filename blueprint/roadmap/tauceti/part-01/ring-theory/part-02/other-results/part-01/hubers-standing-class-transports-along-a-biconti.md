---
declaration: theorem
origin: cited
lean: TauCeti.Huber.IsHuberStandard.of_ringEquiv
statement: formalized
proof: formalized
---

# Huber's standing class transports along a bicontinuous ring isomorphism

Continuity of both
`e` and `e.symm` is required, since a `RingEquiv` is purely algebraic.

```lean
TauCeti.Huber.IsHuberStandard.of_ringEquiv.{u_2, u_3} {A : Type u_2} {B : Type u_3} [CommRing A]
  [TopologicalSpace A] [IsTopologicalRing A] [TauCeti.Huber.IsHuberRing A] [CommRing B]
  [TopologicalSpace B] [IsTopologicalRing B] [TauCeti.Huber.IsHuberRing B]
  [hA : TauCeti.Huber.IsHuberStandard A] (e : A ≃+* B) (he : Continuous ⇑e)
  (he' : Continuous ⇑e.symm) : TauCeti.Huber.IsHuberStandard B
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Huber.IsHuberStandard.of_ringEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianType/HuberStandard.html#TauCeti.Huber.IsHuberStandard.of_ringEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.Huber.IsHuberStandard.of_ringEquiv`](https://taucetiproject.org/docs/TauCeti/RingTheory/Huber/NoetherianType/HuberStandard.html#TauCeti.Huber.IsHuberStandard.of_ringEquiv)
- [Source of `TauCeti.Huber.IsHuberStandard.of_ringEquiv` in TauCeti/RingTheory/Huber/NoetherianType/HuberStandard.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Huber/NoetherianType/HuberStandard.lean#L120)
