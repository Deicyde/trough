---
declaration: lemma
origin: cited
lean: rudin_ineq
statement: formalized
proof: formalized
---

# Rudin's inequality

If the discrete Fourier transform of $f : G \longrightarrow \mathbb{C}$ has dissociated support and $p \ge 2$ is an integer, then $\lVert f\rVert_p \le 4\sqrt{pe} \lVert f\rVert_2$.

## Depends on

- [Dissociation](dissociated.md)

## Proof depends on

- [Rudin's exponential inequality](rudin-exp.md)

## Proof

It is enough to show that $\lVert \Re f\rVert_p \le 2\sqrt{pe} \lVert f\rVert_2$ as then

$$
\lVert f\rVert_p \le \lVert \Re f\rVert_p + \lVert i \Im f\rVert_p = \lVert \Re f\rVert_p + \lVert \Re (-if)\rVert_p \le 4\sqrt{pe} \lVert f\rVert_2
$$

If $f = 0$, the result is obvious. So assume $f \ne 0$. $\lVert f\rVert_2 > 0$, so WLOG $\lVert f\rVert_2 = \sqrt p$.

Rudin's exponential inequality for $f$ becomes $\mathop{ \mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}} {\kern0pt\mathbb{E}} {\kern0pt\mathbb{E}} {\kern0pt\mathbb{E}} }\displaylimits \exp|\Re f| \le 2\exp(\frac p 2) = (2\sqrt e)^p$. Using $\frac{x^p}{p!} \le e^x$ for positive $x$, we get

$$
\frac{\lVert \Re f\rVert_p^p}{p^p} \le \frac{\lVert \Re f\rVert_p^p}{p!} =
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
\frac{|\Re f|^p}{p!} \le
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
\exp|\Re f|
$$

Rearranging, $\lVert \Re f\rVert_p \le 2 p\sqrt{e} = 2 \sqrt{pe} \lVert f\rVert_2$.

## Lean

Formalized as [`rudin_ineq`](https://yaeldillies.github.io/apap/docs/find/#doc/rudin_ineq).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 49](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L49)
