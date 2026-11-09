---
declaration: theorem
origin: cited
lean: Erdos535.erdos_535, Erdos535.erdos_535.variants.first_open_case, Erdos535.erdos_535.variants.erdos_upper_bound, Erdos535.erdos_535.variants.lower_bound, Erdos535.erdos_535.variants.abbott_hanson, Erdos535.erdos_535.variants.sunflower_strong, Erdos535.erdos_535.variants.sunflower_erdos_rado
statement: formalized
---

# Erdős Problem 535

> *References:*
> - [erdosproblems.com/535](https://www.erdosproblems.com/535)
> - [Er64] P. Erdős, _On a problem in elementary number theory and a combinatorial problem_. Math.
>   Comp. (1964), 644–646.
> - [AbHa70] H. L. Abbott and D. Hanson, _An extremal problem in number theory_. Bull. London Math.
>   Soc. (1970), 324–326.
> - [Er73] P. Erdős, _Problems and results on combinatorial number theory_, in
>   *A Survey of Combinatorial Theory*, North-Holland, 1973.

*Quoted from [FormalConjectures/ErdosProblems/535.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/535](https://www.erdosproblems.com/535).

The file states 7 research or textbook statements: 3 open and 4 solved.

## `Erdos535.erdos_535`

Open: stated without proof.

> Let $r \geq 3$, and let $f_r(N)$ denote the size of the largest subset of $\{1,\ldots,N\}$
> such that no subset of size $r$ has the same pairwise greatest common divisor between all
> elements. Erdős [Er64] proved that $f_3(N) > N^{c/\log\log N}$ for some constant $c > 0$, and
> conjectured this should also be an upper bound; here we state the conjectural upper bound
> for all $r \geq 3$.
>
> See also [536].

```lean
theorem erdos_535 : ∀ r ≥ 3, ∃ c > (0 : ℝ),
    ∀ᶠ (N : ℕ) in atTop,
      (f r N : ℝ) ≤ (N : ℝ) ^ (c / log (log (N : ℝ)))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L76).

## `Erdos535.erdos_535.variants.first_open_case`

Open: stated without proof.

> The first open case of Erdős Problem 535 is $r = 3$: there should exist $c > 0$ such that
> $f_3(N) \leq N^{c/\log\log N}$ for all sufficiently large $N$.

```lean
theorem erdos_535.variants.first_open_case : ∃ c > (0 : ℝ),
    ∀ᶠ (N : ℕ) in atTop,
      (f 3 N : ℝ) ≤ (N : ℝ) ^ (c / log (log (N : ℝ)))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L86).

## `Erdos535.erdos_535.variants.erdos_upper_bound`

Solved: stated here without proof.

> Erdős [Er64] proved that $f_r(N) \leq N^{3/4+o(1)}$ for all $r \geq 3$.

```lean
theorem erdos_535.variants.erdos_upper_bound {r : ℕ} (hr : 3 ≤ r) :
    ∀ ε > (0 : ℝ), ∀ᶠ (N : ℕ) in atTop,
      (f r N : ℝ) ≤ (N : ℝ) ^ ((3 : ℝ) / 4 + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 93](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L93).

## `Erdos535.erdos_535.variants.lower_bound`

Solved: stated here without proof.

> Erdős [Er64] proved that $f_3(N) > N^{c/\log\log N}$ for some constant $c > 0$.

```lean
theorem erdos_535.variants.lower_bound : ∃ c > (0 : ℝ),
    ∀ᶠ (N : ℕ) in atTop,
      (N : ℝ) ^ (c / log (log (N : ℝ))) ≤ (f 3 N : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L100).

## `Erdos535.erdos_535.variants.abbott_hanson`

Solved: stated here without proof.

> Abbott and Hanson [AbHa70] improved Erdős's upper bound to $f_r(N) \leq N^{1/2+o(1)}$
> for all $r \geq 3$.

```lean
theorem erdos_535.variants.abbott_hanson {r : ℕ} (hr : 3 ≤ r) :
    ∀ ε > (0 : ℝ), ∀ᶠ (N : ℕ) in atTop,
      (f r N : ℝ) ≤ (N : ℝ) ^ ((1 : ℝ) / 2 + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 108](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L108).

## `Erdos535.erdos_535.variants.sunflower_strong`

Open: stated without proof.

> Erdős [Er73] records that Abbott pointed out the ordinary sunflower conjecture
> does not seem to suffice here. The stronger auxiliary conjecture uses $Ω(n)=k$,
> i.e. prime factors counted with multiplicity; this stronger statement would imply
> the conjectured upper bound for $f_r(N)$.

```lean
theorem erdos_535.variants.sunflower_strong {r : ℕ} (hr : 3 ≤ r) :
    ∃ c_r > (0 : ℝ),
      ∀ k : ℕ, ∀ A : Finset ℕ,
        AllBigOmega k A →
        NoConstantPairwiseGcdCoprimeSubsets r A →
        (A.card : ℝ) ≤ c_r ^ k
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L120).

## `Erdos535.erdos_535.variants.sunflower_erdos_rado`

Solved: stated here without proof.

> For the stronger $Ω(n)=k$ variant above, the Erdős–Rado method gives the weaker
> bound $c_r^k \cdot k!$; see Erdős [Er73].

```lean
theorem erdos_535.variants.sunflower_erdos_rado {r : ℕ} (hr : 3 ≤ r) :
    ∃ c_r > (0 : ℝ),
      ∀ k : ℕ, ∀ A : Finset ℕ,
        AllBigOmega k A →
        NoConstantPairwiseGcdCoprimeSubsets r A →
        (A.card : ℝ) ≤ c_r ^ k * (Nat.factorial k)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/535.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean#L133).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/535.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/535.lean)
- [erdosproblems.com/535](https://www.erdosproblems.com/535)
