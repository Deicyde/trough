---
declaration: theorem
origin: cited
lean: TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle
statement: formalized
proof: formalized
---

# The Liouville–Arnold theorem in action–angle form

On a symplectic manifold of dimension
`2 · |ι|`, let `F` be a smooth family of pairwise Poisson-commuting functions, and let the
connected component `L` of `x` in its level `F⁻¹(F x)` be compact and consist of regular points of
`F`. The Hamiltonian vector fields of the `F_i` need not be complete. Then for every period `p > 0`
there are an open neighbourhood `U` of `L`, an open set `D` of actions, a map `Φ` into the
cotangent bundle of the torus `ι → AddCircle p` and a smooth function `h` on `D` such that `Φ` is
injective on `U`, a local diffeomorphism at every point of `U`, maps `U` onto the covectors whose
actions `ξ(e_i)` lie in `D`, pulls the canonical symplectic form back to `σ` on `U`, and turns `F`
into the function `h` of the actions.

```lean
TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle.{u_1, u_2, u_3, u_4} {E : Type u_1}
  {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M]
  [ChartedSpace H M] [IsManifold I (↑⊤) M] [T2Space M] {σ : TauCeti.SmoothTwoForm I M}
  {ι : Type u_4} [Fintype ι] [DecidableEq ι] {F : M → ι → ℝ} (hσ : σ.IsSymplectic)
  (hF : ContMDiff I (modelWithCornersSelf ℝ (ι → ℝ)) (↑⊤) F)
  (hcomm : ∀ (i j : ι) (x : M), σ.poissonBracket (fun x => F x i) (fun x => F x j) x = 0)
  (hdim : 2 * Fintype.card ι = Module.finrank ℝ E) {x : M}
  (hreg :
    ∀ y ∈ connectedComponentIn (F ⁻¹' {F x}) x,
      TauCeti.IsRegularPoint I (modelWithCornersSelf ℝ (ι → ℝ)) F y)
  (hK : IsCompact (connectedComponentIn (F ⁻¹' {F x}) x)) (p : ℝ) [Fact (0 < p)] :
  ∃ U D Φ h,
    IsOpen U ∧
      connectedComponentIn (F ⁻¹' {F x}) x ⊆ U ∧
        IsOpen D ∧
          Set.InjOn Φ U ∧
            Φ '' U = {z | (fun i => z.snd (Pi.single i 1)) ∈ D} ∧
              (∀ y ∈ U,
                  IsLocalDiffeomorphAt I
                    ((ModelWithCorners.pi fun x => modelWithCornersSelf ℝ ℝ).prod
                      (modelWithCornersSelf ℝ ((ι → ℝ) →L[ℝ] ℝ)))
                    (↑⊤) Φ y) ∧
                (∀ y ∈ U,
                    ∀ (v w : TangentSpace I y),
                      TauCeti.SmoothBundleForm.eval₂
                          (TauCeti.CotangentBundle.symplecticForm
                            (ModelWithCorners.pi fun x => modelWithCornersSelf ℝ ℝ)
                            (ι → AddCircle p))
                          (Φ y) ((mfderiv% Φ y) v) ((mfderiv% Φ y) w) =
                        TauCeti.SmoothBundleForm.eval₂ σ y v w) ∧
                  ContDiffOn ℝ (↑⊤) h D ∧ ∀ y ∈ U, F y = h fun i => (Φ y).snd (Pi.single i 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../../manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [Local action-angle coordinates near a compact regular component of a level](../../symplectic-geometry-and-hamiltonian-mechanics/local-action-angle-coordinates-near-a-compact-re.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/NormalForm.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle`](https://taucetiproject.org/docs/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/NormalForm.html#TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle)
- [Source of `TauCeti.SmoothTwoForm.IsSymplectic.exists_actionAngle` in TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/NormalForm.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Symplectic/Hamiltonian/Liouville/Action/NormalForm.lean#L195)
