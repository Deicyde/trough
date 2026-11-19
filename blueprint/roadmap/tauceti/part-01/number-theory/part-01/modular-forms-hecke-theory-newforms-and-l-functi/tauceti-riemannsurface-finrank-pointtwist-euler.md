---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic
statement: formalized
proof: formalized
---

# TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic

The point-twist step of the Euler characteristic calculation: once the first cohomology
is finite-dimensional, adding a point raises `h⁰ - h¹` by one. The analytic finiteness theorem
is not assumed implicitly or asserted here.

```lean
TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic {X : Type} [TopologicalSpace X]
  [ChartedSpace ℂ X] (D : TauCeti.AlgebraicGeometry.WeilDivisor X) (x : X)
  [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [CompactSpace X] [T2Space X] [ConnectedSpace X]
  [FiniteDimensional ℂ ↑(TauCeti.RiemannSurface.divisorCechCohomology D 1)] :
  ↑(Module.finrank ℂ
          ↑((TauCeti.RiemannSurface.divisorSheaf
                    (D + TauCeti.AlgebraicGeometry.WeilDivisor.ofPoint x)).obj.obj
              (Opposite.op ⊤))) -
      ↑(Module.finrank ℂ
          ↑(TauCeti.RiemannSurface.divisorCechCohomology
              (D + TauCeti.AlgebraicGeometry.WeilDivisor.ofPoint x) 1)) =
    ↑(Module.finrank ℂ ↑((TauCeti.RiemannSurface.divisorSheaf D).obj.obj (Opposite.op ⊤))) -
        ↑(Module.finrank ℂ ↑(TauCeti.RiemannSurface.divisorCechCohomology D 1)) +
      1
```

## Depends on

- [TauCeti.RiemannSurface.divisorSheaf](tauceti-riemannsurface-divisorsheaf.md)
- [TauCeti.Topology.cechCohomology](../../../../part-02/topology/topological-sheaf-cohomology-and-native-comparis/tauceti-topology-cechcohomology.md)

## Proof depends on

- [The analytic inverse function theorem](../../../analysis/part-03/analytic/the-analytic-inverse-function-theorem.md)
- [The connecting map of Čech cohomology](../../../../part-02/topology/topological-sheaf-cohomology-and-native-comparis/the-connecting-map-of-cech-cohomology.md)
- [The identity theorem for Riemann surfaces](../../../analysis/part-03/complex/part-02/the-identity-theorem-for-riemann-surfaces.md)
- [Osgood's lemma](../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [Rouché's theorem for a disc, classical form](../../../analysis/part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [TauCeti.RiemannSurface.MeromorphicFunction](../../../field-theory/belyi-maps-dessins-denfants-and-three-point-cove/tauceti-riemannsurface-meromorphicfunction.md)
- [Taylor's formula to second order](../../../analysis/part-03/calculus/part-02/taylors-formula-to-second-order.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Cohomology/Basic.html#TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Cohomology/Basic.html#TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic)
- [Source of `TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic` in TauCeti/Analysis/Complex/RiemannSurface/Divisor/Cohomology/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Divisor/Cohomology/Basic.lean#L274)
- [Tau Ceti roadmap status: Modular forms — Hecke theory, newforms, and L-functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ModularForms/STATUS.md)
