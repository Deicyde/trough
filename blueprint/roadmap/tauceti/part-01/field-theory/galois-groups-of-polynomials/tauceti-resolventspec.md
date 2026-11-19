---
declaration: structure
origin: cited
lean: TauCeti.ResolventSpec
statement: formalized
---

# TauCeti.ResolventSpec

A **resolvent specification** in degree `n`: a subgroup `H` of `Equiv.Perm (Fin n)`, an
integral invariant `Φ` in `n` formal roots whose stabilizer under renaming is exactly `H`, and the
integral expression of the orbit product of `Φ` in the elementary symmetric polynomials. No
polynomial and no coefficient ring appears; specialization is `ResolventSpec.specialize`.

```lean
TauCeti.ResolventSpec (n : ℕ) : Type
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ResolventSpec`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.html#TauCeti.ResolventSpec).

## Sources

- [Tau Ceti documentation: `TauCeti.ResolventSpec`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.html#TauCeti.ResolventSpec)
- [Source of `TauCeti.ResolventSpec` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.lean#L73)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/PolynomialGaloisGroups/STATUS.md)
