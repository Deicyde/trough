---
declaration: lemma
origin: cited
lean: EisensteinSeries.q_expansion_bernoulli
statement: formalized
proof: formalized
---

# Ek-Fourier

The Eisenstein series possesses the Fourier expansion

$$
E_k(z)=1+\frac{2}{\zeta(1-k)}\sum_{n=1}^\infty \sigma_{k-1}(n)\,e^{2\pi i z},\qquad\text{(3)}
$$

where $\sigma_{k-1}(n)\,=\,\sum_{d|n} d^{k-1}$. In particular, we have

$$
\begin{aligned}
E_4(z)\,=\,& 1+240\sum_{n=1}^\infty \sigma_3(n)\,e^{2\pi i n z}  \\
E_6(z)\,=\,& 1-504\sum_{n=1}^\infty \sigma_5(n)\,e^{2\pi i n z}.
\end{aligned}
$$

## Depends on

- [Ek](def-ek.md)

## Lean

Formalized as [`EisensteinSeries.q_expansion_bernoulli`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/EisensteinSeries.q_expansion_bernoulli).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 142](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L142)
