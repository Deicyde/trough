---
declaration: theorem
origin: cited
lean: Erdos200.erdos_200, Erdos200.erdos_200.variants.upper
statement: formalized
---

# Erdős Problem 200

> *Reference:* [erdosproblems.com/200](https://www.erdosproblems.com/200)

*Quoted from [FormalConjectures/ErdosProblems/200.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/200.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/200](https://www.erdosproblems.com/200).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos200.erdos_200`

Open: stated without proof.

> Does the longest arithmetic progression of primes in $\{1,\ldots,N\}$ have length $o(\log N)$?

```lean
theorem erdos_200 :
    (fun n => (longestPrimeArithmeticProgressions n : ℝ)) =o[atTop] (fun n => log n)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/200.lean, line 42](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/200.lean#L42).

## `Erdos200.erdos_200.variants.upper`

Solved: stated here without proof.

> It follows from the prime number theorem that such a progression has length $\leq(1+o(1))\log N$.

```lean
theorem erdos_200.variants.upper : ∃ (o : ℕ → ℝ) (_ : o =o[atTop] (1 : ℕ → ℝ)),
    ∀ n, longestPrimeArithmeticProgressions n ≤ (1 + o n) * log n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/200.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/200.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/200.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/200.lean)
- [erdosproblems.com/200](https://www.erdosproblems.com/200)
