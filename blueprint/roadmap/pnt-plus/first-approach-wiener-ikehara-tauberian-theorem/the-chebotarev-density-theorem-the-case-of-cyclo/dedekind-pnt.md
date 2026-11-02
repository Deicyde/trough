---
declaration: lemma
origin: cited
---

# PNT for one character

For any nontrivial character $\chi$ of $G$,

$$
\sum_{N\mathfrak{p} \leq x} \chi(\mathfrak{p})\, \log N\mathfrak{p} \;=\; o(x)
\qquad(x\to\infty).
$$

(Equivalently, writing $\Lambda_\chi$ for the von Mangoldt-type coefficients of $-\frac{L'}{L}(\chi,s)$, one has $\sum_{n\leq x} \Lambda_\chi(n) = o(x)$.)

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Dedekind-nonvanishing](dedekind-nonvanishing.md)
- [Continuation of nontrivial Artin $L$-functions](artin-l-continuation.md)

## Proof

By Lemmas [Continuation of nontrivial Artin $L$-functions](artin-l-continuation.md) and [Dedekind-nonvanishing](dedekind-nonvanishing.md), $L(\chi,s)$ is holomorphic and nonvanishing on $\Re(s)\geq 1$, so $-\frac{L'}{L}(\chi,s)$ extends continuously to $\Re(s)\geq 1$. The claimed prime-sum estimate then follows by the same Wiener–Ikehara / Ingham contour argument used for Dirichlet $L$-functions in the prime-number theorem in arithmetic progressions (cf. the material already formalised for Dirichlet $L$-functions earlier in this file). Passing through $\Lambda_\chi$ (rather than the bare prime sum) makes the $j\geq 2$ prime-power contributions explicit and shows they are $O(x^{1/2}\log x)$, hence absorbable in the $o(x)$ error; cf. the remark after the statement.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
