---
declaration: theorem
origin: cited
lean: TauCeti.LieModule.Cohomology.curryLeft_d_succ
statement: formalized
proof: formalized
---

# Cartan's formula `ι_x d ω = L_x ω - d ι_x ω`

```lean
TauCeti.LieModule.Cohomology.curryLeft_d_succ.{u_1, u_2, u_3} {R : Type u_1} [CommRing R]
  {L : Type u_2} [LieRing L] [LieAlgebra R L] {M : Type u_3} [AddCommGroup M] [_root_.Module R M]
  [LieRingModule L M] [LieModule R L M] {n : ℕ} (ω : L [⋀^Fin (n + 1)]→ₗ[R] M) (x : L) :
  ((TauCeti.LieModule.Cohomology.d R L M (n + 1)) ω).curryLeft x =
    ⁅x, ω⁆ - (TauCeti.LieModule.Cohomology.d R L M n) (ω.curryLeft x)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LieModule.Cohomology.curryLeft_d_succ`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.curryLeft_d_succ).

## Sources

- [Tau Ceti documentation: `TauCeti.LieModule.Cohomology.curryLeft_d_succ`](https://taucetiproject.org/docs/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.html#TauCeti.LieModule.Cohomology.curryLeft_d_succ)
- [Source of `TauCeti.LieModule.Cohomology.curryLeft_d_succ` in TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Lie/Cohomology/ChevalleyEilenberg.lean#L159)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
