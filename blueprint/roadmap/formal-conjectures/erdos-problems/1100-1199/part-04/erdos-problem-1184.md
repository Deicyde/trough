---
declaration: theorem
origin: cited
lean: Erdos1184.erdos_1184, Erdos1184.erdos_1184.variants.lower, Erdos1184.erdos_1184.variants.upper
statement: formalized
---

# Erdős Problem 1184

> *References:*
> - [erdosproblems.com/1184](https://www.erdosproblems.com/1184)
> - [Er76e] Erdős, P., *Problems and results on consecutive integers*. Publ. Math. Debrecen 23
>   (1976), 271-282. [DOI](https://doi.org/10.5486/PMD.1976.23.3-4.15)

*Quoted from [FormalConjectures/ErdosProblems/1184.lean](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1184.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [f606af16](https://github.com/google-deepmind/formal-conjectures/tree/f606af160664c5a10952e9a957b100a1cd45bbeb), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1184](https://www.erdosproblems.com/1184).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos1184.erdos_1184`

Open: stated without proof.

> Let $f(n,k)$ count the number of $1\leq i\leq k$ such that $P(n+i)>k$ (where $P(m)$ is the
> largest prime divisor of $m$). Is it true that, if $\alpha>1$ is such that $n=k^{\alpha+o(1)}$,
> then
>
> $$f(n,k)=(1-\rho(\alpha)+o(1))k,$$
>
> where $\rho$ is the Dickman function?
>
> Erdős [Er76e, p. 272] writes that it seems certain that $f(n,k)=(1-c_\alpha+o(1))k$ for
> $\log n=(\alpha+o(1))\log k$, where $U(k^\alpha,k)=(c_\alpha+o(1))k^\alpha$ and $U(x,k)$ counts the
> $m\leq x$ with $P(m)\leq k$; so $c_\alpha=\rho(\alpha)$. He also reports that Ramachandra, Shorey
> and Tijdeman proved $f(n,k)\geq k-\pi(k)$ for $n>\exp(c(\log k)^2)$.
>
> We read $n=k^{\alpha+o(1)}$ as: $n=n(k)$ is any function of
> $k$ with $\log n(k)/\log k\to\alpha$. The conclusion is $f(n(k),k)/k\to 1-\rho(\alpha)$. This is
> equivalent to the uniform statement: for every $\varepsilon>0$ there are $\delta>0$ and $K$ such
> that $\lvert f(n,k)/k-(1-\rho(\alpha))\rvert\lt \varepsilon$ whenever $k\ge K$ and
> $\lvert\log n/\log k-\alpha\rvert\lt \delta$. The Dickman function is given by `IsDickman`, which
> has exactly one solution on $[0,\infty)$, so the hypothesis `IsDickman ρ` is satisfiable and
> determines $\rho(\alpha)$ for $\alpha>1$.

```lean
theorem erdos_1184 :
    ∀ ρ : ℝ → ℝ, IsDickman ρ → ∀ α : ℝ, 1 < α → ∀ n : ℕ → ℕ,
      Tendsto (fun k : ℕ => Real.log (n k) / Real.log k) atTop (𝓝 α) →
        Tendsto (fun k : ℕ => (f (n k) k : ℝ) / k) atTop (𝓝 (1 - ρ α))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1184.lean, line 86](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1184.lean#L86).

## `Erdos1184.erdos_1184.variants.lower`

Solved: stated here without proof.

> Erdős [Er76e, Theorem 2]: to every $\alpha>1$ there is an $\varepsilon_\alpha>0$ so that for
> $k>k_0(\alpha)$ and $n>k^\alpha-k$
>
> $$f(n,k)>k\left(1-\frac{1}{\alpha}+\varepsilon_\alpha\right).$$
>
> Erdős gives an outline of the proof.

```lean
theorem erdos_1184.variants.lower (α : ℝ) (hα : 1 < α) :
    ∃ ε > 0, ∀ᶠ k : ℕ in atTop, ∀ n : ℕ, (k : ℝ) ^ α - k < n →
      k * (1 - 1 / α + ε) < (f n k : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1184.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1184.lean#L99).

## `Erdos1184.erdos_1184.variants.upper`

Solved: stated here without proof.

> Erdős [Er76e, Theorem 3]: for $n\leq k^\alpha-k$
>
> $$f(n,k)\lt k(\alpha-1)+\frac{k}{\log k}.$$
>
> Erdős notes that this is trivial for $\alpha>2$. We take $k\geq 2$, so that $\log k>0$.

```lean
theorem erdos_1184.variants.upper (α : ℝ) (k n : ℕ) (hk : 2 ≤ k)
    (hn : (n : ℝ) ≤ (k : ℝ) ^ α - k) :
    (f n k : ℝ) < k * (α - 1) + k / Real.log k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1184.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1184.lean#L110).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1184.lean at f606af16](https://github.com/google-deepmind/formal-conjectures/blob/f606af160664c5a10952e9a957b100a1cd45bbeb/FormalConjectures/ErdosProblems/1184.lean)
- [erdosproblems.com/1184](https://www.erdosproblems.com/1184)
