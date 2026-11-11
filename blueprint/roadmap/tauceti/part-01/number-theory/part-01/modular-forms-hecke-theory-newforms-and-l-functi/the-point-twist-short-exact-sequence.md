---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.pointTwistSequence_shortExact
statement: formalized
proof: formalized
---

# The point-twist short exact sequence

**The point-twist short exact sequence** of divisor sheaves on a Riemann surface,
`0 → O(D) → O(D+x) → C_x → 0`, using local coefficient extraction at `x`.

```lean
TauCeti.RiemannSurface.pointTwistSequence_shortExact.{u} {X : Type u} [TopologicalSpace X]
  [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X]
  (D : TauCeti.AlgebraicGeometry.WeilDivisor X) (x : X)
  [(U : TopologicalSpace.Opens X) → Decidable (x ∈ U)] :
  (TauCeti.RiemannSurface.pointTwistSequence D x).ShortExact
```

## Depends on

- [TauCeti.RiemannSurface.divisorSheaf](tauceti-riemannsurface-divisorsheaf.md)

## Proof depends on

- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.pointTwistSequence_shortExact`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/PointTwist.html#TauCeti.RiemannSurface.pointTwistSequence_shortExact).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.pointTwistSequence_shortExact`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/PointTwist.html#TauCeti.RiemannSurface.pointTwistSequence_shortExact)
- [Source of `TauCeti.RiemannSurface.pointTwistSequence_shortExact` in TauCeti/Analysis/Complex/RiemannSurface/Divisor/PointTwist.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/RiemannSurface/Divisor/PointTwist.lean#L501)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ModularForms/STATUS.md)
