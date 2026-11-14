---
declaration: lemma
origin: cited
lean: logderiv_tendsto_of_div_exp_tendsto, D_F_div_F_tendsto, D_G_div_G_tendsto
statement: formalized
proof: formalized
---

# log-der-inf

Let $F$ be a quasimodular form where the vanishing order of $F$ at infinity is $n_0 > 0$, i.e. $F(z) = \sum_{n \geq n_0} a_n q^{n}$ with $a_{n_0} \ne 0$. Then

$$
\lim_{t \to \infty} \frac{F'(it)}{F(it)} = n_0.
$$

## Depends on

- [der-q-series](../modular-forms/part-02/lemma-der-q-series.md)

## Proof

By Lemma [der-q-series](../modular-forms/part-02/lemma-der-q-series.md),

$$
\lim_{t \to \infty} \frac{F'(it)}{F(it)} = \lim_{t \to \infty} \frac{\sum_{n \ge n_0} n a_n e^{-2 \pi n t}}{\sum_{n \ge n_0} a_n e^{-2 \pi n t}} = \lim_{t \to \infty} \frac{n_0 a_{n_0} e^{-2 \pi n_0 t} + O(e^{-2 \pi (n_0 + 1) t})}{a_{n_0} e^{-2 \pi n_0 t} + O(e^{-2 \pi (n_0 + 1) t})} = n_0.
$$

## Lean

Formalized as [`logderiv_tendsto_of_div_exp_tendsto`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/logderiv_tendsto_of_div_exp_tendsto), [`D_F_div_F_tendsto`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/D_F_div_F_tendsto), [`D_G_div_G_tendsto`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/D_G_div_G_tendsto).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modform-ineq.tex, line 181](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modform-ineq.tex#L181)
