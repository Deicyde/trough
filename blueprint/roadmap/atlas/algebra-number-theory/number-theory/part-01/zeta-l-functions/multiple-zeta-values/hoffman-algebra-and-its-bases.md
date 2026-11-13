---
declaration: section
origin: cited
lean: MetaMathlibExt.MultipleZeta.xWord, MetaMathlibExt.MultipleZeta.yWord, MetaMathlibExt.MultipleZeta.Index.pnatEntries, MetaMathlibExt.MultipleZeta.zWordPNat, MetaMathlibExt.MultipleZeta.zWord, MetaMathlibExt.MultipleZeta.zMonomial, MetaMathlibExt.MultipleZeta.IsHOneWord, MetaMathlibExt.MultipleZeta.IsHZeroWord
statement: formalized
proof: formalized
---

# Hoffman algebra and its bases

16 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html).

## The letter $x$ as a word

In the free monoid on the two letters $x$ and $y$, with $x$
represented by the Boolean value false and $y$ by true, this is the word of length one
consisting of the letter $x$.

Formalized by `MetaMathlibExt.MultipleZeta.xWord`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 19](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L19). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#x-word).

## The letter $y$ as a word

In the free monoid on the two letters $x$ and $y$, this is the
word of length one consisting of the single letter $y$.

The letters are encoded as booleans, with $x$ as false and $y$ as true.

Formalized by `MetaMathlibExt.MultipleZeta.yWord`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 22](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L22). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#y-word).

## Entries of an index as positive integers

For an index $(k_1, \dots, k_r)$, this is the
list $(k_1, \dots, k_r)$ of its entries in order, each regarded as a positive integer.

Formalized by `MetaMathlibExt.MultipleZeta.Index.pnatEntries`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#pnat-entries).

## Hoffman word of a list of positive integers

For a finite list $(k_1, \dots, k_r)$ of
positive integers, this is the word $z_{k_1} z_{k_2} \cdots z_{k_r}$ in the free monoid on the two
letters $x$ and $y$, where $z_k = x^{k-1} y$ is the Hoffman block of $k$. The empty list gives the
empty word.

Formalized by `MetaMathlibExt.MultipleZeta.zWordPNat`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 29](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L29). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#z-word-pnat).

## Hoffman word of an index

For an index $\mathbf{k} = (k_1, \dots, k_r)$ of positive
integers, the Hoffman word of $\mathbf{k}$ is $z_{k_1} z_{k_2} \cdots z_{k_r}$ in the free monoid on
the two letters $x$ and $y$, where $z_k = x^{k-1} y$. The empty index gives the empty word.

Formalized by `MetaMathlibExt.MultipleZeta.zWord`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#z-word).

## Hoffman monomial of an index

For an index $\mathbf{k} = (k_1, \dots, k_r)$ of positive
integers, this is the monomial $z_{k_1} z_{k_2} \cdots z_{k_r}$ with coefficient $1$ in the free
associative algebra $\mathbb{Q}\langle x, y \rangle$ over $\mathbb{Q}$ on two noncommuting letters
$x$ and $y$, where $z_k = x^{k-1} y$. In other words, it is the Hoffman word of $\mathbf{k}$ viewed
as an element of $\mathbb{Q}\langle x, y \rangle$. The empty index gives $1$.

Formalized by `MetaMathlibExt.MultipleZeta.zMonomial`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 37](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L37). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#z-monomial).

## Words of $\mathfrak{H}^1$

A word $w$ in the two letters $x$ and $y$ is an
$\mathfrak{H}^1$-word when $w$ is empty or $w = uy$ for some word $u$, that is, when $w$ is
empty or ends in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.IsHOneWord`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 43](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L43). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#is-hone-word).

## Words of $\mathfrak{H}^0$

A word $w$ in the two letters $x$ and $y$ is an
$\mathfrak{H}^0$-word when $w$ is empty or $w = xuy$ for some word $u$, that is, when $w$ is
empty or begins with $x$ and ends in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.IsHZeroWord`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 47](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L47). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#is-hzero-word).

## The monoid of $\mathfrak{H}^1$-words

This is the submonoid of the free monoid on the two
letters $x$ and $y$ consisting of the words that are empty or end in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.wordSubmonoidHOne`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 51](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L51). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#word-submonoid-hone).

## The monoid of $\mathfrak{H}^0$-words

This is the submonoid of the free monoid on the two
letters $x$ and $y$ consisting of the words that are empty or begin with $x$ and end in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.wordSubmonoidHZero`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 65](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L65). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#word-submonoid-hzero).

## The subalgebra $\mathfrak{H}^1$

Let $\mathbb{Q}\langle x, y\rangle$ be the free
associative $\mathbb{Q}$-algebra on two letters $x$ and $y$, whose monomials are the words in
$x$ and $y$. The subalgebra $\mathfrak{H}^1$ of $\mathbb{Q}\langle x, y\rangle$ is the
$\mathbb{Q}$-linear span of the words that are empty or end in $y$; equivalently, it consists
of the polynomials in which every word with nonzero coefficient is empty or ends in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.hOne`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#h-one).

## The subalgebra $\mathfrak{H}^0$

Let $\mathbb{Q}\langle x, y\rangle$ be the free
associative $\mathbb{Q}$-algebra on two letters $x$ and $y$, whose monomials are the words in
$x$ and $y$. The subalgebra $\mathfrak{H}^0$ of $\mathbb{Q}\langle x, y\rangle$ is the
$\mathbb{Q}$-linear span of the words that are empty or begin with $x$ and end in $y$;
equivalently, it consists of the polynomials in which every word with nonzero coefficient is
empty or begins with $x$ and ends in $y$.

Formalized by `MetaMathlibExt.MultipleZeta.hZero`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#h-zero).

## Empty or admissible indices

An index is empty-or-admissible when it is admissible, that
is, nonempty with first entry at least $2$, or when it has no entries.

Formalized by `MetaMathlibExt.MultipleZeta.IsHZeroIndex`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 141](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L141). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#is-hzero-index).

## The type of empty or admissible indices

The type whose elements are the indices that
are admissible, that is, nonempty with first entry at least $2$, or that have no entries.

Formalized by `MetaMathlibExt.MultipleZeta.HZeroIndex`, a definition declared in [MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean, line 145](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/WordAlgebra.lean#L145). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#hzero-index).

## Hoffman basis of $\mathfrak{H}^1$

Let $\mathfrak{H} = \mathbb{Q}\langle x, y \rangle$ be
the free associative $\mathbb{Q}$-algebra on two generators $x$ and $y$, let $\mathfrak{H}^1$ be
the $\mathbb{Q}$-linear span of the empty word and the words ending in $y$ (a subalgebra), and
for each positive integer $k$ let $z_k = x^{k-1} y$. The family of monomials
$z_{k_1} z_{k_2} \cdots z_{k_r}$, indexed by all indices $(k_1, \dots, k_r)$ of positive integers
including the empty index (whose monomial is the empty word $1$), is a basis of $\mathfrak{H}^1$
over $\mathbb{Q}$.

## Sources

- M. E. Hoffman, *The Algebra of Multiple Harmonic Series*, J. Algebra 194 (1997), 477–495, DOI 10.1006/jabr.1997.7127.

Formalized by `MathlibExt.NumberTheory.MultipleZeta.WordAlgebraWanted.hOne_basis`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/HOneBasis.lean, line 411](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/HOneBasis.lean#L411). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#h-one-basis).

## Hoffman monomial basis of $\mathfrak{H}^0$

Let $\mathbb{Q}\langle x, y\rangle$ be the free
associative $\mathbb{Q}$-algebra on two letters $x$ and $y$, and let $\mathfrak{H}^0$ be its
subalgebra consisting of the $\mathbb{Q}$-linear combinations of the empty word and of words that
begin with $x$ and end with $y$. For $k \ge 1$ put $z_k = x^{k-1} y$, and for an index
$\mathbf{k} = (k_1, \dots, k_r)$ of positive integers (possibly empty) put
$z_{\mathbf{k}} = z_{k_1} \cdots z_{k_r}$, with $z_{\mathbf{k}} = 1$ for the empty index. Call
$\mathbf{k}$ admissible if $r \ge 1$ and $k_1 \ge 2$. Then there is a $\mathbb{Q}$-basis of
$\mathfrak{H}^0$, indexed by the indices that are empty or admissible, whose element at each such
index $\mathbf{k}$ is $z_{\mathbf{k}}$.

## Sources

- M. E. Hoffman, *The Algebra of Multiple Harmonic Series*, J. Algebra 194 (1997), 477–495, DOI 10.1006/jabr.1997.7127.

Formalized by `MathlibExt.NumberTheory.MultipleZeta.WordAlgebraWanted.hZero_basis`, a theorem declared in [MathlibExt/NumberTheory/MultipleZeta/HZeroBasis.lean, line 367](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/MultipleZeta/HZeroBasis.lean#L367). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html#h-zero-basis).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Hoffman algebra and its bases](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/zeta-l-functions/multiple-zeta-values/hoffman-algebra-and-its-bases)
