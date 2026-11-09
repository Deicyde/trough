---
declaration: theorem
origin: cited
lean: Erdos1048.erdos_1048, Erdos1048.erdos_1048.variants.pommerenke_ncard_components, Erdos1048.erdos_1048.variants.pommerenke_diam_tendsto_zero, Erdos1048.erdos_1048.variants.r_le_one, Erdos1048.erdos_1048.variants.diam_ge_two, Erdos1048.erdos_1048.variants.diam_ge_two_is_best, Erdos1048.erdos_1048.variants.diam_gt_inv_r, Erdos1048.erdos_1048.variants.diam_gt_two_sub_sq
statement: formalized
---

# Erdős Problem 1048

> *References:*
> - [erdosproblems.com/1048](https://www.erdosproblems.com/1048)
> - [EHP58] Erdős, P. and Herzog, F. and Piranian, G., *Metric properties of polynomials*.
>   J. Analyse Math. (1958), 125-148.
> - [Po61] Pommerenke, Ch., *On metric properties of complex polynomials*. Michigan Math. J.
>   (1961), 97-115.

*Quoted from [FormalConjectures/ErdosProblems/1048.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1048](https://www.erdosproblems.com/1048).

The file states 8 research or textbook statements: 8 solved.

## `Erdos1048.erdos_1048`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1048.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos1048.lean).

> If $f\in \mathbb{C}[x]$ is a monic polynomial with all roots satisfying
> $\lvert z\rvert \leq r$ for some $0 < r < 2$, then must
> $$\{ z: \lvert f(z)\rvert <1\}$$
> have a connected component with diameter $>2-r$?
>
> A problem of Erdős, Herzog, and Piranian [EHP58].
>
> Pommerenke [Po61] proved the answer is no for $r>1$, showing that if $f(z)=z^n-r^n$ then
> $\{ z: \lvert f(z)\rvert \leq 1\}$ has $n$ connected components, all with diameter
> $\to 0$ as $n\to \infty$.

```lean
theorem erdos_1048 :
    ¬ ∀ (r : ℝ) (f : ℂ[X]), 0 < r → r < 2 → f.Monic → f.degree ≥ 1 → (∀ z ∈ f.roots, ‖z‖ ≤ r) →
      ∃ z ∈ openLevelSet f, ENNReal.ofReal (2 - r) <
        Metric.ediam (connectedComponentIn (openLevelSet f) z)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L56).

## `Erdos1048.erdos_1048.variants.pommerenke_ncard_components`

Solved: stated here without proof.

> Pommerenke [Po61] proved the answer is no for $r>1$, showing that if $f(z)=z^n-r^n$ then
> $\{ z: \lvert f(z)\rvert \leq 1\}$ has $n$ connected components, all with diameter
> $\to 0$ as $n\to \infty$.

```lean
theorem erdos_1048.variants.pommerenke_ncard_components (r : ℝ) (hr : 1 < r) (n : ℕ) (hn : 1 ≤ n)
    (f : ℂ[X]) (hf : f = (X : ℂ[X]) ^ n - C ((r : ℂ) ^ n)) :
    {C : Set ℂ | ∃ z ∈ levelSet f, C = connectedComponentIn (levelSet f) z}.ncard = n
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L68).

## `Erdos1048.erdos_1048.variants.pommerenke_diam_tendsto_zero`

Solved: stated here without proof.

> Pommerenke [Po61] proved the answer is no for $r>1$, showing that if $f(z)=z^n-r^n$ then
> $\{ z: \lvert f(z)\rvert \leq 1\}$ has $n$ connected components, all with diameter
> $\to 0$ as $n\to \infty$.

```lean
theorem erdos_1048.variants.pommerenke_diam_tendsto_zero (r : ℝ) (hr : 1 < r) (ε : ℝ)
    (hε : 0 < ε) :
    ∀ᶠ n : ℕ in Filter.atTop, ∀ f : ℂ[X], f = (X : ℂ[X]) ^ n - C ((r : ℂ) ^ n) →
      ∀ z ∈ levelSet f,
        Metric.ediam (connectedComponentIn (levelSet f) z) < ENNReal.ofReal ε
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L79).

## `Erdos1048.erdos_1048.variants.r_le_one`

Solved: stated here without proof.

> On the other hand, if $0\lt r\leq 1$, then the answer is yes, as also shown by Pommerenke [Po61].

```lean
theorem erdos_1048.variants.r_le_one (r : ℝ) (hr₀ : 0 < r) (hr₁ : r ≤ 1) (f : ℂ[X])
    (hmonic : f.Monic) (hdeg : f.degree ≥ 1) (hroots : ∀ z ∈ f.roots, ‖z‖ ≤ r) :
    ∃ z ∈ openLevelSet f, ENNReal.ofReal (2 - r) <
      Metric.ediam (connectedComponentIn (openLevelSet f) z)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L90).

## `Erdos1048.erdos_1048.variants.diam_ge_two`

Solved: stated here without proof.

> If $0\leq r\leq 1/2$ then the component which contains $0$ must have diameter $\geq 2$, which
> $f(z)=z^n$ shows is best possible.

```lean
theorem erdos_1048.variants.diam_ge_two (r : ℝ) (hr₀ : 0 ≤ r) (hr₁ : r ≤ 1 / 2) (f : ℂ[X])
    (hmonic : f.Monic) (hdeg : f.degree ≥ 1) (hroots : ∀ z ∈ f.roots, ‖z‖ ≤ r) :
    2 ≤ Metric.ediam (connectedComponentIn (levelSet f) 0)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 101](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L101).

## `Erdos1048.erdos_1048.variants.diam_ge_two_is_best`

Solved: stated here without proof.

> If $0\leq r\leq 1/2$ then the component which contains $0$ must have diameter $\geq 2$, which
> $f(z)=z^n$ shows is best possible.

```lean
theorem erdos_1048.variants.diam_ge_two_is_best (n : ℕ) (hn : 1 ≤ n) :
    Metric.ediam (connectedComponentIn (levelSet ((X : ℂ[X]) ^ n)) 0) = 2
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 111](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L111).

## `Erdos1048.erdos_1048.variants.diam_gt_inv_r`

Solved: stated here without proof.

> If $1/2\lt r\leq \frac{\sqrt{5}-1}{2}$ then the component which contains $0$ must have
> diameter $>1/r$.

```lean
theorem erdos_1048.variants.diam_gt_inv_r (r : ℝ) (hr₀ : 1 / 2 < r)
    (hr₁ : r ≤ (Real.sqrt 5 - 1) / 2) (f : ℂ[X]) (hmonic : f.Monic) (hdeg : f.degree ≥ 1)
    (hroots : ∀ z ∈ f.roots, ‖z‖ ≤ r) :
    ENNReal.ofReal (1 / r) < Metric.ediam (connectedComponentIn (levelSet f) 0)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 120](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L120).

## `Erdos1048.erdos_1048.variants.diam_gt_two_sub_sq`

Solved: stated here without proof.

> If $\frac{\sqrt{5}-1}{2}\leq r\leq 1$ then the component which contains $0$ must have
> diameter $>2-r^2$.

```lean
theorem erdos_1048.variants.diam_gt_two_sub_sq (r : ℝ) (hr₀ : (Real.sqrt 5 - 1) / 2 ≤ r)
    (hr₁ : r ≤ 1) (f : ℂ[X]) (hmonic : f.Monic) (hdeg : f.degree ≥ 1)
    (hroots : ∀ z ∈ f.roots, ‖z‖ ≤ r) :
    ENNReal.ofReal (2 - r ^ 2) < Metric.ediam (connectedComponentIn (levelSet f) 0)
```

Category `research solved`; AMS [30 Functions of a complex variable](../../../by-subject/part-01/30-functions-of-a-complex-variable/README.md). Declared in [FormalConjectures/ErdosProblems/1048.lean, line 131](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean#L131).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1048.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1048.lean)
- [erdosproblems.com/1048](https://www.erdosproblems.com/1048)
