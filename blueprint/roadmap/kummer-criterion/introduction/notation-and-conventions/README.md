# Notation and conventions

Throughout the blueprint:

- $p$ is an odd prime, $\zeta_p$ a primitive $p$th root of unity, $K = \mathbb{Q}(\zeta_p)$, and $K^+$ the maximal real subfield of $K$ ([Definition cm-real-subfield](../../class-numbers-of-the-cyclotomic-cm-field/the-real-subfield-and-the-class-numbers/def-cm-real-subfield.md)). We write $\mathcal O_K$, $\mathcal O_{K^+}$ for the rings of integers and $\mathrm{Cl}(\mathcal O_K)$, $\mathrm{Cl}(\mathcal O_{K^+})$ for the ideal class groups.

- $h = h(K)$, $h^+ = h(K^+)$ and $h^- = h/h^+$ are the class number, the plus class number, and the relative class number ([Definition class-number-h](../../class-numbers-of-the-cyclotomic-cm-field/the-real-subfield-and-the-class-numbers/def-class-number-h.md), [Definition class-number-hplus](../../class-numbers-of-the-cyclotomic-cm-field/the-real-subfield-and-the-class-numbers/def-class-number-hplus.md), [Definition class-number-hminus](../../class-numbers-of-the-cyclotomic-cm-field/the-relative-class-number/def-class-number-hminus.md)).

- $B_n$ is the $n$th Bernoulli number, with the convention $B_1 = -\tfrac12$ (the convention of mathlib's `bernoulli`). Thus $B_n = 0$ for odd $n \ge 3$, and $B_n(X)$ denotes the $n$th Bernoulli polynomial. For a rational number $q$ written in lowest terms we write $\operatorname{num}(q) \in \mathbb{Z}$ and $\operatorname{den}(q) \in \mathbb{N}$ for its numerator and denominator.

- Dirichlet characters modulo $p$ ([Definition dirichlet-character](../../the-minus-class-number-criterion/characters-and-bernoulli-factors/def-dirichlet-character.md)) are written $\chi$; the trivial character is $1$, and $\chi$ is *even* or *odd* according to $\chi(-1) = 1$ or $\chi(-1) = -1$. The generalised Bernoulli numbers $B_{n,\chi}$ are defined in [Definition generalized-bernoulli](../../the-minus-class-number-criterion/characters-and-bernoulli-factors/def-generalized-bernoulli.md), the Teichmüller character $\omega$ in [Definition teichmuller](../../the-minus-class-number-criterion/characters-and-bernoulli-factors/def-teichmuller.md). Gauss sums are taken with respect to the standard additive character $a \mapsto e^{2\pi i a/p}$ and written $\tau(\chi)$.

- $\mathbb{Q}_p$ is the field of $p$-adic numbers and $\mathbb{Z}_p$ its ring of integers. For rational numbers $x, y$ (or, more generally, elements of $\mathbb{Q}_p$) we write

    $$
    x \equiv y \pmod{p}
    $$

    to mean $x - y \in p\mathbb{Z}_p$. In the formalisation this is rendered as the existence of $z \in \mathbb{Z}_p$ with $x - y = pz$ in $\mathbb{Q}_p$.

- For a finite abelian group quotient we write $[E : H]$ for the index of a subgroup $H \le E$.
