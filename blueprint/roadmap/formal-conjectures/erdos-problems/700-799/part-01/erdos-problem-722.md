---
declaration: theorem
origin: cited
lean: Erdos722.erdos_722
statement: formalized
---

# Erdős Problem 722

> *References:*
> - [erdosproblems.com/722](https://www.erdosproblems.com/722)
> - [Ha61] Hanani, Haim, The existence and construction of balanced incomplete block designs. Ann.
>   Math. Statist. (1961), 361-386.
> - [Ke14] P. Keevash, The existence of designs. arXiv:1401.3665 (2014).
> - [Wi72] Wilson, Richard M., An existence theory for pairwise balanced designs. {II}. The structure
>   of {PBD}-closed sets and the existence conjectures. J. Combinatorial Theory Ser. A (1972), 246-273.

*Quoted from [FormalConjectures/ErdosProblems/722.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/722.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/722](https://www.erdosproblems.com/722).

The file states 1 research or textbook statement: 1 solved.

## `Erdos722.erdos_722`

Solved: stated here without proof.

> Let $k>r$ and $n$ be sufficiently large in terms of $k$ and $r$. Does there always exist a block
> $r-(n,k,1)$ design (or Steiner system with parameters $(n,k,r)$), provided the trivial necessary
> divisibility conditions $\binom{k-i}{r-i}\mid \binom{n-i}{r-i}$ are satisfied for every $0\leq i\lt r$?
> That is, can one find a family of $\binom{n}{r}\binom{k}{r}^{-1}$ many subsets of $\{1,\ldots,n\}$,
> all of size $k$, such that any $A\subseteq \{1,\ldots,n\}$ of size $r$ is contained in exactly one
> set in the family?
>
> This was proved by Keevash [Ke14] for all $(r,k)$.

```lean
theorem erdos_722 :
    ∀ r k : ℕ, 1 ≤ r → r < k → ∀ᶠ n : ℕ in atTop,
    (∀ i < r, (k - i).choose (r - i) ∣ (n - i).choose (r - i)) →
      ∃ H : Finset (Finset (Fin n)), H.IsBlockDesign r k
```

Category `research solved`; AMS [05 Combinatorics](../../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/ErdosProblems/722.lean, line 49](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/722.lean#L49).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/722.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/722.lean)
- [erdosproblems.com/722](https://www.erdosproblems.com/722)
