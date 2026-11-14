---
declaration: definition
origin: cited
lean: MIPRE.Tailored.SignedPerm, MIPRE.Tailored.SignedPerm.toMatrix, MIPRE.Tailored.SignedPerm.toMatrixHom, MIPRE.Tailored.SignedPerm.negOne, MIPRE.Tailored.SignedPerm.diag, MIPRE.Tailored.SignedPerm.prod, MIPRE.Tailored.SignedPerm.map, MIPRE.Tailored.signedPermMatrix, MIPRE.Tailored.IsSignedPerm
statement: formalized
---

# Signed permutations; II:1008–1069

A *signed permutation* of a finite set $\Omega$ is a permutation $\sigma$ of $\Omega$ with a sign $(-1)^{s(j)}$ at each point: the permutation $\pm j \mapsto \pm (-1)^{s(j)} \sigma(j)$ of the signed set $\Omega_\pm = \{\pm\} \times \Omega$, which commutes with the sign flip. They form a group, the semidirect product of $\mathrm{Sym}(\Omega)$ and $\mathbb{F}_2^\Omega$ (II:1057), which contains the sign flip $-{I}$, the $\pm 1$ diagonals, and, for two sets, the products $g \times h$ acting on $(\Omega \times \Omega')_\pm$ (II:3062). The *matrix* of a signed permutation is that of its action on the anti-symmetric functions in the basis $B^-$ (II:1049), the *signed permutation matrix* $e_j \mapsto (-1)^{s(j)} e_{\sigma(j)}$.

## Depends on

- [The three forms of a measurement with outcomes in $\mathbb{F}_2^k$; II:972–1006](def-fourier-forms.md)

## Lean

Formalized as [`MIPRE.Tailored.SignedPerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm), [`MIPRE.Tailored.SignedPerm.toMatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrix), [`MIPRE.Tailored.SignedPerm.toMatrixHom`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.toMatrixHom), [`MIPRE.Tailored.SignedPerm.negOne`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.negOne), [`MIPRE.Tailored.SignedPerm.diag`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.diag), [`MIPRE.Tailored.SignedPerm.prod`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.prod), [`MIPRE.Tailored.SignedPerm.map`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.SignedPerm.map), [`MIPRE.Tailored.signedPermMatrix`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.signedPermMatrix), [`MIPRE.Tailored.IsSignedPerm`](https://vidick.github.io/MIPRE-formalization/docs/find/#doc/MIPRE.Tailored.IsSignedPerm).

## Sources

- [MIP* = RE blueprint: content/09_tailored.tex, line 85](https://github.com/vidick/MIPRE-formalization/blob/5926bdff5db621f44682a101007ef2fe3ae8d970/blueprint/src/content/09_tailored.tex#L85)
