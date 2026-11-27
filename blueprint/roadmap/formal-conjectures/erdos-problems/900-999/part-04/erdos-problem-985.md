---
declaration: theorem
origin: cited
lean: Erdos985.erdos_985, Erdos985.erdos_985.variants.two_three_five_primitive_root
statement: formalized
---

# Erdős Problem 985

> *References:*
> - [erdosproblems.com/985](https://www.erdosproblems.com/985)
> - [MTT16] McGown, K., Treviño, E. and Trudgian, T., *Resolving Grosswald's conjecture on GRH*.
>   Funct. Approx. Comment. Math. 55 (2016), 215–225.
>   [arXiv:1508.05182](https://arxiv.org/abs/1508.05182)
> - [Al26] Alpöge, L., [Note on the Riemann Hypothesis](https://alpo.ge/remark.pdf) (2026).

*Quoted from [FormalConjectures/ErdosProblems/985.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/985.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/985](https://www.erdosproblems.com/985).

The file states 2 research or textbook statements: 2 solved.

## `Erdos985.erdos_985`

Solved: stated here without proof.

> Is it true that, for every prime $p$, there is a prime $q \leq p$ which is a primitive root modulo $p$?
>
> The answer is yes. Assuming the Generalized Riemann Hypothesis for Dirichlet $L$-functions, the
> least prime primitive root modulo $p$ is less than $\sqrt{p} - 2$ for every prime $p > 2791$
> [MTT16, Theorem 1]. A finite computation covers the odd primes $p \leq 2791$. The Generalized
> Riemann Hypothesis is proved [Al26].

```lean
theorem erdos_985 : ∀ᵉ (p : ℕ) (hp_prime : p.Prime) (hp_nontrivial : p ≠ 2),
    ∃ q, q.Prime ∧ q < p ∧ orderOf (q : ZMod p) = p - 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/985.lean, line 44](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/985.lean#L44).

## `Erdos985.erdos_985.variants.two_three_five_primitive_root`

Solved: stated here without proof.

> Heath-Brown proved that at least one of 2, 3, or 5 is a primitive root for infinitely many primes $p$.

```lean
theorem erdos_985.variants.two_three_five_primitive_root :
    Set.Infinite
      {p : ℕ | p.Prime ∧
      (orderOf (2 : ZMod p) = p - 1 ∨
       orderOf (3 : ZMod p) = p - 1 ∨
       orderOf (5 : ZMod p) = p - 1)}
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/985.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/985.lean#L56).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/985.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/985.lean)
- [erdosproblems.com/985](https://www.erdosproblems.com/985)
