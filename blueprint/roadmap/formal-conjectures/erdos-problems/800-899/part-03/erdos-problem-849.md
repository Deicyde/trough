---
declaration: theorem
origin: cited
lean: Erdos849.erdos_849
statement: formalized
---

# Erdős Problem 849

> *Reference:* [erdosproblems.com/849](https://www.erdosproblems.com/849)

*Quoted from [FormalConjectures/ErdosProblems/849.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/849.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/849](https://www.erdosproblems.com/849).

The file states 1 research or textbook statement: 1 open.

## `Erdos849.erdos_849`

Open: stated without proof.

> Is it true that, for every integer $t\geq1$, there is some integer $a$ such that ${n \choose k} = a$
> with $1\leq k \le \frac{n}{2}$ has exactly $t$ solutions?

```lean
theorem erdos_849 :
    ∀ t ≥ 1, ∃ a : ℕ,
      {n : ℕ | ∃ k ≥ 1, 2 * k ≤ n ∧ choose n k = a}.ncard = t
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/849.lean, line 37](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/849.lean#L37).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/849.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/849.lean)
- [erdosproblems.com/849](https://www.erdosproblems.com/849)
