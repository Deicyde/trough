---
declaration: theorem
origin: cited
lean: Erdos350.erdos_350, Erdos350.erdos_350.variants.strengthening
statement: formalized
---

# Erdős Problem 350

> *References:*
> - [erdosproblems.com/350](https://www.erdosproblems.com/350)
> - [BeEr74] Benkoski, S. J. and Erdős, P., On weird and pseudoperfect numbers. Math. Comp. (1974),
>   617-623.
> - [HSS77] Hanson, F. and Steele, J. M. and Stenger, F., Distinct sums over subsets. Proc. Amer.
>   Math. Soc. (1977), 179-180.

*Quoted from [FormalConjectures/ErdosProblems/350.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/350.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/350](https://www.erdosproblems.com/350).

The file states 2 research or textbook statements: 2 solved. It also has 2 test statements and 1 API statement, counted here but not shown.

## `Erdos350.erdos_350`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos350.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos350.lean); a Lean proof is at [https://github.com/XC0R/formal-conjectures/blob/ba788c9124b563bce98a3413d474b3a2731fd0af/FormalConjectures/ErdosProblems/350.lean#L226](https://github.com/XC0R/formal-conjectures/blob/ba788c9124b563bce98a3413d474b3a2731fd0af/FormalConjectures/ErdosProblems/350.lean#L226).

> If `A ⊂ ℕ` is a finite set of integers all of whose subset sums are distinct then `∑ n ∈ A, 1/n < 2`.
> Proved by Ryavec.
>
> This was proved by Ryavec, who did not appear to ever publish the proof. Ryavec's proof is
> reproduced in [BeEr74]. More generally, Ryavec's proof delivers that
> $\sum_{n\in A}\frac{1}{n}\leq 2-2^{1-\lvert A\rvert},$ with equality if and only if
> $A=\{1,2,\ldots,2^k\}$.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_350 (A : Finset ℕ) (hA : DecidableDistinctSubsetSums A) :
    ∑ n ∈ A, (1 / n : ℝ) < 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/350.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/350.lean#L77).

## `Erdos350.erdos_350.variants.strengthening`

Solved: stated here without proof.

> If `A ⊂ ℕ` is a finite set of integers all of whose subset sums are distinct then `∑ n ∈ A, 1/n^s < 1/(1 - 2^(-s))`, for any `s > 0`.
> Proved by Hanson, Steele, and Stenger [HSS77].
>
> We exclude here the case `s = 0`, because in the informal formulation then the right hand side is to be interpreted as `∞`, while the left hand side counts the elements in `A`.

```lean
theorem erdos_350.variants.strengthening (A : Finset ℕ) (hA : DecidableDistinctSubsetSums A)
    (s : ℝ) (hs : 0 < s) : ∑ n ∈ A, (1 / n : ℝ)^s < 1 / (1 - 2^(-s))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/350.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/350.lean#L88).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/350.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/350.lean)
- [erdosproblems.com/350](https://www.erdosproblems.com/350)
