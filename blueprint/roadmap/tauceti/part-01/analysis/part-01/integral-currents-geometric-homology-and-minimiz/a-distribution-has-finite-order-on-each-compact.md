---
declaration: theorem
origin: cited
lean: Distribution.exists_norm_apply_le
statement: formalized
proof: formalized
---

# A distribution has finite order on each compact set

For a compact `K ⊆ Ω` there are an
order `N` and a constant `C` such that `‖T φ‖ ≤ C * M` for every test function `φ` supported in
`K` whose derivatives of order at most `N` are all bounded by `M`.

```lean
Distribution.exists_norm_apply_le.{u_1, u_2} {E : Type u_1} {F : Type u_2} [NormedAddCommGroup E]
  [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {Ω : TopologicalSpace.Opens E}
  (T : Distribution Ω F ⊤) {K : TopologicalSpace.Compacts E} (hK : ↑K ⊆ ↑Ω) :
  ∃ N C,
    0 ≤ C ∧
      ∀ (φ : TestFunction Ω ℝ ⊤),
        tsupport ⇑φ ⊆ ↑K →
          ∀ (M : ℝ), 0 ≤ M → (∀ i ≤ N, ∀ (x : E), ‖iteratedFDeriv ℝ i (⇑φ) x‖ ≤ M) → ‖T φ‖ ≤ C * M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Distribution.exists_norm_apply_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Order.html#Distribution.exists_norm_apply_le).

## Sources

- [Tau Ceti documentation: `Distribution.exists_norm_apply_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/Order.html#Distribution.exists_norm_apply_le)
- [Source of `Distribution.exists_norm_apply_le` in TauCeti/Analysis/Distribution/Order.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Distribution/Order.lean#L39)
- [Tau Ceti roadmap status: Integral currents, geometric homology and minimizing hypersurfaces](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricCurrents/STATUS.md)
