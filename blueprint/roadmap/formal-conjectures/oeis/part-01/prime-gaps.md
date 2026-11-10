---
declaration: theorem
origin: cited
lean: OeisA1223.conjecture
statement: formalized
---

# Prime gaps

> Differences between consecutive primes: $a(n) = p_{n+1} - p_n$.
>
> *References:*
> - [A001223](https://oeis.org/A001223)

*Quoted from [FormalConjectures/OEIS/1223.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1223.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 4 test statements, counted here but not shown.

## `OeisA1223.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-oai-jajpvieznaevpoyg/prime_gap_subsequences_occur_infinitely_often/Submission/Spec.lean#L134](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-full-50usd-oai-jajpvieznaevpoyg/prime_gap_subsequences_occur_infinitely_often/Submission/Spec.lean#L134).

> Any subsequence a(n .. n+m) with n > 2 (as to exclude the
> untypical primes 2 and 3) should occur infinitely many times at other starting points k.
>
> This is false. The five-term block starting at $n = 3$ is $(2,4,2,4,2)$, and a congruence
> modulo $5$ shows that it occurs only at $n = 3$.

```lean
theorem conjecture :
    ¬ ∀ (n m : ℕ), n ≥ 3 →
      Set.Infinite {k : ℕ | gapSubsequence k (m + 1) = gapSubsequence n (m + 1)}
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1223.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1223.lean#L74).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1223.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/OEIS/1223.lean)
- [A001223](https://oeis.org/A001223)
