---
declaration: theorem
origin: cited
lean: AnalyticAt.exists_openPartialHomeomorph
statement: formalized
proof: formalized
---

# The analytic inverse function theorem

A map analytic at `a`, whose derivative at `a` is a
continuous linear equivalence, coincides with an `OpenPartialHomeomorph` whose source is a
neighbourhood of `a` inside any prescribed neighbourhood `s`, which is analytic on its source, and
whose inverse is analytic on its target.

```lean
AnalyticAt.exists_openPartialHomeomorph.{u_1, u_2, u_3} {𝕜 : Type u_1} [NontriviallyNormedField 𝕜]
  {E : Type u_2} [NormedAddCommGroup E] [NormedSpace 𝕜 E] [CompleteSpace E] {F : Type u_3}
  [NormedAddCommGroup F] [NormedSpace 𝕜 F] {f : E → F} {a : E} (hf : AnalyticAt 𝕜 f a)
  {L : E ≃L[𝕜] F} (hL : fderiv 𝕜 f a = ↑L) {s : Set E} (hs : s ∈ nhds a) :
  ∃ Θ,
    ↑Θ = f ∧
      a ∈ Θ.source ∧ Θ.source ⊆ s ∧ AnalyticOnNhd 𝕜 f Θ.source ∧ AnalyticOnNhd 𝕜 (↑Θ.symm) Θ.target
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AnalyticAt.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#AnalyticAt.exists_openPartialHomeomorph).

## Sources

- [Tau Ceti documentation: `AnalyticAt.exists_openPartialHomeomorph`](https://taucetiproject.org/docs/TauCeti/Analysis/Analytic/Inverse.html#AnalyticAt.exists_openPartialHomeomorph)
- [Source of `AnalyticAt.exists_openPartialHomeomorph` in TauCeti/Analysis/Analytic/Inverse.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Analytic/Inverse.lean#L102)
