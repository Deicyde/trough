---
declaration: theorem
origin: cited
lean: Erdos680.erdos_680.parts.i, Erdos680.erdos_680.parts.ii
statement: formalized
---

# Erdős Problem 680

> *Reference:* [erdosproblems.com/680](https://www.erdosproblems.com/680)

*Quoted from [FormalConjectures/ErdosProblems/680.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/680.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/680](https://www.erdosproblems.com/680).

The file states 2 research or textbook statements: 2 open.

## `Erdos680.erdos_680.parts.i`

Open: stated without proof.

> Is it true that, for all sufficiently large $n$, there exists some $k$ such that
>
> $$
> p(n+k)>k^2+1,
> $$
>
> where $p(m)$ denotes the least prime factor of $m$?

```lean
theorem erdos_680.parts.i :
    ∀ᶠ (n : ℕ) in .atTop, ∃ k ≠ 0, (n + k).minFac > k^2 + 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/680.lean, line 41](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/680.lean#L41).

## `Erdos680.erdos_680.parts.ii`

Open: stated without proof.

> Can one prove this is false if we replace $k^2+1$ by $e^{(1+\epsilon)\sqrt{k}}+C_\epsilon$, for all
> $\epsilon>0$, where $C_\epsilon>0$ is some constant?

```lean
theorem erdos_680.parts.ii : ∀ ε > 0, ∃ C > 0,
    ¬ ∀ᶠ (n : ℕ) in Filter.atTop, ∃ k ≠ 0,
    Nat.minFac (n + k) > exp ((1 + ε) * √k) + C
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/680.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/680.lean#L50).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/680.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/680.lean)
- [erdosproblems.com/680](https://www.erdosproblems.com/680)
