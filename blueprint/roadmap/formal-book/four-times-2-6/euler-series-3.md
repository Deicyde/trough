---
declaration: theorem
origin: cited
lean: euler_series_3
statement: formalized
---

# Euler's series: Proof 3

$$
\sum_{n\ge 1}\frac{1}{n^2} = \frac{\pi^2}{6}
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The first step is to establish a remarkable relation between values of the (squared) cotangent function. Namely, for all $m \ge 1$ one has

$$
\cot^2 \left(\frac{\pi}{2m+1}\right) + \cot^2 \left(\frac{2\pi}{2m+1}\right) + \dots + \cot^2 \left(\frac{m\pi}{2m+1}\right) = \frac{2m(2m-1)}{6}.\qquad\text{(1)}
$$

To establish this, we start with the relation $e^{ix} = \cos x + i \sin x$. Taking the $n$-th power $e^{inx} = (e^{ix})^n$, we get

$$
\cos nx + i \sin nx = (\cos x + i \sin x)^n.
$$

The imaginary part of this is

$$
\sin nx = \binom{n}{1} \sin x \cos^{n-1} x - \binom{n}{3} \sin^3 x \cos^{n-3} x \pm \cdots\qquad\text{(2)}
$$

Now we let $n = 2m+1$, while for $x$ we will consider the $m$ different values $x = \frac{r\pi}{2m+1}$, for $r = 1, 2, \dots, m$. For each of these values we have $nx = r\pi$, and thus $\sin nx = 0$, while $0 < x < \frac{\pi}{2}$ implies that for $\sin x$ we get $m$ distinct positive values.

In particular, we can divide (2) by $\sin^n x$, which yields

$$
0 = \binom{n}{1} \cot^{n-1} x - \binom{n}{3} \cot^{n-3} x \pm \cdots,
$$

that is,

$$
0 = \binom{2m+1}{1} \cot^{2m} x - \binom{2m+1}{3} \cot^{2m-2} x \pm \cdots
$$

for each of the $m$ distinct values of $x$. Thus for the polynomial of degree $m$

$$
p(t) := \binom{2m+1}{1} t^m - \binom{2m+1}{3} t^{m-1} \pm \dots + (-1)^m \binom{2m+1}{2m+1}
$$

we know $m$ *distinct* roots

$$
a_r = \cot^2 \left(\frac{r\pi}{2m+1}\right) \quad \text{for } r = 1, 2, \dots, m.
$$

The roots are distinct because $\cot^2 x = \cot^2 y$ implies $\sin^2 x = \sin^2 y$ and thus $x = y$ for $x, y \in \{ \frac{r\pi}{2m+1} : 1 \le r \le m \}$.

Hence the polynomial coincides with

$$
p(t) = \binom{2m+1}{1} \left(t - \cot^2 \left(\frac{\pi}{2m+1}\right) \right) \dots \left(t - \cot^2 \left(\frac{m\pi}{2m+1}\right) \right).
$$

Comparison of the coefficients of $t^{m-1}$ in $p(t)$ now yields that the sum of the roots is

$$
a_1 + \dots + a_m = \frac{\binom{2m+1}{3}}{\binom{2m+1}{1}} = \frac{2m(2m-1)}{6},
$$

which proves (1).

We also need a second identity, of the same type,

$$
\csc^2 \left(\frac{\pi}{2m+1}\right) + \csc^2 \left(\frac{2\pi}{2m+1}\right) + \dots + \csc^2 \left(\frac{m\pi}{2m+1}\right) = \frac{2m(2m+2)}{6},\qquad\text{(3)}
$$

for the cosecant function $\csc x = \frac{1}{\sin x}$. But

$$
\csc^2 x = \frac{1}{\sin^2 x} = \frac{\cos^2 x + \sin^2 x}{\sin^2 x} = \cot^2 x + 1,
$$

so we can derive (3) from (1) by adding $m$ to both sides of the equation.

Now the stage is set, and everything falls into place. We use that in the range $0 < y < \frac{\pi}{2}$ we have

$$
0 < \sin y < y < \tan y,
$$

and thus

$$
0 < \cot y < \frac{1}{y} < \csc y,
$$

which implies

$$
\cot^2 y < \frac{1}{y^2} < \csc^2 y.
$$

Now we take this double inequality, apply it to each of the $m$ distinct values of $x$, and add the results. Using (1) for the left-hand side, and (3) for the right-hand side, we obtain

$$
\frac{2m(2m-1)}{6} < \left(\frac{2m+1}{\pi}\right)^2 + \left(\frac{2m+1}{2\pi}\right)^2 + \dots + \left(\frac{2m+1}{m\pi}\right)^2 < \frac{2m(2m+2)}{6},
$$

that is,

$$
\frac{\pi^2}{6} \frac{2m}{2m+1} \frac{2m-1}{2m+1} < \frac{1}{1^2} + \frac{1}{2^2} + \dots + \frac{1}{m^2} < \frac{\pi^2}{6} \frac{2m}{2m+1} \frac{2m+2}{2m+1}.
$$

Both the left-hand and the right-hand side converge to $\frac{\pi^2}{6}$ for $m \to \infty$: end of proof.

## Lean

Stated as [`euler_series_3`](https://mo271.github.io/FormalBook/docs/find/#doc/euler_series_3); the blueprint marks no proof of it as formalized.

## Sources

- [Formal Book blueprint: chapter/chapter09.tex, line 96](https://github.com/mo271/FormalBook/blob/7df264a4d5e57f9036acdf85f7a2702b3ad82a06/blueprint/src/chapter/chapter09.tex#L96)
