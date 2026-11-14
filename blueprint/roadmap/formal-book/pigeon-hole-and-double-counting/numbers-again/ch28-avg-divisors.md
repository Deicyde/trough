---
declaration: theorem
origin: cited
lean: chapter28.sum_divisor_count
statement: formalized
proof: formalized
---

# Average number of divisors

For any positive integer $n$,

$$
\sum_{j=1}^{n} t(j) = \sum_{i=1}^{n} \left\lfloor \frac{n}{i} \right\rfloor.
$$

Consequently,

$$
\log n - 1 < \bar{t}(n) \leq H_n < \log n + 1,
$$

where $H_n = \sum_{i=1}^{n} \frac{1}{i}$ is the $n$-th harmonic number.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Double counting](../sums/double-counting.md)

## Proof

Consider the matrix $A$ (as above) for the integers $1$ up to $n$. Counting by columns we get $\sum_{j=1}^{n} t(j)$. How many $1$'s are in row $i$? Easy enough, the $1$'s correspond to the multiples of $i$: $1 \cdot i, 2 \cdot i, \dots$, and the last multiple not exceeding $n$ is $\lfloor n/i \rfloor \cdot i$. Hence we obtain

$$
\bar{t}(n) = \frac{1}{n} \sum_{j=1}^{n} t(j) = \frac{1}{n} \sum_{i=1}^{n} \left\lfloor \frac{n}{i} \right\rfloor
\leq \frac{1}{n} \sum_{i=1}^{n} \frac{n}{i} = \sum_{i=1}^{n} \frac{1}{i} = H_n,
$$

where the error in each summand, when passing from $\lfloor n/i \rfloor$ to $n/i$, is less than $1$. Together with the standard estimates $\log n < H_n < \log n + 1$ this gives $\log n - 1 < \bar{t}(n) \leq H_n < \log n + 1$.

Thus we have proved the remarkable result that, while $t(n)$ is totally erratic, the average $\bar{t}(n)$ behaves beautifully: It differs from $\log n$ by less than $1$.

## Lean

Formalized as [`chapter28.sum_divisor_count`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter28.sum_divisor_count).

## Sources

- [Formal Book blueprint: chapter/chapter28.tex, line 173](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter28.tex#L173)
