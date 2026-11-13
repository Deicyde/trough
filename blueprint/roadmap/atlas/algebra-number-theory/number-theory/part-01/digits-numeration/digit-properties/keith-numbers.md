---
declaration: section
origin: cited
lean: MetaMathlibExt.keithSequencePrefix, MetaMathlibExt.keithSequence, MetaMathlibExt.IsKeithNumberWithDigits, MetaMathlibExt.IsKeithNumber
statement: formalized
proof: formalized
---

# Keith numbers

4 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html).

## Keith sequence prefix

Given a list $d = (d_0, \dots, d_{k-1})$ of natural numbers and
$j \in \mathbb{N}$, the Keith sequence prefix of $d$ at step $j$ is the list of length $k + j$
obtained from $d$ by appending, $j$ times, the sum of the last $k$ entries of the current list.
This is the recurrence used for Keith numbers.

## Sources

- Martin Klazar and Florian Luca, *Counting Keith Numbers*, Journal of Integer Sequences 10 (2007), Definition in the introduction.

Formalized by `MetaMathlibExt.keithSequencePrefix`, a definition declared in [MathlibExt/NumberTheory/KeithNumber.lean, line 23](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KeithNumber.lean#L23). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html#keith-sequence-prefix).

## Keith sequence

Given a list $d = (d_0, \dots, d_{k-1})$ of natural numbers, the Keith
sequence of $d$ is the sequence $(a_m)_{m \ge 0}$ with $a_m = d_m$ for $m < k$ and
$a_m = \sum_{i=m-k}^{m-1} a_i$ for $m \ge k$: after the initial entries, each term is the sum of
the preceding $k$ terms.

Formalized by `MetaMathlibExt.keithSequence`, a definition declared in [MathlibExt/NumberTheory/KeithNumber.lean, line 33](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KeithNumber.lean#L33). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html#keith-sequence).

## Keith number with given digits

A natural number $N$ is a Keith number with digit list
$d = (d_0, \dots, d_{k-1})$ when $k \ge 2$, $d_i < 10$ for every $i$, $d_0 \ne 0$,
$N = \sum_{i=0}^{k-1} d_i \cdot 10^{k-1-i}$ (so $d$ is the decimal representation of $N$, with at
least two digits), and $N = a_m$ for some $m \ge k$, where $(a_m)_{m \ge 0}$ is the Keith sequence
of $d$ indexed from $0$ (so $N$ occurs after the initial digits).

## Sources

- Martin Klazar and Florian Luca, *Counting Keith Numbers*, Journal of Integer Sequences 10 (2007), Definition in the introduction.

Formalized by `MetaMathlibExt.IsKeithNumberWithDigits`, a definition declared in [MathlibExt/NumberTheory/KeithNumber.lean, line 42](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KeithNumber.lean#L42). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html#is-keith-number-with-digits).

## Keith number

A natural number $N$ is a Keith number when it is a Keith number with some
digit list: that is, $N$ has a decimal representation $d_0 d_1 \cdots d_{k-1}$ with $k \ge 2$
digits and leading digit $d_0 \ne 0$, and $N = a_j$ for some $j \ge k$, where $(a_m)_{m \ge 0}$ is
the Keith sequence of $(d_0, \dots, d_{k-1})$: $a_m = d_m$ for $m < k$, and each later term is the
sum of the preceding $k$ terms.

## Sources

- Martin Klazar and Florian Luca, *Counting Keith Numbers*, Journal of Integer Sequences 10 (2007), Definition in the introduction.

Formalized by `MetaMathlibExt.IsKeithNumber`, a definition declared in [MathlibExt/NumberTheory/KeithNumber.lean, line 55](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/KeithNumber.lean#L55). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html#is-keith-number).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Keith numbers](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/digits-numeration/digit-properties/keith-numbers)
