---
declaration: theorem
origin: cited
lean: Erdos1080.erdos_1080
statement: formalized
---

# Erdős Problem 1080

> *References:*
> - [erdosproblems.com/1080](https://www.erdosproblems.com/1080)
> - [DeSz92] de Caen, D. and Székely, L. A., The maximum size of {$4$}- and {$6$}-cycle free bipartite
>   graphs on {$m,n$} vertices. (1992), 135--142.
> - [Er75] Erdős, P., Some recent progress on extremal problems in graph theory. Congr. Numer. (1975),
>   3-14.
> - [LUW94] Lazebnik, F. and Ustimenko, V. A. and Woldar, A. J., New constructions of bipartite graphs
>   on {$m,n$} vertices with many edges and without small cycles. J. Combin. Theory Ser. B (1994),
>   111--117.

*Quoted from [FormalConjectures/ErdosProblems/1080.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1080.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1080](https://www.erdosproblems.com/1080).

The file states 1 research or textbook statement: 1 solved.

## `Erdos1080.erdos_1080`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1080.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.24.0/ErdosProblems/Erdos1080.lean).

> Let $G$ be a bipartite graph on $n$ vertices such that one part has $\lfloor n^{2/3}\rfloor$
> vertices. Is there a constant $c>0$ such that if $G$ has at least $cn$ edges then $G$ must
> contain a $C_6$?
>
> The answer is no, as shown by De Caen and Székely [DeSz92], who in fact show a stronger result.
> Let $f(n,m)$ be the maximum number of edges of a bipartite graph between $n$ and $m$ vertices which
> does not contain either a $C_4$ or $C_6$. A positive answer to this question would then imply
> $f(n,\lfloor n^{2/3}\rfloor)\ll n$. De Caen and Székely prove
> $n^{10/9}\gg f(n,\lfloor n^{2/3}\rfloor) \gg n^{58/57+o(1)}$ for $m\sim n^{2/3}$. They also prove
> more generally that, for $n^{1/2}\leq m\leq n$, $f(n,m) \ll (nm)^{2/3},$ which was also proved by
> Faudree and Simonovits.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_1080 :
    ¬ ∃ c > (0 : ℝ), ∀ (V : Type) [Fintype V] [Nonempty V] (G : SimpleGraph V) (X Y : Set V),
      IsBipartition G X Y → X.ncard = ⌊(Fintype.card V : ℝ) ^ (2/3 : ℝ)⌋₊ →
      G.edgeSet.ncard ≥ c * Fintype.card V →
        ∃ (v : V) (walk : G.Walk v v), walk.IsCycle ∧ walk.length = 6
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1080.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1080.lean#L61).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1080.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1080.lean)
- [erdosproblems.com/1080](https://www.erdosproblems.com/1080)
