---
declaration: section
origin: cited
lean: MetaMathlibExt.commaMsd, MetaMathlibExt.IsCommaCandidate, MetaMathlibExt.IsCommaSucc, MetaMathlibExt.IsCommaTerminal, MetaMathlibExt.IsInfiniteCommaSeq, MetaMathlibExt.IsCommaTerminating, MetaMathlibExt.commaSequence_terminates_of_base_le_633, MetaMathlibExt.isCommaTerminal_iff_digits
statement: formalized
---

# Comma sequences

14 results, 6 proved and 8 stated but not proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html).

## Most significant digit

For natural numbers $b$ and $m$, let $k$ be the base-$b$
logarithm of $m$ rounded down, that is, the largest $k$ with $b^k \le m$ when $b \ge 2$ and
$m \ge 1$, and $k = 0$ otherwise. The most significant digit of $m$ in base $b$ is
$\lfloor m / b^k \rfloor$. When $b \ge 2$ and $m \ge 1$ this is the leading digit of the
base-$b$ expansion of $m$.

Formalized by `MetaMathlibExt.commaMsd`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 18](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L18). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#comma-msd).

## Comma candidate digits

Let $b$ and $n$ be natural numbers and let $y$ be a digit with
$0 \le y < b$. Put $m = n + b\,(n \bmod b) + y$, where $n \bmod b$ is the remainder of $n$ on
division by $b$. Then $y$ is a comma candidate for $n$ in base $b$ if $m > 0$ and the most
significant base-$b$ digit of $m$ equals $y$.

For such a candidate $y$ in base $b \ge 2$, the difference $m - n = b\,(n \bmod b) + y$ is
written with the base-$b$ digits $n \bmod b$ and $y$: the last digit of $n$ followed by the
leading digit of $m$.

Formalized by `MetaMathlibExt.IsCommaCandidate`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 25](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L25). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-comma-candidate).

## Comma successor

Let $b$, $n$ and $m$ be natural numbers. Then $m$ is the comma successor
of $n$ in base $b$ if there is a comma candidate digit $y < b$ for $n$ in base $b$ such that
$m = n + b\,(n \bmod b) + y$ and no digit $y' < y$ is a comma candidate for $n$ in base $b$.

Taking the least candidate $y$ makes $m$ the smallest possible next term.

Formalized by `MetaMathlibExt.IsCommaSucc`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 32](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L32). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-comma-succ).

## Comma-terminal numbers

Let $b$ and $n$ be natural numbers. Then $n$ is comma-terminal in
base $b$ if no digit $y$ with $0 \le y < b$ is a comma candidate for $n$ in base $b$, so $n$ has
no comma successor in base $b$.

Formalized by `MetaMathlibExt.IsCommaTerminal`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 38](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L38). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-comma-terminal).

## Infinite comma sequences

Let $b$ and $v$ be natural numbers and let
$a : \mathbb{N} \to \mathbb{N}$ be a sequence. Then $a$ is an infinite comma sequence in base $b$
starting at $v$ if $b \ge 2$, $v > 0$, $a_1 = v$, and for every $n \ge 1$ the term $a_{n+1}$ is
the comma successor of $a_n$ in base $b$.

Indexing starts at $1$; the value $a_0$ is unconstrained.

Formalized by `MetaMathlibExt.IsInfiniteCommaSeq`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 44](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L44). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-infinite-comma-seq).

## Terminating comma sequences

Let $b$ and $v$ be natural numbers. The comma sequence in
base $b$ starting at $v$ terminates if $b \ge 2$, $v > 0$, and there is no infinite comma
sequence in base $b$ starting at $v$.

Formalized by `MetaMathlibExt.IsCommaTerminating`, a definition declared in [MathlibExt/NumberTheory/CommaSequence.lean, line 50](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/MathlibExt/NumberTheory/CommaSequence.lean#L50). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-comma-terminating).

## Comma sequences terminate in bases 3 to 633

For every base $b$ with $3 \le b \le 633$
and every positive integer $v$, the comma sequence in base $b$ starting at $v$ terminates, that
is, there is no infinite comma sequence in base $b$ starting at $v$.

## Sources

- Dougherty, *Comma Sequences*, JIS 28, lines 134–137.

Stated but not proved: `MetaMathlibExt.commaSequence_terminates_of_base_le_633` is written with `theorem_wanted` in [WantedExt/NumberTheory/CommaSequenceWanted.lean, line 24](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/CommaSequenceWanted.lean#L24). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#comma-sequence-terminates-of-base-le-633).

## Landmines of the comma sequence

Let $b \ge 2$ and let $n$ be a positive integer. Then no
digit $y < b$ is a comma candidate for $n$ in base $b$ (so $n$ has no comma successor) if and
only if the base-$b$ representation of $n$, most significant digit first, is
$(b-1) \cdots (b-1)\, x\, (b-1-x)$ with some number $i \ge 0$ of leading digits $b - 1$ and
$1 \le x \le b - 2$.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 5.1.

Stated but not proved: `MetaMathlibExt.isCommaTerminal_iff_digits` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 28](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L28). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#is-comma-terminal-iff-digits).

## Numbers with two comma-children

Fix a base $b \ge 2$, and say that $n$ has at least two
comma-children if there are distinct digits $y_1 \ne y_2$ below $b$ that are both comma
candidates for $n$ in base $b$ (distinct candidates $y$ give distinct children
$n + b\,(n \bmod b) + y$). Then a positive integer $n < b^2$ has at least two comma-children if
and only if $n = (b - 1 - 2x)\, b + x$ for some $x$ with $1 \le x$ and $2x \le b - 1$; and an
integer $n \ge b^2$ has at least two comma-children if and only if its base-$b$ representation,
most significant digit first, is $d\,(b-1) \cdots (b-1)\, d\,(b-1-d)$ with some number $i \ge 0$
of middle digits $b - 1$ and $1 \le d \le b - 2$.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 5.2.

Stated but not proved: `MetaMathlibExt.two_commaChildren_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#two-comma-children-iff).

## Recovering the parent of a comma-child

Fix a base $b \ge 2$ and a natural number $n$.
Call $n$ a comma-child of $k$ if $n = k + b\,(k \bmod b) + y$ for some comma candidate digit $y$
of $k$ in base $b$. Let $f$ be the most significant base-$b$ digit of $n$ and let
$x = (n - f) \bmod b$. If $n$ is a comma-child of a positive integer $k$, then
$k = n - x b - f$; and if the integer $n - x b - f$ is negative, then $n$ is not a comma-child
of any positive integer.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Lemma 5.3.

Stated but not proved: `MetaMathlibExt.commaChild_parent_eq` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#comma-child-parent-eq).

## Numbers that are not comma successors

Let $b \ge 3$ and $n \ge b^2 - 1$. Then $n$ is not
the comma successor in base $b$ of any positive integer if and only if $n = c\, b^i$ for some
$i \ge 2$ and some $c$ with $2 \le c \le b - 1$.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 5.4.

Stated but not proved: `MetaMathlibExt.not_commaSucc_iff` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 70](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L70). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#not-comma-succ-iff).

## Every number at least the square of the base is a comma-child

Let $b \ge 2$ and
$n \ge b^2$. Then there are a positive integer $k$ and a comma candidate digit $y$ of $k$ in
base $b$ with $n = k + b\,(k \bmod b) + y$, that is, $n$ is a comma-child of $k$.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 5.5.

Stated but not proved: `MetaMathlibExt.exists_commaParent_of_sq_le` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 80](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L80). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#exists-comma-parent-of-sq-le).

## The comma-child graph has an infinite path

For every base $b \ge 2$ there is a sequence
$a_0, a_1, \dots$ of positive integers such that for every $i$ there is a comma candidate digit
$y$ of $a_i$ in base $b$ with $a_{i+1} = a_i + b\,(a_i \bmod b) + y$, that is, each $a_{i+1}$ is
a comma-child of $a_i$.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 5.6.

Stated but not proved: `MetaMathlibExt.exists_infinite_commaChild_path` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#exists-infinite-comma-child-path).

## There is a unique infinite comma-child path from 1 in base 3

There is exactly one
sequence $a_0, a_1, \dots$ of natural numbers with $a_0 = 1$ such that for every $i$ there is a
comma candidate digit $y$ of $a_i$ in base $3$ with $a_{i+1} = a_i + 3\,(a_i \bmod 3) + y$,
that is, each $a_{i+1}$ is a base-3 comma-child of $a_i$.

The paper also describes this path (at branch points it alternately takes the lower and the
higher child); that description is not part of this statement.

## Sources

- Éric Angelini, Michael S. Branicky, Giovanni Resta, N. J. A. Sloane, and David W. Wilson, *The Comma Sequence: A Simple Sequence with Bizarre Properties*, The Fibonacci Quarterly 62 (2024), no. 3, Theorem 10.1.

Stated but not proved: `MetaMathlibExt.existsUnique_commaChild_path_base_three` is written with `theorem_wanted` in [WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean, line 100](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/WantedExt/NumberTheory/Digits/CommaSequenceGraphsWanted.lean#L100). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html#exists-unique-comma-child-path-base-thre).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Comma sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/comma-sequences)
