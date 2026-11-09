---
declaration: theorem
origin: cited
lean: Bugeaud08.problem_10_8, Bugeaud08.problem_10_8.variants.quadratic, Bugeaud08.problem_10_8.variants.exceptional_set_dimH_zero
statement: formalized
---

# Bugeaud Collection of Conjectures and Open Questions: $p$-adic Littlewood Conjecture

> This is the $p$-adic analogue of the Littlewood conjecture, posed by de Mathan and
> Teulié. A liminf-based formulation also appears in the file
> `FormalConjectures/Wikipedia/LittlewoodConjecture.lean` as `padic_littlewood_conjecture`.
>
> *References:*
>   - [Bug12] Bugeaud, Yann. "Distribution modulo one and Diophantine approximation."
>     Vol. 193. Cambridge University Press, 2012. Chapter 10.
>   - [dMT04] de Mathan, Bernard, and Olivier Teulié. "Problèmes diophantiens simultanés."
>     Monatshefte für Mathematik 143.3 (2004): 229-245.
>   - [EK07] Einsiedler, Manfred, and Dmitry Kleinbock. "Measure rigidity and $p$-adic
>     Littlewood-type problems." Compositio Mathematica 143.3 (2007): 689-702.

*Quoted from [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Bugeaud08.problem_10_8`

Open: stated without proof.

> Problem 10.8 ($p$-adic Littlewood conjecture). For every real number $\xi$ and
> every prime number $p$,
> $$\inf_{q \ge 1} q \cdot \lVert q \xi \rVert \cdot |q|_p = 0,$$
> where $\lVert \cdot \rVert$ denotes the distance to the nearest integer and
> $|\cdot|_p$ denotes the $p$-adic absolute value. Posed by de Mathan and
> Teulié [dMT04].

```lean
theorem problem_10_8 (ξ : ℝ) (p : ℕ) (hp : p.Prime) :
    sInf {x : ℝ | ∃ q : ℕ, 1 ≤ q ∧
      x = q * padicNorm p q * distToNearestInt (q * ξ)} = 0
```

Category `research open`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean#L49).

## `Bugeaud08.problem_10_8.variants.quadratic`

Solved: stated here without proof.

> The quadratic case of Problem 10.8. de Mathan and Teulié [dMT04] solved the
> $p$-adic Littlewood conjecture for quadratic real numbers.

```lean
theorem problem_10_8.variants.quadratic (ξ : ℝ) (p : ℕ) (hp : p.Prime)
    (hξ : (minpoly ℚ ξ).natDegree = 2) :
    sInf {x : ℝ | ∃ q : ℕ, 1 ≤ q ∧
      x = q * padicNorm p q * distToNearestInt (q * ξ)} = 0
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean#L59).

## `Bugeaud08.problem_10_8.variants.exceptional_set_dimH_zero`

Solved: stated here without proof.

> The exceptional set for Problem 10.8 has Hausdorff dimension zero (Einsiedler
> and Kleinbock [EK07].

```lean
theorem problem_10_8.variants.exceptional_set_dimH_zero (p : ℕ) (hp : p.Prime) :
    dimH {ξ : ℝ | Filter.atTop.liminf
      (fun q : ℕ ↦ q * padicNorm p q * distToNearestInt (q * ξ)) ≠ 0} = 0
```

Category `research solved`; AMS [11 Number theory](../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Books/BugeaudDistributionModuloOne/Problem10_8.lean)
