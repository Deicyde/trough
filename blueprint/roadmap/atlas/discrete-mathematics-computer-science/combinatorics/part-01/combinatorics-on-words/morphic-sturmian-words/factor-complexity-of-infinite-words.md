---
declaration: section
origin: cited
lean: InfiniteWord.factor, InfiniteWord.factorSet, InfiniteWord.initial, InfiniteWord.finite_factorSet, InfiniteWord.factorList, InfiniteWord.IsFactor, InfiniteWord.IsNonemptyFactor, InfiniteWord.isFactor_iff_exists_factorList
statement: formalized
proof: formalized
---

# Factor complexity of infinite words

13 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html).

## Factor of an infinite word

A right-infinite word over an alphabet $\alpha$ is a
sequence $u = u_0 u_1 u_2 \cdots$ of letters $u_n \in \alpha$. For natural numbers $k$ and $i$,
the length-$k$ factor of $u$ at position $i$ is the word $u_i u_{i+1} \cdots u_{i+k-1}$, given
as the map $\{0, \ldots, k-1\} \to \alpha$, $s \mapsto u_{i+s}$.

Formalized by `InfiniteWord.factor`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#factor).

## Set of factors of a given length

For a right-infinite word $u = u_0 u_1 u_2 \cdots$
over an alphabet $\alpha$ and a natural number $k$, the set of length-$k$ factors of $u$ is the
set of the maps $\{0, \ldots, k-1\} \to \alpha$, $s \mapsto u_{i+s}$, for $i \in \mathbb{N}$.

Formalized by `InfiniteWord.factorSet`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#factor-set).

## Initial segment of an infinite word

For a right-infinite word $u = u_0 u_1 u_2 \cdots$
over an alphabet $\alpha$ and a natural number $k$, the length-$k$ initial segment of $u$ is the
word $u_0 u_1 \cdots u_{k-1}$, given as the map $\{0, \ldots, k-1\} \to \alpha$, $s \mapsto u_s$;
it is the length-$k$ factor of $u$ at position $0$.

Formalized by `InfiniteWord.initial`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 67](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L67). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#initial).

## Finitely many factors of each length

If the alphabet $\alpha$ is finite, then for every
right-infinite word $u$ over $\alpha$ and every natural number $k$, the set of length-$k$
factors of $u$ is finite.

Formalized by `InfiniteWord.finite_factorSet`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#finite-factor-set).

## Factor as a list

For a right-infinite word $u = u_0 u_1 u_2 \cdots$ over an alphabet
$\alpha$ and natural numbers $k$ and $i$, the length-$k$ factor of $u$ at position $i$, as a
list, is $[u_i, u_{i+1}, \ldots, u_{i+k-1}]$ (the empty list when $k = 0$).

Formalized by `InfiniteWord.factorList`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 84](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L84). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#factor-list).

## Lists occurring in an infinite word

A finite list $w$ over an alphabet $\alpha$ is a
factor of a right-infinite word $u = u_0 u_1 u_2 \cdots$ over $\alpha$ when, writing $\ell$ for
the length of $w$, there is a position $i \in \mathbb{N}$ with
$w = [u_i, u_{i+1}, \ldots, u_{i+\ell-1}]$. In particular, the empty list is a factor of every
right-infinite word over $\alpha$.

Formalized by `InfiniteWord.IsFactor`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 93](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L93). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-factor).

## Nonempty factors of an infinite word

Let $u = u_0 u_1 u_2 \cdots$ be a right-infinite
word over an alphabet $\alpha$, viewed as a map $\mathbb{N} \to \alpha$. A finite word
$w = w_0 w_1 \cdots w_{n-1}$ over $\alpha$ is a nonempty factor of $u$ when $n \ge 1$ and there
is a position $i \in \mathbb{N}$ such that $w_j = u_{i+j}$ for every $j < n$.

The empty word is excluded, following the convention in which a factor is given by its
endpoints $r \le s$.

Formalized by `InfiniteWord.IsNonemptyFactor`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-nonempty-factor).

## Occurrence via list-valued factors

Let $w$ be a finite list of length $\ell$ over an
alphabet $\alpha$ and $u$ a right-infinite word over $\alpha$. Then $w$ is a factor of $u$ if and
only if there is a position $i \in \mathbb{N}$ such that the length-$\ell$ factor of $u$ at
position $i$, as a list, equals $w$.

Formalized by `InfiniteWord.isFactor_iff_exists_factorList`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 102](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L102). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-factor-iff-exists-factor-list).

## Nonempty factors via list-valued factors

Let $w$ be a finite list of length $\ell$ over
an alphabet $\alpha$ and $u = u_0 u_1 u_2 \cdots$ a right-infinite word over $\alpha$. Then $w$
is a nonempty factor of $u$ if and only if $w$ is nonempty and there is a position
$i \in \mathbb{N}$ with $[u_i, u_{i+1}, \ldots, u_{i+\ell-1}] = w$.

Formalized by `InfiniteWord.isNonemptyFactor_iff_exists_factorList`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 108](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L108). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-nonempty-factor-iff-exists-factor-lis).

## Nonempty factors are the factors that are nonempty

For a finite list $w$ over an
alphabet $\alpha$ and a right-infinite word $u$ over $\alpha$, $w$ is a nonempty factor of $u$ if
and only if $w$ is nonempty and $w$ is a factor of $u$.

Formalized by `InfiniteWord.isNonemptyFactor_iff_isFactor_and_ne_nil`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-nonempty-factor-iff-is-factor-and-ne).

## Factors as lists and as tuples agree

Let $k$ be a natural number, $v$ a map
$\{0, \ldots, k-1\} \to \alpha$, written $j \mapsto v_j$, and $u$ a right-infinite word over
$\alpha$. Then the list $[v_0, v_1, \ldots, v_{k-1}]$ is a factor of $u$ if and only if $v$
belongs to the set of length-$k$ factors of $u$. This holds also for $k = 0$.

Formalized by `InfiniteWord.isFactor_ofFn_iff_mem_factorSet`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/Factor.lean, line 150](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/Factor.lean#L150). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#is-factor-of-fn-iff-mem-factor-set).

## Factor complexity of an infinite word

Let $w = w_0 w_1 w_2 \cdots$ be an infinite word
over a finite alphabet $A$. For $n \ge 0$ and a position $i \ge 0$, the factor of $w$ of length
$n$ at position $i$ is the word $w_i w_{i+1} \cdots w_{i+n-1}$. The factor complexity $p_w(n)$ is
the number of distinct factors of $w$ of length $n$, each word being counted once however often it
occurs in $w$.

## Sources

- Fabien Durand, Julien Leroy, and Gwenaël Richomme, *Do the Properties of an S-adic Representation Determine Factor Complexity?*, Journal of Integer Sequences 16 (2013), Article 13.2.6, complexity-function definition, lines 117–128, <https://cs.uwaterloo.ca/journals/JIS/VOL16/Durand/durand2.tex>.

Formalized by `MetaMathlibExt.wordFactorComplexity`, a definition declared in [MathlibExt/Combinatorics/InfiniteWord/WordFactorComplexity.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/WordFactorComplexity.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#word-factor-complexity).

## Factor complexity at length zero

For every infinite word $w$ over a finite alphabet,
the factor complexity of $w$ at length $0$ equals $1$, that is, $p_w(0) = 1$: the empty word is
the only factor of $w$ of length $0$.

Formalized by `MetaMathlibExt.wordFactorComplexity_zero`, a theorem declared in [MathlibExt/Combinatorics/InfiniteWord/WordFactorComplexity.lean, line 34](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/Combinatorics/InfiniteWord/WordFactorComplexity.lean#L34). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html#word-factor-complexity-zero).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Factor complexity of infinite words](https://deicyde.github.io/atlas-lean/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/Combinatorics/combinatorics-on-words/morphic-sturmian-words/factor-complexity-of-infinite-words)
