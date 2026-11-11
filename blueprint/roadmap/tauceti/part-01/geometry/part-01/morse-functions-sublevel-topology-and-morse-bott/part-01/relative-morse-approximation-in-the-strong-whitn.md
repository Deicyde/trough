---
declaration: theorem
origin: cited
lean: ContMDiffMap.exists_isMorse_mem_ball_sub_compl
statement: formalized
proof: formalized
---

# Relative Morse approximation in the strong Whitney topology

Every strong `C^k`
neighbourhood `c.ball f` of a smooth function `f` contains a Morse function `g` which is within a
prescribed continuous positive tolerance `ε` of `f` everywhere. If `f` is Morse on an open
neighbourhood `V` of a closed set `C`, then `g` can be chosen to agree with `f` on a
neighbourhood of `C`.

```lean
ContMDiffMap.exists_isMorse_mem_ball_sub_compl.{u, u_1, u_2} {E : Type u_1} {H : Type u_2}
  {M : Type u} [NormedAddCommGroup E] [NormedSpace ℝ E] [TopologicalSpace H]
  {I : ModelWithCorners ℝ E H} [I.Boundaryless] [TopologicalSpace M] [ChartedSpace H M]
  [FiniteDimensional ℝ E] [IsManifold I (↑⊤) M] [T2Space M] [SigmaCompactSpace M]
  (f : ContMDiffMap I (modelWithCornersSelf ℝ ℝ) M ℝ ↑⊤) (c : ContMDiffMap.StrongCkControl I M ↑⊤)
  {ε : M → ℝ} (hε : Continuous ε) (hε₀ : ∀ (x : M), 0 < ε x) {C V : Set M} (hC : IsClosed C)
  (hV : IsOpen V) (hCV : C ⊆ V) (hfV : TauCeti.IsMorseOn I (⇑f) V) :
  ∃ g ∈ c.ball f,
    TauCeti.IsMorse I ⇑g ∧ (∀ (x : M), |g x - f x| < ε x) ∧ (tsupport fun x => g x - f x) ⊆ Cᶜ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Sard's lemma in equal dimensions](../../../../analysis/part-02/calculus/part-02/sards-lemma-in-equal-dimensions.md)

## Lean

Formalized in Tau Ceti as [`ContMDiffMap.exists_isMorse_mem_ball_sub_compl`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Generic/Strong.html#ContMDiffMap.exists_isMorse_mem_ball_sub_compl).

## Sources

- [Tau Ceti documentation: `ContMDiffMap.exists_isMorse_mem_ball_sub_compl`](https://taucetiproject.org/docs/TauCeti/Geometry/Manifold/Morse/Generic/Strong.html#ContMDiffMap.exists_isMorse_mem_ball_sub_compl)
- [Source of `ContMDiffMap.exists_isMorse_mem_ball_sub_compl` in TauCeti/Geometry/Manifold/Morse/Generic/Strong.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Geometry/Manifold/Morse/Generic/Strong.lean#L246)
- [Tau Ceti roadmap status: Morse functions, sublevel topology and Morse–Bott attachments](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MorseTheory/STATUS.md)
