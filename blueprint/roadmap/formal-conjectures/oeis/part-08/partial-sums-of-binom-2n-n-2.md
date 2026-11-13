---
declaration: theorem
origin: cited
lean: OeisA115257.conjecture
statement: formalized
---

# Partial sums of $\binom{2n}{n}^2$

> $$a(n) = \sum_{k=0}^n \binom{2k}{k}^2$$
>
> *References:*
> - [A115257](https://oeis.org/A115257)

*Quoted from [FormalConjectures/OEIS/115257.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/115257.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 4 test statements, counted here but not shown.

## `OeisA115257.conjecture`

Open: stated without proof.

> Conjecture: For any positive integer n, the polynomials Sum_{k=0}^n binomial(2k,k)^2*x^k
> and Sum_{k=0}^n binomial(2k,k)^2*x^k/(k+1) are irreducible over the field of rational numbers.
> - Zhi-Wei Sun, Mar 23 2013

```lean
theorem conjecture :
  ∀ (n : ℕ), 1 ≤ n → Irreducible (polyP n) ∧ Irreducible (polyQ n)
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/115257.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/115257.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/115257.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/115257.lean)
- [A115257](https://oeis.org/A115257)
