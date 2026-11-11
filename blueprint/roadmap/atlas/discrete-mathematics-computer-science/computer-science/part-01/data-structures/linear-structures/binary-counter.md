---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.BinaryCounter.increment, Cslib.Algorithms.Lean.BinaryCounter.increment_value, Cslib.Algorithms.Lean.BinaryCounter.increment_time, Cslib.Algorithms.Lean.BinaryCounter.increment_time_le, Cslib.Algorithms.Lean.BinaryCounter.run, Cslib.Algorithms.Lean.BinaryCounter.run_zero, Cslib.Algorithms.Lean.BinaryCounter.run_ret_succ, Cslib.Algorithms.Lean.BinaryCounter.run_time_succ
statement: formalized
proof: formalized
---

# Binary counter

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html).

## Binary counter increment

A $k$-bit counter is a vector $b = (b_0, \dots, b_{k-1})$ of bits
stored lowest bit first. Incrementing $b$ changes the initial run of $1$ bits $b_0, \dots, b_{t-1}$
to $0$ and then changes the first $0$ bit $b_t$, if there is one, to $1$; if every bit is $1$, all
bits become $0$ and no new bit is added. The result is again a $k$-bit counter, and the cost of
the increment is the number of bits changed, one unit per changed bit.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.increment`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 107](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L107). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#increment).

## Increment adds one with wraparound

Let $b = (b_0, \dots, b_{k-1})$ be a $k$-bit counter
stored lowest bit first, with bits $b_i \in \{0, 1\}$ and unsigned value
$v(b) = \sum_{i < k} b_i 2^i$. If $b'$ is the counter returned by incrementing $b$, then
$v(b') = (v(b) + 1) \bmod 2^k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.increment_value`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 118](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L118). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#increment-value).

## Exact cost of an increment

Let $b = (b_0, \dots, b_{k-1})$ be a $k$-bit counter stored
lowest bit first, and let $t$ be the length of its initial run of $1$ bits, that is, the largest
$t \le k$ with $b_0 = \dots = b_{t-1} = 1$. The cost of incrementing $b$ is $t + 1$ if $t < k$,
and $t$ if $t = k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.increment_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 125](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L125). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#increment-time).

## Increment costs at most the width

For every $k$-bit counter $b$ (a vector of $k$ bits,
lowest bit first), the cost of incrementing $b$ is at most $k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.increment_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 131](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L131). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#increment-time-le).

## Running the binary counter

For a width $k$, a $k$-bit counter $b$ and $n \in \mathbb{N}$,
the run of $n$ increments from $b$ is defined recursively. The run of $0$ increments returns $b$
at cost zero. The run of $n + 1$ increments performs the run of $n$ increments, then increments
the counter it returned and returns the result; its cost is the cost of the $n$-step run plus
the cost of that increment.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 136](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L136). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run).

## Running zero increments

For every width $k$ and every $k$-bit counter $b$, running zero
increments from $b$ returns $b$ unchanged at cost zero.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 143](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L143). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-zero).

## One more increment

For every bit vector $b$ and every natural number $n$, the bit vector
returned by running $n + 1$ increments from $b$ is the increment of the bit vector returned by
running $n$ increments from $b$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_ret_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 148](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L148). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-ret-succ).

## Cost recurrence for the binary counter run

For every width $k$, every $k$-bit counter
$b$ and every $n$, the cost of running $n + 1$ successive increments from $b$ equals the cost of
running $n$ increments from $b$ plus the cost of incrementing the counter that the $n$-step run
returns.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_time_succ`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 153](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L153). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-time-succ).

## Counter value after successive increments

For every width $k$, every $k$-bit counter $b$
and every $n$, let $v$ be the value of $b$ read as an unsigned binary number with the least
significant bit first. After $n$ successive increments starting from $b$, the counter read the
same way has value $(v + n) \bmod 2^k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_value`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 159](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L159). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-value).

## Flip counts of the individual bits

Let $k$, $i$ and $n$ be natural numbers
with $i < k$, and for each $t$ let $c_t$ be the bit vector returned by running $t$ increments
from the all-false bit vector of width $k$. Then the number of $t < n$ such that the bit at
position $i$ of $c_t$ (counting from the low-order bit, starting at $0$) differs from the bit at
position $i$ of $c_{t+1}$ is $\lfloor n / 2^i \rfloor$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_bit_flips`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 237](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L237). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-bit-flips).

## Incrementing the all-ones counter costs the full width

For every $k$, the cost of
incrementing the $k$-bit counter whose $k$ bits are all $1$ is exactly $k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.increment_time_replicate_true`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 281](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L281). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#increment-time-replicate-true).

## Exact cost of increments from zero

For all natural numbers $k$ and $n$, running
$n$ increments from the all-false bit vector of width $k$ costs exactly
$\sum_{i=0}^{k-1} \lfloor n / 2^i \rfloor$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_time_eq`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 333](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L333). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-time-eq).

## Aggregate cost bound for the binary counter

For every width $k$ and every $n > 0$,
performing $n$ successive increments on the $k$-bit counter that starts with all bits zero
costs strictly fewer than $2n$ bit changes in total.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_time_lt`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 370](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L370). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-time-lt).

## Lower bound on the cost of increments from zero

For all natural numbers $k$
and $n$ with $k > 0$, running $n$ increments from the all-false bit vector of width $k$
costs at least $n$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.run_time_ge`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 376](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L376). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#run-time-ge).

## Resetting a binary counter

Resetting a bit vector $b$ of width $k$ returns the
all-false bit vector of width $k$ and charges cost $1$ for each position of $b$ that holds
true, that is, for each bit it changes from true to false.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset`, a definition declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 433](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L433). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset).

## Reset returns the all-false counter

For every bit vector $b$ of width $k$, the bits
returned by resetting $b$ are, in order, $k$ copies of false.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_toList`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 444](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L444). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-to-list).

## Reset yields the value zero

For every bit vector $b$ of width $k$, the bits returned
by resetting $b$, read low-order bit first as an unsigned binary numeral, have value $0$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_value`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 449](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L449). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-value).

## Cost of resetting a binary counter

For every bit vector $b$ of width $k$, the cost of
resetting $b$ equals the number of positions of $b$ that hold true.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 455](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L455). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time).

## Reset cost is the Hamming distance

Let $b = (b_0, \dots, b_{k-1})$ be a $k$-bit counter
and $b' = (b'_0, \dots, b'_{k-1})$ the counter returned by resetting $b$. The cost of resetting
$b$ equals the number of indices $i < k$ with $b_i \ne b'_i$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time_changes`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 460](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L460). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time-changes).

## Reset costs at most the width

For every $k$-bit counter $b$ (a vector of $k$ bits), the
cost of resetting $b$ is at most $k$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 471](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L471). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time-le).

## Resetting a width-zero counter costs nothing

Resetting a bit vector of width $0$ has
cost $0$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time_zero_width`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 477](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L477). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time-zero-width).

## Resetting the all-false counter costs nothing

For every width $k$, resetting the
all-false bit vector of width $k$ has cost $0$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time_replicate_false`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 485](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L485). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time-replicate-false).

## Reset is idempotent

For every $k$-bit counter $b$, resetting the counter returned by
resetting $b$ returns the same counter as resetting $b$ once.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_ret_idempotent`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 491](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L491). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-ret-idempotent).

## A second reset costs nothing

For every $k$-bit counter $b$, resetting the counter
returned by resetting $b$ has cost $0$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_time_after_reset`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 497](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L497). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-time-after-reset).

## Potential identity for reset

For every $k$-bit counter $b$ (a vector of $k$ bits), the
cost of resetting $b$ plus the number of $1$ bits in the returned counter equals the number of
$1$ bits in $b$.

Formalized by `Cslib.Algorithms.Lean.BinaryCounter.reset_potential`, a theorem declared in [CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean, line 503](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DataStructures/BinaryCounter.lean#L503). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html#reset-potential).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Binary counter](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/data-structures/linear-structures/binary-counter/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/data-structures/linear-structures/binary-counter)
