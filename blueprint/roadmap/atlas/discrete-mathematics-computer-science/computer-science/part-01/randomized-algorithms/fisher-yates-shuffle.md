---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.randomlyPermute, Cslib.Algorithms.Lean.TimeM.randomlyPermute_time, Cslib.Algorithms.Lean.TimeM.randomlyPermute_perm, Cslib.Algorithms.Lean.TimeM.randomlyPermute_empty, Cslib.Algorithms.Lean.TimeM.randomlyPermute_singleton, Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution, Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution_apply, Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution_eq_map_uniform
statement: formalized
proof: formalized
---

# Fisher–Yates shuffle

9 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html).

## Fisher–Yates shuffle with supplied draws

Given a vector $x = (x_0, \dots, x_{n-1})$ and a
draw history $d$, which assigns to each position $i < n$ a number $d_i$ with $0 \le d_i < n - i$,
the Fisher–Yates computation processes the positions $i = 0, 1, \dots, n - 1$ in increasing order
and at position $i$ swaps the entries at positions $i$ and $i + d_i$ of the current vector. It
returns the final vector together with a cost pair in $\mathbb{N} \times \mathbb{N}$: each retrieved
draw adds $(1, 0)$ and each swap adds $(0, 1)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute`, a definition declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Basic.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Basic.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute).

## Cost of the Fisher–Yates shuffle

For every vector $x$ of length $n$ and every draw
history $d$, which assigns to each position $i < n$ a number $d_i$ with $0 \le d_i < n - i$, the
Fisher–Yates computation on $x$ and $d$ has cost pair $(n, n)$: it retrieves exactly $n$ draws
and performs exactly $n$ swaps.

When $n \ge 1$, this count includes the final draw $d_{n-1} = 0$ and the self-swap at position
$n - 1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Basic.lean, line 76](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Basic.lean#L76). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-time).

## Fisher–Yates output is a rearrangement of its input

For every vector $x$ of length $n$
and every draw history $d$, which assigns to each position $i < n$ a number $d_i$ with
$0 \le d_i < n - i$, the list of entries of the vector returned by the Fisher–Yates computation on
$x$ and $d$ is a permutation of the list of entries of $x$. In particular every value occurs
equally often in both, even when values of $x$ repeat.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-perm).

## Fisher–Yates on the empty vector

For the empty vector $x$ (of length $0$) and its empty
draw history, the Fisher–Yates computation returns $x$ with cost pair $(0, 0)$: it retrieves no
draws and performs no swaps.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean, line 213](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean#L213). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-empty).

## Fisher–Yates on a one-element vector

For every vector $x$ of length $1$ and every draw
history $d$, the Fisher–Yates computation returns $x$ unchanged with cost pair $(1, 1)$: it still
retrieves the single draw $d_0 = 0$ and performs the self-swap at position $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute_singleton`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean, line 221](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Correctness.lean#L221). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-singleton).

## Output distribution of the Fisher–Yates shuffle

For a vector $x$ of length $n$, this is
the probability distribution on outcomes (a vector of length $n$ together with a cost pair in
$\mathbb{N} \times \mathbb{N}$) obtained by choosing a draw history $d$ uniformly at random among
all assignments of a number $d_i$ with $0 \le d_i < n - i$ to each position $i < n$, and returning
the result of the Fisher–Yates computation on $x$ and $d$.

This models an ideal source of random draws, not an executable pseudorandom generator, and does
not assume that the output permutation is uniform.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution`, a definition declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean, line 233](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean#L233). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-distribution).

## Probability of a Fisher–Yates outcome

Let $x$ be a vector of length $n$, and consider the
draw histories $d$, which assign to each position $i < n$ a number $d_i$ with $0 \le d_i < n - i$.
For every outcome $o$ (a vector of length $n$ together with a cost pair), the probability that
the Fisher–Yates output distribution of $x$ assigns to $o$ equals the sum, over all draw histories
$d$ for which the Fisher–Yates computation on $x$ and $d$ yields exactly $o$, of
$\prod_{i=0}^{n-1} \frac{1}{n - i}$.

Distinct histories that yield the same outcome (for example when values of $x$ repeat) add up,
and an outcome that no history yields has probability $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution_apply`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean, line 248](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean#L248). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-distribution-apply).

## Fisher–Yates produces a uniformly random permutation

Let $x = (x_0, \dots, x_{n-1})$ be a
vector and let $\sigma$ be a permutation of $\{0, \dots, n - 1\}$ chosen uniformly at random. Then
the Fisher–Yates output distribution of $x$ equals the distribution of the outcome consisting of
the vector $(x_{\sigma(0)}, \dots, x_{\sigma(n-1)})$ with cost pair $(n, n)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermuteDistribution_eq_map_uniform`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean, line 259](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean#L259). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-distribution-eq-map-uni).

## Prefix probabilities of the Fisher–Yates shuffle

Let $k \le n$ and let
$a_0, \dots, a_{k-1}$ be distinct elements of $\{0, \dots, n - 1\}$. Run the Fisher–Yates
computation on the vector $(0, 1, \dots, n - 1)$ with every draw history $d$, which assigns to each
position $i < n$ a number $d_i$ with $0 \le d_i < n - i$, and give each history weight $1/n!$.
Then the total weight of the histories whose output vector has entry $a_p$ at position $p$ for
every $p < k$ equals $(n - k)!/n!$.

There are exactly $n!$ draw histories, so this is the probability of the prefix under a uniformly
random history. The cases $k = 0$ and $k = n$ are included.

Formalized by `Cslib.Algorithms.Lean.TimeM.randomlyPermute_prefix_probability`, a theorem declared in [CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean, line 287](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/CSLibExt/Algorithms/Lean/Random/RandomlyPermute/Probability.lean#L287). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html#randomly-permute-prefix-probability).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fisher–Yates shuffle](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/ComputerScience/randomized-algorithms/fisher-yates-shuffle)
