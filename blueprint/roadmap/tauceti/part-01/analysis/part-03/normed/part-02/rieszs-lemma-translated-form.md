---
declaration: theorem
origin: cited
lean: TauCeti.riesz_lemma_translate, TauCeti.riesz_lemma_of_norm_lt_of_lt
statement: formalized
proof: formalized
---

# Riesz's lemma, translated form

for a closed submodule `F`, a vector `x` and `r < 1`, some
`y ∈ F` satisfies `r * ‖x - y‖ ≤ ‖x - y - z‖` for every `z ∈ F`, so `x - y` is almost as far from
`F` as its norm. For `x ∈ F` one may take `y = x`.

```lean
TauCeti.riesz_lemma_translate.{u_2, u_3} {E : Type u_2} [NormedAddCommGroup E] {R : Type u_3}
  [Semiring R] [_root_.Module R E] {F : Submodule R E} (hFc : IsClosed ↑F) (x : E) {r : ℝ}
  (hr : r < 1) : ∃ y ∈ F, ∀ z ∈ F, r * ‖x - y‖ ≤ ‖x - y - z‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.riesz_lemma_translate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RieszLemma.html#TauCeti.riesz_lemma_translate).

## Other forms

**Riesz's lemma relative to a larger subspace.** Formalized in Tau Ceti as [`TauCeti.riesz_lemma_of_norm_lt_of_lt`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RieszLemma.html#TauCeti.riesz_lemma_of_norm_lt_of_lt).

```lean
TauCeti.riesz_lemma_of_norm_lt_of_lt.{u_1, u_2} {𝕜 : Type u_1} {E : Type u_2} [NormedField 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] {c : 𝕜} (hc : 1 < ‖c‖) {R : ℝ} (hR : ‖c‖ < R)
  {F G : Submodule 𝕜 E} (hFc : IsClosed ↑F) (hFG : F < G) :
  ∃ x₀ ∈ G, ‖x₀‖ ≤ R ∧ ∀ y ∈ F, 1 ≤ ‖x₀ - y‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.riesz_lemma_translate`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/RieszLemma.html#TauCeti.riesz_lemma_translate)
- [Source of `TauCeti.riesz_lemma_translate` in TauCeti/Analysis/Normed/Module/RieszLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/RieszLemma.lean#L42)
