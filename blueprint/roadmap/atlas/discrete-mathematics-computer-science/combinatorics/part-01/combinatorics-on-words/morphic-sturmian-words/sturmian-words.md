---
declaration: section
origin: cited
lean: MetaMathlibExt.factorOnes, MetaMathlibExt.IsBalanced, MetaMathlibExt.IsAperiodic, MetaMathlibExt.IsSturmian
statement: formalized
proof: formalized
---

# Sturmian words

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html).

## Number of ones in a factor

For an infinite binary word $x = x_0 x_1 x_2 \cdots$ over
$\{0, 1\}$ and natural numbers $i$ and $n$, this is the number of indices $k < n$ with
$x_{i+k} = 1$, that is, the number of $1$s in the factor $x_i x_{i+1} \cdots x_{i+n-1}$ of length
$n$ starting at position $i$ (it is $0$ when $n = 0$).

Formalized by `MetaMathlibExt.factorOnes`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html#factor-ones).

## Balanced infinite words

An infinite binary word $x = x_0 x_1 x_2 \cdots$ over $\{0, 1\}$
is balanced when for all natural numbers $i$, $j$ and $n$, the numbers of $1$s in the factors
$x_i x_{i+1} \cdots x_{i+n-1}$ and $x_j x_{j+1} \cdots x_{j+n-1}$ of length $n$ differ by at
most $1$.

Formalized by `MetaMathlibExt.IsBalanced`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean, line 26](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean#L26). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html#is-balanced).

## Aperiodic infinite words

An infinite binary word $x = x_0 x_1 x_2 \cdots$ over $\{0, 1\}$
is aperiodic when it is not ultimately periodic: there are no natural numbers $p > 0$ and $N$
such that $x_{n+p} = x_n$ for all $n \ge N$.

Formalized by `MetaMathlibExt.IsAperiodic`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html#is-aperiodic).

## Sturmian words

An infinite binary word $x = x_0 x_1 x_2 \cdots$ over $\{0, 1\}$ is
Sturmian when it is both aperiodic and balanced.

Formalized by `MetaMathlibExt.IsSturmian`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/SturmianWord.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html#is-sturmian).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Sturmian words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/sturmian-words)
