---
declaration: theorem
origin: cited
lean: OeisA93456.conjecture
statement: formalized
---

# Product of composite numbers in triangular intervals

> Product of all composite numbers between $n(n-1)/2+1$ and $n(n+1)/2$ (including boundaries),
> where $n(n-1)/2 = \binom{n}{2}$ and $n(n+1)/2 = \binom{n+1}{2}$.
>
> *References:*
> - [A093456](https://oeis.org/A093456)

*Quoted from [FormalConjectures/OEIS/93456.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/93456.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA93456.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_93456_conjecture_0/Submission/Spec.lean#L109](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-ant-j0j0g4uzligm1k41/oeis_93456_conjecture_0/Submission/Spec.lean#L109).

> Conjecture: There are finitely many numbers such that $a(n)$ is not $\equiv 0 \pmod{a(n-1)}$.
> (Also mentioned in A093455.) In fact there are infinitely many such numbers.

```lean
theorem conjecture :
    ¬ Set.Finite {n : ℕ | 1 < n ∧ ¬ (a (n - 1) ∣ a n)}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/93456.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/93456.lean#L65).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/93456.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/93456.lean)
- [A093456](https://oeis.org/A093456)
