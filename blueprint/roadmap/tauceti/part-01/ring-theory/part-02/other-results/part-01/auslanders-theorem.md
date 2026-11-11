---
declaration: theorem
origin: cited
lean: TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson, TauCeti.globalDimension_eq_iSup_cyclic
statement: formalized
proof: formalized
---

# Auslander's theorem

The global dimension of a semiprimary ring `A`, for instance an
Artinian ring, is the projective dimension of `A ⧸ J`, where `J` is the Jacobson radical. Both
sides are `⊥` for the zero ring. Auslander, *On the dimension of modules and algebras III*,
Corollary 11 (b).

```lean
TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson.{v, u} {A : Type u} [Ring A]
  [Small.{v, u} A] [IsSemiprimaryRing A] :
  TauCeti.globalDimension A =
    CategoryTheory.projectiveDimension ↧(Shrink.{v, u} (A ⧸ Ring.jacobson A))
```

## Depends on

- [TauCeti.globalDimension](../../../part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson`](https://taucetiproject.org/docs/TauCeti/RingTheory/GlobalDimension/Semiprimary.html#TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson).

## Other forms

**Auslander's theorem: the global dimension is the supremum over cyclic modules.** Formalized in Tau Ceti as [`TauCeti.globalDimension_eq_iSup_cyclic`](https://taucetiproject.org/docs/TauCeti/RingTheory/GlobalDimension.html#TauCeti.globalDimension_eq_iSup_cyclic).

```lean
TauCeti.globalDimension_eq_iSup_cyclic.{v, u} (R : Type u) [Ring R] [Small.{v, u} R] :
  TauCeti.globalDimension R = ⨆ I, CategoryTheory.projectiveDimension ↧(Shrink.{v, u} (R ⧸ I))
```

## Sources

- [Tau Ceti documentation: `TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson`](https://taucetiproject.org/docs/TauCeti/RingTheory/GlobalDimension/Semiprimary.html#TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson)
- [Source of `TauCeti.globalDimension_eq_projectiveDimension_quotient_jacobson` in TauCeti/RingTheory/GlobalDimension/Semiprimary.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/GlobalDimension/Semiprimary.lean#L67)
