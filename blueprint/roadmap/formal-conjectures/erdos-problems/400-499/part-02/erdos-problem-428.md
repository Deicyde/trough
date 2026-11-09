---
declaration: theorem
origin: cited
lean: Erdos428.erdos_428
statement: formalized
---

# Erdős Problem 428

> *Reference:* [erdosproblems.com/428](https://www.erdosproblems.com/428)

*Quoted from [FormalConjectures/ErdosProblems/428.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/428.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/428](https://www.erdosproblems.com/428).

The file states 1 research or textbook statement: 1 open.

## `Erdos428.erdos_428`

Open: stated without proof.

> Is there a set $A\subseteq \mathbb{N}$ such that, for infinitely many $n$, all of $n-a$
> are prime for all $a\in A$ with $0 < a < n$ and $$\liminf\frac{\lvert A\cap [1,x]\rvert}{\pi(x)}>0?$$

```lean
theorem erdos_428 :
    ∃ A : Set ℕ,
      (∃ᶠ n in atTop, ∀ a ∈ A, 0 < a → a < n → (n - a).Prime) ∧
      liminf (fun n ↦ primeDensityRatio A n) atTop > 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/428.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/428.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/428.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/428.lean)
- [erdosproblems.com/428](https://www.erdosproblems.com/428)
