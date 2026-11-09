---
declaration: theorem
origin: cited
lean: Erdos602.erdos_602, Erdos602.erdos_602.variants.disjoint, Erdos602.erdos_602.variants.countable_index, Erdos602.erdos_602.variants.single_set, Erdos602.erdos_602.variants.empty_index, Erdos602.erdos_602.variants.unique_index, Erdos602.erdos_602.variants.two_sets, Erdos602.disjoint_without_infinite_claim.disproof
statement: formalized
---

# Erdős Problem 602

> *Reference:* [erdosproblems.com/602](https://www.erdosproblems.com/602)

*Quoted from [FormalConjectures/ErdosProblems/602.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/602](https://www.erdosproblems.com/602).

The file states 8 research or textbook statements: 1 open, 4 solved and 3 textbook results.

## `Erdos602.erdos_602`

Open: stated without proof.

> Does every almost-disjoint family of countably infinite sets whose pairwise
> intersections all have size ≠ 1 have Property B?
>
> Formally: let `α` be any type, let `(A_i)_{i ∈ I}` be a family of countably infinite subsets
> of `α` such that for all `i ≠ j`, the intersection `A_i ∩ A_j` is finite and
> `|A_i ∩ A_j| ≠ 1`. Does there exist a 2-colouring `f : α → Fin 2` such that no `A_i` is
> monochromatic?
>
> This is an open question about Property B for almost-disjoint families with a
> forbidden intersection size of 1.
>
> **Note:** This generalises the formulation in which the ground set is `ℕ`. Since every
> countably infinite set is in bijection with `ℕ`, the two formulations are equivalent, but
> working over an arbitrary ground type makes the statement apply immediately to, e.g.,
> almost-disjoint families of countable subsets of an uncountable space.

```lean
theorem erdos_602 :
    ∀ {α : Type*} {I : Type*} (A : I → Set α),
      (∀ i, (A i).Countable ∧ (A i).Infinite) →
      (∀ i j, i ≠ j → (A i ∩ A j).Finite) →
      (∀ i j, i ≠ j → Set.ncard (A i ∩ A j) ≠ 1) →
      HasPropertyB I A
```

Category `research open`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 78](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L78).

## `Erdos602.erdos_602.variants.disjoint`

Proved here.

> **Trivial case: pairwise disjoint families.**
>
> If the `A_i` are pairwise disjoint (all intersections are empty, which in
> particular satisfies `|A_i ∩ A_j| ≠ 1`), then Property B holds trivially.
>
> **Proof sketch:** Since each `A_i` is infinite, it has (at least) two distinct elements
> `a_i` and `b_i`. We can define a colouring that assigns colour 0 to `a_i` and colour 1
> to `b_i` for each `i` (using disjointness, these choices don't conflict), and extend
> arbitrarily elsewhere. Then no `A_i` is monochromatic.

```lean
theorem erdos_602.variants.disjoint :
    ∀ {α : Type*} {I : Type*} (A : I → Set α),
      (∀ i, (A i).Infinite) →
      (∀ i j, i ≠ j → Disjoint (A i) (A j)) →
      HasPropertyB I A
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L99).

## `Erdos602.erdos_602.variants.countable_index`

Solved: stated here without proof.

> **Countable index set case.**
>
> If the index set is countable, the answer is yes, and the intersection
> condition is unnecessary. This is Bernstein's Lemma:
> every countable system of infinite sets has Property B.

```lean
theorem erdos_602.variants.countable_index :
    ∀ {α : Type*} (A : ℕ → Set α),
      (∀ i, (A i).Countable ∧ (A i).Infinite) →
      (∀ i j, i ≠ j → (A i ∩ A j).Finite) →
      (∀ i j, i ≠ j → Set.ncard (A i ∩ A j) ≠ 1) →
      HasPropertyB ℕ A
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 156](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L156).

## `Erdos602.erdos_602.variants.single_set`

Textbook result, proved here.

> **Intersections of size ≥ 2 suffice.**
>
> For a single countably infinite set `A ⊆ α`, there trivially exists a 2-colouring
> of `α` that makes `A` non-monochromatic: since `A` is infinite, it has two distinct
> elements, so any colouring that assigns them different colours works.

```lean
theorem erdos_602.variants.single_set {α : Type*} (A : Set α) (hA : A.Infinite) :
    ∃ f : α → Fin 2, ¬IsMonochromatic f A
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 171](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L171).

## `Erdos602.erdos_602.variants.empty_index`

Textbook result, proved here.

> **Empty index set.**
>
> If the index set `I` is empty (has no elements), then Property B holds vacuously:
> any 2-colouring works, since there are no sets to be made non-monochromatic.

```lean
theorem erdos_602.variants.empty_index {α : Type*} :
    ∀ (A : PEmpty → Set α),
      (∀ i, (A i).Infinite) →
      HasPropertyB PEmpty A
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 204](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L204).

## `Erdos602.erdos_602.variants.unique_index`

Textbook result, proved here.

> **Unique index set.**
>
> If the index set has exactly one element (i.e., `[Unique I]`), then Property B holds:
> any 2-colouring that makes the single set `A (default : I)` non-monochromatic works.
> This follows from the single-set case.

```lean
theorem erdos_602.variants.unique_index {α : Type*} (I : Type*) [Unique I]
    (A : I → Set α) (hInfinite : ∀ i, (A i).Infinite) :
    HasPropertyB I A
```

Category `textbook`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 218](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L218).

## `Erdos602.erdos_602.variants.two_sets`

Proved here.

> **Two infinite sets with pairwise intersection of size ≠ 1.**
>
> If the family consists of exactly two countably infinite sets `A₀` and `A₁` with
> `|A₀ ∩ A₁| ≠ 1` (and finite), then Property B holds.
>
> **Proof sketch:**
> - If `A₀ ∩ A₁ = ∅`: the sets are disjoint. Pick distinct `a, b ∈ A₀` and distinct
>   `c, d ∈ A₁`. Colour `b` and `c` with 1, everything else with 0. Then `A₀` has
>   `a` (colour 0) and `b` (colour 1), and `A₁` has `c` (colour 1) and `d` (colour 0),
>   so neither is monochromatic.
> - If `|A₀ ∩ A₁| ≥ 2`: the intersection contains two distinct points `x` and `y`.
>   Assign `x` colour 0 and `y` colour 1. Both `A₀` and `A₁` contain `x` and `y`,
>   so neither is monochromatic.

```lean
theorem erdos_602.variants.two_sets :
    ∀ {α : Type*} (A : Fin 2 → Set α),
      (∀ i, (A i).Infinite) →
      (A 0 ∩ A 1).Finite →
      Set.ncard (A 0 ∩ A 1) ≠ 1 →
      HasPropertyB (Fin 2) A
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 243](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L243).

## `Erdos602.disjoint_without_infinite_claim.disproof`

Proved here.

> Formal disproof of `disjoint_without_infinite_claim`.
>
> **Counterexample:** Take `α = ℕ`, `I = Fin 2`, with `A 0 = {0}` and `A 1 = {1}`.
> These are pairwise disjoint, satisfying the only hypothesis. But singleton sets
> are vacuously monochromatic under any colouring: the only pair `(x, y) ∈ {0} × {0}`
> is `(0, 0)`, and `f 0 = f 0` trivially. So any colouring makes `A 0` monochromatic,
> meaning `HasPropertyB` fails.

```lean
theorem disjoint_without_infinite_claim.disproof :
    ¬ disjoint_without_infinite_claim
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md). Declared in [FormalConjectures/ErdosProblems/602.lean, line 449](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean#L449).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/602.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/602.lean)
- [erdosproblems.com/602](https://www.erdosproblems.com/602)
