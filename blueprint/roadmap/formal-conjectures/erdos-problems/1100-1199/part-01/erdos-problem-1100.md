---
declaration: theorem
origin: cited
lean: Erdos1100.erdos_1100.parts.i, Erdos1100.erdos_1100.parts.ii, Erdos1100.erdos_1100.parts.iii, Erdos1100.erdos_1100.variants.omega_le, Erdos1100.erdos_1100.variants.eq_omega, Erdos1100.erdos_1100.variants.erdos_hall, Erdos1100.erdos_1100.variants.erdos_tenenbaum_max, Erdos1100.erdos_1100.variants.normal_order, Erdos1100.erdos_1100.variants.erdos_simonovits, Erdos1100.erdos_1100.variants.erdos_tenenbaum_g
statement: formalized
---

# Erdős Problem 1100

> *References:*
> - [erdosproblems.com/1100](https://www.erdosproblems.com/1100)
> - [ErHa78] Erdős, P. and Hall, R. R., *On some unconventional problems on the divisors of
>   integers*. J. Austral. Math. Soc. Ser. A 25 (1978), 479-485.
>   [PDF](https://www.renyi.hu/~p_erdos/1978-26.pdf)
> - [Er81h] Erdős, P., *Some problems and results on additive and multiplicative number theory*.
>   Analytic number theory (Philadelphia, Pa., 1980) (1981), 171-182.
>   [PDF](https://www.renyi.hu/~p_erdos/1981-33.pdf)
> - [ErTe89] Erdős, P. and Tenenbaum, G., *Sur les fonctions arithmétiques liées aux diviseurs
>   consécutifs*. J. Number Theory 31 (1989), 285-311.
>   [PDF](https://www.renyi.hu/~p_erdos/1989-37.pdf)
>
> The function $\tau_\perp(n)$ is called $\tau_r(n)$ in [Er81h] and $f(n)$ in [ErHa78] and [ErTe89].

*Quoted from [FormalConjectures/ErdosProblems/1100.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1100](https://www.erdosproblems.com/1100).

The file states 10 research or textbook statements: 1 open, 8 solved and 1 textbook result.

## `Erdos1100.erdos_1100.parts.i`

Solved: stated here without proof.

> If $1=d_1\lt \cdots\lt d_{\tau(n)}=n$ are the divisors of $n$, then let $\tau_\perp(n)$ count the number
> of $i$ for which $(d_i,d_{i+1})=1$.
>
> Is it true that $\tau_\perp(n)/\omega(n)\to \infty$ for almost all $n$?
>
> This is the first part, asked by Erdős and Hall [ErHa78, p. 483]. We read it as: for every $C$ the
> set of $n$ with $\tau_\perp(n)\leq C\omega(n)$ has natural density $0$. This is equivalent to
> $\tau_\perp(n)/\omega(n)\to\infty$ along a set of density $1$, and it avoids dividing by
> $\omega(1)=0$.
>
> The answer is yes. By [ErTe89, Corollary 2, p. 288], $\tau_\perp(n)\geq(\log n)^{\log 3-1+o(1)}$
> for almost all $n$ (see `erdos_1100.variants.normal_order`), while $\omega(n)\sim\log\log n$ for
> almost all $n$ (Hardy-Ramanujan).

```lean
theorem erdos_1100.parts.i :
    ∀ C : ℝ, {n : ℕ | (tauPerp n : ℝ) ≤ C * (ω n : ℝ)}.HasDensity 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L75).

## `Erdos1100.erdos_1100.parts.ii`

Solved: stated here without proof.

> If $1=d_1\lt \cdots\lt d_{\tau(n)}=n$ are the divisors of $n$, then let $\tau_\perp(n)$ count the number
> of $i$ for which $(d_i,d_{i+1})=1$.
>
> Is it true that
> $$\tau_\perp(n)< \exp((\log n)^{o(1)})$$
> for all $n$?
>
> This is the second part. Erdős and Hall [ErHa78, p. 483] say it would be reasonable to expect
> that for every $\epsilon>0$ one has $\tau_\perp(n)\lt \exp((\log n)^{\epsilon})$; the problem page
> asks it as a question. We read $o(1)$ as: for every $\epsilon>0$ and all sufficiently large $n$.
> This is equivalent to a bound for all $n$ with an exponent that tends to $0$. A bound for all $n$
> with a fixed small $\epsilon$ fails: for example $\tau_\perp(30)=4>\exp((\log 30)^{0.1})$.
>
> The answer is no. Erdős and Tenenbaum [ErTe89, Theorem 4, p. 289] proved
> $\max_{n\leq x}\tau_\perp(n)\geq\exp\bigl(((\log 2)^2+o(1))\log x/(\log\log x)^2\bigr)$ (see
> `erdos_1100.variants.erdos_tenenbaum_max`). This gives infinitely many $n$ with
> $\tau_\perp(n)>\exp((\log n)^{1/2})$.

```lean
theorem erdos_1100.parts.ii :
    ¬ ∀ ε : ℝ, 0 < ε → ∀ᶠ n : ℕ in atTop, (tauPerp n : ℝ) < Real.exp (Real.log n ^ ε)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L99).

## `Erdos1100.erdos_1100.parts.iii`

Open: stated without proof.

> Let
> $$g(k) = \max_{\omega(n)=k}\tau_\perp(n),$$
> where $\omega(n)$ counts the number of distinct prime divisors of $n$, and $n$ is restricted to
> squarefree integers. Determine the growth of $g(k)$.
>
> This is the third part. We read "determine the growth" as $g(k)=\Theta(\texttt{answer}\ k)$. Known
> bounds are $(\sqrt2+o(1))^k\lt g(k)<(2-c)^k$ [Er81h, p. 173] (see
> `erdos_1100.variants.erdos_simonovits`), and $g(k)\leq 3\cdot(3\cdot 2^{-2/3})^k$
> [ErTe89, Theorem 1] (see `erdos_1100.variants.erdos_tenenbaum_g`). So $g$ is at most exponential,
> the lower bound announced in [Er81h] would make it exponential, and already the base of the
> exponential is open.

```lean
theorem erdos_1100.parts.iii :
    (fun k : ℕ ↦ (g k : ℝ)) =Θ[atTop] erdos_1100.parts.iii.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 119](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L119).

## `Erdos1100.erdos_1100.variants.omega_le`

Textbook result, stated without proof.

> It is trivial that $\tau_\perp(n)\geq \omega(n)$ [ErHa78, p. 480], [ErTe89, (1.9), p. 288]: each
> prime divisor of $n$ is the larger member of a coprime pair of consecutive divisors.

```lean
theorem erdos_1100.variants.omega_le : ∀ n : ℕ, 0 < n → ω n ≤ tauPerp n
```

Category `textbook`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L128).

## `Erdos1100.erdos_1100.variants.eq_omega`

Solved: stated here without proof.

> There is equality $\tau_\perp(n)=\omega(n)$ for infinitely many $n$: Erdős and Hall [ErHa78, p. 480]
> note equality when $n=p_1\cdots p_k$ and $p_i>p_1\cdots p_{i-1}$ for $2\leq i\leq k$. Such $n$
> exist for every $k$, which we state.

```lean
theorem erdos_1100.variants.eq_omega (k : ℕ) :
    ∃ n : ℕ, Squarefree n ∧ ω n = k ∧ tauPerp n = k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L137).

## `Erdos1100.erdos_1100.variants.erdos_hall`

Solved: stated here without proof.

> Erdős and Hall [ErHa78, Theorem 1, p. 480] prove, for all $\epsilon>0$ and sufficiently large $x$,
> $$\max_{n\lt x} \tau_\perp(n) > \exp((\log\log x)^{2-\epsilon}).$$
> We write the maximum as: some $n\lt x$ has $\tau_\perp(n)$ above the bound.

```lean
theorem erdos_1100.variants.erdos_hall : ∀ ε : ℝ, 0 < ε → ∀ᶠ x : ℝ in atTop,
    ∃ n : ℕ, (n : ℝ) < x ∧ Real.exp (Real.log (Real.log x) ^ (2 - ε)) < (tauPerp n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 147](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L147).

## `Erdos1100.erdos_1100.variants.erdos_tenenbaum_max`

Solved: stated here without proof.

> Erdős and Tenenbaum [ErTe89, Theorem 4, p. 289] improved this considerably: for $x\geq 3$,
> $$\max_{n\leq x}\tau_\perp(n)\geq \exp\Bigl(\bigl((\log 2)^2+o(1)\bigr)
> \frac{\log x}{(\log\log x)^2}\Bigr).$$
> We write $o(1)$ as an arbitrarily small $\delta>0$ and the maximum as: some $n\leq x$ has
> $\tau_\perp(n)$ above the bound.

```lean
theorem erdos_1100.variants.erdos_tenenbaum_max : ∀ δ : ℝ, 0 < δ → ∀ᶠ x : ℝ in atTop,
    ∃ n : ℕ, (n : ℝ) ≤ x ∧
      Real.exp (((Real.log 2) ^ 2 - δ) * Real.log x / (Real.log (Real.log x)) ^ 2) ≤
        (tauPerp n : ℝ)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L159).

## `Erdos1100.erdos_1100.variants.normal_order`

Solved: stated here without proof.

> Erdős and Tenenbaum [ErTe89, Corollary 2, p. 288] proved that for almost all $n$ (that is, on a set
> of density $1$)
> $$(\log n)^{\log 3-1+o(1)}\leq \tau_\perp(n)\leq (\log n)^{\log 2-1/2+o(1)}.$$
> The paper credits the upper bound to an earlier work of the same authors (Bull. Soc. Math. France
> 111 (1983)). We write $o(1)$ as: for every $\epsilon>0$ the set of $n$ with
> both bounds, with exponents shifted by $\mp\epsilon$, has density $1$.

```lean
theorem erdos_1100.variants.normal_order : ∀ ε : ℝ, 0 < ε →
    {n : ℕ | Real.log n ^ (Real.log 3 - 1 - ε) ≤ (tauPerp n : ℝ) ∧
      (tauPerp n : ℝ) ≤ Real.log n ^ (Real.log 2 - 1 / 2 + ε)}.HasDensity 1
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L174).

## `Erdos1100.erdos_1100.variants.erdos_simonovits`

Solved: stated here without proof.

> Erdős and Simonovits (see [Er81h, p. 173]) proved
> $$(2^{1/2}+o(1))^k < g(k) < (2-c)^k$$
> for some constant $c>0$. We write the lower bound as: every fixed $0\leq r\lt \sqrt2$ satisfies
> $r^k\lt g(k)$ for all large $k$, and the upper bound for all large $k$.
>
> [Er81h] announces this without proof, and [ErTe89, p. 291] calls the argument of Erdős and
> Simonovits for squarefree $n$, which it uses for the upper bound, unpublished. The upper bound also
> follows from `erdos_1100.variants.erdos_tenenbaum_g`.

```lean
theorem erdos_1100.variants.erdos_simonovits :
    (∀ r : ℝ, 0 ≤ r → r < Real.sqrt 2 → ∀ᶠ k : ℕ in atTop, r ^ k < (g k : ℝ)) ∧
      ∃ c : ℝ, 0 < c ∧ ∀ᶠ k : ℕ in atTop, (g k : ℝ) < (2 - c) ^ k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 190](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L190).

## `Erdos1100.erdos_1100.variants.erdos_tenenbaum_g`

Solved: stated here without proof.

> For squarefree $n$ with $\omega(n)=k$ the bound $f(n)\leq 3\tau(n)B_1^{\omega_1(n)}$ of
> [ErTe89, Theorem 1, (1.3), p. 287], with $B_1=3\cdot 2^{-5/3}$, gives
> $$g(k)\leq 3\left(3\cdot 2^{-2/3}\right)^k,$$
> and $3\cdot 2^{-2/3}=1.88988\ldots<2$.

```lean
theorem erdos_1100.variants.erdos_tenenbaum_g (k : ℕ) :
    (g k : ℝ) ≤ 3 * (3 / (2 : ℝ) ^ ((2 : ℝ) / 3)) ^ k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/1100.lean, line 202](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean#L202).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1100.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1100.lean)
- [erdosproblems.com/1100](https://www.erdosproblems.com/1100)
