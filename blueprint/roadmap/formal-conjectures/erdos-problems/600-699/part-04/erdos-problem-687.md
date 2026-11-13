---
declaration: theorem
origin: cited
lean: Erdos687.erdos_687.parts.i, Erdos687.erdos_687.parts.ii, Erdos687.erdos_687.parts.iii, Erdos687.erdos_687.variants.iwaniec, Erdos687.erdos_687.variants.fgkmt, Erdos687.erdos_687.variants.maier_pomerance
statement: formalized
---

# Erdős Problem 687

> *References:*
> - [erdosproblems.com/687](https://www.erdosproblems.com/687)
> - [Ben Green's Open Problem 46](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.46):
>   the same question; see `Green46` in `FormalConjectures.GreensOpenProblems.«46»`.
> - [OEIS A058989](https://oeis.org/A058989): the values $Y(p_n)$, where $p_n$ is the $n$-th prime.
> - [OEIS A048670](https://oeis.org/A048670): Jacobsthal's function of $\prod_{p \leq p_n} p$,
>   which is $Y(p_n) + 1$.
> - [Er79d] Erdős, P., *Some unconventional problems in number theory*. Acta Math. Acad. Sci.
>   Hungar. 33 (1979), 71-80.
> - [Er80] Erdős, Paul, *A survey of problems in combinatorial number theory*. Ann. Discrete Math.
>   6 (1980), 89-115.
> - [Er96b] Erdős, Paul, *Some problems I presented or planned to present in my short talk*.
>   Analytic number theory, Vol. 1 (Allerton Park, IL, 1995), Progr. Math. 138 (1996), 333-335.
> - [Iw78] Iwaniec, Henryk, *On the problem of Jacobsthal*. Demonstratio Math. 11 (1978), 225-232.
>   [doi:10.1515/dema-1978-0121](https://doi.org/10.1515/dema-1978-0121)
> - [MaPo90] Maier, Helmut and Pomerance, Carl, *Unusually large gaps between consecutive primes*.
>   Trans. Amer. Math. Soc. 322 (1990), 201-237.
> - [FGKMT18] Ford, Kevin and Green, Ben and Konyagin, Sergei and Maynard, James and Tao, Terence,
>   *Long gaps between primes*. J. Amer. Math. Soc. 31 (2018), 65-105.
>   [arXiv:1412.5029](https://arxiv.org/abs/1412.5029)
> - [OAI26a] OpenAI, *A quadratic bound for Jacobsthal's function*. OpenAI Math Release preprint
>   (2026).
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-quadratic-bound-for-Jacobsthals-function-September-25-2026/paper.pdf

*Quoted from [FormalConjectures/ErdosProblems/687.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/687](https://www.erdosproblems.com/687).

The file states 6 research or textbook statements: 3 open and 3 solved. It also has 4 test statements, counted here but not shown.

## `Erdos687.erdos_687.parts.i`

Open: stated without proof.

> Let $Y(x)$ be the maximal $y$ such that there exists a choice of congruence classes $a_p$ for
> all primes $p\leq x$ such that every integer in $[1,y]$ is congruent to at least one of the
> $a_p\pmod{p}$. Give good estimates for $Y(x)$.
>
> We formalise this as determining $Y(x)$ up to constant factors.

```lean
theorem erdos_687.parts.i :
    (fun x : ℕ ↦ (Y x : ℝ)) =Θ[atTop] erdos_687.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 164](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L164).

## `Erdos687.erdos_687.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/30k30/scholia/blob/b072c89c3edac06521868e32cc15b2bc91bd8533/erdos-687/glue/JacobsthalTo687.lean#L325](https://github.com/30k30/scholia/blob/b072c89c3edac06521868e32cc15b2bc91bd8533/erdos-687/glue/JacobsthalTo687.lean#L325).

> In particular, can one prove that $Y(x)=o(x^2)$?
>
> Yes: an internal OpenAI model proved $h(k) \ll k^2$ for Jacobsthal's function $h$ [OAI26a]
> (see `Erdos970.erdos_970`). Since $Y(x) + 1$ is Jacobsthal's function of $\prod_{p \leq x} p$,
> which has $\pi(x) \ll x/\log x$ prime factors, this gives $Y(x) \ll x^2/(\log x)^2$.
> The linked Lean proof is by 30k30, from the bound of [OAI26a].

```lean
theorem erdos_687.parts.ii :
    (fun x : ℕ ↦ (Y x : ℝ)) =o[atTop] (fun x : ℕ ↦ (x : ℝ) ^ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L179).

## `Erdos687.erdos_687.parts.iii`

Open: stated without proof.

> Or, even stronger, can one prove that $Y(x)\ll x^{1+o(1)}$?
>
> We read $Y(x)\ll x^{1+o(1)}$ as $Y(x) = O(x^{1+\varepsilon})$ for every fixed
> $\varepsilon > 0$.

```lean
theorem erdos_687.parts.iii :
    ∀ ε > (0 : ℝ), (fun x : ℕ ↦ (Y x : ℝ)) =O[atTop] (fun x : ℕ ↦ (x : ℝ) ^ (1 + ε))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L190).

## `Erdos687.erdos_687.variants.iwaniec`

Solved: stated here without proof.

> Iwaniec's upper bound for Jacobsthal's function [Iw78] gives $Y(x) \ll x^2$.

```lean
theorem erdos_687.variants.iwaniec :
    (fun x : ℕ ↦ (Y x : ℝ)) =O[atTop] (fun x : ℕ ↦ (x : ℝ) ^ 2)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 198](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L198).

## `Erdos687.erdos_687.variants.fgkmt`

Solved: stated here without proof.

> Ford, Green, Konyagin, Maynard and Tao [FGKMT18] proved
>
> $$Y(x) \gg \frac{x \log x \log\log\log x}{\log\log x}.$$

```lean
theorem erdos_687.variants.fgkmt :
    (fun x : ℕ ↦ (x : ℝ) * Real.log x * Real.log (Real.log (Real.log x)) /
      Real.log (Real.log x)) =O[atTop] (fun x : ℕ ↦ (Y x : ℝ))
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 207](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L207).

## `Erdos687.erdos_687.variants.maier_pomerance`

Open: stated without proof.

> Maier and Pomerance [MaPo90] conjectured that $Y(x) \ll x(\log x)^{2+o(1)}$ (in this form it is
> stated in [FGKMT18]).
>
> We read this as $Y(x) = O(x(\log x)^{2+\varepsilon})$ for every fixed $\varepsilon > 0$.

```lean
theorem erdos_687.variants.maier_pomerance :
    ∀ ε > (0 : ℝ), (fun x : ℕ ↦ (Y x : ℝ)) =O[atTop]
      (fun x : ℕ ↦ (x : ℝ) * Real.log x ^ (2 + ε))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/687.lean, line 219](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean#L219).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/687.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/687.lean)
- [erdosproblems.com/687](https://www.erdosproblems.com/687)
