---
declaration: theorem
origin: cited
lean: Erdos504.erdos_504, Erdos504.erdos_504.variants.endpoint, Erdos504.erdos_504.variants.erdos_szekeres_1960, Erdos504.erdos_504.variants.szekeres_lower, Erdos504.erdos_504.variants.szekeres_upper, Erdos504.erdos_504.variants.sendov
statement: formalized
---

# Erdős Problem 504

> *Reference:* [erdosproblems.com/504](https://www.erdosproblems.com/504)
>
> Blumenthal's minimax angle problem: let $\alpha_N$ be the supremum of all
> $0 \le \alpha \le \pi$ such that every set of $N$ points in the plane contains
> three distinct points determining an angle at least $\alpha$. Determine
> $\alpha_N$.
>
> Szekeres [Sz41] proved $\alpha_{2^n} \le \pi(1 - 1/n)$ together with a lower
> bound for $2^n + 1$ points. Erdős and Szekeres [ErSz60] proved
> $\alpha_{2^n} = \alpha_{2^n - 1} = \pi(1 - 1/n)$, and Sendov [Se95] determined
> $\alpha_N$ for every $N$.
>
> [Sz41] Szekeres, G., _On an extremum problem in the plane_. Amer. J. Math. 63
> (1941), 208-210.
>
> [ErSz60] Erdős, P. and Szekeres, G., _On some extremum problems in elementary
> geometry_. Ann. Univ. Sci. Budapest. Eötvös Sect. Math. 3-4 (1960-61), 53-62.
>
> [Se95] Sendov, Bl., _Minimax of the angles in a plane configuration of points_.
> Acta Math. Hungar. 69 (1995), 27-46. (Reviewed in Zbl 0853.52009, which states the
> main theorem as $\alpha_N = \pi\left(1 - \frac{2}{2n+1}\right)$ for
> $2^n < N \le 2^n + 2^{n-2}$ and $\alpha_N = \pi\left(1 - \frac{1}{n+1}\right)$ for
> $2^n + 2^{n-2} < N \le 2^{n+1}$, $n \ge 2$.)

*Quoted from [FormalConjectures/ErdosProblems/504.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/504](https://www.erdosproblems.com/504).

The file states 6 research or textbook statements: 6 solved.

## `Erdos504.erdos_504`

Solved: stated here without proof.

> **Erdős–Szekeres (1960).** For $n \ge 3$,
> $\alpha_{2^n} = \pi\left(1 - \frac{1}{n}\right)$.

```lean
theorem erdos_504 {n : ℕ} (hn : 3 ≤ n) :
    minimaxAngle (2 ^ n) = (1 - 1 / (n : ℝ)) * π
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L71).

## `Erdos504.erdos_504.variants.endpoint`

Solved: stated here without proof.

> **Erdős–Szekeres (1960).** For $n \ge 3$, also
> $\alpha_{2^n - 1} = \pi\left(1 - \frac{1}{n}\right)$.

```lean
theorem erdos_504.variants.endpoint {n : ℕ} (hn : 3 ≤ n) :
    minimaxAngle (2 ^ n - 1) = (1 - 1 / (n : ℝ)) * π
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L80).

## `Erdos504.erdos_504.variants.erdos_szekeres_1960`

Solved: stated here; a Lean proof is at [https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L6501](https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L6501).

> The lower-bound half of `erdos_504` in existential form (Theorem 1 of
> [ErSz60]): any $2^n$ points of the plane contain three points determining an
> angle strictly greater than $\pi(1 - 1/n)$.

```lean
theorem erdos_504.variants.erdos_szekeres_1960 {n : ℕ} (hn : 3 ≤ n)
    (S : Finset ℂ) (hcard : S.card = 2 ^ n) :
    ∃ p ∈ S, ∃ q ∈ S, ∃ r ∈ S, p ≠ q ∧ r ≠ q ∧
      (1 - 1 / (n : ℝ)) * π < EuclideanGeometry.angle p q r
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L92).

## `Erdos504.erdos_504.variants.szekeres_lower`

Solved: stated here; a Lean proof is at [https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L341](https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L341).

> **Szekeres (1941), lower bound.** More than $2^n$ points of the plane contain
> three points determining an angle strictly greater than $\pi(1 - 1/n)$.

```lean
theorem erdos_504.variants.szekeres_lower {n : ℕ} (hn : 0 < n) (S : Finset ℂ)
    (hcard : 2 ^ n < S.card) :
    ∃ p ∈ S, ∃ q ∈ S, ∃ r ∈ S, p ≠ q ∧ r ≠ q ∧
      (1 - 1 / (n : ℝ)) * π < EuclideanGeometry.angle p q r
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L105).

## `Erdos504.erdos_504.variants.szekeres_upper`

Solved: stated here; a Lean proof is at [https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L801](https://github.com/ToshiDad/erdos-504/blob/fd344a9/Erdos504.lean#L801).

> **Szekeres (1941), upper-bound construction.** For every $\varepsilon > 0$
> there is a set of exactly $2^t$ points of the plane all of whose angles are
> less than $\pi(1 - 1/t) + \varepsilon$. Together with
> `erdos_504.variants.erdos_szekeres_1960` this pins down
> $\alpha_{2^t} = \pi(1 - 1/t)$ for $t \ge 3$, where the supremum is approached
> but not attained by any finite configuration. (For $t = 2$ it is attained:
> a square has all angles at most $\pi/2 = \alpha_4$.)

```lean
theorem erdos_504.variants.szekeres_upper {t : ℕ} (ht : 0 < t) {ε : ℝ}
    (hε : 0 < ε) :
    ∃ S : Finset ℂ, S.card = 2 ^ t ∧
      ∀ p ∈ S, ∀ q ∈ S, ∀ r ∈ S, p ≠ q → r ≠ q →
        EuclideanGeometry.angle p q r < (1 - 1 / (t : ℝ)) * π + ε
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L123).

## `Erdos504.erdos_504.variants.sendov`

Solved: stated here without proof.

> **Sendov (1995).** The complete determination: for $n \ge 3$,
> $\alpha_N = \pi(1 - 1/n)$ whenever $2^{n-1} + 2^{n-3} < N \le 2^n$, and
> $\alpha_N = \pi\left(1 - \frac{2}{2n - 1}\right)$ whenever
> $2^{n-1} < N \le 2^{n-1} + 2^{n-3}$.
>
> This is the statement of [Se95] (as given in Zbl 0853.52009) with $n$ shifted by one.
> For $n = 3$ the second branch gives $\alpha_5 = 3\pi/5$, the value computed in [ErSz60],
> and $\alpha_N$ is nondecreasing in $N$ across the two branches.
> The problem page [erdosproblems.com/504](https://www.erdosproblems.com/504) prints the
> second branch as $\pi(1 - \frac{1}{2n-1})$, which would give $\alpha_5 = 4\pi/5 > \alpha_6$;
> that appears to be a typo.

```lean
theorem erdos_504.variants.sendov {n N : ℕ} (hn : 3 ≤ n)
    (h1 : 2 ^ (n - 1) < N) (h2 : N ≤ 2 ^ n) :
    minimaxAngle N =
      if 2 ^ (n - 1) + 2 ^ (n - 3) < N then (1 - 1 / (n : ℝ)) * π
      else (1 - 2 / (2 * (n : ℝ) - 1)) * π
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/504.lean, line 144](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean#L144).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/504.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/504.lean)
- [erdosproblems.com/504](https://www.erdosproblems.com/504)
