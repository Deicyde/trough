---
declaration: theorem
origin: cited
lean: TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul
statement: formalized
proof: formalized
---

# The orbifold area formula for a fundamental polygon

Let the translates of a side-paired
convex `n`-gon `P` by a group `Γ` containing the side-pairing maps be locally finite, with disjoint
interiors. Then the covolume of `Γ` is `2π ((n - k) / 2 - 1 - V + ∑ₑ (1 - 1 / mₑ))`, where `k` is
the number of self-paired sides, `V` the number of finite vertex cycles, and `e` runs over the
elliptic orbits of `Γ`, with stabilizer orders `mₑ`.

```lean
TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul {n : ℕ} [NeZero n]
  {P : TauCeti.UpperHalfPlane.ConvexPolygon n} (σ : P.SidePairing)
  {Γ : Subgroup (Matrix.ProjectiveSpecialLinearGroup (Fin 2) ℝ)} (hmap : ∀ (i : Fin n), σ.map i ∈ Γ)
  (hlf : LocallyFinite fun γ => ↑γ • P.carrier)
  (hdisj : ∀ (γ : ↥Γ), γ ≠ 1 → Disjoint (↑γ • interior P.carrier) (interior P.carrier)) :
  MeasureTheory.covolume (↥Γ) UpperHalfPlane MeasureTheory.volume =
    ENNReal.ofReal
      (2 * Real.pi *
        ((↑n - ↑(Nat.card { i // σ.pair i = i })) / 2 - 1 - ↑(Nat.card σ.FiniteVertexCycle) +
          ∑ᶠ (e : MulAction.orbitRel.Quotient (↥Γ) UpperHalfPlane) (_ : e ∈ Γ.ellipticOrbits),
            (1 - (↑(TauCeti.cardStabilizerOnOrbit e))⁻¹)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Polygon/Area.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul).

## Sources

- [Tau Ceti documentation: `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Fuchsian/Polygon/Area.html#TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul)
- [Source of `TauCeti.UpperHalfPlane.ConvexPolygon.SidePairing.covolume_eq_two_pi_mul` in TauCeti/Analysis/Complex/Fuchsian/Polygon/Area.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Fuchsian/Polygon/Area.lean#L124)
- [Tau Ceti roadmap status: Fuchsian groups and orbifold Riemann surfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FuchsianOrbifolds/STATUS.md)
