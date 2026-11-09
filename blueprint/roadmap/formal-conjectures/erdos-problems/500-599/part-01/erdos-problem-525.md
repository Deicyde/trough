---
declaration: theorem
origin: cited
lean: Erdos525.erdos_525.parts.i, Erdos525.erdos_525.parts.ii, Erdos525.erdos_525.variants.kashin, Erdos525.erdos_525.variants.konyagin, Erdos525.erdos_525.variants.konyagin_schlag
statement: formalized
---

# Erdős Problem 525

> *References:*
> - [erdosproblems.com/525](https://www.erdosproblems.com/525)
> - [Er61] Erdős, Paul, _Some unsolved problems_. Magyar Tud. Akad. Mat. Kutató Int. Közl. (1961),
>   221-254.
> - [Li66] Littlewood, J. E., _On polynomials $\sum^n \pm z^m$, $\sum^n e^{\alpha_m i} z^m$,
>   $z = e^{\theta i}$_. J. London Math. Soc. (1966), 367-376.
> - [Ka87] Kashin, B. S., _The properties of random trigonometric polynomials with $\pm 1$
>   coefficients_. Vestnik Moskov. Univ. Ser. I Mat. Mekh. (1987), 40-46, 105.
> - [Ko94] Konyagin, S. V., _On the minimum modulus of random trigonometric polynomials with
>   coefficients $\pm1$_. Mat. Zametki (1994), 80-101, 158.
> - [KoSc99] Konyagin, S. V. and Schlag, W., _Lower bounds for the absolute value of random
>   polynomials on a neighborhood of the unit circle_. Trans. Amer. Math. Soc. (1999), 4963-4980.
> - [CoNg21] Cook, Nicholas A. and Nguyen, Hoi H., _Universality of the minimum modulus for random
>   trigonometric polynomials_. Discrete Anal. (2021), Paper No. 20, 46.

*Quoted from [FormalConjectures/ErdosProblems/525.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/525](https://www.erdosproblems.com/525).

The file states 5 research or textbook statements: 5 solved.

## `Erdos525.erdos_525.parts.i`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos525.lean#L118](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos525.lean#L118).

> Is it true that all except at most $o(2^n)$ many degree $n$ polynomials with $\pm 1$-valued
> coefficients $f(z)$ have $\lvert f(z)\rvert <1$ for some $\lvert z\rvert=1$?
>
> The answer is yes: Littlewood [Li66] conjectured the stronger $m(f)=o(1)$ almost surely, which
> was proved by Kashin [Ka87].

```lean
theorem erdos_525.parts.i :
    (fun n : ℕ ↦ ((exceptional n).ncard : ℝ)) =o[atTop] fun n : ℕ ↦ (2 : ℝ) ^ n
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/525.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean#L75).

## `Erdos525.erdos_525.parts.ii`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos525.lean#L118](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos525.lean#L118).

> What is the behaviour of
>
> $$m(f)=\min_{\lvert z\rvert=1}\lvert f(z)\rvert?$$
>
> Cook and Nguyen [CoNg21] have identified the limiting distribution, proving that for any
> $\epsilon>0$
>
> $$\lim_{n\to \infty} \mathbb{P}(m(f) > \epsilon n^{-1/2}) = e^{-\epsilon \lambda}$$
>
> where $\lambda=\sqrt{\pi/12}$.

```lean
theorem erdos_525.parts.ii (ε : ℝ) (hε : 0 < ε) :
    Tendsto (fun n : ℕ ↦ prob n fun f ↦ ε / √n < m f) atTop
      (nhds (exp (-√(π / 12) * ε)))
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/525.lean, line 91](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean#L91).

## `Erdos525.erdos_525.variants.kashin`

Solved: stated here without proof.

> Littlewood [Li66] conjectured that $m(f)=o(1)$ holds almost surely; this was proved by
> Kashin [Ka87].

```lean
theorem erdos_525.variants.kashin (δ : ℝ) (hδ : 0 < δ) :
    Tendsto (fun n : ℕ ↦ prob n fun f ↦ m f < δ) atTop (nhds 1)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/525.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean#L99).

## `Erdos525.erdos_525.variants.konyagin`

Solved: stated here without proof.

> Konyagin [Ko94] proved that $m(f)\leq n^{-1/2+o(1)}$ almost surely.

```lean
theorem erdos_525.variants.konyagin (δ : ℝ) (hδ : 0 < δ) :
    Tendsto (fun n : ℕ ↦ prob n fun f ↦ m f ≤ (n : ℝ) ^ (-1 / 2 + δ : ℝ)) atTop
      (nhds 1)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/525.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean#L105).

## `Erdos525.erdos_525.variants.konyagin_schlag`

Solved: stated here without proof.

> Konyagin and Schlag [KoSc99] proved that for any $\epsilon>0$
>
> $$\limsup_{n\to \infty} \mathbb{P}(m(f) \leq \epsilon n^{-1/2})\ll \epsilon.$$

```lean
theorem erdos_525.variants.konyagin_schlag :
    ∃ C : ℝ, ∀ ε : ℝ, 0 < ε →
      limsup (fun n : ℕ ↦ prob n fun f ↦ m f ≤ ε / √n) atTop ≤ C * ε
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md), [60 Probability theory and stochastic processes](../../../by-subject/part-02/60-probability-theory-and-stochastic-processes/README.md). Declared in [FormalConjectures/ErdosProblems/525.lean, line 113](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean#L113).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/525.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/525.lean)
- [erdosproblems.com/525](https://www.erdosproblems.com/525)
