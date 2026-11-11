---
declaration: theorem
origin: cited
lean: TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq
statement: formalized
proof: formalized
---

# Borel conjugacy

Any two Borel subgroups of a finite-type affine group over an
algebraically closed field are conjugate by a rational point. The ambient group need not
be smooth, reduced, or connected.

```lean
TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq.{u} {k : Type u} [Field k]
  {H : TauCeti.FiniteTypeCommHopfAlgCat k} {I J : TauCeti.HopfIdeal k ↑H.obj}
  (hI : TauCeti.HopfIdeal.IsBorelOverAlgClosed k H I)
  (hJ : TauCeti.HopfIdeal.IsBorelOverAlgClosed k H J) : ∃ g, I.conjugate g = J
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Borel fixed-point theorem, orbit form](../algebraic-group/borel-fixed-point-theorem-orbit-form.md)
- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.html#TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.html#TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq)
- [Source of `TauCeti.HopfIdeal.IsBorelOverAlgClosed.exists_conjugate_eq` in TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Borel/Conjugacy/Existence.lean#L131)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ReductiveGroups/STATUS.md)
