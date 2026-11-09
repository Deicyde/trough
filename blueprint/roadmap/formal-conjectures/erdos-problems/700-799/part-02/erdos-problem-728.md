---
declaration: theorem
origin: cited
lean: Erdos728.erdos_728
statement: formalized
---

# Erdős Problem 728

> *Reference:* [erdosproblems.com/728](https://www.erdosproblems.com/728)

*Quoted from [FormalConjectures/ErdosProblems/728.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/728.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/728](https://www.erdosproblems.com/728).

The file states 1 research or textbook statement: 1 solved.

## `Erdos728.erdos_728`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos728p.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos728p.lean).

> Let $\varepsilon$ be sufficiently small and $C, C' > 0$. Are there integers $a, b, n$ such that
>
> $$a, b > \varepsilon n\quad a!\, b! \mid n!\, (a + b - n)!, $$
>
> and
>
> $$C \log n < a + b - n < C' \log n ?$$
>
> Note that the website currently displays a simpler (trivial) version of this problem because
> $a + b$ isn't assumed to be in the $n + O(\log n)$ regime.
>
> Barreto and ChatGPT-5.2 have proved that, for any $0 < C_1 < C_2$, there are infinitely many
> $a, b, n$ with $b = n/2$, $a = n/2 + O(\log n)$, and $C_1 \log n < a + b - n < C_2 \log n$ such
> that $a! b! \mid n! (a + b - n)!$
>
> This appears to answer the question in the spirit it was intended.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_728 :
    ∀ᶠ ε : ℝ in 𝓝[>] 0, ∀ C > (0 : ℝ), ∀ C' > C,
      ∃ a b n : ℕ,
        0 < n ∧
        ε * n < a ∧
        ε * n < b ∧
        a ! * b ! ∣ n ! * (a + b - n)! ∧
        a + b > n + C * log n ∧
        a + b < n + C' * log n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/728.lean, line 52](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/728.lean#L52).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/728.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/728.lean)
- [erdosproblems.com/728](https://www.erdosproblems.com/728)
