---
declaration: theorem
origin: cited
lean: TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt
statement: formalized
proof: formalized
---

# The joint holomorphic implicit function theorem in charts

Suppose `G : M × N → P` is
holomorphic near `u`, and the partial derivative in the `N` coordinate of its representative in
holomorphic charts `e`, `d`, `c` is invertible at `u`. There is a solution `ψ : M × P → N`,
holomorphic near `(u.1, G u)`, taking that point to `u.2`. Near `(u, G u)`, the equation
`G (z, v) = w` is equivalent to `ψ (z, w) = v`. In particular solutions sufficiently near `u.2`
are unique. Only the parameter and unknown model spaces need be assumed finite-dimensional;
invertibility of the partial derivative forces the level model to have the same dimension as
the unknown model. No separation or global countability assumptions are needed.

```lean
TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {F : Type u_2} {K : Type u_3} [NormedAddCommGroup E] [NormedSpace ℂ E]
  [FiniteDimensional ℂ E] [NormedAddCommGroup F] [NormedSpace ℂ F] [FiniteDimensional ℂ F]
  [NormedAddCommGroup K] [NormedSpace ℂ K] {M : Type u_4} {N : Type u_5} {P : Type u_6}
  [TopologicalSpace M] [ChartedSpace E M] [TopologicalSpace N] [ChartedSpace F N]
  [TopologicalSpace P] [ChartedSpace K P] {G : M × N → P} {u : M × N}
  {e : OpenPartialHomeomorph M E} {d : OpenPartialHomeomorph N F} {c : OpenPartialHomeomorph P K}
  (he : e ∈ IsManifold.maximalAtlas (modelWithCornersSelf ℂ E) 1 M)
  (hd : d ∈ IsManifold.maximalAtlas (modelWithCornersSelf ℂ F) 1 N)
  (hc : c ∈ IsManifold.maximalAtlas (modelWithCornersSelf ℂ K) 1 P) (hu : u.1 ∈ e.source)
  (hv : u.2 ∈ d.source) (hw : G u ∈ c.source) (hG : ∀ᶠ (q : M × N) in nhds u, MDiffAt G q)
  (hinv :
    (fderiv ℂ (fun q => ↑c (G (↑e.symm q.1, ↑d.symm q.2))) (↑e u.1, ↑d u.2) ∘SL
        ContinuousLinearMap.inr ℂ E F).IsInvertible) :
  ∃ ψ,
    (∀ᶠ (p : M × P) in nhds (u.1, G u), MDiffAt ψ p) ∧
      ψ (u.1, G u) = u.2 ∧
        (∀ᶠ (p : M × P) in nhds (u.1, G u), G (p.1, ψ p) = p.2) ∧
          ∀ᶠ (q : (M × N) × P) in nhds (u, G u), G q.1 = q.2 ↔ ψ (q.1.1, q.2) = q.1.2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The joint holomorphic implicit function theorem](../../../../analysis/part-02/complex/part-02/the-joint-holomorphic-implicit-function-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ImplicitFunction.html#TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Complex/ImplicitFunction.html#TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt)
- [Source of `TauCeti.exists_jointImplicitFunction_of_eventually_mdifferentiableAt` in TauCeti/Geometry/Manifold/Complex/ImplicitFunction.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Geometry/Manifold/Complex/ImplicitFunction.lean#L44)
