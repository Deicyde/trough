---
declaration: theorem
origin: cited
lean: Erdos1085.erdos_1085.variants.lower_d2, Erdos1085.erdos_1085.variants.upper_d2, Erdos1085.erdos_1085.variants.lower_d3, Erdos1085.erdos_1085.variants.upper_d3, Erdos1085.erdos_1085.variants.lower_d4_lenz, Erdos1085.erdos_1085.variants.upper_d4_erdos, Erdos1085.erdos_1085.variants.upper_lower_d5_odd
statement: formalized
---

# Erdős Problem 1085

> Let f_d(n) be minimal such that, in any set of n points in ℝ^d, there exist at most f_d(n) pairs
> of points which are distance 1 apart. Estimate f_d(n).
>
> *Reference:* [erdosproblems.com/1085](https://www.erdosproblems.com/1085)

*Quoted from [FormalConjectures/ErdosProblems/1085.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1085](https://www.erdosproblems.com/1085).

The file states 7 research or textbook statements: 1 open and 6 solved.

## `Erdos1085.erdos_1085.variants.lower_d2`

Solved: stated here without proof.

> Erdős showed $f_2(n) > n^{1+c/\log\log n}$ for some $c > 0$.

```lean
theorem erdos_1085.variants.lower_d2 :
    ∃ c > (0 : ℝ), ∀ᶠ n : ℕ in atTop, (n : ℝ) ^ (1 + c / log (log n)) < f 2 n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L45).

## `Erdos1085.erdos_1085.variants.upper_d2`

Solved: stated here without proof.

> Spencer, Szemerédi, and Trotter showed $f_2(n) = O(n^{4/3})$.

```lean
theorem erdos_1085.variants.upper_d2 : (fun n ↦ (f 2 n : ℝ)) =O[atTop] (fun n ↦ (n : ℝ) ^ (4/3 : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 51](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L51).

## `Erdos1085.erdos_1085.variants.lower_d3`

Solved: stated here without proof.

> Erdős showed $f_3(n) = Ω(n^{4/3}\log\log n)$.

```lean
theorem erdos_1085.variants.lower_d3 :
    (fun n : ℕ ↦ (n : ℝ) ^ (4/3 : ℝ) * log (log n)) =O[atTop] (fun n ↦ (f 3 n : ℝ))
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L56).

## `Erdos1085.erdos_1085.variants.upper_d3`

Open: stated without proof.

> Is the $n^{4/3}\log\log n$ lower bound in 3D also an upper bound?.

```lean
theorem erdos_1085.variants.upper_d3 :
    (fun n ↦ (f 3 n : ℝ)) =O[atTop] (fun n : ℕ ↦ (n : ℝ) ^ (4/3 : ℝ) * log (log n))
```

Category `research open`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L62).

## `Erdos1085.erdos_1085.variants.lower_d4_lenz`

Solved: stated here without proof.

> Lenz showed that, for $d \ge 4$, $f_d(n) \ge \frac{p - 1}{2p} n^2 - O(1)$ where
> $p = \lfloor\frac d2\rfloor$.

```lean
theorem erdos_1085.variants.lower_d4_lenz (hd : 4 ≤ d) :
    ∃ C : ℝ, ∀ n : ℕ, ↑(d / 2 - 1) / (2 * ↑(d / 2)) * n ^ 2 - C ≤ f d n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 69](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L69).

## `Erdos1085.erdos_1085.variants.upper_d4_erdos`

Solved: stated here without proof.

> Erdős showed that, for $d \ge 4$, $f_d(n) \le \left(\frac{p - 1}{2p} + o(1)\right) n^2$ where
> $p = \lfloor\frac d2\rfloor$.

```lean
theorem erdos_1085.variants.upper_d4_erdos (hd : 4 ≤ d) :
    ∃ g : ℕ → ℝ, Tendsto g atTop (𝓝 0) ∧
      ∀ n, f d n ≤ (↑(d / 2 - 1) / (2 * ↑(d / 2)) + g n) * n ^ 2
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 76](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L76).

## `Erdos1085.erdos_1085.variants.upper_lower_d5_odd`

Solved: stated here without proof.

> Erdős and Pach showed that, for $d \ge 5$ odd, there exist constants $c_1(d), c_2(d) > 0$
> such that $\frac{p - 1}{2p} n^2 + c_1 n^{4/3} \le f_d(n) \le \frac{p - 1}{2p} n^2 + c_2 n^{4/3}$ where
> $p = \lfloor\frac d2\rfloor$.

```lean
theorem erdos_1085.variants.upper_lower_d5_odd (hd : 5 ≤ d) (hd_odd : Odd d) :
    ∃ c₁ > (0 : ℝ), ∃ c₂ : ℝ, ∀ᶠ n in atTop,
      ↑(d / 2 - 1) / (2 * ↑(d / 2)) * n ^ 2 + c₁ * n ^ (4 / 3 : ℝ) ≤ f d n ∧
      f d n ≤ ↑(d / 2 - 1) / (2 * ↑(d / 2)) * n ^ 2 + c₂ * n ^ (4 / 3 : ℝ)
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/ErdosProblems/1085.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean#L85).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1085.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1085.lean)
- [erdosproblems.com/1085](https://www.erdosproblems.com/1085)
