---
declaration: lemma
origin: cited
lean: isBoundedAtImInfty_H_slash
statement: formalized
proof: formalized
---

# theta-bounded-im-infty

For all $\gamma \in \Gamma_1$, $H_{2}|_2 \gamma$, $H_{3}|_2 \gamma$, and $H_{4}|_2 \gamma$ are holomorphic at $i\infty$.

## Depends on

- [theta-slash-invariant](lemma-theta-slash-invariant.md)
- [Gamma-1-generators](../part-01/lemma-gamma-1-generators.md)

## Proof

We want to show that for $\gamma \in \Gamma_1$, $\|H_2|_2\gamma(z)\|$ is bounded as $z \in \mathbb{H} \to i\infty$. Firstly, by [Lemma theta-transform-S-T](lemma-theta-transform-s-t.md), [Lemma Gamma-2-generators](../part-01/lemma-gamma-2-generators.md) and induction on group elements, we notice that $\{\pm H_2, \pm H_3, \pm H_4\}$ is closed under action by $\Gamma_1$. Hence, it suffices to prove that $H_2$, $H_3$ and $H_4$ are bounded at $i\infty$. Consider $z \in \mathbb{H}$ with $\Im(z) \geq A$. We proceed by direct algebraic manipulation:

$$
\begin{aligned}
\|H_2(z)\|
&= \left\|\sum_{n \in \mathbb{Z}} \exp\left(\pi i \left(n + \frac{1}{2}\right)^2 z\right)\right\|^4
\leq \left(\sum_{n \in \mathbb{Z}} \left\|\exp\left(\pi i \left(n + \frac{1}{2}\right)^2 z\right)\right)\right\|^4 \\
&= \left(\sum_{n \in \mathbb{Z}} \left\|\exp\left(-\pi \left(n + \frac{1}{2}\right)^2 \Im(z)\right)\right)\right\|^4
\leq \left(\sum_{n \in \mathbb{Z}} \left\|\exp\left(-\pi \left(n + \frac{1}{2}\right)^2 A\right)\right)\right\|^4
\end{aligned}
$$

Where we prove the final term is convergent by noticing that it equals $\exp(-\pi A / 4)\theta(iA / 2, iA)$, which has been shown to converge in `Mathlib`. The proofs for $H_3$ and $H_4$ are similar (actually easier) and have been omitted.

**It seems the `MDifferentiable` requirement is missing.**

## Lean

Formalized as [`isBoundedAtImInfty_H_slash`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/isBoundedAtImInfty_H_slash).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 424](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L424)
