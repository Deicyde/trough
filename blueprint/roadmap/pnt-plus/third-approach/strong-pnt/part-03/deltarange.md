---
declaration: theorem
origin: cited
lean: DeltaRange
statement: formalized
proof: formalized
---

# DeltaRange

For all $t\in\mathbb{R}$ with $|t|\geq 2$ we have that

$$
\delta_t<1/9.
$$

## Depends on

- [DeltaT](deltat.md)

## Proof depends on

- [ZeroInequality](../part-02/zeroinequality.md)

## Proof

Note that $\delta_t=E/\log|t|$ where $E$ is the implied constant from Lemma [ZeroInequality](../part-02/zeroinequality.md). But we know that $E=(14D)^{-1}$ where $D\geq 5A+4B+C$ where $A$, $B$, and $C$ are the constants coming from Lemmas [ShiftZeroBound](../part-02/shiftzerobound.md), [ShiftOneBound](../part-02/shiftonebound.md), and [ShiftTwoBound](../part-02/shifttwobound.md) respectively. Thus,

$$
E\leq\frac{1}{14\,(5A+4B+C)}.
$$

But note that $A\geq 1$, $B>0$, and $C>0$ by Lemmas [ShiftZeroBound](../part-02/shiftzerobound.md), [ShiftOneBound](../part-02/shiftonebound.md), and [ShiftTwoBound](../part-02/shifttwobound.md) respectively. So, by a very lazy estimate we have $E\leq 1/14$. Thus,

$$
\delta_t=\frac{E}{\log|t|}\leq\frac{1}{14\,\log2}\lt \frac{1}{9}.
$$

## Lean

Formalized as [`DeltaRange`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/DeltaRange).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/StrongPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/StrongPNT.lean)
