---
declaration: theorem
origin: cited
lean: Erdos148.erdos_148, Erdos148.erdos_148.variants.lower_bound, Erdos148.erdos_148.variants.upper_bound
statement: formalized
---

# Erdős Problem 148

> *References:*
> - [erdosproblems.com/148](https://www.erdosproblems.com/148)
> - [ElPl21] Elsholtz, Christian and Planitzer, Stefan, *Sums of four and more unit fractions and
>   approximate parametrizations*. Bull. Lond. Math. Soc. (2021), 695-709.
> - [Ko14] Konyagin, S. V., *Double exponential lower bound for the number of representations of
>   unity by Egyptian fractions*. Math. Notes (2014), 277-281.
> - [OEIS A006585](https://oeis.org/A006585)

*Quoted from [FormalConjectures/ErdosProblems/148.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/148.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/148](https://www.erdosproblems.com/148).

The file states 3 research or textbook statements: 1 open and 2 solved. It also has 5 test statements, counted here but not shown.

## `Erdos148.erdos_148`

Open: stated without proof.

> Let $F(k)$ be the number of solutions to
>
> $$ 1= \frac{1}{n_1}+\cdots+\frac{1}{n_k},$$
>
> where $1\leq n_1\lt \cdots\lt n_k$ are distinct integers. Find good estimates for $F(k)$.

```lean
theorem erdos_148 : (fun k ↦ (F k : ℝ)) =Θ[atTop] erdos_148.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/148.lean, line 174](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/148.lean#L174).

## `Erdos148.erdos_148.variants.lower_bound`

Solved: stated here without proof.

> The current best bounds known are
>
> $$2^{c^{\frac{k}{\log k}}}\leq F(k) \leq c_0^{(\frac{1}{5}+o(1))2^k},$$
>
> where $c>0$ is some absolute constant and $c_0=1.5979102\ldots$ is the square of the 'Vardi
> constant' $1.26408\cdots$. The lower bound is due to Konyagin [Ko14] and the upper bound to
> Elsholtz and Planitzer [ElPl21]. (erdosproblems.com gives $c_0=1.26408\cdots$;
> [ElPl21, Remark 3] gives $c_0=1.5979102\ldots$.)
>
> [Ko14, Theorem 1] states the lower bound in the explicit form
>
> $$F(k) \geq \exp\left(\exp\left(\left(\frac{(\log 2)(\log 3)}{3}+o(1)\right)
> \frac{k}{\log k}\right)\right) \quad (k \to \infty),$$
>
> which is the statement formalised here.

```lean
theorem erdos_148.variants.lower_bound :
    ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧ ∀ᶠ k : ℕ in atTop,
      exp (exp ((log 2 * log 3 / 3 + o k) * ((k : ℝ) / log k))) ≤ F k
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/148.lean, line 191](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/148.lean#L191).

## `Erdos148.erdos_148.variants.upper_bound`

Solved: stated here without proof.

> The current best bounds known are
>
> $$2^{c^{\frac{k}{\log k}}}\leq F(k) \leq c_0^{(\frac{1}{5}+o(1))2^k},$$
>
> where $c>0$ is some absolute constant and $c_0=1.5979102\ldots$ is the square of the 'Vardi
> constant' $1.26408\cdots$. The lower bound is due to Konyagin [Ko14] and the upper bound to
> Elsholtz and Planitzer [ElPl21]. (erdosproblems.com gives $c_0=1.26408\cdots$;
> [ElPl21, Remark 3] gives $c_0=1.5979102\ldots$.)
>
> [ElPl21, Corollary 3(2)] shows that for every $\varepsilon > 0$ and all $k \geq k(\varepsilon)$,
> the number $f_k(1,1) \geq F(k)$ of solutions with $n_1 \leq \cdots \leq n_k$ is less than
> $c_0^{(\frac{2}{5}+\varepsilon)2^{k-1}} = c_0^{(\frac{1}{5}+\frac{\varepsilon}{2})2^k}$.

```lean
theorem erdos_148.variants.upper_bound :
    ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧ ∀ᶠ k : ℕ in atTop,
      (F k : ℝ) ≤ c₀ ^ ((1 / 5 + o k) * 2 ^ k)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/148.lean, line 209](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/148.lean#L209).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/148.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/148.lean)
- [erdosproblems.com/148](https://www.erdosproblems.com/148)
