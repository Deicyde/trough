---
declaration: theorem
origin: cited
lean: Erdos357.erdos_357.parts.i, Erdos357.erdos_357.parts.ii.bigO_version, Erdos357.erdos_357.parts.ii.bigO_version_symm, Erdos357.erdos_357.parts.ii.bigTheta_version, Erdos357.erdos_357.parts.ii.littleO_version, Erdos357.erdos_357.parts.ii.littleO_version_symm, Erdos357.erdos_357.variants.weisenberg, Erdos357.erdos_357.variants.infinite_set_lower_density, Erdos357.erdos_357.variants.infinite_set_density, Erdos357.erdos_357.variants.infinite_set_sum, Erdos357.erdos_357.variants.hegyvari, Erdos357.erdos_357.variants.monotone.parts.i, Erdos357.erdos_357.variants.monotone.parts.ii.bigO_version, Erdos357.erdos_357.variants.monotone.parts.ii.bigO_version_symm, Erdos357.erdos_357.variants.monotone.parts.ii.bigTheta_version, Erdos357.erdos_357.variants.monotone.parts.ii.littleO_version, Erdos357.erdos_357.variants.monotone.parts.ii.littleO_version_symm
statement: formalized
---

# Erdős Problem 357

> *References:*
> - [erdosproblems.com/357](https://www.erdosproblems.com/357)
> - [He86] Hegyvári, Norbert, On consecutive sums in sequences. Acta Math. Hungar. (1986), 193--200.

*Quoted from [FormalConjectures/ErdosProblems/357.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/357](https://www.erdosproblems.com/357).

The file states 17 research or textbook statements: 14 open and 3 solved.

## `Erdos357.erdos_357.parts.i`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. Is $f(n)=o(n)$?

```lean
theorem erdos_357.parts.i : (fun n ↦ (f n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L45).

## `Erdos357.erdos_357.parts.ii.bigO_version`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $g = O(f)$ ?

```lean
theorem erdos_357.parts.ii.bigO_version :
    erdos_357.parts.ii.bigO_version.answer =O[atTop] (fun n ↦ (f n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 65](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L65).

## `Erdos357.erdos_357.parts.ii.bigO_version_symm`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = O(g)$ ?

```lean
theorem erdos_357.parts.ii.bigO_version_symm :
    (fun n ↦ (f n : ℝ)) =O[atTop] erdos_357.parts.ii.bigO_version_symm.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 75](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L75).

## `Erdos357.erdos_357.parts.ii.bigTheta_version`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = \Theta(g)$ ?

```lean
theorem erdos_357.parts.ii.bigTheta_version :
    (fun n ↦ (f n : ℝ)) =Θ[atTop] erdos_357.parts.ii.bigTheta_version.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 85](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L85).

## `Erdos357.erdos_357.parts.ii.littleO_version`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $g = o(f)$ ?

```lean
theorem erdos_357.parts.ii.littleO_version :
    erdos_357.parts.ii.littleO_version.answer =o[atTop] (fun n ↦ (f n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 95](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L95).

## `Erdos357.erdos_357.parts.ii.littleO_version_symm`

Open: stated without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> How does $f(n)$ grow? Can we find a (good) explicit function $g$ such that $f = o(g)$ ?

```lean
theorem erdos_357.parts.ii.littleO_version_symm :
    (fun n ↦ (f n : ℝ)) =o[atTop] erdos_357.parts.ii.littleO_version_symm.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L105).

## `Erdos357.erdos_357.variants.weisenberg`

Solved: stated here without proof.

> Let $f(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 < \dotsc < a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct.
> It is known that $f(n) \geq (2+o(1))\sqrt{n}$.
> Source: See comment by Desmond Weisenberg here: https://www.erdosproblems.com/forum/thread/357.

```lean
theorem erdos_357.variants.weisenberg : ∃ o : ℕ → ℝ, o =o[atTop] (1 : ℕ → ℝ) ∧
    ∀ᶠ n in atTop, (2 + o n) * √n ≤ f n
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 115](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L115).

## `Erdos357.erdos_357.variants.infinite_set_lower_density`

Solved: stated here without proof.

> Suppose $A$ is an infinite set such that all finite sums of consecutive terms of $A$ are distinct.
> Then $A$ has lower density 0.

```lean
theorem erdos_357.variants.infinite_set_lower_density (A : ℕ → ℕ) (hA : StrictMono A)
    (hA : HasDistinctSums A) : (Set.range A).lowerDensity = 0
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 122](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L122).

## `Erdos357.erdos_357.variants.infinite_set_density`

Open: stated without proof.

> Suppose $A$ is an infinite set such that all finite sums of consecutive terms of $A$ are distinct.
> Then it is conjectured that $A$ has density 0.

```lean
theorem erdos_357.variants.infinite_set_density (A : ℕ → ℕ) (hA : StrictMono A)
    (hA : HasDistinctSums A) :
    (Set.range A).HasDensity 0
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 129](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L129).

## `Erdos357.erdos_357.variants.infinite_set_sum`

Open: stated without proof.

> Suppose $A$ is an infinite set such that all finite sums of consecutive terms of $A$ are distinct.
> Then it is conjectured that the sum $\sum_k \frac{1}{a_k}$ converges.

```lean
theorem erdos_357.variants.infinite_set_sum (A : ℕ → ℕ) (hA : StrictMono A)
    (hA : HasDistinctSums A) :
    Summable (fun i ↦ (1 : ℝ) / A i)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 138](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L138).

## `Erdos357.erdos_357.variants.hegyvari`

Solved: stated here without proof.

> Let $g(n)$ be the maximal $k$ such that there exist integers $1 \le a_1, \dotsc, a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. Hegyvári [He86] proved
> that
>
> $$\left(\frac 1 3 + o(1) \right)n \leq g(n) \leq \left(\frac 2 3 + o(1) \right)n.$$

```lean
theorem erdos_357.variants.hegyvari : ∃ (o o' : ℕ → ℝ), o =o[atTop] (1 : ℕ → ℝ) ∧
    o' =o[atTop] (1 : ℕ → ℝ) ∧
      ∀ᶠ n in atTop, (g n : ℝ) ∈ Set.Icc ((1 / 3 + o n) * n) ((2 / 3 + o' n)*n)
```

Category `research solved`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L153).

## `Erdos357.erdos_357.variants.monotone.parts.i`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. Is $h(n)=o(n)$?

```lean
theorem erdos_357.variants.monotone.parts.i : (fun n ↦ (h n : ℝ)) =o[atTop] (fun n ↦ (n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 170](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L170).

## `Erdos357.erdos_357.variants.monotone.parts.ii.bigO_version`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. How does $h(n)$ grow?
> Can we find a (good) explicit function $g$ such that $g = O(h)$ ?

```lean
theorem erdos_357.variants.monotone.parts.ii.bigO_version :
    erdos_357.variants.monotone.parts.ii.bigO_version.answer =O[atTop] (fun n ↦ (h n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 179](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L179).

## `Erdos357.erdos_357.variants.monotone.parts.ii.bigO_version_symm`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. How does $h(n)$ grow?
> Can we find a (good) explicit function $g$ such that $h = O(g)$ ?

```lean
theorem erdos_357.variants.monotone.parts.ii.bigO_version_symm :
    (fun n ↦ (h n : ℝ)) =O[atTop] erdos_357.variants.monotone.parts.ii.bigO_version_symm.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 189](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L189).

## `Erdos357.erdos_357.variants.monotone.parts.ii.bigTheta_version`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. How does $h(n)$ grow?
> Can we find a (good) explicit function $g$ such that $h = \Theta(g)$ ?

```lean
theorem erdos_357.variants.monotone.parts.ii.bigTheta_version :
    (fun n ↦ (h n : ℝ)) =Θ[atTop] erdos_357.variants.monotone.parts.ii.bigTheta_version.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L200).

## `Erdos357.erdos_357.variants.monotone.parts.ii.littleO_version`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. How does $h(n)$ grow?
> Can we find a (good) explicit function $g$ such that $g = o(h)$ ?

```lean
theorem erdos_357.variants.monotone.parts.ii.littleO_version :
    erdos_357.variants.monotone.parts.ii.littleO_version.answer =o[atTop] (fun n ↦ (h n : ℝ))
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 210](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L210).

## `Erdos357.erdos_357.variants.monotone.parts.ii.littleO_version_symm`

Open: stated without proof.

> Let $h(n)$ be the maximal $k$ such that there exist integers $1 \le a_1 \leq \dotsc \leq a_k \le n$
> such that all sums of the shape $\sum_{u \le i \le v} a_i$ are distinct. How does $h(n)$ grow?
> Can we find a (good) explicit function $g$ such that $h = o(g)$ ?

```lean
theorem erdos_357.variants.monotone.parts.ii.littleO_version_symm :
    (fun n ↦ (h n : ℝ)) =o[atTop] erdos_357.variants.monotone.parts.ii.littleO_version_symm.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/357.lean, line 220](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean#L220).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/357.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/357.lean)
- [erdosproblems.com/357](https://www.erdosproblems.com/357)
