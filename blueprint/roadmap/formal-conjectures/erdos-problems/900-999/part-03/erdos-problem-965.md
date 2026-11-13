---
declaration: theorem
origin: cited
lean: Erdos965.erdos_965, Erdos965.erdos_965.variants.generalization
statement: formalized
---

# Erdős Problem 965

> For every 2-coloring of ℝ, is there an uncountable set $A ⊆ ℝ$ such that
> all sums $a + b$ for $a, b ∈ A, a ≠ b$ have the same colour?
>
> *References:*
> - [erdosproblems.com/965](https://www.erdosproblems.com/965)
> - [Er75b] Erdős, Paul, Problems and results in combinatorial number theory. Journées Arithmétiques de Bordeaux (Conf., Univ. Bordeaux, Bordeaux, 1974) (1975), 295-310.
> - [HLS17] Hindman, Neil and Leader, Imre and Strauss, Dona, Pairwise sums in colourings of the reals. Abh. Math. Semin. Univ. Hambg. (2017), 275--287.
> - [Ko16] Komjáth, Péter, A certain 2-coloring of the reals. Real Anal. Exchange (2016), 227--231.
> - [SWCol] Sokoup Dániel and Weiss, William, Sums and Anti-Ramsey Colourings of ℝ. https://danieltsoukup.github.io/academic/finset_colouring.pdf

*Quoted from [FormalConjectures/ErdosProblems/965.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/965.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/965](https://www.erdosproblems.com/965).

The file states 2 research or textbook statements: 2 solved.

## `Erdos965.erdos_965`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos965.lean#L42](https://github.com/plby/lean-proofs/blob/dfe2d78128b493c572cf525b1b8edf4897fb7664/src/latest/ErdosProblems/Erdos965.lean#L42).

> Erdős asks in [Er75b] if for every 2-coloring of ℝ, there is an uncountable set $A ⊆ ℝ$ such that
> all sums $a + b$ for $a, b ∈ A, a ≠ b$ have the same colour.
>
> In [Ko16] Péter Komjáth constructed a counterexample.
> The same result was proven independently in [SWCol] by Sokoup and Weiss.

```lean
theorem erdos_965 :
    ¬ ∀ f : ℝ → Fin 2, ∃ A : Set ℝ, ¬ A.Countable ∧
      ∀ᵉ (a ∈ A) (b ∈ A) (c ∈ A) (d ∈ A), a ≠ b → c ≠ d → f (a + b) = f (c + d)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/965.lean, line 48](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/965.lean#L48).

## `Erdos965.erdos_965.variants.generalization`

Solved: stated here without proof.

> For every 2-coloring of ℝ, is there some $k ≥ 2$ and an uncountable set $A ⊆ ℝ$ such that all
> sums $a_1 + \cdots + a_k$ of $k$ distinct elements of $A$ have the same colour?
>
> In fact, in both [Ko16] and [SWCol] a single 2-coloring of ℝ is constructed such that for every
> $k ≥ 2$ and every uncountable $A ⊆ ℝ$ the sums of $k$ distinct elements of $A$ are not
> monochromatic.

```lean
theorem erdos_965.variants.generalization :
    ¬ ∀ f : ℝ → Fin 2, ∃ k ≥ 2, ∃ A : Set ℝ, ¬ A.Countable ∧ ∀ s t : Finset ℝ,
      ↑s ⊆ A → ↑t ⊆ A → s.card = k → t.card = k → f (s.sum id) = f (t.sum id)
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/965.lean, line 62](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/965.lean#L62).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/965.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/965.lean)
- [erdosproblems.com/965](https://www.erdosproblems.com/965)
