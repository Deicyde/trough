---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit
statement: formalized
proof: formalized
---

# The number of cusps of a locally finite fundamental polygon

The number of cusp orbits
of `Γ` is the number of ideal vertex cycles of `P`.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit {n : ℕ} [NeZero n]
  {P : TauCeti.UpperHalfPlane.ConvexPolygon n} (σ : P.SidePairing)
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hmap : ∀ (i : Fin n), σ.map i ∈ Γ)
  (hlf : LocallyFinite fun γ => ↑γ • P.carrier)
  (hdisj : ∀ (γ : ↥Γ), γ ≠ 1 → Disjoint (↑γ • interior P.carrier) (interior P.carrier)) :
  Nat.card Γ.CuspOrbit = Nat.card σ.IdealVertexCycle
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Shimizu's inequality at two cusps](../../part-02/complex/part-03/shimizus-inequality-at-two-cusps.md)
- [Subgroup.CompactifiedQuotient](subgroup-compactifiedquotient.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Cusp/VertexCycle.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit).

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Cusp/VertexCycle.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.natCard_cuspOrbit` in TauCeti/Analysis/Complex/Fuchsian/Cusp/VertexCycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Cusp/VertexCycle.lean#L116)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
