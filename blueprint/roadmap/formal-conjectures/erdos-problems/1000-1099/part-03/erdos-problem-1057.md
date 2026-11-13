---
declaration: theorem
origin: cited
lean: Erdos1057.erdos_1057, Erdos1057.erdos_1057.variants.upper_bound, Erdos1057.erdos_1057.variants.pomerance, Erdos1057.erdos_1057.variants.agp_infinite, Erdos1057.erdos_1057.variants.agp_lower_bound, Erdos1057.erdos_1057.variants.harman_lower_bound, Erdos1057.erdos_1057.variants.lichtman_lower_bound
statement: formalized
---

# Erdős Problem 1057

> *References:*
> - [erdosproblems.com/1057](https://www.erdosproblems.com/1057)
> - [AGP94] Alford, W. R. and Granville, Andrew and Pomerance, Carl, There are infinitely many
>   Carmichael numbers. Ann. of Math. (2) (1994), 703--722.
> - [Er56c] Erdős, P., On pseudoprimes and Carmichael numbers. Publ. Math. Debrecen (1956),
>   201--206.
> - [Gu04] Guy, Richard K., Unsolved problems in number theory. (2004), xviii+437.
> - [Ha08] Harman, Glyn, Watt's mean value theorem and Carmichael numbers. Int. J. Number Theory
>   (2008), 241--248.
> - [Li22] J. D. Lichtman, Primes in arithmetic progressions to large moduli and shifted primes
>   without large prime factors. arXiv:2211.09641 (2022).
> - [Po89] Pomerance, Carl, Two methods in elementary analytic number theory. (1989), 135--161.

*Quoted from [FormalConjectures/ErdosProblems/1057.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1057](https://www.erdosproblems.com/1057).

The file states 7 research or textbook statements: 2 open and 5 solved.

## `Erdos1057.erdos_1057`

Open: stated without proof.

> Is it true that $C(x)=x^{1-o(1)}$?
>
> This is discussed in problem A13 of Guy's collection [Gu04].

```lean
theorem erdos_1057 :
    Tendsto (fun x ↦ Real.log (carmichaelCounting x) / Real.log x) atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L57).

## `Erdos1057.erdos_1057.variants.upper_bound`

Solved: stated here without proof.

> Erdős [Er56c] proved $C(x) < x \exp\left(-c \frac{\log x\log\log\log x}{\log\log x}\right)$
> for some constant $c>0$.

```lean
theorem erdos_1057.variants.upper_bound :
    ∃ c > 0, ∀ᶠ x in atTop,
      carmichaelCounting x < x * Real.exp (-c * (Real.log x * Real.log (Real.log (Real.log x))) /
        Real.log (Real.log x))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L66).

## `Erdos1057.erdos_1057.variants.pomerance`

Open: stated without proof.

> Pomerance [Po89] gave a heuristic suggesting that this is the true order of growth, and in fact
> $C(x)= x \exp\left(-(1+o(1))\frac{\log x\log\log\log x}{\log\log x}\right)$.

```lean
theorem erdos_1057.variants.pomerance :
    Tendsto (fun x ↦
      -(Real.log (carmichaelCounting x / x) * Real.log (Real.log x)) /
      (Real.log x * Real.log (Real.log (Real.log x)))) atTop (𝓝 1)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L77).

## `Erdos1057.erdos_1057.variants.agp_infinite`

Solved: stated here without proof.

> Alford, Granville, and Pomerance [AGP94] proved that $C(x)\to \infty$.

```lean
theorem erdos_1057.variants.agp_infinite :
    Tendsto carmichaelCounting atTop atTop
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 87](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L87).

## `Erdos1057.erdos_1057.variants.agp_lower_bound`

Solved: stated here without proof.

> Alford, Granville, and Pomerance [AGP94] proved that $C(x)>x^{2/7}$ for large $x$.

```lean
theorem erdos_1057.variants.agp_lower_bound :
    ∀ᶠ x in atTop, carmichaelCounting x > x ^ (2 / 7 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L95).

## `Erdos1057.erdos_1057.variants.harman_lower_bound`

Solved: stated here without proof.

> The lower bound $C(x)> x^{0.33336704}$ was proved by Harman [Ha08].

```lean
theorem erdos_1057.variants.harman_lower_bound :
    ∀ᶠ x in atTop, carmichaelCounting x > x ^ (0.33336704 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L103).

## `Erdos1057.erdos_1057.variants.lichtman_lower_bound`

Solved: stated here without proof.

> This exponent was improved to $0.3389$ by Lichtman [Li22].

```lean
theorem erdos_1057.variants.lichtman_lower_bound :
    ∀ᶠ x in atTop, carmichaelCounting x > x ^ (0.3389 : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1057.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean#L111).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1057.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1057.lean)
- [erdosproblems.com/1057](https://www.erdosproblems.com/1057)
