---
declaration: section
origin: cited
lean: MetaMathlibExt.normalSeq, MetaMathlibExt.normalSeq_one, MetaMathlibExt.normalSeq_two, MetaMathlibExt.normalSeq_recurrence, MetaMathlibExt.normalSeqFib, MetaMathlibExt.normalSeqFib_add, MetaMathlibExt.normalSeq_odd_identity
statement: formalized
proof: formalized
---

# Normal second-order sequences

7 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html).

## Normal second-order number sequence

For integers $a_1$ and $a_2$, the normal
second-order number sequence $(u_n)_{n \ge 0}$ with coefficients $a_1, a_2$ is the integer
sequence defined by $u_0 = 0$, $u_1 = 1$ and $u_{n+2} = a_1 u_{n+1} + a_2 u_n$ for every
$n \ge 0$.

The source requires $a_1$ and $a_2$ to be nonzero and starts the sequence at $u_1$; the value
$u_0 = 0$ extends it, and the indices $u_1, u_2, \dots$ agree with the source.

Formalized by `MetaMathlibExt.normalSeq`, a definition declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 31](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L31). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq).

## First term of a normal number sequence

For all integers $a_1$ and $a_2$, the normal
second-order number sequence $(u_n)_{n \ge 0}$ with coefficients $a_1, a_2$ has $u_1 = 1$.

Formalized by `MetaMathlibExt.normalSeq_one`, a theorem declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 39](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L39). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-one).

## Second term of a normal number sequence

For all integers $a_1$ and $a_2$, the normal
second-order number sequence $(u_n)_{n \ge 0}$ with coefficients $a_1, a_2$ has $u_2 = a_1$.

Formalized by `MetaMathlibExt.normalSeq_two`, a theorem declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 46](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L46). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-two).

## Recurrence for a normal number sequence

For all integers $a_1$ and $a_2$ and every
natural number $n$, the normal second-order number sequence $(u_n)_{n \ge 0}$ with coefficients
$a_1, a_2$ satisfies $u_{n+2} = a_1 u_{n+1} + a_2 u_n$.

Formalized by `MetaMathlibExt.normalSeq_recurrence`, a theorem declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-recurrence).

## Normal number sequence with second coefficient one

For an integer $a$, this sequence is
the normal second-order number sequence $(u_n)_{n \ge 0}$ with coefficients $a_1 = a$ and
$a_2 = 1$; that is, $u_0 = 0$, $u_1 = 1$ and $u_{n+2} = a u_{n+1} + u_n$ for every $n \ge 0$.

The source takes $a$ to be a nonzero integer; the definition allows every integer $a$.

Formalized by `MetaMathlibExt.normalSeqFib`, a definition declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 61](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L61). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-fib).

## Addition formula for the normal sequence with second coefficient one

Let $a$ be an
integer and let $(u_n)_{n \ge 0}$ be the normal second-order number sequence with coefficients
$a_1 = a$ and $a_2 = 1$. Then $u_{m+n+1} = u_{m+1} u_{n+1} + u_m u_n$ for all natural numbers
$m$ and $n$.

Formalized by `MetaMathlibExt.normalSeqFib_add`, a theorem declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-fib-add).

## Odd-index sum of two squares for the normal sequence with second coefficient one

Let $a$ be an integer and let $(u_n)_{n \ge 0}$ be the normal second-order number sequence with
coefficients $a_1 = a$ and $a_2 = 1$. Then $u_{2n-1} = u_n^2 + u_{n-1}^2$ for every natural
number $n \ge 2$.

The source assumes $a \ne 0$; the identity holds for every integer $a$.

Formalized by `MetaMathlibExt.normalSeq_odd_identity`, a theorem declared in [MathlibExt/NumberTheory/NormalNumberSequence.lean, line 129](https://github.com/Deicyde/atlas-lean/blob/035e1808ca0c8983682b74153a02628d616d77ce/MathlibExt/NumberTheory/NormalNumberSequence.lean#L129). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html#normal-seq-odd-identity).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Normal second-order sequences](https://deicyde.github.io/atlas-lean/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences/index.html)
- [Deicyde/atlas-lean at 035e1808](https://github.com/Deicyde/atlas-lean/tree/035e1808ca0c8983682b74153a02628d616d77ce/blueprint/roadmap/NumberTheory/linear-recurrences/second-order-sequences/normal-second-order-sequences)
