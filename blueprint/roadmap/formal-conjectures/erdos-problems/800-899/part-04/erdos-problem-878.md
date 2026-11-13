---
declaration: theorem
origin: cited
lean: Erdos878.erdos_878.parts.i, Erdos878.erdos_878.parts.ii, Erdos878.erdos_878.parts.iii_all, Erdos878.erdos_878.parts.iii_eventually, Erdos878.erdos_878.parts.iv, Erdos878.erdos_878.parts.v, Erdos878.erdos_878.parts.vi, Erdos878.erdos_878.variants.second_question_subsequence, Erdos878.erdos_878.variants.proposed_first_question_sharp, Erdos878.erdos_878.variants.H_div_self_limsup_infinite, Erdos878.erdos_878.variants.H_div_self_liminf_finite, Erdos878.erdos_878.variants.H_upper_triple_log, Erdos878.erdos_878.variants.H_lower_quadruple_log_infinitely_often, Erdos878.erdos_878.variants.original_formula_17
statement: formalized
---

# Erdős Problem 878

> *References:*
> - [erdosproblems.com/878](https://www.erdosproblems.com/878)
> - [Er84e] Erdős, P., _On two unconventional number theoretic functions and on some
>   related problems_. (1984), 113--121.
> - [Ki26] Kitamura, K., _Erdős Problem #878 in Lean_,
>   [GitHub repository](https://github.com/KitaKen1/erdos-878-lean/tree/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76) (2026).

*Quoted from [FormalConjectures/ErdosProblems/878.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/878](https://www.erdosproblems.com/878).

The file states 14 research or textbook statements: 3 open and 11 solved.

## `Erdos878.erdos_878.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/FixedLoss.lean#L120](https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/FixedLoss.lean#L120).

> Is it true that, for almost all $n$, $f(n)=o(n\log\log n)$ and
> $F(n)\gg n\log\log n$?
>
> The answer is yes; a Lean proof is given in [Ki26].

```lean
theorem erdos_878.parts.i :
    ∃ A : Set ℕ, A.HasDensity 1 ∧
      (fun n : A ↦ (f n : ℝ)) =o[atTop]
        (fun n : A ↦ (n : ℝ) * Real.log (Real.log (n : ℝ))) ∧
      (fun n : A ↦ (n : ℝ) * Real.log (Real.log (n : ℝ))) =O[atTop]
        (fun n : A ↦ (F n : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L66).

## `Erdos878.erdos_878.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/TrackBEndpointParameters.lean#L630](https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/TrackBEndpointParameters.lean#L630).

> Is it true that $\max_{n\le x}f(n)\sim x\log x/\log\log x$?
>
> The answer is yes; a Lean proof is given in [Ki26].

```lean
theorem erdos_878.parts.ii :
    Tendsto (fun x : ℕ ↦
        (maxUpTo f x : ℝ) / ((x : ℝ) * Real.log x / Real.log (Real.log x)))
        atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L81).

## `Erdos878.erdos_878.parts.iii_all`

Solved: stated here without proof.

> Is it true that, for all $x$, $\max_{n\le x}f(n)=\max_{n\le x}F(n)$?
> Barreto noted that this is false at $x=210$.

```lean
theorem erdos_878.parts.iii_all :
    ¬ ∀ x : ℕ, maxUpTo f x = maxUpTo F x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L90).

## `Erdos878.erdos_878.parts.iii_eventually`

Solved: stated here; a Lean proof is at [https://github.com/ilpauzner/formal-conjectures/blob/b7742e7d900ca30503c0dd4c940625a6d9cf0a0c/FormalConjectures/ErdosProblems/878.lean#L435](https://github.com/ilpauzner/formal-conjectures/blob/b7742e7d900ca30503c0dd4c940625a6d9cf0a0c/FormalConjectures/ErdosProblems/878.lean#L435).

> Is it true that, for all large $x$, $\max_{n\le x}f(n)=\max_{n\le x}F(n)$?
>
> This is false, as formalized in Lean 4 by Ilia Pauzner using Gemini 4 Argon.

```lean
theorem erdos_878.parts.iii_eventually :
    ¬ ∀ᶠ x : ℕ in atTop, maxUpTo f x = maxUpTo F x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L99).

## `Erdos878.erdos_878.parts.iv`

Open: stated without proof.

> Find an asymptotic formula for the number of $n\lt x$ such that $f(n)=F(n)$.

```lean
theorem erdos_878.parts.iv :
    (fun x : ℕ ↦
      (((Finset.Ico 1 x).filter fun n ↦ f n = F n).card : ℝ))
      ~[atTop] erdos_878.parts.iv.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L107).

## `Erdos878.erdos_878.parts.v`

Open: stated without proof.

> Find an asymptotic formula for $H(x)=\sum_{n\lt x}f(n)/n$.

```lean
theorem erdos_878.parts.v :
    H ~[atTop] erdos_878.parts.v.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L117).

## `Erdos878.erdos_878.parts.vi`

Open: stated without proof.

> Is it true that $H(x)\ll x\log\log\log\log x$?

```lean
theorem erdos_878.parts.vi :
    H =O[atTop] fun x : ℕ ↦
        (x : ℝ) * Real.log (Real.log (Real.log (Real.log (x : ℝ))))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L123).

## `Erdos878.erdos_878.variants.second_question_subsequence`

Solved: stated here without proof.

> Erdős [Er84e] proved that $\max_{n\le x}f(n)\sim x\log x/\log\log x$
> for a sequence of $x\to\infty$.

```lean
theorem erdos_878.variants.second_question_subsequence :
    ∃ X : ℕ → ℕ, Tendsto X atTop atTop ∧
      Tendsto (fun k : ℕ ↦
        (maxUpTo f (X k) : ℝ) /
          ((X k : ℝ) * Real.log (X k) / Real.log (Real.log (X k))))
        atTop (𝓝 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L131).

## `Erdos878.erdos_878.variants.proposed_first_question_sharp`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/SharpFirstAsymptotic.lean#L168](https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/SharpFirstAsymptotic.lean#L168).

> For almost all $n$, $F(n)\sim \frac12 n\log\log n$.
> A Lean proof is given in [Ki26].

```lean
theorem erdos_878.variants.proposed_first_question_sharp :
    ∃ A : Set ℕ, A.HasDensity 1 ∧
      Tendsto (fun n : A ↦
        (F n : ℝ) / ((n : ℝ) * Real.log (Real.log (n : ℝ))))
        atTop (𝓝 (1 / 2 : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L145).

## `Erdos878.erdos_878.variants.H_div_self_limsup_infinite`

Solved: stated here without proof.

> Erdős [Er84e] showed that $\limsup_{x\to\infty}H(x)/x=\infty$.

```lean
theorem erdos_878.variants.H_div_self_limsup_infinite :
    ∀ C : ℝ, ∃ᶠ x : ℕ in atTop, C ≤ H x / (x : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L154).

## `Erdos878.erdos_878.variants.H_div_self_liminf_finite`

Solved: stated here without proof.

> Erdős [Er84e] showed that $\liminf_{x\to\infty}H(x)/x\lt \infty$.

```lean
theorem erdos_878.variants.H_div_self_liminf_finite :
    ∃ C : ℝ, ∃ᶠ x : ℕ in atTop, H x / (x : ℝ) ≤ C
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 160](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L160).

## `Erdos878.erdos_878.variants.H_upper_triple_log`

Solved: stated here without proof.

> Erdős [Er84e] proved that $H(x)\ll x\log\log\log x$.

```lean
theorem erdos_878.variants.H_upper_triple_log :
    H =O[atTop] fun x : ℕ ↦
      (x : ℝ) * Real.log (Real.log (Real.log (x : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L166).

## `Erdos878.erdos_878.variants.H_lower_quadruple_log_infinitely_often`

Solved: stated here without proof.

> Erdős [Er84e] proved that $x\log\log\log\log x\ll H(x)$;
> this entry records the infinitely-often consequence.

```lean
theorem erdos_878.variants.H_lower_quadruple_log_infinitely_often :
    ∃ c : ℝ, 0 < c ∧ ∃ᶠ x : ℕ in atTop,
      c * ((x : ℝ) * Real.log (Real.log (Real.log (Real.log (x : ℝ))))) ≤ H x
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L174).

## `Erdos878.erdos_878.variants.original_formula_17`

Solved: stated here; a Lean proof is at [https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/Formula17.lean#L192](https://github.com/KitaKen1/erdos-878-lean/blob/d4a8eecf0606b3eee7342c2040a31c8c30eb5d76/lean/Erdos878/Formula17.lean#L192).

> Formula (17) of [Er84e]: does $(x h(x)-m(x))/x\to\infty$?
>
> The answer is yes; a Lean proof is given in [Ki26].

```lean
theorem erdos_878.variants.original_formula_17 :
    Tendsto (fun x : ℕ ↦
        ((x * h x - m x : ℕ) : ℝ) / (x : ℝ)) atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/878.lean, line 193](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean#L193).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/878.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/878.lean)
- [erdosproblems.com/878](https://www.erdosproblems.com/878)
