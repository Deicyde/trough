---
declaration: theorem
origin: cited
lean: Erdos1183.erdos_1183.parts.i, Erdos1183.erdos_1183.parts.ii, Erdos1183.erdos_1183.parts.iii, Erdos1183.erdos_1183.variants.f_ge
statement: formalized
---

# Erdős Problem 1183

> *References:*
> - [erdosproblems.com/1183](https://www.erdosproblems.com/1183)
> - [Er78] Erdős, P., *Problems and results in combinatorial analysis and combinatorial number
>   theory*. Proceedings of the Ninth Southeastern Conference on Combinatorics, Graph Theory, and
>   Computing (Florida Atlantic Univ., Boca Raton, Fla., 1978) (1978), 29-40.
>   [PDF](https://www.renyi.hu/~p_erdos/1978-36.pdf)

*Quoted from [FormalConjectures/ErdosProblems/1183.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1183](https://www.erdosproblems.com/1183).

The file states 4 research or textbook statements: 3 open and 1 textbook result.

## `Erdos1183.erdos_1183.parts.i`

Open: stated without proof.

> Let $f(n)$ be maximal such that in any $2$-colouring of the subsets of $\{1,\ldots,n\}$ there is
> always a monochromatic family of at least $f(n)$ sets which is closed under taking unions and
> intersections. Estimate $f(n)$.
>
> Let $F(n)$ be defined similarly, except that we only require the family be closed under taking
> unions. Estimate $F(n)$. In particular, is it true that $F(n)\geq n^{\omega(n)}$ for some
> $\omega(n)\to \infty$ as $n\to \infty$, and $F(n)<(1+o(1))^n$?
>
> This is the first part, a problem of Erdős and Ulam [Er78, p. 39]. We read "estimate" as
> $f(n)=\Theta(\text{answer})$.

```lean
theorem erdos_1183.parts.i :
    (fun n : ℕ ↦ (f n : ℝ)) =Θ[atTop] erdos_1183.parts.i.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1183.lean, line 74](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean#L74).

## `Erdos1183.erdos_1183.parts.ii`

Open: stated without proof.

> Let $f(n)$ be maximal such that in any $2$-colouring of the subsets of $\{1,\ldots,n\}$ there is
> always a monochromatic family of at least $f(n)$ sets which is closed under taking unions and
> intersections. Estimate $f(n)$.
>
> Let $F(n)$ be defined similarly, except that we only require the family be closed under taking
> unions. Estimate $F(n)$. In particular, is it true that $F(n)\geq n^{\omega(n)}$ for some
> $\omega(n)\to \infty$ as $n\to \infty$, and $F(n)<(1+o(1))^n$?
>
> This is the second part. We read "estimate" as $F(n)=\Theta(\text{answer})$.

```lean
theorem erdos_1183.parts.ii :
    (fun n : ℕ ↦ (F n : ℝ)) =Θ[atTop] erdos_1183.parts.ii.answer
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1183.lean, line 92](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean#L92).

## `Erdos1183.erdos_1183.parts.iii`

Open: stated without proof.

> Let $f(n)$ be maximal such that in any $2$-colouring of the subsets of $\{1,\ldots,n\}$ there is
> always a monochromatic family of at least $f(n)$ sets which is closed under taking unions and
> intersections. Estimate $f(n)$.
>
> Let $F(n)$ be defined similarly, except that we only require the family be closed under taking
> unions. Estimate $F(n)$. In particular, is it true that $F(n)\geq n^{\omega(n)}$ for some
> $\omega(n)\to \infty$ as $n\to \infty$, and $F(n)<(1+o(1))^n$?
>
> This is the third part, the "in particular" question: both conjuncts must hold. We state it as
> printed in [Er78, p. 39]: $F(n) > n^c$ for every $c$ if $n > n_0(c)$, and
> $F(n) < (1+\varepsilon)^n$ for every $\varepsilon > 0$ if $n > n_0(\varepsilon)$.

```lean
theorem erdos_1183.parts.iii :
    (∀ c : ℝ, ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ c < (F n : ℝ)) ∧
      ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, (F n : ℝ) < (1 + ε) ^ n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1183.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean#L110).

## `Erdos1183.erdos_1183.variants.f_ge`

Textbook result, stated without proof.

> It is trivial that $f(n)\geq \frac{n+1}{2}$, since there is a sequence of $n+1$ many nested
> subsets.

```lean
theorem erdos_1183.variants.f_ge (n : ℕ) : ((n : ℝ) + 1) / 2 ≤ (f n : ℝ)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1183.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean#L120).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1183.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1183.lean)
- [erdosproblems.com/1183](https://www.erdosproblems.com/1183)
