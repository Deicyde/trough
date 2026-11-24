---
declaration: lemma
origin: cited
lean: control_approximation_effect
statement: formalized
proof: formalized
---

# control approximation effect

There is a set $E \subset {\mathbb{R}}$ with Lebesgue measure $|E|\le \epsilon$ such that for all

$$
x\in [0,2\pi)\setminus E
$$

we have

$$
\sup_{N\ge 0} |S_Nf(x)-S_Nf_0(x)| \le \frac \epsilon 4\,.\qquad\text{(4)}
$$

## Depends on

- [partial Fourier sums of small](../part-02/partial-fourier-sums-of-small.md)

## Proof

*Proof of control approximation effect.* control approximation effect follows directly from [partial Fourier sums of small](../part-02/partial-fourier-sums-of-small.md) with $\delta:=\epsilon'$.

## Lean

Formalized as [`control_approximation_effect`](https://fpvandoorn.github.io/carleson/docs/find/#doc/control_approximation_effect).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8205](https://github.com/fpvandoorn/carleson/blob/f7487cc9da4d1e73f009dc0280cd5b958f3e2c78/blueprint/src/chapter/main.tex#L8205)
