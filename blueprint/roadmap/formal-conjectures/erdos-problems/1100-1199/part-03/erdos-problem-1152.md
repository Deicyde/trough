---
declaration: theorem
origin: cited
lean: Erdos1152.erdos_1152
statement: formalized
---

# Erdős Problem 1152

> *References:*
> - [erdosproblems.com/1152](https://www.erdosproblems.com/1152)
> - [EKS89] Erdős, P., Kroó, A. and Szabados, J., *On convergent interpolatory polynomials*.
>   J. Approx. Theory 58 (1989), 232-241. [PDF](https://www.renyi.hu/~p_erdos/1989-16.pdf)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).

*Quoted from [FormalConjectures/ErdosProblems/1152.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1152.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1152](https://www.erdosproblems.com/1152).

The file states 1 research or textbook statement: 1 open.

## `Erdos1152.erdos_1152`

Open: stated without proof.

> For $n\geq 1$ fix some sequence of $n$ distinct numbers $x_{1n},\ldots,x_{nn}\in [-1,1]$. Let
> $\epsilon=\epsilon(n)\to 0$.
>
> Does there always exist a continuous function $f:[-1,1]\to \mathbb{R}$ such that if $p_n$ is a
> sequence of polynomials, with degrees $\deg p_n<(1+\epsilon(n))n$, such that
> $p_n(x_{kn})=f(x_{kn})$ for all $1\leq k\leq n$, then $p_n(x)\not\to f(x)$ for almost all
> $x\in [-1,1]$?
>
> This is Problem 2.42 in [Va99]. The $n$ nodes of the $n$-th row form the finite set `nodes n`.
> We take $\epsilon(n)>0$. A smaller $\epsilon$ only shrinks the class of $p_n$, so this is
> equivalent to allowing any real $\epsilon(n)\to 0$. We impose the degree bound only for
> $n\geq 1$, since for $n=0$ the bound `natDegree < 0` can never hold. We read
> "$p_n(x)\not\to f(x)$ for almost all $x$" as: for almost every $x$, the sequence $p_n(x)$ does
> not converge to $f(x)$.
>
> For $\deg p_n\lt n$ the interpolating polynomial is unique (the Lagrange polynomial). Erdős, Kroó
> and Szabados [EKS89, pp. 232-233] give necessary and sufficient conditions on the nodes under
> which, for every continuous $f$ and every fixed $\epsilon>0$, there are interpolating polynomials
> of degree at most $\lfloor n(1+\epsilon)\rfloor$ approximating $f$ at the rate of the best
> uniform approximation (in particular converging uniformly to $f$).

```lean
theorem erdos_1152 :
    ∀ nodes : ℕ → Finset ℝ, (∀ n, (nodes n).card = n) →
      (∀ n, ∀ x ∈ nodes n, x ∈ Set.Icc (-1 : ℝ) 1) →
      ∀ ε : ℕ → ℝ, (∀ n, 0 < ε n) → Tendsto ε atTop (𝓝 0) →
        ∃ f : ℝ → ℝ, ContinuousOn f (Set.Icc (-1 : ℝ) 1) ∧
          ∀ p : ℕ → ℝ[X],
            (∀ n : ℕ, 1 ≤ n → ((p n).natDegree : ℝ) < (1 + ε n) * n) →
            (∀ n, ∀ x ∈ nodes n, (p n).eval x = f x) →
              ∀ᵐ t ∂(volume.restrict (Set.Icc (-1 : ℝ) 1)),
                ¬ Tendsto (fun n => (p n).eval t) atTop (𝓝 (f t))
```

Category `research open`; AMS [41 Approximations and expansions](../../../by-subject/part-02/41-approximations-and-expansions/README.md). Declared in [FormalConjectures/ErdosProblems/1152.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1152.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1152.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/1152.lean)
- [erdosproblems.com/1152](https://www.erdosproblems.com/1152)
