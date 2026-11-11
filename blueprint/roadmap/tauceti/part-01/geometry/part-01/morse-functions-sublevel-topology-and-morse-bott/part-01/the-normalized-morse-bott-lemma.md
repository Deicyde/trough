---
declaration: theorem
origin: cited
lean: TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart
statement: formalized
proof: formalized
---

# The normalized Morse–Bott lemma

Let `i : S → M` be a Morse–Bott critical submanifold of
`f`, with slice charts `h.domChart` of `S` and `h.codChart` of `M` at `s` and
`h.equiv : E' × F ≃ E` in which `i` reads `b ↦ (b, 0)`, and let `f` be `C^{k+2}` near `i s` with
`1 ≤ k` and `k + 2 ≤ n`. Write `g = f ∘ (h.codChart.extend I).symm ∘ h.equiv`. There is a `C^k`
chart `ψ` from a product neighbourhood `U ×ˢ V` of `(h.domChart.extend J s, 0)`, inside the chart
domains, onto an open subset of `E' × ℝᵐ`, where `m = dim F` is the codimension of `S`, preserving
the base coordinate and fixing the zero section, whose zero section over `U` is the submanifold,
and in which

`g z = f (i s) - Σ_{j < λ} (ψ z).2ⱼ² + Σ_{j ≥ λ} (ψ z).2ⱼ²`

on the whole source, where `λ` is the Morse index of `f` at `i s`.

```lean
TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart.{u_1,
    u_2, u_3, u_4, u_5, u_6, u_7}
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
                              ∀ z ∈ ψ.source,
                                (f ∘ ↑(h.codChart.extend I).symm ∘ ⇑h.equiv) z =
                                  f (i s) +
                                    ∑ j,
                                      (if ↑j < TauCeti.manifoldMorseIndex I f (i s) then -1
                                        else 1) *
                                        (↑ψ z).2.ofLp j ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Morse–Bott lemma](../part-02/the-morse-bott-lemma.md)
- [Sylvester's law of inertia for regular forms](../../../../linear-algebra/quadratic-form/sylvesters-law-of-inertia-for-regular-forms.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart).

## Sources

- [Tau Ceti documentation: `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.html#TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart)
- [Source of `TauCeti.SmoothEmbedding.IsNondegenerateCriticalSubmanifold.exists_normalized_morseBott_chart` in TauCeti/Geometry/Manifold/Morse/Bott/Lemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Bott/Lemma.lean#L256)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
