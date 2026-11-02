---
declaration: theorem
origin: cited
lean: ZeroInequality
statement: formalized
proof: formalized
---

# ZeroInequality

There exists a constant $0 < E<1/14$ such that for all $\rho=\sigma+it$ with $\zeta(\rho)=0$ and $|t|\geq 2$, one has

$$
\sigma\leq 1-\frac{E}{\log|t|}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ShiftOneBound](shiftonebound.md)
- [ShiftTwoBound](shifttwobound.md)
- [vonMangoldtLSeriesSummable](vonmangoldtlseriessummable.md)
- [ShiftZeroBound](shiftzerobound.md)
- [LogDerivativeDirichlet](../../../second-approach/proof-of-medium-pnt/part-01/logderivativedirichlet.md)
- [ZeroWindowFinite](zerowindowfinite.md)
- [ZeroWindow](zerowindow.md)

## Proof

From Theorem [LogDerivativeDirichlet](../../../second-approach/proof-of-medium-pnt/part-01/logderivativedirichlet.md) when $\Re s>1$ we have

$$
-\frac{\zeta'}{\zeta}(s)=\sum_{1\leq n}\frac{\Lambda(n)}{n^s}.
$$

Thus,

$$
-3\,\frac{\zeta'}{\zeta}(1+\delta)
-4\,\frac{\zeta'}{\zeta}(1+\delta+it)
-\frac{\zeta'}{\zeta}(1+\delta+2it)
=\sum_{1\leq n}\Lambda(n)\,n^{-(1+\delta)}\left(3+4n^{-it}+n^{-2it}\right).
$$

Now applying Euler's identity

$$
\begin{aligned}
-3\,\Re \left(\frac{\zeta'}{\zeta}(1+\delta)\right)&
-4\,\Re \left(\frac{\zeta'}{\zeta}(1+\delta+it)\right)
-\Re \left(\frac{\zeta'}{\zeta}(1+\delta+2it)\right) \\
&\qquad\qquad\qquad=\sum_{1\leq n}\Lambda(n)\,n^{-(1+\delta)}
\left(3+4\cos(-t\log n)+\cos(-2t\log n)\right)
\end{aligned}
$$

Since

$$
3+4\cos(-t\log n)+\cos(-2t\log n)=2\,(1+\cos(-t\log n))^2\geq 0,
$$

we know that the series on the right hand side is bounded below by $0$, and by Lemmas [ShiftTwoBound](shifttwobound.md), [ShiftOneBound](shiftonebound.md), and [ShiftZeroBound](shiftzerobound.md) we have an upper bound on the left hand side. So,

$$
0\leq\frac{3}{\delta}+3A-\frac{4}{1+\delta-\sigma}+4B\log|t|+C\log|t|
$$

where $A$, $B$, and $C$ are the implied constants coming from Lemmas [ShiftZeroBound](shiftzerobound.md), [ShiftOneBound](shiftonebound.md), and [ShiftTwoBound](shifttwobound.md) respectively. By choosing $D\geq 5A+4B+C\geq 3A/\log 2+4B+C$ we have

$$
\frac{4}{1+\delta-\sigma}\leq\frac{3}{\delta}+D\log|t|
$$

by some manipulation. Now if we choose $\delta=(2D\log|t|)^{-1}$ then we have

$$
\frac{4}{1-\sigma+1/(2D\log|t|)}\leq7D\log|t|.
$$

So with some manipulation we have that

$$
\sigma\leq 1-\frac{1}{14D\log|t|}.
$$

This is exactly the desired result with the constant $E=(14D)^{-1}$. Since $D\geq 5A+4B+C\geq 1$ we have that $E\in(0,1/14)$.

## Lean

Formalized as [`ZeroInequality`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZeroInequality).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
