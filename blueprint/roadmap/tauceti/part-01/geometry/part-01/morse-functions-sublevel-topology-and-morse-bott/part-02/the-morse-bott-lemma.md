---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart
statement: formalized
proof: formalized
---

# The Morse–Bott lemma

Let `i : S → M` be a Morse–Bott critical submanifold of `f`, with
slice charts `h.domChart` of `S` and `h.codChart` of `M` at `s` and `h.equiv : E' × F ≃ E` in which
`i` reads `b ↦ (b, 0)`, and let `f` be `C^{k+2}` near `i s` with `1 ≤ k` and `k + 2 ≤ n`. Write
`g = f ∘ (h.codChart.extend I).symm ∘ h.equiv`. There is a `C^k` chart `ψ` of `E' × F` with
product source `U ×ˢ V` around `(h.domChart.extend J s, 0)`, inside the chart domains, preserving
the base coordinate and fixing the zero section, such that

* the zero section over `U` is the submanifold: `g` there reads `f ∘ i` in the chart of `S`,
* `f` is constant, equal to `f (i s)`, along the submanifold over `U`,
* the vertical Hessian of `g` at each point of the zero section over `U` is invertible, and
* `g z = f (i s) + ½ D²(g (z.1, ·))(0) ((ψ z).2, (ψ z).2)` on the source of `ψ`.

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

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse–Bott lemma in product coordinates](../../../../analysis/part-02/calculus/part-01/the-morse-bott-lemma-in-product-coordinates.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart)
- [Source of `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_morseBott_chart` in TauCeti/Geometry/Manifold/Morse/Bott/Lemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.lean#L150)
