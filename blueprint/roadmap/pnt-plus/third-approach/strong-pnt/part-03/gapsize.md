---
declaration: theorem
origin: cited
lean: GapSize
statement: formalized
proof: formalized
---

# GapSize

Let $t\in\mathbb{R}$ with $|t|\geq 3$ and $z=\sigma+it$ where $1-\delta_t/3\leq\sigma\leq 3/2$. Additionally, let $\rho\in\mathcal{Z}_t$. Then we have that

$$
|z-\rho|\geq\delta_t/6.
$$

## Depends on

- [DeltaT](../part-02/deltat.md)
- [ZeroWindow](../part-02/zerowindow.md)

## Proof depends on

- [ZeroInequality](../part-02/zeroinequality.md)

## Proof

Let $\rho=\sigma'+it'$ and note that since $\rho\in\mathcal{Z}_t$, we have $t'\in(t-3/4,t+3/4)$. Thus, if $t>1$ we have

$$
\log|t'|\leq\log|t+3/4|\leq\log|2t|=\log 2+\log|t|\leq 2\log|t|.
$$

And otherwise if $t<-1$ we have

$$
\log|t'|\leq\log|t-3/4|\leq\log|2t|=\log 2+\log|t|\leq 2\log|t|.
$$

So by taking reciprocals and multiplying through by a constant we have that $\delta_t\leq2\delta_{t'}$. Now note that since $\rho\in\mathcal{Z}_t$ we know that $\sigma'\leq 1-\delta_{t'}$ by Theorem [ZeroInequality](../part-02/zeroinequality.md) (here we use the fact that $|t|\geq 3$ to give us that $|t'|\geq 2$). Thus,

$$
\delta_t/6\leq\delta_{t'}-\delta_t/3
=1-\delta_t/3-(1-\delta_{t'})\leq\sigma-\sigma'\leq|z-\rho|.
$$

## Lean

Formalized as [`GapSize`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/GapSize).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
