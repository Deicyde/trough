---
declaration: theorem
origin: cited
lean: Erdos1109.erdos_1109, Erdos1109.erdos_1109.variants.polylog, Erdos1109.erdos_1109.variants.erdos_sarkozy_lower, Erdos1109.erdos_1109.variants.erdos_sarkozy_upper, Erdos1109.erdos_1109.variants.konyagin_lower, Erdos1109.erdos_1109.variants.konyagin_upper
statement: formalized
---

# Erdős Problem 1109

> *References:*
> - [erdosproblems.com/1109](https://www.erdosproblems.com/1109)
> - [ErSa87] P. Erdős and A. Sárközy, *On divisibility properties of integers of the form
>   $a+a'$*, Acta Math. Hungar. (1987), 117--122.
> - [Gy01] Katalin Gyarmati, *On divisibility properties of integers of the form $ab+1$*,
>   Period. Math. Hungar. (2001), 71--79.
> - [Ko04] S. V. Konyagin, *Problems of the set of square-free numbers*,
>   Izv. Ross. Akad. Nauk Ser. Mat. (2004), 63--90.
> - [Sa92c] G. N. Sárközy, *On a problem of P. Erdős*, Acta Math. Hungar.
>   (1992), 271--282.

*Quoted from [FormalConjectures/ErdosProblems/1109.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1109](https://www.erdosproblems.com/1109).

The file states 6 research or textbook statements: 2 open and 4 solved.

## `Erdos1109.erdos_1109`

Open: stated without proof.

> Let $f(N)$ be the size of the largest subset $A\subseteq \{1,\ldots,N\}$ such that
> every $n\in A+A$ is squarefree. Estimate $f(N)$. In particular, is it true that
> $f(N)\leq N^{o(1)}$, or even $f(N) \leq (\log N)^{O(1)}$?
>
> This theorem formalizes the subpolynomial bound as `f(N) = O(N^ε)` for every `ε > 0`.

```lean
theorem erdos_1109 :
    ∀ ε > (0 : ℝ),
      (fun N : ℕ => (f N : ℝ)) ≪ fun N : ℕ => (N : ℝ) ^ ε
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L58).

## `Erdos1109.erdos_1109.variants.polylog`

Open: stated without proof.

> Is the stronger polylogarithmic bound $f(N) \leq (\log N)^{O(1)}$ true?

```lean
theorem erdos_1109.variants.polylog :
    ∃ C > (0 : ℝ),
      (fun N : ℕ => (f N : ℝ)) ≪ fun N : ℕ => (Real.log N) ^ C
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L67).

## `Erdos1109.erdos_1109.variants.erdos_sarkozy_lower`

Solved: stated here without proof.

> Erdős and Sárközy [ErSa87] proved the lower bound $\log N \ll f(N)$.

```lean
theorem erdos_1109.variants.erdos_sarkozy_lower :
    (fun N : ℕ => Real.log N) ≪ fun N : ℕ => (f N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L76).

## `Erdos1109.erdos_1109.variants.erdos_sarkozy_upper`

Solved: stated here without proof.

> Erdős and Sárközy [ErSa87] proved the upper bound $f(N) \ll N^{3/4}\log N$.

```lean
theorem erdos_1109.variants.erdos_sarkozy_upper :
    (fun N : ℕ => (f N : ℝ)) ≪
      fun N : ℕ => (N : ℝ) ^ ((3 : ℝ) / 4) * Real.log N
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 84](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L84).

## `Erdos1109.erdos_1109.variants.konyagin_lower`

Solved: stated here without proof.

> Konyagin [Ko04] improved the lower bound to
> $\log\log N(\log N)^2 \ll f(N)$.

```lean
theorem erdos_1109.variants.konyagin_lower :
    (fun N : ℕ => Real.log (Real.log N) * (Real.log N) ^ 2) ≪
      fun N : ℕ => (f N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L94).

## `Erdos1109.erdos_1109.variants.konyagin_upper`

Solved: stated here without proof.

> Konyagin [Ko04] improved the upper bound to $f(N) \ll N^{11/15+o(1)}$.

```lean
theorem erdos_1109.variants.konyagin_upper :
    ∀ ε > (0 : ℝ), (fun N : ℕ => (f N : ℝ)) ≪
      fun N : ℕ => (N : ℝ) ^ ((11 : ℝ) / 15 + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1109.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean#L103).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1109.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1109.lean)
- [erdosproblems.com/1109](https://www.erdosproblems.com/1109)
