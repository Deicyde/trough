---
declaration: lemma
origin: cited
lean: MIPRE.Repetition.Pauli.pauliA, MIPRE.Repetition.Pauli.pauliTrace, MIPRE.Repetition.Pauli.pauliStd, MIPRE.Repetition.Pauli.pauliSites, MIPRE.Repetition.Pauli.pauliStd_hasDyadicUnits
statement: formalized
proof: formalized
---

# The twisted Pauli algebra

Let $\Lambda$ be the set of finitely supported sequences $g = (x(g)_k, z(g)_k)_{k \in \mathbb{N}}$ of pairs of bits, and $\omega(g, h) = (-1)^{\sum_k z(g)_k x(h)_k}$. On $\ell^2(\Lambda)$ the unitaries $W_g \delta_h = \omega(g, h)\, \delta_{g + h}$ satisfy $W_g W_h = \omega(g, h)\, W_{g + h}$ and $W_g^* = \omega(g, g)\, W_g$, so their linear span $\mathcal{P}$ is a $*$-algebra. With the trace $\tau(a) = \langle \delta_0, a \delta_0 \rangle$, the map $a \mapsto a \delta_0$, the inclusion as the left action and $a^{\mathrm{op}} \mapsto J a^* J$ as the right action, for the antiunitary $(J \xi)_k = \omega(k, k)\, \overline{\xi_k}$, it is a tracial algebra in standard form, in the sense of the vendored commuting-operator development used for Theorem [Lin's tracial density theorem](../../parallel-repetition/thm-tracial-density.md); and $\mathcal{P}$ itself has unital dyadic matrix units (Definition [Unital dyadic matrix units](def-dyadic-units.md)).

## Depends on

- [Pauli sites give dyadic matrix units](lem-pauli-sites-units.md)

## Proof

$\tau(W_g) = 1$ if $g = 0$ and $0$ otherwise, so $\tau(W_g W_h)$ and $\tau(W_h W_g)$ both vanish unless $h = g$, where the two products agree: $\tau$ is tracial on a spanning set, hence on $\mathcal{P}$. The vectors $W_g \delta_0 = \delta_g$ span a dense subspace. $J$ is an involutive antiunitary with $J(a \delta_0) = a^* \delta_0$, from which the formula for the right action and its commutation with the left action follow on that dense subspace. Finally $X_k = W_g$ for $g$ the pair $(1, 0)$ at site $k$, and $Z_k = W_g$ for $(0, 1)$ at site $k$, are self-adjoint symmetries that anticommute at one site and commute at distinct sites, by the values of $\omega$; so Lemma [Pauli sites give dyadic matrix units](lem-pauli-sites-units.md) gives units in $\mathcal{P}$ itself, not only after representation. No closure is taken: the interface asks only for a $*$-algebra. The candidates and the choice are in `reports/c6b-paper-proofs.md`, Section 3.8.

## Lean

Formalized as [`MIPRE.Repetition.Pauli.pauliA`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.Pauli.pauliA), [`MIPRE.Repetition.Pauli.pauliTrace`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.Pauli.pauliTrace), [`MIPRE.Repetition.Pauli.pauliStd`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.Pauli.pauliStd), [`MIPRE.Repetition.Pauli.pauliSites`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.Pauli.pauliSites), [`MIPRE.Repetition.Pauli.pauliStd_hasDyadicUnits`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Repetition.Pauli.pauliStd_hasDyadicUnits).

## Sources

- [MIP* = RE blueprint: content/08_downstream.tex, line 2999](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/08_downstream.tex#L2999)
