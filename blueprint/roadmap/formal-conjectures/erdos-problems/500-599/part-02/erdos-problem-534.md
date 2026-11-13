---
declaration: theorem
origin: cited
lean: Erdos534.erdos_534
statement: formalized
---

# Erdős Problem 534

> *References:*
> - [erdosproblems.com/534](https://www.erdosproblems.com/534)
> - [Er73] Erdős, P., _Problems and results on combinatorial number theory_. A survey of
>   combinatorial theory (Proc. Internat. Sympos., Colorado State Univ., Fort Collins, Colo., 1971)
>   (1973), 117-138.
> - [Er80] Erdős, Paul, _A survey of problems in combinatorial number theory_. Ann. Discrete Math.
>   (1980), 89-115.
> - [AhKh96] Ahlswede, Rudolf and Khachatrian, Levon H., _Sets of integers with pairwise common
>   divisor and a factor from a specified set of primes_. Acta Arith. (1996), 259--276.

*Quoted from [FormalConjectures/ErdosProblems/534.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/534.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/534](https://www.erdosproblems.com/534).

The file states 1 research or textbook statement: 1 solved.

## `Erdos534.erdos_534`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos534.lean#L39](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos534.lean#L39).

> What is the largest possible subset $A\subseteq\{1,\ldots,N\}$ which contains $N$ such that
> $\mathrm{gcd}(a,b)>1$ for all $a\neq b\in A$?
>
> Erdős conjectured that if $N=q_1^{k_1}\cdots q_r^{k_r}$ (where $q_1\lt \cdots \lt q_r$ are distinct
> primes) then the maximum is achieved by, for some $1\leq j\leq r$, those integers in $[1,N]$
> which are a multiple of at least one of $\{2q_1,\ldots,2q_j,q_1\cdots q_j\}$.
>
> This conjecture was proved by Ahlswede and Khachatrian [AhKh96].

```lean
theorem erdos_534 (N : ℕ) (hN : 2 ≤ N) :
    ∃ q ∈ N.primeFactors, IsAdmissible N (ahlswedeKhachatrian N q) ∧
      maxCard N = (ahlswedeKhachatrian N q).card
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/534.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/534.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/534.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/534.lean)
- [erdosproblems.com/534](https://www.erdosproblems.com/534)
