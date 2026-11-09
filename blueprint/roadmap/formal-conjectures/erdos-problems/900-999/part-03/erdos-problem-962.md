---
declaration: theorem
origin: cited
lean: Erdos962.erdos_962, Erdos962.erdos_962.variants.tang_lower_bound, Erdos962.erdos_962.variants.tao_upper_bound
statement: formalized
---

# Erdős Problem 962

> *References:*
> - [erdosproblems.com/962](https://www.erdosproblems.com/962)
> - [Er65] Erdős, P., Extremal problems in number theory. Proc. Sympos. Pure Math., Vol. VIII (1965), 181-189.
> - [Er76e] Erdős, P., Problems and results on consecutive integers. Publ. Math. Debrecen (1976), 271-282.
> - [Tang](https://github.com/QuanyuTang/erdos-problem-962/blob/main/On_Erd%C5%91s_Problem_962.pdf)
> - [Tao](https://www.erdosproblems.com/forum/thread/962)

*Quoted from [FormalConjectures/ErdosProblems/962.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/962.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/962](https://www.erdosproblems.com/962).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos962.erdos_962`

Open: stated without proof.

> Main conjecture:
>
> $\log k(n) \le (\log n)^{(1/2 + o(1))}$

```lean
theorem erdos_962 :
    ∃ ε : ℕ → ℝ,
      (∀ δ > 0, ∀ᶠ n in atTop, |ε n| < δ) ∧
      ∀ᶠ n : ℕ in atTop,
        log (k n : ℝ)
          ≤ rpow (log n) ((1 : ℝ) / 2 + ε n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/962.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/962.lean#L59).

## `Erdos962.erdos_962.variants.tang_lower_bound`

Solved: stated here without proof.

> Tang's lower bound [Tang]:
>
> $\log k(n) \ge (1/\sqrt{2} - o(1)) * \sqrt{\log n * \log \log n}$

```lean
theorem erdos_962.variants.tang_lower_bound :
    ∃ ε : ℕ → ℝ,
      (∀ δ > 0, ∀ᶠ n in atTop, |ε n| < δ) ∧
      ∀ᶠ n : ℕ in atTop,
          (1 / sqrt 2 - ε n) *
              sqrt (log n * log (log n))
            ≤ log (k n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/962.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/962.lean#L73).

## `Erdos962.erdos_962.variants.tao_upper_bound`

Solved: stated here without proof.

> Tao's upper bound [Tao]:
>
> $k(n) \le (1 + o(1)) * n^{1/2}$

```lean
theorem erdos_962.variants.tao_upper_bound :
    ∃ ε : ℕ → ℝ,
      (∀ δ > 0, ∀ᶠ n in atTop, |ε n| < δ) ∧
      ∀ᶠ n : ℕ in atTop,
          (k n : ℝ) ≤ (1 + ε n) * sqrt n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/962.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/962.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/962.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/962.lean)
- [erdosproblems.com/962](https://www.erdosproblems.com/962)
