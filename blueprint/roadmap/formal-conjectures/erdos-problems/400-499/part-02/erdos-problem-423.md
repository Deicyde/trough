---
declaration: theorem
origin: cited
lean: Erdos423.erdos_423, Erdos423.erdos_423.variants.nondecreasing, Erdos423.erdos_423.variants.unbounded, Erdos423.erdos_423.variants.infinite_complement, Erdos423.erdos_423.variants.upper_bound, Erdos423.erdos_423.variants.lower_bound
statement: formalized
---

# Erdős Problem 423

> *References:*
> - [erdosproblems.com/423](https://www.erdosproblems.com/423)
> - [Er77c] Erdős, P., *Problems and results on combinatorial number theory. III*,
>   Number theory day (Proc. Conf., Rockefeller Univ., New York, 1976), 1977, pp. 43–72.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial
>   number theory*, Monographies de L'Enseignement Mathématique (1980).
> - [Cu25] Cushman, A., *A Note on the Sum-Product Problem and the Convex Sumset Problem*.
>   arXiv:2512.13849 (2025).
> - [Ta26] Tang, Q., *The Hofstadter consecutive-sum sequence omits infinitely many positive
>   integers*. arXiv:2603.09939 (2026).
> - [Bolan] Bolan, M., *Hofstader–Ulam Sequence*,
>   https://github.com/mjtb49/HofstaderUlam/blob/main/HofstaderUlamSequence.pdf
> - [OEIS A005243](https://oeis.org/A005243)

*Quoted from [FormalConjectures/ErdosProblems/423.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/423](https://www.erdosproblems.com/423).

The file states 6 research or textbook statements: 1 open and 5 solved. It also has 3 test statements and 5 API statements, counted here but not shown.

## `Erdos423.erdos_423`

Open: stated without proof.

> Erdős Problem 423 [Er77c, p.71; ErGr80, p.83]:
>
> Let $a(1) = 1$, $a(2) = 2$, and for $k \ge 3$ let $a(k)$ be the least integer greater
> than $a(k-1)$ that is a sum of at least two consecutive terms of the sequence.
> What is the asymptotic behaviour of this sequence? It seems likely that $a_n = n + o(n)$.

```lean
theorem erdos_423 :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a →
    (fun n : ℕ => (a n : ℝ) - n) =o[atTop] (fun n : ℕ => (n : ℝ))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L110).

## `Erdos423.erdos_423.variants.nondecreasing`

Proved here.

> Bolan and Tang [Ta26] independently proved that $a_n-n$ is nondecreasing.

```lean
theorem erdos_423.variants.nondecreasing :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a →
    ∀ n m : ℕ, 1 ≤ n → n ≤ m → a n - n ≤ a m - m
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L119).

## `Erdos423.erdos_423.variants.unbounded`

Solved: stated here without proof.

> Bolan and Tang [Ta26] independently proved that $a_n-n\to\infty$.

```lean
theorem erdos_423.variants.unbounded :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a →
    ∀ M : ℕ, ∀ᶠ n in atTop, M + n ≤ a n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L148).

## `Erdos423.erdos_423.variants.infinite_complement`

Solved: stated here without proof.

> Bolan and Tang [Ta26] independently proved that infinitely many positive integers do not occur in
> the Hofstadter sequence.

```lean
theorem erdos_423.variants.infinite_complement :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a → Set.Infinite (Set.range a)ᶜ
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 158](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L158).

## `Erdos423.erdos_423.variants.upper_bound`

Solved: stated here without proof.

> Tang [Ta26] proved $a_n \ll n^{1/(c-1)+o(1)}$ whenever every finite convex set $A$ satisfies
> $|A-A|\geq |A|^{c-o(1)}$. Using the bound of Cushman [Cu25] gives
> $a_n\ll n^{688/413+o(1)}$.

```lean
theorem erdos_423.variants.upper_bound :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a →
    ∀ ε > (0 : ℝ), (fun n => (a n : ℝ)) =O[atTop]
      (fun n => (n : ℝ) ^ ((688 : ℝ) / 413 + ε))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 295](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L295).

## `Erdos423.erdos_423.variants.lower_bound`

Solved: stated here without proof.

> Tang [Ta26] proved the lower bound $a_n=n+\Omega(\log\log n)$.

```lean
theorem erdos_423.variants.lower_bound :
    ∀ a : ℕ → ℕ, IsHofstadterSeq a →
    (fun n : ℕ => Real.log (Real.log n)) =O[atTop]
      (fun n : ℕ => (a n : ℝ) - n)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/423.lean, line 305](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean#L305).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/423.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/423.lean)
- [erdosproblems.com/423](https://www.erdosproblems.com/423)
