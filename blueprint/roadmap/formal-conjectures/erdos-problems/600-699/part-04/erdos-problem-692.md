---
declaration: theorem
origin: cited
lean: Erdos692.erdos_692.parts.i, Erdos692.erdos_692.parts.ii, Erdos692.erdos_692.variants.erdos_upper_bound, Erdos692.erdos_692.variants.cambie_three, Erdos692.erdos_692.variants.cambie_local_maxima
statement: formalized
---

# Erdős Problem 692

> *References:*
> - [erdosproblems.com/692](https://www.erdosproblems.com/692)
> - [Er79e] Erdős, Paul, Some unconventional problems in number theory. Astérisque (1979), 73-82.
> - [Ob1] Erdős, P., *Oberwolfach Mathematical Problems, Volume 1*. Mathematisches
>   Forschungsinstitut Oberwolfach (Various).
> - [Fo08] Ford, Kevin, *The distribution of integers with a divisor in a given interval*.
>   Ann. of Math. (2) (2008), 367-433.
> - [Ca25] Cambie, S., *Resolution of Erdős' problems about unimodularity*.
>   arXiv:2501.10333 (2025).

*Quoted from [FormalConjectures/ErdosProblems/692.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/692](https://www.erdosproblems.com/692).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos692.erdos_692.parts.i`

Solved: stated here; a Lean proof is at [https://gist.githubusercontent.com/pitmonticone/96516af9100a37a1da81908dc0b0410c/raw/a1d6ca7f3835c58b257e5e715c8fdf3a224e1bd0/Erdos692.lean](https://gist.githubusercontent.com/pitmonticone/96516af9100a37a1da81908dc0b0410c/raw/a1d6ca7f3835c58b257e5e715c8fdf3a224e1bd0/Erdos692.lean).

> Let $\delta_1(n,m)$ be the density of the set of integers with exactly one divisor in $(n,m)$.
> Is $\delta_1(n,m)$ unimodular for $m>n+1$ (i.e. increases until some $m$ then decreases
> thereafter)?
>
> Cambie has calculated that unimodularity fails even for $n=2$ and $n=3$.
>
> This was formalized in Lean by Monticone using Aristotle.

```lean
theorem erdos_692.parts.i :
    ¬ ∀ δ : ℕ → ℕ → ℝ, (∀ a b, IsDelta₁ a b (δ a b)) → ∀ n, UnimodularOn (δ n) (n + 1)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/692.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean#L72).

## `Erdos692.erdos_692.parts.ii`

Open: stated without proof.

> Let $\delta_1(n,m)$ be the density of the set of integers with exactly one divisor in $(n,m)$.
> For fixed $n$, where does $\delta_1(n,m)$ achieve its maximum?

```lean
theorem erdos_692.parts.ii (n : ℕ) :
    ∀ δ : ℕ → ℕ → ℝ, (∀ a b, IsDelta₁ a b (δ a b)) →
      IsGreatest (δ n '' Set.Ioi (n + 1)) (δ n erdos_692.parts.ii.answer)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/692.lean, line 83](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean#L83).

## `Erdos692.erdos_692.variants.erdos_upper_bound`

Solved: stated here without proof.

> Erdős proved that
>
> $$\delta_1(n,m) \ll \frac{1}{(\log n)^c}$$
>
> for all $m$, for some constant $c>0$.

```lean
theorem erdos_692.variants.erdos_upper_bound :
    ∀ δ : ℕ → ℕ → ℝ, (∀ a b, IsDelta₁ a b (δ a b)) →
      ∃ c > (0 : ℝ), ∃ C > (0 : ℝ), ∀ᶠ n in atTop, ∀ m, δ n m ≤ C / Real.log n ^ c
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/692.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean#L94).

## `Erdos692.erdos_692.variants.cambie_three`

Solved: stated here; a Lean proof is at [https://github.com/linrock/math-proofs/blob/b8e7531a14cbe5c18ea1ae2e9e85b811bc3c7a46/erdos-692/Solution.lean#L26](https://github.com/linrock/math-proofs/blob/b8e7531a14cbe5c18ea1ae2e9e85b811bc3c7a46/erdos-692/Solution.lean#L26).

> Cambie has calculated that unimodularity fails even for $n=2$ and $n=3$. For example,
>
> $$\delta_1(3,6)= 0.35\quad \delta_1(3,7)\approx 0.33\quad \delta_1(3,8)\approx 0.3619.$$

```lean
theorem erdos_692.variants.cambie_three :
    ∀ δ : ℕ → ℕ → ℝ, (∀ a b, IsDelta₁ a b (δ a b)) →
      δ 3 7 < δ 3 6 ∧ δ 3 7 < δ 3 8
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/692.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean#L106).

## `Erdos692.erdos_692.variants.cambie_local_maxima`

Solved: stated here without proof.

> Cambie [Ca25] has shown that, for fixed $n$, the sequence $\delta_1(n,m)$ has superpolynomially
> many local maxima $m$. A local maximum is a maximal run of equal values of the sequence that is
> strictly larger than the values just before and just after the run.

```lean
theorem erdos_692.variants.cambie_local_maxima (k : ℕ) :
    ∀ δ : ℕ → ℕ → ℝ, (∀ a b, IsDelta₁ a b (δ a b)) →
      ∀ᶠ n : ℕ in atTop, (n : ℕ∞) ^ k ≤ (localMaxima (δ n) (n + 1)).encard
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/692.lean, line 117](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean#L117).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/692.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/692.lean)
- [erdosproblems.com/692](https://www.erdosproblems.com/692)
