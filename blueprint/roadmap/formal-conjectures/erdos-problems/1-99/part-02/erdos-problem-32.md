---
declaration: theorem
origin: cited
lean: Erdos32.erdos_32.variants.log_squared, Erdos32.erdos_32.variants.liminf_gt_one, Erdos32.erdos_32, Erdos32.erdos_32.variants.log_bound, Erdos32.erdos_32.variants.ruzsa
statement: formalized
---

# Erdős Problem 32

> *References:*
> * [erdosproblems.com/32](https://www.erdosproblems.com/32)
> * [Erd54] Erdős, Paul, Some results on additive number theory. Proc. Amer. Math. Soc. (1954),
>  847-853.
> * [Guy04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437
> * [Ru98c] Ruzsa, Imre Z., On the additive completion of primes. Acta Arith. (1998), 269-275.

*Quoted from [FormalConjectures/ErdosProblems/32.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/32](https://www.erdosproblems.com/32).

The file states 5 research or textbook statements: 2 open and 3 solved.

## `Erdos32.erdos_32.variants.log_squared`

Solved: stated here without proof.

> Erdős proved in [Erd54] that there exists an additive complement $A$ to the primes with
> $|A \cap \{1, \ldots, N\}| = O((\log N)^2)$.

```lean
theorem erdos_32.variants.log_squared : ∃ A : Set ℕ,
    IsAdditiveComplementToPrimes A ∧
    (fun N => (((Finset.Icc 1 N).filter (· ∈ A)).card : ℝ)) =O[atTop]
      fun N => (Real.log N) ^ 2
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/32.lean, line 50](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean#L50).

## `Erdos32.erdos_32.variants.liminf_gt_one`

Solved: stated here without proof.

> Must every additive complement $A$ to the primes satisfy
> $\liminf_{N \to \infty} \frac{|A \cap \{1, \ldots, N\}|}{\log N} > 1$?

```lean
theorem erdos_32.variants.liminf_gt_one : ∀ A : Set ℕ,
    IsAdditiveComplementToPrimes A →
    (1 : EReal) < liminf (fun N => (((Finset.Icc 1 N).filter (· ∈ A)).card / Real.log N : EReal))
      atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/32.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean#L62).

## `Erdos32.erdos_32`

Open: stated without proof.

> Does there exist a set $A \subseteq \mathbb{N}$ such that $|A \cap \{1, \ldots, N\}| = o((\log N)^2)$
> and every sufficiently large integer can be written as $p + a$ for some prime $p$ and $a \in A$?

```lean
theorem erdos_32 : ∃ A : Set ℕ,
    IsAdditiveComplementToPrimes A ∧
    (fun N => (((Finset.Icc 1 N).filter (· ∈ A)).card : ℝ)) =o[atTop]
      fun N => (Real.log N) ^ 2
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/32.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean#L74).

## `Erdos32.erdos_32.variants.log_bound`

Open: stated without proof.

> Can the bound $O(\log N)$ be achieved for an additive complement to the primes? [Guy04] writes
> that Erdős offered \$50 for the solution.

```lean
theorem erdos_32.variants.log_bound : ∃ A : Set ℕ,
    IsAdditiveComplementToPrimes A ∧
    (fun N => (((Finset.Icc 1 N).filter (· ∈ A)).card : ℝ)) =O[atTop]
      fun N => Real.log N
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/32.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean#L86).

## `Erdos32.erdos_32.variants.ruzsa`

Solved: stated here without proof.

> Ruzsa proved that any additive complement $A$ to the primes must satisfy
> $\liminf_{N \to \infty} \frac{|A \cap \{1, \ldots, N\}|}{\log N} \geq e^\gamma$,
> where $\gamma$ is the Euler-Mascheroni constant.

```lean
theorem erdos_32.variants.ruzsa : ∀ A : Set ℕ,
    IsAdditiveComplementToPrimes A →
    (Real.exp Real.eulerMascheroniConstant : EReal) ≤
      liminf (fun N => (((Finset.Icc 1 N).filter (· ∈ A)).card / Real.log N : EReal)) atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/32.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/32.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/32.lean)
- [erdosproblems.com/32](https://www.erdosproblems.com/32)
