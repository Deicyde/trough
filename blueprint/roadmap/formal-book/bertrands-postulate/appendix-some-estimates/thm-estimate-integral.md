---
declaration: theorem
origin: cited
lean: chapter2.harmonic_number_bounds
statement: formalized
---

# estimate_integral

For all $n \in \mathbb{N}$

$$
\log n + \frac 1 n < H_n < \log n + 1.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

There is a very simple-but-effective method of estimating sums by integrals. For estimating the harmonic numbers

$$
H_n = \sum_{k=1}^{n} \frac{1}{k}
$$

we draw the figure and derive from it

$$
H_n - 1 = \sum_{k=2}^{n} \frac{1}{k} < \int_{1}^{n} \frac{1}{t} \, dt = \log n
$$

by comparing the area below the graph of $f(t) = \frac{1}{t} (1 \le t \le n)$ with the area of the dark shaded rectangles, and

$$
H_n - \frac{1}{n} = \sum_{k=1}^{n-1} \frac{1}{k} > \int_{1}^{n} \frac{1}{t} \, dt = \log n
$$

by comparing with the area of the large rectangles (including the lightly shaded parts). Taken together, this yields

$$
\log n + \frac{1}{n} < H_n < \log n + 1. \qedhere
$$

## Lean

Stated as [`chapter2.harmonic_number_bounds`](https://mo271.github.io/FormalBook/docs/find/#doc/chapter2.harmonic_number_bounds); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter02.tex, line 101](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter02.tex#L101)
