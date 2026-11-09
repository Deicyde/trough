---
declaration: theorem
origin: cited
lean: Erdos626.erdos_626.parts.i, Erdos626.erdos_626.variants.kostochka, Erdos626.erdos_626.variants.erdos_upper, Erdos626.erdos_626.parts.ii, Erdos626.erdos_626.variants.h_lower, Erdos626.erdos_626.variants.h_upper_odd, Erdos626.erdos_626.variants.h_odd_conjecture, Erdos626.erdos_626.variants.h_even_conjecture
statement: formalized
---

# Erdős Problem 626

> *References:*
> - [erdosproblems.com/626](https://www.erdosproblems.com/626)
> - [Er59b] Erdős, P., *Graph theory and probability*. Canadian J. Math. (1959), 34-38.
> - [Er62b] Erdős, P., *On circuits and subgraphs of chromatic graphs*. Mathematika (1962),
>   170-175.
> - [Er69b] Erdős, P., *Problems and results in chromatic graph theory*. Proof Techniques in Graph
>   Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968) (1969), 27-35.
> - [Ko88] Kostochka, A. V., *Upper bounds on the chromatic number of graphs*. Trudy Inst. Mat.
>   (Novosibirsk) (1988), 204-226, 265.

*Quoted from [FormalConjectures/ErdosProblems/626.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/626](https://www.erdosproblems.com/626).

The file states 8 research or textbook statements: 4 open and 4 solved. It also has 1 test statement, counted here but not shown.

## `Erdos626.erdos_626.parts.i`

Open: stated without proof.

> Let $k \geq 4$ and let $g_k(n)$ denote the largest $m$ such that there is a graph on $n$
> vertices with chromatic number $k$ and girth $> m$ (i.e. containing no cycle of length
> $\leq m$). Does
> $$\lim_{n\to\infty}\frac{g_k(n)}{\log n}$$
> exist?
>
> By `Erdos626.erdos_626.variants.kostochka` and `Erdos626.erdos_626.variants.erdos_upper`, the
> limit, if it exists, is a positive real number.

```lean
theorem erdos_626.parts.i :
    ∀ k : ℕ, 4 ≤ k → ∃ L : ℝ,
      Tendsto (fun n : ℕ ↦ (g k n : ℝ) / Real.log n) atTop (𝓝 L)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L85).

## `Erdos626.erdos_626.variants.kostochka`

Solved: stated here without proof.

> Kostochka [Ko88] proved that for $k \geq 4$
> $$g_k(n) \geq \frac{1}{4\log k}\log n.$$
> Kostochka's theorem gives this lower bound for the girth itself, and $g_k(n)$ is one less than the
> largest possible girth, so the inequality above holds only up to $1$. The statement below is a
> consequence of his theorem, not the theorem itself: for every $\varepsilon > 0$ and all
> sufficiently large $n$, $g_k(n) \geq \left(\frac{1}{4\log k} - \varepsilon\right)\log n$.

```lean
theorem erdos_626.variants.kostochka :
    ∀ k : ℕ, 4 ≤ k → ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (1 / (4 * Real.log k) - ε) * Real.log n ≤ (g k n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L99).

## `Erdos626.erdos_626.variants.erdos_upper`

Solved: stated here without proof.

> Erdős [Er59b] proved that for $k \geq 4$
> $$g_k(n) \leq \frac{2}{\log(k-2)}\log n + 1.$$
> We state it for all sufficiently large $n$.

```lean
theorem erdos_626.variants.erdos_upper :
    ∀ k : ℕ, 4 ≤ k → ∀ᶠ n : ℕ in atTop,
      (g k n : ℝ) ≤ 2 * Real.log n / Real.log ((k : ℝ) - 2) + 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 110](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L110).

## `Erdos626.erdos_626.parts.ii`

Open: stated without proof.

> Let $h^{(m)}(n)$ be the maximal chromatic number of a graph on $n$ vertices with girth $> m$.
> Does
> $$\lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n}$$
> exist, and what is its value? The value is asked for in
> `Erdos626.erdos_626.variants.h_odd_conjecture` and `Erdos626.erdos_626.variants.h_even_conjecture`.

```lean
theorem erdos_626.parts.ii :
    ∀ m : ℕ, ∃ L : ℝ,
      Tendsto (fun n : ℕ ↦ Real.log (h m n : ℝ) / Real.log n) atTop (𝓝 L)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 123](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L123).

## `Erdos626.erdos_626.variants.h_lower`

Solved: stated here without proof.

> Erdős [Er59b] proved that
> $$\lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n} \gg \frac{1}{m}.$$
> The existence of the limit is open, so we state the lower bound for the lower limit: there is
> an absolute constant $c > 0$ such that for every $m \geq 1$ and $\varepsilon > 0$, eventually
> $h^{(m)}(n) \geq n^{c/m - \varepsilon}$.

```lean
theorem erdos_626.variants.h_lower :
    ∃ c > (0 : ℝ), ∀ m : ℕ, 1 ≤ m → ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ (c / (m : ℝ) - ε) ≤ (h m n : ℝ)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 136](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L136).

## `Erdos626.erdos_626.variants.h_upper_odd`

Solved: stated here without proof.

> Erdős [Er59b] proved that for odd $m$
> $$\lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n} \leq \frac{2}{m+1}.$$
> The existence of the limit is open, so we state the bound for the upper limit: for every
> $\varepsilon > 0$, eventually $h^{(m)}(n) \leq n^{2/(m+1) + \varepsilon}$.

```lean
theorem erdos_626.variants.h_upper_odd :
    ∀ m : ℕ, Odd m → ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (h m n : ℝ) ≤ (n : ℝ) ^ (2 / ((m : ℝ) + 1) + ε)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 148](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L148).

## `Erdos626.erdos_626.variants.h_odd_conjecture`

Open: stated without proof.

> Erdős conjectured that the bound in `Erdos626.erdos_626.variants.h_upper_odd` is sharp: for
> odd $m$,
> $$\lim_{n\to\infty}\frac{\log h^{(m)}(n)}{\log n} = \frac{2}{m+1}.$$

```lean
theorem erdos_626.variants.h_odd_conjecture :
    ∀ m : ℕ, Odd m → Tendsto (fun n : ℕ ↦ Real.log (h m n : ℝ) / Real.log n) atTop
      (𝓝 (2 / ((m : ℝ) + 1)))
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 159](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L159).

## `Erdos626.erdos_626.variants.h_even_conjecture`

Open: stated without proof.

> For even $m$, Erdős had no good guess for the value of the limit, other than that it should
> lie in $\left[\frac{2}{m+2}, \frac{2}{m}\right]$. He could not prove this even for $m = 4$.
>
> The existence of the limit is open, so we state the claim for the lower and upper limits: for
> every $\varepsilon > 0$, eventually
> $n^{2/(m+2) - \varepsilon} \leq h^{(m)}(n) \leq n^{2/m + \varepsilon}$. We require $m \geq 2$,
> since $2/m$ is undefined for $m = 0$. The upper half is known: girth $> m$ implies girth
> $> m - 1$, so $h^{(m)}(n) \leq h^{(m-1)}(n)$, and `Erdos626.erdos_626.variants.h_upper_odd` for
> the odd number $m - 1$ gives the exponent $2/m$.

```lean
theorem erdos_626.variants.h_even_conjecture :
    ∀ m : ℕ, Even m → 2 ≤ m → ∀ ε > (0 : ℝ), ∀ᶠ n : ℕ in atTop,
      (n : ℝ) ^ (2 / ((m : ℝ) + 2) - ε) ≤ (h m n : ℝ) ∧
        (h m n : ℝ) ≤ (n : ℝ) ^ (2 / (m : ℝ) + ε)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/626.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean#L176).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/626.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/626.lean)
- [erdosproblems.com/626](https://www.erdosproblems.com/626)
