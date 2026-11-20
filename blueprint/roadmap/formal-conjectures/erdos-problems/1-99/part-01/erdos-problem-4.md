---
declaration: theorem
origin: cited
lean: Erdos4.erdos_4, Erdos4.erdos_4.variants.rankin
statement: formalized
---

# Erdős Problem 4

> *Reference:* [erdosproblems.com/4](https://www.erdosproblems.com/4)

*Quoted from [FormalConjectures/ErdosProblems/4.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/4.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/4](https://www.erdosproblems.com/4).

The file states 2 research or textbook statements: 2 solved.

## `Erdos4.erdos_4`

Solved: stated here without proof.

> Is it true that, for any $C > 0$, there infinitely many $n$ such that:
>
> $$
>   p_{n + 1} - p_n > C \frac{\log\log n\log\log\log\log n}{(\log\log\log n) ^ 2}\log n
> $$

```lean
theorem erdos_4 : (∀ C > 0, Erdos4For C)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/4.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/4.lean#L43).

## `Erdos4.erdos_4.variants.rankin`

Solved: stated here without proof.

> Rankin's theorem: there exists a positive constant $C$ such that `Erdos4For C` holds.

```lean
theorem erdos_4.variants.rankin :
    ∃ C > 0, Erdos4For C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/4.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/4.lean#L48).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/4.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/4.lean)
- [erdosproblems.com/4](https://www.erdosproblems.com/4)
