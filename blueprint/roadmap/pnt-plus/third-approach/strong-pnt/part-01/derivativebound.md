---
declaration: lemma
origin: cited
lean: DerivativeBound
statement: formalized
proof: formalized
---

# DerivativeBound

Let $R,\,M>0$ and $0 < r < r' < R$. Let $f$ be analytic on $|z|\leq R$ such that $f(0)=0$ and suppose $\Re f(z)\leq M$ for all $|z|\leq R$. Then we have that

$$
|f'(z)|\leq\frac{2M(r')^2}{(R-r')(r'-r)^2}
$$

for all $|z|\leq r$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [cauchy-formula-deriv](cauchy-formula-deriv.md)
- [borelCaratheodory'](borelcaratheodory.md)

## Proof

By Lemma [cauchy-formula-deriv](cauchy-formula-deriv.md) we know that

$$
f'(z)=\frac{1}{2\pi i}\oint_{|w|=r'}\frac{f(w)}{(w-z)^2}\,dw
=\frac{1}{2\pi }\int_0^{2\pi}\frac{r'e^{it}\,f(r'e^{it})}{(r'e^{it}-z)^2}\,dt.
$$

Thus,

$$
|f'(z)|=\left|\frac{1}{2\pi}\int_0^{2\pi}
\frac{r'e^{it}\,f(r'e^{it})}{(r'e^{it}-z)^2}\,dt\right|
\leq\frac{1}{2\pi}\int_0^{2\pi}
\left|\frac{r'e^{it}\,f(r'e^{it})}{(r'e^{it}-z)^2}\right|\,dt.\qquad\text{(1)}
$$

Now applying Theorem [borelCaratheodory'](borelcaratheodory.md), and noting that $r'-r\leq|r'e^{it}-z|$, we have that

$$
\left|\frac{r'e^{it}\,f(r'e^{it})}{(r'e^{it}-z)^2}\right|
\leq\frac{2M(r')^2}{(R-r')(r'-r)^2}.
$$

Substituting this into Equation (1) and evaluating the integral completes the proof.

## Lean

Formalized as [`DerivativeBound`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/DerivativeBound).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
