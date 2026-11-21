---
declaration: theorem
origin: cited
lean: Erdos1201.erdos_1201, Erdos1201.erdos_1201.variants.epsilon_half
statement: formalized
---

# Erdős Problem 1201

> *Reference:* [erdosproblems.com/1201](https://www.erdosproblems.com/1201)

*Quoted from [FormalConjectures/ErdosProblems/1201.lean](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1201.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [d8d031d4](https://github.com/google-deepmind/formal-conjectures/tree/d8d031d4998c78575159ccab9a7a9e95ce043883), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1201](https://www.erdosproblems.com/1201).

The file states 2 research or textbook statements: 1 open and 1 solved.

## `Erdos1201.erdos_1201`

Open: stated without proof.

> Is it true that for every $\epsilon,\eta>0$ there exists a $k$ such that the density of $n$
> for which $P(n(n+1)\cdots(n+k))>n^{1-\epsilon}$ is at least $1-\eta$ (where $P(m)$ is the greatest
> prime divisor of $m$)?

```lean
theorem erdos_1201 :
    ∀ ε > 0, ∀ η > 0, ∃ k : ℕ,
      atTop.liminf (fun x : ℕ ↦
        (((count (· ∈ Erdos1201Set ε k) x : ℝ) / (x : ℝ)) : EReal)) ≥ (1 - η : EReal)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1201.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1201.lean#L47).

## `Erdos1201.erdos_1201.variants.epsilon_half`

Solved: stated here without proof.

> Erdős wrote he could prove this for $\epsilon=1/2$.

```lean
theorem erdos_1201.variants.epsilon_half :
    ∀ η > 0, ∃ k : ℕ,
      atTop.liminf (fun x : ℕ ↦
        (((count (· ∈ Erdos1201Set (1 / 2 : ℝ) k) x : ℝ) / (x : ℝ)) : EReal)) ≥ (1 - η : EReal)
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1201.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1201.lean#L58).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1201.lean at d8d031d4](https://github.com/google-deepmind/formal-conjectures/blob/d8d031d4998c78575159ccab9a7a9e95ce043883/FormalConjectures/ErdosProblems/1201.lean)
- [erdosproblems.com/1201](https://www.erdosproblems.com/1201)
