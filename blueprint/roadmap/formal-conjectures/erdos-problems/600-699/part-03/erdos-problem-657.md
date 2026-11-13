---
declaration: theorem
origin: cited
lean: Erdos657.erdos_657, Erdos657.erdos_657.variants.higher_dim, Erdos657.erdos_657.variants.dim_one, Erdos657.erdos_657.variants.dim_one_lower, Erdos657.erdos_657.variants.dim_one_upper, Erdos657.erdos_657.variants.straus
statement: formalized
---

# Erdős Problem 657

> *References:*
> - [erdosproblems.com/657](https://www.erdosproblems.com/657)
> - [Er73] Erdős, P., *Problems and results on combinatorial number theory*. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [Er75f] Erdős, Paul, *On some problems of elementary and combinatorial geometry*. Ann. Mat.
>   Pura Appl. (4) (1975), 99-108.
> - [ErPa90] Erdős, P. and Pach, J., *Variations on the theme of repeated distances*.
>   Combinatorica (1990), 261-269.
> - [Er97e] Erdős, Paul, *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [Du08] Dumitrescu, Adrian, *On distinct distances and λ-free point sets*. Discrete Math.
>   (2008), 6533-6538.

*Quoted from [FormalConjectures/ErdosProblems/657.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/657](https://www.erdosproblems.com/657).

The file states 6 research or textbook statements: 2 open and 4 solved.

## `Erdos657.erdos_657`

Open: stated without proof.

> Is it true that if $A\subset \mathbb{R}^2$ is a set of $n$ points such that every subset of $3$
> points determines $3$ distinct distances (that is, $A$ has no isosceles triangles, degenerate
> ones included) then $A$ determines at least $f(n)n$ distinct distances, for some function $f$
> with $f(n)\to \infty$?

```lean
theorem erdos_657 :
    ∃ f : ℕ → ℝ, Tendsto f atTop atTop ∧
      ∀ n : ℕ, ∀ A : Finset ℝ², A.card = n → (A : Set ℝ²).IsIsoscelesFree →
        f n * (n : ℝ) ≤ (distinctDistances A : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L51).

## `Erdos657.erdos_657.variants.higher_dim`

Open: stated without proof.

> In [Er73] Erdős attributes the problem, more generally in $\mathbb{R}^k$, to himself and Davies:
> for every fixed $k \geq 1$, is there a function $f$ with $f(n)\to \infty$ such that every set of
> $n$ points in $\mathbb{R}^k$ with no isosceles triangles determines at least $f(n)n$ distinct
> distances?
>
> Here the dimension $k$ is fixed and $f$ may depend on $k$.

```lean
theorem erdos_657.variants.higher_dim :
    ∀ k : ℕ, 1 ≤ k → ∃ f : ℕ → ℝ, Tendsto f atTop atTop ∧
      ∀ n : ℕ, ∀ A : Finset (ℝ^k), A.card = n → (A : Set (ℝ^k)).IsIsoscelesFree →
        f n * (n : ℝ) ≤ (distinctDistances A : ℝ)
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L66).

## `Erdos657.erdos_657.variants.dim_one`

Solved: stated here without proof.

> The question on the real line, which Erdős [Er73] said was open, has a positive answer: there is
> a function $f$ with $f(n)\to \infty$ such that every set of $n$ real numbers with no three-term
> arithmetic progression determines at least $f(n)n$ distinct distances. This follows from the
> lower bound of Dumitrescu [Du08].
>
> On the line, a set has no isosceles triangle exactly when it has no three-term arithmetic
> progression.

```lean
theorem erdos_657.variants.dim_one :
    ∃ f : ℕ → ℝ, Tendsto f atTop atTop ∧
      ∀ n : ℕ, ∀ A : Finset ℝ, A.card = n → (A : Set ℝ).IsIsoscelesFree →
        f n * (n : ℝ) ≤ (distinctDistances A : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L82).

## `Erdos657.erdos_657.variants.dim_one_lower`

Solved: stated here without proof.

> Dumitrescu [Du08] proved that there is a constant $c > 0$ such that, for all large $n$, every set
> of $n$ real numbers with no three-term arithmetic progression determines at least
> $n(\log n)^c$ distinct distances.

```lean
theorem erdos_657.variants.dim_one_lower :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∀ A : Finset ℝ, A.card = n → (A : Set ℝ).IsIsoscelesFree →
        (n : ℝ) * (Real.log n) ^ c ≤ (distinctDistances A : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 94](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L94).

## `Erdos657.erdos_657.variants.dim_one_upper`

Solved: stated here without proof.

> As noted in [Du08], Behrend's construction of large sets without three-term arithmetic
> progressions shows that there is a constant $C > 0$ such that, for all large $n$, some set
> of $n$ real numbers with no three-term arithmetic progression determines at most
> $n 2^{C\sqrt{\log n}}$ distinct distances.

```lean
theorem erdos_657.variants.dim_one_upper :
    ∃ C > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      ∃ A : Finset ℝ, A.card = n ∧ (A : Set ℝ).IsIsoscelesFree ∧
        (distinctDistances A : ℝ) ≤ (n : ℝ) * (2 : ℝ) ^ (C * √(Real.log n))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L107).

## `Erdos657.erdos_657.variants.straus`

Solved: stated here; a Lean proof is at [https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000007](https://palomar-registry.org/entry.html?id=PALOMAR-2026-11-02-000007).

> Straus observed that for every $k$ there is a set of $2^k$ points in $\mathbb{R}^k$ with no
> isosceles triangles which determines at most $2^k - 1$ distinct distances.

```lean
theorem erdos_657.variants.straus (k : ℕ) :
    ∃ A : Finset (ℝ^k), A.card = 2 ^ k ∧ (A : Set (ℝ^k)).IsIsoscelesFree ∧
      distinctDistances A ≤ 2 ^ k - 1
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/657.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/657.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/657.lean)
- [erdosproblems.com/657](https://www.erdosproblems.com/657)
