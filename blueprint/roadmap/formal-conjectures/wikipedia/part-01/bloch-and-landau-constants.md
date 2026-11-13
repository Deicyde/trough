---
declaration: theorem
origin: cited
lean: Bloch.blochConstant_lower_bound, Bloch.blochConstant_upper_bound, Bloch.blochConstant_exact_value, Bloch.univalentBlochConstant_lower_bound, Bloch.univalentBlochConstant_upper_bound, Bloch.landauConstant_lower_bound, Bloch.landauConstant_upper_bound, Bloch.landauConstant_exact_value
statement: formalized
---

# Bloch and Landau constants

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Bloch%27s_theorem_(complex_analysis))
> - [CP96] Chen, H., Gauthier, P. M. "On Bloch's constant." Journal d'Analyse Mathématique 69 (1996),
>   275–291.
> - [AG37] Ahlfors, L. V., Grunsky, H. "Über die Blochsche Konstante." Mathematische Zeitschrift 42
>   (1937), 671–673.
> - [Ya95] Yanagihara, H. "On the locally univalent Bloch constant." Journal d'Analyse Mathématique
>   65 (1995), 1–17.
> - [Ra43] Rademacher, H. "On the Bloch-Landau Constant."" American Journal of Mathematics 65 (1943),
>   387–390.
> - [OptimizationConstants](https://teorth.github.io/optimizationproblems/constants/57c.html)
> - [Skin2009] Skinner, Brian. The univalent Bloch constant problem. Complex Variables and Elliptic
>   Equations 54 (2009), no. 10, 951–955.
> - [MathWorld](https://mathworld.wolfram.com/BlochConstant.html)
> - [Bhowmik–Sen](https://www.cambridge.org/core/journals/canadian-mathematical-bulletin/article/improved-bloch-and-landau-constants-for-meromorphic-functions/FD465D1F2CEF7E8C62AFF16C3E89B7B4)
> - [Re2008] Rettinger, R. ["Bloch's constant is computable."](https://jucs.org/jucs_14_6/blochs_constant_is_computable/jucs_14_06_0896_0907_rettinger.pdf)
>   Journal of Universal Computer Science 14 (2008), 896–907. In particular, a schlicht disk is the
>   image of a subdomain under a biholomorphic restriction.

*Quoted from [FormalConjectures/Wikipedia/Bloch.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 8 research or textbook statements: 2 open and 6 solved. It also has 4 API statements, counted here but not shown.

## `Bloch.blochConstant_lower_bound`

Solved: stated here without proof.

> It is proved in [CP96] that the Bloch constant is bounded below by
> $\sqrt{3}/4 + 2 \times 10^{-4}$

```lean
theorem blochConstant_lower_bound : Real.sqrt 3 / 4 + 2 * 10 ^ (-4 : ℤ) ≤ blochConstant
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L136).

## `Bloch.blochConstant_upper_bound`

Solved: stated here without proof.

> It is proved in [AG37] that the Bloch constant is bounded above by
> $\frac{1}{\sqrt{1 + \sqrt{3}}}\frac{\Gamma(1/3) \Gamma(11/12)}{\Gamma(1/4)}$.

```lean
theorem blochConstant_upper_bound :
    blochConstant ≤ Real.Gamma (1 / 3) * Real.Gamma (11 / 12) /
    (Real.Gamma (1 / 4) * Real.sqrt (1 + Real.sqrt 3))
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 142](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L142).

## `Bloch.blochConstant_exact_value`

Open: stated without proof.

> Ahlfors and Grunsky also conjectured in [AG37] that this upper bound is the precise value of the
> Bloch constant.

```lean
theorem blochConstant_exact_value :
    blochConstant = Real.Gamma (1 / 3) * Real.Gamma (11 / 12) /
    (Real.Gamma (1 / 4) * Real.sqrt (1 + Real.sqrt 3))
```

Category `research open`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 150](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L150).

## `Bloch.univalentBlochConstant_lower_bound`

Solved: stated here without proof.

> It is proved in [Skin2009] that the Univalent Bloch constant is bounded below by $0.5708858$.

```lean
theorem univalentBlochConstant_lower_bound : 0.5708858 ≤ univalentBlochConstant
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L166).

## `Bloch.univalentBlochConstant_upper_bound`

Proved here.

> The Univalent Bloch constant is trivially bounded above by the Bloch radius of the identity
> function, which is $1$. This is the best upper bound we know according to [OptimizationConstants].

```lean
theorem univalentBlochConstant_upper_bound : univalentBlochConstant ≤ 1
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 172](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L172).

## `Bloch.landauConstant_lower_bound`

Solved: stated here without proof.

> It is proved in [Ya95] that the Landau constant is bounded below by $0.5 + 10 ^ {-335}$.

```lean
theorem landauConstant_lower_bound : 0.5 + 10 ^ (-335 : ℤ) ≤ landauConstant
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 194](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L194).

## `Bloch.landauConstant_upper_bound`

Solved: stated here without proof.

> It is proved in [Ra43] that the Landau constant is bounded above by
> $\frac{1}{\sqrt{1 + \sqrt{3}}}\frac{\Gamma(1/3) \Gamma(5/6)}{\Gamma(1/6)}$.

```lean
theorem landauConstant_upper_bound :
    landauConstant ≤ Real.Gamma (1 / 3) * Real.Gamma (5 / 6) / Real.Gamma (1 / 6)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L200).

## `Bloch.landauConstant_exact_value`

Open: stated without proof.

> In [Ra43], Rademacher says that he strongly believed that this upper bound is the precise value
> of the Landau constant.

```lean
theorem landauConstant_exact_value :
    landauConstant = Real.Gamma (1 / 3) * Real.Gamma (5 / 6) / Real.Gamma (1 / 6)
```

Category `research open`; AMS [30 Functions of a complex variable](../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/Wikipedia/Bloch.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean#L207).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/Bloch.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/Bloch.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Bloch%27s_theorem_%28complex_analysis%29)
