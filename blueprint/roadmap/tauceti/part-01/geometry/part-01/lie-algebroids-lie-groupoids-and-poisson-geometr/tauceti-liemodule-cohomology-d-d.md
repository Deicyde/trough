---
declaration: theorem
origin: cited
lean: TauCeti.LieModule.Cohomology.d_d
statement: formalized
proof: formalized
---

# TauCeti.LieModule.Cohomology.d_d

The Chevalley–Eilenberg differential squares to zero.

```lean
TauCeti.LieModule.Cohomology.d_d.{u_1, u_2, u_3} {R : Type u_1} [CommRing R] {L : Type u_2}
  [LieRing L] [LieAlgebra R L] {M : Type u_3} [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] (n : ℕ) (ω : L [⋀^Fin n]→ₗ[R] M) :
  (TauCeti.LieModule.Cohomology.d R L M (n + 1)) ((TauCeti.LieModule.Cohomology.d R L M n) ω) = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's formula `ι_x d ω = L_x ω - d ι_x ω`](cartans-formula-x-d-l-x-d-x.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.d_d`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d_d).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.d_d`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.d_d)
- [Source of `TauCeti.LieModule.Cohomology.d_d` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L186)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
