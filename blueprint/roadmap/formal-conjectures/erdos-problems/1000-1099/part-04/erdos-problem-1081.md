---
declaration: theorem
origin: cited
lean: Erdos1081.erdos_1081, Erdos1081.erdos_1081.variants.blomer_granville
statement: formalized
---

# Erdős Problem 1081

> *References:*
> - [erdosproblems.com/1081](https://www.erdosproblems.com/1081)
> - [Er76e] Erdős, P., *Problems and results on consecutive integers*.
>   Publ. Math. Debrecen 23 (1976), 271-282.
> - [Od81] Odoni, R. W. K., *A problem of Erdős on sums of two squarefull numbers*.
>   Acta Arith. 39 (1981), 145-162.
> - [BlGr06] Blomer, V. and Granville, A., *Estimates for representation numbers of quadratic
>   forms*. Duke Math. J. 135 (2006), 261-302.

*Quoted from [FormalConjectures/ErdosProblems/1081.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1081.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1081](https://www.erdosproblems.com/1081).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos1081.erdos_1081`

Solved: stated here without proof.

> Let $A(x)$ count the number of $n\leq x$ which are the sum of two squarefull numbers (a number
> $m$ is squarefull if $p\mid m$ implies $p^2\mid m$). Is it true that
>
> $$A(x) \sim c \frac{x}{\sqrt{\log x}}$$
>
> for some $c>0$?
>
> Odoni [Od81] proved this is false.

```lean
theorem erdos_1081 :
    ¬ ∃ c > (0 : ℝ),
      (fun x : ℝ ↦ (A x : ℝ)) ~[atTop] fun x ↦ c * x / Real.sqrt (Real.log x)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1081.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1081.lean#L67).

## `Erdos1081.erdos_1081.variants.blomer_granville`

Solved: stated here without proof.

> Blomer and Granville [BlGr06] proved
>
> $$A(x)= (\log\log x)^{O(1)}\frac{x}{(\log x)^{\alpha}}$$
>
> where $\alpha=1-2^{-1/3}\approx 0.206299$: for some $C$ and all large $x$, $A(x)$ lies between
> $(\log\log x)^{-C}$ and $(\log\log x)^{C}$ times $x/(\log x)^{\alpha}$.

```lean
theorem erdos_1081.variants.blomer_granville :
    ∃ C : ℝ, 0 < C ∧ ∀ᶠ x : ℝ in atTop,
      x / Real.log x ^ alpha / Real.log (Real.log x) ^ C ≤ A x ∧
        (A x : ℝ) ≤ x / Real.log x ^ alpha * Real.log (Real.log x) ^ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1081.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1081.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1081.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1081.lean)
- [erdosproblems.com/1081](https://www.erdosproblems.com/1081)
