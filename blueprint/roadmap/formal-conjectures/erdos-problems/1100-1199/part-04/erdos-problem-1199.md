---
declaration: theorem
origin: cited
lean: Erdos1199.erdos_1199, Erdos1199.erdos_1199.variants.three
statement: formalized
---

# Erdős Problem 1199

> *References:*
> - [erdosproblems.com/1199](https://www.erdosproblems.com/1199)
> - [Hi79] Hindman, Neil, Partitions and sums of integers with repetition.
>   J. Combin. Theory Ser. A (1979), 19--32.
> - [Ow74] J. Owings, E2494. Amer. Math. Monthly (1974), 902.

*Quoted from [FormalConjectures/ErdosProblems/1199.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1199.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1199](https://www.erdosproblems.com/1199).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1199.erdos_1199`

Open: stated without proof.

> Is it true that in any 2-colouring of $\mathbb{N}$ there exists an infinite set $A$
> such that all elements of $A+A$ are the same colour?
>
> A conjecture of Owings [Ow74].

```lean
theorem erdos_1199 :
    ∀ (color : ℕ → Fin 2), ∃ (A : Set ℕ),
    A.Infinite ∧ ∀ n ∈ (A+A), ∀ m ∈ (A+A), color n = color m
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1199.lean, line 43](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1199.lean#L43).

## `Erdos1199.erdos_1199.variants.three`

Solved: stated here; a Lean proof is at [https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P1199.lean#L85](https://github.com/HowieHwong/lean-erdos-proofs/blob/b8b641ba2d00dc4d1fe205a078a4159372672459/Erdos/P1199.lean#L85).

> Hindman [Hi79] has shown that this is false for 3-colourings.

```lean
theorem erdos_1199.variants.three :
    ∃ (color : ℕ → Fin 3), ∀ (A : Set ℕ),
    A.Infinite → ∃ n ∈ (A+A), ∃ m ∈ (A+A), color n ≠ color m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1199.lean, line 54](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1199.lean#L54).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1199.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1199.lean)
- [erdosproblems.com/1199](https://www.erdosproblems.com/1199)
