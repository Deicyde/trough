---
declaration: theorem
origin: cited
lean: Erdos72.erdos_72, Erdos72.erdos_72.variants.powers_of_two
statement: formalized
---

# Erdős Problem 72

> *References:*
> - [erdosproblems.com/72](https://www.erdosproblems.com/72)
> - [Er94b] Erdős, Paul, *Some problems in number theory, combinatorics and combinatorial geometry*.
>   Math. Pannon. (1994), 261-269.
> - [Er95] Erdős, Paul, *Some of my favourite problems in number theory, combinatorics, and
>   geometry*. Resenhas (1995), 165-186.
> - [Er97b] Erdős, Paul, *Some old and new problems in various branches of combinatorics*. Discrete
>   Math. (1997), 227-231.
> - [Er97c] Erdős, Paul, *Some of my favorite problems and results*. The mathematics of Paul
>   Erdős, I (1997), 47-67.
> - [Bo77] Bollobás, Béla, *Cycles modulo $k$*. Bull. London Math. Soc. (1977), 97-98.
> - [Ve05] Verstraete, Jacques, *Unavoidable cycle lengths in graphs*. J. Graph Theory (2005),
>   151-167.
> - [LiMo20] Liu, Hong and Montgomery, Richard, *A solution to Erdős and Hajnal's odd cycle
>   problem*. arXiv:2010.15802 (2020).

*Quoted from [FormalConjectures/ErdosProblems/72.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/72.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/72](https://www.erdosproblems.com/72).

The file states 2 research or textbook statements: 2 solved.

## `Erdos72.erdos_72`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos72.lean#L184](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos72.lean#L184).

> Is there a set $A\subset \mathbb{N}$ of density $0$ and a constant $c>0$ such that every graph on
> sufficiently many vertices with average degree $\geq c$ contains a cycle whose length is in $A$?
>
> Bollobás [Bo77] proved that such a $c$ does exist if $A$ is an infinite arithmetic progression
> containing even numbers (see [71](https://www.erdosproblems.com/71)).
>
> Erdős was 'almost certain' that if $A$ is the set of powers of $2$ then no such $c$ exists
> (although he conjectured that $n$ vertices and average degree $\gg (\log n)^{C}$ suffices for
> some $C=O(1)$). If $A$ is the set of squares (or the set of $p\pm 1$ for $p$ prime) then he had
> no guess.
>
> Solved by Verstraëte [Ve05], who gave a non-constructive proof that such a set $A$ exists.
>
> Liu and Montgomery [LiMo20] proved that in fact this is true when $A$ is the set of powers of $2$
> (more generally any set of even numbers which doesn't grow too quickly) - in particular this
> contradicts the previous belief of Erdős.

```lean
theorem erdos_72 : ∃ A : Set ℕ, A.HasDensity 0 ∧ ∃ c : ℚ, 0 < c ∧
    ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n), c ≤ G.averageDegree →
      ∃ (v : Fin n) (w : G.Walk v v), w.IsCycle ∧ w.length ∈ A
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/72.lean, line 68](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/72.lean#L68).

## `Erdos72.erdos_72.variants.powers_of_two`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos72.lean#L157](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos72.lean#L157).

> Liu and Montgomery [LiMo20] proved that there is a constant $c > 0$ such that every graph on
> sufficiently many vertices with average degree $\geq c$ contains a cycle whose length is a power
> of $2$.

```lean
theorem erdos_72.variants.powers_of_two : ∃ c : ℚ, 0 < c ∧
    ∀ᶠ n : ℕ in atTop, ∀ G : SimpleGraph (Fin n), c ≤ G.averageDegree →
      ∃ (v : Fin n) (w : G.Walk v v), w.IsCycle ∧ ∃ k : ℕ, w.length = 2 ^ k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/72.lean, line 82](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/72.lean#L82).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/72.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/72.lean)
- [erdosproblems.com/72](https://www.erdosproblems.com/72)
