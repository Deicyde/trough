---
declaration: lemma
origin: cited
lean: rudin_exp_ineq
statement: formalized
proof: formalized
---

# Rudin's exponential inequality

If the discrete Fourier transform of $f : G \longrightarrow \mathbb{C}$ has dissociated support, then

$$
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
\exp(\Re f) \le \exp\left(\frac{\lVert f\rVert_2^2} 2\right)
$$

It follows that

$$
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
_x e^{\left\lvert f(x)\right\rvert} \le 2e^{\| f\|_2^2/2}.
$$

## Depends on

- [Dissociation](dissociated.md)

## Proof depends on

- [Complex-valued Marcinkiewicz-Zygmund inequality](../almost-periodicity/mzi-complex.md)

## Proof

Using the convexity of $t\mapsto e^{tx}$ (for all $x\geq 0$ and $t\in[-1,1]$) we have

$$
e^{tx}\le \cosh(x)+t\sinh(x).
$$

It follows (taking $x=\lvert z\rvert$ and $t=\Re(z)/\lvert z\rvert$) that, for any $z\in \mathbb{C}$,

$$
e^{\Re z}\le \cosh \lvert z\rvert +\Re(z/\lvert z\rvert)\sinh \lvert z\rvert.
$$

In particular, if $c_\gamma\in \mathbb{C}$ with $\lvert c_\gamma\rvert=1$ is such that $\widehat{f}(\gamma)=c_\gamma\lvert \widehat{f}(\gamma)\rvert$, then

$$
\begin{aligned}
e^{\Re f(x)}
&= \exp\left( \Re \sum_{\gamma\in\Gamma}\widehat{f}(\gamma)\gamma(x)\right)\\
&=\prod_{\gamma\in \Gamma} \exp\left( \Re \widehat{f}(\gamma)\gamma(x)\right)\\
&\le \prod_{\gamma\in \Gamma}\left( \cosh \lvert \widehat{f}(\gamma)\rvert +\Re c_\gamma \gamma(x)\sinh \lvert \widehat{f}(\gamma)\rvert\right).
\end{aligned}
$$

Therefore

$$
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
_x e^{\Re f(x)}\le
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
_x \prod_{\gamma\in \Gamma} \left( \cosh\lvert \widehat{f}(\gamma)\rvert+\Re c_\gamma \gamma(x)\sinh\lvert \widehat{f}(\gamma)\rvert\right).
$$

Using $\Re z=(z+\overline{z})/2$ the product here can be expanded as the sum of

$$
\prod_{\gamma\in \Gamma_2}\frac{c_\gamma}{2}\prod_{\gamma\in \Gamma_3}\frac{\overline{c_\gamma}}{2}\left(\prod_{\gamma\in \Gamma_1}\cosh\lvert \widehat{f}(\gamma)\rvert\right)\left(\prod_{\gamma\in \Gamma_2\cup\Gamma_3}\sinh\lvert \widehat{f}(\gamma)\rvert\right)\left(\sum_{\gamma\in \Gamma_2}\gamma-\sum_{\lambda\in \Gamma_3}\lambda\right)(x)
$$

as $\Gamma_1\sqcup \Gamma_2\sqcup \Gamma_3=\Gamma$ ranges over all partitions of $\Gamma$ into three disjoint parts. Using the definition of dissociativity we see that

$$
\sum_{\gamma\in \Gamma_2}\gamma-\sum_{\lambda\in \Gamma_3}\lambda\neq 0
$$

unless $\Gamma_2=\Gamma_3=\emptyset$. In particular summing this term over all $x\in G$ gives $0$. Therefore the only term that survives averaging over $x$ is when $\Gamma_1=\Gamma$, and so

$$
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
_x e^{\Re f(x)}\le \prod_{\gamma\in \Gamma} \cosh \lvert \widehat{f}(\gamma)\rvert.
$$

The conclusion now follows using $\cosh(x) \le e^{x^2/2}$ and $\sum_{\gamma\in \Gamma}\lvert \widehat{f}(\gamma)\rvert^2=\| f\|_2^2$. The second conclusion follows by applying it to $f(x)$ and $-f(x)$ and using

$$
e^{\left\lvert y\right\rvert}\le e^y+e^{-y}.
$$

## Lean

Formalized as [`rudin_exp_ineq`](https://yaeldillies.github.io/apap/docs/find/#doc/rudin_exp_ineq).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 12](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L12)
