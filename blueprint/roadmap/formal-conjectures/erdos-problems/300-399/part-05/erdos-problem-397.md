---
declaration: theorem
origin: cited
lean: Erdos397.erdos_397
statement: formalized
---

# Erdős Problem 397

> *References:*
> - [erdosproblems.com/397](https://www.erdosproblems.com/397)
> - [MathOverflow] (https://mathoverflow.net/questions/138209/product-of-central-binomial-coefficients)

*Quoted from [FormalConjectures/ErdosProblems/397.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/397.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/397](https://www.erdosproblems.com/397).

The file states 1 research or textbook statement: 1 solved.

## `Erdos397.erdos_397`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/llllvvuu/40d68cfa9de9f43eece07ff4fdc3b0ef/raw/966750065320fe126fbe5a8a7ea50439d7519c6c/397.lean](https://gist.githubusercontent.com/llllvvuu/40d68cfa9de9f43eece07ff4fdc3b0ef/raw/966750065320fe126fbe5a8a7ea50439d7519c6c/397.lean); a Lean proof is at [https://github.com/XC0R/formal-conjectures/blob/3c356a50a21bcbf3543f960b0c92d7fb26228cb6/FormalConjectures/ErdosProblems/397.lean#L147](https://github.com/XC0R/formal-conjectures/blob/3c356a50a21bcbf3543f960b0c92d7fb26228cb6/FormalConjectures/ErdosProblems/397.lean#L147).

> Are there only finitely many solutions to
>
> $$
>   \prod_i \binom{2m_i}{m_i}=\prod_j \binom{2n_j}{n_j}
> $$
>
> with the $m_i,n_j$ distinct?
>
> Somani, using ChatGPT, has given a negative answer. In fact, for any $a\geq 2$, if $c=8a^2+8a+1$,
> $\binom{2a}{a}\binom{4a+4}{2a+2}\binom{2c}{c}= \binom{2a+2}{a+1}\binom{4a}{2a}\binom{2c+2}{c+1}.$
> Further families of solutions are given in the comments by SharkyKesa.
>
> This was earlier asked about in a [MathOverflow] question, in response to which Elkies also gave an
> alternative construction which produces solutions - at the moment it is not clear whether Elkies'
> argument gives infinitely many solutions (although Bloom believes that it can).
>
> This was formalized in Lean by Wu using Aristotle.

```lean
theorem erdos_397 :
    ¬ {(M, N) : Finset ℕ × Finset ℕ | Disjoint M N ∧
    ∏ i ∈ M, centralBinom i = ∏ j ∈ N, centralBinom j}.Finite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/397.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/397.lean#L55).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/397.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/397.lean)
- [erdosproblems.com/397](https://www.erdosproblems.com/397)
