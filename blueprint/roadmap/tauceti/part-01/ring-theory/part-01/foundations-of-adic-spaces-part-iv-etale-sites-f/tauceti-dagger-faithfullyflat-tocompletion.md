---
declaration: theorem
origin: cited
lean: TauCeti.Dagger.faithfullyFlat_toCompletion
statement: formalized
proof: formalized
---

# TauCeti.Dagger.faithfullyFlat_toCompletion

The completion map of a dagger algebra is faithfully flat.

```lean
TauCeti.Dagger.faithfullyFlat_toCompletion.{u_1, u_2} {K : Type u_1} [NontriviallyNormedField K]
  [IsUltrametricDist K] [CompleteSpace K] {A : Type u_2} [CommRing A] [Algebra K A]
  [TauCeti.Dagger.IsDaggerAlgebra K A] : (TauCeti.Dagger.toCompletion K A).FaithfullyFlat
```

## Depends on

- [TauCeti.Dagger.completion](tauceti-dagger-completion.md)
- [TauCeti.Dagger.IsDaggerAlgebra](tauceti-dagger-isdaggeralgebra.md)

## Proof depends on

- [The Tate algebra is faithfully flat over the Monsky–Washnitzer algebra](the-tate-algebra-is-faithfully-flat-over-the-mon.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Dagger.faithfullyFlat_toCompletion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.faithfullyFlat_toCompletion).

## Sources

- [Tau Ceti documentation: `TauCeti.Dagger.faithfullyFlat_toCompletion`](https://taucetiproject.org/docs/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.html#TauCeti.Dagger.faithfullyFlat_toCompletion)
- [Source of `TauCeti.Dagger.faithfullyFlat_toCompletion` in TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Dagger/DaggerAlgebra/FaithfullyFlat.lean#L121)
- [Tau Ceti roadmap status: Foundations of adic spaces, part IV — étale sites, families and dagger geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AdicSpacesPartIV/STATUS.md)
