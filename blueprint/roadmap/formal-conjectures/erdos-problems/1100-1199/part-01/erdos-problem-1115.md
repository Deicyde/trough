---
declaration: theorem
origin: cited
lean: Erdos1115.erdos_1115
statement: formalized
---

# Erdős Problem 1115

> *References:*
> - [erdosproblems.com/1115](https://www.erdosproblems.com/1115)
> - [Ha74] Hayman, W. K., *Research problems in function theory: new problems*. Proceedings of
>   the Symposium on Complex Analysis (Canterbury, 1973), London Math. Soc. Lecture Note Ser. 12
>   (1974), 155--180.
> - [HaLi18] Hayman, W. K. and Lingham, E. F., *Research problems in function theory*.
>   [arXiv:1809.07200](https://arxiv.org/abs/1809.07200) (2018).
> - [GoEr79] Gol'dberg, A. A. and Erëmenko, A. È., *On asymptotic curves of entire functions of
>   finite order*. Mat. Sb. (N.S.) (1979), 555--581, 647. English translation: Math. USSR-Sb. 37
>   (1980), 509--533. [Math-Net.Ru](https://www.mathnet.ru/eng/sm2401)
> - [Ha60b] Hayman, W. K., *Slowly growing integral and subharmonic functions*. Comment. Math.
>   Helv. 34 (1960), 75--84.

*Quoted from [FormalConjectures/ErdosProblems/1115.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1115.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1115](https://www.erdosproblems.com/1115).

The file states 1 research or textbook statement: 1 solved. It also has 1 API statement, counted here but not shown.

## `Erdos1115.erdos_1115`

Solved: stated here without proof.

> Let $f(z)$ be an entire function of finite order, and let $\Gamma$ be a rectifiable path on which
> $f(z)\to \infty$. Let $\ell(r)$ be the length of $\Gamma$ in the disc $\lvert z\rvert\lt r$.
>
> Find a path for which $\ell(r)$ grows as slowly as possible, and estimate $\ell(r)$ in terms of
> $M(r)=\max_{\lvert z\rvert=r}\lvert f(z)\rvert$.
>
> In particular, can such a path $\Gamma$ be found for which $\ell(r)\ll r$?
>
> This is Problem 2.41 of [Ha74], where it is attributed to Erdős; see also [HaLi18, Problem 2.41].
> The answer is no: Gol'dberg and Eremenko [GoEr79] proved that for every $\rho\in[0,\infty]$ there
> is an entire function $f$ of order $\rho$ such that, for any asymptotic curve $\Gamma$ on which
> $f\to\infty$, the length of $\Gamma$ in $\lvert z\rvert\leq r$ is not $O(r)$ (see also [HaLi18,
> Updates 2.7 and 2.41]). The length in $\lvert z\rvert\leq r$ is at most the length in
> $\lvert z\rvert<2r$, so $\ell(r)=O(r)$ for the open disc used here would make the length in the
> closed disc $O(r)$ too.
>
> We formalise the last question only: the first part asks for a best possible path and an estimate
> in terms of $M(r)$ and has no precise claim to state, so it is not formalised. Reading choices:
> $f$ is non-constant (a constant has no path on which $f\to\infty$, which would make the statement
> trivially true); finite order is `Erdos516.OfFiniteOrder`; $\Gamma$ is given by its arc length
> parametrisation `γ` (every rectifiable path on which $f\to\infty$ has infinite length and can be
> reparametrised by arc length, without changing the curve traversed or the length in any disc);
> $\ell(r)\ll r$ means $\ell(r)\le Cr$ for some $C$ and all large $r$.
>
> [HaLi18, Problem 2.41] also report that Hayman [Ha60b] (and Piranian) showed that if
> $\log M(r)=O((\log r)^2)$, one can take for $\Gamma$ a ray from the origin, so that $\ell(r)=r$.

```lean
theorem erdos_1115 :
    ¬ ∀ f : ℂ → ℂ, Erdos516.OfFiniteOrder f → (¬ ∃ a : ℂ, ∀ z, f z = a) →
      ∃ γ : ℝ → ℂ, IsAsymptoticPath f γ ∧
        ∃ C : ℝ, ∀ᶠ r : ℝ in atTop, lengthInDisc γ r ≤ ENNReal.ofReal (C * r)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1115.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1115.lean#L99).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1115.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1115.lean)
- [erdosproblems.com/1115](https://www.erdosproblems.com/1115)
