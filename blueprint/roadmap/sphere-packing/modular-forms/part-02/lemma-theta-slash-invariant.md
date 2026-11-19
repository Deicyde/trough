---
declaration: lemma
origin: cited
lean: H₂_SIF, H₃_SIF, H₄_SIF
statement: formalized
proof: formalized
---

# theta-slash-invariant

$H_{2}$, $H_{3}$, and $H_{4}$ are slash invariant under $\Gamma(2)$, i.e. for all $\gamma \in \Gamma(2)$ and $i \in \{2, 3, 4\}$, we have $H_i|\gamma = H_i|\gamma^{-1} = H_i$.

## Depends on

- [slash-operator-chain-rule](../part-01/lemma-slash-operator-chain-rule.md)
- [slash-negI-even-weight](../part-01/lemma-slash-negi-even-weight.md)
- [theta-transform-S-T](lemma-theta-transform-s-t.md)
- [Gamma-2-generators](../part-01/lemma-gamma-2-generators.md)

## Proof

By [Lemma Gamma-2-generators](../part-01/lemma-gamma-2-generators.md) and [Lemma slash-operator-chain-rule](../part-01/lemma-slash-operator-chain-rule.md), it suffices to show that the $H_i$ are invariant under slash actions with respect to $\alpha$, $\beta$, and $-I$. Invariance under $-I$ follows from Lemma [slash-negI-even-weight](../part-01/lemma-slash-negi-even-weight.md). The rest follows from Lemma [slash-operator-chain-rule](../part-01/lemma-slash-operator-chain-rule.md), [theta-transform-S-T](lemma-theta-transform-s-t.md), and the matrix identities

$$
\alpha = T^2, \quad \beta = -S\alpha^{-1}S = -ST^{-2}S.\qquad\text{(21)}
$$

For example, invariance for $H_2$ can be proved by

$$
\begin{aligned}
H_2|\alpha &= H_2 |T^{2} = -H_2 |T = H_2 \\
H_2|\beta &= H_2 |(-S\alpha^{-1}S) = H_2 | (S\alpha^{-1}S) =-H_4 |(\alpha^{-1}S) = -H_4 |S  = H_2.
\end{aligned}
$$

## Lean

Formalized as [`H₂_SIF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₂_SIF), [`H₃_SIF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₃_SIF), [`H₄_SIF`](https://thefundamentaltheor3m.github.io/Sphere-Packing-Lean/docs/find/#doc/H₄_SIF).

## Sources

- [Sphere packing in dimension 8 blueprint: subsections/modular-forms.tex, line 407](https://github.com/thefundamentaltheor3m/Sphere-Packing-Lean/blob/efe3bbbc1ece548f4672a772b94d8f621c10fdda/blueprint/src/subsections/modular-forms.tex#L407)
