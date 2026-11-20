---
declaration: theorem
origin: cited
lean: Erdos681.erdos_681
statement: formalized
---

# Erdős Problem 681

> *Reference:* [erdosproblems.com/681](https://www.erdosproblems.com/681)

*Quoted from [FormalConjectures/ErdosProblems/681.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/681.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/681](https://www.erdosproblems.com/681).

The file states 1 research or textbook statement: 1 open.

## `Erdos681.erdos_681`

Open: stated without proof.

> **Erdős problem 681.**
> Is it true that for all large $n$ there exists $k$
> such that $n + k$ is composite and $p(n+k) > k^2$,
> where $p(m)$ is the least prime factor of $m$ ?

```lean
theorem erdos_681 :
    ∀ᶠ n in .atTop, ∃ k > 0, (n + k).Composite ∧ ∀ p, IsLPF p (n + k) → p > k ^ 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/681.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/681.lean#L40).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/681.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/681.lean)
- [erdosproblems.com/681](https://www.erdosproblems.com/681)
