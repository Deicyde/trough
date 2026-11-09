---
declaration: theorem
origin: cited
lean: Green97.green_97, Green97.green_97.variants.simkin, Green97.green_97.variants.alpha, Green97.green_97.variants.bowtell_keevash, Green97.green_97.variants.toroidal, Green97.green_97.variants.eberhard_manners_mrazovic
statement: formalized
---

# Ben Green's Open Problem 97

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.97)
> - [Si23] Simkin, M., *The number of $n$-queens configurations*. Adv. Math. 427 (2023),
>   Paper No. 109127. [arXiv:2107.13460](https://arxiv.org/abs/2107.13460)
> - [BoKe21] Bowtell, C. and Keevash, P., *The $n$-queens problem*.
>   [arXiv:2109.08083](https://arxiv.org/abs/2109.08083) (2021).
> - [NAB23] Nobel, P., Agrawal, A. and Boyd, S., *Computing tighter bounds on the $n$-queens
>   constant via Newton's method*. Optim. Lett. 17 (2023), 1229--1240.
>   [arXiv:2112.03336](https://arxiv.org/abs/2112.03336)
> - [EMM19] Eberhard, S., Manners, F. and Mrazović, R., *Additive triples of bijections, or the
>   toroidal semiqueens problem*. J. Eur. Math. Soc. 21 (2019), 441--463.
>   [arXiv:1510.05987](https://arxiv.org/abs/1510.05987)

*Quoted from [FormalConjectures/GreensOpenProblems/97.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 3 open and 3 solved. It also has 3 test statements, counted here but not shown.

## `Green97.green_97`

Open: stated without proof.

> In how many ways (asymptotically) $Q(n)$ may $n$ non-attacking queens be placed on an
> $n \times n$ chessboard?
>
> This is the $n$-queens problem, see [Gr24, Problem 97]. We read "asymptotically" as: find an
> explicit function `green_97.answer` with $Q(n) \sim$ `green_97.answer n`. The function
> $n \mapsto Q(n)$ itself is not an explicit answer. [Gr24] notes that an asymptotic "rather than
> an asymptotic for the log" is open. What is known is $Q(n) = ((1+o(1))\, n e^{-\alpha})^n$ for a
> constant $1.94 < \alpha < 1.9449$ [Si23], see `green_97.variants.simkin`.

```lean
theorem green_97 :
    (fun n : ℕ ↦ (numQueens n : ℝ)) ~[atTop] green_97.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L122).

## `Green97.green_97.variants.simkin`

Solved: stated here without proof.

> **Simkin's theorem.** There is a constant $1.94 < \alpha < 1.9449$ such that
>
> $$\lim_{n \to \infty} \frac{Q(n)^{1/n}}{n} = e^{-\alpha},$$
>
> that is, $Q(n) = ((1+o(1))\, n e^{-\alpha})^n$ [Si23, Theorem 1.1]. The constant $\alpha$ is
> defined in [Si23] as the solution of a convex optimisation problem over Borel probability measures
> on the square $[-1/2, 1/2]^2$. The limit determines $\alpha$ uniquely. Nobel, Agrawal and Boyd
> [NAB23] combined Simkin's formulation with a sharper bound of Knuth, solved the resulting convex
> problems numerically, and report the tighter range
> $\alpha \in [1.944000752, 1.944001082]$.

```lean
theorem green_97.variants.simkin :
    ∃ α : ℝ, 1.94 < α ∧ α < 1.9449 ∧
      Tendsto (fun n : ℕ ↦ (numQueens n : ℝ) ^ ((1 : ℝ) / n) / n) atTop
        (𝓝 (Real.exp (-α)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L137).

## `Green97.green_97.variants.alpha`

Open: stated without proof.

> Find an explicit value for the constant $\alpha$ of `green_97.variants.simkin`, that is, the
> number with $Q(n)^{1/n}/n \to e^{-\alpha}$.
>
> [Gr24] writes that "an explicit solution remains an open problem". The value $\alpha$ is the
> solution of an entropy optimisation problem [Si23]. As for `green_97`, an explicit closed form is
> intended.

```lean
theorem green_97.variants.alpha :
    Tendsto (fun n : ℕ ↦ (numQueens n : ℝ) ^ ((1 : ℝ) / n) / n) atTop
      (𝓝 (Real.exp (-green_97.variants.alpha.answer)))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 154](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L154).

## `Green97.green_97.variants.bowtell_keevash`

Solved: stated here without proof.

> **Bowtell and Keevash.** For $n \equiv 1, 5 \pmod 6$ the number of toroidal $n$-queens
> configurations satisfies $T(n) = ((1+o(1))\, n e^{-3})^n$ [BoKe21, Theorem 1.2]. The filter
> `toroidalDegrees` restricts to these $n$, because $T(n) = 0$ for all other $n \ge 1$.

```lean
theorem green_97.variants.bowtell_keevash :
    Tendsto (fun n : ℕ ↦ (numToroidalQueens n : ℝ) ^ ((1 : ℝ) / n) / n) toroidalDegrees
      (𝓝 (Real.exp (-3)))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L165).

## `Green97.green_97.variants.toroidal`

Open: stated without proof.

> Find an asymptotic for the number $T(n)$ of toroidal $n$-queens configurations, for
> $n \equiv 1, 5 \pmod 6$.
>
> [Gr24] writes, after the result of [BoKe21], that the problem of "obtaining an asymptotic (rather
> than an asymptotic for the log) remains open". [BoKe21] proved the asymptotic of the logarithm, see
> `green_97.variants.bowtell_keevash`. We read "asymptotic" as for `green_97`: an explicit function
> is intended.

```lean
theorem green_97.variants.toroidal :
    (fun n : ℕ ↦ (numToroidalQueens n : ℝ)) ~[toroidalDegrees]
      green_97.variants.toroidal.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 182](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L182).

## `Green97.green_97.variants.eberhard_manners_mrazovic`

Solved: stated here without proof.

> **Eberhard, Manners and Mrazović.** For odd $n$, the number $s_n$ of pairs $(\pi_1, \pi_2)$ of
> bijections $\{1, \dots, n\} \to \mathbb{Z}/n\mathbb{Z}$ with $\pi_1 + \pi_2$ also a bijection is
>
> $$s_n = (e^{-1/2} + o(1))\, \frac{(n!)^3}{n^{n-1}}$$
>
> [EMM19, Theorem 1.2]. [Gr24] refers to this paper for the variant of the toroidal question where
> only $\pi_1$, $\pi_2$ and $\pi_1 - \pi_2$ are required to be bijections. Replacing $\pi_2$ by
> $-\pi_2$ shows that this variant has the same count $s_n$. For even $n$, $s_n = 0$
> [EMM19, Section 1], so the theorem is stated for odd $n$.

```lean
theorem green_97.variants.eberhard_manners_mrazovic :
    (fun n : ℕ ↦ (numAdditiveTriples n : ℝ)) ~[atTop ⊓ Filter.principal {n : ℕ | Odd n}]
      fun n : ℕ ↦ Real.exp (-(1 / 2)) * ((n ! : ℕ) : ℝ) ^ 3 / (n : ℝ) ^ (n - 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/GreensOpenProblems/97.lean, line 208](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean#L208).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/97.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/97.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.97)
