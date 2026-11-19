---
declaration: theorem
origin: cited
lean: chang
statement: formalized
proof: formalized
---

# Chang's lemma

Let $G$ be a finite abelian group and $f:G\to \mathbb{C}$. Let $\eta >0$ and $\alpha=N^{-1}\lVert f\rVert_1^2/\lVert f\rVert_2^2$. There exists some $\Delta\subseteq \Delta_\eta(f)$ such that

$$
\left\lvert \Delta\right\rvert\le \lceil e\mathcal{L}(\alpha)\eta^{-2}\rceil
$$

and

$$
\Delta_\eta(f)\subseteq \left\{ \sum_{\gamma\in\Delta}c_\gamma \gamma : c_\gamma\in \{-1,0,1\} \right\}.
$$

## Depends on

- [Large spectrum](large-spec.md)

## Proof depends on

- [diss_energy](diss-energy.md)
- [diss_span](diss-span.md)
- [spec_hoelder](spec-hoelder.md)

## Proof

By Lemma [diss_span](diss-span.md) it suffices to show that $\Delta_\eta(f)$ contains no dissociated set with at least

$$
K= \lceil e\mathcal{L}(\alpha)\eta^{-2}\rceil+1
$$

many elements. Suppose not, and let $\Delta\subseteq \Delta_\eta(f)$ be a dissociated set of size $K$. Then by Lemma [diss_energy](diss-energy.md) we have, for any $m\geq 1$,

$$
E_{2m}(\Delta)\le m!K^m.
$$

On the other hand, by Lemma [spec_hoelder](spec-hoelder.md),

$$
\eta^{2m}\alpha K^{2m}\le E_{2m}(\Delta).
$$

Rearranging these bounds, we have

$$
K^m \le m! \alpha^{-1}\eta^{-2m}\le m^m\alpha^{-1}\eta^{-2m}.
$$

Therefore $K\le \alpha^{-1/m}m\eta^{-2}$. This is a contradiction to the choice of $K$ if we choose $m=\mathcal{L}(\alpha)$, since $\alpha^{-1/m}\le e$.

## Lean

Formalized as [`chang`](https://yaeldillies.github.io/apap/docs/find/#doc/chang).

## Sources

- [Kelley-Meka bound blueprint: chapter/chang.tex, line 213](https://github.com/YaelDillies/apap/blob/5b8cc8c5483512ee077ffa5a8bafc0a1a4c09f86/blueprint/src/chapter/chang.tex#L213)
