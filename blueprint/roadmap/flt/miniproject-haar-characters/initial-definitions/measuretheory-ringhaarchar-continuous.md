---
declaration: corollary
origin: cited
lean: MeasureTheory.ringHaarChar_continuous
statement: formalized
proof: formalized
discussion: https://github.com/ImperialCollegeLondon/FLT/issues/516
---

# MeasureTheory.ringHaarChar_continuous

The function $\delta_R:R^\times\to\mathbb{R}_{>0}$ is continuous.

## Depends on

- [MeasureTheory.ringHaarChar](measuretheory-ringhaarchar.md)

## Proof depends on

- [MeasureTheory.ringHaarChar_mul_integral](measuretheory-ringhaarchar-mul-integral.md)

## Proof

Fix a Haar measure $\mu$ on $R$ and a continuous real-valued function $f$ on $R$ with compact support and such that $\int f(x) d\mu(x)\not=0$. Then $r \mapsto \int f(rx) d\mu(x)$ is a continuous function from $R\to\mathbb{R}$ (because a continuous function with compact support is uniformly continuous) and thus gives a continuous function $R^\times\to\mathbb{R}$. Thus the function $u\mapsto (\int f(ux) d\mu(x))/(\int f(x)d\mu(x))$ is a continuous function from $R^\times$ to $\mathbb{R}$ taking values in $\mathbb{R}_{>0}$. Hence $\delta_R^{-1}$ is continuous, from lemma [MeasureTheory.ringHaarChar_mul_integral](measuretheory-ringhaarchar-mul-integral.md), and thus $\delta_R$ is too.

## Lean

Formalized as [`MeasureTheory.ringHaarChar_continuous`](https://ImperialCollegeLondon.github.io/FLT/docs/find/#doc/MeasureTheory.ringHaarChar_continuous).

## Sources

- [Fermat's Last Theorem (Imperial) blueprint: chapter/HaarCharacterProject.tex, line 250](https://github.com/ImperialCollegeLondon/FLT/blob/a3210204ad8876e851e32f73dd97d882bf1ccd0a/blueprint/src/chapter/HaarCharacterProject.tex#L250)
