---
declaration: theorem
origin: cited
lean: Green84.green_84, Green84.green_84.variants.bbmst, Green84.green_84.variants.littlewood, Green84.green_84.variants.golay, Green84.green_84.variants.ultraflat_mod
statement: formalized
---

# Ben Green's Open Problem 84

> Erdős's two-sided version of this question, $\sqrt{N} \ll |P(z)| \ll \sqrt{N}$ on the unit
> circle, is `Erdos228.erdos_228` in `FormalConjectures.ErdosProblems.«228»`.
>
> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.84)
> - [BBMST20] Balister, P., Bollobás, B., Morris, R., Sahasrabudhe, J. and Tiba, M., *Flat
>   Littlewood polynomials exist*. Ann. of Math. (2) 192 (2020), 977--1004.
>   [arXiv:1907.09464](https://arxiv.org/abs/1907.09464)
> - [JKS13] Jedwab, J., Katz, D. J. and Schmidt, K.-U., *Advances in the merit factor problem for
>   binary sequences*. J. Combin. Theory Ser. A 120 (2013), 882--906.
>   [arXiv:1205.0626](https://arxiv.org/abs/1205.0626)
> - [OAI26a] OpenAI, *Asymptotically minimal maxima of real Littlewood polynomials*. OpenAI Math
>   Release preprint (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Asymptotically-minimal-maxima-of-real-Littlewood-polynomials-September-23-2026/paper.pdf

*Quoted from [FormalConjectures/GreensOpenProblems/84.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Green84.green_84`

Solved: stated here without proof.

> Is there a function $f : \{1, \dots, N\} \to \{-1, 1\}$ with $|\hat{f}(\theta)| \geq c\sqrt{N}$
> for all $\theta$?
>
> We read this as: is there an absolute constant $c > 0$ such that such an $f$ exists for all
> sufficiently large $N$? It cannot hold for all $N$: for $N = 2$,
> $\hat f(\theta) = e(\theta)(f(1) + f(2)e(\theta))$ vanishes for some $\theta$. The answer is yes
> [BBMST20], see `green_84.variants.bbmst`.

```lean
theorem green_84 :
    ∃ c : ℝ, 0 < c ∧ ∀ᶠ N in atTop, ∃ f : ℕ → ℤ, IsSignOn N f ∧
      ∀ θ : ℝ, c * √N ≤ ‖fourierSum N f θ‖
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/84.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean#L80).

## `Green84.green_84.variants.bbmst`

Solved: stated here without proof.

> **Flat Littlewood polynomials exist.** There are constants $\Delta > \delta > 0$ such that, for
> all $n \ge 2$, there is a polynomial $P(z) = \sum_{k=0}^{n} \varepsilon_k z^k$ with
> $\varepsilon_k \in \{-1, 1\}$ such that $\delta\sqrt{n} \le |P(z)| \le \Delta\sqrt{n}$ for all
> $z \in \mathbb{C}$ with $|z| = 1$ [BBMST20, Theorem 1.1].
>
> With $N = n + 1$ and $f(m) = \varepsilon_{m-1}$, one has $|\hat f(\theta)| = |P(e(\theta))|$, so
> this answers `green_84` for all $N \ge 3$.

```lean
theorem green_84.variants.bbmst :
    ∃ δ Δ : ℝ, 0 < δ ∧ δ < Δ ∧ ∀ n : ℕ, 2 ≤ n → ∃ ε : Fin (n + 1) → ℤ,
      (∀ k, ε k = 1 ∨ ε k = -1) ∧
        ∀ z : ℂ, ‖z‖ = 1 → δ * √n ≤ ‖signPoly ε z‖ ∧ ‖signPoly ε z‖ ≤ Δ * √n
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/84.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean#L95).

## `Green84.green_84.variants.littlewood`

Open: stated without proof.

> Littlewood's problem asks "whether there is in fact such a polynomial with
> $|P(z)| = (1 + o(1))\sqrt{N}$ always"; [Gr24] adds that "the answer to this may well be no".
>
> We read it as for `green_84`: for every $\varepsilon > 0$ and all sufficiently large $N$ there is
> $f : [N] \to \{-1, 1\}$ with $\bigl||\hat f(\theta)| - \sqrt{N}\bigr| \le \varepsilon\sqrt{N}$ for
> all $\theta$. With unimodular complex coefficients in place of $\pm 1$ such polynomials exist,
> by Kahane's theorem `Erdos230.erdos_230.variants.ultraflat`. For $\pm 1$ coefficients the upper
> half holds: for every $\eta > 0$ and all large $N$ some choice gives $\max_\theta |\hat f(\theta)|
> \le (1 + \eta)\sqrt{N}$ [OAI26a, Theorem 1.1] (which answers `Erdos1150.erdos_1150`), but that
> theorem gives no lower bound for $|\hat f|$.

```lean
theorem green_84.variants.littlewood :
    ∀ ε : ℝ, 0 < ε → ∀ᶠ N in atTop, ∃ f : ℕ → ℤ, IsSignOn N f ∧
      ∀ θ : ℝ, |‖fourierSum N f θ‖ - √N| ≤ ε * √N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/84.lean, line 114](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean#L114).

## `Green84.green_84.variants.golay`

Solved: stated here without proof.

> The merit factor problem of Golay: "it is conjectured ... that
> $\int_0^1 |P(z)|^4 \, dz \geq (1 + c)N^2$ for some universal $c > 0$" [Gr24], for every
> polynomial $P(z) = \sum_{i=0}^{N-1} \varepsilon_i z^i$ with $\pm 1$ coefficients, where
> $z = e(\theta)$. Since $|P(e(\theta))| = |\hat f(\theta)|$ for $f(n) = \varepsilon_{n-1}$, we
> integrate $|\hat f|^4$.
>
> We require $N \ge 2$, since for $N = 1$ the integral equals $1 = N^2$. The integral is
> $N^2(1 + 1/F)$, where $F$ is the merit factor of the coefficient sequence [JKS13], so the
> conjecture says that the merit factor of binary sequences is bounded.
>
> [Gr24] lists this as open. The conjecture is false: the largest merit factor of a binary sequence
> of length $N$ tends to infinity as $N \to \infty$ [OAI26a, Corollary 8.1], a consequence of
> [OAI26a, Theorem 1.1], which answers `Erdos1150.erdos_1150`. [OAI26a] is a 2026 preprint.

```lean
theorem green_84.variants.golay :
    ¬ ∃ c : ℝ, 0 < c ∧ ∀ N : ℕ, 2 ≤ N → ∀ f : ℕ → ℤ, IsSignOn N f →
      (1 + c) * (N : ℝ) ^ 2 ≤ ∫ θ in (0 : ℝ)..1, ‖fourierSum N f θ‖ ^ 4
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/84.lean, line 135](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean#L135).

## `Green84.green_84.variants.ultraflat_mod`

Open: stated without proof.

> [Gr24]: "I am not sure if it known whether or not there exists, for infinitely many $q$, a subset
> $A \subset \mathbb{Z}/q\mathbb{Z}$ of size $\sim q^{1/3}$, all of whose nontrivial Fourier
> coefficients have size $O(q^{1/6})$."
>
> We read $\sim$ as asymptotic equality, $|A_q| / q^{1/3} \to 1$ as $q \to \infty$ in an infinite set
> $Q$, and the $O(q^{1/6})$ bound as uniform in $q \in Q$. [Gr24] notes that $O(q^{1/6} \log q)$
> follows easily from a random construction.

```lean
theorem green_84.variants.ultraflat_mod :
    ∃ Q : Set ℕ, Q.Infinite ∧ ∃ C : ℝ, ∃ A : (q : ℕ) → Finset (ZMod q),
      Tendsto (fun q ↦ (#(A q) : ℝ) / (q : ℝ) ^ ((1 : ℝ) / 3))
        (atTop ⊓ Filter.principal Q) (𝓝 1) ∧
      ∀ q ∈ Q, ∀ r : ZMod q, r ≠ 0 → ‖fourierMod (A q) r‖ ≤ C * (q : ℝ) ^ ((1 : ℝ) / 6)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [42 Harmonic analysis on Euclidean spaces](../../by-subject/part-02/42-harmonic-analysis-on-euclidean-spaces/README.md). Declared in [FormalConjectures/GreensOpenProblems/84.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean#L150).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/84.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/84.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.84)
