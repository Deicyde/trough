---
declaration: theorem
origin: cited
lean: AlgebraicNormality.irrational_algebraic_absolutely_normal, AlgebraicNormality.irrational_algebraic_normal_in_some_base
statement: formalized
---

# Normality of Irrational Algebraic Numbers

> It is unknown whether every irrational algebraic real number is normal in any integer base.
> Here a real number is *normal in base* $b$ if, for every $k \ge 1$, every string of $k$ digits
> appears in its base-$b$ expansion with asymptotic frequency $1/b^k$.
> The stronger conjecture that every irrational algebraic real number is absolutely normal is stated
> separately: normality in one base and normality in every base are not equivalent definitions.
>
> In a 1950 note on the decimal digits of $\sqrt{2}$, Borel [Bor50] conjectured that every
> irrational algebraic number is normal in every base. This was the first publication to address
> the expansion of an irrational algebraic number [AB07].
>
> For the characterisation of normality by uniform distribution modulo $1$, see
> `FormalConjectures/Books/BugeaudDistributionModuloOne/NormalAndRich.lean`.
>
> *References:*
> - [Wikipedia: Normal number](https://en.wikipedia.org/wiki/Normal_number)
> - [Bor50] Borel, Émile. "Sur les chiffres décimaux de $\sqrt{2}$ et divers problèmes de
>   probabilités en chaîne." C. R. Acad. Sci. Paris 230 (1950): 591-593.
> - [AB07] Adamczewski, Boris, and Yann Bugeaud. "On the complexity of algebraic numbers I.
>   Expansions in integer bases." Annals of Mathematics 165.2 (2007): 547-565.
> - [BC01] Bailey, David H., and Richard E. Crandall. "On the random character of fundamental constant
>   expansions." Experimental Mathematics 10.2 (2001): 175-190.
>   https://projecteuclid.org/journals/experimental-mathematics/volume-10/issue-2/On-the-random-character-of-fundamental-constant-expansions/em/999188630.full

*Quoted from [FormalConjectures/Wikipedia/AlgebraicNormality.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlgebraicNormality.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 2 research or textbook statements: 2 open. It also has 1 API statement, counted here but not shown.

## `AlgebraicNormality.irrational_algebraic_absolutely_normal`

Open: stated without proof.

> Borel's normality conjecture [Bor50]: every irrational algebraic real is absolutely normal.

```lean
theorem irrational_algebraic_absolutely_normal :
    ∀ x : ℝ, IsIrrationalAlgebraic x → IsAbsolutelyNormal x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [41 Approximations and expansions](../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/Wikipedia/AlgebraicNormality.lean, line 59](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlgebraicNormality.lean#L59).

## `AlgebraicNormality.irrational_algebraic_normal_in_some_base`

Open: stated without proof.

> The weaker normality conjecture: every irrational algebraic real is normal in at least one
> integer base `b ≥ 2`.

```lean
theorem irrational_algebraic_normal_in_some_base :
    ∀ x : ℝ, IsIrrationalAlgebraic x → ∃ b : ℕ, 2 ≤ b ∧ IsNormalInBase b x
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [12 Field theory and polynomials](../../by-subject/part-01/12-field-theory-and-polynomials/README.md), [41 Approximations and expansions](../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/Wikipedia/AlgebraicNormality.lean, line 66](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlgebraicNormality.lean#L66).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/AlgebraicNormality.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/AlgebraicNormality.lean)
- [Wikipedia: Normal number](https://en.wikipedia.org/wiki/Normal_number)
