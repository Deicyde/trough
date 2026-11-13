---
declaration: theorem
origin: cited
lean: HasseWeil.exists_hasMeromorphicContinuation, HasseWeil.exists_hasAnalyticContinuation, HasseWeil.exists_hasAnalyticContinuation_rat
statement: formalized
---

# The Hasse--Weil conjecture for elliptic curves

> The $L$-series $L(E, s)$ of an elliptic curve $E$ over a number field converges absolutely on
> $\operatorname{Re} s > 3/2$ ([Tate1966], p. 416; [Gross2011], Lecture 2, §1). The **Hasse--Weil
> conjecture** predicts that it has an analytic continuation to the whole complex plane and satisfies
> a functional equation ([Tate1966], p. 416; [Gross2011], Conjecture 2.7, stated there for the
> completed $L$-function). Only the continuation is stated here. Over $\mathbb{Q}$ it follows from
> the modularity theorem.
>
> [Wikipedia] states the conjecture for the Hasse--Weil zeta function and asks only for a
> meromorphic continuation, which is equivalent to a meromorphic continuation of $L(E, s)$. That
> weaker form is the one the Birch and Swinnerton-Dyer conjecture rests on, so it is recorded here as
> well. [Gross2011], Conjecture 2.10 takes it as a hypothesis, and only near $s = 1$. The
> formulation of the Birch and Swinnerton-Dyer conjecture in `FormalConjectures/Millennium/BSD.lean`
> instead asserts a global meromorphic continuation, so it implies
> `exists_hasMeromorphicContinuation` below.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Hasse%E2%80%93Weil_zeta_function#Hasse%E2%80%93Weil_conjecture)
> - [Tate1966] John Tate. "On the conjectures of Birch and Swinnerton-Dyer and a geometric analog."
>   Seminaire Bourbaki, Vol. 9, Exp. No. 306 (1966), 415-440,
>   [numdam](https://www.numdam.org/item/SB_1964-1966__9__415_0/)
> - [Gross2011] Benedict H. Gross. "Lectures on the conjecture of Birch and Swinnerton-Dyer."
>   Arithmetic of L-functions, IAS/Park City Math. Ser. 18, AMS (2011), 169-209,
>   [math.harvard.edu](https://people.math.harvard.edu/~gross/preprints/lectures-pcmi.pdf)

*Quoted from [FormalConjectures/Wikipedia/HasseWeil.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HasseWeil.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 3 research or textbook statements: 2 open and 1 solved. It also has 2 API statements, counted here but not shown.

## `HasseWeil.exists_hasMeromorphicContinuation`

Open: stated without proof.

> The $L$-series of an elliptic curve over a number field has a meromorphic continuation to
> $\mathbb{C}$. This is the **Hasse--Weil conjecture** in the form stated in [Wikipedia], and a weak
> form of [Gross2011], Conjecture 2.7. It is also what the Birch and Swinnerton-Dyer conjecture rests
> on, as the hypothesis of [Gross2011], Conjecture 2.10.

```lean
theorem exists_hasMeromorphicContinuation (E : WeierstrassCurve K) [E.IsElliptic] :
    ∃ L, HasMeromorphicContinuation E L
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/HasseWeil.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HasseWeil.lean#L95).

## `HasseWeil.exists_hasAnalyticContinuation`

Open: stated without proof.

> The **Hasse--Weil conjecture** ([Tate1966], p. 416; [Gross2011], Conjecture 2.7): the
> $L$-series of an elliptic curve over a number field has an analytic continuation to $\mathbb{C}$.

```lean
theorem exists_hasAnalyticContinuation (E : WeierstrassCurve K) [E.IsElliptic] :
    ∃ L, HasAnalyticContinuation E L
```

Category `research open`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/HasseWeil.lean, line 103](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HasseWeil.lean#L103).

## `HasseWeil.exists_hasAnalyticContinuation_rat`

Solved: stated here without proof.

> The **Hasse--Weil conjecture** over $\mathbb{Q}$: the $L$-series of an elliptic curve over
> $\mathbb{Q}$ has an analytic continuation to $\mathbb{C}$. This follows from the modularity
> theorem, see [Wikipedia].

```lean
theorem exists_hasAnalyticContinuation_rat (E : WeierstrassCurve ℚ) [E.IsElliptic] :
    ∃ L, HasAnalyticContinuation E L
```

Category `research solved`; AMS [11 Number theory](../../by-subject/part-01/11-number-theory/README.md), [14 Algebraic geometry](../../by-subject/part-01/14-algebraic-geometry/README.md). Declared in [FormalConjectures/Wikipedia/HasseWeil.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HasseWeil.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/HasseWeil.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/HasseWeil.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Hasse%E2%80%93Weil_zeta_function#Hasse%E2%80%93Weil_conjecture)
