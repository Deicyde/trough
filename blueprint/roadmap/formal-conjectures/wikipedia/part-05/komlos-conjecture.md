---
declaration: theorem
origin: cited
lean: KomlosConjecture.komlos_conjecture, KomlosConjecture.komlos_conjecture.variants.banaszczyk
statement: formalized
---

# Komlós conjecture

> The Komlós conjecture in discrepancy theory: there is a universal constant $K$ such
> that for all $n, m$ and all vectors $v\_1, \dots, v\_n \in \mathbb{R}^m$ with
> $\|v\_i\|\_2 \le 1$, there exist signs $\varepsilon\_i \in \{-1, +1\}$ such that
> $$\left\|\sum\_{i=1}^n \varepsilon\_i v\_i\right\|\_\infty \le K.$$
>
> For a long time the best known bound was due to Banaszczyk, who proved that one can always
> achieve $O(\sqrt{\log n})$. The Beck–Fiala theorem on the discrepancy of sparse set systems
> is a special case (up to scaling), and the conjecture implies the Beck–Fiala
> conjecture that set systems of degree $t$ have discrepancy $O(\sqrt{t})$.
>
> The conjecture was proved in September 2026 by Guo, Fang and Lu with $K = 3\sqrt{2\pi}$.
> Karingula and Lovett gave an elementary proof with $K = 36$. A formalisation of their proof is
> recorded in the `formal_proof` attributes below.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Discrepancy_theory#Major_open_problems)
> - [W. Banaszczyk, *Balancing vectors and Gaussian measures of n-dimensional convex bodies*,
>   Random Structures & Algorithms **12** (1998), 351–360](https://doi.org/10.1002/(SICI)1098-2418(199807)12:4%3C351::AID-RSA3%3E3.0.CO;2-S)
> - [J. Spencer, *Six standard deviations suffice*,
>   Trans. Amer. Math. Soc. **289** (1985), 679–706](https://doi.org/10.1090/S0002-9947-1985-0784009-0)
> - [S. Guo, E. X. Fang and J. Lu, *Vector balancing via directional total variation*,
>   arXiv:2609.11189](https://arxiv.org/abs/2609.11189)
> - [S. R. Karingula and S. Lovett, *An elementary proof of the Komlós conjecture*,
>   arXiv:2609.20979](https://arxiv.org/abs/2609.20979)

*Quoted from [FormalConjectures/Wikipedia/KomlosConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/KomlosConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `KomlosConjecture.komlos_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/416b6597cb193b6745748fdfef0d64342c71dae9/FormalConjectures/Wikipedia/KomlosConjecture.lean#L64](https://github.com/mo271/formal-conjectures/blob/416b6597cb193b6745748fdfef0d64342c71dae9/FormalConjectures/Wikipedia/KomlosConjecture.lean#L64).

> **The Komlós conjecture**
>
> There exists a universal constant $K > 0$ such that for all $n, m \in \mathbb{N}$ and
> all vectors $v\_1, \dots, v\_n \in \mathbb{R}^m$ with $\|v\_i\|\_2 \le 1$ (encoded here as
> $\sum\_j v\_{ij}^2 \le 1$), there exist signs $\varepsilon\_i \in \{-1, +1\}$ such that
> $\left\|\sum\_i \varepsilon\_i v\_i\right\|\_\infty \le K$, i.e.
> $\left|\sum\_i \varepsilon\_i v\_{ij}\right| \le K$ for every coordinate $j$.
>
> Proved by Guo, Fang and Lu with $K = 3\sqrt{2\pi}$ and by Karingula and Lovett with $K = 36$.

```lean
theorem komlos_conjecture :
    ∃ K : ℝ, 0 < K ∧ ∀ (n m : ℕ) (v : Fin n → Fin m → ℝ),
      (∀ i, ∑ j, (v i j) ^ 2 ≤ 1) →
      ∃ ε : Fin n → ℝ, (∀ i, ε i = 1 ∨ ε i = -1) ∧
        ∀ j, |∑ i, ε i * v i j| ≤ K
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/KomlosConjecture.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/KomlosConjecture.lean#L67).

## `KomlosConjecture.komlos_conjecture.variants.banaszczyk`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/416b6597cb193b6745748fdfef0d64342c71dae9/FormalConjectures/Wikipedia/KomlosConjecture.lean#L86](https://github.com/mo271/formal-conjectures/blob/416b6597cb193b6745748fdfef0d64342c71dae9/FormalConjectures/Wikipedia/KomlosConjecture.lean#L86).

> **Banaszczyk's theorem**
>
> There exists a constant $C > 0$ such that for all $n, m \in \mathbb{N}$ and all vectors
> $v\_1, \dots, v\_n \in \mathbb{R}^m$ with $\|v\_i\|\_2 \le 1$, there exist signs
> $\varepsilon\_i \in \{-1, +1\}$ such that
> $\left\|\sum\_i \varepsilon\_i v\_i\right\|\_\infty \le C \sqrt{\log(n + 2)}$.
> This was the best known bound towards the Komlós conjecture before its solution. (The shift
> $n + 2$ inside the logarithm is a harmless normalization keeping it positive for
> $n \in \{0, 1\}$.) It follows from the Komlós conjecture with $C = 36 / \sqrt{\log 2}$.
>
> [W. Banaszczyk, *Balancing vectors and Gaussian measures of n-dimensional convex bodies*,
> Random Structures & Algorithms **12** (1998), 351–360.]

```lean
theorem komlos_conjecture.variants.banaszczyk :
    ∃ C : ℝ, 0 < C ∧ ∀ (n m : ℕ) (v : Fin n → Fin m → ℝ),
      (∀ i, ∑ j, (v i j) ^ 2 ≤ 1) →
      ∃ ε : Fin n → ℝ, (∀ i, ε i = 1 ∨ ε i = -1) ∧
        ∀ j, |∑ i, ε i * v i j| ≤ C * Real.sqrt (Real.log (n + 2))
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/KomlosConjecture.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/KomlosConjecture.lean#L91).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/KomlosConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/KomlosConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Discrepancy_theory#Major_open_problems)
