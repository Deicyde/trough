---
declaration: theorem
origin: cited
lean: TauCeti.frobeniusKernelSubgroup_eq_of_isComplement'
statement: formalized
proof: formalized
---

# Frobenius's theorem returns the complement it was handed

If `N` is a complement to a
trivial-intersection subgroup `H` (`N.IsComplement' H`, with no normality assumed), then the
subgroup that the exceptional-character argument above constructs -- out of the irreducible
characters of `H`, with no reference to `N` -- is `N` itself.

This is what makes the abstract construction checkable on a concrete Frobenius group, which comes
presented as such a decomposition with `H` acting on `N` without nonidentity fixed points
(`TauCeti.isTISubgroup_of_isComplement'_of_fixedPointFree`).

```lean
TauCeti.frobeniusKernelSubgroup_eq_of_isComplement'.{u} {G : Type u} [Group G] [Finite G]
  {H N : Subgroup G} (hH : TauCeti.IsTISubgroup H) (hNH : N.IsComplement' H) :
  TauCeti.frobeniusKernelSubgroup hH = N
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Frobenius reciprocity for class functions](../induction/frobenius-reciprocity-for-class-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusKernelSubgroup_eq_of_isComplement'`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.html#TauCeti.frobeniusKernelSubgroup_eq_of_isComplement').

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusKernelSubgroup_eq_of_isComplement'`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.html#TauCeti.frobeniusKernelSubgroup_eq_of_isComplement')
- [Source of `TauCeti.frobeniusKernelSubgroup_eq_of_isComplement'` in TauCeti/RepresentationTheory/FrobeniusGroup/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/FrobeniusGroup/Basic.lean#L340)
