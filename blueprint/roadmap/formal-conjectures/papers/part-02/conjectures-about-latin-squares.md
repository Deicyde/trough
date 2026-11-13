---
declaration: theorem
origin: cited
lean: LatinSquare.oddOrderLatinSquareTransversal, LatinSquare.oddOrderLeq9LatinSquareTransversal, LatinSquare.latinSquareOrder11Transversal, LatinSquare.latinSquareNearTransversal, LatinSquare.z_even, LatinSquare.numTransversalsZn, LatinSquare.growthRateZn, LatinSquare.maxTransversalsBound, LatinSquare.molsExistenceProblem, LatinSquare.molsOrder12
statement: formalized
---

# Conjectures about Latin Squares

> This file formalizes some conjectures and theorems around latin squares.
>
> *References:*
> * [Wa2011] Wanless, Ian. "Transversals in Latin Squares: A Survey."
>   Surveys in Combinatorics 2011, R. Chapman, Ed. Cambridge University Press, 2011, pp. 403–437.
>   https://users.monash.edu.au/~iwanless/papers/transurveyBCC.pdf
> * https://en.wikipedia.org/wiki/Problems_in_Latin_squares

*Quoted from [FormalConjectures/Paper/LatinSquare.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 10 research or textbook statements: 7 open, 2 solved and 1 textbook result. It also has 2 test statements, counted here but not shown.

## `LatinSquare.oddOrderLatinSquareTransversal`

Open: stated without proof.

> Conjecture 3.2 in [Wa2011]:
> Each Latin square of odd order has at least one transversal.

```lean
theorem oddOrderLatinSquareTransversal :
    ∀ (n : ℕ), Odd n → ∀ (L : LatinSquare n), ∃ σ, IsTransversal L σ
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L60).

## `LatinSquare.oddOrderLeq9LatinSquareTransversal`

Solved: stated here without proof.

> The conjecture is known to be true for $n \leq 9$.

```lean
theorem oddOrderLeq9LatinSquareTransversal :
    ∀ n ≤ 9, Odd n → ∀ (L : LatinSquare n), ∃ σ, IsTransversal L σ
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L68).

## `LatinSquare.latinSquareOrder11Transversal`

Open: stated without proof.

> The smallest odd number for which this conjecture is not known is 11.

```lean
theorem latinSquareOrder11Transversal :
    ∀ (L : LatinSquare 11), ∃ σ, IsTransversal L σ
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L76).

## `LatinSquare.latinSquareNearTransversal`

Open: stated without proof.

> Conjecture 5.1 in [Wa2011]:
> Every latin square has a near-transversal

```lean
theorem latinSquareNearTransversal :
    ∀ (n : ℕ) (L : LatinSquare n), ∃ ρ σ, IsNearTransversal L ρ σ
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L91).

## `LatinSquare.z_even`

Textbook result, proved here.

> The Cayley table of $\mathbb{Z}_n$ for positive even $n$ has no transversals.

```lean
theorem z_even (n : ℕ) : z (2 * (n + 1)) = 0
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L118).

## `LatinSquare.numTransversalsZn`

Open: stated without proof.

> Conjecture 6.7 in [Wa2011]:
> There exist real constants $0 < c_1 < c_2 < 1$ such that
>
> $$
> c_1^n n! \leq z_n \leq c_2^n n!
> $$
>
> for all odd $n \geq 3$.

```lean
theorem numTransversalsZn :
      ∃ᵉ (c₁ > (0 : ℝ)) (c₂ < (1 : ℝ)) (_ : c₁ < c₂),
      ∀ n ≥ 3, Odd n →
        (z n : ℝ) ∈ Set.Icc (c₁ ^ n * n.factorial) (c₂ ^ n * n.factorial)
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 169](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L169).

## `LatinSquare.growthRateZn`

Open: stated without proof.

> Conjecture 6.9 in [Wa2011]:
>
> $$
> \lim_{\substack{n \to \infty \\ n \text{ odd}}} \frac{1}{n} \log(z_n / n!) = -1
> $$
>
> It is not even known if this limit exists. Note that $z_n = 0$ for even $n$ (see `z_even`), so the
> limit must be restricted to odd $n$; here we parametrise odd $n$ as $2k + 1$.

```lean
theorem growthRateZn :
    Filter.Tendsto (fun k => (1 : ℝ) / (2 * k + 1) *
      Real.log (z (2 * k + 1) / (2 * k + 1).factorial)) Filter.atTop
      (nhds (-1))
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 184](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L184).

## `LatinSquare.maxTransversalsBound`

Solved: stated here without proof.

> Theorem 7.2 in [Wa2011]:
> For all $n \geq 5$,
>
> $$
> 15^{n/5} \leq T(n) \leq c^n \sqrt{n} \cdot n!
> $$
>
> where $c = \sqrt{\frac{3 - \sqrt{3}}{6}} \cdot e^{\sqrt{3}/6}$

```lean
theorem maxTransversalsBound :
    let c := Real.sqrt ((3 - Real.sqrt 3) / 6) * Real.exp (Real.sqrt 3 / 6)
    ∀ n : ℕ, n ≥ 5 →
      (T n : ℝ) ∈ Set.Icc ((15 : ℝ) ^ ((n : ℝ) / 5)) (c ^ n * Real.sqrt n * n.factorial)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L202).

## `LatinSquare.molsExistenceProblem`

Open: stated without proof.

> MOLS existence problem: determine exactly which orders `n` admit a complete set of `n - 1`
> mutually orthogonal latin squares.
>
> Equivalently, this asks for which orders affine planes of order `n` exist. Complete sets are known
> for prime-power orders; the smallest currently unresolved order is `12`.

```lean
theorem molsExistenceProblem : molsExistenceProblem.answer = {n : ℕ | HasCompleteMOLS n}
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L218).

## `LatinSquare.molsOrder12`

Open: stated without proof.

> The smallest unresolved case of the MOLS existence problem: whether there are `11` mutually
> orthogonal latin squares of order `12`.

```lean
theorem molsOrder12 : HasCompleteMOLS 12
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Paper/LatinSquare.lean, line 226](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean#L226).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Paper/LatinSquare.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Paper/LatinSquare.lean)
- [https://users.monash.edu.au/~iwanless/papers/transurveyBCC.pdf](https://users.monash.edu.au/~iwanless/papers/transurveyBCC.pdf)
