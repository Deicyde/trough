---
declaration: theorem
origin: cited
lean: Borsuk.borsuk_conjecture, Borsuk.borsuk_conjecture.four, Borsuk.borsuk_conjecture.four.nine_parts, Borsuk.borsuk_conjecture.four.eight_parts, Borsuk.borsuk_conjecture.one, Borsuk.borsuk_conjecture.two, Borsuk.borsuk_conjecture.three, Borsuk.borsuk_conjecture.not_forall, Borsuk.borsuk_conjecture.not_sixty_five, Borsuk.borsuk_conjecture.not_sixty_four, Borsuk.borsuk_conjecture.not_sixty_three, Borsuk.borsuk_conjecture.not_nine, Borsuk.borsuk_conjecture.not_of_nine_le
statement: formalized
---

# Borsuk's conjecture

> In 1933 Karol Borsuk [Bo33] asked whether every bounded subset of $\mathbb{R}^n$ can be
> partitioned into $n + 1$ sets, each of strictly smaller diameter. The hypothesis that the
> answer is positive became known as **Borsuk's conjecture**.
>
> The conjecture is true for $n = 2$ [Bo33] and $n = 3$ [Pe47, Eg55]. It is false in general:
> Kahn and Kalai [KK93] disproved it for $n = 1325$ and for all $n > 2014$. Bondarenko [Bo14]
> gave a counterexample in dimension $65$, and Jenrich and Brouwer [JB14] one in dimension $64$,
> the smallest refereed counterexample. In 2026 Grinsztajn [Gr26] posted a 321-point
> counterexample in dimension $63$, obtained with AI assistance and verified by exact
> computation; the same configuration was found independently by Konz and by Ji [Ji26]. In
> September 2026 an internal OpenAI model gave a compact counterexample in dimension $9$
> [OAI26]: the set of rank-one orthogonal projectors on $\mathbb{R}^4$, viewed in the
> nine-dimensional affine space of trace-one symmetric $4 \times 4$ matrices with the Frobenius
> metric, has diameter $\sqrt{2}$ and cannot be covered by $10$ sets of smaller diameter. The
> paper extends this to every dimension $n \geq 9$ (Corollary 7.1); see
> `borsuk_conjecture.not_of_nine_le`. The linked Lean proof establishes the case $n = 9$.
> The cases $4 \leq n \leq 8$ are open. In dimension $4$, every bounded set can be
> partitioned into $9$ parts of smaller diameter [La82], and a 2026 preprint reduces this to $8$
> parts [TV26].
>
> Erdős Problem 505 (`FormalConjectures.ErdosProblems.«505»`) points to this file.
>
> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Borsuk%27s_conjecture)
> - [Bo33] Borsuk, K. (1933). *Drei Sätze über die n-dimensionale euklidische Sphäre*.
>   Fundamenta Mathematicae 20, 177–190. https://doi.org/10.4064/fm-20-1-177-190
> - [Pe47] Perkal, J. (1947). *Sur la subdivision des ensembles en parties de diamètre inférieur*.
>   Colloquium Mathematicum 2, 45.
> - [Eg55] Eggleston, H. G. (1955). *Covering a three-dimensional set with sets of smaller
>   diameter*. Journal of the London Mathematical Society 30, 11–24.
>   https://doi.org/10.1112/jlms/s1-30.1.11
> - [La82] Lassak, M. (1982). *An estimate concerning Borsuk partition problem*.
>   Bulletin of the Polish Academy of Sciences, Mathematics 30(9–10), 449–451.
> - [KK93] Kahn, J., Kalai, G. (1993). *A counterexample to Borsuk's conjecture*.
>   Bulletin of the American Mathematical Society 29(1), 60–62.
>   https://arxiv.org/abs/math/9307229
> - [Bo14] Bondarenko, A. (2014). *On Borsuk's conjecture for two-distance sets*.
>   Discrete & Computational Geometry 51(3), 509–515. https://doi.org/10.1007/s00454-014-9579-4
> - [JB14] Jenrich, T., Brouwer, A. E. (2014). *A 64-dimensional counterexample to Borsuk's
>   conjecture*. Electronic Journal of Combinatorics 21(4), P4.29. https://doi.org/10.37236/4069
> - [Gr26] Grinsztajn, M. (2026). *A 63-dimensional counterexample to Borsuk's conjecture*.
>   Proof note and verification script, https://github.com/maaxgrin/borsuk-63-counterexample
> - [Ji26] Ji, Y. (2026). *An AI generated counterexample to Borsuk problem in dimension 63*.
>   https://arxiv.org/abs/2608.12561 (withdrawn as a duplicate of [Gr26])
> - [TV26] Tolmachev, A., Voronov, V. (2026). *Reducing the upper bound for the Borsuk number
>   in $\mathbb{R}^4$ to 8*. https://arxiv.org/abs/2605.19068
> - [OAI26] OpenAI (2026). *A nine-dimensional counterexample to Borsuk's covering assertion*.
>   OpenAI Math Release preprint.
>   https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/A-nine-dimensional-counterexample-to-Borsuks-covering-assertion-September-23-2026/paper.pdf
> - [OP28a] Tao, T. et al., *Optimization problems*, constant 28a (smallest Borsuk
>   counterexample dimension). https://teorth.github.io/optimizationproblems/constants/28a.html
> - [Ka15] Kalai, G. (2015). *Some old and new problems in combinatorial geometry I: Around
>   Borsuk's problem*. https://arxiv.org/abs/1505.04952

*Quoted from [FormalConjectures/Wikipedia/BorsukConjecture.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 13 research or textbook statements: 1 open, 11 solved and 1 textbook result. It also has 1 test statement and 1 API statement, counted here but not shown.

## `Borsuk.borsuk_conjecture`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/Borsuk/Main.lean#L117](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/Borsuk/Main.lean#L117).

> **Borsuk's conjecture** fails in the formerly open range $4 \leq n \leq 62$: it is not the case
> that every bounded subset of $\mathbb{R}^n$ with at least two points can be partitioned into
> $n + 1$ sets of strictly smaller diameter for every such $n$.
>
> The conjecture is true for $n \leq 3$ and false for $n \geq 9$. It was disproved in dimension
> $9$ by an internal OpenAI model in September 2026 [OAI26]; see `borsuk_conjecture.not_nine` and
> the linked Lean proof. The cases $4 \leq n \leq 8$ remain open.

```lean
theorem borsuk_conjecture : ¬ ∀ n, 4 ≤ n → n ≤ 62 → BorsukConjecture n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 141](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L141).

## `Borsuk.borsuk_conjecture.four`

Open: stated without proof.

> **Borsuk's conjecture** in dimension $4$, the smallest open case.

```lean
theorem borsuk_conjecture.four : BorsukConjecture 4
```

Category `research open`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 146](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L146).

## `Borsuk.borsuk_conjecture.four.nine_parts`

Solved: stated here without proof.

> **Partial result in dimension $4$**: every bounded subset of $\mathbb{R}^4$ with at least two
> points can be partitioned into $9$ sets of strictly smaller diameter. Proved by Lassak [La82],
> who showed more generally that $2^{n-1} + 1$ parts suffice in $\mathbb{R}^n$.

```lean
theorem borsuk_conjecture.four.nine_parts (s : Set (ℝ^4)) (hs : IsBounded s)
    (hs' : s.Nontrivial) : HasBorsukCover 9 s
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 155](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L155).

## `Borsuk.borsuk_conjecture.four.eight_parts`

Solved: stated here without proof.

> **Partial result in dimension $4$**: every bounded subset of $\mathbb{R}^4$ with at least two
> points can be partitioned into $8$ sets of strictly smaller diameter. Claimed by Tolmachev and
> Voronov [TV26] via computer-assisted partitions of a truncated Lassak cover, with floating-point
> verification; the preprint is not yet refereed.

```lean
theorem borsuk_conjecture.four.eight_parts (s : Set (ℝ^4)) (hs : IsBounded s)
    (hs' : s.Nontrivial) : HasBorsukCover 8 s
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 166](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L166).

## `Borsuk.borsuk_conjecture.one`

Textbook result, stated without proof. A Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L126](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L126).

> **Borsuk's conjecture** in dimension $1$: a bounded set of reals with at least two points
> splits at the midpoint of its smallest enclosing interval into two parts of smaller diameter.

```lean
theorem borsuk_conjecture.one : BorsukConjecture 1
```

Category `textbook`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 184](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L184).

## `Borsuk.borsuk_conjecture.two`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L131](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L131).

> **Borsuk's conjecture** in the plane, proved by Borsuk [Bo33].

```lean
theorem borsuk_conjecture.two : BorsukConjecture 2
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 192](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L192).

## `Borsuk.borsuk_conjecture.three`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L136](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L136).

> **Borsuk's conjecture** in dimension $3$, proved by Perkal [Pe47] and Eggleston [Eg55].

```lean
theorem borsuk_conjecture.three : BorsukConjecture 3
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 200](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L200).

## `Borsuk.borsuk_conjecture.not_forall`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L144](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L144).

> **Borsuk's conjecture** is false in general: Kahn and Kalai [KK93] gave counterexamples in
> dimension $1325$ and in every dimension $n > 2014$.

```lean
theorem borsuk_conjecture.not_forall : ¬ ∀ n, BorsukConjecture n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 211](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L211).

## `Borsuk.borsuk_conjecture.not_sixty_five`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L149](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L149).

> **Borsuk's conjecture** fails in dimension $65$, by Bondarenko [Bo14].

```lean
theorem borsuk_conjecture.not_sixty_five : ¬ BorsukConjecture 65
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 219](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L219).

## `Borsuk.borsuk_conjecture.not_sixty_four`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L157](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L157).

> **Borsuk's conjecture** fails in dimension $64$, by Jenrich and Brouwer [JB14]. This is the
> smallest dimension with a refereed counterexample.

```lean
theorem borsuk_conjecture.not_sixty_four : ¬ BorsukConjecture 64
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 230](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L230).

## `Borsuk.borsuk_conjecture.not_sixty_three`

Solved: stated here; a Lean proof is at [https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L166](https://github.com/mo271/formal-conjectures/blob/07a6d25f07ba0e16a916be14e9830c36cfcb9777/FormalConjectures/Wikipedia/BorsukConjecture.lean#L166).

> **Borsuk's conjecture** fails in dimension $63$, by a 321-point configuration found in 2026
> by Grinsztajn [Gr26] and independently by Konz and Ji [Ji26]. This was the smallest dimension
> with a known counterexample before [OAI26].

```lean
theorem borsuk_conjecture.not_sixty_three : ¬ BorsukConjecture 63
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 242](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L242).

## `Borsuk.borsuk_conjecture.not_nine`

Solved: stated here; a Lean proof is at [https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/Borsuk/Main.lean#L117](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Geometry/Borsuk/Main.lean#L117).

> **Borsuk's conjecture** fails in dimension $9$: the set of rank-one orthogonal projectors on
> $\mathbb{R}^4$, a compact subset of the nine-dimensional Euclidean space of trace-one symmetric
> $4 \times 4$ matrices with the Frobenius metric, has diameter $\sqrt{2}$ and cannot be covered
> by $10$ sets of smaller diameter. This was proved by an internal OpenAI model in September 2026
> [OAI26]; see the linked Lean proof. This is the smallest dimension in which the conjecture is
> currently known to be false.

```lean
theorem borsuk_conjecture.not_nine : ¬ BorsukConjecture 9
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 256](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L256).

## `Borsuk.borsuk_conjecture.not_of_nine_le`

Solved: stated here without proof.

> **Borsuk's conjecture** fails in every dimension $n \geq 9$. Corollary 7.1 of [OAI26]
> extends the dimension-nine counterexample by adjoining $n - 9$ points at diameter distance
> from one another and from the original set.

```lean
theorem borsuk_conjecture.not_of_nine_le (n : ℕ) (hn : 9 ≤ n) : ¬ BorsukConjecture n
```

Category `research solved`; AMS [52 Convex and discrete geometry](../../by-subject/part-02/52-convex-and-discrete-geometry/README.md). Declared in [FormalConjectures/Wikipedia/BorsukConjecture.lean, line 263](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean#L263).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/BorsukConjecture.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/BorsukConjecture.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Borsuk%27s_conjecture)
