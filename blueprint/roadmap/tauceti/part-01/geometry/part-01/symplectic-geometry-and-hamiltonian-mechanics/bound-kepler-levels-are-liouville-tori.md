---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace
statement: formalized
proof: formalized
---

# Bound Kepler levels are Liouville tori

Let `m, κ > 0`, and let `x` be a state of the bound
phase space with energy `E` and angular momentum `ℓ`, where `E` is above the circular energy
`-m κ² / (2 ℓ²)`. Then the connected component of `x` in its common level of the energy and the
angular momentum is homeomorphic to the torus `(ℝ / ℤ)²`.

```lean
TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] (b : OrthonormalBasis (Fin 2) ℝ V) {m κ : ℝ}
  [FiniteDimensional ℝ V] (hm : 0 < m) (hκ : 0 < κ) (x : ↥(TauCeti.keplerBoundPhaseSpace b m κ))
  (hx :
    -(m * κ ^ 2) / (2 * TauCeti.angularMomentum (b 0) (b 1) ↑x ^ 2) <
      TauCeti.centralForceHamiltonian m (fun r => -κ / r) ↑x) :
  Nonempty
    (↑(connectedComponentIn
          ((TauCeti.centralForceEnergyMomentum b m fun r => -κ / r) ∘ Subtype.val ⁻¹'
            {TauCeti.centralForceEnergyMomentum b m (fun r => -κ / r) ↑x})
          x) ≃ₜ
      UnitAddTorus (Fin 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cartan's magic formula](../../part-02/manifold/part-01/cartans-magic-formula.md)
- [The inverse function theorem for manifolds](../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/Kepler/Torus.html#TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/Kepler/Torus.html#TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace)
- [Source of `TauCeti.nonempty_homeomorph_unitAddTorus_keplerBoundPhaseSpace` in TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/Kepler/Torus.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Hamiltonian/CentralForce/Kepler/Torus.lean#L290)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
