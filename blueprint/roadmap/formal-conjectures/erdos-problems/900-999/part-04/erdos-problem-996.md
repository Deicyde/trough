---
declaration: theorem
origin: cited
lean: Erdos996.erdos_996, Erdos996.erdos_996.variants.log2
statement: formalized
---

# Erdős Problem 996

> *Reference:*
>  - [erdosproblems.com/996](https://www.erdosproblems.com/996)
>  - [Er49d] Erdös, P. "On the strong law of large numbers." Transactions of the American Mathematical
>     Society 67.1 (1949): 51-56.
>  - [Ma66] Matsuyama, Noboru. "On the strong law of large numbers." Tohoku Mathematical Journal,
>     Second Series 18.3 (1966): 259-269.

*Quoted from [FormalConjectures/ErdosProblems/996.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/996.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/996](https://www.erdosproblems.com/996).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos996.erdos_996`

Open: stated without proof.

> Does there exists a positive constant `C` such that for all `f ∈ L²[0,1]` and all lacunary
> sequences `n`, if `‖f - fₖ‖₂ = O(1 / log log log k ^ C)`, then for almost every `x`,
> `lim ∑ k ∈ Finset.range N, f (n k • x)) / N = ∫ t, f t ∂t`?

```lean
theorem erdos_996 :
    ∃ (C : ℝ), 0 < C ∧ ∀ (f : Lp ℂ 2 (haarAddCircle (T := 1))) (n : ℕ → ℕ),
    IsLacunary n →
    (fun k => (eLpNorm (⇑f - fourierPartial f k) 2 (haarAddCircle (T := 1))).toReal) =O[atTop]
    (fun k => 1 / (log (log (log k))) ^ C)
    →
    ∀ᵐ x, Tendsto (fun N => (∑ k ∈ .range N, f (n k • x)) / N) atTop
    (𝓝 (∫ t, f t ∂haarAddCircle))
```

Category `research open`; AMS [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/996.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/996.lean#L45).

## `Erdos996.erdos_996.variants.log2`

Solved: stated here without proof.

> The following theorem is proved in [Ma66].

```lean
theorem erdos_996.variants.log2 : ∀ (C : ℝ), 0.5 < C →
    ∀ (f : Lp ℂ 2 (haarAddCircle (T := 1))) (n : ℕ → ℕ),
    IsLacunary n →
    (fun k => (eLpNorm (⇑f - fourierPartial f k) 2 (haarAddCircle (T := 1))).toReal) =O[atTop]
    (fun k => 1 / (log (log k)) ^ C)
    →
    ∀ᵐ x, Tendsto (fun N => (∑ k ∈ .range N, f (n k • x)) / N) atTop
    (𝓝 (∫ t, f t ∂haarAddCircle))
```

Category `research solved`; AMS [42 Harmonic analysis on Euclidean spaces](../../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/ErdosProblems/996.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/996.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/996.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/996.lean)
- [erdosproblems.com/996](https://www.erdosproblems.com/996)
