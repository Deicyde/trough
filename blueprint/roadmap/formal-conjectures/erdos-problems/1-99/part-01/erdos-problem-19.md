---
declaration: theorem
origin: cited
lean: Erdos19.EFLConfig.le_chromaticNumber, Erdos19.EFLConfig.colorable_of_sharedColoring, Erdos19.EFLConfig.card_sharedSet_le, Erdos19.erdos_19, Erdos19.erdos_19.variants.lt_ten, Erdos19.erdos_19.variants.kahn, Erdos19.erdos_19.variants.large_n
statement: formalized
---

# Erdős Problem 19

> The Erdős–Faber–Lovász conjecture: if $G$ is an edge-disjoint union of $n$ copies of $K_n$,
> is $\chi(G) = n$?
>
> We model $G$ by a family of $n$ vertex sets of size $n$ (the copies of $K_n$) which pairwise
> share at most one vertex and which cover the vertex type. Two copies of $K_n$ are
> edge-disjoint exactly when their vertex sets share at most one vertex.
>
> *References:*
> * [erdosproblems.com/19](https://www.erdosproblems.com/19)
> * [Hi81] Hindman, N., *On a conjecture of Erdős, Faber, and Lovász about $n$-colorings*.
>   Canad. J. Math. (1981).
> * [Ka92] Kahn, J., *Coloring nearly-disjoint hypergraphs with $n + o(n)$ colors*.
>   J. Combin. Theory Ser. A (1992).
> * [KKKMO21] Kang, D. Y., Kelly, T., Kühn, D., Methuku, A. and Osthus, D., *A proof of the
>   Erdős–Faber–Lovász conjecture*. Ann. of Math. (2023).
>   [arXiv:2101.04698](https://arxiv.org/abs/2101.04698)

*Quoted from [FormalConjectures/ErdosProblems/19.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/19](https://www.erdosproblems.com/19).

The file states 7 research or textbook statements: 1 open, 3 solved and 3 textbook results. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Erdos19.EFLConfig.le_chromaticNumber`

Textbook result, proved here.

> The graph $G$ contains a copy of $K_n$, so $n \le \chi(G)$.

```lean
theorem le_chromaticNumber : (n : ℕ∞) ≤ C.graph.chromaticNumber
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L79).

## `Erdos19.EFLConfig.colorable_of_sharedColoring`

Textbook result, proved here.

> If the shared vertices can be coloured with $n$ colours so that shared vertices in a common
> clique get distinct colours, then $G$ is $n$-colourable.

```lean
theorem colorable_of_sharedColoring (c : V → Fin n)
    (hc : ∀ i u v, u ∈ C.A i → v ∈ C.A i → C.IsShared u → C.IsShared v → c u = c v → u = v) :
    C.graph.Colorable n
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 99](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L99).

## `Erdos19.EFLConfig.card_sharedSet_le`

Textbook result, proved here.

> There are at most $\binom{n}{2}$ shared vertices, since two cliques share at most one
> vertex.

```lean
theorem card_sharedSet_le : C.sharedSet.card ≤ n.choose 2
```

Category `textbook`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L155).

## `Erdos19.erdos_19`

Open: stated without proof.

> If $G$ is an edge-disjoint union of $n$ copies of $K_n$, then is $\chi(G) = n$?

```lean
theorem erdos_19 :
    ∀ (V : Type) (n : ℕ) (C : EFLConfig V n), C.graph.chromaticNumber = n
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 195](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L195).

## `Erdos19.erdos_19.variants.lt_ten`

Solved: stated here without proof.

> Hindman [Hi81] proved the Erdős–Faber–Lovász conjecture for $n < 10$.

```lean
theorem erdos_19.variants.lt_ten :
    ∀ (V : Type) (n : ℕ) (C : EFLConfig V n), n < 10 → C.graph.chromaticNumber = n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 230](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L230).

## `Erdos19.erdos_19.variants.kahn`

Solved: stated here without proof.

> Kahn [Ka92] proved that $\chi(G) \le (1 + o(1))n$.

```lean
theorem erdos_19.variants.kahn :
    ∀ ε > (0 : ℝ), ∀ᶠ n in atTop, ∀ (V : Type) (C : EFLConfig V n),
      C.graph.Colorable ⌊(1 + ε) * n⌋₊
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 238](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L238).

## `Erdos19.erdos_19.variants.large_n`

Solved: stated here without proof.

> Kang, Kelly, Kühn, Methuku and Osthus [KKKMO21] proved the Erdős–Faber–Lovász conjecture for
> all sufficiently large $n$.

```lean
theorem erdos_19.variants.large_n :
    ∀ᶠ n in atTop, ∀ (V : Type) (C : EFLConfig V n), C.graph.chromaticNumber = n
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/19.lean, line 248](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean#L248).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/19.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/19.lean)
- [erdosproblems.com/19](https://www.erdosproblems.com/19)
