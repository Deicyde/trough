---
declaration: lemma
origin: cited
lean: E_k_q_expansion
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

Formalized as [`E_k_q_expansion`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/E_k_q_expansion).

## Sources

- [Sphere packing in dimensions 8 and 24 (Math Inc) blueprint: subsections/modular-forms.tex, line 131](https://github.com/math-inc/Sphere-Packing-Lean/blob/1e98fb493088948ca7bbf47d7faed49cc5b39fc4/blueprint/src/subsections/modular-forms.tex#L131)
