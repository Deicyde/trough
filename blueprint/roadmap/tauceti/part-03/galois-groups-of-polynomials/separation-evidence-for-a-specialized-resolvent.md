---
declaration: structure
origin: cited
lean: TauCeti.ResolventSeparationEvidence
statement: formalized
---

# Separation evidence for a specialized resolvent

This records that the specialized
resolvent is separable. Under the usual monic degree-`n` splitting description, it says that
distinct elements of the symbolic orbit take distinct values at the roots of `f`. This is the
hypothesis that lets a root or a factorization of the resolvent constrain the Galois image;
specialization never loses degree, but its values can collide.

```lean
TauCeti.ResolventSeparationEvidence.{u_1} {F : Type u_1} [Field F] {n : ℕ}
  (spec : TauCeti.ResolventSpec n) (f : Polynomial F) : Prop
```

## Depends on

- [TauCeti.ResolventSpec](tauceti-resolventspec.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ResolventSeparationEvidence`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.html#TauCeti.ResolventSeparationEvidence).

## Sources

- [Tau Ceti documentation: `TauCeti.ResolventSeparationEvidence`](https://taucetiproject.org/docs/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.html#TauCeti.ResolventSeparationEvidence)
- [Source of `TauCeti.ResolventSeparationEvidence` in TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/FieldTheory/GaloisGroups/Resolvent/Spec.lean#L175)
- [Tau Ceti roadmap status: Galois groups of polynomials](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/PolynomialGaloisGroups/STATUS.md)
