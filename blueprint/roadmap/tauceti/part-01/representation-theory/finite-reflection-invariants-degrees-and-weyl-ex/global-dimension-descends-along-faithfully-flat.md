---
declaration: theorem
origin: cited
lean: TauCeti.globalDimension_le_of_faithfullyFlat
statement: formalized
proof: formalized
---

# Global dimension descends along faithfully flat algebras

A noetherian ring `R` has global
dimension at most that of any faithfully flat `R`-algebra `S`: the projective dimension of a
finite `R`-module equals that of its base change to `S`
(`ModuleCat.hasProjectiveDimensionLE_baseChange_iff`), and finite modules detect the global
dimension.

```lean
TauCeti.globalDimension_le_of_faithfullyFlat.{u} {R : Type u} [CommRing R] {S : Type u} [CommRing S]
  [Algebra R S] [IsNoetherianRing R] [Module.FaithfullyFlat R S] :
  TauCeti.globalDimension R ≤ TauCeti.globalDimension S
```

## Depends on

- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Proof depends on

- [Schanuel's lemma in automorphism form](../../algebra/part-02/module/schanuels-lemma-in-automorphism-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.globalDimension_le_of_faithfullyFlat`](https://taucetiproject.org/docs/TauCeti/RingTheory/GlobalDimension.html#TauCeti.globalDimension_le_of_faithfullyFlat).

## Sources

- [Tau Ceti documentation: `TauCeti.globalDimension_le_of_faithfullyFlat`](https://taucetiproject.org/docs/TauCeti/RingTheory/GlobalDimension.html#TauCeti.globalDimension_le_of_faithfullyFlat)
- [Source of `TauCeti.globalDimension_le_of_faithfullyFlat` in TauCeti/RingTheory/GlobalDimension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/GlobalDimension.lean#L236)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
