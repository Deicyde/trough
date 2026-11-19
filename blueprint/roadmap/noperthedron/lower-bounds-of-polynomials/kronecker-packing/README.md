# Kronecker packing

The kernel evaluates arithmetic on natural numbers with GMP, but each step of a recursive function is comparatively expensive. The checker therefore represents a polynomial by a single large integer.

- [layout](def-layout.md)
- [kronecker](lem-kronecker.md)

Since evaluation is a ring homomorphism, the checker computes $p$ at the Kronecker point with a handful of big-integer additions and multiplications. Every coefficient is then available as a digit: the top bit of each offset digit is its sign, a bitwise *and* with a mask selects a set of slots, and the sum of a set of digits is a remainder modulo $2^W - 1$.

- [packed_bounds](lem-packed-bounds.md)
- [packN](lem-packn.md)

The checker uses slot width $W = 400$ and requires coefficient norms below $2^{390}$, which leaves room for the Bernstein transform.

- [Norm guard](lem-norm-guard.md)
