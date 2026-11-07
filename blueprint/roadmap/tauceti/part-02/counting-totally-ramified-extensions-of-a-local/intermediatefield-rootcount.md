---
declaration: def
origin: cited
lean: IntermediateField.rootCount
statement: formalized
---

# IntermediateField.rootCount

The root count of a coefficient vector `a : Fin n → K` in a subextension `L`: the number of
roots of the monic polynomial `monicOfCoeff a` lying in `L`, counted with multiplicity.

```lean
IntermediateField.rootCount.{u_1, u_2} {K : Type u_1} {E : Type u_2} [Field K] [Field E]
  [Algebra K E] (L : IntermediateField K E) {n : ℕ} (a : Fin n → K) : ℕ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`IntermediateField.rootCount`](https://taucetiproject.org/docs/TauCeti/FieldTheory/IntermediateField/RootCount.html#IntermediateField.rootCount).

## Sources

- [Tau Ceti documentation: `IntermediateField.rootCount`](https://taucetiproject.org/docs/TauCeti/FieldTheory/IntermediateField/RootCount.html#IntermediateField.rootCount)
- [Source of `IntermediateField.rootCount` in TauCeti/FieldTheory/IntermediateField/RootCount.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/IntermediateField/RootCount.lean#L65)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/MassFormula/STATUS.md)
