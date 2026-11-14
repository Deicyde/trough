---
declaration: lemma
origin: cited
lean: H₂_T_action, H₃_T_action, H₄_T_action, H₂_S_action, H₃_S_action, H₄_S_action
statement: formalized
proof: formalized
---

# theta-transform-S-T

These elements act on the theta functions in the following way

$$
\begin{aligned}
H_2 | S &= -H_4\qquad\text{(10)}\\
H_3 | S &= -H_3\qquad\text{(11)}\\
H_4 | S &= -H_2\qquad\text{(12)}\end{aligned}
$$

and

$$
\begin{aligned}
H_2 | T &= -H_2\qquad\text{(13)}\\
H_3 | T &= H_4\qquad\text{(14)}\\
H_4 | T &= H_3\qquad\text{(15)}\end{aligned}
$$

## Depends on

- [th00-th01-th10](def-th00-th01-th10.md)
- [H2-H3-H4](def-h2-h3-h4.md)

## Proof

The last three identities easily follow from the definition. For example, (13) follows from

$$
\begin{aligned}
\Theta_{2}(z + 1) &= \sum_{n\in\mathbb{Z}}e^{\pi i (n+\frac12)^2 (z + 1)}
= \sum_{n \in \mathbb{Z}} e^{\pi i (n + \frac{1}{2})^{2}} e^{\pi i (n + \frac{1}{2})^{2} z} \\
&= \sum_{n \in \mathbb{Z}} e^{\pi i (n^2 + n + \frac{1}{4})} e^{\pi i (n + \frac{1}{2})^{2} z} = \sum_{n \in \mathbb{Z}} (-1)^{n^2 + n}e^{\pi i / 4} e^{\pi i (n + \frac{1}{2})^{2} z} \\
&= e^{\pi i / 4} \Theta_{2}(z)
\end{aligned}
$$

and taking 4th power. (10) and (12) are equivalent under $z \leftrightarrow -1/z$, so it is enough to show (10) and (11). These identities follow from the identities of the *two-variable* Jacobi theta function, which is defined as (be careful for the variables, where we use $\tau$ instead of $z$)

$$
\theta(z, \tau) = \sum_{n \in \mathbb{Z}} e^{2 \pi i n z + \pi i n^2 \tau}\qquad\text{(16)}
$$

and already formalized by David Loeffler. This function specialize to the theta functions as

$$
\begin{aligned}
\Theta_{2}(\tau) &= e^{\pi i \tau / 4} \theta(-\tau / 2, \tau)\qquad\text{(17)}\\
\Theta_{3}(\tau) &= \theta(0, \tau)\qquad\text{(18)}\\
\Theta_{4}(\tau) &= \theta(1/2, \tau)\qquad\text{(19)}\\
\end{aligned}
$$

Poisson summation formula gives

$$
\theta(z, \tau) = \frac{1}{\sqrt{-i \tau}} e^{-\frac{\pi i z^2}{\tau}} \theta\left(\frac{z}{\tau}, -\frac{1}{\tau}\right)\qquad\text{(20)}
$$

and applying the specializations above yield the identities. For example, (12) follows from

$$
\Theta_{4}(\tau) = \theta\left(\frac{1}{2}, \tau\right) = \frac{1}{\sqrt{-i\tau}} e^{- \frac{\pi i }{4 \tau}} \theta\left(\frac{1}{2 \tau}, -\frac{1}{\tau}\right) = \frac{1}{\sqrt{-i\tau}} \Theta_{2}\left(-\frac{1}{\tau}\right)
$$

and taking 4th power.

## Lean

Formalized as [`H₂_T_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂_T_action), [`H₃_T_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₃_T_action), [`H₄_T_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄_T_action), [`H₂_S_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂_S_action), [`H₃_S_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₃_S_action), [`H₄_S_action`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄_S_action).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 357](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L357)
