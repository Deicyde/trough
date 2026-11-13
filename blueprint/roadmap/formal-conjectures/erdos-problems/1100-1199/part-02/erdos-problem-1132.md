---
declaration: theorem
origin: cited
lean: Erdos1132.erdos_1132.parts.i, Erdos1132.erdos_1132.parts.ii, Erdos1132.erdos_1132.variants.erdos_max, Erdos1132.erdos_1132.variants.tao
statement: formalized
---

# Erdős Problem 1132

> *References:*
> - [erdosproblems.com/1132](https://www.erdosproblems.com/1132)
> - [Be31] Bernstein, S., *Sur la limitation des valeurs d'un polynome $P_n(x)$ de degré $n$ sur
>   tout un segment par ses valeurs en $(n+1)$ points du segment*. Izv. Akad. Nauk SSSR (1931),
>   1025-1050.
> - [Er61c] Erdős, P., *Problems and results on the theory of interpolation. II*. Acta Math. Acad.
>   Sci. Hungar. 12 (1961), 235-244. [PDF](https://www.renyi.hu/~p_erdos/1961-20.pdf)
> - [Er67] Erdős, P., *Problems and results on the convergence and divergence properties of the
>   Lagrange interpolation polynomials and some extremal problems*. Mathematica (Cluj) 10 (1968),
>   65-73. [PDF](https://www.renyi.hu/~p_erdos/1967-20.pdf)
> - [Ta26b] Tao, T., *Local Bernstein theory, and lower bounds for Lebesgue constants*.
>   [arXiv:2603.21453](https://arxiv.org/abs/2603.21453) (2026).
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1132.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1132](https://www.erdosproblems.com/1132).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1132.erdos_1132.parts.i`

Open: stated without proof.

> For $x_1,\ldots,x_n\in [-1,1]$ let
>
> $$l_k(x)=\frac{\prod_{i\neq k}(x-x_i)}{\prod_{i\neq k}(x_k-x_i)},$$
>
> which are such that $l_k(x_k)=1$ and $l_k(x_i)=0$ for $i\neq k$.
>
> Let $x_1,x_2,\ldots\in [-1,1]$ be an infinite sequence, and let
>
> $$L_n(x) = \sum_{1\leq k\leq n}\lvert l_k(x)\rvert,$$
>
> where each $l_k(x)$ is defined above with respect to $x_1,\ldots,x_n$.
>
> Must there exist $x\in (-1,1)$ such that
>
> $$L_n(x) >\frac{2}{\pi}\log n-O(1)$$
>
> for infinitely many $n$?
>
> This is the first part, asked in [Er67, p. 68] (see also [Va99, 2.43]); [Er61c, (4)] states it as
> "quite possibly true". Both papers consider an arbitrary triangular array of nodes; as on the
> problem page, we take the first $n$ terms of one sequence, a special case. The nodes are required
> to be distinct, so that $l_k$ is defined. We let the constant $C$ in $O(1)$ depend on the sequence
> and on $x$, the weakest reading. In [Er61c, (4)] it is an absolute constant.

```lean
theorem erdos_1132.parts.i :
    ∀ x : ℕ → ℝ, (∀ k, x k ∈ Set.Icc (-1 : ℝ) 1) → Function.Injective x →
      ∃ t ∈ Set.Ioo (-1 : ℝ) 1, ∃ C : ℝ, ∃ᶠ n : ℕ in atTop,
        2 / Real.pi * Real.log n - C < lebesgueFunction n x t
```

Category `research open`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1132.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean#L88).

## `Erdos1132.erdos_1132.parts.ii`

Open: stated without proof.

> For $x_1,\ldots,x_n\in [-1,1]$ let
>
> $$l_k(x)=\frac{\prod_{i\neq k}(x-x_i)}{\prod_{i\neq k}(x_k-x_i)},$$
>
> which are such that $l_k(x_k)=1$ and $l_k(x_i)=0$ for $i\neq k$.
>
> Let $x_1,x_2,\ldots\in [-1,1]$ be an infinite sequence, and let
>
> $$L_n(x) = \sum_{1\leq k\leq n}\lvert l_k(x)\rvert,$$
>
> where each $l_k(x)$ is defined above with respect to $x_1,\ldots,x_n$.
>
> Is it true that
>
> $$\limsup_{n\to \infty}\frac{L_n(x)}{\log n}\geq \frac{2}{\pi}$$
>
> for almost all $x\in (-1,1)$?
>
> This is the second part, asked in [Er67, p. 68] ("Perhaps (7) holds for almost all $x_0$"), again
> for triangular arrays. The nodes are required to be distinct. We write the $\limsup$ condition as:
> for every $\varepsilon>0$, there are infinitely many $n$ with
>
> $$L_n(x)\geq\left(\frac{2}{\pi}-\varepsilon\right)\log n.$$
>
> This is equivalent, and avoids the junk value of a real `limsup` of an unbounded sequence.
>
> The problem page says that a result of Bernstein [Be31] implies that the set of such $x$ is
> everywhere dense. In [Er67, p. 68] Erdős derives this from his own unpublished bound (6), which
> sharpens a result of Bernstein. It also follows from `erdos_1132.variants.tao` with
> $\omega(n)=\log\log n$.

```lean
theorem erdos_1132.parts.ii :
    ∀ x : ℕ → ℝ, (∀ k, x k ∈ Set.Icc (-1 : ℝ) 1) → Function.Injective x →
      ∀ᵐ t ∂(volume.restrict (Set.Ioo (-1 : ℝ) 1)),
        ∀ ε > (0 : ℝ), ∃ᶠ n : ℕ in atTop,
          (2 / Real.pi - ε) * Real.log n ≤ lebesgueFunction n x t
```

Category `research open`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1132.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean#L119).

## `Erdos1132.erdos_1132.variants.erdos_max`

Solved: stated here without proof.

> Erdős [Er61c, Theorem 1] proved that, for any fixed $x_1,\ldots,x_n\in [-1,1]$,
>
> $$\max_{x\in [-1,1]}\sum_{1\leq k\leq n}\lvert l_k(x)\rvert>\frac{2}{\pi}\log n-O(1).$$
>
> Here $O(1)$ is an absolute constant $C$, and the maximum exceeds a bound if and only if some point
> does, so we write the statement with `∃ t`. The nodes are required to be distinct.

```lean
theorem erdos_1132.variants.erdos_max :
    ∃ C : ℝ, ∀ n : ℕ, 1 ≤ n → ∀ x : ℕ → ℝ, (∀ k < n, x k ∈ Set.Icc (-1 : ℝ) 1) →
      Set.InjOn x (Set.Iio n) →
        ∃ t ∈ Set.Icc (-1 : ℝ) 1, 2 / Real.pi * Real.log n - C < lebesgueFunction n x t
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1132.lean, line 133](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean#L133).

## `Erdos1132.erdos_1132.variants.tao`

Solved: stated here without proof.

> Tao [Ta26b, Corollary 1.11] has proved that for any function $\omega(n)$ which tends to infinity
> with $n$ there exists a dense set of $x\in (-1,1)$ such that
>
> $$L_n(x)\geq \frac{2}{\pi}\log n-\omega(n)$$
>
> for infinitely many $n$.
>
> Tao proves this for an arbitrary triangular array of distinct nodes in $[-1,1]$, so in particular
> for the first $n$ terms of a sequence. We state the array version: `x n k` is the $k$-th node
> (counted from $0$) of the $n$-th row, and the set is dense in $(-1,1)$ if every point of
> $(-1,1)$ is in its closure.

```lean
theorem erdos_1132.variants.tao :
    ∀ x : ℕ → ℕ → ℝ, (∀ n, ∀ k < n, x n k ∈ Set.Icc (-1 : ℝ) 1) →
      (∀ n, Set.InjOn (x n) (Set.Iio n)) →
      ∀ ω : ℕ → ℝ, Tendsto ω atTop atTop →
        Set.Ioo (-1 : ℝ) 1 ⊆ closure {t ∈ Set.Ioo (-1 : ℝ) 1 |
          ∃ᶠ n : ℕ in atTop, 2 / Real.pi * Real.log n - ω n ≤ lebesgueFunction n (x n) t}
```

Category `research solved`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1132.lean, line 151](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean#L151).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1132.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1132.lean)
- [erdosproblems.com/1132](https://www.erdosproblems.com/1132)
