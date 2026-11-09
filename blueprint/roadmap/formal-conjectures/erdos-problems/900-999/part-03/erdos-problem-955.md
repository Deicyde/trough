---
declaration: theorem
origin: cited
lean: Erdos955.erdos_955, Erdos955.erdos_955.variants.positive_density, Erdos955.erdos_955.variants.empty_preimage, Erdos955.erdos_955.variants.pollack_primes, Erdos955.erdos_955.variants.troupe_unusually_many_prime_factors, Erdos955.erdos_955.variants.troupe_sum_of_two_squares, Erdos955.erdos_955.variants.pollack_pomerance_thompson_bound
statement: formalized
---

# Erdős Problem 955

> *References:*
> - [erdosproblems.com/955](https://www.erdosproblems.com/955)
> - [EGPS90] Erdős, P. and Granville, A. and Pomerance, C. and Spiro, C., On the normal behavior of
>   the iterates of some arithmetic functions. Analytic number theory (Allerton Park, IL, 1989)
>   (1990), 165-204.
> - [Er73b] Erdős, P., Über die Zahlen der Form $\sigma(n) - n$ und $n - \phi(n)$. Elem. Math.
>   (1973), 83--86.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [PPT18] Pollack, Paul and Pomerance, Carl and Thompson, Lola, Divisor-sum fibers. Mathematika
>   (2018), 330--342.
> - [Po14b] Pollack, Paul, Some arithmetic properties of the sum of proper divisors and the sum of
>   prime divisors. Illinois J. Math. (2014), 125--147.
> - [PoPo16] Pollack, Paul and Pomerance, Carl, Some problems of Erdős on the sum-of-divisors
>   function. Trans. Amer. Math. Soc. Ser. B (2016), 1--26.
> - [Tr15] Troupe, Lee, On the number of prime factors of values of the sum-of-proper-divisors
>   function. J. Number Theory (2015), 120--135.
> - [Tr20] Troupe, Lee, Divisor sums representable as the sum of two squares. Proc. Amer. Math. Soc.
>   (2020), 4189--4202.

*Quoted from [FormalConjectures/ErdosProblems/955.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/955](https://www.erdosproblems.com/955).

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 5 test statements, counted here but not shown.

## `Erdos955.erdos_955`

Open: stated without proof.

> If $A\subset \mathbb{N}$ has density $0$ then $s^{-1}(A)$ must also have density $0$.
>
> A conjecture of Erdős, Granville, Pomerance, and Spiro [EGPS90].

```lean
theorem erdos_955 :
    ∀ A : Set ℕ, A.HasDensity 0 → { x | s x ∈ A }.HasDensity 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L76).

## `Erdos955.erdos_955.variants.positive_density`

Solved: stated here without proof.

> It is possible for $s(A)$ to have positive density even if $A$ has zero density (for example
> taking $A$ to be the product of two distinct primes).

```lean
theorem erdos_955.variants.positive_density :
    ∃ A : Set ℕ, A.HasDensity 0 ∧ (∃ d > 0, (s '' A).HasDensity d)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L85).

## `Erdos955.erdos_955.variants.empty_preimage`

Solved: stated here without proof.

> Erdős [Er73b] proved that there are sets $A$ of positive density such that $s^{-1}(A)$ is empty.
>
> Here "positive density" means positive lower density: Erdős proved that the set of untouchable
> numbers (those not of the form $s(n)$) has positive lower density [Er73b, Satz I]. Pollack and
> Pomerance [PoPo16] conjecture that this set has a natural density and give a heuristic for its
> value. The same result is stated as `erdos_418.variants.sigma` in Erdős Problem 418.

```lean
theorem erdos_955.variants.empty_preimage :
    ∃ A : Set ℕ, 0 < A.lowerDensity ∧ { x | s x ∈ A } = ∅
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L98).

## `Erdos955.erdos_955.variants.pollack_primes`

Solved: stated here without proof.

> Pollack [Po14b] has shown that this is true if $A$ is the set of primes.

```lean
theorem erdos_955.variants.pollack_primes :
    { x | Nat.Prime (s x) }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L106).

## `Erdos955.erdos_955.variants.troupe_unusually_many_prime_factors`

Solved: stated here without proof.

> Troupe [Tr15] has shown that this is true if $A$ is the set of integers with unusually many prime
> factors.

```lean
theorem erdos_955.variants.troupe_unusually_many_prime_factors :
    ∀ ε > 0, { x | (1 + ε) * Real.log (Real.log (s x)) <
      (ArithmeticFunction.cardDistinctFactors (s x) : ℝ) }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L115).

## `Erdos955.erdos_955.variants.troupe_sum_of_two_squares`

Solved: stated here without proof.

> Troupe [Tr20] has also shown this is true if $A$ is the set of integers which are the sum of two
> squares.

```lean
theorem erdos_955.variants.troupe_sum_of_two_squares :
    { x | ∃ a b : ℕ, s x = a^2 + b^2 }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L125).

## `Erdos955.erdos_955.variants.pollack_pomerance_thompson_bound`

Solved: stated here without proof.

> Pollack, Pomerance, and Thompson [PPT18] prove that if $\epsilon(x)=o(1)$ and $A\subset \mathbb{N}$
> has size at most $x^{1/2+\epsilon(x)}$ then $\#\{ n\leq x: s(n)\in A\} =o(x)$ as $x\to \infty$. It
> follows that (using $s(n)\ll n\log\log n$) if $A$ grows like
> $\lvert A\cap [1,x]\rvert\leq x^{1/2+o(1)}$ then $s^{-1}(A)$ has density $0$.

```lean
theorem erdos_955.variants.pollack_pomerance_thompson_bound :
    ∀ (A : Set ℕ) (ε : ℕ → ℝ),
      Tendsto ε atTop (𝓝 0) →
      (∀ᶠ n : ℕ in atTop, (count (· ∈ A) n : ℝ) ≤ (n : ℝ) ^ ((1 / 2 : ℝ) + ε n)) →
      { x | s x ∈ A }.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/955.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean#L137).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/955.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/955.lean)
- [erdosproblems.com/955](https://www.erdosproblems.com/955)
