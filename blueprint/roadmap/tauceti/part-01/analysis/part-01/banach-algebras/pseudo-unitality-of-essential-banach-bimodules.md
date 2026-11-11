---
declaration: theorem
origin: cited
lean: ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span
statement: formalized
proof: formalized
---

# Pseudo-unitality of essential Banach bimodules

Let `A` be a Banach algebra with a
two-sided approximate identity `l` bounded by `C`, and let `E` be a Banach `A`-bimodule with
bounded actions `L` and `R`. Every element of the essential part `closure (span (A · E · A))` is a
single triple product: `x = L a (R z b)` with `‖a‖ ≤ C` and `‖b‖ ≤ C`.

```lean
ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span.{u_1, u_2, u_3}
  {𝕜 : Type u_1} {A : Type u_2} {E : Type u_3} [RCLike 𝕜] [NonUnitalNormedRing A] [NormedSpace 𝕜 A]
  [IsScalarTower 𝕜 A A] [SMulCommClass 𝕜 A A] [CompleteSpace A] [NormedAddCommGroup E]
  [NormedSpace 𝕜 E] [CompleteSpace E] (L : A →L[𝕜] E →L[𝕜] E) (R : E →L[𝕜] A →L[𝕜] E)
  (hL : ∀ (a b : A) (z : E), (L (a * b)) z = (L a) ((L b) z))
  (hR : ∀ (x : E) (a b : A), (R ((R x) a)) b = (R x) (a * b))
  (hLR : ∀ (a : A) (z : E) (b : A), (R ((L a) z)) b = (L a) ((R z) b)) {l : Filter A}
  (hl : l.IsApproximateUnit) {C : ℝ} (hC : ∀ᶠ (e : A) in l, ‖e‖ ≤ C) {x : E}
  (hx : x ∈ (Submodule.span 𝕜 (Set.range fun p => (R ((L p.1) p.2.1)) p.2.2)).topologicalClosure) :
  ∃ a z b, ‖a‖ ≤ C ∧ ‖b‖ ≤ C ∧ (L a) ((R z) b) = x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Bimodule.html#ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span).

## Sources

- [Tau Ceti documentation: `ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Module/CohenFactorization/Bimodule.html#ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span)
- [Source of `ContinuousLinearMap.exists_apply_apply_eq_of_mem_topologicalClosure_span` in TauCeti/Analysis/Normed/Module/CohenFactorization/Bimodule.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Module/CohenFactorization/Bimodule.lean#L147)
- [Tau Ceti roadmap status: Banach algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachAlgebras/STATUS.md)
