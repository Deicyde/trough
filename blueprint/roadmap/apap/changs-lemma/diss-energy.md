---
declaration: lemma
origin: cited
lean: AddDissociated.boringEnergy_le
statement: formalized
proof: formalized
---

# diss_energy

If $A\subseteq G$ is dissociated then $E_{2m}(A) \le (32e m \left\lvert A\right\rvert)^m$.

## Depends on

- [Dissociation](dissociated.md)
- [Energy](energy.md)

## Proof depends on

- [energy_alt](energy-alt.md)
- [Rudin's inequality](rudin.md)

## Proof

By Lemma [energy_alt](energy-alt.md) and Lemma [Rudin's inequality](rudin.md)

$$
\begin{aligned}
E_{2m}(A)
& =
\mathop{
\mathchoice{\vcenter{\hbox{\larger[4]$\mathbb{E}$}}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
{\kern0pt\mathbb{E}}
}\displaylimits
_\gamma \left\lvert \hat 1_A(\gamma)\right\rvert^{2m} \\
& = \lVert \hat 1_A\rVert_{2m}^{2m} \\
& \le (4\sqrt{2em})^{2m} \lVert \hat 1_A\rVert_2^{2m} \\
& = (32em)^m \lVert 1_A\rVert_2^{2m} \\
& = (32em)^m \left\lvert A\right\rvert^m
\end{aligned}
$$

## Lean

Formalized as [`AddDissociated.boringEnergy_le`](https://yaeldillies.github.io/apap/docs/find/#doc/AddDissociated.boringEnergy_le).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 166](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L166)
