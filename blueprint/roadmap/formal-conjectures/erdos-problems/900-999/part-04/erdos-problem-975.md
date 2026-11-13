---
declaration: theorem
origin: cited
lean: Erdos975.erdos_975, Erdos975.erdos_975.variants.upper_bound, Erdos975.erdos_975.variants.lower_bound, Erdos975.erdos_975.variants.quadratic, Erdos975.erdos_975.variants.n2_plus_1_strong, Erdos975.erdos_975.variants.n2_plus_1
statement: formalized
---

# Erdős Problem 975

> *References:*
>  - [erdosproblems.com/975](https://www.erdosproblems.com/975)
>  - [Va39] van der Corput, J. G., Une in\'egalit\'e{} relative au nombre des diviseurs. Nederl. Akad. Wetensch., Proc. (1939), 547--553.
>  - [Er52b] Erd\"os, P., On the sum {$\sum^x_{k=1} d(f(k))$}. J. London Math. Soc. (1952), 7--15.
>  - [Ho63] Hooley, Christopher, On the number of divisors of a quadratic polynomial. Acta Math. (1963), 97--114.
>  - [Mc95] McKee, James, On the average number of divisors of quadratic polynomials. Math. Proc. Cambridge Philos. Soc. (1995), 389--392.
>  - [Mc97] McKee, James, A note on the number of divisors of quadratic polynomials. (1997), 275--281.
>  - [Mc99] McKee, James, The average number of divisors of an irreducible quadratic polynomial. Math. Proc. Cambridge Philos. Soc. (1999), 17--22.
>  - [T] T. Tao, Erdos' divisor bound, https://terrytao.wordpress.com/2011/07/23/erdos-divisor-bound/

*Quoted from [FormalConjectures/ErdosProblems/975.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/975](https://www.erdosproblems.com/975).

The file states 6 research or textbook statements: 1 open and 5 solved.

## `Erdos975.erdos_975`

Open: stated without proof.

> For an irreducible polynomial $f \in \mathbb{Z}[x]$ with $f(n) \ge 1$ for sufficiently large $n$,
> does there exists a constant $c = c(f) > 0$ such that
> $\sum_{n \le x} \tau(f(n)) \approx c \cdot x \log x$?
>
> Note that it is unclear whether the polynomial should have integer coefficients or merely be
> integer-valued. We assume the former.

```lean
theorem erdos_975 :
    ∀ f : ℤ[X], f.natDegree ≠ 0 → Irreducible f → (∀ᶠ n in atTop, 1 ≤ f.eval n) →
    ∃ c > (0 : ℝ), Tendsto (fun x ↦ Erdos975Sum f x / (x * log x)) atTop (𝓝 c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 58](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L58).

## `Erdos975.erdos_975.variants.upper_bound`

Solved: stated here without proof.

> The correctness of the growth rate is shown in [Va39] (lower bound) and [Er52b] (upper bound).

```lean
theorem erdos_975.variants.upper_bound (f : ℤ[X]) (hf : Irreducible f)
    (hf_pos : ∀ᶠ n in atTop, 1 ≤ f.eval n) : Erdos975Sum f =O[atTop] (fun x ↦ x * log x)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 67](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L67).

## `Erdos975.erdos_975.variants.lower_bound`

Solved: stated here without proof.

> Lower bound for the growth rate of `Erdos975Sum`, shown in [Va39].

```lean
theorem erdos_975.variants.lower_bound (f : ℤ[X]) (hf : Irreducible f) (hfdeg : f.natDegree ≠ 0)
    (hf_pos : ∀ᶠ n in atTop, 1 ≤ f.eval n) :
    (fun x ↦ x * log x) =O[atTop] Erdos975Sum f
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 73](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L73).

## `Erdos975.erdos_975.variants.quadratic`

Solved: stated here without proof.

> When $f$ is an irreducible quadratic polynomial, the question is answered first by Hooley [Ho63].
> More compact expression of the constant in terms of Hurwitz class numbers (when $a = 1$)
> is given by McKey in [Mc95], [Mc97], [Mc99].
>
> TODO: formalize Hurwitz class numbers and the expression of the constant in terms of them.

```lean
theorem erdos_975.variants.quadratic (f : ℤ[X]) (hf : Irreducible f)
    (hf_pos : ∀ᶠ n : ℕ in atTop, 1 ≤ f.eval ↑n) (hf_degree : f.degree = 2) (c : ℝ) :
    c = erdos_975.variants.quadratic.answer → 0 < c ∧ Tendsto
      (fun x ↦ Erdos975Sum f x / (x * log x)) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L90).

## `Erdos975.erdos_975.variants.n2_plus_1_strong`

Solved: stated here without proof.

> More concrete example for $f(n) = n^2 + 1$, where the asymptote is
> $\sum_{n \le x} \tau(n^2 + 1) \sim \frac{3}{\pi} x \log x + O(x)$. See Tao's blog [T].

```lean
theorem erdos_975.variants.n2_plus_1_strong :
    (fun x ↦ Erdos975Sum (X ^ 2 + 1) x - (3 / π) * x * log x) =O[atTop] id
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L101).

## `Erdos975.erdos_975.variants.n2_plus_1`

Solved: stated here without proof.

> Asymptotics for `Erdos975Sum` with $f(X) = X^2 + 1$.

```lean
theorem erdos_975.variants.n2_plus_1 :
    ∃ c > (0 : ℝ), Tendsto (fun x ↦ Erdos975Sum (X ^ 2 + 1) x / (x * log x)) atTop (𝓝 c)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/975.lean, line 107](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean#L107).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/975.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/975.lean)
- [erdosproblems.com/975](https://www.erdosproblems.com/975)
