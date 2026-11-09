---
declaration: theorem
origin: cited
lean: Erdos408.erdos_408.parts.i, Erdos408.erdos_408.parts.ii, Erdos408.erdos_408.variants.pillai, Erdos408.erdos_408.variants.ford_konyagin_luca
statement: formalized
---

# Erdős Problem 408

> *References:*
> - [erdosproblems.com/408](https://www.erdosproblems.com/408)
> - [OEIS A003434](https://oeis.org/A003434): the values $f(n)$ for $n \geq 2$.
> - [ErGr80] Erdős, P. and Graham, R., *Old and new problems and results in combinatorial number
>   theory*. Monographies de L'Enseignement Mathématique (1980).
> - [Pi29] Pillai, S. Sivasankaranarayana, *On a function connected with $\phi(n)$*. Bull. Amer.
>   Math. Soc. 35 (1929), 837-841.
>   [doi:10.1090/S0002-9904-1929-04800-6](https://doi.org/10.1090/S0002-9904-1929-04800-6)
> - [Sh50] Shapiro, Harold N., *On the iterates of a certain class of arithmetic functions*. Comm.
>   Pure Appl. Math. 3 (1950), 259-272.
> - [EGPS90] Erdős, P., Granville, A., Pomerance, C. and Spiro, C., *On the normal behavior of the
>   iterates of some arithmetic functions*. Analytic number theory (Allerton Park, IL, 1989),
>   Progr. Math. 85 (1990), 165-204.
> - [Gu04] Guy, Richard K., *Unsolved problems in number theory*. Third edition, Springer (2004),
>   Problem B41.
> - [FKL10] Ford, K., Konyagin, S. V. and Luca, F., *Prime chains and Pratt trees*. Geom. Funct.
>   Anal. 20 (2010), 1231-1258. [arXiv:0904.0473](https://arxiv.org/abs/0904.0473)
>   [doi:10.1007/s00039-010-0089-0](https://doi.org/10.1007/s00039-010-0089-0)

*Quoted from [FormalConjectures/ErdosProblems/408.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/408](https://www.erdosproblems.com/408).

The file states 4 research or textbook statements: 2 open and 2 solved. It also has 4 test statements, counted here but not shown.

## `Erdos408.erdos_408.parts.i`

Open: stated without proof.

> Let $\phi(n)$ be the Euler totient function and $\phi_k(n)$ be the iterated $\phi$ function, so
> that $\phi_1(n)=\phi(n)$ and $\phi_k(n)=\phi(\phi_{k-1}(n))$. Let
>
> $$f(n) = \min\{k : \phi_k(n)=1\}.$$
>
> Does $f(n)/\log n$ have a distribution function?
>
> We ask for a distribution function $F$ (non-decreasing, with $F(-\infty) = 0$ and
> $F(+\infty) = 1$) such that, for every continuity point $c$ of $F$, the set
> $\{n : f(n)/\log n \leq c\}$ has natural density $F(c)$. For $n \leq 1$ the quotient is $0$ in
> Lean, which does not affect densities. Erdős, Granville, Pomerance and Spiro [EGPS90] proved
> that the answer is yes, conditional on a form of the Elliott–Halberstam conjecture.

```lean
theorem erdos_408.parts.i :
    ∃ F : ℝ → ℝ, Monotone F ∧ Tendsto F atBot (𝓝 0) ∧ Tendsto F atTop (𝓝 1) ∧
      ∀ c : ℝ, ContinuousAt F c →
        {n : ℕ | (f n : ℝ) / Real.log n ≤ c}.HasDensity (F c)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/408.lean, line 118](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean#L118).

## `Erdos408.erdos_408.parts.ii`

Open: stated without proof.

> Is $f(n)/\log n$ almost always constant?
>
> We read this as: is there a constant $\alpha$ such that, for every $\epsilon > 0$, the set of
> $n$ with $|f(n)/\log n - \alpha| < \epsilon$ has natural density $1$? Erdős, Granville,
> Pomerance and Spiro [EGPS90] proved that, conditional on a form of the Elliott–Halberstam
> conjecture, $f(n)$ has normal order $\alpha \log n$ for some constant $\alpha > 0$, so that the
> answer is yes under this hypothesis.

```lean
theorem erdos_408.parts.ii :
    ∃ α : ℝ, ∀ ε > (0 : ℝ),
      {n : ℕ | |(f n : ℝ) / Real.log n - α| < ε}.HasDensity 1
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/408.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean#L134).

## `Erdos408.erdos_408.variants.pillai`

Solved: stated here without proof.

> Pillai [Pi29] proved that, for all $n \geq 2$,
>
> $$\left\lfloor \frac{\log n - \log 2}{\log 3} \right\rfloor + 1 \leq f(n) \leq
>   \left\lfloor \frac{\log n}{\log 2} \right\rfloor + 1.$$
>
> These are Theorems I and III of [Pi29]; Pillai's function $R(n)$ is the least $r$ with
> $\phi_r(n) = 1$, which is $f(n)$. The lower bound is attained at $n = 2 \cdot 3^k$, and
> $f(2^k) = k$ (`Erdos408.f_two_pow`), so the upper bound cannot be replaced by $f(n) < \log_2 n$.

```lean
theorem erdos_408.variants.pillai (n : ℕ) (hn : 2 ≤ n) :
    ⌊(Real.log n - Real.log 2) / Real.log 3⌋₊ + 1 ≤ f n ∧
      f n ≤ ⌊Real.log n / Real.log 2⌋₊ + 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/408.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean#L148).

## `Erdos408.erdos_408.variants.ford_konyagin_luca`

Solved: stated here without proof.

> The third question asks what can be said about the largest prime factor $P^+(\phi_k(n))$ when,
> say, $k = \log\log n$; it is open-ended and is not formalised. The site remarks that it is likely
> true that, if $k \to \infty$ however slowly with $n$, then $P^+(\phi_k(n)) \leq n^{o(1)}$ for
> almost all $n$.
>
> Ford, Konyagin and Luca [FKL10, Theorem 5] proved that for every $\epsilon > 0$ and $\delta > 0$
> there is an integer $k$ such that, for all large $x$, at least $(1 - \epsilon)x$ integers
> $n \leq x$ satisfy $P^+(\phi_k(n)) \leq x^{\delta}$. Since $P^+(\phi(m)) \leq P^+(m)$, this gives
> the remark above for every $k = k(n) \to \infty$.

```lean
theorem erdos_408.variants.ford_konyagin_luca (ε δ : ℝ) (hε : 0 < ε) (hδ : 0 < δ) :
    ∃ k : ℕ, ∀ᶠ x : ℝ in atTop, (1 - ε) * x ≤
      ((Finset.Icc 1 ⌊x⌋₊).filter fun n ↦
        ((Nat.totient^[k] n).maxPrimeFac : ℝ) ≤ x ^ δ).card
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/408.lean, line 165](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean#L165).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/408.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/408.lean)
- [erdosproblems.com/408](https://www.erdosproblems.com/408)
