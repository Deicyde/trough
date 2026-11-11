---
declaration: theorem
origin: cited
lean: TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded
statement: formalized
proof: formalized
---

# Phragmén–Lindelöf principle on the upper half-plane

If `f` is bounded on the open upper
half-plane, holomorphic there, continuous on its closure, and bounded by `C` on the real axis,
then `f` is bounded by `C` on the closed upper half-plane.

```lean
TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [NormedSpace ℂ E] {f : ℂ → E} {C : ℝ} {z : ℂ} (hd : DiffContOnCl ℂ f {z | 0 < z.im})
  (hb : Bornology.IsBounded (f '' {z | 0 < z.im})) (hre : ∀ (x : ℝ), ‖f ↑x‖ ≤ C) (hz : 0 ≤ z.im) :
  ‖f z‖ ≤ C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PhragmenLindelof/Basic.html#TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded).

## Sources

- [Tau Ceti documentation: `TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/PhragmenLindelof/Basic.html#TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded)
- [Source of `TauCeti.PhragmenLindelof.upper_half_plane_of_isBounded` in TauCeti/Analysis/Complex/PhragmenLindelof/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/PhragmenLindelof/Basic.lean#L30)
