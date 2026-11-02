---
declaration: lemma
origin: cited
lean: WeakPNT_character
statement: formalized
proof: formalized
---

# WeakPNT-character

If $q ≥ 1$ and $a$ is coprime to $q$, and $\mathrm{Re} s > 1$, we have

$$
\sum_{n: n = a\ (q)} \frac{\Lambda(n)}{n^s} = - \frac{1}{\varphi(q)} \sum_{\chi\ (q)}
\overline{\chi(a)} \frac{L'(s,\chi)}{L(s,\chi)}.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

From the Fourier inversion formula on the multiplicative group $(\mathbb{Z}/q\mathbb{Z})^\times$, we have

$$
1_{n=a\ (q)} = \frac{\varphi(q)}{q} \sum_{\chi\ (q)} \overline{\chi(a)} \chi(n).
$$

On the other hand, from standard facts about L-series we have for each character $\chi$ that

$$
\sum_{n} \frac{\Lambda(n) \chi(n)}{n^s} = - \frac{L'(s,\chi)}{L(s,\chi)}.
$$

Combining these two facts, we obtain the claim.

## Lean

Formalized as [`WeakPNT_character`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/WeakPNT_character).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
