---
declaration: theorem
origin: cited
lean: JBlaschkeDerivBound
statement: formalized
proof: formalized
---

# JBlaschkeDerivBound

Let $B>1$ and $0 < r' < r < R<1$. If $f:\mathbb{C}\to\mathbb{C}$ is a function analytic on neighborhoods of points in $\overline{\mathbb{D}_1}$ with $f(0)=1$ and $|f(z)|\leq B$ for all $|z|\leq R$, then for all $|z|\leq r'$

$$
|L_f'(z)|\leq\frac{16\log(B)\,r^2}{(r-r')^3}.
$$

## Depends on

- [SetOfZeros](../part-01/setofzeros.md)
- [JBlaschke](jblaschke.md)

## Proof depends on

- [BlaschkeNonZero](../part-01/blaschkenonzero.md)
- [BlaschkeB](../part-01/blaschkeb.md)
- [norm-fOfZero-le-norm-BlaschkeOfZero](../part-01/norm-fofzero-le-norm-blaschkeofzero.md)
- [DiskBound](../part-01/diskbound.md)
- [BlaschkeAnalytic](../part-01/blaschkeanalytic.md)
- [LogOfAnalyticFunction'](../part-01/logofanalyticfunction-2.md)
- [BorelCaratheodoryDeriv](../part-01/borelcaratheodoryderiv.md)

## Proof

By Lemma [DiskBound](../part-01/diskbound.md) we immediately know that $|B_f(z)|\leq B$ for all $|z|\leq R$. Now since $L_f=J_{B_f}$ by Definition [JBlaschke](jblaschke.md), by Theorem [LogOfAnalyticFunction](../part-01/logofanalyticfunction.md) we know that

$$
L_f(0)=0\qquad\text{and}\qquad
\Re L_f(z)=\log|B_f(z)|-\log|B_f(0)|\leq\log|B_f(z)|\leq\log B
$$

for all $|z|\leq r$. Note that in the above

$$
0=\log|f(0)|\leq\log|B_f(0)|
$$

because of Lemma [norm-fOfZero-le-norm-BlaschkeOfZero](../part-01/norm-fofzero-le-norm-blaschkeofzero.md). So by Theorem [BorelCaratheodoryDeriv](../part-01/borelcaratheodoryderiv.md), it follows that

$$
|L_f'(z)|\leq\frac{16\log(B)\,r^2}{(r-r')^3}
$$

for all $|z|\leq r'$.

## Lean

Formalized as [`JBlaschkeDerivBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/JBlaschkeDerivBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
