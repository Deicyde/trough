---
declaration: theorem
origin: cited
lean: TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq
statement: formalized
proof: formalized
---

# The Euler–Lagrange equation of the Yamabe quotient

On a closed manifold of dimension
`n > 2`, a nonzero `C²` function `u` is a critical point of the Yamabe quotient, in the sense that
`t ↦ Q_g(u + t v)` has derivative `0` at `t = 0` for every smooth `v`, exactly when it solves
`L_g u = λ |u| ^ (pₙ - 2) u` for some constant `λ`.

```lean
TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq.{u_1, u_2,
    u_3}
  {E : Type u_1} [NormedAddCommGroup E] [NormedSpace ℝ E] [FiniteDimensional ℝ E] {H : Type u_2}
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type u_3} [TopologicalSpace M]
  [ChartedSpace H M] [T2Space M] [SigmaCompactSpace M] [IsManifold I (↑⊤) M] [MeasurableSpace M]
  [BorelSpace M] [Bundle.RiemannianBundle fun x => TangentSpace I x]
  [IsContMDiffRiemannianBundle I (↑⊤) E fun x => TangentSpace I x]
  [IsContinuousRiemannianBundle E fun x => TangentSpace I x] [CompactSpace M] [I.Boundaryless]
  (hn : 2 < Module.finrank ℝ E) {u : M → ℝ} (hu : ContMDiff I (modelWithCornersSelf ℝ ℝ) 2 u)
  (hu0 : u ≠ 0) :
  (∀ (v : M → ℝ),
      ContMDiff I (modelWithCornersSelf ℝ ℝ) (↑⊤) v →
        HasDerivAt (fun t => TauCeti.Yamabe.yamabeQuotient I (u + t • v)) 0 0) ↔
    ∃ c,
      ∀ (x : M),
        TauCeti.Yamabe.conformalLaplacian I u x =
          c * (|u x| ^ (TauCeti.Yamabe.criticalExponent (Module.finrank ℝ E) - 2) * u x)
```

## Depends on

- [TauCeti.Yamabe.yamabeQuotient](tauceti-yamabe-yamabequotient.md)

## Proof depends on

- [Green's first identity on a manifold without boundary](../../../geometry/part-02/manifold/part-02/greens-first-identity-on-a-manifold-without-boun.md)
- [The Koszul formula](../../../geometry/part-02/manifold/part-03/the-koszul-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Quotient.html#TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Yamabe/Quotient.html#TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq)
- [Source of `TauCeti.Yamabe.forall_hasDerivAt_yamabeQuotient_add_smul_iff_exists_conformalLaplacian_eq` in TauCeti/Analysis/PDE/Yamabe/Quotient.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Yamabe/Quotient.lean#L369)
- [Tau Ceti roadmap status: The Yamabe problem and conformal scalar curvature](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Yamabe/STATUS.md)
