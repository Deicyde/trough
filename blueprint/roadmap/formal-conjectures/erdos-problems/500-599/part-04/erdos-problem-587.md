---
declaration: theorem
origin: cited
lean: Erdos587.erdos_587.variants.nguyen_vu
statement: formalized
---

# Erdős Problem 587

> *Reference:* [erdosproblems.com/587](https://www.erdosproblems.com/587)

*Quoted from [FormalConjectures/ErdosProblems/587.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/587.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/587](https://www.erdosproblems.com/587).

The file states 1 research or textbook statement: 1 solved.

## `Erdos587.erdos_587.variants.nguyen_vu`

Solved: stated here without proof.

> Nguyen and Vu proved that $|A| \ll N^{1/3} (\log N)^{O(1)}$.

```lean
theorem erdos_587.variants.nguyen_vu : ∃ᵉ (O > 0) (O' > 0),
    ∀ᶠ N in Filter.atTop, (MaxNotSqSum N : ℝ) ≤ O' * Real.nthRoot 3 N * (N : ℝ).log^O
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/587.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/587.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/587.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/587.lean)
- [erdosproblems.com/587](https://www.erdosproblems.com/587)
