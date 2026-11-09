---
declaration: theorem
origin: cited
lean: Erdos895.erdos_895, Erdos895.erdos_895.variants.eighteen, Erdos895.erdos_895.variants.hindman
statement: formalized
---

# Erdős Problem 895

> *References:*
> - [erdosproblems.com/895](https://www.erdosproblems.com/895)
> - [Er95d] Erdős, Paul, *On some problems in combinatorial set theory*. Publ. Inst. Math.
>   (Beograd) (N.S.) (1995), 61-65.

*Quoted from [FormalConjectures/ErdosProblems/895.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/895.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/895](https://www.erdosproblems.com/895).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos895.erdos_895`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean#L268](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean#L268).

> Is it true that, for all sufficiently large $n$, if $G$ is a triangle-free graph on
> $\{1,\ldots,n\}$ then there must exist three independent points $a,b,a+b$?
>
> A problem of Erdős and Hajnal [Er95d]. The stated problem has been resolved by Barber (personal
> communication) who verified using a SAT solver that this is true for all $n\geq 18$.

```lean
theorem erdos_895 :
    ∀ᶠ n in atTop, ∀ G : SimpleGraph (Set.Icc 1 n), G.CliqueFree 3 →
      ∃ a b c : Set.Icc 1 n, a ≠ b ∧ (a : ℕ) + (b : ℕ) = c ∧ G.IsIndepSet {a, b, c}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/895.lean, line 45](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/895.lean#L45).

## `Erdos895.erdos_895.variants.eighteen`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean#L243](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos895.lean#L243).

> Barber's sharp form of [erdős_895](https://www.erdosproblems.com/895): every triangle-free graph on
> $\{1,\ldots,n\}$ with $n\geq 18$ contains three independent points $a,b,a+b$.

```lean
theorem erdos_895.variants.eighteen (n : ℕ) (hn : 18 ≤ n) (G : SimpleGraph (Set.Icc 1 n))
    (hG : G.CliqueFree 3) :
    ∃ a b c : Set.Icc 1 n, a ≠ b ∧ (a : ℕ) + (b : ℕ) = c ∧ G.IsIndepSet {a, b, c}
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/895.lean, line 57](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/895.lean#L57).

## `Erdos895.erdos_895.variants.hindman`

Open: stated without proof.

> Hajnal thought that there is in fact an independent set which is a Hindman set - that is, an
> independent set of the shape
>
> $$\left\{ \sum_{i\in S}a_i : S\subseteq \{1,\ldots,k\}\right\}$$
>
> for some $a_1,\ldots,a_k$ (provided $n$ is sufficiently large depending on $k$).
>
> The general question of an independent Hindman set remains open. Here the $a_i$ are taken to be
> distinct positive integers and $S$ ranges over the nonempty subsets of $\{1,\ldots,k\}$.

```lean
theorem erdos_895.variants.hindman :
    ∀ k : ℕ, ∀ᶠ n in atTop, ∀ G : SimpleGraph (Set.Icc 1 n), G.CliqueFree 3 →
      ∃ a : Fin k → ℕ, StrictMono a ∧ ∃ I : Set (Set.Icc 1 n), G.IsIndepSet I ∧
        Subtype.val '' I = {m | ∃ S : Finset (Fin k), S.Nonempty ∧ m = ∑ i ∈ S, a i}
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/895.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/895.lean#L72).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/895.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/895.lean)
- [erdosproblems.com/895](https://www.erdosproblems.com/895)
