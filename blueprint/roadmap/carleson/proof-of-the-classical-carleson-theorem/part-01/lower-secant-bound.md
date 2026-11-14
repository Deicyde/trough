---
declaration: lemma
origin: cited
lean: lower_secant_bound'
statement: formalized
proof: formalized
---

# lower secant bound

Let $\eta>0$ and $-2\pi +\eta \le x\le 2\pi-\eta$ with $|x|\ge \eta$. Then

$$
|1-e^{ix}|\ge \frac{2}{\pi} \eta
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

We have

$$
|1 - e^{ix}| = \sqrt{(1 - \cos(x))^2 + \sin^2(x)} \ge |\sin(x)|\,.
$$

If $0 \le x \le \frac{\pi}{2}$, then we have from concavity of $\sin$ on $[0, \pi]$ and $\sin(0) = 0$ and $\sin(\frac{\pi}{2}) = 1$

$$
|\sin(x)| \ge \frac{2}{\pi} x \ge \frac{2}{\pi} \eta\,.
$$

When $x\in \frac{m\pi}{2} + [0, \frac{\pi}{2}]$ for $m \in \{-4, -3, -2, -1, 1, 2, 3\}$ one can argue similarly.

## Lean

Formalized as [`lower_secant_bound'`](https://fpvandoorn.github.io/carleson/docs/find/#doc/lower_secant_bound').

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8393](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8393)
