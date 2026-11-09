---
declaration: theorem
origin: cited
lean: Erdos208.erdos_208.parts.i, Erdos208.erdos_208.parts.ii, Erdos208.erdos_208.variants.log_bound
statement: formalized
---

# Erdős Problem 208

> *Reference:* [erdosproblems.com/208](https://www.erdosproblems.com/208)

*Quoted from [FormalConjectures/ErdosProblems/208.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/208.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/208](https://www.erdosproblems.com/208).

The file states 3 research or textbook statements: 3 open.

## `Erdos208.erdos_208.parts.i`

Open: stated without proof.

> Let $s_1 < s_2 < \dots$ be the sequence of squarefree numbers. Is it true that
> for any $\epsilon > 0$ and large $n$, $s_{n+1} - s_n \ll_\epsilon s_n^\epsilon$?

```lean
theorem erdos_208.parts.i :
    ∀ ε > (0 : ℝ), (fun n => (s (n + 1) - s n : ℝ)) =O[atTop] (fun n => (s n : ℝ)^ε)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/208.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/208.lean#L41).

## `Erdos208.erdos_208.parts.ii`

Open: stated without proof.

> Let $s_1 < s_2 < \dots$ be the sequence of squarefree numbers. Is it true that
> $s_{n + 1} - s_n \le (1 + o(1)) \cdot (\pi^2 / 6) \cdot \log (s_n) / \log (\log (s_n))$?

```lean
theorem erdos_208.parts.ii : ∃ (c : ℕ → ℝ), (c =o[atTop] (1 : ℕ → ℝ)) ∧ ∀ᶠ n in atTop,
      s (n + 1) - s n ≤ (1 + (c n)) * (π^2 / 6) * log (s n) / log (log (s n))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/208.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/208.lean#L49).

## `Erdos208.erdos_208.variants.log_bound`

Open: stated without proof.

> In [Er79] Erdős says perhaps $s_{n+1} - s_n \ll \log s_n$, but he is 'very doubtful'.
>
> [Er79] Erdős, Paul, __Some unconventional problems in number theory__. Math. Mag. (1979), 67-70.

```lean
theorem erdos_208.variants.log_bound :
    (fun n ↦ (s (n + 1) - s n : ℝ)) =O[atTop] fun n ↦ log (s n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/208.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/208.lean#L59).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/208.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/208.lean)
- [erdosproblems.com/208](https://www.erdosproblems.com/208)
