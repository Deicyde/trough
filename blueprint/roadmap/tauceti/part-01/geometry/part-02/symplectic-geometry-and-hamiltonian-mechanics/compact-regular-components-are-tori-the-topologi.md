---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus
statement: formalized
proof: formalized
---

# Compact regular components are tori (the topological part of the Liouville–Arnold theorem)

Let `F` be a family of `n` Poisson-commuting functions on a `2n`-dimensional symplectic
manifold. If the connected component of `x` in its common level `F⁻¹(F x)` is compact and consists
of regular points of `F`, then it is homeomorphic to the torus `(ℝ / ℤ)ⁿ`. The Hamiltonian vector
fields of the `F_i` need not be complete.

```lean
TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus.{u_1, u_2, u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] [BoundarylessManifold I M] [I.Boundaryless]
  {σ : TauCeti.SmoothTwoForm I M} (hσ : σ.IsSymplectic) {ι : Type u_4} [Fintype ι] {F : M → ι → ℝ}
  (hF : ContMDiff I (modelWithCornersSelf ℝ (ι → ℝ)) (↑⊤) F)
  (hcomm : ∀ (i j : ι) (x : M), σ.poissonBracket (fun x => F x i) (fun x => F x j) x = 0) {x : M}
  (hreg :
    ∀ y ∈ connectedComponentIn (F ⁻¹' {F x}) x,
      TauCeti.IsRegularPoint I (modelWithCornersSelf ℝ (ι → ℝ)) F y)
  (hdim : 2 * Fintype.card ι = Module.finrank ℝ E)
  (hK : IsCompact (connectedComponentIn (F ⁻¹' {F x}) x)) :
  Nonempty (↑(connectedComponentIn (F ⁻¹' {F x}) x) ≃ₜ UnitAddTorus ι)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [The inverse function theorem for manifolds](../manifold/part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Torus.html#TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Torus.html#TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.nonempty_homeomorph_unitAddTorus` in TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Torus.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Torus.lean#L109)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
