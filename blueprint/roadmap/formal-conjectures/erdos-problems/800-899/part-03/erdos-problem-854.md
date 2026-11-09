---
declaration: theorem
origin: cited
lean: Erdos854.erdos_854.parts.i, Erdos854.erdos_854.parts.ii
statement: formalized
---

# Erdős Problem 854

> *References:*
> - [erdosproblems.com/854](https://www.erdosproblems.com/854)
> - [Er85c] Erdős, P., *On some of my problems in number theory I would most like to see solved*.
>   Number theory (Ootacamund, 1984), Lecture Notes in Math. 1122 (1985), 74-84.
>   [PDF](https://www.renyi.hu/~p_erdos/1985-17.pdf)
> - [Ob1] Erdős, P., *Oberwolfach Mathematical Problems*, Volume 1. Mathematisches
>   Forschungsinstitut Oberwolfach.
> - [OEIS A389839](https://oeis.org/A389839): smallest even number which cannot be written as the
>   difference of two consecutive numbers which are relatively prime to the $n$th primorial. It
>   agrees with `minEvenNonGap k` for $k\geq 3$.
> - [OEIS A048670](https://oeis.org/A048670): Jacobsthal's function of the product of the first $n$
>   primes, which is the largest gap.

*Quoted from [FormalConjectures/ErdosProblems/854.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/854.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The problem's page on erdosproblems.com: [https://www.erdosproblems.com/854](https://www.erdosproblems.com/854).

The file states 2 research or textbook statements: 2 open. It also has 1 test statement, counted here but not shown.

## `Erdos854.erdos_854.parts.i`

Open: stated without proof.

> Let $n_k$ denote the $k$th primorial, i.e. the product of the first $k$ primes.
>
> If $1=a_1\lt a_2\lt \cdots \lt a_{\phi(n_k)}=n_k-1$ is the sequence of integers coprime to $n_k$, then
> estimate the smallest even integer not of the form $a_{i+1}-a_i$. Are there
>
> $$\gg \max_i (a_{i+1}-a_i)$$
>
> many even integers of the form $a_{j+1}-a_j$?
>
> This is the first part. A problem of Erdős [Er85c, p. 80], who writes "integer" instead of "even
> integer"; all differences $a_{i+1}-a_i$ are even, so only even integers are meaningful. Here
> "estimate" is read as $\Theta$. Erdős first thought that for large $k$ every even $t \leq
> \max_i(a_{i+1}-a_i)$ is a gap, but [Ob1] reports computations of Lacampagne and Selfridge showing
> this fails for $n_6 = 30030$ (OEIS A389839 and A048670 give $20$ and $22$).

```lean
theorem erdos_854.parts.i :
    (fun k ↦ (minEvenNonGap k : ℝ)) =Θ[atTop] erdos_854.parts.i.answer
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/854.lean, line 90](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/854.lean#L90).

## `Erdos854.erdos_854.parts.ii`

Open: stated without proof.

> Let $n_k$ denote the $k$th primorial, i.e. the product of the first $k$ primes.
>
> If $1=a_1\lt a_2\lt \cdots \lt a_{\phi(n_k)}=n_k-1$ is the sequence of integers coprime to $n_k$, then
> estimate the smallest even integer not of the form $a_{i+1}-a_i$. Are there
>
> $$\gg \max_i (a_{i+1}-a_i)$$
>
> many even integers of the form $a_{j+1}-a_j$?
>
> This is the second part. We read it as: there is an absolute constant $c > 0$ such that, for all
> large $k$, the number of distinct gap values is at least $c$ times the largest gap.

```lean
theorem erdos_854.parts.ii :
    ∃ c > (0 : ℝ), ∀ᶠ k : ℕ in atTop,
      c * (maxGap (kthPrimorial k) : ℝ) ≤ ((gapSet (kthPrimorial k)).card : ℝ)
```

Category `research open`; AMS [11 Number theory](../../../by-subject/part-01/11-number-theory/README.md). Declared in [FormalConjectures/ErdosProblems/854.lean, line 106](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/854.lean#L106).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/ErdosProblems/854.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/ErdosProblems/854.lean)
- [erdosproblems.com/854](https://www.erdosproblems.com/854)
