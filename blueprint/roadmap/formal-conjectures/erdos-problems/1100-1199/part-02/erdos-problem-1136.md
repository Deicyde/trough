---
declaration: theorem
origin: cited
lean: Erdos1136.erdos_1136, Erdos1136.erdos_1136.variants.multiples_of_three, Erdos1136.erdos_1136.variants.mueller, Erdos1136.erdos_1136.variants.upper_bound
statement: formalized
---

# Erdős Problem 1136

> *References:*
> - [erdosproblems.com/1136](https://www.erdosproblems.com/1136)
> - [Mu11] Müller, Helmut, *Über ein additiv-zahlentheoretisches Problem von P. Erdős*.
>   Mitt. Math. Ges. Hamburg (2011), 75-78.

*Quoted from [FormalConjectures/ErdosProblems/1136.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1136](https://www.erdosproblems.com/1136).

The file states 4 research or textbook statements: 4 solved.

## `Erdos1136.erdos_1136`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1136.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1136.lean).

> Does there exist $A\subset \mathbb{N}$ with lower density $>1/3$ such that $a+b\neq 2^k$ for
> any $a,b\in A$ and $k\geq 0$?
>
> Müller [Mu11] settled this question in the affirmative: in fact one can take $A$ to be
> the set of all integers congruent to $3\cdot 2^i\pmod{2^{i+2}}$ for any $i\geq 0$, which has
> density $1/2$.

```lean
theorem erdos_1136 :
    ∃ A : Set ℕ, (1 / 3 : ℝ) < A.lowerDensity ∧ AvoidsPowersOfTwo A
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1136.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean#L53).

## `Erdos1136.erdos_1136.variants.multiples_of_three`

Solved: stated here without proof.

> Achieving density $1/3$ is trivial, taking $A$ to be all multiples of $3$.

```lean
theorem erdos_1136.variants.multiples_of_three :
    AvoidsPowersOfTwo {n : ℕ | 3 ∣ n} ∧ Set.HasDensity {n : ℕ | 3 ∣ n} (1 / 3)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1136.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean#L61).

## `Erdos1136.erdos_1136.variants.mueller`

Solved: stated here without proof.

> Müller [Mu11] settled this question in the affirmative: in fact one can take $A$ to be
> the set of all integers congruent to $3\cdot 2^i\pmod{2^{i+2}}$ for any $i\geq 0$, which has
> density $1/2$.

```lean
theorem erdos_1136.variants.mueller :
    AvoidsPowersOfTwo muellerSet ∧ muellerSet.HasDensity (1 / 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1136.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean#L71).

## `Erdos1136.erdos_1136.variants.upper_bound`

Solved: stated here without proof.

> Müller also proved this is best possible, in that $A$ with the property in the question has
> lower density at most $1/2$.

```lean
theorem erdos_1136.variants.upper_bound (A : Set ℕ) (hA : AvoidsPowersOfTwo A) :
    A.lowerDensity ≤ 1 / 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1136.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1136.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1136.lean)
- [erdosproblems.com/1136](https://www.erdosproblems.com/1136)
