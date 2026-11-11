---
declaration: theorem
origin: cited
lean: TauCeti.degree_lowSimpleSet_mem_Ioo
statement: formalized
proof: formalized
---

# TauCeti.degree_lowSimpleSet_mem_Ioo

The constructed c.e. degree lies strictly between the computable and halting degrees.

```lean
TauCeti.degree_lowSimpleSet_mem_Ioo :
  toAntisymmetrization TuringReducible TauCeti.lowSimpleSet.oracle ∈
    Set.Ioo (toAntisymmetrization TuringReducible ∅.oracle)
      (toAntisymmetrization TuringReducible ∅.jump.oracle)
```

## Depends on

- [Set.jump](set-jump.md)
- [TauCeti.Oracle.Single.Code](tauceti-oracle-single-code.md)

## Proof depends on

- [Adequacy](adequacy.md)
- [The constructed set is simple](the-constructed-set-is-simple.md)
- [Set.Low](set-low.md)
- [TauCeti.low_lowSimpleSet](tauceti-low-lowsimpleset.md)
- [The use principle](the-use-principle.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.degree_lowSimpleSet_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/Lowness.html#TauCeti.degree_lowSimpleSet_mem_Ioo).

## Sources

- [Tau Ceti documentation: `TauCeti.degree_lowSimpleSet_mem_Ioo`](https://taucetiproject.org/docs/TauCeti/Computability/Simple/Lowness.html#TauCeti.degree_lowSimpleSet_mem_Ioo)
- [Source of `TauCeti.degree_lowSimpleSet_mem_Ioo` in TauCeti/Computability/Simple/Lowness.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Computability/Simple/Lowness.lean#L122)
- [Tau Ceti roadmap status: Computability theory and finite-injury constructions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ComputabilityTheory/STATUS.md)
