---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum, Cslib.Algorithms.Lean.TimeM.IsMaxSuffixSum, Cslib.Algorithms.Lean.TimeM.kadaneScan, Cslib.Algorithms.Lean.TimeM.maxSubarraySum, Cslib.Algorithms.Lean.TimeM.kadaneScan_time, Cslib.Algorithms.Lean.TimeM.maxSubarraySum_time, Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.ne_nil, Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.unique
statement: formalized
proof: formalized
---

# Maximum subarray problem

25 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html).

## Being the maximum subarray sum

For a list $L$ over an additive monoid $\alpha$ with a
linear order, an element $m \in \alpha$ is the maximum subarray sum of $L$ when some nonempty
contiguous sublist of $L$ has sum $m$ and every nonempty contiguous sublist of $L$ has sum at
most $m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 53](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L53). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#is-max-subarray-sum).

## Being the maximum suffix sum

For a list $L$ over an additive monoid $\alpha$ with a
linear order, an element $e \in \alpha$ is the maximum suffix sum of $L$ when some nonempty suffix
of $L$ has sum $e$ and every nonempty suffix of $L$ has sum at most $e$. A nonempty suffix is a
contiguous run ending at the last element of $L$.

Kadane's scan maintains its first accumulator as the maximum suffix sum of the elements read
so far.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSuffixSum`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 58](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L58). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#is-max-suffix-sum).

## Kadane's scan

Given accumulators $e, b$ in an additive monoid $\alpha$ with a linear
order, the scan over the empty list returns $b$ at cost $0$. Over a list with first element $x$
and remaining elements $L$, it sets $e' = \max(x, e + x)$ and returns the result of the scan of
$L$ from the accumulators $e'$ and $\max(b, e')$, at cost $3$ plus the cost of that scan.

Here $e$ is the best sum of a nonempty run ending at the last element read and $b$ is the best
sum of any nonempty run read so far.

Formalized by `Cslib.Algorithms.Lean.TimeM.kadaneScan`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 63](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L63). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#kadane-scan).

## Kadane's algorithm

Let $\alpha$ be a linearly ordered type with an additive monoid
structure. On the empty list, Kadane's algorithm returns no value. On a list
$x_1, x_2, \dots, x_n$ of elements of $\alpha$ with $n \ge 1$, it sets $e = b = x_1$; then for
$i = 2, \dots, n$ in turn it replaces $e$ by $\max(x_i, e + x_i)$ and then $b$ by $\max(b, e)$;
finally it returns $b$. Each of the steps $i = 2, \dots, n$ is charged three operations, and
nothing else is charged.

When $u \le v$ implies $u + w \le v + w$ for all $u, v, w \in \alpha$, after each step $e$ is the
largest sum of a nonempty contiguous run ending at the element just read, and $b$ is the largest
sum of a nonempty contiguous run among the elements read so far.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySum`, a definition declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum).

## Cost of Kadane's scan

Let $\alpha$ be an additive monoid with a linear order. For all
accumulators $e, b \in \alpha$ and every list $L$ over $\alpha$ of length $n$, Kadane's scan of
$L$ from the accumulators $e$ and $b$ costs exactly $3n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.kadaneScan_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#kadane-scan-time).

## Cost of Kadane's algorithm

Over an additive monoid $\alpha$ with a linear order, Kadane's
algorithm on a list of length $n \ge 1$ costs exactly $3(n - 1)$ operations, and on the empty
list it costs $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySum_time`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 89](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L89). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-time).

## A list with a maximum subarray sum is nonempty

Let $\alpha$ be an additive monoid with a
linear order. If an element $m \in \alpha$ is the maximum subarray sum of a list $L$ over
$\alpha$, then $L$ is nonempty.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.ne_nil`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 97](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L97). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#ne-nil).

## Uniqueness of the maximum subarray sum

Let $\alpha$ be a linearly ordered type with an
additive monoid structure, and let $L$ be a list over $\alpha$. If $m, m' \in \alpha$ are both
maximum subarray sums of $L$, meaning that each is the sum of some nonempty contiguous run of $L$
and bounds the sum of every nonempty contiguous run of $L$, then $m = m'$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.unique`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 104](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L104). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#unique).

## Maximum suffix sum after appending an element

Let $\alpha$ be an additive monoid with a
linear order such that $a \le b$ implies $a + c \le b + c$. If $e$ is the maximum sum of a
nonempty suffix of a list $p$ over $\alpha$, then for every $x \in \alpha$ the maximum sum of a
nonempty suffix of the list obtained by appending $x$ to $p$ is $\max(x, e + x)$.

Such a suffix is either $[x]$ alone or a nonempty suffix of $p$ followed by $x$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSuffixSum.concat`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 126](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L126). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#concat).

## Maximum subarray sum after appending an element

Let $\alpha$ be an additive monoid
with a linear order such that $a \le b$ implies $a + c \le b + c$. Let $p$ be a list over
$\alpha$, let $e$ be the maximum sum of a nonempty suffix of $p$, and let $b$ be the maximum sum
of a nonempty contiguous sublist of $p$. Then for every $x \in \alpha$, the maximum sum of a
nonempty contiguous sublist of the list obtained by appending $x$ to $p$ is
$\max(b, \max(x, e + x))$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.concat`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 144](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L144). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#concat-2).

## Invariant of Kadane's scan

Let $\alpha$ be an additive monoid with a linear order such
that $a \le b$ implies $a + c \le b + c$. Let $p$ be a list over $\alpha$, let $e$ be the maximum
sum of a nonempty suffix of $p$, and let $b$ be the maximum sum of a nonempty contiguous sublist
of $p$. Then for every list $r$ over $\alpha$, the value that Kadane's scan from the accumulators
$e$ and $b$ returns on $r$ is the maximum sum of a nonempty contiguous sublist of the list $p$
followed by $r$.

Formalized by `Cslib.Algorithms.Lean.TimeM.kadaneScan_ret`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 163](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L163). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#kadane-scan-ret).

## Correctness of Kadane's algorithm

Let $\alpha$ be an additive monoid with a linear order
such that $a \le b$ implies $a + c \le b + c$. For every list $L$ over $\alpha$ and every
$m \in \alpha$, Kadane's algorithm returns $m$ on $L$ if and only if $m$ is the maximum sum of a
nonempty contiguous sublist of $L$: some nonempty contiguous sublist of $L$ has sum $m$, and
every nonempty contiguous sublist of $L$ has sum at most $m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySum_ret_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 174](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L174). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-ret-eq-some-iff).

## Kadane's algorithm bounds every nonempty run

Let $\alpha$ be a linearly ordered type
with an additive monoid structure in which $b \le c$ implies $b + a \le c + a$. If Kadane's
algorithm returns the value $m$ on a list $L$ over $\alpha$, then every nonempty contiguous run
of $L$ has sum at most $m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.sum_le_of_maxSubarraySum`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 192](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L192). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#sum-le-of-max-subarray-sum).

## Kadane's algorithm returns an attained sum

Let $\alpha$ be an additive monoid with a
linear order such that $a \le b$ implies $a + c \le b + c$. If Kadane's algorithm returns a value
$m$ on a list $L$ over $\alpha$, then some nonempty contiguous sublist of $L$ has sum $m$.

Formalized by `Cslib.Algorithms.Lean.TimeM.exists_sum_eq_of_maxSubarraySum`, a theorem declared in [CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean, line 198](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DynamicProgramming/MaximumSubarray.lean#L198). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#exists-sum-eq-of-max-subarray-sum).

## Maximum prefix sum

Let $\alpha$ be an additive monoid with a linear order. For a list $xs$
over $\alpha$ and $p \in \alpha$, $p$ is the maximum prefix sum of $xs$ when some nonempty prefix
of $xs$ has sum $p$ and every nonempty prefix of $xs$ has sum at most $p$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxPrefixSum`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 52](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L52). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#is-max-prefix-sum).

## Right-to-left suffix scan

Let $\alpha$ be an additive monoid carrying a linear order.
For a nonempty list $x_1, \dots, x_n$ in $\alpha$, this timed computation returns the pair
$(x_1 + \dots + x_n, s)$, where $s$ is the maximum of the suffix sums $x_i + \dots + x_n$ over
$1 \le i \le n$. It scans from the right: the step for $x_i$ forms $x_i + (x_{i+1} + \dots + x_n)$
and takes its maximum with the best suffix sum found so far, at a cost of $2$ time units per
element, $2n$ in total. On the empty list it returns $(0, 0)$ at no cost.

Formalized by `Cslib.Algorithms.Lean.TimeM.suffixScan`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 56](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L56). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#suffix-scan).

## Prefix scan

For lists over an additive monoid with a linear order, the prefix scan returns
$0$ on the empty list at no cost, and $x$ on a one-element list $[x]$ at cost $2$. On a list with
first element $x$ and nonempty tail $t$ it returns $\max(x, x + b)$, where $b$ is the prefix scan
of $t$, at the cost of the scan of $t$ plus $2$.

When $u \le v$ implies $a + u \le a + v$, the value on a nonempty list is the maximum sum of a
nonempty prefix of the list.

Formalized by `Cslib.Algorithms.Lean.TimeM.prefixScan`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 68](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L68). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#prefix-scan).

## Divide-and-conquer core of maximum subarray

For lists over an additive monoid with a
linear order: on the empty list it returns $0$ and on a one-element list $[x]$ it returns $x$,
both at no cost. On a list of length $n \ge 2$, let $m = \lfloor n/2 \rfloor$, let $l$ and $r$ be
its results on the first $m$ elements and on the remaining $n - m$ elements, let $s$ be the best
nonempty suffix sum of the first $m$ elements as computed by the suffix scan, and let $p$ be the
prefix scan of the remaining elements. It returns $\max(\max(l, r), s + p)$, at the cost of
these four computations plus $3$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarrayDC`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 79](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L79). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-dc).

## Divide-and-conquer maximum subarray

The CLRS algorithm FIND-MAXIMUM-SUBARRAY over an
additive monoid with a linear order, returning only the sum. On the empty list it returns no
value, at no cost. On a nonempty list it returns the value of the divide-and-conquer core on that
list, at the same cost; the core splits a list of length $n \ge 2$ after its first
$\lfloor n/2 \rfloor$ elements and returns the largest of its results on the two parts and the
best nonempty suffix sum of the first part plus the prefix scan of the second part.

When $b \le c$ implies $a + b \le a + c$ and $b + a \le c + a$, the value returned on a nonempty
list is the maximum sum of a nonempty contiguous run of the list.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySumDC`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 98](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L98). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-dc).

## Cost recurrence of divide-and-conquer maximum subarray

The function
$T : \mathbb{N} \to \mathbb{N}$ given by $T(n) = 0$ for $n \le 1$ and
$T(n) = T(\lfloor n/2 \rfloor) + T(n - \lfloor n/2 \rfloor) + 2n + 3$ for $n \ge 2$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarrayDCCost`, a definition declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 106](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L106). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-dccost).

## Running time of divide-and-conquer maximum subarray

Let $\alpha$ be an additive monoid
with a linear order. On a nonempty list over $\alpha$ of length $n$, the cost $T$ of the
divide-and-conquer maximum subarray algorithm satisfies
$T + 3 \le 2n\lceil \log_2 n \rceil + 3n$, that is, $T \le 2n\lceil \log_2 n \rceil + 3(n - 1)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySumDC_time_le`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 185](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L185). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-dc-time-le).

## Correctness of the suffix scan

Let $\alpha$ be an additive monoid with a linear order. For
every nonempty list $xs$ over $\alpha$, the suffix scan of $xs$ returns a pair whose first
component is the sum of $xs$ and whose second component is the maximum sum of a nonempty suffix
of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.suffixScan_spec`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 199](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L199). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#suffix-scan-spec).

## Maximum subarray sum of a concatenation

Let $\alpha$ be an additive monoid with a linear
order such that $b \le c$ implies $a + b \le a + c$ and $b + a \le c + a$, and let $L$ and $R$ be
lists over $\alpha$. Suppose that $l$ is the maximum sum of a nonempty contiguous run of $L$, $r$
is the maximum sum of a nonempty contiguous run of $R$, $s$ is the maximum sum of a nonempty
suffix of $L$, and $p$ is the maximum sum of a nonempty prefix of $R$. Then
$\max(\max(l, r), s + p)$ is the maximum sum of a nonempty contiguous run of the concatenation of
$L$ followed by $R$.

Formalized by `Cslib.Algorithms.Lean.TimeM.IsMaxSubarraySum.append`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 250](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L250). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#append).

## Correctness of divide-and-conquer maximum subarray

Let $\alpha$ be an additive monoid
with a linear order such that $b \le c$ implies $a + b \le a + c$ and $b + a \le c + a$. For every
list $xs$ over $\alpha$ and every $m \in \alpha$, the divide-and-conquer algorithm returns $m$ on
$xs$ if and only if $m$ is the maximum sum of a nonempty contiguous run of $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySumDC_ret_eq_some_iff`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 295](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L295). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-dc-ret-eq-some-iff).

## Divide and conquer agrees with Kadane's algorithm

Let $\alpha$ be an additive monoid with
a linear order such that $b \le c$ implies $a + b \le a + c$ and $b + a \le c + a$. For every list
$xs$ over $\alpha$, the divide-and-conquer maximum subarray algorithm and Kadane's algorithm
return the same result on $xs$.

Formalized by `Cslib.Algorithms.Lean.TimeM.maxSubarraySumDC_eq_maxSubarraySum`, a theorem declared in [CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean, line 307](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/DivideAndConquer/MaximumSubarray.lean#L307). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html#max-subarray-sum-dc-eq-max-subarray-sum).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Maximum subarray problem](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/dynamic-programming/maximum-subarray-problem)
