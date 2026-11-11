---
declaration: def
origin: cited
lean: TauCeti.Diffeotopy.flux
statement: formalized
---

# TauCeti.Diffeotopy.flux

The **flux** of a diffeotopy `φ` with respect to a closed two-form `σ` preserved by its final
diffeomorphism: the de Rham class of the closed flux form `∫₀¹ φ_t^* (ι_{X_t} σ) dt`. For a
symplectic form `σ` and a symplectic isotopy this is the flux of the isotopy.

```lean
TauCeti.Diffeotopy.flux.{u_1, u_2, u_3} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] {J : ModelWithCorners ℝ E H} {M : Type u_3}
  [TopologicalSpace M] [ChartedSpace H M] (Φ : TauCeti.Diffeotopy J (↑⊤) M) [IsManifold J (↑⊤) M]
  (σ : ↥(TauCeti.closedForms J M 2)) (hΦ : Φ.final ∈ (↑σ).diffeomorphStabilizer) :
  TauCeti.deRhamCohomology J M 1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Diffeotopy.flux`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Flux.html#TauCeti.Diffeotopy.flux).

## Sources

- [Tau Ceti documentation: `TauCeti.Diffeotopy.flux`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Flux.html#TauCeti.Diffeotopy.flux)
- [Source of `TauCeti.Diffeotopy.flux` in TauCeti/Geometry/Symplectic/Flux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Symplectic/Flux.lean#L203)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
