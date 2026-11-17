---
declaration: theorem
origin: cited
lean: borelCaratheodory'
statement: formalized
proof: formalized
---

# borelCaratheodory'

An application of `Complex.borelCaratheodory_zero`.

Let $0\lt M$ and $0\lt r\lt R$ with $f$ analytic on $\mathbb{D}_R$ with $f(0)=0$ s.t. for all $|z|\lt R$ we have $\mathfrak{R}(f(z))\leq M$. Then for all $|z|\leq r$ we have

$$
|f(z)|\leq\frac{2Mr}{R-r}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let

$$
f_M(z)=\frac{f(z)/z}{2M-f(z)}.
$$

Note that $2M-f(z)\neq 0$ because $\Re (2M-f(z))=2M-\Re f(z)\geq M>0$. Additionally, since $f(z)$ has a zero at $0$, we know that $f(z)/z$ is analytic on $|z|\leq R'$ for all $r\lt R'\lt R$. Likewise, $f_M(z)$ is analytic on $|z|\leq R'$. Now note that $|f(z)|\leq|2M-f(z)|$ since $\Re f(z)\leq M$. Thus we have that

$$
|f_M(z)|=\frac{|f(z)|/|z|}{|2M-f(z)|}
\leq\frac{1}{|z|}.
$$

Now by the maximum modulus principle, we know the maximum of $|f_M|$ must occur on the boundary where $|z|=R'$. Thus, $|f_M(z)|\leq 1/R'$ for all $|z|\leq R'$. So for $|z|=r$ we have

$$
|f_M(z)|=\frac{|f(z)|/r}{|2M-f(z)|}\leq\frac{1}{R'}
\qquad\implies\qquad R'\,|f(z)|\leq r\,|2M-f(z)|\leq 2Mr+r\,|f(z)|.
$$

Which by algebraic manipulation gives

$$
|f(z)|\leq\frac{2Mr}{R'-r}.
$$

Once more, by the maximum modulus principle, we know the maximum of $|f|$ must occur on the boundary $|z|=r$. Now by taking the limit $R'\to R$, the desired result immediately follows.

## Lean

Formalized as [`borelCaratheodory'`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/borelCaratheodory').

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/a4fb6989b07e9c76b511807ae93e33e25b820e9b/PrimeNumberTheoremAnd/StrongPNT.lean)
