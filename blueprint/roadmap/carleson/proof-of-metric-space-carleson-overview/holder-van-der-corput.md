---
declaration: proposition
origin: cited
lean: holder_van_der_corput
statement: formalized
proof: formalized
---

# Holder van der Corput

Let $z\in X$ and $R>0$ and set $B=B(z,R)$. Let $\varphi: X \to \mathbb{C}$ be supported on $B$ and satisfy $\|{\varphi}\|_{C^\tau(B(z, 2R))}\lt \infty$. Let ${\vartheta}, {\theta} \in {\Theta}$. Then

$$
|\int e({\vartheta}(x)-{{\theta}(x)})\varphi(x) dx|\le
2^{7a} \mu(B) \|{\varphi}\|_{C^\tau(B(z, 2R))}
(1 + d_{B}({\vartheta},{\theta}))^{-\frac{1}{2a^2+a^3}}
\,.\qquad\text{(39)}
$$

## Depends on

- [Lipschitz Holder approximation](../proof-of-the-holder-cancellative-condition/lipschitz-holder-approximation.md)

## Proof

*Proof of Holder van der Corput.* Let $z\in X$ and $R>0$ and set $B=B(z,R)$. Let $\varphi$ be given as in Holder van der Corput. Set

$$
t:=(1+d_B({\vartheta},{\theta}))^{-\frac{\tau}{2+a}}\qquad\text{(40)}
$$

and define $\tilde{\varphi}$ as in [Lipschitz Holder approximation](../proof-of-the-holder-cancellative-condition/lipschitz-holder-approximation.md). Let ${\vartheta}$ and ${\theta}$ be in ${\Theta}$. Then

$$
\left|\int e({\vartheta}(x)-{{\theta}(x)}) \varphi (x)\, \mathrm{d}\mu(x)\right|\qquad\text{(41)}
$$

$$
\le \left|\int e({\vartheta}(x)-{{\theta}(x)}) \tilde{\varphi} (x)\, \mathrm{d}\mu(x)\right|\qquad\text{(42)}
$$

$$
+ \left|\int e({\vartheta}(x)-{{\theta}(x)}) (\varphi (x)-\tilde{\varphi}(x))\, \mathrm{d}\mu(x)\right|\qquad\text{(43)}
$$

Using the cancellative condition [(12)](../introduction/README.md) of ${\Theta}$ on the ball $B(z,2R)$, the term (42) is bounded above by

$$
2^a \mu(B(z,2R)) \|\tilde{\varphi}\|_{\operatorname{\operatorname{Lip}}(B(z,2R))} (1 + d_{B(z,2R)}({\vartheta},{\theta}))^{-\tau} \, .\qquad\text{(44)}
$$

Using the doubling condition [(5)](../introduction/README.md), the inequality [(2)](../proof-of-the-holder-cancellative-condition/lipschitz-holder-approximation.md), and the estimate $d_B\le d_{B(z,2R)}$ from the definition, we estimate (44) from above by

$$
2^{6a}t^{-1-a} \mu(B) \|{\varphi}\|_{C^\tau(B)}
(1 + d_{B}({\vartheta},{\theta}))^{-\tau} \, .\qquad\text{(45)}
$$

The term (43) we estimate using [(1)](../proof-of-the-holder-cancellative-condition/lipschitz-holder-approximation.md) and that ${\vartheta}$ and ${\theta}$ are real and thus $e({\vartheta})$ and $e({\theta})$ bounded in absolute value by $1$. We obtain for (43) with [(5)](../introduction/README.md) the upper bound

$$
\mu(B(z,2R)) (t/2)^{\tau} \|\varphi\|_{C^\tau(B)}
\le 2^a \mu(B) t^{\tau} \|\varphi\|_{C^\tau(B)}
\,.\qquad\text{(46)}
$$

Using the definition (40) of $t$ and adding (45) and (46) estimates (41) from above by

$$
2^{6a} \mu(B) \|{\varphi}\|_{C^\tau(B)}
(1 + d_{B}({\vartheta},{\theta}))^{-\frac{\tau}{2+a}}
$$

$$
+
2^a \mu(B) \|{\varphi}\|_{C^\tau(B)}
(1 + d_{B}({\vartheta},{\theta}))^{-\frac{\tau^2}{2+a}}\, .
$$

$$
\le 2^{1+6a} \mu(B) \|{\varphi}\|_{C^\tau(B)}
(1 + d_{B}({\vartheta},{\theta}))^{-\frac{\tau^2}{2+a}} \, ,\qquad\text{(47)}
$$

where we used $\tau\le 1$. This completes the proof of Holder van der Corput.

## Lean

Formalized as [`holder_van_der_corput`](https://fpvandoorn.github.io/carleson/docs/find/#doc/holder_van_der_corput).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 734](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L734)
