---
declaration: theorem
origin: cited
lean: VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall
statement: formalized
proof: formalized
---

# VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall

Every closed norm ball of a concrete von Neumann algebra is weak operator compact; in
particular, so is its unit ball.

```lean
VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall.{u_1} {H : Type u_1} [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] (M : VonNeumannAlgebra H) (A : H →L[ℂ] H) (r : ℝ) :
  IsCompact (ContinuousLinearMapWOT.ofCLM '' (↑M ∩ Metric.closedBall A r))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The bicommutant theorem](the-bicommutant-theorem.md)
- [Weak operator compactness of operator balls](weak-operator-compactness-of-operator-balls.md)

## Lean

Formalized in Tau Ceti as [`VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.html#VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall).

## Sources

- [Tau Ceti documentation: `VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.html#VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall)
- [Source of `VonNeumannAlgebra.isCompact_image_ofCLM_inter_closedBall` in TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/VonNeumannAlgebra/Bicommutant.lean#L201)
- [Tau Ceti roadmap status: Von Neumann algebras, factors, and modular theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/VonNeumannAlgebras/STATUS.md)
