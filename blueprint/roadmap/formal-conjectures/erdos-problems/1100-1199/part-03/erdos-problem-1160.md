---
declaration: theorem
origin: cited
lean: Erdos1160.erdos_1160, Erdos1160.erdos_1160.variants.sum
statement: formalized
---

# Erdős Problem 1160

> *References:*
> - [erdosproblems.com/1160](https://www.erdosproblems.com/1160)
> - [Va99] Various, *Some of Paul's favorite problems*. Booklet produced for the conference
>   "Paul Erdős and his mathematics", Budapest, July 1999 (1999).
> - [BNV07] Blackburn, S. R., Neumann, P. M. and Venkataraman, G., *Enumeration of finite groups*.
>   Cambridge Tracts in Mathematics 173, Cambridge University Press (2007), xii+281.
> - [Pa03] Pantelidakis, I., *On the Number of Non-isomorphic Groups of the Same Order*. DPhil
>   thesis, University of Oxford (2003).

*Quoted from [FormalConjectures/ErdosProblems/1160.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1160.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/1160](https://www.erdosproblems.com/1160).

The file states 2 research or textbook statements: 2 open. It also has 1 test statement, counted here but not shown.

## `Erdos1160.erdos_1160`

Open: stated without proof.

> Let $g(n)$ denote the number of groups of order $n$. If $n\leq 2^m$ then
> $g(n)\leq g(2^m)$.
>
> This is [Va99, 5.71] and an open problem (Question 22.16) in [BNV07], where its origin could not
> be traced. It has been attributed to Erdős, Higman and others. Pantelidakis [Pa03] proved it for
> odd $n$ and $m\geq 3619$.
>
> It is a conjecture, not a question. We take $n\geq 1$; for $n=0$ it holds trivially, since
> $g(0)=0$.

```lean
theorem erdos_1160 : ∀ n m : ℕ, 0 < n → n ≤ 2 ^ m → g n ≤ g (2 ^ m)
```

Category `research open`; AMS [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1160.lean, line 72](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1160.lean#L72).

## `Erdos1160.erdos_1160.variants.sum`

Open: stated without proof.

> Question 22.18 of [BNV07] suggests the even stronger conjecture
>
> $$\sum_{n<2^m}g(n) \leq g(2^m)$$
>
> for all sufficiently large $m$ (perhaps even as soon as $m\geq 7$).
>
> The sum is over $1\leq n<2^m$.

```lean
theorem erdos_1160.variants.sum :
    ∀ᶠ m : ℕ in atTop, ∑ n ∈ Finset.Ico 1 (2 ^ m), g n ≤ g (2 ^ m)
```

Category `research open`; AMS [20 Group theory and generalizations](../../../by-subject/part-01/20-group-theory-and-generalizations/README.md). Declared in [FormalConjectures/ErdosProblems/1160.lean, line 81](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1160.lean#L81).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/1160.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/1160.lean)
- [erdosproblems.com/1160](https://www.erdosproblems.com/1160)
