---
declaration: theorem
origin: cited
lean: Erdos1064.erdos_1064, Erdos1064.erdos_1064.variants.k2, Erdos1064.erdos_1064.variants.general_function
statement: formalized
---

# Erdős Problem 1064

> *Reference:* [erdosproblems.com/1064](https://www.erdosproblems.com/1064)

*Quoted from [FormalConjectures/ErdosProblems/1064.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1064.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1064](https://www.erdosproblems.com/1064).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1064.erdos_1064`

Solved: stated here without proof.

> Let $ϕ(n)$ be the Euler's totient function, then the $n$ satisfies $ϕ(n)>ϕ(n - ϕ(n))$
> have asymptotic density 1.
> Reference: [LuPo02] Luca, Florian and Pomerance, Carl, On some problems of {M}\polhk akowski-{S}chinzel and {E}rd\H
> os concerning the arithmetical functions {$\phi$} and
> {$\sigma$}. Colloq. Math.

```lean
theorem erdos_1064 : {n | φ n > φ (n - φ n)}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1064.lean, line 40](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1064.lean#L40).

## `Erdos1064.erdos_1064.variants.k2`

Proved here.

> Let $ϕ(n)$ be the Euler's totient function, there exist infinitely many $n$
> such that $ϕ(n)< ϕ(n - ϕ(n))$
> Reference: [GLW01] Grytczuk, A. and Luca, F. and W\'ojtowicz, M., A conjecture of {E}rdős concerning inequalities for the
> {E}uler totient function.

```lean
theorem erdos_1064.variants.k2 : {n | φ n < φ (n - φ n)}.Infinite
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1064.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1064.lean#L50).

## `Erdos1064.erdos_1064.variants.general_function`

Solved: stated here without proof.

> For any function $f(n)=o(n)$,
> we have $\phi(n)>\phi(n-\phi(n))+f(n)$ for almost all $n$.
> Reference:
> [LuPo02] Luca, Florian and Pomerance, Carl, On some problems of {M}\polhk akowski-{S}chinzel and {E}rd\H
> os concerning the arithmetical functions {$\phi$} and
> {$\sigma$}. Colloq. Math. (2002), 111--130.

```lean
theorem erdos_1064.variants.general_function (f : ℕ → ℕ)
    (hf : (fun n ↦ (f n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ))) :
    {n : ℕ | φ (n - φ n) + f n < φ n}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1064.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1064.lean#L87).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1064.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1064.lean)
- [erdosproblems.com/1064](https://www.erdosproblems.com/1064)
