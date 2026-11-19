---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient
statement: formalized
proof: formalized
---

# The Yamabe invariant is at most that of the sphere

On a nonempty Riemannian manifold
without boundary of dimension `n > 2`, a lower bound `c` for the Yamabe quotient of all
nonnegative smooth compactly supported functions with positive critical mass satisfies
`c ≤ Y(Sⁿ)`.

```lean
TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient.{u_1, u_2, u_3} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [SigmaCompactSpace M] [IsManifold I (↑⊤) M] [MeasurableSpace M]
  [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [I.Boundaryless] [Nonempty M]
  (hn : 2 < Module.finrank ℝ E) {c : ℝ}
  (hc :
    ∀ (u : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) u →
        HasCompactSupport u →
          (∀ (x : M), 0 ≤ u x) →
            0 <
                ∫ (x : M),
                  |u x| ^
                    TauCeti.Yamabe.criticalExponent
                      (Module.finrank ℝ E) ∂TauCeti.riemannianVolume I M →
              c ≤ TauCeti.Yamabe.yamabeQuotient I u) :
  c ≤ TauCeti.Yamabe.sphereYamabeConstant (Module.finrank ℝ E)
```

## Depends on

- [TauCeti.Yamabe.yamabeQuotient](tauceti-yamabe-yamabequotient.md)

## Proof depends on

- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/UpperBound.html#TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/UpperBound.html#TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient)
- [Source of `TauCeti.Yamabe.le_sphereYamabeConstant_of_forall_le_yamabeQuotient` in TauCeti/Analysis/PDE/Yamabe/UpperBound.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Yamabe/UpperBound.lean#L586)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
