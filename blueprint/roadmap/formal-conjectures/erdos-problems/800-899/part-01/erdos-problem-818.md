---
declaration: theorem
origin: cited
lean: Erdos818.erdos_818, Erdos818.erdos_818.variants.solymosi
statement: formalized
---

# Erdős Problem 818

> *References:*
> - [erdosproblems.com/818](https://www.erdosproblems.com/818)
> - [So09d] Solymosi, József, *Bounding multiplicative energy by the sumset*. Adv. Math. (2009),
>   402-408.

*Quoted from [FormalConjectures/ErdosProblems/818.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/818.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/818](https://www.erdosproblems.com/818).

The file states 2 research or textbook statements: 2 solved.

## `Erdos818.erdos_818`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos818.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos818.lean).

> Let $A$ be a finite set of integers such that $\lvert A+A\rvert \ll \lvert A\rvert$. Is it true that
>
> $$\lvert AA\rvert \gg \frac{\lvert A\rvert^2}{(\log \lvert A\rvert)^C}$$
>
> for some constant $C>0$?
>
> This was proved by Solymosi [So09d], in the strong form
>
> $$\lvert AA\rvert \gg \frac{\lvert A\rvert^2}{\log \lvert A\rvert}.$$
>
> See also [52].

```lean
theorem erdos_818 :
    ∀ K : ℝ, 0 < K → ∃ C : ℝ, 0 < C ∧ ∃ c : ℝ, 0 < c ∧
      ∀ A : Finset ℤ, 2 ≤ A.card → ((A + A).card : ℝ) ≤ K * (A.card : ℝ) →
        c * (A.card : ℝ) ^ 2 / (Real.log (A.card : ℝ)) ^ C ≤ ((A * A).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/818.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/818.lean#L46).

## `Erdos818.erdos_818.variants.solymosi`

Solved: stated here without proof.

> This was proved by Solymosi [So09d], in the strong form
>
> $$\lvert AA\rvert \gg \frac{\lvert A\rvert^2}{\log \lvert A\rvert}.$$

```lean
theorem erdos_818.variants.solymosi :
    ∀ K : ℝ, 0 < K → ∃ c : ℝ, 0 < c ∧
      ∀ A : Finset ℤ, 2 ≤ A.card → ((A + A).card : ℝ) ≤ K * (A.card : ℝ) →
        c * (A.card : ℝ) ^ 2 / Real.log (A.card : ℝ) ≤ ((A * A).card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/818.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/818.lean#L57).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/818.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/818.lean)
- [erdosproblems.com/818](https://www.erdosproblems.com/818)
