---
declaration: theorem
origin: cited
lean: Erdos394.erdos_394.parts.i, Erdos394.erdos_394.parts.ii, Erdos394.erdos_394.variants.hall_bound, Erdos394.erdos_394.variants.hall_conjecture, Erdos394.erdos_394.variants.lower_bound, Erdos394.erdos_394.variants.factorial_gap_conjecture, Erdos394.erdos_394.variants.factorial_gap_10
statement: formalized
---

# Erdős Problem 394

> *References:*
> - [erdosproblems.com/394](https://www.erdosproblems.com/394)
> - [ErGr80] Erdős, P. and Graham, R., Old and new problems and results in combinatorial number
>   theory. Monographies de L'Enseignement Mathematique (1980).
> - [ErHa78] Erdős, P. and Hall, R. R., On some unconventional problems on the divisors of integers.
>   J. Austral. Math. Soc. Ser. A (1978), 479--485.

*Quoted from [FormalConjectures/ErdosProblems/394.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/394](https://www.erdosproblems.com/394).

The file states 7 research or textbook statements: 2 open and 5 solved. It also has 2 API statements, counted here but not shown.

## `Erdos394.erdos_394.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/FirstQuestion.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/FirstQuestion.lean).

> Is it true that $\sum_{n\leq x}t_2(n)\ll \frac{x^2}{(\log x)^c}$ for some $c>0$?

```lean
theorem erdos_394.parts.i :
    ∃ c > (0 : ℝ), (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
    (t 2 n : ℝ)) ≪ (fun x ↦ x ^ 2 / (Real.log x) ^ c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L70).

## `Erdos394.erdos_394.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/DenseHierarchyLittleO.lean](https://github.com/williamjblair/lean-proofs/blob/4f915a323443bfb1709a6805a013812016dca88a/starfleet/erdos-394/Research/DenseHierarchyLittleO.lean).

> Is it true that, for $k\geq 2$, $\sum_{n\leq x}t_{k+1}(n) =o\left(\sum_{n\leq x}t_k(n)\right)?$

```lean
theorem erdos_394.parts.ii :
    ∀ k ≥ 2, (fun (x : ℝ) ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
    (t (k + 1) n : ℝ)) =o[atTop]
    (fun (x : ℝ) ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
    (t k n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L80).

## `Erdos394.erdos_394.variants.hall_bound`

Solved: stated here without proof.

> In [ErGr80] they mention a conjecture of Erdős that the sum is $o(x^2)$. This was proved by Erdős
> and Hall [ErHa78], who proved that in fact
> $\sum_{n\leq x}t_2(n)\ll \frac{\log\log\log x}{\log\log x}x^2.$

```lean
theorem erdos_394.variants.hall_bound :
    (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊, (t 2 n : ℝ)) ≪
    (fun x ↦ x ^ 2 * (Real.log (Real.log (Real.log x)) / Real.log (Real.log x)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L93).

## `Erdos394.erdos_394.variants.hall_conjecture`

Open: stated without proof.

> Erdős and Hall conjecture that the sum is $o(x^2/(\log x)^c)$ for any $c\lt \log 2$.

```lean
theorem erdos_394.variants.hall_conjecture :
    ∀ c < Real.log 2, (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊,
    (t 2 n : ℝ)) =o[atTop]
    (fun x ↦ x ^ 2 / (Real.log x) ^ c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L102).

## `Erdos394.erdos_394.variants.lower_bound`

Solved: stated here without proof.

> Since $t_2(p)=p-1$ for prime $p$ it is trivial that $\sum_{n\leq x}t_2(n)\gg \frac{x^2}{\log x}$.

```lean
theorem erdos_394.variants.lower_bound :
    (fun x ↦ x ^ 2 / Real.log x) ≪
    (fun x ↦ ∑ n ∈ Icc 1 ⌊x⌋₊, (t 2 n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 112](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L112).

## `Erdos394.erdos_394.variants.factorial_gap_conjecture`

Open: stated without proof.

> They ask about the behaviour of $t_{n-3}(n!)$ and also ask whether, for infinitely many $n$,
> $t_k(n!)< t_{k-1}(n!)-1$ for all $1\leq k < n$.

```lean
theorem erdos_394.variants.factorial_gap_conjecture :
    Set.Infinite { n : ℕ | ∀ k, 2 ≤ k → k < n →
    t k (n !) < t (k - 1) (n !) - 1 }
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L122).

## `Erdos394.erdos_394.variants.factorial_gap_10`

Proved here.

> They proved (with Selfridge) that this holds for $n=10$.

```lean
theorem erdos_394.variants.factorial_gap_10 :
    ∀ (k : ℕ), 2 ≤ k → k < 10 →
    t k (10 !) <
    t (k - 1) (10 !) - 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/394.lean, line 132](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean#L132).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/394.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/394.lean)
- [erdosproblems.com/394](https://www.erdosproblems.com/394)
