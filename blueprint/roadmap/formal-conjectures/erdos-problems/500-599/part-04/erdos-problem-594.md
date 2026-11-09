---
declaration: theorem
origin: cited
lean: Erdos594.erdos_594, Erdos594.erdos_594.variants.erdos_hajnal
statement: formalized
---

# Erdős Problem 594

> *References:*
> - [erdosproblems.com/594](https://www.erdosproblems.com/594)
> - [ErHa66] Erdős, P. and Hajnal, A., On chromatic number of graphs and set-systems.
>   Acta Math. Acad. Sci. Hungar. (1966), 61-99.
> - [Er69b] Erdős, P., Problems and results in chromatic graph theory. Proof Techniques in
>   Graph Theory (Proc. Second Ann Arbor Graph Theory Conf., Ann Arbor, Mich., 1968)
>   (1969), 27-35.
> - [EHS74] Erdős, P. and Hajnal, A. and Shelah, S., On some general properties of chromatic
>   numbers. Topics in topology (Proc. Colloq., Keszthely, 1972) (1974), 243-255.

*Quoted from [FormalConjectures/ErdosProblems/594.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/594.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/594](https://www.erdosproblems.com/594).

The file states 2 research or textbook statements: 2 solved. It also has 1 test statement, counted here but not shown.

## `Erdos594.erdos_594`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos594.lean#L907](https://github.com/plby/lean-proofs/blob/1268917deaaaa0d674f651287027baa26cea9920/src/latest/ErdosProblems/Erdos594.lean#L907).

> **Erdős Problem 594** (Erdős–Hajnal [ErHa66], [Er69b]):
>
> Does every graph $G$ with chromatic number $\geq \aleph_1$ contain all sufficiently
> large odd cycles?
>
> The answer is **Yes**, proved by Erdős, Hajnal, and Shelah [EHS74].
>
> A graph has chromatic number $\geq \aleph_1$ (i.e. uncountable chromatic number)
> if and only if it admits no proper colouring with countably many colours; this is
> encoded as `IsEmpty (G.Coloring ℕ)`. The conclusion states that there is some
> $N$ such that for every $k \geq N$ the graph contains a cycle of odd length $2k + 1$.

```lean
theorem erdos_594 :
    ∀ (V : Type) (G : SimpleGraph V), IsEmpty (G.Coloring ℕ) →
      ∃ N : ℕ, ∀ k : ℕ, N ≤ k →
        ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length = 2 * k + 1
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/594.lean, line 56](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/594.lean#L56).

## `Erdos594.erdos_594.variants.erdos_hajnal`

Solved: stated here without proof.

> The earlier result of Erdős and Hajnal [ErHa66]: every graph with chromatic number
> $\geq \aleph_2$ contains all sufficiently large odd cycles.
>
> Chromatic number $\geq \aleph_2$ is encoded as the nonexistence of a proper colouring
> with any set of at most $\aleph_1$ colours.

```lean
theorem erdos_594.variants.erdos_hajnal (V : Type) (G : SimpleGraph V)
    (h : ∀ (α : Type), #α ≤ ℵ_ 1 → IsEmpty (G.Coloring α)) :
    ∃ N : ℕ, ∀ k : ℕ, N ≤ k →
      ∃ (v : V) (w : G.Walk v v), w.IsCycle ∧ w.length = 2 * k + 1
```

Category `research solved`; AMS [03 Mathematical logic and foundations](../../../by-subject/part-01/03-mathematical-logic-and-foundations/README.md), [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/594.lean, line 70](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/594.lean#L70).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/594.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/594.lean)
- [erdosproblems.com/594](https://www.erdosproblems.com/594)
