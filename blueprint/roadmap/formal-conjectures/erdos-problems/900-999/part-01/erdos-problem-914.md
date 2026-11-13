---
declaration: theorem
origin: cited
lean: Erdos914.erdos_914, Erdos914.erdos_914.variants.equitable_colouring
statement: formalized
---

# Erdős Problem 914

> *References:*
> - [erdosproblems.com/914](https://www.erdosproblems.com/914)
> - [CoHa63] Corrádi, K. and Hajnal, A., *On the maximal number of independent circuits in a graph*.
>   Acta Math. Acad. Sci. Hungar. (1963), 423-439.
> - [HaSz70] Hajnal, A. and Szemerédi, E., *Proof of a conjecture of P. Erdős*. (1970), 601-623.
> - [KiKo08] Kierstead, H. A. and Kostochka, A. V., *A short proof of the Hajnal-Szemerédi theorem on
>   equitable colouring*. Combin. Probab. Comput. (2008), 265-270.

*Quoted from [FormalConjectures/ErdosProblems/914.lean](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/914.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [5258ab9a](https://github.com/google-deepmind/formal-conjectures/tree/5258ab9ac6db5eb0047aa4100ea0f995c5466da6), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/914](https://www.erdosproblems.com/914).

The file states 2 research or textbook statements: 2 solved.

## `Erdos914.erdos_914`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos914.lean](https://github.com/plby/lean-proofs/blob/main/src/v4.29.1/ErdosProblems/Erdos914.lean).

> Let $r\geq 2$ and $m\geq 1$. Every graph with $rm$ vertices and minimum degree at least $m(r-1)$
> contains $m$ vertex disjoint copies of $K_r$.
>
> When $r=2$ this follows from Dirac's theorem. Corrádi and Hajnal [CoHa63] proved this when $r=3$.
> Hajnal and Szemerédi [HaSz70] proved this for all $r\geq 4$.
>
> A shorter proof was given by Kierstead and Kostochka [KiKo08].

```lean
theorem erdos_914 {r m : ℕ} (hr : 2 ≤ r) (hm : 1 ≤ m) {V : Type*} [Fintype V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hV : Fintype.card V = r * m)
    (hdeg : m * (r - 1) ≤ G.minDegree) :
    ∃ K : Fin m → Finset V, (∀ i, G.IsNClique r (K i)) ∧
      Pairwise fun i j => Disjoint (K i) (K j)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/914.lean, line 47](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/914.lean#L47).

## `Erdos914.erdos_914.variants.equitable_colouring`

Solved: stated here without proof.

> Equivalently, every graph with $rm$ vertices and maximum degree at most $m-1$ has a proper vertex
> colouring with $m$ colours in which every colour class has exactly $r$ vertices (an equitable
> colouring).

```lean
theorem erdos_914.variants.equitable_colouring {r m : ℕ} (hr : 2 ≤ r) (hm : 1 ≤ m) {V : Type*}
    [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj] (hV : Fintype.card V = r * m)
    (hdeg : G.maxDegree ≤ m - 1) :
    ∃ C : G.Coloring (Fin m), ∀ i, (C.colorClass i).ncard = r
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/914.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/914.lean#L60).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/914.lean at 5258ab9a](https://github.com/google-deepmind/formal-conjectures/blob/5258ab9ac6db5eb0047aa4100ea0f995c5466da6/FormalConjectures/ErdosProblems/914.lean)
- [erdosproblems.com/914](https://www.erdosproblems.com/914)
