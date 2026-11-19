---
declaration: theorem
origin: cited
lean: TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul
statement: formalized
proof: formalized
---

# Chevalley's identity at every root

`n_γ(s) = h_γ(s) n_γ(1)`, with `h_γ` the coroot of
`γ` in the actual torus of the datum.

```lean
TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul.{v} {t : TauCeti.DynkinType}
  {ht : t.Valid} (D : t.ChevalleyDatum ht) (γ : Fin t.numRoots) (A : Type v) [CommRing A] (s : Aˣ) :
  D.weylElement γ A s = (D.corootPoints γ A) s * D.weylElement γ A 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Chevalley's rank-one identity](../../part-02/lie/part-01/chevalleys-rank-one-identity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Root/Weyl.html#TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Chevalley/Root/Weyl.html#TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul)
- [Source of `TauCeti.DynkinType.ChevalleyDatum.weylElement_eq_corootPoints_mul` in TauCeti/Algebra/AlgebraicGroup/Chevalley/Root/Weyl.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/AlgebraicGroup/Chevalley/Root/Weyl.lean#L68)
