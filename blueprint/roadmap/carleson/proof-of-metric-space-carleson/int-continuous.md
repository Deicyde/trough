---
declaration: lemma
origin: cited
lean: continuous_carlesonOperatorIntegrand, rightContinuous_carlesonOperatorIntegrand, leftContinuous_carlesonOperatorIntegrand, measurable_carlesonOperatorIntegrand, enorm_carlesonOperatorIntegrand_le
statement: formalized
proof: formalized
---

# int continuous

Let $f$ be a measurable function with $|f| \le 1$. Then the function

$$
G: X \times \Theta \times (0,\infty) \times (0, \infty) \to \mathbb{C}
$$

$$
G(x, {\vartheta}, R_1, R_2) := \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) e({\vartheta}(y)) \, \mathrm{d}\mu(y)
$$

is continuous in ${\vartheta}$ for fixed $x, R_1, R_2$. It is right-continuous in $R_1$ for fixed $x, \vartheta, R_2$ and left-continuous in $R_2$ for fixed $x, \vartheta, R_1$. Finally, it is measurable in $x$ and bounded for fixed $\vartheta, R_1, R_2$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Measurability in $x$ follows from joint measurability of

$$
K(x,y) \mathbf{1}_{B(x,R_2) \setminus B(x,R_1)}(y)
$$

in $x$ and $y$ and (part of the proof of) Fubini's theorem.

(Partial) continuity in $R_1$ and $R_2$ is also a standard lemma in measure theory. It follows for example by splitting the integrand as $F_1 - F_{-1} + iF_i - iF_{-i}$ for positive, disjointly supported functions $F_{-}$ and applying the monotone convergence theorem to each summand.

For continuity in ${\vartheta}$ note that

$$
|G(x, {\vartheta}, R_1, R_2) - G(x, {\vartheta}', R_1, R_2)|
$$

$$
= \left| \int_{R_1 < \rho(x,y) < R_2} K(x,y) f(y) (e({\vartheta}(y)) - e({\vartheta}'(y))) \, \mathrm{d}\mu(y) \right|
$$

$$
\le \int_{R_1 < \rho(x,y) < R_2} |K(x,y)| |f(y)| |e({\vartheta}(y) - {\vartheta}'(y) - {\vartheta}(o) + {\vartheta}'(o)) - 1| \, \mathrm{d}\mu(y).
$$

By $1$-Lipschitz continuity of $e^{ix}$, the property [(7)](../introduction/README.md) of the metrics $d$, the kernel upper bound [(14)](../introduction/README.md) and $|f| \le 1$ this is

$$
\le \mu(B(x, R_2)) \sup_{R_1 < \rho(x,y) < R_2} \frac{2^{a^3}}{V(x,y)} d_{B(x,\rho(o,x)+R_2)}(\vartheta, \vartheta').
$$

If $R_1 < \rho(x,y) < R_2$ then there exists $n$ with $B(x,R_2) \subset B(x, 2^n \rho(x,y))$ and $2^n \le 2 R_2/R_1$. Hence, by the doubling property [(5)](../introduction/README.md),

$$
V(x,y) = \mu(B(x, \rho(x,y))) \ge 2^{-an} \mu(B(x, R_2)) \ge (2R_2 / R_1)^{-a} \mu(B(x, R_2)).
$$

Hence

$$
|G(x, {\vartheta}, R_1, R_2) - G(x, {\vartheta}', R_1, R_2)| \le 2^{a^3} \Big(\frac{2R_2}{R_1}\Big)^a d_{B(x, \rho(o,x)+R_2)}({\vartheta}, {\vartheta}').
$$

Since the topology on ${\Theta}$ is the one induced by any of the metrics $d_B$, continuity follows.

Finally, for boundedness as a function of $x$ note that we also have by a similar computation using $|e({\vartheta})|=1$

$$
|G(x, {\vartheta}, R_1, R_2)| \le 2^{a^3} \Big(\frac{2R_2}{R_1}\Big)^a.
$$

## Lean

Formalized as [`continuous_carlesonOperatorIntegrand`](https://fpvandoorn.github.io/carleson/docs/find/#doc/continuous_carlesonOperatorIntegrand), [`rightContinuous_carlesonOperatorIntegrand`](https://fpvandoorn.github.io/carleson/docs/find/#doc/rightContinuous_carlesonOperatorIntegrand), [`leftContinuous_carlesonOperatorIntegrand`](https://fpvandoorn.github.io/carleson/docs/find/#doc/leftContinuous_carlesonOperatorIntegrand), [`measurable_carlesonOperatorIntegrand`](https://fpvandoorn.github.io/carleson/docs/find/#doc/measurable_carlesonOperatorIntegrand), [`enorm_carlesonOperatorIntegrand_le`](https://fpvandoorn.github.io/carleson/docs/find/#doc/enorm_carlesonOperatorIntegrand_le).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 962](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L962)
