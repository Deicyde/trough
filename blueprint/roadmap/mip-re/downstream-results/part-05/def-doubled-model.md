---
declaration: definition
origin: cited
lean: MIPRE.LIDT.Co.Doubling.LocA, MIPRE.LIDT.Co.Doubling.LocB, MIPRE.LIDT.Co.Doubling.Loc, MIPRE.LIDT.Co.Doubling.model, MIPRE.LIDT.Co.Doubling.model_L, MIPRE.LIDT.Co.Doubling.model_R, MIPRE.LIDT.Co.Doubling.equiv
statement: formalized
---

# The doubled model

Let $M$ be a finite pair in a unit state $\psi$, with commutants $\mathcal{A}_c$ and $\mathcal{B}_c$ as in Lemma [The players' algebras of a finite pair, as commutants with their order](lem-finite-pair-order.md). Its *doubled model* $D(M)$ is the following symmetric model (Definition [Symmetric models](def-sym-model.md)). Its local algebra is the C$^*$-algebra $\mathcal{P} = \mathcal{A}_c \times \mathcal{B}_c$, with componentwise operations and order, and its space is $K = \mathcal{H} \oplus \mathcal{H}$. The state is $\Psi = (\psi, \psi)/\sqrt{2}$, the first placement is $L(a, b) = a \oplus b$, and the flip is $J(\xi, \eta) = (\eta, \xi)$. The second placement is then $R(a, b) = b \oplus a$, and $L(x)$ commutes with $R(y)$ because $\mathcal{A}_c$ commutes with $\mathcal{B}_c$.

By Lemma [The players' algebras of a finite pair, as commutants with their order](lem-finite-pair-order.md), $\mathcal{P}$ is $*$-isomorphic to $\mathcal{A} \times \mathcal{B}$, the product of the players' algebras, which is how `reports/c6b-paper-proofs.md` writes the doubled model's local algebra. The model is built over the commutants because a symmetric model needs a C$^*$-algebra, and $\mathcal{A}$ and $\mathcal{B}$ need not be C$^*$-algebras.

## Depends on

- [Symmetric models](def-sym-model.md)
- [The players' algebras of a finite pair, as commutants with their order](lem-finite-pair-order.md)

## Lean

Formalized as [`MIPRE.LIDT.Co.Doubling.LocA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.LocA), [`MIPRE.LIDT.Co.Doubling.LocB`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.LocB), [`MIPRE.LIDT.Co.Doubling.Loc`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.Loc), [`MIPRE.LIDT.Co.Doubling.model`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.model), [`MIPRE.LIDT.Co.Doubling.model_L`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.model_L), [`MIPRE.LIDT.Co.Doubling.model_R`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.model_R), [`MIPRE.LIDT.Co.Doubling.equiv`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.LIDT.Co.Doubling.equiv).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3375](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3375)
