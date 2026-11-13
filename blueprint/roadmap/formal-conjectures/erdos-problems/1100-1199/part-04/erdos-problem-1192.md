---
declaration: theorem
origin: cited
lean: Erdos1192.erdos_1192, Erdos1192.erdos_1192.variants.renyi, Erdos1192.erdos_1192.variants.ruzsa
statement: formalized
---

# Erdős Problem 1192

> *References:*
> - [erdosproblems.com/1192](https://www.erdosproblems.com/1192)
> - [Ru90] Ruzsa, Imre Z., A just basis. Monatsh. Math. (1990), 145--151.
> - [Er80] Erdős, Paul, A survey of problems in combinatorial number theory.
>   Ann. Discrete Math. 6 (1980), 89--115.

*Quoted from [FormalConjectures/ErdosProblems/1192.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1192.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1192](https://www.erdosproblems.com/1192).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 4 test statements, counted here but not shown.

## `Erdos1192.erdos_1192`

Open: stated without proof.

> Does there exist, for all $r\geq 2$, a basis $A$ of order $r$ (so that $f_r(n)>0$ for all
> large $n$) such that
>
> $$\sum_{n\leq x}f_r(n)^2 \ll x$$
>
> for all $x$?

```lean
theorem erdos_1192 :
    ∀ r ≥ 2, ∃ A : Set ℕ,
      (∀ᶠ n in atTop, f_r A r n > 0) ∧
      (fun (x : ℕ) ↦ ∑ n ∈ range (x + 1), (f_r A r n : ℝ) ^ 2) =O[atTop]
        (fun (x : ℕ) ↦ (x : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1192.lean, line 97](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1192.lean#L97).

## `Erdos1192.erdos_1192.variants.renyi`

Solved: stated here without proof.

> Erdős and Rényi proved by the probabilistic method that there exists a set $A$ such that
>
> $$\sum_{n\leq x}f_r(n)^2 \ll x$$
>
> and
>
> $$\lvert A\cap [1,x]\rvert\gg x^{1/r}$$
>
> for all $x$.

```lean
theorem erdos_1192.variants.renyi :
    ∀ r ≥ 2, ∃ A : Set ℕ,
      ((fun (x : ℕ) ↦ ∑ n ∈ range (x + 1), (f_r A r n : ℝ) ^ 2) =O[atTop]
        (fun (x : ℕ) ↦ (x : ℝ))) ∧
      ((fun (x : ℕ) ↦ (x : ℝ) ^ (1 / (r : ℝ))) =O[atTop]
        (fun (x : ℕ) ↦ (count (· ∈ A) x : ℝ)))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1192.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1192.lean#L110).

## `Erdos1192.erdos_1192.variants.ruzsa`

Solved: stated here without proof.

> Ruzsa [Ru90] proved that the answer is yes for $r=2$.

```lean
theorem erdos_1192.variants.ruzsa :
    ∃ A : Set ℕ,
      (∀ᶠ n in atTop, f_r A 2 n > 0) ∧
      (fun (x : ℕ) ↦ ∑ n ∈ range (x + 1), (f_r A 2 n : ℝ) ^ 2) =O[atTop]
        (fun (x : ℕ) ↦ (x : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1192.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1192.lean#L122).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1192.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1192.lean)
- [erdosproblems.com/1192](https://www.erdosproblems.com/1192)
