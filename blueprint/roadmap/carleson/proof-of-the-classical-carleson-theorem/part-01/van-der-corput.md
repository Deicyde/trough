---
declaration: lemma
origin: cited
lean: van_der_Corput
statement: formalized
proof: formalized
---

# van der Corput

Let $\alpha\le\beta$ be real numbers. Let $g:{\mathbb{R}}\to {\mathbb{C}}$ be a measurable function and assume

$$
\|g\|_{Lip(\alpha,\beta)}:=\sup_{\alpha\le x\le \beta}|g(x)|+\frac{|\beta-\alpha|}{2}
\sup_{\alpha\le x\lt y\le \beta} \frac {|g(y)-g(x)|}{|y-x|}\lt \infty\, .
$$

Then for any $\alpha \le \beta$ and $n\in{\mathbb{Z}}$ we have

$$
\int _{\alpha}^{\beta} g(x) e^{inx}\, dx\le 2\pi |\beta-\alpha|\|g\|_{Lip(\alpha,\beta)}(1+|n||\beta-\alpha|)^{-1}\, .
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

*Proof of van der Corput.* Let $g$ be a Lipschitz continuous function as in the lemma. Assume first that $n=0$. Then

$$
\int_\alpha^\beta g(x) \, \mathrm{d}x \le |\beta - \alpha| \sup_{\alpha\le x\le \beta}|g(x)|
\le |\beta-\alpha|\|g\|_{Lip(\alpha,\beta)}(1+|n||\beta-\alpha|)^{-1}
$$

Assume now $n\ne 0$. Without loss of generality, we may assume $n>0$. We distinguish two cases. If $\beta-\alpha < \frac{\pi}{n}$, we have by the triangle inequality

$$
\left|\int_\alpha^\beta g(x) e^{inx} \, \mathrm{d}x\right|
\le |\beta -\alpha| \sup_{x \in [\alpha,\beta]} |g(x)|
\le 2\pi |\beta-\alpha|\|g\|_{Lip(\alpha,\beta)}(1+|n||\beta-\alpha|)^{-1} \,.
$$

We turn to the case $\frac{\pi}{n} \le \beta-\alpha$. We have

$$
e^{in(x + \pi/n)} = -e^{inx}\,.
$$

Using this, we write

$$
\int_\alpha^\beta g(x) e^{inx} \, \mathrm{d}x
= \frac{1}{2} \int_\alpha^\beta g(x) e^{inx} \, \mathrm{d}x - \frac{1}{2} \int_\alpha^\beta g(x) e^{in(x + \pi/n)}) \, \mathrm{d}x\,.
$$

We split the first integral at $\alpha + \frac{\pi}{n}$ and the second one at $\beta - \frac{\pi}{n}$, and make a change of variables in the second part of the first integral to obtain

$$
= \frac{1}{2} \int_{\alpha}^{\alpha + \frac{\pi}{n}} g(x) e^{inx} \, \mathrm{d}x - \frac{1}{2} \int_{\beta - \frac{\pi}{n}}^{\beta} g(x) e^{in(x + \pi/n)} \, \mathrm{d}x
$$

$$
+ \frac{1}{2} \int_{\alpha + \frac{\pi}{n}}^{\beta} (g(x) - g(x - \frac{\pi}{n})) e^{inx} \, \mathrm{d}x\,.
$$

The sum of the first two terms is by the triangle inequality bounded by

$$
\frac{\pi}{n} \sup_{x \in [\alpha,\beta]} |g(x)|\,.
$$

The third term is by the triangle inequality at most

$$
\frac{1}{2} \int_{\alpha + \frac{\pi}{n}}^\beta |g(x) - g(x - \frac{\pi}{n})| \, \mathrm{d}x
$$

$$
\le \frac{|\beta-\alpha|}{2} \frac{\pi}{n} \sup_{\alpha \le x < y \le \beta} \frac{|g(x) - g(y)|}{|x-y|}\,.
$$

Adding the two terms, we obtain

$$
\left|\int_\alpha^\beta g(x) e^{-inx} \, \mathrm{d}x\right| \le \frac{\pi}{n} \|g\|_{\mathrm{Lip}(\alpha,\beta)}\,.
$$

This completes the proof of the lemma, using that with $\frac{\pi}{n} \le \beta-\alpha$,

$$
\frac{\pi}{n} = \frac{2 \pi |\beta-\alpha|}{2n|\beta-\alpha|} \le 2 \pi |\beta-\alpha|(1 + n|\beta-\alpha|)^{-1}\,.
$$

## Lean

Formalized as [`van_der_Corput`](https://fpvandoorn.github.io/carleson/docs/find/#doc/van_der_Corput).

## Sources

- [Carleson's theorem blueprint: chapter/main.tex, line 8321](https://github.com/fpvandoorn/carleson/blob/d4446d3cab5d096d936a94e998d24c413b2b017d/blueprint/src/chapter/main.tex#L8321)
