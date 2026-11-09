---
declaration: theorem
origin: cited
lean: Erdos420.erdos_420.parts.i, Erdos420.erdos_420.parts.ii, Erdos420.erdos_420.parts.iii, Erdos420.erdos_420.variants.log_frequently_lt_two, Erdos420.erdos_420.variants.rankin_frequently_lt_two, Erdos420.erdos_420.variants.pow_four_ninths
statement: formalized
---

# Erdős Problem 420

> *References:*
> - [erdosproblems.com/420](https://www.erdosproblems.com/420)
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathematique (1980).
> - [EGIP96] Erdős, P. and Graham, S. W. and Ivić, A. and Pomerance, C., *On the number of divisors
>   of $n!$*. Analytic number theory, Vol. 1 (Allerton Park, IL, 1995), Progr. Math. 138, Birkhäuser
>   Boston (1996), 337-355.
>
> In the solved variants, $K(n)$ is the least $K \geq 1$ with $\tau((n+K)!) \geq 2\tau(n!)$, so that
> $K(n) > h$ if and only if $F(h, n) < 2$. These variants state Corollaries 2 and 3 of [EGIP96] as
> printed; the stronger claims on erdosproblems.com are not stated.

*Quoted from [FormalConjectures/ErdosProblems/420.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/420](https://www.erdosproblems.com/420).

The file states 6 research or textbook statements: 3 open and 3 solved. It also has 3 test statements, counted here but not shown.

## `Erdos420.erdos_420.parts.i`

Open: stated without proof.

> If $\tau(n)$ counts the number of divisors of $n$ then let
>
> $$F(f,n)=\frac{\tau((n+\lfloor f(n)\rfloor)!)}{\tau(n!)}.$$
>
> Is it true that
>
> $$\lim_{n\to \infty}F((\log n)^C,n)=\infty$$
>
> for large $C$?
>
> "For large $C$" means for all sufficiently large real $C$. Since $(\log n)^C$ increases with $C$
> for $n \geq 3$ and $F(f,n)$ is nondecreasing in $f(n)$, this is equivalent to asking for one
> such $C$.

```lean
theorem erdos_420.parts.i :
    ∀ᶠ C : ℝ in atTop, Tendsto (F fun m ↦ Real.log m ^ C) atTop atTop
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L98).

## `Erdos420.erdos_420.parts.ii`

Open: stated without proof.

> Is it true that $F(\log n,n)$ is everywhere dense in $(1,\infty)$?
>
> This asks that every point of $(1,\infty)$ lies in the closure of the set of values
> $F(\log n, n)$. Note that $F(f,n) \geq 1$ always (`Erdos420.one_le_F`).

```lean
theorem erdos_420.parts.ii :
    Set.Ioi (1 : ℝ) ⊆ closure (Set.range (F fun m ↦ Real.log m))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L109).

## `Erdos420.erdos_420.parts.iii`

Open: stated without proof.

> More generally, if $f(n)\leq \log n$ is a monotonic function such that $f(n)\to \infty$ as
> $n\to \infty$, then is $F(f,n)$ everywhere dense?
>
> "Everywhere dense" means dense in $(1,\infty)$, as in `Erdos420.erdos_420.parts.ii`. Asking for
> $f(n) \leq \log n$ for all $n$, rather than for all large $n$, gives an equivalent question.

```lean
theorem erdos_420.parts.iii :
    ∀ f : ℕ → ℝ, Monotone f → (∀ n, f n ≤ Real.log n) → Tendsto f atTop atTop →
      Set.Ioi (1 : ℝ) ⊆ closure (Set.range (F f))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L121).

## `Erdos420.erdos_420.variants.log_frequently_lt_two`

Solved: stated here without proof.

> Erdős, Graham, Ivić and Pomerance proved [EGIP96, Corollary 2] that $K(n)/\log n$ is unbounded,
> with $K(n)$ as in the module docstring. Equivalently, for every $c > 0$ we have
> $F(c\log n, n) < 2$ for infinitely many $n$. In particular
> $\liminf F(c\log n, n) \leq 2$.

```lean
theorem erdos_420.variants.log_frequently_lt_two :
    ∀ c > (0 : ℝ), ∃ᶠ n : ℕ in atTop, F (fun m ↦ c * Real.log m) n < 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L133).

## `Erdos420.erdos_420.variants.rankin_frequently_lt_two`

Solved: stated here without proof.

> Erdős, Graham, Ivić and Pomerance proved [EGIP96, Corollary 2] that for infinitely many $n$,
>
> $$K(n) > \frac{\log n \cdot \log\log n \cdot \log\log\log\log n}{9(\log\log\log n)^3},$$
>
> with $K(n)$ as in the module docstring. Equivalently,
> $F(f,n) < 2$ for infinitely many $n$, where $f(n)$ is the right-hand side.

```lean
theorem erdos_420.variants.rankin_frequently_lt_two :
    ∃ᶠ n : ℕ in atTop, F (fun m ↦ Real.log m * Real.log (Real.log m) *
      Real.log (Real.log (Real.log (Real.log m))) /
        (9 * Real.log (Real.log (Real.log m)) ^ 3)) n < 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L144).

## `Erdos420.erdos_420.variants.pow_four_ninths`

Solved: stated here without proof.

> Erdős, Graham, Ivić and Pomerance proved [EGIP96, Corollary 3] that for all sufficiently large
> $n$ we have $K(n) < n^{4/9}$, with $K(n)$ as in the module docstring. Hence
> $F(n^{4/9}, n) \geq 2$ for all large $n$.

```lean
theorem erdos_420.variants.pow_four_ninths :
    ∀ᶠ n : ℕ in atTop, 2 ≤ F (fun m ↦ (m : ℝ) ^ (4 / 9 : ℝ)) n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/420.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean#L156).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/420.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/420.lean)
- [erdosproblems.com/420](https://www.erdosproblems.com/420)
