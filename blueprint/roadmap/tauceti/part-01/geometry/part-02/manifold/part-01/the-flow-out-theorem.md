---
declaration: theorem
origin: cited
lean: TauCeti.isLocalDiffeomorph_globalFlow_comp
statement: formalized
proof: formalized
---

# The flow-out theorem

Let `v` be a complete `C^n` vector field, `1 ≤ n`, on a
finite-dimensional boundaryless `C^n` manifold `M`, with flow `ψ`, and let `ι : S → M` be a `C^n`
immersion of a boundaryless `C^n` manifold of one dimension less, with `v` transverse to it:
`v (ι s)` is never in the image of `dι` at `s`. Then the flow-out `(t, s) ↦ ψₜ (ι s)` is a `C^n`
local diffeomorphism `ℝ × S → M`.

```lean
TauCeti.isLocalDiffeomorph_globalFlow_comp.{u_1, u_2, u_3, u_4, u_5, u_6} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [BoundarylessManifold I M] {v : (x : M) → TangentSpace I x}
  {E' : Type u_4} {H' : Type u_5} {S : Type u_6} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} [TopologicalSpace S] [ChartedSpace H' S]
  (hc : TauCeti.IsCompleteVectorField v) {ι : S → M} [BoundarylessManifold J S] {n : ℕ∞}
  (hn : 1 ≤ n) [IsManifold I 1 M] [IsManifold I (↑n) M] [IsManifold J (↑n) S]
  (hv : ContMDiff I I.tangent ↑n fun x => ⟨x, v x⟩) (hι : ContMDiff J I (↑n) ι)
  (himm : ∀ (s : S), Function.Injective ⇑(mfderiv% ι s)) (htr : TauCeti.IsTransverseAlong J v ι)
  (hdim : Module.finrank ℝ E = Module.finrank ℝ E' + 1) :
  IsLocalDiffeomorph ((modelWithCornersSelf ℝ ℝ).prod J) I ↑n fun p =>
    (TauCeti.globalFlow v ⋯ hc).toFun p.1 (ι p.2)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../part-02/the-inverse-function-theorem-for-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isLocalDiffeomorph_globalFlow_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/FlowOut.html#TauCeti.isLocalDiffeomorph_globalFlow_comp).

## Sources

- [Tau Ceti documentation: `TauCeti.isLocalDiffeomorph_globalFlow_comp`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Flow/FlowOut.html#TauCeti.isLocalDiffeomorph_globalFlow_comp)
- [Source of `TauCeti.isLocalDiffeomorph_globalFlow_comp` in TauCeti/Geometry/Manifold/Flow/FlowOut.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Flow/FlowOut.lean#L87)
