---
declaration: theorem
origin: cited
lean: ContMDiff.isInvolutiveDistribution_ker_mfderiv
statement: formalized
proof: formalized
---

# ContMDiff.isInvolutiveDistribution_ker_mfderiv

The differential kernels of a sufficiently smooth map form an involutive distribution.
In particular this applies to the vertical distribution of a smooth submersion, without
requiring surjectivity or constant rank for this conclusion.

```lean
ContMDiff.isInvolutiveDistribution_ker_mfderiv.{u_1, u_2, u_3, u_4, u_5, u_6, u_7} {𝕜 : Type u_1}
  [NontriviallyNormedField 𝕜] {n : WithTop ℕ∞} {E : Type u_2} [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [CompleteSpace E] {H : Type u_3} [TopologicalSpace H]
  {I : ModelWithCorners 𝕜 E H} {M : Type u_4} [TopologicalSpace M] [ChartedSpace H M]
  [IsManifold I (minSmoothness 𝕜 2) M] {F : Type u_5} [NormedAddCommGroup F] [NormedSpace 𝕜 F]
  [CompleteSpace F] {G : Type u_6} [TopologicalSpace G] {J : ModelWithCorners 𝕜 F G} {N : Type u_7}
  [TopologicalSpace N] [ChartedSpace G N] [IsManifold J (minSmoothness 𝕜 2) N] {f : M → N}
  (hf : ContMDiff I J n f) (hn : minSmoothness 𝕜 2 ≤ n) :
  TauCeti.IsInvolutiveDistribution I fun x => (↑(mfderiv% f x)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContMDiff.isInvolutiveDistribution_ker_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Kernel.html#ContMDiff.isInvolutiveDistribution_ker_mfderiv).

## Sources

- [Tau Ceti documentation: `ContMDiff.isInvolutiveDistribution_ker_mfderiv`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Distribution/Kernel.html#ContMDiff.isInvolutiveDistribution_ker_mfderiv)
- [Source of `ContMDiff.isInvolutiveDistribution_ker_mfderiv` in TauCeti/Geometry/Manifold/Distribution/Kernel.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Distribution/Kernel.lean#L99)
- [Tau Ceti roadmap status: Lie algebroids, Lie groupoids and Poisson geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/LieGroupoidsPoisson/STATUS.md)
