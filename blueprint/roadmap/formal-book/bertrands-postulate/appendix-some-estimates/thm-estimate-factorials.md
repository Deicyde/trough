---
declaration: theorem
origin: cited
lean: chapter2.bound_factorial
statement: formalized
---

# estimate_factorials

For all $n \in \mathbb{N}$

$$
e\left(\frac{n}{e}\right)^n < n! < en\left(\frac{n}{e}\right)^n.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The same method applied to

$$
\log(n!) = \log 2 + \log 3 + \dots + \log n = \sum_{k=2}^{n} \log k
$$

yields

$$
\log((n-1)!) < \int_{1}^{n} \log t \, dt < \log(n!),
$$

where the integral is easily computed:

$$
\int_{1}^{n} \log t \, dt = \left[t\log t - t\right]_{1}^{n} = n\log n - n + 1.
$$

Thus we get a lower estimate on $n!$

$$
n! > e^{n\log n - n + 1} = e\left(\frac{n}{e}\right)^n
$$

and at the same time an upper estimate

$$
n! = n(n-1)! < n e^{n\log n - n + 1} = en\left(\frac{n}{e}\right)^n. \qedhere
$$

## Lean

Stated as [`chapter2.bound_factorial`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter2.bound_factorial); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter02.tex, line 130](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter02.tex#L130)
