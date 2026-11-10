---
declaration: theorem
origin: cited
lean: Bugeaud06.pollington_de_mathan, Bugeaud06.furstenberg_two_three, Bugeaud06.boshernitzan, Bugeaud06.exists_dense_of_growth, Bugeaud06.exists_dense_of_growth_and_sparsity, Bugeaud06.problem_10_6_variant_1, Bugeaud06.problem_10_6_variant_2
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: Rapidly Increasing Sequences Dense Modulo One

> Problem 10.6 asks for a "very rapidly increasing" sequence $(m_n)_{n \ge 1}$ of positive
> integers with $(\{\xi m_n\})_{n \ge 1}$ dense modulo one for every irrational $\xi$. The
> informal phrase admits several readings, and they are not equivalent:
>
> * a lower bound on the size of the terms, $m_n \ge f(n)$;
> * an upper bound on the counting function of $\{m_n\}$;
> * a lower bound on the consecutive ratios, $m_{n+1}/m_n \ge 1 + c/\log n$.
>
> The first two readings are vacuous, and `exists_dense_of_growth_and_sparsity` below says so: a
> sequence built from runs of consecutive integers is dense modulo one for every irrational $\xi$
> by an elementary argument, and the runs may be placed so that its terms dominate any prescribed
> $f$ while its counting function stays below $(\log\log N)^2$. In the subexponential range the
> growth half is a special case of [Bos83, Thm. 1.5], which produces such a sequence in any
> prescribed subexponential corridor and in the stronger uniform-distribution form; the sparsity
> half sits below the $\log N$ floor that every sublacunary sequence obeys, and so below the
> counting function of [Kat16, Cor. 4.10]. Consequently `problem_10_6_variant_2`, which asks only
> for intermediate growth, is not open.
>
> The third reading is `IsGenuinelySublacunary`, and it is the only one with content: it implies
> the first (`hasIntermediateGrowth_of_isGenuinelySublacunary`), and it is not answered by runs,
> since inside a run $m_{n+1} - m_n = 1$. That reading is `problem_10_6_variant_1`, which remains
> open; [Kat16, Cor. 4.9] gives a universally densifying sequence of multiplicative shape
> $\{2^n 3^e\}$ whose ratio behaviour reduces the question to a Diophantine statement about
> $\log_2 3$.
>
> The three statements that need a long proof carry a `formal_proof` link to the version of this
> file that contains it: the construction by runs, its counting function, and the growth estimate
> behind `hasIntermediateGrowth_of_isGenuinelySublacunary`.
>
> *References:*
>   - [Bos83] Boshernitzan, Michael D. "Homogeneously distributed sequences and Poincaré sequences
>     of integers of sublacunary growth." Monatshefte für Mathematik 96.3 (1983): 173-181.
>   - [Bos94] Boshernitzan, Michael D. "Density modulo 1 of dilations of sublacunary sequences."
>     Advances in Mathematics 108.1 (1994): 104-117.
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [Fur67] Furstenberg, H. "Disjointness in ergodic theory, minimal sets, and a problem
>     in diophantine approximation". Math. Systems Theory 1, 1–49 (1967).
>   - [Kat16] Katz, Asaf. "Generalizations of Furstenberg's Diophantine result."
>     arXiv:1607.00670 (2016).
>   - [Mat80] de Mathan, Bernard. "Numbers contravening a condition in density modulo 1."
>     Acta Mathematica Hungarica 36.3-4 (1980): 237-241.
>   - [Pol79] Pollington, Andrew Douglas. "On the density of sequence $\{n_ {k}\xi\} $."
>     Illinois Journal of Mathematics 23.4 (1979): 511-515.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 7 research or textbook statements: 1 open and 6 solved. It also has 3 test statements and 2 API statements, counted here but not shown.

## `Bugeaud06.pollington_de_mathan`

Solved: stated here without proof.

> The **Pollington–de Mathan theorem** [Pol79][Mat80]. For every lacunary sequence
> $(m_n)_{n \ge 1}$ of positive integers, the set of real numbers $\xi$ for which
> $(\{\xi m_n\})_{n \ge 1}$ is *not* dense modulo one has full Hausdorff dimension.

```lean
theorem pollington_de_mathan (m : ℕ → ℕ) (hm : ∀ n, 0 < m n) (hlac : IsLacunary m) :
    dimH {ξ : ℝ | ¬ Dense (Set.range fun n => (↑(ξ * m n) : AddCircle (1 : ℝ)))} = 1
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L81).

## `Bugeaud06.furstenberg_two_three`

Solved: stated here without proof.

> **Furstenberg's theorem** [Fur67] (the $\times 2, \times 3$ case). For every irrational
> number $\xi$, the two-parameter family $(\{\xi \, 2^m 3^n\})_{m, n \ge 1}$ is dense modulo
> one.

```lean
theorem furstenberg_two_three (ξ : ℝ) (hξ : Irrational ξ) :
    Dense {x : AddCircle (1 : ℝ) |
      ∃ m n : ℕ, 0 < m ∧ 0 < n ∧ x = ↑(ξ * (2 ^ m * 3 ^ n : ℕ))}
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 89](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L89).

## `Bugeaud06.boshernitzan`

Solved: stated here without proof.

> **Boshernitzan's theorem** [Bos94]. Given a real sublacunary sequence $r$, the set of
> real numbers $\xi$ for which $(\{\xi r_n\})_{n \ge 1}$ is *not* dense modulo one has
> Hausdorff dimension zero.

```lean
theorem boshernitzan (r : ℕ → ℝ) (hr : ∀ n, 0 < r n) (hunb : ¬ BddAbove (Set.range r))
    (hsub : Tendsto (fun n => r (n + 1) / r n) atTop (nhds 1)) :
    dimH {ξ : ℝ | ¬ Dense (Set.range fun n => (↑(ξ * r n) : AddCircle (1 : ℝ)))} = 0
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L98).

## `Bugeaud06.exists_dense_of_growth`

Solved: stated here; a Lean proof is at [https://github.com/rwst/formal-conjectures/blob/63c3e7233f1e512ea2474f35f4f2cd70624583f6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L398](https://github.com/rwst/formal-conjectures/blob/63c3e7233f1e512ea2474f35f4f2cd70624583f6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L398).

> **A lower bound on the size of the terms cannot make Problem 10.6 nontrivial.** For every
> growth demand `f` there is a strictly increasing sequence dominating `f` at every index which
> is dense modulo one for every irrational $\xi$.
>
> In the subexponential range this is a special case of [Bos83, Thm. 1.5], which produces such a
> sequence inside any prescribed corridor $[n_k, m_k)$ with $m_k - n_k \to \infty$ and
> $m_k / n_k \to 1$, and in the stronger form of uniform distribution; the elementary
> construction of the linked proof is uniform in `f` and has no growth ceiling.

```lean
theorem exists_dense_of_growth (f : ℕ → ℕ) :
    ∃ m : ℕ → ℕ, StrictMono m ∧ (∀ n, f n ≤ m n) ∧
      ∀ ξ : ℝ, Irrational ξ →
        Dense (Set.range fun n => (↑(ξ * m n) : AddCircle (1 : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L123).

## `Bugeaud06.exists_dense_of_growth_and_sparsity`

Solved: stated here; a Lean proof is at [https://github.com/rwst/formal-conjectures/blob/63c3e7233f1e512ea2474f35f4f2cd70624583f6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L411](https://github.com/rwst/formal-conjectures/blob/63c3e7233f1e512ea2474f35f4f2cd70624583f6/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L411).

> **Neither can an upper bound on the counting function, even together with the growth
> demand.** The same sequence dominates an arbitrary `f` *and* has counting function below
> $(\log\log N)^2$ — an exponential below the $\log N$ floor that every sublacunary sequence
> obeys, and so below the counting function of [Kat16, Cor. 4.10]. So a reading of "very rapidly
> increasing" that constrains only the size of the terms or the sparsity of their range leaves
> Problem 10.6 with no content.

```lean
theorem exists_dense_of_growth_and_sparsity (f : ℕ → ℕ) :
    ∃ m : ℕ → ℕ, StrictMono m ∧ (∀ n, f n ≤ m n) ∧
      (∀ᶠ N : ℕ in atTop, (countingFn m N : ℝ) ≤ (Real.log (Real.log N)) ^ 2) ∧
      ∀ ξ : ℝ, Irrational ξ →
        Dense (Set.range fun n => (↑(ξ * m n) : AddCircle (1 : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L138).

## `Bugeaud06.problem_10_6_variant_1`

Open: stated without proof.

> Problem 10.6. Find a very rapidly increasing sequence $(m_n)_{n \ge 1}$ of positive
> integers such that $(\{\xi m_n\})_{n \ge 1}$ is dense modulo one for every irrational
> number $\xi$. Note: Furstenberg's $2^m3^n$ is sublacunary but requires two parameters.
>
> This is the reading of "very rapidly increasing" as a lower bound on the consecutive ratios,
> and it is the one that remains open. It is not answered by runs of consecutive integers, since
> inside a run $m_{n+1} - m_n = 1$; and by `not_isLacunary_of_dense` any answer is pinched
> between a decaying ratio floor and the failure of lacunarity. [Kat16, Cor. 4.9] gives a
> universally densifying sequence of the multiplicative shape $\{2^n 3^e\}$, for which the
> ratio condition reduces to a Diophantine statement about the differences of the exponents
> $e$ times $\log_2 3$ modulo one.

```lean
theorem problem_10_6_variant_1 :
    ∃ m : ℕ → ℕ,
    StrictMono m ∧
    IsGenuinelySublacunary m ∧
    ∀ ξ : ℝ, Irrational ξ →
      Dense (Set.range fun n => (↑(ξ * m n) : AddCircle (1 : ℝ)))
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 250](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L250).

## `Bugeaud06.problem_10_6_variant_2`

Proved here.

> Problem 10.6, intermediate-growth variant. This asks only for a lower bound on the size of
> the terms, and under that reading the problem is not open: runs of consecutive integers answer
> it, by `exists_dense_of_growth` applied to $f(n) = \lceil e^n \rceil$. The witness below is
> exhibited at $\alpha = 1/2$; the same sequence works for every $\alpha < 1$, since
> $\exp(n^\alpha) \le \exp(n) \le f(n)$ there.
>
> The result is not new: [Bos83, Thm. 1.5] gives a sequence of any prescribed subexponential
> growth that is uniformly distributed — not merely dense — modulo one for every irrational
> dilate.

```lean
theorem problem_10_6_variant_2 :
    ∃ m : ℕ → ℕ,
    StrictMono m ∧
    (∃ α : ℝ, 0 < α ∧ α < 1 ∧ HasIntermediateGrowth α m) ∧
    ∀ ξ : ℝ, Irrational ξ →
      Dense (Set.range fun n => (↑(ξ * m n) : AddCircle (1 : ℝ)))
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean, line 268](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean#L268).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_6.lean)
