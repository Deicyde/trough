---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval₂_mfderiv_eq_of_isCompact
statement: formalized
proof: formalized
---

# Local action-angle coordinates near a compact regular component of a level

On a
symplectic manifold of dimension `2 · |ι|`, let `F` be a smooth family of pairwise
Poisson-commuting functions, and let the connected component `L` of `x` in its level `F⁻¹(F x)` be
compact and consist of regular points of `F`. The Hamiltonian vector fields of the `F_i` need not
be complete. Then there are a map `Ψ : ℝ^ι × ℝ^ι → M`, action variables `A`, a local
diffeomorphism at `F x`, and an open neighbourhood `U` of `F x` such that the angles
`θ ↦ Ψ(θ, F x)` sweep out `L`, and for all `c, c' ∈ U` and all angles `θ`:

* `F (Ψ(θ, c)) = c`;
* `Ψ` is a local diffeomorphism at `(θ, c)`;
* `Ψ` pulls `σ` back to `∑ᵢ dθᵢ ∧ dAᵢ` at `(θ, c)`;
* `Ψ(θ, c) = Ψ(θ', c')` exactly when `c' = c` and `θ' - θ ∈ 2πℤ^ι`.

So `(θ mod 2π, A)` are action-angle coordinates on a neighbourhood of `L`, in which
`σ = ∑ᵢ dθᵢ ∧ dIᵢ` with `I = A`.

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval₂_mfderiv_eq_of_isCompact.{u_1,
    u_2, u_3, u_4}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M]
  [BoundarylessManifold I M] {σ : TauCeti.SmoothTwoForm I M} {ι : Type u_4} [Fintype ι]
  {F : M → ι → ℝ} (hσ : σ.IsSymplectic) (hF : ContMDiff I (modelWithCornersSelf ℝ (ι → ℝ)) (↑⊤) F)
  (hcomm : ∀ (i j : ι) (x : M), σ.poissonBracket (fun x => F x i) (fun x => F x j) x = 0)
  (hdim : 2 * Fintype.card ι = Module.finrank ℝ E) {x : M}
  (hreg :
    ∀ y ∈ connectedComponentIn (F ⁻¹' {F x}) x,
      TauCeti.IsRegularPoint I (modelWithCornersSelf ℝ (ι → ℝ)) F y)
  (hK : IsCompact (connectedComponentIn (F ⁻¹' {F x}) x)) :
  ∃ Ψ A U,
    IsOpen U ∧
      F x ∈ U ∧
        IsLocalDiffeomorphAt (modelWithCornersSelf ℝ (ι → ℝ)) (modelWithCornersSelf ℝ (ι → ℝ)) (↑⊤)
            A (F x) ∧
          (Set.range fun θ => Ψ (θ, F x)) = connectedComponentIn (F ⁻¹' {F x}) x ∧
            ∀ c ∈ U,
              (∀ (θ : ι → ℝ), F (Ψ (θ, c)) = c) ∧
                (∀ (θ : ι → ℝ),
                    IsLocalDiffeomorphAt (modelWithCornersSelf ℝ ((ι → ℝ) × (ι → ℝ))) I (↑⊤) Ψ
                      (θ, c)) ∧
                  (∀ (θ a a' b b' : ι → ℝ),
                      TauCeti.SmoothBundleForm.eval₂ σ (Ψ (θ, c)) ((mfderiv% Ψ (θ, c)) (a, b))
                          ((mfderiv% Ψ (θ, c)) (a', b')) =
                        ∑ i,
                          (a i * (fderiv ℝ (fun c => A c i) c) b' -
                            a' i * (fderiv ℝ (fun c => A c i) c) b)) ∧
                    ∀ c' ∈ U,
                      ∀ (θ θ' : ι → ℝ),
                        Ψ (θ, c) = Ψ (θ', c') ↔ c' = c ∧ ∃ m, θ' = θ + fun i => 2 * Real.pi * ↑(m i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [A maximal integral curve confined to a compact set is defined for all time](../../part-01/geodesics-the-exponential-map-and-the-hopf-rinow/a-maximal-integral-curve-confined-to-a-compact-s.md)
- [Cartan's magic formula](../manifold/part-01/cartans-magic-formula.md)
- [The inverse function theorem for manifolds](../manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Poincaré lemma](../../../analysis/part-03/calculus/part-02/the-poincare-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval₂_mfderiv_eq_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/Chart.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval%E2%82%82_mfderiv_eq_of_isCompact).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval₂_mfderiv_eq_of_isCompact`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/Chart.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval%E2%82%82_mfderiv_eq_of_isCompact)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.exists_isLocalDiffeomorphAt_eval₂_mfderiv_eq_of_isCompact` in TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/Chart.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/Chart.lean#L263)
- [Tau Ceti roadmap status: Symplectic geometry and Hamiltonian mechanics](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SymplecticGeometry/STATUS.md)
