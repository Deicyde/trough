---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle, TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart
statement: formalized
proof: formalized
---

# The Morse–Bott lemma on the normal bundle

Let `i : S → M` be a nondegenerate critical
submanifold of `f`, for a smooth embedding of a nonempty manifold into a Hausdorff,
second-countable, finite-dimensional, boundaryless manifold, and let `f` be `C^{k+2}`,
`1 ≤ k ≤ ∞`, on an open neighbourhood `O` of the image of `i`. Then there is a `C^k` partial
diffeomorphism `Θ` from the total space of the intrinsic normal bundle of `i` to `M`, whose source
contains the whole zero section, which sends the zero section to `i` and has image in `O`, such
that `f (Θ x) = f (i s) + ½ Hessₛ (x, x)` for every `x` in its source over `s`, where `Hessₛ` is
the normal Hessian.

```lean
TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [TopologicalSpace M]
  [ChartedSpace H M] {E' : Type u_4} {H' : Type u_5} {S : Type u_6} {P : Type u_7}
  [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H'] {J : ModelWithCorners ℝ E' H'}
  [TopologicalSpace S] [ChartedSpace H' S] {f : M → ℝ} {i : TauCeti.SmoothEmbedding J I (↑⊤) S M}
  [I.Boundaryless] [IsManifold I (↑⊤) M] [T2Space M] (hn : ↑⊤ ≠ 0)
  (h : i.IsNondegenerateCriticalSubmanifold f) [SecondCountableTopology M] [Nonempty S]
  [FiniteDimensional ℝ E'] [J.Boundaryless] [IsManifold J (↑⊤) S] [NormedAddCommGroup P]
  [NormedSpace ℝ P] [FiniteDimensional ℝ P] {k : ℕ∞} (hk : k ≠ 0)
  (hdim : Module.finrank ℝ P = Module.finrank ℝ E - Module.finrank ℝ E') {O : Set M} (hO : IsOpen O)
  (hiO : Set.range ⇑i ⊆ O) (hf : ContMDiffOn I (modelWithCornersSelf ℝ ℝ) (↑k + 2) f O) :
  ∃ Θ,
    (∀ (s : S), Bundle.zeroSection P (fun s => i.NormalSpace s hn) s ∈ Θ.source) ∧
      (∀ (s : S), ↑Θ.toPartialEquiv (Bundle.zeroSection P (fun s => i.NormalSpace s hn) s) = i s) ∧
        Θ.target ⊆ O ∧
          ∀ x ∈ Θ.source,
            f (↑Θ.toPartialEquiv x) =
              f (i x.proj) +
                2⁻¹ *
                  ((TauCeti.SmoothEmbedding.IsCriticalSubmanifold.normalHessian hn ⋯ x.proj) x.snd)
                    x.snd
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The inverse function theorem for manifolds](../../../part-02/manifold/part-02/the-inverse-function-theorem-for-manifolds.md)
- [The Koszul formula](../../../part-02/manifold/part-03/the-koszul-formula.md)
- [The Morse–Bott lemma in product coordinates](../../../../analysis/part-03/calculus/part-01/the-morse-bott-lemma-in-product-coordinates.md)
- [The parametric Morse lemma on a vector bundle](../part-02/the-parametric-morse-lemma-on-a-vector-bundle.md)
- [TauCeti.Manifold.riemannianExp](../../geodesics-the-exponential-map-and-the-hopf-rinow/tauceti-manifold-riemannianexp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Tubular.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle).

## Other forms

**The Morse–Bott lemma.** Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart).

```lean
TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart.{u_1, u_2, u_3,
    u_4, u_5, u_6, u_7}
  {E : Type u_1} {H : Type u_2} {M : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E]
  [FiniteDimensional ℝ E] [TopologicalSpace H] {I : ModelWithCorners ℝ E H} [I.Boundaryless]
  [TopologicalSpace M] [ChartedSpace H M] [IsManifold I 2 M] {E' : Type u_4} {H' : Type u_5}
  {S : Type u_6} [NormedAddCommGroup E'] [NormedSpace ℝ E'] [TopologicalSpace H']
  {J : ModelWithCorners ℝ E' H'} [J.Boundaryless] [TopologicalSpace S] [ChartedSpace H' S]
  {F : Type u_7} [NormedAddCommGroup F] [NormedSpace ℝ F] {f : M → ℝ} {n : WithTop ℕ∞} {k : ℕ∞}
  {i : TauCeti.SmoothEmbedding J I n S M} {s : S} (hi : i.IsNondegenerateCriticalSubmanifold f)
  (h : Manifold.IsImmersionAtOfComplement F J I n (⇑i) s) (hkn : ↑k + 2 ≤ n) (hk : k ≠ 0)
  (hf : ∀ᶠ (y : M) in nhds (i s), ContMDiffAt I (modelWithCornersSelf ℝ ℝ) (↑k + 2) f y) :
  ∃ ψ U V,
    IsOpen U ∧
      IsOpen V ∧
        ↑(h.domChart.extend J) s ∈ U ∧
          0 ∈ V ∧
            ψ.source = U ×ˢ V ∧
              U ⊆ (h.domChart.extend J).target ∧
                U ×ˢ V ⊆ ⇑h.equiv ⁻¹' (h.codChart.extend I).target ∧
                  (∀ b ∈ U,
                      ↑(h.codChart.extend I).symm (h.equiv (b, 0)) =
                        i (↑(h.domChart.extend J).symm b)) ∧
                    (∀ (z : E' × F), (↑ψ z).1 = z.1) ∧
                      (∀ (b : E'), ↑ψ (b, 0) = (b, 0)) ∧
                        (∀ z ∈ ψ.target, (↑ψ.symm z).1 = z.1) ∧
                          ContDiffOn ℝ (↑k) (↑ψ) ψ.source ∧
                            ContDiffOn ℝ (↑k) (↑ψ.symm) ψ.target ∧
                              (∀ b ∈ U, f (i (↑(h.domChart.extend J).symm b)) = f (i s)) ∧
                                (∀ b ∈ U,
                                    (fderiv ℝ
                                        (fderiv ℝ fun v =>
                                          (f ∘ ↑(h.codChart.extend I).symm ∘ ⇑h.equiv) (b, v))
                                        0).IsInvertible) ∧
                                  ∀ z ∈ ψ.source,
                                    (f ∘ ↑(h.codChart.extend I).symm ∘ ⇑h.equiv) z =
                                      f (i s) +
                                        2⁻¹ *
                                          ((fderiv ℝ
                                                (fderiv ℝ fun v =>
                                                  (f ∘ ↑(h.codChart.extend I).symm ∘ ⇑h.equiv)
                                                    (z.1, v))
                                                0)
                                              (↑ψ z).2)
                                            (↑ψ z).2
```

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Tubular.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle)
- [Source of `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_partialDiffeomorph_normalBundle` in TauCeti/Geometry/Manifold/Morse/Bott/Tubular.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Geometry/Manifold/Morse/Bott/Tubular.lean#L77)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/MorseTheory/STATUS.md)
