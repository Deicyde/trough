---
declaration: theorem
origin: cited
lean: Erdos651.nonempty_cardSet, Erdos651.erdos_651, Erdos651.erdos_651.variants.pohoata_zakharov, Erdos651.erdos_651.variants.subexponential, Erdos651.erdos_651.variants.planar, Erdos651.erdos_651.variants.antitone
statement: formalized
---

# Erdős Problem 651

> *References:*
> - [erdosproblems.com/651](https://www.erdosproblems.com/651)
> - [Er97e] Erdős, P., *Some of my favourite unsolved problems*. Math. Japon. (1997), 527-537.
> - [ErSz60] Erdős, P. and Szekeres, G., *On some extremum problems in elementary geometry*.
>   Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1960/61), 53-62.
> - [PoZa22] Pohoata, C. and Zakharov, D., *Convex polytopes from fewer points*.
>   [arXiv:2208.04878](https://arxiv.org/abs/2208.04878) (2022).
> - [Va96] Valtr, P., *Several results related to the Erdős-Szekeres theorem*. Doctoral
>   dissertation, Charles University, Prague (1996).

*Quoted from [FormalConjectures/ErdosProblems/651.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/651](https://www.erdosproblems.com/651).

The file states 6 research or textbook statements: 6 solved. It also has 2 API statements, counted here but not shown.

## `Erdos651.nonempty_cardSet`

Solved: stated here without proof.

> For $k \geq 2$ and every $n$ there is an integer $N$ such that any $N$ points in general
> position in $\mathbb{R}^k$ contain $n$ points in convex position. So $f_k(n)$ is well defined.
>
> This is the higher-dimensional Erdős-Szekeres theorem. For $n \leq k + 1$ one can take $N = n$.
> For larger $n$ it follows from Ramsey's theorem, which gives $f_k(n) \leq R_{k+2}(k+3, n)$, see
> [PoZa22, Section 1].

```lean
theorem nonempty_cardSet {k : ℕ} (hk : 2 ≤ k) (n : ℕ) : (cardSet k n).Nonempty
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L103).

## `Erdos651.erdos_651`

Solved: stated here without proof.

> Let $f_k(n)$ denote the smallest integer such that any $f_k(n)$ points in general position in
> $\mathbb{R}^k$ contain $n$ which determine a convex polyhedron. Is it true that
>
> $$
>   f_k(n) > (1+c_k)^n
> $$
>
> for some constant $c_k>0$?
>
> A problem of Erdős [Er97e]. We read "determine a convex polyhedron" as "are in convex position",
> and the inequality as holding, with some $c_k > 0$, for all sufficiently large $n$. We ask the
> question for every dimension $k \geq 3$. The planar case $k = 2$ is the Erdős-Klein-Szekeres
> problem (see `erdos_651.variants.planar`).
>
> The answer is no. Pohoata and Zakharov [PoZa22, Theorem 1.1] proved that $f_3(n) \leq 2^{o(n)}$,
> and this implies $f_k(n) \leq 2^{o(n)}$ for every $k \geq 3$, see
> `erdos_651.variants.pohoata_zakharov`.

```lean
theorem erdos_651 :
    ¬ ∀ k : ℕ, 3 ≤ k → ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (1 + c) ^ n < (f k n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 124](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L124).

## `Erdos651.erdos_651.variants.pohoata_zakharov`

Solved: stated here without proof.

> Pohoata and Zakharov [PoZa22, Theorem 1.1] proved that $ES_3(n) = 2^{o(n)}$, where $ES_k(n)$ is
> the function $f_k(n)$ above: for every $\varepsilon > 0$ and all large $n$, any set of at least
> $2^{\varepsilon n}$ points in general position in $\mathbb{R}^3$ contains $n$ points in convex
> position. By the projection argument of Valtr [Va96] (see `erdos_651.variants.antitone`) the same
> holds in every dimension $k \geq 3$ [PoZa22, abstract and Section 1].
>
> The theorem gives $f_k(n) \leq \lceil 2^{\varepsilon n} \rceil$. The form below follows by
> applying it with $\varepsilon / 2$.

```lean
theorem erdos_651.variants.pohoata_zakharov {k : ℕ} (hk : 3 ≤ k) :
    ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (f k n : ℝ) ≤ (2 : ℝ) ^ (ε * (n : ℝ))
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 139](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L139).

## `Erdos651.erdos_651.variants.subexponential`

Solved: stated here without proof.

> For every dimension $k \geq 3$ and every $c > 0$ one has $f_k(n) \leq (1+c)^n$ for all large
> $n$. This is `erdos_651.variants.pohoata_zakharov` with $\varepsilon = \log_2(1 + c)$. In
> particular, for every $c > 0$ the lower bound $f_k(n) > (1+c)^n$ fails not only for infinitely
> many $n$ but for all large $n$.

```lean
theorem erdos_651.variants.subexponential {k : ℕ} (hk : 3 ≤ k) :
    ∀ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (f k n : ℝ) ≤ (1 + c) ^ n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L150).

## `Erdos651.erdos_651.variants.planar`

Solved: stated here without proof.

> For $k = 2$ the lower bound of the question holds: $f_2(n) > (1+c)^n$ for some $c > 0$ and all
> large $n$. Erdős and Szekeres [ErSz60] proved that
> $2^{n-2} + 1 \leq f_2(n)$, see [PoZa22, abstract and Section 1], and $(3/2)^n < 2^{n-2} + 1$ for
> all $n \geq 5$. The Erdős-Klein-Szekeres conjecture (Erdős Problem 107) states that
> $f_2(n) = 2^{n-2} + 1$ for $n \geq 3$.

```lean
theorem erdos_651.variants.planar :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (1 + c) ^ n < (f 2 n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L162).

## `Erdos651.erdos_651.variants.antitone`

Solved: stated here without proof.

> The function $f_k(n)$ does not increase with the dimension: $f_{k+1}(n) \leq f_k(n)$ for
> $k \geq 2$. Given a set in general position in $\mathbb{R}^{k+1}$ with at least $f_k(n)$ points,
> project it to a generic hyperplane, find $n$ points in convex position in the projection, and
> lift them back. This projection argument is due to Valtr [Va96]; see [PoZa22, Section 1, (1)].
>
> The site states that $f_2(n) > f_3(n) > \cdots$. [PoZa22] gives only the non-strict inequality, so
> we state that. The strict inequalities fail for small $n$: for example $f_2(3) = f_3(3) = 3$.

```lean
theorem erdos_651.variants.antitone {k : ℕ} (hk : 2 ≤ k) (n : ℕ) : f (k + 1) n ≤ f k n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/651.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean#L176).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/651.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/651.lean)
- [erdosproblems.com/651](https://www.erdosproblems.com/651)
