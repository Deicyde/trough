---
declaration: section
origin: cited
lean: Cslib.Algorithms.Lean.TimeM.bucketSort, Cslib.Algorithms.Lean.TimeM.bucketSort_time, Cslib.Algorithms.Lean.TimeM.bucketSort_time_lower, Cslib.Algorithms.Lean.TimeM.bucketSort_time_le_sum_sq, Cslib.Algorithms.Lean.TimeM.bucketSort_empty, Cslib.Algorithms.Lean.TimeM.bucketSort_perm, Cslib.Algorithms.Lean.TimeM.bucketSort_sorted, Cslib.Algorithms.Lean.TimeM.bucketSort_occupancy_mean
statement: formalized
proof: formalized
---

# Bucket sort

17 results, all proved, quoted from [Deicyde/atlas-lean](https://github.com/Deicyde/atlas-lean) at commit [a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d); [its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html).

## Bucket sort

Let $R$ be a linearly ordered field with a floor function and let
$x_1, \dots, x_n$ be an array of elements of $R$ that all lie in $[0, 1)$. If $n = 0$, bucket
sort returns the empty array at zero cost. Otherwise it creates $n$ empty buckets indexed by
$0, \dots, n - 1$, visits the entries in order and prepends each entry $x$ to bucket
$\lfloor n x \rfloor$, sorts each bucket with insertion sort, and concatenates the sorted
buckets in increasing order of index. The cost is $n$ for creating the buckets, plus one per
entry placed, plus one per bucket sorted together with the comparisons insertion sort makes on
it, plus one per bucket and one per entry during concatenation.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort`, a definition declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 72](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L72). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort).

## Exact cost of bucket sort

Let $R$ be a linearly ordered field with a floor function
and let $x_1, \dots, x_n$ be an array of elements of $R$ that all lie in $[0, 1)$. For
$0 \le i < n$ let $B_i$ be the list of the entries $x_j$ with $\lfloor n x_j \rfloor = i$,
in decreasing order of $j$, and let $T(B_i)$ be the number of comparisons insertion sort makes
on $B_i$. Then the cost of bucket sort on this array equals $5n + \sum_{i=0}^{n-1} T(B_i)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 441](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L441). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time).

## Linear lower bound on the cost of bucket sort

Let $R$ be a linearly ordered field with
a floor function. For every array of $n$ elements of $R$ that all lie in $[0, 1)$, the cost
of bucket sort on this array is at least $5n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_lower`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 465](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L465). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-lower).

## Bound on the cost of bucket sort via squared bucket sizes

Let $R$ be a linearly
ordered field with a floor function and let $x_1, \dots, x_n$ be an array of elements of $R$
that all lie in $[0, 1)$. For $0 \le i < n$ let $c_i$ be the number of indices $j$ with
$\lfloor n x_j \rfloor = i$. Then the cost of bucket sort on this array is at most
$5n + \sum_{i=0}^{n-1} c_i^2$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_le_sum_sq`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 473](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L473). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-le-sum-sq).

## Bucket sort on the empty array

For every linearly ordered field $R$ with a floor
function, bucket sort applied to the empty array of elements of $R$ returns the empty array
at zero cost.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_empty`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 492](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L492). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-empty).

## Bucket sort permutes its input

Let $R$ be a linearly ordered field with a floor
function. For every array of elements of $R$ that all lie in $[0, 1)$, the array returned by
bucket sort is a permutation of the input: every element occurs in the output exactly as many
times as in the input.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_perm`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 499](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L499). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-perm).

## Bucket sort sorts

Let $R$ be a linearly ordered field with a floor function. For every
array of elements of $R$ that all lie in $[0, 1)$, the array returned by bucket sort is
nondecreasing: each entry is at most every entry after it.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_sorted`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean, line 505](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/Basic.lean#L505). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-sorted).

## Expected occupancy of a bucket in bucket sort

Let $n \ge 1$ and let
$\omega_0, \dots, \omega_{n-1}$ be independent random variables, each uniformly distributed on
$[0, 1)$. For $i < n$, let $N_i$ be the number of indices $j < n$ with
$\lfloor n \omega_j \rfloor = i$. Then $\mathbb{E}[N_i] = 1$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_occupancy_mean`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 664](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L664). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-occupancy-mean).

## Variance of a bucket's occupancy in bucket sort

Let $n \ge 1$ and let
$\omega_0, \dots, \omega_{n-1}$ be independent random variables, each uniformly distributed on
$[0, 1)$. For $i < n$, let $N_i$ be the number of indices $j < n$ with
$\lfloor n \omega_j \rfloor = i$. Then $\operatorname{Var}(N_i) = 1 - 1/n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_occupancy_variance`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 671](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L671). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-occupancy-variance).

## Second moment of a bucket's occupancy in bucket sort

Let $n \ge 1$ and let
$\omega_0, \dots, \omega_{n-1}$ be independent random variables, each uniformly distributed on
$[0, 1)$. For $i < n$, let $N_i$ be the number of indices $j < n$ with
$\lfloor n \omega_j \rfloor = i$. Then $\mathbb{E}[N_i^2] = 2 - 1/n$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_occupancy_secondMoment`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 678](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L678). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-occupancy-second-moment).

## The running time of bucket sort is measurable

For every $n$, the function
$T : \mathbb{R}^n \to \mathbb{R}$ that maps $\omega = (\omega_0, \dots, \omega_{n-1})$ to the
number of time steps that bucket sort charges on the array $(\omega_0, \dots, \omega_{n-1})$ if
every $\omega_j$ lies in $[0, 1)$, and to $0$ otherwise, is measurable.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_measurable`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 686](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L686). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-measurable).

## The running time of bucket sort is integrable

For every $n$, let
$T : \mathbb{R}^n \to \mathbb{R}$ map $\omega = (\omega_0, \dots, \omega_{n-1})$ to the number of
time steps that bucket sort charges on the array $(\omega_0, \dots, \omega_{n-1})$ if every
$\omega_j$ lies in $[0, 1)$, and to $0$ otherwise. Then $T$ is integrable with respect to the
product of $n$ copies of the uniform distribution on $[0, 1)$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_integrable`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 694](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L694). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-integrable).

## Lower bound on the expected time of bucket sort

Let $n \ge 1$ and let
$\omega = (\omega_0, \dots, \omega_{n-1})$ have independent coordinates, each uniformly
distributed on $[0, 1)$. Let $T(\omega)$ be the number of time steps that bucket sort charges
on the array $(\omega_0, \dots, \omega_{n-1})$ if every $\omega_j$ lies in $[0, 1)$, and
$T(\omega) = 0$ otherwise. Then $5n \le \mathbb{E}[T]$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_expected_lower`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 703](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L703). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-expected-lower).

## Upper bound on the expected time of bucket sort

Let $n \ge 1$ and let
$\omega = (\omega_0, \dots, \omega_{n-1})$ have independent coordinates, each uniformly
distributed on $[0, 1)$. Let $T(\omega)$ be the number of time steps that bucket sort charges
on the array $(\omega_0, \dots, \omega_{n-1})$ if every $\omega_j$ lies in $[0, 1)$, and
$T(\omega) = 0$ otherwise. Then $\mathbb{E}[T] \le 5n + (n - 1)/2$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_expected_upper`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 712](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L712). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-expected-upper).

## Bucket sort on the empty input has expected time zero

Let $T$ be the number of time
steps that bucket sort charges on the empty array, the only input of length $n = 0$. Its
expectation under the product of zero copies of the uniform distribution on $[0, 1)$ is $0$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_expected_zero`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 721](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L721). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-expected-zero).

## Expected time of bucket sort on one input

Let $\omega_0$ be uniformly distributed on
$[0, 1)$, and let $T(\omega_0)$ be the number of time steps that bucket sort charges on the
one-element array $(\omega_0)$ if $\omega_0 \in [0, 1)$, and $T(\omega_0) = 0$ otherwise.
Then $\mathbb{E}[T] = 5$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_expected_one`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 730](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L730). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-expected-one).

## Bucket sort runs in expected linear time

For each $n$, let
$\omega = (\omega_0, \dots, \omega_{n-1})$ have independent coordinates, each uniformly
distributed on $[0, 1)$. Let $T_n(\omega)$ be the number of time steps that bucket sort charges
on the array $(\omega_0, \dots, \omega_{n-1})$ if every $\omega_j$ lies in $[0, 1)$, and
$T_n(\omega) = 0$ otherwise. Then $\mathbb{E}[T_n] = \Theta(n)$ as $n \to \infty$.

Formalized by `Cslib.Algorithms.Lean.TimeM.bucketSort_time_expected_isTheta`, a theorem declared in [CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean, line 741](https://github.com/Deicyde/atlas-lean/blob/a3690dd2ad41e1ad4d871b062779ed7b0452800d/CSLibExt/Algorithms/Lean/Sort/Bucket/ExpectedCost.lean#L741). [Its page on the ATLAS site](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html#bucket-sort-time-expected-is-theta).

## Depends on

No dependencies are recorded: this chapter reads the vault and the repository's source text without running Lean, and the vault records no edges between its results.

## Sources

- [ATLAS: Bucket sort](https://deicyde.github.io/atlas-lean/roadmap/ComputerScience/sorting-and-searching/bucket-sort/index.html)
- [Deicyde/atlas-lean at a3690dd2](https://github.com/Deicyde/atlas-lean/tree/a3690dd2ad41e1ad4d871b062779ed7b0452800d/blueprint/roadmap/ComputerScience/sorting-and-searching/bucket-sort)
