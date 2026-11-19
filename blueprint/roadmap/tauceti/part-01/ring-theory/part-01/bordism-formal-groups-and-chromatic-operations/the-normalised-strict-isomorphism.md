---
declaration: def
origin: cited
lean: FormalGroup.exponentTwoLogIso
statement: formalized
---

# The normalised strict isomorphism

**The normalised strict isomorphism** from a commutative formal group law `F` with
`[2]_F = 0` to the additive formal group law: the normalised logarithm, with the normalised
exponential as its inverse.

```lean
FormalGroup.exponentTwoLogIso.{u_1} {R : Type u_1} [CommRing R] (F : FormalGroup R) [F.IsComm]
  (hF : F.nsmulSeries 2 = 0) : TauCeti.FormalGroupIso F FormalGroup.𝔾ₐ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Nakayama's lemma over `ℤ`](../../part-02/other-results/part-02/nakayamas-lemma-over-z.md)

## Lean

Formalized in Tau Ceti as [`FormalGroup.exponentTwoLogIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/ExponentTwo/Iso.html#FormalGroup.exponentTwoLogIso).

## Sources

- [Tau Ceti documentation: `FormalGroup.exponentTwoLogIso`](https://taucetiproject.org/docs/TauCeti/RingTheory/FormalGroup/ExponentTwo/Iso.html#FormalGroup.exponentTwoLogIso)
- [Source of `FormalGroup.exponentTwoLogIso` in TauCeti/RingTheory/FormalGroup/ExponentTwo/Iso.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/FormalGroup/ExponentTwo/Iso.lean#L125)
- [Tau Ceti roadmap status: Bordism, formal groups and chromatic operations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/BordismFormalGroups/STATUS.md)
