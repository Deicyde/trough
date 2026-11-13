---
declaration: theorem
origin: cited
lean: OeisA363347.exists_a_eq_prime
statement: formalized
---

# Realization of primes $p \equiv \pm 1 \pmod{10}$ by continued fraction denominators

> $a(n)$ is the denominator of the finite continued fraction
>
> $$\frac{1}{2 - \frac{3}{3 - \frac{4}{4 - \frac{5}{\dots - \frac{n-1}{(n-1) - \frac{n}{-4}}}}}}$$
>
> *References:*
> - [A363347](https://oeis.org/A363347)
> - [arxiv/2605.22763](https://arxiv.org/abs/2605.22763) *Advancing Mathematics Research with AI-Driven Formal Proof Search* by George Tsoukalas et al.

*Quoted from [FormalConjectures/OEIS/363347.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/363347.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA363347.exists_a_eq_prime`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/363347.wip.lean#L825](https://github.com/mo271/formal-conjectures/blob/a32396489dcb8f86c3549b93aa358ac6a10a3a1f/FormalConjectures/OEIS/363347.wip.lean#L825).

> Conjecture: The sequence contains all prime numbers which end with a 1 or 9 (i.e., primes $p \equiv 1$ or $9 \pmod{10}$).
>
> A formal proof has been found with the methods described in
> [arxiv/2605.22763](https://arxiv.org/abs/2605.22763).

```lean
theorem exists_a_eq_prime :
    ∀ p : ℕ, (p.Prime ∧ (p ≡ 1 [MOD 10] ∨ p ≡ 9 [MOD 10])) → ∃ n : ℕ, a n = p
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/363347.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/363347.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/363347.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/363347.lean)
- [A363347](https://oeis.org/A363347)
