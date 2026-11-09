---
declaration: theorem
origin: cited
lean: Erdos782.erdos_782.parts.i, Erdos782.erdos_782.parts.ii, Erdos782.erdos_782.variants.no_four_term_ap, Erdos782.erdos_782.variants.dietmann_elsholtz
statement: formalized
---

# Erdős Problem 782

> *References:*
> - [erdosproblems.com/782](https://www.erdosproblems.com/782)
> - [BEF90] Brown, T. C. and Erdős, P. and Freedman, A. R., _Quasi-progressions and descending
>   waves_. J. Combin. Theory Ser. A 53 (1990), 81-95.
> - [BFS03] Brown, T. C., Freedman, A. R. and Shiue, P. J.-S., _Progressions of squares_.
>   Australas. J. Combin. 27 (2003), 187-192.
> - [BEU26] Bremner, A., Elsholtz, C. and Ulas, M., _There are infinitely many Hilbert cubes of
>   dimension 3 in the set of squares_. [arXiv:2604.05459](https://arxiv.org/abs/2604.05459) (2026).
> - [CiGr07] Cilleruelo, J. and Granville, A., _Lattice points on circles, squares in arithmetic
>   progressions and sumsets of squares_. Additive combinatorics (2007), 241-262.
> - [DiEl12] Dietmann, R. and Elsholtz, C., _Hilbert cubes in progression-free sets and in the set
>   of squares II_. [arXiv:1207.1461](https://arxiv.org/abs/1207.1461) (2012).
> - [So07] Solymosi, J., _Elementary additive combinatorics_. Additive combinatorics (2007), 29-38.

*Quoted from [FormalConjectures/ErdosProblems/782.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/782](https://www.erdosproblems.com/782).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos782.erdos_782.parts.i`

Open: stated without proof.

> Do the squares contain arbitrarily long quasi-progressions? That is, does there exist some
> constant $C>0$ such that, for any $k$, the squares contain a sequence $x_1,\ldots,x_k$ where, for
> some $d$ and all $1\leq i\lt k$,
>
> $$x_i+d\leq x_{i+1}\leq x_i+d+C.$$
>
> A question of Brown, Erdős, and Freedman [BEF90]. This is the first question. Here $C$ and $d$ are
> positive integers; $d\geq 1$ excludes constant sequences.

```lean
theorem erdos_782.parts.i :
    ∃ C : ℕ, 0 < C ∧ ∀ k : ℕ, ContainsQuasiProgression {n : ℕ | IsSquare n} C k
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/782.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean#L87).

## `Erdos782.erdos_782.parts.ii`

Open: stated without proof.

> Do the squares contain arbitrarily large cubes
>
> $$a+\left\{ \sum_i \epsilon_ib_i : \epsilon_i\in \{0,1\}\right\}?$$
>
> A question of Brown, Erdős, and Freedman [BEF90]. This is the second question. The generators
> $b_i$ are nonzero integers, as in [BEU26]. Solymosi [So07] conjectured that the answer is no, and
> Cilleruelo and Granville [CiGr07] observed that the answer is no conditional on the
> Bombieri-Lang conjecture.

```lean
theorem erdos_782.parts.ii :
    ∀ d : ℕ, ∃ (a : ℤ) (b : Fin d → ℤ),
      (∀ i, b i ≠ 0) ∧ hilbertCube a b ⊆ {n : ℤ | IsSquare n}
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/782.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean#L101).

## `Erdos782.erdos_782.variants.no_four_term_ap`

Solved: stated here without proof.

> It is a classical fact that the squares do not contain arithmetic progressions of length
> $4$.

```lean
theorem erdos_782.variants.no_four_term_ap :
    Set.IsAPOfLengthFree {n : ℕ | IsSquare n} 4
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/782.lean, line 109](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean#L109).

## `Erdos782.erdos_782.variants.dietmann_elsholtz`

Solved: stated here without proof.

> Dietmann and Elsholtz [DiEl12, Theorem 1] proved that, for all sufficiently large $N$, if
> $a_0\geq 0$ and $b_1,\ldots,b_d$ are distinct positive integers such that the Hilbert cube
> $a_0+\{0,b_1\}+\cdots+\{0,b_d\}$ consists of squares in $[1,N]$, then $d\leq 7\log\log N$.

```lean
theorem erdos_782.variants.dietmann_elsholtz :
    ∃ N₀ : ℕ, ∀ N ≥ N₀, ∀ (d : ℕ) (a₀ : ℤ) (b : Fin d → ℤ),
      0 ≤ a₀ → Function.Injective b → (∀ i, 0 < b i) →
      hilbertCube a₀ b ⊆ {n : ℤ | IsSquare n ∧ 1 ≤ n ∧ n ≤ N} →
        (d : ℝ) ≤ 7 * Real.log (Real.log N)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/782.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean#L119).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/782.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/782.lean)
- [erdosproblems.com/782](https://www.erdosproblems.com/782)
