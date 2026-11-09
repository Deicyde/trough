---
declaration: theorem
origin: cited
lean: SnakeInBox.snake_small_dimensions, SnakeInBox.coil_small_dimensions, SnakeInBox.snake_dim_nine, SnakeInBox.snake_dim_nine_lower_bound, SnakeInBox.snake_upper_bound, SnakeInBox.coil_upper_bound
statement: formalized
---

# Snake in the box

> *References:*
> - [Wikipedia](https://en.wikipedia.org/wiki/Snake-in-the-box)
> - [Hypercube](https://en.wikipedia.org/wiki/Hypercube_graph)
> - [xkcd](https://xkcd.com/3125/)
> - [DK67] L. Danzer and V. Klee, *Lengths of snakes in boxes*, Journal of Combinatorial Theory 2
>   (1967), 258–265.
> - [Ze97] G. Zémor, *An upper bound on the size of the snake-in-the-box*, Combinatorica 17
>   (1997), 287–298.

*Quoted from [FormalConjectures/Wikipedia/SnakeInTheBox.lean](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean) in [Formal Conjectures](https://github.com/google-deepmind/formal-conjectures) (Google DeepMind) at commit [2055e5ad](https://github.com/google-deepmind/formal-conjectures/tree/2055e5adadae0b2e392365938faa82ef6f1464f0), Apache-2.0, as are the docstrings and Lean statements below.*

The file states 6 research or textbook statements: 1 open and 5 solved. It also has 2 test statements, counted here but not shown.

## `SnakeInBox.snake_small_dimensions`

Solved: stated here without proof.

> The maximum length for the snake-in-the-box problem is known for dimensions zero through eight;
> it is $0, 1, 2, 4, 7, 13, 26, 50, 98$.

```lean
theorem snake_small_dimensions :
    map LongestSnakeInTheBox (range 9) = [0, 1, 2, 4, 7, 13, 26, 50, 98]
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 125](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L125).

## `SnakeInBox.coil_small_dimensions`

Solved: stated here without proof.

> The maximum length for the coil-in-the-box problem is known for dimensions zero through eight;
> it is $0, 0, 4, 6, 8, 14, 26, 48, 96$.

```lean
theorem coil_small_dimensions :
    map LongestCoilInTheBox (range 9) = [0, 0, 4, 6, 8, 14, 26, 48, 96]
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 134](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L134).

## `SnakeInBox.snake_dim_nine`

Open: stated without proof.

> For dimension $9$, the length of the longest snake in the box is not known.
> This is currently the smallest dimension where this question is open.

```lean
theorem snake_dim_nine : LongestSnakeInTheBox 9 = snake_dim_nine.answer
```

Category `research open`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 145](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L145).

## `SnakeInBox.snake_dim_nine_lower_bound`

Solved: stated here without proof.

> The best length found so far for dimension nine is 190.

```lean
theorem snake_dim_nine_lower_bound : 190 ≤ LongestSnakeInTheBox 9
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 152](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L152).

## `SnakeInBox.snake_upper_bound`

Solved: stated here without proof.

> For $n \geq 1$, an upper bound on the length of the longest snake in a box is $2^{n-1}$
> (see [DK67, Theorem B]).

```lean
theorem snake_upper_bound (n : ℕ) (hn : 1 ≤ n) : LongestSnakeInTheBox n ≤ 2 ^ (n - 1)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 162](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L162).

## `SnakeInBox.coil_upper_bound`

Solved: stated here without proof.

> For $n \geq 2$, an upper bound on the maximal length of the longest coil in a box is given by
> $$
> 1 + 2^{n-1}\frac{6n}{6n + \frac{1}{6\sqrt{6}}n^{\frac 1 2} - 7}
> $$
> (see [Ze97]). The case $n = 1$ is excluded since the right-hand side is negative there.

```lean
theorem coil_upper_bound (n : ℕ) (hn : 2 ≤ n) : LongestCoilInTheBox n
    ≤ (1 : ℝ) + 2 ^ (n - 1) * (6 * n) / (6 * n + (1 / (6 * √6) * √n) - 7)
```

Category `research solved`; AMS [05 Combinatorics](../../by-subject/part-01/05-combinatorics/README.md). Declared in [FormalConjectures/Wikipedia/SnakeInTheBox.lean, line 173](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean#L173).

## Depends on

No dependencies are recorded: this chapter reads Formal Conjectures' source text without running Lean, which edges between statements need.

## Sources

- [FormalConjectures/Wikipedia/SnakeInTheBox.lean at 2055e5ad](https://github.com/google-deepmind/formal-conjectures/blob/2055e5adadae0b2e392365938faa82ef6f1464f0/FormalConjectures/Wikipedia/SnakeInTheBox.lean)
- [Wikipedia](https://en.wikipedia.org/wiki/Snake-in-the-box)
