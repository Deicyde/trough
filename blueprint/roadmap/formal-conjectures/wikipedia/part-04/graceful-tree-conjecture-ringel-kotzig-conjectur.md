---
declaration: theorem
origin: cited
lean: GracefulLabeling.graceful_tree_conjecture
statement: formalized
---

# Graceful Tree Conjecture (Ringel–Kotzig conjecture)

> *Reference:* [Wikipedia/Graceful_labeling](https://en.wikipedia.org/wiki/Graceful_labeling)
>
> Conjectured by Ringel (1963) and Kotzig; formalized by Rosa (1967).

*Quoted from [FormalConjectures/Wikipedia/GracefulLabeling.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GracefulLabeling.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 1 research or textbook statement: 1 open. It also has 2 test statements, counted here but not shown.

## `GracefulLabeling.graceful_tree_conjecture`

Open: stated without proof.

> Every tree admits a graceful labeling.
>
> A graceful labeling of a tree $T$ with $m$ edges is an injective map $f : V \to \{0, \dots, m\}$
> such that the multiset of absolute differences $|f(u) - f(v)|$ over edges $\{u,v\}$ of $T$
> equals $\{1, \dots, m\}$.

```lean
theorem graceful_tree_conjecture {V : Type*} [Fintype V] [DecidableEq V]
    (T : SimpleGraph V) [DecidableRel T.Adj] (hT : T.IsTree) :
    let m := T.edgeFinset.card
    ∃ f : V → ℕ,
      Function.Injective f ∧
      (∀ v, f v ≤ m) ∧
      T.edgeFinset.image (fun e =>
        e.lift ⟨fun u v => Int.natAbs ((f u : ℤ) - (f v : ℤ)),
                fun u v => by
                  show ((f u : ℤ) - f v).natAbs = ((f v : ℤ) - f u).natAbs
                  rw [← Int.natAbs_neg, neg_sub]⟩) = Finset.Icc 1 m
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/GracefulLabeling.lean, line 77](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GracefulLabeling.lean#L77).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/GracefulLabeling.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/Wikipedia/GracefulLabeling.lean)
- [Wikipedia/Graceful_labeling](https://en.wikipedia.org/wiki/Graceful_labeling)
