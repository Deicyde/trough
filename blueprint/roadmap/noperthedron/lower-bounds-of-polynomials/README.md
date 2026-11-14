# Lower bounds of polynomials

Every leaf test reduces to a statement of the form “the polynomial $p$ is at least $m$ on $[-1,1]^5$”, where $p$ has integer coefficients and degree at most $2$ in each variable (degree at most $4$ in $t_0, t_1$ for one family of orbit tests). This chapter gives the two lower bounds that are used, and the integer encoding that lets the kernel compute them quickly.

- [pe](def-pe.md)

The leaf tests are written once, generically in the arithmetic: the same definition, instantiated with integers, is the checker; instantiated with polynomial expressions it produces $p$; instantiated with reals it gives the geometric quantity. Maps that commute with the ring operations commute with the generic definitions, which relates the three instances.

- [The coefficient bound](the-coefficient-bound/README.md)
- [The Bernstein bound](the-bernstein-bound/README.md)
- [Kronecker packing](kronecker-packing/README.md)
