---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.leftVNHom, MIPRE.Repetition.rightVNHom, MIPRE.Repetition.isDyadicPair_stdModel, MIPRE.Repetition.hasDyadicUnits_tensorStep, MIPRE.Repetition.isDyadicPair_stdModel_tensorStep, MIPRE.Repetition.inclLeft, MIPRE.Repetition.τ_inclLeft, MIPRE.Repetition.isPosElem_map, MIPRE.Repetition.amplify, MIPRE.Repetition.amplify_correlation, MIPRE.Repetition.isDyadicPair_stdModel_amplify, MIPRE.Repetition.exists_tracialStrategy_isDyadicPair
statement: formalized
proof: formalized
---

# Amplification by an algebra with dyadic matrix units

Let ${\mathscr{A}}$ and $\mathcal{B}$ be tracial algebras in standard form, and suppose that $\mathcal{B}$ has unital dyadic matrix units (Definition [Unital dyadic matrix units](def-dyadic-units.md)).

- (A) For every vector $\psi$, the standard-form model of ${\mathscr{A}} \otimes \mathcal{B}$ — the commutant $\mathcal{N}$ of its right action and the commutant $\mathcal{N}'$ of $\mathcal{N}$, as the players' algebras, in the state $\psi$ — is a dyadic pair (Definition [Dyadic pairs](def-dyadic-pair.md)).
- (T) A tracial strategy $(\sigma, E, F)$ in ${\mathscr{A}}$ gives the tracial strategy $(\sigma \otimes 1, E \otimes 1, F \otimes 1)$ in ${\mathscr{A}} \otimes \mathcal{B}$, with the same correlation.

Consequently, for every game with nonempty alphabets and every $\lambda < {\omega^{\mathrm{co}}}$, there is a tracial strategy of winning probability greater than $\lambda$ whose standard-form model is a dyadic pair in every state.

## Depends on

- [Dyadic pairs](def-dyadic-pair.md)
- [Transport of dyadic matrix units](lem-dyadic-units-closure.md)

## Proof

For (A): the elements $1 \otimes f_{ij}$, for units $f$ of $\mathcal{B}$, are unital dyadic matrix units of ${\mathscr{A}} \otimes \mathcal{B}$, the image of those of $\mathcal{B}$ under the unital $*$-homomorphism $b \mapsto 1 \otimes b$. The left action maps ${\mathscr{A}} \otimes \mathcal{B}$ into $\mathcal{N}$, and the right action maps its opposite algebra into $\mathcal{N}'$, both as unital $*$-homomorphisms, so both players' algebras have units (Lemma [Transport of dyadic matrix units](lem-dyadic-units-closure.md)). The model is a finite pair: the trace vector is tracial on $\mathcal{N}$ and, through the conjugation $J$ of the standard form, on $\mathcal{N}'$, and it separates both, being cyclic for the left and for the right actions. So it is a dyadic pair, and so are its ancilla extensions with nonempty registers, which is how Lemma [${\omega^{\mathrm{co}}}$ is approached in dyadic pairs](lem-co-value-finite-pair.md) uses it (Lemma [Dyadic pairs are closed under ancilla extensions](lem-dyadic-pair-closure.md)). For (T): $a \mapsto a \otimes 1$ is a unital $*$-homomorphism, so it maps sums of squares to sums of squares and keeps the measurements' sums equal to $1$, and the trace of ${\mathscr{A}} \otimes \mathcal{B}$ restricts to that of ${\mathscr{A}}$ on ${\mathscr{A}} \otimes 1$, since $\tau(a \otimes b) = \tau(a) \tau(b)$ and $\tau(1) = 1$; so the normalization of the density and the correlation $\mathrm{Re}\, \tau(\sigma^* E^x_a \sigma F^y_b)$ are unchanged. The consequence is the vendored strict form of Lin's tracial density for game values (Theorem [Lin's tracial density theorem](../../parallel-repetition/thm-tracial-density.md)), followed by (T) and (A). The full proof is `reports/c6b-paper-proofs.md`, Section 3, Theorems A and T (Lemmas 8 and 9).

## Lean

Formalized as [`MIPRE.Repetition.leftVNHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.leftVNHom), [`MIPRE.Repetition.rightVNHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.rightVNHom), [`MIPRE.Repetition.isDyadicPair_stdModel`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.isDyadicPair_stdModel), [`MIPRE.Repetition.hasDyadicUnits_tensorStep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.hasDyadicUnits_tensorStep), [`MIPRE.Repetition.isDyadicPair_stdModel_tensorStep`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.isDyadicPair_stdModel_tensorStep), [`MIPRE.Repetition.inclLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.inclLeft), [`MIPRE.Repetition.τ_inclLeft`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.τ_inclLeft), [`MIPRE.Repetition.isPosElem_map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.isPosElem_map), [`MIPRE.Repetition.amplify`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.amplify), [`MIPRE.Repetition.amplify_correlation`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.amplify_correlation), [`MIPRE.Repetition.isDyadicPair_stdModel_amplify`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.isDyadicPair_stdModel_amplify), [`MIPRE.Repetition.exists_tracialStrategy_isDyadicPair`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.exists_tracialStrategy_isDyadicPair).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 3031](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L3031)
