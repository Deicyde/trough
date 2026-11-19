---
declaration: theorem
origin: cited
lean: TauCeti.exists_mlogDeriv_coe_eq
statement: formalized
proof: formalized
---

# Closed imaginary forms with periods in `2πiℤ` are logarithmic derivatives of circle-valued maps

A smooth closed imaginary `1`-form whose integrals over singular `1`-cycles lie in `2πiℤ`
is `dlog u` for a smooth map `u : M → U(1)`.

```lean
TauCeti.exists_mlogDeriv_coe_eq.{u_1, u_2} {E : Type u_1} {H : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} {M : Type}
  [TopologicalSpace M] [ChartedSpace H M] [FiniteDimensional ℝ E] [T2Space M] [IsManifold I (↑⊤) M]
  {φ : TauCeti.RoughForm I M ℂ 1} (hφ : TauCeti.IsSmoothForm I (↑⊤) φ)
  (hclosed : TauCeti.mextDeriv φ = 0)
  (hre : ∀ (x : M) (v : Fin 1 → TangentSpace I x), ((φ x) v).re = 0)
  (hper :
    ∀ (c : ↑(HomologicalComplex.homology ((TauCeti.singularChains ℤ).obj ↧M) 1)),
      ∃ n, (TauCeti.homologyPeriodHom φ) c = ↑n * (2 * ↑Real.pi * Complex.I)) :
  ∃ u, (TauCeti.mlogDeriv I fun x => ↑(u x)) = φ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Poincaré lemma on manifolds](../../../geometry/part-02/manifold/part-03/the-poincare-lemma-on-manifolds.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_mlogDeriv_coe_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/LogDeriv.html#TauCeti.exists_mlogDeriv_coe_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_mlogDeriv_coe_eq`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/DeRham/LogDeriv.html#TauCeti.exists_mlogDeriv_coe_eq)
- [Source of `TauCeti.exists_mlogDeriv_coe_eq` in TauCeti/Geometry/Manifold/DeRham/LogDeriv.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/DeRham/LogDeriv.lean#L465)
- [Tau Ceti roadmap status: Four-dimensional Seiberg–Witten theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SeibergWittenTheory/STATUS.md)
