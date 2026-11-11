---
declaration: theorem
origin: cited
lean: TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries
statement: formalized
proof: formalized
---

# The product of the orbit-torus weights is the orbit zeta function

For a family of
orbits of classes `γ i` of positive period, finitely many below each cutoff, whose return maps
`P i` have determinant one and nondegenerate nonzero powers, the product over the orbits of the
labelled local series at `t = e^(γ i)` is, over any `ℚ`-algebra `K`, the orbit zeta function
`exp (∑ᵢ ∑_{n ≥ 1} sgn det (1 - P i ^ n) e^(n • γ i) / n)`.

```lean
TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries.{u_1, u_2, u_3, u_4}
  {ι : Type u_1} {H : Type u_2} [AddCommMonoid H] {N : H →+ ℝ} {γ : ι → H}
  (hpos : ∀ (i : ι), 0 < N (γ i))
  (hfin : Filter.Tendsto (fun i => N (γ i)) Filter.cofinite Filter.atTop) {R : Type u_3}
  [CommRing R] [LinearOrder R] [IsStrictOrderedRing R] {P : ι → Matrix (Fin 2) (Fin 2) R}
  (hdet : ∀ (i : ι), (P i).det = 1) (hP : ∀ (i : ι) (k : ℕ), k ≠ 0 → (1 - P i ^ k).det ≠ 0)
  (K : Type u_4) [CommRing K] [Algebra ℚ K] :
  (TauCeti.NovikovSeries.orbitZeta K N γ fun i n => ↑(SignType.sign (1 - P i ^ n).det)) =
    (TauCeti.NovikovSeries.mapRingHom (Int.castRingHom K) (AddMonoidHom.id H) ⋯)
      (∏' (i : ι),
        (TauCeti.NovikovSeries.ofPowerSeries (γ i) ⋯)
          (TauCeti.torusWeightSeries (decide (0 < (1 - P i).det))
            (if (1 + P i).det < 0 then 1 else 0)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cayley–Hamilton in size two](../../../linear-algebra/matrix/cayley-hamilton-in-size-two.md)
- [Integrality of the orbit zeta function](../../../algebra/part-01/morse-novikov-homology-and-dynamical-reidemeiste/integrality-of-the-orbit-zeta-function.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Zeta.html#TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries).

## Sources

- [Tau Ceti documentation: `TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Zeta.html#TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries)
- [Source of `TauCeti.orbitZeta_eq_mapRingHom_tprod_ofPowerSeries_torusWeightSeries` in TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Zeta.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/JHolomorphic/OrbitTorus/Zeta.lean#L174)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TaubesGromov/STATUS.md)
