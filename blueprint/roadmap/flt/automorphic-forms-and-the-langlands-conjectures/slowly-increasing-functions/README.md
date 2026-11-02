# Slowly-increasing functions

Automorphic representations satisfy a growth condition which we may as well factor out into a separate definition.

We define the following temporary “size” function $s:\operatorname{GL}_n(\mathbb{R})\to\mathbb{R}$ by $s(M)=trace(MM^T+M^{-1}M^{-T})$ where $M^{-T}$ denotes inverse-transpose. Note that $s(M)$ is always positive, and is large if $M$ has a very large or very small (in absolute value) eigenvalue.

- [AutomorphicForm.GLn.IsSlowlyIncreasing](automorphicform-gln-isslowlyincreasing.md)

Note: the book says $n$ is positive, but $\{M|s(M)\leq 1\}$ is compact so I don't think it makes any difference.
