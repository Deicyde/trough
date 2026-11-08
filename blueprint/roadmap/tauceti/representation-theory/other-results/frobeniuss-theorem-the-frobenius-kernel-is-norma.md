---
declaration: theorem
origin: cited
lean: TauCeti.frobeniusKernelSubgroup_normal
statement: formalized
proof: formalized
---

# Frobenius's theorem: the Frobenius kernel is normal

```lean
TauCeti.frobeniusKernelSubgroup_normal.{u} {G : Type u} [Group G] [Finite G] {H : Subgroup G}
  (hH : TauCeti.IsTISubgroup H) : (TauCeti.frobeniusKernelSubgroup hH).Normal
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frobenius reciprocity for class functions](../induction/frobenius-reciprocity-for-class-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusKernelSubgroup_normal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.html#TauCeti.frobeniusKernelSubgroup_normal).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusKernelSubgroup_normal`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.html#TauCeti.frobeniusKernelSubgroup_normal)
- [Source of `TauCeti.frobeniusKernelSubgroup_normal` in TauCeti/RepresentationTheory/FrobeniusGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.lean#L247)
