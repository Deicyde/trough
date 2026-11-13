---
declaration: theorem
origin: cited
lean: OeisA1359.conjecture
statement: formalized
---

# Lesser of twin primes

> Primes $p$ such that $p+2$ is also prime.
>
> *References:*
> - [A001359](https://oeis.org/A001359)

*Quoted from [FormalConjectures/OEIS/1359.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1359.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA1359.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/robzilla1738/formal-conjectures/blob/c7de1452e5b9b8165a30466637b83f7fedfb95fe/FormalConjectures/OEIS/1359.lean#L589](https://github.com/robzilla1738/formal-conjectures/blob/c7de1452e5b9b8165a30466637b83f7fedfb95fe/FormalConjectures/OEIS/1359.lean#L589).

> Primes $p_k$ such that $p_k! \equiv 1 \pmod{p_{k+1}}$ with the exception of $p_{991} = 7841$ and
> other unknown primes $p_k$ for which $(p_k+1)(p_k+2)\cdots(p_{k+1}-2) \equiv 1 \pmod{p_{k+1}}$
> where $p_{k+1} - p_k > 2$.
>
> A formal proof is hosted at the `formal_proof` link: a Wilson-theorem argument with a
> fixed-divisor trial-division sieve and a verified length-7840 certificate.

```lean
theorem conjecture (k : ℕ) (hk : k > 1) :
    let Pk := Nat.nth Nat.Prime (k - 1)
    let Pk_succ := Nat.nth Nat.Prime k
    let Congruence := Pk.factorial ≡ 1 [MOD Pk_succ]
    let IsLesserTwinPrime := (Pk + 2).Prime
    let Wk_prod : ℕ := ∏ i ∈ Finset.Icc (Pk + 1) (Pk_succ - 2), i
    Congruence ↔ (IsLesserTwinPrime ∨ (k = 991) ∨ (Pk_succ - Pk > 2 ∧ Wk_prod ≡ 1 [MOD Pk_succ]))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/1359.lean, line 80](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1359.lean#L80).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/1359.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/1359.lean)
- [A001359](https://oeis.org/A001359)
