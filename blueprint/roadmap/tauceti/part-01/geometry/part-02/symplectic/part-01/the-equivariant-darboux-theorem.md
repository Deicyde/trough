---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart
statement: formalized
proof: formalized
---

# The equivariant Darboux theorem

Let a compact group `G`, a manifold without boundary, act
smoothly on a finite-dimensional manifold `M` without boundary, preserving a symplectic form
`form`, and let `x₀` be a fixed point. Then there is a smooth chart `chart` of `M` around `x₀`,
with values in `E = T_{x₀} M` and `chart x₀ = 0`, whose source is `G`-invariant, in which `G` acts
through its isotropy representation `g ↦ d(g • ·)_{x₀}`, and which pulls the constant form
`form_{x₀}` back to `form`. A point of the source is fixed by `G` exactly when its image is fixed
by the isotropy representation.

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart.{u_1, u_2, u_3, u_4, u_5, u_6}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [I.Boundaryless] [IsManifold I (↑⊤) M] {EG : Type u_4} {HG : Type u_5}
  {G : Type u_6} [NormedAddCommGroup EG] [NormedSpace ℝ EG] [TopologicalSpace HG]
  {IG : ModelWithCorners ℝ EG HG} [IG.Boundaryless] [TopologicalSpace G] [ChartedSpace HG G]
  [IsManifold IG (↑⊤) G] [Group G] [IsTopologicalGroup G] [CompactSpace G] [MulAction G M]
  [ContMDiffSMul IG I (↑⊤) G M] {form : TauCeti.SmoothTwoForm I M} (hform : form.IsSymplectic)
  (hG : ∀ (g : G), (TauCeti.SmoothForm.mpullback (fun y => g • y) ⋯) form = form) {x₀ : M}
  (hx₀ : ∀ (g : G), g • x₀ = x₀) :
  ∃ chart,
    x₀ ∈ chart.source ∧
      ↑chart.toPartialEquiv x₀ = 0 ∧
        (∀ (g : G),
            ∀ x ∈ chart.source,
              g • x ∈ chart.source ∧
                ↑chart.toPartialEquiv (g • x) =
                  ((mfderiv% fun x => g • x) x₀) (↑chart.toPartialEquiv x)) ∧
          (∀ x ∈ chart.source,
              ∀ (v w : TangentSpace I x),
                TauCeti.SmoothBundleForm.eval₂ form x v w =
                  (fun v w => ((⋯.symplecticFormAt x₀).toBilinForm v) w)
                    ((d% ↑chart.toPartialEquiv x) v) ((d% ↑chart.toPartialEquiv x) w)) ∧
            ∀ x ∈ chart.source,
              (∀ (g : G), g • x = x) ↔
                ∀ (g : G),
                  ((mfderiv% fun x => g • x) x₀) (↑chart.toPartialEquiv x) = ↑chart.toPartialEquiv x
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Darboux's theorem](darbouxs-theorem.md)
- [The inverse function theorem for a converging family](../../../../analysis/part-03/calculus/part-01/the-inverse-function-theorem-for-a-converging-fa.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/EquivariantDarboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Manifold/EquivariantDarboux.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.exists_equivariant_darbouxChart` in TauCeti/Geometry/Symplectic/Manifold/EquivariantDarboux.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Manifold/EquivariantDarboux.lean#L137)
