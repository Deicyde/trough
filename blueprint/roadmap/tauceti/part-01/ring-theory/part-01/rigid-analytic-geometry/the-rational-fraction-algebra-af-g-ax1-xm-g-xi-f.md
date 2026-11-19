---
declaration: abbrev
origin: cited
lean: TauCeti.RationalFraction
statement: formalized
---

# The rational fraction algebra `A⟨f/g⟩ = A⟨X₁, …, Xₘ⟩ ⧸ (g Xᵢ - fᵢ)`

It carries the
quotient ring, algebra and topology structures of `Ideal.Quotient`.

```lean
TauCeti.RationalFraction.{u_1} {A : Type u_1} [NormedCommRing A] [IsUltrametricDist A] {m : ℕ}
  (g : A) (f : Fin m → A) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.RationalFraction`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/RationalFraction.html#TauCeti.RationalFraction).

## Sources

- [Tau Ceti documentation: `TauCeti.RationalFraction`](https://taucetiproject.org/docs/TauCeti/RingTheory/Affinoid/RationalFraction.html#TauCeti.RationalFraction)
- [Source of `TauCeti.RationalFraction` in TauCeti/RingTheory/Affinoid/RationalFraction.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Affinoid/RationalFraction.lean#L107)
- [Tau Ceti roadmap status: Rigid analytic geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/RigidAnalyticGeometry/STATUS.md)
