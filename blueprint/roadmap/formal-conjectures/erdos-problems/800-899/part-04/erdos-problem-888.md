---
declaration: theorem
origin: cited
lean: Erdos888.erdos_888, Erdos888.erdos_888.variants.sarkozy, Erdos888.erdos_888.variants.primes, Erdos888.erdos_888.variants.semiprimes
statement: formalized
---

# Erdős Problem 888

> *References:*
> - [erdosproblems.com/888](https://www.erdosproblems.com/888)
> - [Er98] Erdős, Paul, Some of my new and almost new problems and results in combinatorial number
>   theory. Number theory (Eger, 1996) (1998), 169-180.

*Quoted from [FormalConjectures/ErdosProblems/888.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/888](https://www.erdosproblems.com/888).

The file states 4 research or textbook statements: 4 solved.

## `Erdos888.erdos_888`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos888.lean#L47](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos888.lean#L47).

> What is the size of the largest $A\subseteq \{1,\ldots,n\}$ such that if
> $a\leq b\leq c\leq d\in A$ are such that $abcd$ is a square then $ad=bc$?
>
> This was proved by GPT-5.5 Pro (prompted by Chojecki).

```lean
theorem erdos_888 :
    (fun n : ℕ ↦ (Nat.findGreatest (p n) n : ℝ)) =Θ[atTop]
      (fun n : ℕ ↦ (n : ℝ) * Real.log (Real.log n) / Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/888.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean#L59).

## `Erdos888.erdos_888.variants.sarkozy`

Solved: stated here without proof.

> Erdős claims that Sárközy proved that $\lvert A\rvert =o(n)$ (a proof of this
> bound is provided by Tao in the comments).

```lean
theorem erdos_888.variants.sarkozy :
    (fun n ↦ (Nat.findGreatest (p n) n : ℝ)) =o[atTop] (Nat.cast : ℕ → ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/888.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean#L70).

## `Erdos888.erdos_888.variants.primes`

Solved: stated here without proof.

> The primes show that $\lvert A\rvert \gg n/\log n$ is possible.

```lean
theorem erdos_888.variants.primes :
    (fun n : ℕ ↦ (Nat.findGreatest (p n) n : ℝ)) ≫ (fun n : ℕ ↦ (n : ℝ) / Real.log n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/888.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean#L79).

## `Erdos888.erdos_888.variants.semiprimes`

Solved: stated here without proof.

> Cambie and Weisenberg have noted in the comments that the set of semiprimes
> also works, showing $(1+o(1))\frac{\log\log n}{\log n}n \leq \lvert A\rvert$ is achievable.

```lean
theorem erdos_888.variants.semiprimes :
    ∃ c : ℕ → ℝ, c =o[atTop] (1 : ℕ → ℝ) ∧ ∀ᶠ n : ℕ in atTop,
      (1 + c n) * ((n : ℝ) * Real.log (Real.log n) / Real.log n) ≤ Nat.findGreatest (p n) n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/888.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean#L89).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/888.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/888.lean)
- [erdosproblems.com/888](https://www.erdosproblems.com/888)
