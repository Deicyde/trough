---
declaration: theorem
origin: cited
lean: Erdos367.erdos_367.parts.i, Erdos367.erdos_367.parts.ii, Erdos367.erdos_367.variants.k_le_two, Erdos367.erdos_367.variants.k_ge_three_lower, Erdos367.erdos_367.variants.higher_full_parts
statement: formalized
---

# Erdős Problem 367

> *References:*
> - [erdosproblems.com/367](https://www.erdosproblems.com/367)
> - [ErGr80] P. Erdős and R. L. Graham, *Old and New Problems and Results in Combinatorial Number Theory*, L'Enseignement Mathématique (1980).

*Quoted from [FormalConjectures/ErdosProblems/367.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/367](https://www.erdosproblems.com/367).

The file states 5 research or textbook statements: 1 open and 4 solved.

## `Erdos367.erdos_367.parts.i`

Open: stated without proof.

> Let $B_2(n)$ be the $2$-full part of $n$ (that is, $B_2(n)=n/n'$ where $n'$ is the product of all
> primes that divide $n$ exactly once). Is it true that, for every fixed $k \geq 1$,
> $\prod_{n \leq m < n+k} B_2(m) \ll n^{2+o(1)}$?

```lean
theorem erdos_367.parts.i : ∀ k : ℕ, 1 ≤ k →
    ∃ e : ℕ → ℝ,
      e =o[atTop] (1 : ℕ → ℝ) ∧
      ∀ᶠ n in atTop,
        ((∏ m ∈ .Ico n (n + k), B 2 m : ℕ) : ℝ) ≤ (n : ℝ) ^ (2 + e n)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/367.lean, line 46](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean#L46).

## `Erdos367.erdos_367.parts.ii`

Solved: stated here without proof.

> Or perhaps even $\prod_{n \leq m < n+k} B_2(m) \ll_k n^2$?
>
> van Doorn notes in the comments that this fails for all $k \geq 3$.

```lean
theorem erdos_367.parts.ii : ¬ ∀ k : ℕ, 1 ≤ k →
    (fun n ↦ ((∏ m ∈ .Ico n (n + k), B 2 m : ℕ) : ℝ)) =O[atTop]
      fun n ↦ (n : ℝ) ^ (2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/367.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean#L59).

## `Erdos367.erdos_367.variants.k_le_two`

Solved: stated here without proof.

> van Doorn notes in the comments that for $k \leq 2$ we trivially have
> $\prod_{n \leq m < n+k} B_2(m) \ll n^2$.

```lean
theorem erdos_367.variants.k_le_two : ∀ k : ℕ, k ≤ 2 →
    (fun n ↦ ((∏ m ∈ .Ico n (n + k), B 2 m : ℕ) : ℝ)) =O[atTop]
      fun n ↦ (n : ℝ) ^ (2 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/367.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean#L69).

## `Erdos367.erdos_367.variants.k_ge_three_lower`

Solved: stated here without proof.

> But this fails for all $k \geq 3$, and in fact
> $\prod_{n \leq m < n+3} B_2(m) \gg n^2 \log n$ infinitely often.

```lean
theorem erdos_367.variants.k_ge_three_lower :
    ∃ c > (0 : ℝ), ∃ᶠ (n : ℕ) in atTop,
      c * ((n : ℝ) ^ 2 * Real.log (n : ℝ)) ≤
        ((∏ m ∈ .Ico n (n + 3), B 2 m : ℕ) : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/367.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean#L79).

## `Erdos367.erdos_367.variants.higher_full_parts`

Solved: stated here; a Lean proof is at [https://github.com/kusasyu36/erdos367-higher-full-parts/blob/9c995fbb1ec62bd675ac9bc162f9e2337d6db4f9/Erdos367HigherFullParts.lean#L57](https://github.com/kusasyu36/erdos367-higher-full-parts/blob/9c995fbb1ec62bd675ac9bc162f9e2337d6db4f9/Erdos367HigherFullParts.lean#L57).

> It would also be interesting to find upper and lower bounds for the analogous product with $B_r$
> for $r \geq 3$, where $B_r(n)$ is the $r$-full part of $n$ (that is, the product of prime powers
> $p^a \mid n$ such that $p^{a+1} \nmid n$ and $a \geq r$). Is it true that, for every fixed
> $r \geq 3$ and $k \geq 2$, there is some $\epsilon = \epsilon(r, k) > 0$ with
> $\limsup \frac{\prod_{n \leq m < n+k} B_r(m)}{n^{1+\epsilon}} = \infty$?
>
> The webpage writes "for every fixed $r,k \geq 2$ and $\epsilon > 0$", but van Doorn observes in
> the [comments](https://www.erdosproblems.com/forum/thread/367#post-1766) that the intended
> reading lets $\epsilon$ depend on $r$ and $k$. Since $B_r(m) \mid m$, the product is at most
> $\prod_{n \leq m < n+k} m$, so the reading with $\epsilon$ universally quantified is false.
>
> The answer is yes: $\epsilon = 1/(2r)$ works. For $j \geq r$ let $x = 2^j + 1$ and $n = x^r - 1$;
> then $B_r(n+1) = x^r$ and $2^j \mid n$ gives $B_r(n) \geq 2^j$, so the product over $[n, n+k)$ is at
> least $2^j x^r \geq (\sqrt{x}/2)\, n^{1 + 1/(2r)}$, which is unbounded. A stronger exponent
> (any $\epsilon < (r+1)/r^2$) is claimed in the [forum](https://www.erdosproblems.com/forum/thread/367)
> but is not formalised.

```lean
theorem erdos_367.variants.higher_full_parts :
    ∀ r k : ℕ, 3 ≤ r → 2 ≤ k → ∃ ε : ℝ, 0 < ε ∧
      atTop.limsup (fun n ↦
        ((∏ m ∈ .Ico n (n + k), B r m : ℕ) / (n : ℝ) ^ (1 + ε) |>.toEReal)) = ⊤
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/367.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/367.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/367.lean)
- [erdosproblems.com/367](https://www.erdosproblems.com/367)
