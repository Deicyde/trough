---
declaration: abbrev
origin: cited
lean: TauCeti.CurrentAlgebra.CompletedEnveloping
statement: formalized
---

# The completed enveloping algebra

**The completed enveloping algebra** `Û = lim_n U / I_n` of the residue central extension of
`Φ` at the central value `a`: the left `U`-module of compatible families of classes modulo the left
ideals of high-order currents, with the inverse limit topology.

```lean
TauCeti.CurrentAlgebra.CompletedEnveloping.{u_1, u_2} {R : Type u_1} {L : Type u_2} [CommRing R]
  [LieRing L] [LieAlgebra R L] (Φ : LinearMap.BilinForm R L)
  (hΦ : LinearMap.BilinForm.lieInvariant L Φ) (hΦs : Φ.IsSymm) (a : R) : Type (max u_1 u_2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CurrentAlgebra.CompletedEnveloping`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Completion.html#TauCeti.CurrentAlgebra.CompletedEnveloping).

## Sources

- [Tau Ceti documentation: `TauCeti.CurrentAlgebra.CompletedEnveloping`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Current/Completion.html#TauCeti.CurrentAlgebra.CompletedEnveloping)
- [Source of `TauCeti.CurrentAlgebra.CompletedEnveloping` in TauCeti/Algebra/Lie/Current/Completion.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Current/Completion.lean#L134)
- [Tau Ceti roadmap status: Affine Lie algebras, smooth modules and completed centers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AffineLieAlgebras/STATUS.md)
