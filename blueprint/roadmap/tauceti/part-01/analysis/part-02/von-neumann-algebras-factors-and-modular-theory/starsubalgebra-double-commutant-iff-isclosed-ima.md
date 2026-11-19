---
declaration: theorem
origin: cited
lean: StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM
statement: formalized
proof: formalized
---

# StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM

A unital star subalgebra equals its double commutant if and only if it is
strong operator closed.

```lean
StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM.{u_1, u_2}
  {𝕜 : Type u_1} {H : Type u_2} [RCLike 𝕜] [NormedAddCommGroup H] [InnerProductSpace 𝕜 H]
  [CompleteSpace H] (S : StarSubalgebra 𝕜 (H →L[𝕜] H)) :
  (↑S).centralizer.centralizer = ↑S ↔
    IsClosed (⇑(ContinuousLinearMap.toPointwiseConvergenceCLM 𝕜 (RingHom.id 𝕜) H H) '' ↑S)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The von Neumann density theorem](../../part-04/other-results/the-von-neumann-density-theorem.md)

## Lean

Formalized in Tau Ceti as [`StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.html#StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM).

## Sources

- [Tau Ceti documentation: `StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.html#StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM)
- [Source of `StarSubalgebra.double_commutant_iff_isClosed_image_toPointwiseConvergenceCLM` in TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.lean#L179)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
