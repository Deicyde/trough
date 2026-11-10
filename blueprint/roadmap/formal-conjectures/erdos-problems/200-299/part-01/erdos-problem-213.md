---
declaration: theorem
origin: cited
lean: Erdos213.erdos_213, Erdos213.erdos_213.variants.KK08
statement: formalized
---

# Erdős Problem 213

> *Reference:* [erdosproblems.com/213](https://www.erdosproblems.com/213)

*Quoted from [FormalConjectures/ErdosProblems/213.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/213.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/213](https://www.erdosproblems.com/213).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos213.erdos_213`

Open: stated without proof.

> Let $n \geq 4$. Are there $n$ points in $\mathbb{R}^2$, no three on a line and no four on a circle,
> such that all pairwise distances are integers?

```lean
theorem erdos_213 : ∀ n : ℕ, n ≥ 4 → Erdos213For n
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/213.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/213.lean#L47).

## `Erdos213.erdos_213.variants.KK08`

Solved: stated here without proof.

> The best construction to date, due to Kreisel and Kurz, has $n = 7$.

```lean
theorem erdos_213.variants.KK08 : Erdos213For 7
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/213.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/213.lean#L53).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/213.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/213.lean)
- [erdosproblems.com/213](https://www.erdosproblems.com/213)
