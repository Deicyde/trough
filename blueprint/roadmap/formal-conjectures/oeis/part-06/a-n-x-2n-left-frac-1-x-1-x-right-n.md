---
declaration: theorem
origin: cited
lean: OeisA103885.conjecture
statement: formalized
---

# $a(n) = [x^{2n}] \left(\frac{1 + x}{1 - x}\right)^n$

> The sequence is given by the combinatorial identity:
> $a(n) = \sum_{k = 0}^n \binom{n}{k} \binom{2n+k-1}{n-1}$
> with $a(0) = 1$.
>
> *References:*
> - [A103885](https://oeis.org/A103885)

*Quoted from [FormalConjectures/OEIS/103885.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103885.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 solved. It also has 5 test statements, counted here but not shown.

## `OeisA103885.conjecture`

Solved: stated here; a Lean proof is at [https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-sol-nk5wh4g0vh3546nm/oeis_a103885_conjecture_0/Submission/Spec.lean#L2587](https://github.com/epoch-research/LeanOpenProblems-results/blob/f02efd9a8c5fc6a735d2a90c33e24f7278ce0ffc/runs/oeis-lite-200usd-sol-nk5wh4g0vh3546nm/oeis_a103885_conjecture_0/Submission/Spec.lean#L2587).

> The recurrence given below can be rewritten in the form
>
> $$(2n+1)(2n+2)P(2,n)a(n+1) - (2n-1)(2n-2)P(2,-n)a(n-1) = Q(2,n^2)a(n),$$
>
> where the polynomial $Q(2,n) = 4(55n^2 - 34n + 3)$ and the polynomial $P(2,n) = 5n^2 - 5n + 1$
> satisfies the symmetry condition $P(2,n) = P(2,1-n)$ and has real zeros.
> More generally, for fixed $m = 1,2,3, \ldots$, we conjecture that the sequence $b(n) := a(mn)$
> satisfies a recurrence of the form
>
> $$( \prod_{k = 1}^{2m} (2mn + k) )P(2m,n)b(n+1) + (-1)^m( \prod_{k = 1}^{2*m} (2mn - k) )
>   P(2m,-n)b(n-1) = Q(2m,n^2)b(n),$$
>
> where the polynomials $P(2m,n)$ and $Q(2m,n)$ have degree $2m$. Conjecturally, the polynomial
> $P(2m,n) = P(2m,1-n)$ and has real zeros in the interval [0, 1].
> The $4m$ zeros of the polynomial $Q(2m,n^2)$ seem to belong to the interval $[-1, 1]$ and
> $4m - 2$ of these zeros appear to be approximated by the rational numbers
> $\pm k/(3m)$, where $1 \le k \le 3m - 2$, $k$ not a multiple of $3$.

```lean
theorem conjecture (m : ℕ) (hm : 1 ≤ m) :
    ∃ (P Q : Polynomial ℝ),
      -- P and Q have degree 2m
      P.degree = (2 * m : ℕ) ∧ Q.degree = (2 * m : ℕ) ∧
      -- The recurrence relation holds for all n >= 1
      (∀ (n : ℕ) (hn : 1 ≤ n),
        (prodFactorPlus m n * P.eval (n : ℝ)) * (aSubsequenceReal m (n + 1)) +

        ((-1 : ℝ) ^ m * prodFactorMinus m n * P.eval (-(n : ℝ))) * (aSubsequenceReal m (n - 1)) =

        (Q.eval ((n : ℝ)^2)) * (aSubsequenceReal m n)) ∧

      -- P symmetry: P(x) = P(1-x)
      (∀ x : ℝ, P.eval x = P.eval (1 - x)) ∧

      -- P has real zeros in [0, 1]: all complex zeros are real and in [0, 1]
      (∀ z : ℂ, (P.map (algebraMap ℝ ℂ)).eval z = 0 → z.im = 0 ∧ z.re ∈ (Set.Icc 0 1)) ∧

      -- Q zero properties: The zeros of Q(x^2) are real and in [-1, 1].
      (∀ z : ℂ, (Q.map (algebraMap ℝ ℂ)).eval (z^2) = 0 → z.im = 0 ∧ z.re ∈ (Set.Icc (-1) 1))
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/OEIS/103885.lean, line 100](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103885.lean#L100).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/OEIS/103885.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/OEIS/103885.lean)
- [A103885](https://oeis.org/A103885)
