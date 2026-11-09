---
declaration: theorem
origin: cited
lean: Erdos501.erdos_501, Erdos501.erdos_501.variants.erdosHajnal_finite, Erdos501.erdos_501.variants.hechler_CH, Erdos501.erdos_501.variants.closed_size3, Erdos501.erdos_501.variants.newelski_pawlikowski_seredynski, Erdos501.erdos_501.variants.gladysz_size2, Erdos501.erdos_501.variants.singleton_independent, Erdos501.erdos_501.variants.pair_independent_iff
statement: formalized
---

# Erdős Problem 501

> *References:*
> - [erdosproblems.com/501](https://www.erdosproblems.com/501)
> - [Er61] Erdős, Paul, Some unsolved problems. Magyar Tud. Akad. Mat. Kutató Int. Közl. 6
>   (1961), 221-254.
> - [ErHa71] Erdős, Paul and Hajnal, András, Unsolved problems in set theory. Axiomatic Set
>   Theory, Proc. Sympos. Pure Math. XIII Part I (1971), 17-48.
> - [ErHa60] Erdős, Paul and Hajnal, András. On some combinatorial problems involving
>   complete graphs. Acta Math. Acad. Sci. Hungar. (1960), 395-424.
> - [Gl62] Gladysz, S. Some topological properties of independent sets. Colloq. Math. (1962).
> - [He72] Hechler, S. H. A dozen small uncountable cardinals. TOPO 72, Lecture Notes
>   in Math. (1972), 207-218.
> - [NPS87] Newelski, L., Pawlikowski, J., and Seredyński, F. Infinite independent sets in
>   the closed case. Acta Math. Acad. Sci. Hungar. (1987).

*Quoted from [FormalConjectures/ErdosProblems/501.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/501](https://www.erdosproblems.com/501).

The file states 8 research or textbook statements: 1 open, 5 solved and 2 textbook results. It also has 5 test statements, counted here but not shown.

## `Erdos501.erdos_501`

Open: stated without proof.

> For every $x \in \mathbb{R}$ let $A_x \subset \mathbb{R}$ be a bounded set with outer measure
> $< 1$. Must there exist an infinite independent set, that is, some infinite $X \subseteq
> \mathbb{R}$ such that $x \notin A_y$ for all $x \neq y \in X$?
>
> If the sets $A_x$ are closed and have measure $< 1$, then must there exist an independent set
> of size $3$?
>
> Known results: Erdős–Hajnal [ErHa60] proved the existence of arbitrarily large finite
> independent sets. Hechler [He72] showed the answer is **no** assuming the continuum
> hypothesis.

```lean
theorem erdos_501 :
    ∀ (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) →
      (∀ x, volume.toOuterMeasure (A x) < 1) →
      ∃ X : Set ℝ, X.Infinite ∧ X.Pairwise (fun x y => x ∉ A y)
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 71](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L71).

## `Erdos501.erdos_501.variants.erdosHajnal_finite`

Solved: stated here without proof.

> **Erdős–Hajnal (1960): arbitrarily large finite independent sets exist.**
>
> For every `n : ℕ` and every family `A : ℝ → Set ℝ` of bounded sets with Lebesgue
> outer measure `< 1`, there exists a finite independent set of size at least `n`.
>
> This was proved by Erdős and Hajnal [ErHa60].

```lean
theorem erdos_501.variants.erdosHajnal_finite :
    ∀ (n : ℕ) (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) →
      (∀ x, volume.toOuterMeasure (A x) < 1) →
      ∃ X : Finset ℝ, n ≤ X.card ∧ (X : Set ℝ).Pairwise (fun x y => x ∉ A y)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 88](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L88).

## `Erdos501.erdos_501.variants.hechler_CH`

Solved: stated here without proof.

> **Hechler (1972) [He72]: the answer to the main question is NO, assuming the continuum
> hypothesis.**
>
> Assuming CH (`ℵ₁ = 𝔠`), there exists a family `A : ℝ → Set ℝ` of bounded sets with
> Lebesgue outer measure `< 1` for which no infinite independent set exists.

```lean
theorem erdos_501.variants.hechler_CH :
    (ℵ₁ = 𝔠) →
    ∃ (A : ℝ → Set ℝ),
      (∀ x, Bornology.IsBounded (A x)) ∧
      (∀ x, volume.toOuterMeasure (A x) < 1) ∧
      ¬ ∃ X : Set ℝ, X.Infinite ∧ X.Pairwise (fun x y => x ∉ A y)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 102](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L102).

## `Erdos501.erdos_501.variants.closed_size3`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos501.lean#L38](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos501.lean#L38).

> **Closed sets case: existence of an independent set of size 3.**
>
> If the sets `A x` are closed with Lebesgue measure `< 1`, must there exist an
> independent set of size 3?
>
> This is implied by the stronger theorem of Newelski–Pawlikowski–Seredyński [NPS87] below;
> Gladysz [Gl62] earlier proved the existence of an independent set of size 2.

```lean
theorem erdos_501.variants.closed_size3 :
    ∀ (A : ℝ → Set ℝ),
      (∀ x, IsClosed (A x)) →
      (∀ x, volume (A x) < 1) →
      ∃ X : Set ℝ, 3 ≤ X.ncard ∧ X.Pairwise (fun x y => x ∉ A y)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L121).

## `Erdos501.erdos_501.variants.newelski_pawlikowski_seredynski`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos501.lean#L31](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos501.lean#L31).

> **Newelski–Pawlikowski–Seredyński (1987) [NPS87]: infinite independent set in the closed case.**
>
> If all the sets `A x` are closed with Lebesgue measure `< 1`, then there **is** an
> infinite independent set. This gives a strong affirmative answer to the second
> question of Problem 501.

```lean
theorem erdos_501.variants.newelski_pawlikowski_seredynski :
    ∀ (A : ℝ → Set ℝ),
      (∀ x, IsClosed (A x)) →
      (∀ x, volume (A x) < 1) →
      ∃ X : Set ℝ, X.Infinite ∧ X.Pairwise (fun x y => x ∉ A y)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 137](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L137).

## `Erdos501.erdos_501.variants.gladysz_size2`

Solved: stated here without proof.

> **Gladysz (1962) [Gl62]: independent set of size 2 in the closed case.**
>
> If all the sets `A x` are closed with Lebesgue measure `< 1`, then there exist two
> distinct reals `x y` such that `x ∉ A y` and `y ∉ A x`.
>
> This is a weaker result proved by Gladysz before the full Newelski–Pawlikowski–
> Seredyński theorem [NPS87].

```lean
theorem erdos_501.variants.gladysz_size2 :
    ∀ (A : ℝ → Set ℝ),
      (∀ x, IsClosed (A x)) →
      (∀ x, volume (A x) < 1) →
      ∃ X : Set ℝ, 2 ≤ X.ncard ∧ X.Pairwise (fun x y => x ∉ A y)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 153](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L153).

## `Erdos501.erdos_501.variants.singleton_independent`

Textbook result, proved here.

> **Trivial lower bound: a single-element set is always independent.**
>
> For any family `A`, any singleton `{x}` is vacuously independent: there are no two
> distinct elements.

```lean
theorem erdos_501.variants.singleton_independent (A : ℝ → Set ℝ) (x : ℝ) :
    ({x} : Set ℝ).Pairwise (fun x y => x ∉ A y)
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L166).

## `Erdos501.erdos_501.variants.pair_independent_iff`

Textbook result, proved here.

> **Two-element sets: independent iff mutual non-membership.**
>
> A two-element set `{x, y}` (with `x ≠ y`) is independent for `A` if and only if
> `x ∉ A y` and `y ∉ A x`.

```lean
theorem erdos_501.variants.pair_independent_iff (A : ℝ → Set ℝ) {x y : ℝ} (hxy : x ≠ y) :
    ({x, y} : Set ℝ).Pairwise (fun x y => x ∉ A y) ↔ x ∉ A y ∧ y ∉ A x
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md), [28 Measure and integration](../../../by-subject/part-01/28-measure-and-integration/README.md). Declared in [FormalConjectures/ErdosProblems/501.lean, line 176](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean#L176).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/501.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/501.lean)
- [erdosproblems.com/501](https://www.erdosproblems.com/501)
