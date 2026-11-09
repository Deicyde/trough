---
declaration: theorem
origin: cited
lean: Erdos855.erdos_855
statement: formalized
---

# Erdős Problem 855

> *Reference:* [erdosproblems.com/855](https://www.erdosproblems.com/855)
>
> This is an "eventually" formulation of the Second Hardy–Littlewood conjecture.

*Quoted from [FormalConjectures/ErdosProblems/855.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/855.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/855](https://www.erdosproblems.com/855).

The file states 1 research or textbook statement: 1 open.

## `Erdos855.erdos_855`

Open: stated without proof.

> Erdős Problem 855 (Segal's conjecture): $\pi(x + y) \le \pi(x) + \pi(y)$
> for all sufficiently large $x, y$, i.e. for all $x, y \ge N$ for some $N$.

```lean
theorem erdos_855 :
    ∀ᶠ (xy : ℕ × ℕ) in atTop ×ˢ atTop, π (xy.1 + xy.2) ≤ π xy.1 + π xy.2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/855.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/855.lean#L41).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/855.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/855.lean)
- [erdosproblems.com/855](https://www.erdosproblems.com/855)
