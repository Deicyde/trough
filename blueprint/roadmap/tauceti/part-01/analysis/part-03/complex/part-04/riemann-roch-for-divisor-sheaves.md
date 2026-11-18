---
declaration: theorem
origin: cited
lean: TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic
statement: formalized
proof: formalized
---

# Riemann–Roch for divisor sheaves

On a compact connected Riemann surface with
finite-dimensional `H¹(X, 𝒪)`, every divisor `D` satisfies
`h⁰(D) - h¹(D) = deg D + 1 - g_an`.

```lean
TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic {X : Type} [TopologicalSpace X]
  [ChartedSpace ℂ X] [IsManifold (modelWithCornersSelf ℂ ℂ) 1 X] [CompactSpace X] [T2Space X]
  [ConnectedSpace X]
  [FiniteDimensional ℂ
      ↑((TauCeti.Topology.cechCohomology (↧X) (ModuleCat ℂ) 1).obj
          (TauCeti.holomorphicStructureSheafModules (modelWithCornersSelf ℂ ℂ) X).obj)]
  (D : TauCeti.AlgebraicGeometry.WeilDivisor X) :
  ↑(Module.finrank ℂ ↑((TauCeti.RiemannSurface.divisorSheaf D).obj.obj (Opposite.op ⊤))) -
      ↑(Module.finrank ℂ ↑(TauCeti.RiemannSurface.divisorCechCohomology D 1)) =
    TauCeti.AlgebraicGeometry.WeilDivisor.degree D + 1 - ↑(TauCeti.RiemannSurface.analyticGenus X)
```

## Depends on

- [TauCeti.RiemannSurface.divisorSheaf](../../../../number-theory/part-01/modular-forms-hecke-theory-newforms-and-l-functi/tauceti-riemannsurface-divisorsheaf.md)
- [TauCeti.Topology.cechCohomology](../../../../../part-02/topology/topological-sheaf-cohomology-and-native-comparis/tauceti-topology-cechcohomology.md)

## Proof depends on

- [The connecting map of Čech cohomology](../../../../../part-02/topology/topological-sheaf-cohomology-and-native-comparis/the-connecting-map-of-cech-cohomology.md)
- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)
- [TauCeti.RiemannSurface.finrank_pointTwist_euler_characteristic](../../../../number-theory/part-01/modular-forms-hecke-theory-newforms-and-l-functi/tauceti-riemannsurface-finrank-pointtwist-euler.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/RiemannRoch.html#TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic).

## Sources

- [Tau Ceti documentation: `TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/RiemannSurface/Divisor/RiemannRoch.html#TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic)
- [Source of `TauCeti.RiemannSurface.finrank_divisorSheaf_euler_characteristic` in TauCeti/Analysis/Complex/RiemannSurface/Divisor/RiemannRoch.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/RiemannSurface/Divisor/RiemannRoch.lean#L88)
