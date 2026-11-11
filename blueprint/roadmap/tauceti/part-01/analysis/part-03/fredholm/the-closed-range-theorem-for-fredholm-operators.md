---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker
statement: formalized
proof: formalized
---

# The closed range theorem for Fredholm operators

The range of the transpose of a Fredholm
operator `T` is the annihilator of `ker T`: a continuous functional on `E` is of the form `ψ ∘ T`
for a continuous functional `ψ` on `F` exactly when it vanishes on `ker T`. Unlike the closed
range theorem `ContinuousLinearMap.range_precomp_eq_orthogonalBilin_ker` for Banach spaces, this
holds between arbitrary topological vector spaces.

```lean
ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker.{u_1, u_2, u_3} {𝕜 : Type u_1}
  {E : Type u_2} {F : Type u_3} [NontriviallyNormedField 𝕜] [AddCommGroup E] [_root_.Module 𝕜 E]
  [TopologicalSpace E] [AddCommGroup F] [_root_.Module 𝕜 F] [TopologicalSpace F] [CompleteSpace 𝕜]
  [IsTopologicalAddGroup E] [IsTopologicalAddGroup F] [ContinuousSMul 𝕜 F] {T : E →L[𝕜] F}
  (hT : T.IsFredholm) :
  (↑(ContinuousLinearMap.precomp 𝕜 T)).range =
    Submodule.orthogonalBilin (topDualPairing 𝕜 E).flip (↑T).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Transpose.html#ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker`](https://taucetiproject.org/docs/TauCeti/Analysis/Fredholm/Transpose.html#ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker)
- [Source of `ContinuousLinearMap.IsFredholm.range_precomp_eq_orthogonalBilin_ker` in TauCeti/Analysis/Fredholm/Transpose.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fredholm/Transpose.lean#L87)
