---
declaration: theorem
origin: cited
lean: TauCeti.Diffeotopy.exists_flux_eq
statement: formalized
proof: formalized
---

# Every first de Rham class is a flux

On a compact manifold with a closed nondegenerate
two-form `σ`, every class in `H¹_dR(M)` is the flux of a diffeotopy all of whose maps preserve
`σ`: the time-one flow of the symplectic vector field `(σ♭)⁻¹ α`, for a closed representative
`α` of the class.

```lean
TauCeti.Diffeotopy.exists_flux_eq.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} {M : Type u_3}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M] [T2Space M]
  [IsManifold I (↑⊤) M] [CompactSpace M] (σ : ↥(TauCeti.closedForms I M 2))
  (hσ : TauCeti.SmoothTwoForm.IsNondegenerate ↑σ) (c : TauCeti.deRhamCohomology I M 1) :
  ∃ Φ,
    ∃ (hΦ : Φ.final ∈ (↑σ).diffeomorphStabilizer),
      (∀ (t : ↑unitInterval), Φ.timeSlice t ∈ (↑σ).diffeomorphStabilizer) ∧ Φ.flux σ hΦ = c
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Diffeotopy.exists_flux_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Flux/Flow.html#TauCeti.Diffeotopy.exists_flux_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Diffeotopy.exists_flux_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Flux/Flow.html#TauCeti.Diffeotopy.exists_flux_eq)
- [Source of `TauCeti.Diffeotopy.exists_flux_eq` in TauCeti/Geometry/Symplectic/Flux/Flow.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Flux/Flow.lean#L143)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
