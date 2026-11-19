---
declaration: definition
origin: cited
lean: BohrSet
statement: formalized
---

# Bohr sets

Let $\nu: \widehat{G} \to \mathbb{R}$. The corresponding Bohr set is defined to be

$$
\mathrm{Bohr}(\nu)=\left\{ x\in G : \left\lvert 1-\gamma(x)\right\rvert\leq \nu(\gamma)\textrm{ for all }\gamma\in\Gamma\right\}.
$$

The rank of $\nu$, denoted by $\mathrm{rk}(\nu)$, is defined to be the size of the set of those $\gamma\in\widehat{G}$ such that $\nu(\gamma)<2$.

(Basic API facts: Bohr sets are symmetric and contain $0$. Also that, without loss of generality, we can assume $\nu$ takes only values in $\mathbb{R}_{\geq 0}$ - I think it might be easier to have the definition allow arbitrary real values, and then switch to non-negative only in proofs where convenient. Or could have the definition only allow non-negative valued functions in the first place.)

## Depends on

Its statement uses no other node of the blueprint.

## Lean

Formalized as [`BohrSet`](https://yaeldillies.github.io/apap/docs/find/#doc/BohrSet).

## Sources

- [Kelley-Meka bound blueprint: chapter/bohr.tex, line 3](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/bohr.tex#L3)
