---
declaration: theorem
origin: cited
lean: TauCeti.Manifold.SobolevH1.inner_ofSmooth_right
statement: formalized
proof: formalized
---

# Green's identity on `H¹(M)`

On a closed manifold with a `C¹` metric, for `w ∈ H¹(M)` and a
smooth function `φ`, `⟪w, φ⟫_{H¹} = ∫ w (φ - Δφ) dV`, where `Δ = div grad`.

```lean
TauCeti.Manifold.SobolevH1.inner_ofSmooth_right.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] {H : Type u_2} [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [CompactSpace M] [IsManifold I 1 M] [MeasurableSpace M] [BorelSpace M]
  [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [I.Boundaryless] [IsManifold I (↑⊤) M]
  [T2Space M] [IsContMDiffRiemannianBundle I 1 E fun x => TangentSpace I x]
  (w : TauCeti.Manifold.SobolevH1 I M) (φ : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤) :
  inner ℝ w (TauCeti.Manifold.SobolevH1.ofSmooth φ) =
    ∫ (x : M),
      ↑↑(TauCeti.Manifold.SobolevH1.toLp w) x *
        (φ x - TauCeti.Manifold.laplaceBeltrami I (⇑φ) x) ∂TauCeti.riemannianVolume I M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Green's first identity on a manifold without boundary](../part-01/greens-first-identity-on-a-manifold-without-boun.md)
- [The Koszul formula](the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Manifold.SobolevH1.inner_ofSmooth_right`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/H1.html#TauCeti.Manifold.SobolevH1.inner_ofSmooth_right).

## Sources

- [Tau Ceti documentation: `TauCeti.Manifold.SobolevH1.inner_ofSmooth_right`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Riemannian/Sobolev/H1.html#TauCeti.Manifold.SobolevH1.inner_ofSmooth_right)
- [Source of `TauCeti.Manifold.SobolevH1.inner_ofSmooth_right` in TauCeti/Geometry/Manifold/Riemannian/Sobolev/H1.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Riemannian/Sobolev/H1.lean#L364)
