---
declaration: def
origin: cited
lean: ContRepresentation.hilbertSum
statement: formalized
---

# ContRepresentation.hilbertSum

The Hilbert direct sum of a family of unitary representations, acting coordinatewise on
`lp H 2`.

```lean
ContRepresentation.hilbertSum.{u_1, u_2, u_3, u_4} {𝕜 : Type u_1} {G : Type u_2} {ι : Type u_3}
  [RCLike 𝕜] [Monoid G] {H : ι → Type u_4} [(i : ι) → NormedAddCommGroup (H i)]
  [(i : ι) → InnerProductSpace 𝕜 (H i)] (π : (i : ι) → ContRepresentation 𝕜 G (H i))
  (hπ : ∀ (i : ι), (π i).IsUnitary) : ContRepresentation 𝕜 G ↥(lp H 2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContRepresentation.hilbertSum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Unitary/HilbertSum.html#ContRepresentation.hilbertSum).

## Sources

- [Tau Ceti documentation: `ContRepresentation.hilbertSum`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Continuous/Unitary/HilbertSum.html#ContRepresentation.hilbertSum)
- [Source of `ContRepresentation.hilbertSum` in TauCeti/RepresentationTheory/Continuous/Unitary/HilbertSum.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Continuous/Unitary/HilbertSum.lean#L37)
- [Tau Ceti roadmap status: Approximation, deformation and rigidity of finite factors](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FactorRigidity/STATUS.md)
