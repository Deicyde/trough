---
declaration: theorem
origin: cited
lean: Erdos1022.erdos_1022, Erdos1022.erdos_1022.variants.lt_two, Erdos1022.erdos_1022.variants.lovasz
statement: formalized
---

# Erdős Problem 1022

> *References:*
> - [erdosproblems.com/1022](https://www.erdosproblems.com/1022)
> - [Er71] Erdős, P., *Some unsolved problems in graph theory and combinatorial analysis*.
>   Combinatorial Mathematics and its Applications (Proc. Conf., Oxford, 1969) (1971), 97-109.
> - [Lo68] Lovász, L., *On covering of graphs*. Theory of Graphs (Proc. Colloq., Tihany, 1966)
>   (1968), 231-236.
> - [Wo13b] Wood, D. R., *Hypergraph colouring and degeneracy*. arXiv:1310.2972 (2013).

*Quoted from [FormalConjectures/ErdosProblems/1022.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1022.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1022](https://www.erdosproblems.com/1022).

The file states 3 research or textbook statements: 3 solved.

## `Erdos1022.erdos_1022`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/main/src/latest/ErdosProblems/Erdos1022.lean](https://github.com/plby/lean-proofs/blob/main/src/latest/ErdosProblems/Erdos1022.lean).

> Is there a constant $c_t$, where $c_t\to \infty$ as $t\to \infty$, such that if $\mathcal{F}$
> is a finite family of finite sets, all of size at least $t$, and for every set $X$ there are
> $\lt c_t\lvert X\rvert$ many $A\in \mathcal{F}$ with $A\subseteq X$, then $\mathcal{F}$ has
> chromatic number $2$ (in other words, has property B)?
>
> This is false, and $c_t<2$ for all $t$: a counterexample is provided by Wood [Wo13b], who
> constructs, for any $r\geq 2$, a triangle-free $2$-degenerate $r$-uniform hypergraph with
> chromatic number $3$. A similar counterexample was found independently by KoishiChan in the
> comments.
>
> This was formalized in Lean by Alexeev using Aristotle.

```lean
theorem erdos_1022 :
    ¬ ∃ c : ℕ → ℝ, Filter.Tendsto c Filter.atTop Filter.atTop ∧
      ∀ t : ℕ, SparseImpliesPropertyB t (c t)
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1022.lean, line 60](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1022.lean#L60).

## `Erdos1022.erdos_1022.variants.lt_two`

Solved: stated here without proof.

> This is false, and $c_t<2$ for all $t$: a counterexample is provided by Wood [Wo13b], who
> constructs, for any $r\geq 2$, a triangle-free $2$-degenerate $r$-uniform hypergraph with
> chromatic number $3$. A similar counterexample was found independently by KoishiChan in the
> comments.

```lean
theorem erdos_1022.variants.lt_two :
    ∀ (t : ℕ) (c : ℝ), SparseImpliesPropertyB t c → c < 2
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1022.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1022.lean#L72).

## `Erdos1022.erdos_1022.variants.lovasz`

Solved: stated here without proof.

> Erdős originally conjectured, in this language, that $c_2=1$, which he reports in [Er71] was
> proved by Lovász.

```lean
theorem erdos_1022.variants.lovasz :
    IsGreatest {c : ℝ | SparseImpliesPropertyB 2 c} 1
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/1022.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1022.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1022.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1022.lean)
- [erdosproblems.com/1022](https://www.erdosproblems.com/1022)
