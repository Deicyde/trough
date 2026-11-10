---
declaration: theorem
origin: cited
lean: Erdos664.erdos_664, Erdos664.erdos_664.variants.two_fifths, Erdos664.erdos_664.variants.block_design
statement: formalized
---

# Erdős Problem 664

> *References:*
> - [erdosproblems.com/664](https://www.erdosproblems.com/664)
> - [Er81] Erdős, P., _On the combinatorial problems which I would most like to see solved_.
>   Combinatorica (1981), 25-42.
> - [Er97f] Erdős, Paul, _Some unsolved problems_. Combinatorics, geometry and probability
>   (Cambridge, 1993) (1997), 1-10.

*Quoted from [FormalConjectures/ErdosProblems/664.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/664.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/664](https://www.erdosproblems.com/664).

The file states 3 research or textbook statements: 1 open and 2 solved.

## `Erdos664.erdos_664`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos664.lean#L214](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos664.lean#L214).

> Let $c<1$ be some constant and $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ be such that
> $\lvert A_i\rvert >c\sqrt{n}$ for all $i$ and $\lvert A_i\cap A_j\rvert\leq 1$ for all $i\neq j$.
>
> Must there exist some set $B$ such that $B\cap A_i\neq \emptyset$ and
> $\lvert B\cap A_i\rvert \ll_c 1$ for all $i$?
>
> The answer is no, proved by Alon: if $q$ is a large prime power and $n=m=q^2+q+1$ then there
> exist $A_1,\ldots,A_m\subseteq \{1,\ldots,n\}$ such that
> $\lvert A_i\rvert \geq \tfrac{2}{5}\sqrt{n}$ for all $i$ and $\lvert A_i\cap A_j\rvert\leq 1$ for
> all $i\neq j$, and yet if $B$ has non-empty intersection with all $A_i$ then there exists $A_j$
> such that $\lvert B\cap A_j\rvert \gg \log n$.

```lean
theorem erdos_664 :
    ¬ ∀ c : ℝ, 0 < c → c < 1 → ∃ K : ℕ, ∀ (n m : ℕ) (A : Fin m → Finset (Fin n)),
      (∀ i, c * √n < (A i).card) → (∀ i j, i ≠ j → (A i ∩ A j).card ≤ 1) →
        ∃ B : Finset (Fin n), (∀ i, (B ∩ A i).Nonempty) ∧
          ∀ i, (B ∩ A i).card ≤ K
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/664.lean, line 53](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/664.lean#L53).

## `Erdos664.erdos_664.variants.two_fifths`

Solved: stated here; a Lean proof is at [https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos664.lean#L214](https://github.com/plby/lean-proofs/blob/8822f7ddef30fadbd92e1c6ab4ed897af356af5e/src/latest/ErdosProblems/Erdos664.lean#L214).

> Alon's counterexample already works for $c=2/5$.

```lean
theorem erdos_664.variants.two_fifths :
    ¬ ∃ K : ℕ, ∀ (n m : ℕ) (A : Fin m → Finset (Fin n)),
      (∀ i, 2 / 5 * √n < (A i).card) → (∀ i j, i ≠ j → (A i ∩ A j).card ≤ 1) →
        ∃ B : Finset (Fin n), (∀ i, (B ∩ A i).Nonempty) ∧
          ∀ i, (B ∩ A i).card ≤ K
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/664.lean, line 64](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/664.lean#L64).

## `Erdos664.erdos_664.variants.block_design`

Open: stated without proof.

> In [Er81] the condition $\lvert A_i\cap A_j\rvert\leq 1$ for all $i\neq j$ is replaced by every
> two points in $\{1,\ldots,n\}$ being contained in exactly one $A_i$, that is,
> $A_1,\ldots,A_m$ is a pairwise balanced block design. The bound $\lvert A_i\rvert>c\sqrt{n}$ is
> kept, only the condition $c<1$ is omitted. This weaker version remains open, although Alon
> conjectures the answer there to also be no.

```lean
theorem erdos_664.variants.block_design :
    ∀ c : ℝ, 0 < c → ∃ K : ℕ, ∀ (n m : ℕ) (A : Fin m → Finset (Fin n)),
      (∀ i, c * √n < (A i).card) → (∀ x y : Fin n, x ≠ y → ∃! i, x ∈ A i ∧ y ∈ A i) →
        ∃ B : Finset (Fin n), (∀ i, (B ∩ A i).Nonempty) ∧
          ∀ i, (B ∩ A i).card ≤ K
```

Category `research open`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/664.lean, line 79](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/664.lean#L79).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/664.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/664.lean)
- [erdosproblems.com/664](https://www.erdosproblems.com/664)
