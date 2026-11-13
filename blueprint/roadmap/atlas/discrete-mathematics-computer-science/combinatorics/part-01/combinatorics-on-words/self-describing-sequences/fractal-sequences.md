---
declaration: section
origin: cited
lean: MetaMathlibExt.FractalSequence, MetaMathlibExt.FractalSequence.pos_injective, MetaMathlibExt.FractalSequence.infinite_occurrences
statement: formalized
proof: formalized
---

# Fractal sequences

3 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences/index.html).

## Regular fractal sequence

A regular fractal sequence is a sequence $(x_n)_{n \ge 0}$ of
positive integers together with a position array $(p_i(j))_{i, j \ge 0}$ of natural numbers such
that: for every $i \ge 0$, the strictly increasing sequence $p_i(0) < p_i(1) < \cdots$ lists
exactly the positions $n$ with $x_n = i + 1$ (so every positive integer occurs infinitely often);
for all $i$ and $n$ with $x_n = i + 2$, some $m < n$ has $x_m = i + 1$; for all $h$, $i$ and $j$
with $h < i$, exactly one $k$ satisfies $p_i(j) < p_h(k) < p_i(j + 1)$; and for every $j$,
$p_i(j)$ is strictly increasing in $i$.

Source JIS VOL25/Kimberling,
<https://cs.uwaterloo.ca/journals/JIS/VOL25/Kimberling/kimber16.tex>, lines 103–219.

Source positive value `i + 1` is represented directly as the natural `i + 1`,
and `pos i j` is the zero-based position of its `j`-th occurrence.

Formalized by `MetaMathlibExt.FractalSequence`, a structure declared in [MathlibExt/Combinatorics/FractalSequence.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/FractalSequence.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences/index.html#fractal-sequence).

## Occurrence positions are distinct

In a regular fractal sequence with position array
$p$, for every $i \ge 0$ the map $j \mapsto p_i(j)$, sending $j$ to the position of the $j$-th
occurrence of $i + 1$ (counting from $j = 0$), is injective.

Formalized by `MetaMathlibExt.FractalSequence.pos_injective`, a theorem declared in [MathlibExt/Combinatorics/FractalSequence.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/FractalSequence.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences/index.html#pos-injective).

## Every value occurs infinitely often in a regular fractal sequence

Let $(x_n)_{n \ge 0}$
be a regular fractal sequence. Then for every positive integer $k$ there are infinitely many $n$
with $x_n = k$.

Formalized by `MetaMathlibExt.FractalSequence.infinite_occurrences`, a theorem declared in [MathlibExt/Combinatorics/FractalSequence.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/FractalSequence.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences/index.html#infinite-occurrences).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Fractal sequences](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/self-describing-sequences/fractal-sequences)
