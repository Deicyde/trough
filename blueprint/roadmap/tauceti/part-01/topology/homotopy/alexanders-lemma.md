---
declaration: def
origin: cited
lean: Homeomorph.alexanderIsotopyClosedBall
statement: formalized
---

# Alexander's lemma

A homeomorphism of the closed unit ball fixing the unit sphere is
joined to the identity through homeomorphisms of the ball fixing the sphere.

```lean
Homeomorph.alexanderIsotopyClosedBall.{u_1} {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E]
  (f : ↑(Metric.closedBall 0 1) ≃ₜ ↑(Metric.closedBall 0 1))
  (hf : ∀ (x : ↑(Metric.closedBall 0 1)), ‖↑x‖ = 1 → f x = x) :
  TauCeti.AmbientIsotopy ↑(Metric.closedBall 0 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Homeomorph.alexanderIsotopyClosedBall`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Isotopy/Alexander.html#Homeomorph.alexanderIsotopyClosedBall).

## Sources

- [Tau Ceti documentation: `Homeomorph.alexanderIsotopyClosedBall`](https://taucetiproject.org/docs/TauCeti/Topology/Homotopy/Isotopy/Alexander.html#Homeomorph.alexanderIsotopyClosedBall)
- [Source of `Homeomorph.alexanderIsotopyClosedBall` in TauCeti/Topology/Homotopy/Isotopy/Alexander.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Topology/Homotopy/Isotopy/Alexander.lean#L130)
