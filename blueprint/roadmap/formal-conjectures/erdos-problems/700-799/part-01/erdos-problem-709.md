---
declaration: theorem
origin: cited
lean: Erdos709.erdos_709.variants.singleton, Erdos709.erdos_709, Erdos709.erdos_709.variants.ersu_lower, Erdos709.erdos_709.variants.ersu_upper, Erdos709.erdos_709.variants.van_doorn_lower
statement: formalized
---

# Erdős Problem 709

> *References:*
> - [erdosproblems.com/709](https://www.erdosproblems.com/709)
> - [ErSu59] P. Erdős and J. Surányi, Bemerkungen zu einer Aufgabe eines mathematischen
>   Wettbewerbs, Mat. Lapok 10 (1959), 39–48.
> - [Er92c] P. Erdős, Some of my forgotten problems in number theory, Hardy–Ramanujan J. 15
>   (1992), 34–50.
> - [vD26] W. van Doorn, On the length of an interval that contains distinct multiples of the
>   first $n$ positive integers, Integers (2026), #A7.

*Quoted from [FormalConjectures/ErdosProblems/709.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/709](https://www.erdosproblems.com/709).

The file states 5 research or textbook statements: 1 open, 3 solved and 1 textbook result. It also has 1 test statement and 4 API statements, counted here but not shown.

## `Erdos709.erdos_709.variants.singleton`

Textbook result, proved here.

> Erdős Problem 709 holds for a singleton input: the multiplier `1` suffices.

```lean
theorem erdos_709.variants.singleton : Works 1 1
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/709.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean#L109).

## `Erdos709.erdos_709`

Open: stated without proof.

> Let $f(n)$ be minimal such that, for any $A=\{a_1,\ldots,a_n\}\subseteq [2,\infty)\cap\mathbb{N}$
> of size $n$, in any interval $I$ of $f(n)\max(A)$ consecutive integers there exist distinct
> $x_1,\ldots,x_n\in I$ such that $a_i\mid x_i$.
>
> Obtain good bounds for $f(n)$, or even an asymptotic formula.
>
> We read "good bounds" as determining the order of magnitude of $f(n)$.

```lean
theorem erdos_709 : f =Θ[atTop] erdos_709.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/709.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean#L174).

## `Erdos709.erdos_709.variants.ersu_lower`

Solved: stated here without proof.

> A problem of Erdős and Surányi [ErSu59], who proved
>
> $$(\log n)^c \ll f(n) \ll n^{1/2}$$
>
> for some constant $c>0$.
>
> This is the lower bound.

```lean
theorem erdos_709.variants.ersu_lower :
    ∃ c > (0 : ℝ), (fun n : ℕ ↦ Real.log n ^ c) =O[atTop] f
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/709.lean, line 185](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean#L185).

## `Erdos709.erdos_709.variants.ersu_upper`

Solved: stated here without proof.

> A problem of Erdős and Surányi [ErSu59], who proved
>
> $$(\log n)^c \ll f(n) \ll n^{1/2}$$
>
> for some constant $c>0$.
>
> This is the upper bound.

```lean
theorem erdos_709.variants.ersu_upper :
    f =O[atTop] fun n : ℕ ↦ (n : ℝ) ^ (1 / 2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/709.lean, line 197](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean#L197).

## `Erdos709.erdos_709.variants.van_doorn_lower`

Solved: stated here without proof.

> The lower bound here can be improved, using van Doorn's lower bound for [711] from [vD26], to
>
> $$\frac{\log n}{\log\log n}\ll f(n).$$

```lean
theorem erdos_709.variants.van_doorn_lower :
    (fun n : ℕ ↦ Real.log n / Real.log (Real.log n)) =O[atTop] f
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/709.lean, line 206](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean#L206).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/709.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/709.lean)
- [erdosproblems.com/709](https://www.erdosproblems.com/709)
