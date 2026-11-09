---
declaration: theorem
origin: cited
lean: Erdos303.erdos_303
statement: formalized
---

# Erdős Problem 303

> *References:*
> - [erdosproblems.com/303](https://www.erdosproblems.com/303)
> - [BrRo91] Brown, Tom C. and Rödl, Voijtech, Monochromatic solutions to equations with unit
>   fractions. Bull. Austral. Math. Soc. (1991), 387-392.

*Quoted from [FormalConjectures/ErdosProblems/303.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/303.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/303](https://www.erdosproblems.com/303).

The file states 1 research or textbook statement: 1 solved.

## `Erdos303.erdos_303`

Solved: stated here; a Lean proof is at [https://www.erdosproblems.com/forum/thread/303](https://www.erdosproblems.com/forum/thread/303).

> Is it true that in any finite colouring of the integers there exists a monochromatic solution
> to $\frac 1 a = \frac 1 b + \frac 1 c$ with distinct $a, b, c$?
>
> This is true, as proved by Brown and Rödl [BrRo91].
>
> This was formalized in Lean by Yuan using Seed-Prover.

```lean
theorem erdos_303 :
    -- For any finite colouring of the integers
    ∀ (𝓒 : ℤ → ℤ), (Set.range 𝓒).Finite →
      -- There exists integers `a, b, c`
      ∃ (a b c : ℤ),
      -- that are non-zero and distinct.
      [a, b, c, 0].Nodup ∧
      -- `a, b, c` satisfy the equation
      (1/a : ℝ) = 1/b + 1/c ∧
      -- `a, b, c` have the same color
      (𝓒 '' {a, b, c}).Subsingleton
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/303.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/303.lean#L43).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/303.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/303.lean)
- [erdosproblems.com/303](https://www.erdosproblems.com/303)
