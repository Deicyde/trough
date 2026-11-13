---
declaration: theorem
origin: cited
lean: Erdos825.erdos_825, Erdos825.erdos_825.variants.necessary_cond
statement: formalized
---

# Erdős Problem 825

> *Reference:* [erdosproblems.com/825](https://www.erdosproblems.com/825)

*Quoted from [FormalConjectures/ErdosProblems/825.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/825.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/825](https://www.erdosproblems.com/825).

The file states 2 research or textbook statements: 2 solved.

## `Erdos825.erdos_825`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos825.lean#L5893](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos825.lean#L5893).

> Is there an absolute constant $C > 0$ such that every integer $n$ with
> $\sigma(n) > Cn$ is the distinct sum of proper divisors of $n$?
>
> This has been solved in the affirmative by Larsen - in fact, for any $\epsilon>0$ there exists $L$
> such that if $n$ has only prime divisors $>L$ and $\sigma(n)>(2+\epsilon)n$ then $n$ is the distinct
> sum of proper divisors of $n$.

```lean
theorem erdos_825 :
    ∃ (C : ℝ) (_ : C > 0),
      ∀ (n) (_ : σ 1 n > C * n),
        ∃ s ⊆ n.properDivisors, n = s.sum id
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/825.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/825.lean#L43).

## `Erdos825.erdos_825.variants.necessary_cond`

Proved here.

> Show that if the constant $C > 0$ is such that every integer $n$ with
> $\sigma(n) > Cn$ is the distinct sum of proper divisors of $n$, then we
> must have $C > 2$.

```lean
theorem erdos_825.variants.necessary_cond (C : ℝ) (_hC : 0 < C)
    (h : ∀ (n : ℕ) (_ : σ 1 n > C * n),
        ∃ s ⊆ n.properDivisors, n = s.sum id) :
    2 < C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/825.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/825.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/825.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/825.lean)
- [erdosproblems.com/825](https://www.erdosproblems.com/825)
