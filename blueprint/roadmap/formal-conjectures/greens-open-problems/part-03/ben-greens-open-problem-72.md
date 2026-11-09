---
declaration: theorem
origin: cited
lean: Green72.allowedSetSize_le, Green72.NoKInLine, Green72.green_72, Green72.green_72.variants.eventually, Green72.no_three_in_line_le, Green72.no_k_in_line_big
statement: formalized
---

# Ben Green's Open Problem 72

> More commonly known as the **no-three-in-line problem**.
>
> What is the largest subset of the grid $[N]^2$ with no three points in a line? In particular,
> for $N$ sufficiently large, is it impossible to have a set of size $2N$ with this property?
>
> The upper bound $2N$ is the easy half and is `allowedSetSize_le` below, by pigeonhole on the
> columns. The open content is whether $2N$ is attained. Green records that it is for $N$ up to
> around 50, that $(3/2 + o(1))N$ points are achievable for arbitrary $N$, and that his "personal
> suspicion is that this is optimal". The Wikipedia reference points the same way: Guy and Kelly
> conjectured $c = \sqrt[3]{2\pi^2/3} \approx 1.874$, and after an error in the heuristic was found
> Guy corrected it to $c = \pi/\sqrt3 \approx 1.814$. Both are below $2$, so the expected answer to
> the question above is yes.
>
> *References:*
> - [Ben Green's Open Problem 72](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.72)
> - [Wikipedia](https://en.wikipedia.org/wiki/No-three-in-line_problem)
> - [GK2025] Grebennikov, A. Kwan, M. No $(k + 1)$-in-line problem for large constant $k$.
>   https://arxiv.org/abs/2510.17743

*Quoted from [FormalConjectures/GreensOpenProblems/72.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 3 open, 2 solved and 1 textbook result.

## `Green72.allowedSetSize_le`

Textbook result, proved here.

> By the pigeon hole principle, the size of a subset of an $N \times N$ grid such that no $k$
> points lie on a line is bounded by $\leq (k - 1) * N$.

```lean
theorem allowedSetSize_le {k : ℕ} {N : ℕ} :
    AllowedSetSize k N ≤ (k - 1) * N
```

Category `textbook`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 61](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L61).

## `Green72.NoKInLine`

Open: stated without proof.

> The **no-k-in-line problem**:
> For which $k > 2$ does every $N \times N$ grid with $N \geq k$ contain a set of $(k - 1) N$ points
> with no $k$ on a line, so that `AllowedSetSize k N` is the pigeonhole bound $(k - 1) N$?
>
> [GK2025] proves that every $k > 10^{37}$ has this property, which is `no_k_in_line_big` below,
> and does not optimise this constant. At $k = 3$ it is the property that Green expects to fail
> for large $N$, see `green_72`.

```lean
theorem NoKInLine : NoKInLine.answer = {k | 2 < k ∧ ∀ N, k ≤ N → NoKInLineFor k N}
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 98](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L98).

## `Green72.green_72`

Open: stated without proof.

> **Green's Open Problem 72 / No-three-in-line problem**:
> For $N$ sufficiently large, is it impossible to have $2N$ points in $[N]^2$ with no three in a
> line? Green suspects the answer is yes, and that $(3/2 + o(1))N$ is optimal.

```lean
theorem green_72 : ∀ᶠ N in Filter.atTop, ¬ NoKInLineFor 3 N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 105](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L105).

## `Green72.green_72.variants.eventually`

Open: stated without proof.

> Is $2N$ attained for all sufficiently large $N$?
>
> This is not the negation of `green_72`. Negating that one gives $\exists^f N$ where this asks
> $\forall^f N$, so both can be answered `False` if the behaviour oscillates. Green asks his
> question in the `green_72` form.

```lean
theorem green_72.variants.eventually : ∀ᶠ N in Filter.atTop, NoKInLineFor 3 N
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 116](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L116).

## `Green72.no_three_in_line_le`

Solved: stated here without proof.

> For $N \leq 60$, this has been verified with computers.

```lean
theorem no_three_in_line_le {N : ℕ} (hN : 3 ≤ N) (hN' : N ≤ 60) :
    NoKInLineFor 3 N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 121](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L121).

## `Green72.no_k_in_line_big`

Solved: stated here without proof.

> In [GK2025] Grebennikov and Kwan prove that the pigeonhole bound $(k - 1) N$ is attained
> for $k > 10 ^ {37}$ and $N \geq k$.

```lean
theorem no_k_in_line_big {k : ℕ} (N : ℕ) (h : 10 ^ 37 < k) (hN : k ≤ N) :
    NoKInLineFor k N
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md), [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/GreensOpenProblems/72.lean, line 128](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean#L128).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/GreensOpenProblems/72.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/GreensOpenProblems/72.lean)
- [Ben Green's Open Problem 72](https://people.maths.ox.ac.uk/greenbj/papers/open-problems.pdf#problem.72)
