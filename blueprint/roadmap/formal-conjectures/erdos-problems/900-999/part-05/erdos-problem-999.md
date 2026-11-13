---
declaration: theorem
origin: cited
lean: Erdos999.erdos_999, Erdos999.erdos_999.variants.easy_direction, Erdos999.erdos_999.variants.erdos
statement: formalized
---

# Erdős Problem 999

> *References:*
> - [erdosproblems.com/999](https://www.erdosproblems.com/999)
> - [Er64b] Erdős, P., _Problems and results on diophantine approximations_. Compositio Math.
>   (1964), 52-65.
> - [KoMa20] Koukoulopoulos, Dimitris and Maynard, James, _On the Duffin-Schaeffer conjecture_.
>   Ann. of Math. (2) (2020), 251--307.

*Quoted from [FormalConjectures/ErdosProblems/999.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/999.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/999](https://www.erdosproblems.com/999).

The file states 3 research or textbook statements: 2 solved and 1 textbook result.

## `Erdos999.erdos_999`

Solved: stated here without proof.

> For any function $f:\mathbb{N}\to \mathbb{R}_{\geq 0}$ the property that, for almost all
> $\alpha$
>
> $$\left\lvert \alpha-\frac{p}{q}\right\rvert < \frac{f(q)}{q}$$
>
> has infinitely many solutions with $(p,q)=1$, is equivalent to
>
> $$\sum_{q\geq 1}\phi(q)\frac{f(q)}{q}=\infty.$$
>
> The Duffin–Schaeffer conjecture. It is easy to prove that the latter follows from the former.
> Erdős proved this in the special case when $f(q)q$ is bounded. The full conjecture was proved by
> Koukoulopoulos and Maynard [KoMa20].

```lean
theorem erdos_999 : ∀ f : ℕ → ℝ, (∀ q, 0 ≤ f q) →
    ((∀ᵐ x : ℝ, IsApproximable f x) ↔
      ¬ Summable fun q : ℕ ↦ (Nat.totient q : ℝ) * f q / q)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/999.lean, line 55](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/999.lean#L55).

## `Erdos999.erdos_999.variants.easy_direction`

Textbook result, stated without proof.

> It is easy to prove that divergence of the series follows from approximability almost
> everywhere (the Borel–Cantelli lemma).

```lean
theorem erdos_999.variants.easy_direction (f : ℕ → ℝ) (hf : ∀ q, 0 ≤ f q)
    (h : ∀ᵐ x : ℝ, IsApproximable f x) :
    ¬ Summable fun q : ℕ ↦ (Nat.totient q : ℝ) * f q / q
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/999.lean, line 63](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/999.lean#L63).

## `Erdos999.erdos_999.variants.erdos`

Solved: stated here without proof.

> Erdős [Er64b] proved the conjecture in the special case when $f(q)q$ is bounded.

```lean
theorem erdos_999.variants.erdos (f : ℕ → ℝ) (hf : ∀ q, 0 ≤ f q)
    (hb : ∃ C : ℝ, ∀ q, f q * q ≤ C) :
    (∀ᵐ x : ℝ, IsApproximable f x) ↔
      ¬ Summable fun q : ℕ ↦ (Nat.totient q : ℝ) * f q / q
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/999.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/999.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/999.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/999.lean)
- [erdosproblems.com/999](https://www.erdosproblems.com/999)
