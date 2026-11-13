---
declaration: theorem
origin: cited
lean: Green17.green_17.parts.i, Green17.green_17.parts.ii, Green17.green_17.variants.exponential, Green17.green_17.variants.bklm, Green17.green_17.variants.symmetric
statement: formalized
---

# Ben Green's Open Problem 17

> *References:*
> - [Gr24] [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.17)
> - [Hą20] Hązła, J., *On arithmetic progressions in symmetric sets in finite field model*.
>   Electron. J. Combin. 27 (2020), no. 3, Paper No. 3.61.
>   [arXiv:1811.09947](https://arxiv.org/abs/1811.09947)
> - [BKLM24] Bhangale, A., Khot, S., Liu, Y. P. and Minzer, D., *On approximability of satisfiable
>   $k$-CSPs: VI*. [arXiv:2411.15133](https://arxiv.org/abs/2411.15133) (2024).

*Quoted from [FormalConjectures/GreensOpenProblems/17.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 5 research or textbook statements: 3 open and 2 solved. It also has 1 test statement, counted here but not shown.

## `Green17.green_17.parts.i`

Open: stated without proof.

> Suppose that $A \subset \mathbb{F}_3^n$ is a set of density $\alpha$. Under what conditions on
> $\alpha$ is $A$ guaranteed to contain a 3-term progression with nonzero common difference in
> $\{0, 1\}^n$?
>
> We read the question as asking for the order of magnitude of the threshold density
> $\alpha(n) = r(n) / 3^n$, where $r(n)$ is `maxFree n`: every set of density greater than
> $\alpha(n)$ contains such a progression, and some set of density $\alpha(n)$ does not. [Gr24]
> notes that $\alpha(n) \to 0$ by the density Hales-Jewett theorem; for the best known bound see
> `green_17.variants.bklm`.

```lean
theorem green_17.parts.i :
    (fun n : ℕ ↦ (maxFree n : ℝ) / 3 ^ n) =Θ[atTop] green_17.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/17.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean#L101).

## `Green17.green_17.parts.ii`

Open: stated without proof.

> Suppose that $A \subset \mathbb{F}_3^n$ is a set of density $\alpha$. For fixed $\alpha$, must
> $A$ contain $\gg_\alpha 6^n$ 3-term progressions with nonzero common difference in
> $\{0, 1\}^n$?
>
> A progression is counted as a pair $(x, d)$, see `numRestrictedAPs`. We read $\gg_\alpha 6^n$ as
> at least $c(\alpha) 6^n$ for all $n \ge n_0(\alpha)$. A bound for all $n$ is false: for $n = 1$
> the set $\{0, 1\}$ has density $2/3$ and contains no such progression.

```lean
theorem green_17.parts.ii :
    ∀ α : ℝ, 0 < α → ∃ c : ℝ, 0 < c ∧ ∀ᶠ n : ℕ in atTop, ∀ A : Finset (𝔽₃ n),
      α * 3 ^ n ≤ (A.card : ℝ) → c * 6 ^ n ≤ (numRestrictedAPs A : ℝ)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/17.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean#L115).

## `Green17.green_17.variants.exponential`

Open: stated without proof.

> Is there a constant $c \in (0, 1)$ such that, for all large $n$, every set
> $A \subseteq \mathbb{F}_3^n$ of density at least $(1 - c)^n$ contains a 3-term progression with
> nonzero common difference in $\{0, 1\}^n$?
>
> [Gr24] notes that a density $\alpha \to 0$ slowly enough forces such a progression, and that
> this may even hold with $\alpha = (1-c)^n$ for some $c > 0$. We require $c < 1$, so that
> $(1 - c)^n > 0$.

```lean
theorem green_17.variants.exponential :
    ∃ c : ℝ, 0 < c ∧ c < 1 ∧ ∀ᶠ n : ℕ in atTop, ∀ A : Finset (𝔽₃ n),
      (1 - c) ^ n * 3 ^ n ≤ (A.card : ℝ) → HasRestrictedAP A
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/17.lean, line 130](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean#L130).

## `Green17.green_17.variants.bklm`

Solved: stated here without proof.

> **Bhangale, Khot, Liu and Minzer.** There are constants $c, C > 0$ such that every set
> $A \subseteq \mathbb{F}_3^n$ of density at least $C (\log \log \log n)^{-c}$ contains a 3-term
> progression with nonzero common difference in $\{0, 1\}^n$.
>
> This is [BKLM24, Theorem 3] for $\Sigma = \mathbb{F}_3$ and
> $S = \{(x, x + a, x + 2a) : x \in \mathbb{F}_3, a \in \{0, 1\}\}$, as in [BKLM24, Section 1.2.1]:
> three points of $A$, not all equal, with $(x_i, y_i, z_i) \in S$ for all $i$ form such a
> progression. We state it for large $n$, where $\log \log \log n > 0$.

```lean
theorem green_17.variants.bklm :
    ∃ c C : ℝ, 0 < c ∧ 0 < C ∧ ∀ᶠ n : ℕ in atTop, ∀ A : Finset (𝔽₃ n),
      C / Real.log (Real.log (Real.log n)) ^ c * 3 ^ n ≤ (A.card : ℝ) → HasRestrictedAP A
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/17.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean#L146).

## `Green17.green_17.variants.symmetric`

Solved: stated here without proof.

> **Hązła.** For every $\mu > 0$ there is $\delta > 0$ such that every symmetric set
> $A \subseteq \mathbb{F}_3^n$ of density at least $\mu$ contains at least $\delta 6^n$
> progressions $x, x + d, x + 2d$ with $d \in \{0, 1\}^n$ [Hą20, abstract and Theorem 2, case
> $q = 3$].
>
> [Hą20] counts all pairs $(x, d)$ with $d \in \{0, 1\}^n$, including the $|A|$ pairs with
> $d = 0$; this is why `A.card` is added to `numRestrictedAPs A`. For large $n$ the $d = 0$ pairs
> are negligible, so `green_17.parts.ii` holds for symmetric sets. [Hą20, abstract] states the
> result for sets of density exactly $\mu$. The form with density at least $\mu$ follows from the
> removal statement [Hą20, Theorem 2] with $\mu/2$ in place of $\mu$: it removes a single symmetric
> set of density at most $\mu/2$ and leaves a set with no progressions, but the remaining set is
> nonempty and contains the progressions with $d = 0$.

```lean
theorem green_17.variants.symmetric :
    ∀ μ : ℝ, 0 < μ → ∃ δ : ℝ, 0 < δ ∧ ∀ n : ℕ, ∀ A : Finset (𝔽₃ n), IsSymmetric A →
      μ * 3 ^ n ≤ (A.card : ℝ) → δ * 6 ^ n ≤ (numRestrictedAPs A + A.card : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/GreensOpenProblems/17.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean#L166).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/17.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/GreensOpenProblems/17.lean)
- [Green, Ben. "100 open problems." (2024).](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.17)
