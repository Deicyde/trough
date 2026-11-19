---
declaration: def
origin: cited
lean: Module.End.jordanPartition
statement: formalized
---

# Module.End.jordanPartition

The Jordan partition of a nilpotent endomorphism, with each Jordan block contributing
its size as a part. It is characterized by `count_jordanPartition_parts_succ`.

```lean
Module.End.jordanPartition.{u_1, u_2} {K : Type u_1} {V : Type u_2} [Field K] [AddCommGroup V]
  [_root_.Module K V] [FiniteDimensional K V] (f : Module.End K V) (hf : IsNilpotent f) :
  (Module.finrank K V).Partition
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Module.End.jordanPartition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/JordanChain/Partition.html#Module.End.jordanPartition).

## Sources

- [Tau Ceti documentation: `Module.End.jordanPartition`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/End/JordanChain/Partition.html#Module.End.jordanPartition)
- [Source of `Module.End.jordanPartition` in TauCeti/LinearAlgebra/End/JordanChain/Partition.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/LinearAlgebra/End/JordanChain/Partition.lean#L115)
- [Tau Ceti roadmap status: Nilpotent orbits, Springer resolution and subregular geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/NilpotentOrbits/STATUS.md)
