---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace
statement: formalized
proof: formalized
---

# The normal bundle of a Morse–Bott submanifold is the sum of its negative and positive normal bundles

Let `i` be a nondegenerate critical submanifold of `f`, with `f` of class `C^{k+2}`
along it and `i` of class `C^{k+1}`, and let `g` be a `C^k` fibre metric on its normal bundle `ν`.
If the Morse indices of `f` and of `-f` are `r` and `r'` at every point of the submanifold, then
`(s, u, v) ↦ (s, u + v)` is a `C^k` diffeomorphism from the total space of the direct-sum bundle
`ν⁻ ×ᵇ ν⁺` of the negative and positive normal bundles relative to `g`
(`hasLocalContMDiffSubbundleFrames_negativeNormalSpace` and
`hasLocalContMDiffSubbundleFrames_positiveNormalSpace`) onto the total space of `ν`.

```lean
TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M] [ChartedSpace H M]
  {E' : Type u_4} {H' : Type u_5} {S : Type u_6} [NormedAddCommGroup E'] [NormedSpace ℝ E']
  [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'} [TopologicalSpace S] [ChartedSpace H' S]
  {f : M → ℝ} {n : WithTop ℕ∞} {i : TauCeti.SmoothEmbedding J I n S M} (hn : n ≠ 0) [I.Boundaryless]
  [FiniteDimensional ℝ E] [FiniteDimensional ℝ E'] {P : Type u_7} [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] {k : WithTop ℕ∞} [IsManifold I (k + 2) M]
  [IsManifold J (k + 1) S] (h : i.IsNondegenerateCriticalSubmanifold f) (hk : k + 1 ≤ n)
  (hf : ∀ (s : S), ContMDiffAt I (modelWithCornersSelf ℝ ℝ) (k + 2) f (i s))
  (hdim : Module.finrank ℝ P = Module.finrank ℝ E - Module.finrank ℝ E')
  (g : Bundle.ContMDiffRiemannianMetric J k P fun s => i.NormalSpace s hn) {r r' : ℕ}
  (hr : ∀ (s : S), TauCeti.manifoldMorseIndex I f (i s) = r)
  (hr' : ∀ (s : S), TauCeti.manifoldMorseIndex I (-f) (i s) = r') :
  ∃ Φ,
    ∀
      (v :
        Bundle.TotalSpace ((Fin r → ℝ) × (Fin r' → ℝ)) fun x =>
          ↥((fun s =>
                  TauCeti.SmoothEmbedding.IsCriticalSubmanifold.negativeNormalSpace hn ⋯
                    g.toRiemannianMetric s)
                x) ×
            ↥((fun s =>
                  TauCeti.SmoothEmbedding.IsCriticalSubmanifold.positiveNormalSpace hn ⋯
                    g.toRiemannianMetric s)
                x)),
      Φ v = ⟨v.proj, ↑v.snd.1 + ↑v.snd.2⟩
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [ContinuousLinearMap.metricChangeTransport](../../../../../part-02/topology/characteristic-classes-and-chern-weil-theory/part-01/continuouslinearmap-metricchangetransport.md)
- [Sylvester's law of inertia for regular forms](../../../../linear-algebra/part-01/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)
- [TauCeti.Complexification](../../../../analysis/part-02/one-parameter-semigroups-completely-monotone-and/tauceti-complexification.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/NormalSubbundle.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/NormalSubbundle.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace)
- [Source of `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_bundleDiffeomorph_prod_negativeNormalSpace_positiveNormalSpace` in TauCeti/Geometry/Manifold/Morse/Bott/NormalSubbundle.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Bott/NormalSubbundle.lean#L673)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
