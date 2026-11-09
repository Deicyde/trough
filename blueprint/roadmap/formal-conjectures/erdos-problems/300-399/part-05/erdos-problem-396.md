---
declaration: theorem
origin: cited
lean: Erdos396.erdos_396
statement: formalized
---

# Erdős Problem 396

> *Reference:* [erdosproblems.com/396](https://www.erdosproblems.com/396)

*Quoted from [FormalConjectures/ErdosProblems/396.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/396.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/396](https://www.erdosproblems.com/396).

The file states 1 research or textbook statement: 1 open.

## `Erdos396.erdos_396`

Open: stated without proof.

> Is it true that for every $k$ there exists $n$ such that
>
> $$\prod_{0\leq i\leq k}(n-i) \mid \binom{2n}{n}?$$

```lean
theorem erdos_396 : ∀ k : ℕ, ∃ n : ℕ, descFactorial n (k + 1) ∣ centralBinom n
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/396.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/396.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/396.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/396.lean)
- [erdosproblems.com/396](https://www.erdosproblems.com/396)
